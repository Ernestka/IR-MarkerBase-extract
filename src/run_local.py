"""
Run the pipeline on a LOCAL folder of PDFs — no Google Drive, no GitHub Actions.
Use it for the gold-standard set and for trying prompts/models.

    python src/run_local.py papers/                 # eligibility + extraction
    python src/run_local.py papers/ --only eligibility
    python src/run_local.py papers/one_paper.pdf --model pro
    python src/run_local.py papers/ --skip-eligibility   # extract everything

Supplements (optional): put them in  <pdf folder>/supplements/<pdf name without .pdf>/

Outputs go to --out (default: local_output/, git-ignored):
    roster.csv, eligibility/<id>.json, extracted/<id>/..., final/ir_extraction.{csv,xlsx}
Papers already done in that roster are skipped unless --redo is given.

Needs GEMINI_API_KEY (or the key for whichever provider --model uses).
"""
import argparse
import sys
from datetime import date
from pathlib import Path

import eligibility as agent
import export
import llm
import run_extraction
import store
import supplements


def _supplement_parts(pdf):
    folder = pdf.parent / "supplements" / pdf.stem
    if not folder.is_dir():
        return None
    files = [{"name": f.name, "bytes": f.read_bytes()} for f in sorted(folder.iterdir()) if f.is_file()]
    parts, summary = supplements.load(files)
    print(f"    supplement: {summary}")
    return parts


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="a PDF or a folder of PDFs")
    ap.add_argument("--out", default="local_output")
    ap.add_argument("--model", default="flash", help="model spec for both stages (see llm.py)")
    ap.add_argument("--extract-model", help="model for extraction (default: flash-extract, or --model if given)")
    ap.add_argument("--only", choices=["eligibility", "extraction"])
    ap.add_argument("--skip-eligibility", action="store_true",
                    help="treat every paper as eligible (e.g. a hand-picked gold set)")
    ap.add_argument("--redo", action="store_true", help="re-run papers already in the roster")
    args = ap.parse_args()

    src = Path(args.path)
    pdfs = [src] if src.is_file() else sorted(src.glob("*.pdf")) + sorted(src.glob("*.PDF"))
    if not pdfs:
        sys.exit(f"No PDFs found at {src}")

    out = Path(args.out)
    roster_path, elig_dir, ext_dir = out / "roster.csv", out / "eligibility", out / "extracted"
    out.mkdir(parents=True, exist_ok=True)
    roster = store.load_roster(roster_path)
    emodel = args.extract_model or (args.model if args.model != "flash" else "flash-extract")

    try:
        _run(pdfs, args, roster, roster_path, elig_dir, ext_dir, emodel)
    except llm.AllModelsFailed as e:
        print(f"\n! Stopped: {e}\nProgress so far is saved; re-run later to continue.")
    store.save_roster(roster_path, roster)
    if args.only != "eligibility":
        print(f"\nFinal table: {export.build(ext_dir, out / 'final')}")
    print(f"Roster: {roster_path}")


def _run(pdfs, args, roster, roster_path, elig_dir, ext_dir, emodel):
    for pdf in pdfs:
        rid = store.stem(pdf.name)
        row = roster.get(rid) or {"id": rid, "source": "local", "first_seen": date.today().isoformat()}
        print(f"\n== {rid}")
        data = pdf.read_bytes()
        supp = _supplement_parts(pdf)

        # --- Stage 1
        if args.only != "extraction" and not args.skip_eligibility and (
                args.redo or not row.get("status")):
            res = agent.assess_pdf_bytes(data, model=args.model, supplement_parts=supp)
            a = res.parsed
            row.update(last_assessed=date.today().isoformat(), spec_version=agent.SPEC_VERSION,
                       elig_model=res.model_id, elig_tok_in=res.tok_in, elig_tok_out=res.tok_out)
            if a is None:
                row.update(status=store.INELIGIBLE, notes=f"no structured result: {res.error[:120]}")
            else:
                agent.print_assessment(a)
                store.save_assessment(elig_dir, rid, {"id": rid, "model": res.model_id,
                                                      "spec_version": agent.SPEC_VERSION,
                                                      "assessed": date.today().isoformat(),
                                                      "assessment": a.model_dump(mode="json")})
                row.update(eligible=a.eligible, confidence=a.confidence.value,
                           duplicate_risk=a.duplicate_risk.level.value,
                           needs_supplement=a.supplement.needed,
                           status=store.ELIGIBLE if a.eligible else store.INELIGIBLE)
            roster[rid] = row
            store.save_roster(roster_path, roster)
        if args.skip_eligibility and row.get("status") in (None, "", store.INELIGIBLE):
            row["status"] = store.ELIGIBLE
            roster[rid] = row

        # --- Stage 2
        if args.only == "eligibility":
            continue
        if row.get("status") == store.ELIGIBLE or (args.redo and row.get("status") in (
                store.EXTRACTED, store.EXTRACTION_FAILED)):
            elig = (store.load_assessment(elig_dir, rid) or {}).get("assessment", {})
            run_extraction.extract_one(rid, data, supp, elig, roster, model=emodel,
                                       extracted_dir=ext_dir)
            store.save_roster(roster_path, roster)
        else:
            print(f"  (skipping extraction: status {row.get('status')})")


if __name__ == "__main__":
    main()
