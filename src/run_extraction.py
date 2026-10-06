"""
Stage 2 — the extraction driver. Run on demand by
.github/workflows/pipeline.yml (after eligibility, every 4 h or on demand).

For each ELIGIBLE paper in the roster (capped per run):
  1. Fetch the PDF (+ supplements) from Drive.
  2. Ask the extractor for study/survey/genotype/bioassay/geno_pheno data.
  3. Validate it in Python (validate.py).
  4. If it fails, feed the errors back to the model and retry — up to MAX_REPAIRS.
  5. On success: write data/extracted/<id>/{study.yaml, surveys.csv, genotypes.csv,
     bioassays.csv, geno_pheno.csv, README.md}, set status EXTRACTED, and rebuild
     the combined table data/final/ (export.py). On repeated failure: set
     EXTRACTION_FAILED (surfaced in the weekly digest) and record the errors.

Env:
  GOOGLE_APPLICATION_CREDENTIALS, DRIVE_FOLDER_ID, DRIVE_SUPPLEMENT_FOLDER_ID,
  GEMINI_API_KEY (or the key for whichever provider EXTRACT_MODEL uses),
  EXTRACT_MODEL (default flash-extract — see llm.py), EXTRACT_MAX_PER_RUN (default 10),
  EXTRACT_MAX_REPAIRS (default 3).
"""
import os
import sys
from datetime import date
from pathlib import Path

import drive
import enrich
import extraction
import llm
import store
import supplements
import validate

ROOT = Path(__file__).resolve().parent
DATA = ROOT.parent / "data"
ROSTER = DATA / "roster.csv"
ELIG = DATA / "eligibility"
EXTRACTED = DATA / "extracted"

MODEL = os.environ.get("EXTRACT_MODEL") or "flash-extract"
MAX_PER_RUN = int(os.environ.get("EXTRACT_MAX_PER_RUN") or "10")
MAX_REPAIRS = int(os.environ.get("EXTRACT_MAX_REPAIRS") or "3")


def today():
    return date.today().isoformat()


def _set(roster, rid, status, notes, model=None, tok_in=0, tok_out=0):
    row = roster.get(rid) or {"id": rid}
    row["status"] = status
    row["notes"] = notes
    if model is not None:
        row["extract_model"] = model
        row["extract_tok_in"] = tok_in
        row["extract_tok_out"] = tok_out
    roster[rid] = row


def extract_one(rid, pdf, supp_parts, elig_ctx, roster, model=None, extracted_dir=EXTRACTED):
    """Extract + validate-repair loop for a single paper. Returns True on success."""
    model = model or MODEL
    sid = extraction.study_id(rid)
    out_dir = Path(extracted_dir) / sid
    repair, last_err, tok_in, tok_out, model_id = None, "", 0, 0, ""
    for attempt in range(1, MAX_REPAIRS + 2):      # first try + MAX_REPAIRS repairs
        try:
            res = extraction.extract(pdf, sid, model=model, supplement_parts=supp_parts,
                                     eligibility_record=elig_ctx, repair=repair)
        except llm.AllModelsFailed:
            raise                          # out of quota — not this paper's fault
        except Exception as e:
            last_err = f"extractor error: {e}"
            print(f"  ! {rid} attempt {attempt}: {last_err}")
            break
        tok_in += res.tok_in
        tok_out += res.tok_out
        model_id = res.model_id
        ex = res.parsed
        if ex is None:
            last_err = f"no structured output (stop: {res.stop_reason}) {res.error}"
            print(f"  ! {rid} attempt {attempt}: {last_err[:200]}")
            if res.stop_reason == "refusal":
                break
            if res.stop_reason == "max_tokens":
                if repair and repair.get("too_long"):
                    break                  # already asked for a shorter answer once
                repair = {"too_long": True}
            continue

        extraction.keep_printed_only(ex)
        errors, warnings = validate.check(ex)
        if not errors:
            extraction.write_outputs(out_dir, sid, ex, model_id, warnings)
            print(f"    enrich: {enrich.enrich_study(out_dir)}")   # PMID + geocoding, in code
            fail = out_dir / "EXTRACTION_FAILED.md"
            if fail.exists():
                fail.unlink()
            _set(roster, rid, store.EXTRACTED,
                 f"{len(ex.surveys)} survey(s), {len(ex.genotypes)} genotype, "
                 f"{len(ex.bioassays)} bioassay, {len(ex.geno_pheno)} geno-pheno rows"
                 + (f"; {len(warnings)} warning(s)" if warnings else ""),
                 model=model_id, tok_in=tok_in, tok_out=tok_out)
            print(f"  · {rid}: EXTRACTED (attempt {attempt}, {len(warnings)} warning(s))")
            return True

        last_err = validate.format_errors(errors)
        repair = {"error": last_err, "previous": ex.model_dump(mode="json")}
        print(f"  · {rid} attempt {attempt}: {len(errors)} validation error(s) — {errors[0][:140]}")

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "EXTRACTION_FAILED.md").write_text(
        f"# Extraction failed — {rid}\n\n"
        f"Could not produce valid output on {today()} "
        f"(up to {MAX_REPAIRS} repair attempts).\n\n"
        f"Last error(s):\n\n```\n{last_err}\n```\n", encoding="utf-8")
    _set(roster, rid, store.EXTRACTION_FAILED, last_err.replace("\n", " ")[:160],
         model=model_id, tok_in=tok_in, tok_out=tok_out)
    print(f"  ! {rid}: EXTRACTION_FAILED — {last_err[:140]}")
    return False


def main():
    folder_id = os.environ.get("DRIVE_FOLDER_ID", "").strip()
    if not folder_id:
        sys.exit("Set DRIVE_FOLDER_ID.")
    supp_folder_id = os.environ.get("DRIVE_SUPPLEMENT_FOLDER_ID", "").strip()  # optional

    svc = drive.service()
    by_stem = {store.stem(p["name"]): p for p in drive.list_pdfs(svc, folder_id)}

    roster = store.load_roster(ROSTER)
    todo = [rid for rid, row in roster.items() if row.get("status") == store.ELIGIBLE]
    todo = sorted(todo)[:MAX_PER_RUN]
    if not todo:
        print("No ELIGIBLE papers to extract.")
        return

    done = failed = 0
    for rid in todo:
        p = by_stem.get(rid)
        if not p:
            print(f"  ! {rid}: PDF no longer in Drive; skipping")
            continue
        pdf = drive.fetch_bytes(svc, p["id"])
        supp_parts = None
        if supp_folder_id:
            files = drive.fetch_supplement_files(svc, supp_folder_id, rid)
            supp_parts, summary = supplements.load(files)
            if files:
                print(f"    supplement for {rid}: {summary}")
        elig = store.load_assessment(ELIG, rid) or {}
        try:
            ok = extract_one(rid, pdf, supp_parts, elig.get("assessment", {}), roster)
        except llm.AllModelsFailed as e:
            print(f"  ! stopping: {e}")
            break
        if ok:
            done += 1
        else:
            failed += 1

    store.save_roster(ROSTER, roster)
    try:
        import export
        print(f"Final table: {export.build()}")
    except Exception as e:
        print(f"(final table not rebuilt: {e})")
    try:
        import stats
        stats.generate()
    except Exception as e:
        print(f"(stats not updated: {e})")

    print(f"\nExtracted {done}, failed {failed} (of {len(todo)} eligible this run; model {MODEL}).")


if __name__ == "__main__":
    main()
