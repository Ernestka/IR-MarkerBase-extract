"""
Build the FINAL combined table from every data/extracted/<id>/ folder:

    data/final/ir_extraction.csv
    data/final/ir_extraction.xlsx

Long format: one row per data point, with the paper- and survey-level fields
repeated on each row. `Record type` says which kind of row it is:

    genotype    population genotype counts for one marker (bioassay columns NA)
    bioassay    one bioassay (gene/marker columns NA)
    geno_pheno  one bioassay x marker, with RR/RS/SS split into survivors vs dead
    no_data     a paper that was extracted but yielded no records (all NA)

Empty values are written as NA. Every DERIVED value (allele and genotype
frequencies, mortality/survival, WHO phenotype, pyrethroid subtype, collection
year, temporal precision) is computed here from raw counts — never by the LLM.
Bioassay dead/alive counts are derived from a reported % x n only when that
gives a unique whole number, and the row says so in `Data quality flag`.

Run standalone:  python src/export.py
"""
import csv
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
EXTRACTED = ROOT / "data" / "extracted"
FINAL = ROOT / "data" / "final"
NA = "NA"

COLUMNS = [
    "Paper/Study ID", "Record type", "Survey ID", "DOI", "PMID", "Publication year", "Country",
    "Data source", "Evidence location (data source)",
    "Species reported", "Species complex/group", "Molecular species",
    "Country (site)", "Sampling site", "Admin level 1", "Admin level 2", "Latitude", "Longitude",
    "Coordinates reported or inferred", "Evidence location (coordinates)",
    "Spatial precision / uncertainty",
    "Collection start date", "Collection end date", "Collection year", "Temporal precision",
    "Mosquito collection method", "Mosquito life stage", "Wild/laboratory population",
    "Generation", "Total sample size",
    "Insecticide name", "Pyrethroid subtype", "Insecticide concentration", "Exposure duration",
    "Assay method", "Assay type", "Synergist used", "Number exposed", "Number surviving",
    "Number dead", "Survival proportion", "Mortality proportion", "Phenotype",
    "Mortality assessment time",
    "Gene", "Variant/marker", "Amino-acid change", "Nucleotide change", "Resistant allele",
    "Genotyping method", "Number genotyped", "Resistant allele count", "Allele frequency",
    "Homozygous resistant (RR)", "Heterozygous (RS)", "Homozygous susceptible (SS)",
    "RR frequency", "RS frequency", "SS frequency",
    "Phenotype group", "VGSC variant in survivors", "VGSC variant in dead mosquitoes",
    "RR survivors", "RS survivors", "SS survivors", "RR dead", "RS dead", "SS dead",
    "Coordinates verified", "Species identification method", "Sample size reported",
    "Raw counts available", "AI extraction confidence", "Human verified",
    "Source sentence/table", "Page number", "Figure number", "Supplementary material",
    # Not in the original column list: anything a human should check before trusting the row
    # (numbers inconsistent in the paper, counts derived in code, pooled tests).
    "Data quality flag",
]

PYRETHROIDS = {
    "type I": {"permethrin", "bifenthrin", "etofenprox", "resmethrin", "phenothrin",
               "d-phenothrin", "tetramethrin", "transfluthrin", "allethrin"},
    "type II": {"deltamethrin", "alpha-cypermethrin", "alphacypermethrin", "cypermethrin",
                "lambda-cyhalothrin", "lambdacyhalothrin", "cyfluthrin", "beta-cyfluthrin",
                "fenvalerate", "esfenvalerate", "cyphenothrin", "zeta-cypermethrin"},
}


# --- Helpers ----------------------------------------------------------------

def _read_csv(path):
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _num(v):
    try:
        x = float(v)
        return int(x) if x.is_integer() else x
    except (TypeError, ValueError):
        return None


def _ratio(a, b, nd=4):
    a, b = _num(a), _num(b)
    return round(a / b, nd) if a is not None and b else None


def _loc(prov):
    """'p. 5; Table 2; Fig 3; Suppl S1' from a provenance dict (prefix-free keys)."""
    bits = []
    if prov.get("page"):
        bits.append(f"p. {prov['page']}")
    for k in ("table", "figure", "supplement"):
        if prov.get(k):
            bits.append(str(prov[k]))
    return "; ".join(bits) or None


def pyrethroid_subtype(insecticide, klass):
    name = (insecticide or "").strip().lower()
    for sub, names in PYRETHROIDS.items():
        if name in names:
            return sub
    if klass and "pyrethroid" not in klass.lower():
        return "not a pyrethroid"
    return None


def who_phenotype(mortality, assay_type, synergist):
    """WHO (2016/2022) interpretation of diagnostic-dose mortality."""
    if mortality is None or synergist:
        return None
    t = (assay_type or "").lower()
    if any(w in t for w in ("intensity", "5x", "10x", "5 x", "10 x", "synergist")):
        return None   # WHO thresholds apply to the diagnostic (susceptibility) dose only
    if mortality >= 0.98:
        return "susceptible"
    if mortality >= 0.90:
        return "possible resistance"
    return "confirmed resistance"


def collection_year(start, end):
    ys, ye = (start or "")[:4], (end or "")[:4]
    if ys and ye and ys != ye:
        return f"{ys}-{ye}"
    return ys or ye or None


def temporal_precision(start, end):
    if not start and not end:
        return "unknown"
    s, e = start or end, end or start
    if s[:4] != e[:4]:
        return "multi-year"
    if len(s) == 10 and s == e:
        return "day"
    if len(s) >= 7 and s[:7] == e[:7]:
        return "month"
    if len(s) >= 7 and len(e) >= 7:
        return "months within year"
    return "year"


def _geno_freqs(rr, rs, ss):
    rr, rs, ss = _num(rr), _num(rs), _num(ss)
    if None in (rr, rs, ss) or rr + rs + ss == 0:
        return {}
    n = rr + rs + ss
    return {"Allele frequency": round((2 * rr + rs) / (2 * n), 4),
            "RR frequency": round(rr / n, 4), "RS frequency": round(rs / n, 4),
            "SS frequency": round(ss / n, 4), "_n": n}


def _prov_cols(r):
    p = {k: r.get(k) for k in ("source_text", "page", "table", "figure", "supplement")}
    src = p["source_text"]
    if p["table"]:
        src = f"{p['table']}: {src}" if src else p["table"]
    return {"Source sentence/table": src, "Page number": p["page"],
            "Figure number": p["figure"], "Supplementary material": p["supplement"]}


# --- Row builders -------------------------------------------------------------

def _study_cols(rid, study):
    prov = study.get("provenance") or {}
    return {
        "Paper/Study ID": rid, "DOI": study.get("doi"), "PMID": study.get("pmid"),   # PMID: enrich.py
        "Publication year": study.get("publication_year"),
        "Country": "; ".join(study.get("countries") or []) or None,
        "Data source": study.get("data_source"),
        "Evidence location (data source)": _loc(prov),
        "AI extraction confidence": study.get("confidence"),
        "Human verified": "FALSE",
    }


def _survey_cols(s):
    if not s:
        return {}
    lat, lon = _num(s.get("latitude_reported")), _num(s.get("longitude_reported"))
    coord_prov = {k: s.get(f"coord_{k}") for k in ("page", "table", "figure", "supplement")}
    coord_how = "reported" if lat is not None else None
    coord_where = _loc(coord_prov) or s.get("coord_source_text")
    precision = s.get("spatial_precision")
    if lat is None and _num(s.get("latitude_geocoded")) is not None:   # enrich.py, never the LLM
        lat, lon = _num(s.get("latitude_geocoded")), _num(s.get("longitude_geocoded"))
        coord_how = "inferred (geocoded)"
        coord_where = f"geocoded from '{s.get('geocode_query')}' — {s.get('geocode_source')}"
        precision = f"{precision}; geocoded at {s.get('geocode_level')} level"
    start, end = s.get("collection_start") or None, s.get("collection_end") or None
    return {
        "Survey ID": s.get("survey_id"),
        "Species reported": s.get("species_reported"),
        "Species complex/group": s.get("species_complex"),
        "Molecular species": s.get("molecular_species"),
        "Country (site)": s.get("country"), "Sampling site": s.get("site_name"),
        "Admin level 1": s.get("admin1"), "Admin level 2": s.get("admin2"),
        "Latitude": lat, "Longitude": lon,
        "Coordinates reported or inferred": coord_how,
        "Evidence location (coordinates)": coord_where,
        "Spatial precision / uncertainty": precision,
        "Collection start date": start, "Collection end date": end,
        "Collection year": collection_year(start, end),
        "Temporal precision": temporal_precision(start, end),
        "Mosquito collection method": s.get("collection_method"),
        "Mosquito life stage": s.get("life_stage"),
        "Wild/laboratory population": s.get("population_type"),
        "Generation": s.get("generation"),
        "Total sample size": _num(s.get("total_sample_size")),
        "Species identification method": s.get("species_id_method"),
        "Coordinates verified": "FALSE",
    }


def _flag(*notes):
    return "; ".join(n for n in notes if n) or None


def dead_from_pct(pct, n):
    """n_dead from a printed mortality % and n tested — only if exactly one whole
    number fits the % as printed (e.g. 36.25% of 80 = 29). None otherwise."""
    pct, n = _num(pct), _num(n)
    if pct is None or not n:
        return None
    decimals = len(repr(float(pct)).split(".")[1].rstrip("0"))
    slack = 0.5 * 10 ** -decimals * n / 100     # rounding of the printed % in mosquitoes
    if slack >= 0.5:
        return None                             # several counts fit: not uniquely determined
    d = pct * n / 100
    return round(d) if abs(d - round(d)) <= slack + 1e-9 else None


def _bioassay_cols(b):
    if not b:
        return {}
    exposed, dead, alive = _num(b.get("n_exposed")), _num(b.get("n_dead")), _num(b.get("n_alive"))
    derived = None
    if dead is None and alive is None:
        dead = dead_from_pct(b.get("reported_mortality_pct"), exposed)
        if dead is not None:
            derived = "dead/surviving counts derived in code from reported % x number exposed"
    if alive is None and exposed is not None and dead is not None:
        alive = exposed - dead
    if dead is None and exposed is not None and alive is not None:
        dead = exposed - alive
    mort = _ratio(dead, exposed)
    if mort is None and _num(b.get("reported_mortality_pct")) is not None:
        mort = round(_num(b.get("reported_mortality_pct")) / 100, 4)   # reported only
    dur = _num(b.get("exposure_duration_min"))
    t = _num(b.get("mortality_time_h"))
    return {
        "Insecticide name": b.get("insecticide"),
        "Pyrethroid subtype": pyrethroid_subtype(b.get("insecticide"), b.get("insecticide_class")),
        "Insecticide concentration": b.get("concentration"),
        "Exposure duration": f"{dur} min" if dur is not None else None,
        "Assay method": b.get("assay_method"), "Assay type": b.get("assay_type"),
        "Synergist used": b.get("synergist") or "none",
        "Number exposed": exposed, "Number surviving": alive, "Number dead": dead,
        "Survival proportion": round(1 - mort, 4) if mort is not None else None,
        "Mortality proportion": mort,
        "Phenotype": who_phenotype(mort, b.get("assay_type"), b.get("synergist")),
        "Mortality assessment time": f"{t} h" if t is not None else None,
        "_derived": derived,
        "_note": b.get("inconsistency_note") or None,
    }


def _marker_cols(g):
    gene, var = g.get("gene_std") or g.get("gene"), g.get("variant_std") or g.get("marker")
    return {"Gene": gene, "Variant/marker": var}


def study_rows(rid, folder):
    study = yaml.safe_load((folder / "study.yaml").read_text(encoding="utf-8")) or {}
    surveys = {s["survey_id"]: s for s in _read_csv(folder / "surveys.csv")}
    bioassays = {b["bioassay_id"]: b for b in _read_csv(folder / "bioassays.csv")}
    base = _study_cols(rid, study)
    rows = []

    for g in _read_csv(folder / "genotypes.csv"):
        r = {**base, **_survey_cols(surveys.get(g["survey_id"])), **_marker_cols(g), **_prov_cols(g)}
        f = _geno_freqs(g.get("rr"), g.get("rs"), g.get("ss"))
        n = _num(g.get("n_genotyped")) or f.get("_n")
        rac = _num(g.get("resistant_allele_count"))
        freq = f.get("Allele frequency")
        raw = "yes" if f else "no"
        if freq is None and rac is not None and n and g.get("pooled") != "True":
            if g.get("variant_type") == "SNP":
                freq, raw = round(rac / (2 * n), 4), "yes (allele counts)"
            else:   # CNV / SV, older extractions: carriers were stored here
                freq, raw = round(rac / n, 4), "yes (carrier counts)"
        carriers = _num(g.get("n_carriers"))
        if freq is None and carriers is not None and n:
            if g.get("variant_type") in ("CNV", "SV"):   # carrier frequency is the usual measure
                freq, raw = round(carriers / n, 4), f"yes (carrier counts: {carriers}/{n})"
            else:   # SNP: RR vs RS unknown, so the allele frequency is not determined
                raw = f"carriers only ({carriers}/{n}) — allele frequency not determinable"
        if freq is None and _num(g.get("reported_allele_freq")) is not None:
            freq = _num(g.get("reported_allele_freq"))
            raw = "no (reported frequency only" + (f"; carriers {carriers}/{n})" if carriers is not None
                                                   and n else ")")
        r.update({
            "Record type": "genotype",
            "Amino-acid change": g.get("amino_acid_change"),
            "Nucleotide change": g.get("nucleotide_change"),
            "Resistant allele": g.get("resistant_allele"),
            "Genotyping method": g.get("genotyping_method"),
            "Number genotyped": n, "Resistant allele count": rac, "Allele frequency": freq,
            "Homozygous resistant (RR)": _num(g.get("rr")), "Heterozygous (RS)": _num(g.get("rs")),
            "Homozygous susceptible (SS)": _num(g.get("ss")),
            "RR frequency": f.get("RR frequency"), "RS frequency": f.get("RS frequency"),
            "SS frequency": f.get("SS frequency"),
            "Sample size reported": "yes" if n else "no",
            "Raw counts available": raw + (" — pooled" if g.get("pooled") == "True" else ""),
            "Data quality flag": g.get("inconsistency_note") or None,
        })
        rows.append(r)

    for b in bioassays.values():
        r = {**base, **_survey_cols(surveys.get(b["survey_id"])), **_bioassay_cols(b), **_prov_cols(b)}
        raw = "no (reported mortality only)"
        if _num(b.get("n_dead")) is not None or _num(b.get("n_alive")) is not None:
            raw = "yes"
        elif r["_derived"]:
            raw = "derived (reported % x n)"
        r.update({"Record type": "bioassay",
                  "Sample size reported": "yes" if _num(b.get("n_exposed")) else "no",
                  "Raw counts available": raw,
                  "Data quality flag": _flag(r["_note"], r["_derived"])})
        rows.append(r)

    # geno_pheno: merge alive + dead rows of the same (survey, test, marker) into one row.
    # The test is the linked bioassay, or — when survivors/dead were pooled across tests —
    # the insecticide as reported. (Older outputs have no survey_id column: use the bioassay's.)
    groups = {}
    for gp in _read_csv(folder / "geno_pheno.csv"):
        bid = gp.get("bioassay_id") or None
        sid = gp.get("survey_id") or bioassays.get(bid, {}).get("survey_id")
        key = (sid, bid or gp.get("insecticide") or "", gp.get("gene_std") or gp["gene"],
               gp.get("variant_std") or gp["marker"])
        groups.setdefault(key, {})[gp["phenotype_group"]] = gp
    for (sid, _test, gene, var), by in groups.items():
        first = by.get("alive") or by.get("dead")
        b = bioassays.get(first.get("bioassay_id") or None, {})
        if b:
            test_cols = _bioassay_cols(b)
        else:   # pooled across tests: only the insecticide is known
            ins = first.get("insecticide") or None
            test_cols = {"Insecticide name": ins, "Pyrethroid subtype": pyrethroid_subtype(ins, None)}
        r = {**base, **_survey_cols(surveys.get(sid)), **test_cols,
             **_marker_cols(first), **_prov_cols(first)}
        al, de = by.get("alive", {}), by.get("dead", {})
        tot = {k: sum(_num(x.get(k)) or 0 for x in (al, de)) for k in ("rr", "rs", "ss")}
        has_counts = all(_num(x.get(k)) is not None for x in by.values() for k in ("rr", "rs", "ss"))
        f = _geno_freqs(tot["rr"], tot["rs"], tot["ss"]) if has_counts else {}
        is_vgsc = gene == "Vgsc"
        raw = "yes" if f else "no"
        if not f:
            groups_ = (("survivors", al), ("dead", de))
            carr = [f"{lab} {_num(x.get('n_carriers'))}/{_num(x.get('n'))}" for lab, x in groups_
                    if _num(x.get("n_carriers")) is not None]
            freqs = [f"{lab} {_num(x.get('reported_allele_freq'))}" for lab, x in groups_
                     if _num(x.get("reported_allele_freq")) is not None]
            if carr:
                raw = "carriers only (" + ", ".join(carr) + ")"
            elif freqs:
                raw = "no (reported allele frequency only: " + ", ".join(freqs) + ")"
        notes = [x.get("inconsistency_note") for x in (al, de)]
        if not b:
            notes.append("survivors/dead pooled across tests — not linked to a single bioassay")
        r.update({
            "Record type": "geno_pheno",
            "Phenotype group": " + ".join(k for k in ("alive", "dead") if k in by),
            "VGSC variant in survivors": var if is_vgsc and al else None,
            "VGSC variant in dead mosquitoes": var if is_vgsc and de else None,
            "RR survivors": _num(al.get("rr")), "RS survivors": _num(al.get("rs")),
            "SS survivors": _num(al.get("ss")),
            "RR dead": _num(de.get("rr")), "RS dead": _num(de.get("rs")), "SS dead": _num(de.get("ss")),
            "Number genotyped": f.get("_n"), "Allele frequency": f.get("Allele frequency"),
            "Homozygous resistant (RR)": tot["rr"] if f else None,
            "Heterozygous (RS)": tot["rs"] if f else None,
            "Homozygous susceptible (SS)": tot["ss"] if f else None,
            "RR frequency": f.get("RR frequency"), "RS frequency": f.get("RS frequency"),
            "SS frequency": f.get("SS frequency"),
            "Sample size reported": "yes" if f or any(_num(x.get("n")) for x in by.values()) else "no",
            "Raw counts available": raw,
            "Data quality flag": _flag(*notes, test_cols.get("_note"), test_cols.get("_derived")),
        })
        rows.append(r)

    if not rows:
        rows.append({**base, "Record type": "no_data"})
    return rows


def build(extracted=EXTRACTED, out_dir=FINAL):
    extracted, out_dir = Path(extracted), Path(out_dir)
    rows = []
    for folder in sorted(p for p in extracted.glob("*") if (p / "study.yaml").exists()):
        rows.extend(study_rows(folder.name, folder))
    out_dir.mkdir(parents=True, exist_ok=True)
    table = [[NA if r.get(c) in (None, "") else r.get(c) for c in COLUMNS] for r in rows]

    csv_path = out_dir / "ir_extraction.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(COLUMNS)
        w.writerows(table)

    try:
        import openpyxl
        from openpyxl.styles import Font
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "extraction"
        ws.append(COLUMNS)
        for c in ws[1]:
            c.font = Font(bold=True)
        for row in table:
            ws.append(row)
        ws.freeze_panes = "C2"
        wb.save(out_dir / "ir_extraction.xlsx")
    except ImportError:
        print("(openpyxl not installed — wrote CSV only)")
    return csv_path


if __name__ == "__main__":
    print(f"Wrote {build()}")
