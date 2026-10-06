"""
Stage 2 core: the extractor. Pulls insecticide-resistance data out of one paper
into the relational data model (see CLAUDE.md):

    study       one paper
    surveys     site x time window x species x collection method
    genotypes   survey x marker            (RR/RS/SS or allele counts; pooled flag)
    bioassays   survey x insecticide x concentration x synergist
    geno_pheno  survey x bioassay (or insecticide, if pooled) x marker x outcome (alive/dead)
                -> RR/RS/SS

Every record carries provenance (source sentence/table, page, figure, supplement).

Division of labour:
  - the LLM extracts RAW COUNTS + text exactly as printed (markers as written,
    place names, any coordinates the paper STATES) — it never corrects a value;
    mismatches go in `inconsistency_note` for a human;
  - code (targets.normalise, validate.py, export.py) normalises marker names,
    checks consistency, and computes every derived value (frequencies,
    mortality %, WHO phenotype, pyrethroid subtype...).

The validator (validate.py) is the guardrail: its errors are fed back here for a
repair attempt (see run_extraction.extract_one).
"""
import csv
import re
from datetime import date
from enum import Enum
from pathlib import Path

import yaml
from pydantic import BaseModel

import llm
import targets


def study_id(paper_id):
    """Filesystem/ID-safe version of the roster id."""
    return re.sub(r"[^A-Za-z0-9_]", "_", str(paper_id))


# --- The schema the model fills in -----------------------------------------

class Confidence(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class Provenance(BaseModel):
    source_text: str | None   # verbatim sentence, or the table row/cell(s) used
    page: str | None          # page number(s) in the PDF, e.g. "5" or "5-6"
    table: str | None         # e.g. "Table 2"
    figure: str | None        # e.g. "Figure 3B"
    supplement: str | None    # e.g. "Additional file 2, Table S1"


class SpatialPrecision(str, Enum):
    point = "point"           # exact coordinates of the collection point
    village = "village"
    town = "town"             # town / city / neighbourhood
    admin2 = "admin2"         # district / county / health zone
    admin1 = "admin1"         # region / province / state
    country = "country"
    unknown = "unknown"


class PopulationType(str, Enum):
    wild_adult = "wild_adult"               # field-caught adults (F0)
    wild_reared = "wild_reared"             # field larvae/pupae reared to adults (F0)
    f1_progeny = "f1_progeny"               # F1 offspring of field-caught females
    laboratory = "laboratory"               # lab colony (should normally not be extracted)
    unknown = "unknown"


class StudyInfo(BaseModel):
    title: str | None
    first_author: str | None
    doi: str | None
    pmid: str | None
    publication_year: int | None
    countries: list[str]
    data_source: str | None     # e.g. "primary field study", "national IR monitoring (NMCP/PMI)"
    provenance: Provenance


class Survey(BaseModel):
    survey_id: str
    country: str
    site_name: str | None
    admin1: str | None
    admin2: str | None
    latitude_reported: float | None      # ONLY if the paper states coordinates
    longitude_reported: float | None
    coordinates_provenance: Provenance | None
    spatial_precision: SpatialPrecision
    collection_start: str | None         # "YYYY", "YYYY-MM" or "YYYY-MM-DD" — as precise as reported
    collection_end: str | None
    temporal_notes: str | None
    species_reported: str | None         # as written, e.g. "An. gambiae s.l."
    species_complex: str | None          # e.g. "An. gambiae complex", "An. funestus group"
    molecular_species: str | None        # e.g. "An. coluzzii", "An. arabiensis", "An. funestus s.s."
    species_id_method: str | None        # e.g. "SINE200 PCR", "morphology + Scott et al. PCR"
    collection_method: str | None        # e.g. "larval collection", "HLC", "PSC", "CDC light trap"
    life_stage: str | None               # stage COLLECTED: larvae / pupae / adult
    population_type: PopulationType
    generation: str | None               # "F0", "F1"
    total_sample_size: int | None        # mosquitoes in this survey (as reported)
    provenance: Provenance


class Genotype(BaseModel):
    survey_id: str
    gene: str                            # as reported, e.g. "kdr", "Vgsc", "Ace-1"
    marker: str                          # as reported, e.g. "L1014F", "kdr-west", "G119S"
    amino_acid_change: str | None
    nucleotide_change: str | None        # e.g. "TTA>TTT"
    resistant_allele: str | None         # e.g. "1014F", "R"
    genotyping_method: str | None        # e.g. "TaqMan", "AS-PCR", "HOLA", "sequencing"
    pooled: bool                         # pooled samples (no individual genotypes)
    n_genotyped: int | None              # individuals genotyped at this marker
    rr: int | None                       # homozygous resistant
    rs: int | None                       # heterozygous
    ss: int | None                       # homozygous susceptible
    n_carriers: int | None               # individuals with >=1 resistant copy, when RR/RS not split
    resistant_allele_count: int | None   # only if reported as allele counts
    reported_allele_freq: float | None   # 0-1, only as printed in the paper
    inconsistency_note: str | None       # the paper's own numbers don't reconcile (values kept as printed)
    provenance: Provenance


class Bioassay(BaseModel):
    bioassay_id: str
    survey_id: str
    insecticide: str                     # e.g. "deltamethrin"
    insecticide_class: str | None        # pyrethroid / organochlorine / carbamate / organophosphate / ...
    concentration: str | None            # with units, as reported, e.g. "0.05%", "12.5 µg/bottle"
    exposure_duration_min: float | None
    assay_method: str | None             # "WHO tube", "CDC bottle", "cone", ...
    assay_type: str | None               # "diagnostic dose", "intensity 5x", "intensity 10x", "synergist"
    synergist: str | None                # e.g. "PBO"; null if none
    dead_alive_printed: bool             # the paper itself prints the number dead or alive
    n_exposed: int | None
    n_dead: int | None
    n_alive: int | None
    reported_mortality_pct: float | None # only as printed
    mortality_time_h: float | None       # e.g. 24
    inconsistency_note: str | None
    provenance: Provenance


class Outcome(str, Enum):
    alive = "alive"                      # bioassay survivors (papers often say "resistant")
    dead = "dead"                        # killed by the bioassay ("susceptible")


class GenoPheno(BaseModel):
    survey_id: str
    bioassay_id: str | None              # the ONE bioassay these mosquitoes come from; null if pooled
    insecticide: str | None              # as reported, e.g. "deltamethrin" or "deltamethrin + permethrin"
    gene: str
    marker: str
    phenotype_group: Outcome
    rr: int | None
    rs: int | None
    ss: int | None
    n: int | None
    n_carriers: int | None               # individuals with >=1 resistant copy, when RR/RS not split
    reported_allele_freq: float | None   # 0-1, only if printed and counts are not given
    inconsistency_note: str | None
    provenance: Provenance


class Extraction(BaseModel):
    study: StudyInfo
    surveys: list[Survey]
    genotypes: list[Genotype]
    bioassays: list[Bioassay]
    geno_pheno: list[GenoPheno]
    confidence: Confidence
    decisions_readme: str                # markdown documenting extraction decisions


# --- The spec / rules given to the model -----------------------------------

RULES = (
    "EXTRACTION RULES:\n"
    "1. Markers: extract ONLY the target markers listed below (other markers are ignored). Give "
    "`gene` and `marker` EXACTLY as the paper writes them (e.g. 'kdr' / 'L1014F'); code maps them "
    "to An. gambiae numbering. Do not renumber yourself.\n"
    "2. RAW COUNTS ONLY. Mosquitoes are diploid: give genotype classes RR (homozygous resistant), "
    "RS (heterozygous), SS (homozygous susceptible) and n_genotyped. Never compute frequencies or "
    "percentages yourself. If the paper gives ONLY a frequency/percentage, put it in "
    "`reported_allele_freq` (as a 0-1 proportion) or `reported_mortality_pct`, and leave the count "
    "fields null — never back-calculate counts from percentages. E.g. a bioassay reported as "
    "'80 tested, 36.25% mortality' -> n_exposed = 80, reported_mortality_pct = 36.25, "
    "dead_alive_printed = false, n_dead = n_alive = null (code derives the counts and flags "
    "them as derived). Set dead_alive_printed = true ONLY if the number dead or alive for that "
    "test is literally printed in the paper or supplement.\n"
    "2b. Carriers: if the paper gives only how many mosquitoes CARRY the mutation without "
    "splitting homozygotes and heterozygotes (e.g. '1 of 100 was positive for kdr-west'), put that "
    "number in `n_carriers` and the number tested in n_genotyped (or n). Do not turn it into a "
    "frequency.\n"
    "3. Pooled samples: set `pooled` true and give what is reported (e.g. reported_allele_freq).\n"
    "4. CNVs / duplications (Ace-1, Cyp6aa1) and the 6.5 kb SV: put the number of mosquitoes "
    "carrying the variant in `n_carriers` and the number tested in `n_genotyped`; use "
    "rr/rs/ss only if the paper reports genotype classes.\n"
    "4b. Multi-allelic codon (Vgsc 995/1014 carries L, F and S): record L995F and L995S as two "
    "separate genotype rows. For each, RR = individuals with two copies of THAT allele, RS = one "
    "copy, SS = n_genotyped - RR - RS (individuals with no copy of that allele, which includes "
    "carriers of the other mutation). This is the one case where you may derive SS by subtraction; "
    "state the true wild-type (L/L) count and any F/S heterozygotes in the README.\n"
    "5. Bioassays: extract them ONLY for surveys in this paper (one record per survey x insecticide "
    "x concentration x synergist x time point). Give n_exposed, n_dead, n_alive as reported. Skip "
    "laboratory reference strains (e.g. Kisumu) — they are controls, not data.\n"
    "6. Genotype-phenotype: WHENEVER genotypes are reported separately for bioassay SURVIVORS "
    "(alive, often called 'resistant') and DEAD ('susceptible') mosquitoes, record them in "
    "geno_pheno: one row per (survey, test, marker, alive/dead) with RR/RS/SS and n (or "
    "reported_allele_freq if only a frequency is printed). Set bioassay_id when the genotyped "
    "mosquitoes come from exactly ONE extracted bioassay. Otherwise — e.g. survivors pooled across "
    "several insecticides or doses, or the bioassay itself is not extractable — leave bioassay_id "
    "null and give `insecticide` as reported (e.g. 'deltamethrin + permethrin'). Never drop "
    "phenotype-split genotypes just because they cannot be linked to a single bioassay. Do NOT "
    "also add the same mosquitoes to `genotypes` (no double counting); `genotypes` is for "
    "population samples not split by bioassay outcome.\n"
    "7. Resolution & no double counting: extract at the FINEST spatial, temporal and species "
    "breakdown the paper reports (per site, per time window, per molecular species). If the paper "
    "ALSO gives pooled totals (all sites, all years, all species), do NOT additionally extract them.\n"
    "8. Values exactly as printed: NEVER change a number the paper prints, even an obvious typo. "
    "If a record's own numbers don't reconcile (RR+RS+SS != N, dead + alive != exposed, counts that "
    "contradict the paper's frequency...), keep every value as printed and describe the mismatch in "
    "that record's `inconsistency_note` (e.g. 'RR+RS+SS = 36 but N = 34; printed freq 0.0735 fits "
    "N = 34, so SS = 33 may be a typo for 31'). A human decides. `inconsistency_note` is ONLY for "
    "printed numbers that contradict each other — leave it null otherwise. Never use it for "
    "comments, methods, pooling, missing counts or how you read a value: those go in the README. "
    "If data are missing or not uniquely determined, extract only what is printed and explain "
    "what was dropped in the README.\n"
    "8b. Bioassays are actual tests reported by the paper: one specific insecticide each (never a "
    "class like 'pyrethroids'), with the counts the paper gives for that test. Never build a "
    "bioassay record from genotyped subsets or from pooled results across insecticides. If the "
    "paper reports only knockdown times (KDT50) and no mortality, skip that bioassay.\n"
    "9. Missing information: use null. Never guess.\n"
)

SPATIAL = (
    "SPATIAL: one survey per distinct site x time window x species x collection method. Give the "
    "country, site name and any admin units named in the paper. Fill latitude_reported / "
    "longitude_reported ONLY when the paper itself states coordinates (convert degrees-minutes-"
    "seconds to decimal degrees; S and W are negative) and cite where in "
    "`coordinates_provenance`. NEVER invent or look up coordinates — geocoding is done later in "
    "code. Set spatial_precision to the finest level the location is described at.\n"
)

TEMPORAL = (
    "TEMPORAL: collection_start / collection_end as precise as reported: 'YYYY-MM-DD', 'YYYY-MM' or "
    "'YYYY'. A single year -> start = end = 'YYYY'. A season -> its months if stated. If ONLY the "
    "publication date is known, leave both null and say so in temporal_notes.\n"
)

SPECIES = (
    "SPECIES: species_reported as written; species_complex (An. gambiae complex / An. funestus "
    "group / other); molecular_species when molecularly identified (An. gambiae s.s., An. coluzzii, "
    "An. arabiensis, An. funestus s.s., hybrids...). When genotypes are reported per molecular "
    "species, create one survey per species.\n"
)

IDENTIFIERS = (
    "IDENTIFIERS: survey_id = study_id + short suffix (e.g. '<study_id>_kisumu_2019_col'); "
    "bioassay_id = survey_id + short suffix (e.g. '_delta_005'). Use letters, digits and underscores. "
    "Every genotype/bioassay/geno_pheno must point to an existing survey_id; a geno_pheno "
    "bioassay_id, when given, must be an existing bioassay of that same survey.\n"
)

PROVENANCE = (
    "PROVENANCE: for EVERY record, fill `provenance` with the verbatim sentence (or a description "
    "of the table row/cells used), the PDF page, and the table / figure / supplementary file. This "
    "is how humans will verify your numbers.\n"
)

DOCUMENTATION = (
    "README: in `decisions_readme`, write concise markdown documenting the key decisions — how "
    "surveys were split, marker names as written, any pooling, data you could not use and why, "
    "any values read from figures. Set `confidence` to your overall confidence in the extraction.\n"
)


def system_prompt():
    return (
        "You are a meticulous data extractor building a database of insecticide-resistance marker "
        "frequencies and linked bioassays in African Anopheles mosquitoes. Extract study, survey, "
        "genotype, bioassay and genotype-phenotype data from the paper into the required schema.\n\n"
        + RULES + "\n" + SPATIAL + "\n" + TEMPORAL + "\n" + SPECIES + "\n" + IDENTIFIERS + "\n"
        + PROVENANCE + "\n" + DOCUMENTATION
        + "\nTARGET MARKERS (extract only these):\n" + targets.summary()
    )


def extract(pdf_bytes, sid, model="flash", supplement_parts=None,
            eligibility_record=None, repair=None, max_tokens=65536):
    """Run the extractor. Returns an llm.LLMResult; `.parsed` is an `Extraction`
    (or None). repair: optional {"error": str, "previous": dict} for a fix-up retry.
    """
    supplement_parts = supplement_parts or []
    parts = [llm.Pdf(pdf_bytes), *supplement_parts]

    instr = [f"Extract this paper. study_id = '{sid}'."]
    if supplement_parts:
        instr.append(f"{len(supplement_parts)} supplementary file(s) are included above "
                     "(spreadsheets/CSV/Word as text) — use them.")
    if eligibility_record:
        instr.append("Context from the eligibility stage (what was already spotted): "
                     + str(eligibility_record))
    if repair and repair.get("too_long"):
        instr.append("Your PREVIOUS answer was TOO LONG and got cut off. Extract the same data, but "
                     "keep every provenance.source_text to at most 20 words (or just the table row "
                     "label), leave temporal_notes null unless essential, and keep decisions_readme "
                     "under 200 words.")
    elif repair:
        instr.append("Your PREVIOUS attempt FAILED validation with these errors:\n"
                     + repair["error"]
                     + "\n\nYour previous output was:\n" + str(repair["previous"])
                     + "\n\nFix the specific problems (re-check the paper) and return the "
                       "corrected, complete extraction. If a flagged value really is printed that "
                       "way in the paper, keep it and explain in that record's inconsistency_note "
                       "instead of changing it.")
    parts.append(llm.Text("\n\n".join(instr)))
    return llm.call(model, system_prompt(), parts, Extraction, max_tokens=max_tokens)


def keep_printed_only(ex: Extraction):
    """Drop bioassay dead/alive counts the model computed instead of read (it says so in
    dead_alive_printed). export.py re-derives them from the printed % and flags them."""
    for b in ex.bioassays:
        if not b.dead_alive_printed:
            b.n_dead = b.n_alive = None
    return ex


# --- Writing the per-study output files ------------------------------------

PROV_COLS = ["source_text", "page", "table", "figure", "supplement"]

SURVEY_COLS = ["survey_id", "country", "site_name", "admin1", "admin2",
               "latitude_reported", "longitude_reported", "spatial_precision",
               "collection_start", "collection_end", "temporal_notes",
               "species_reported", "species_complex", "molecular_species", "species_id_method",
               "collection_method", "life_stage", "population_type", "generation",
               "total_sample_size"] \
    + [f"coord_{c}" for c in PROV_COLS] + PROV_COLS
GENOTYPE_COLS = ["survey_id", "gene", "marker", "gene_std", "variant_std", "variant_type", "tier",
                 "amino_acid_change", "nucleotide_change", "resistant_allele", "genotyping_method",
                 "pooled", "n_genotyped", "rr", "rs", "ss", "n_carriers", "resistant_allele_count",
                 "reported_allele_freq", "inconsistency_note"] + PROV_COLS
BIOASSAY_COLS = ["bioassay_id", "survey_id", "insecticide", "insecticide_class", "concentration",
                 "exposure_duration_min", "assay_method", "assay_type", "synergist",
                 "dead_alive_printed", "n_exposed", "n_dead", "n_alive", "reported_mortality_pct",
                 "mortality_time_h", "inconsistency_note"] + PROV_COLS
GENO_PHENO_COLS = ["survey_id", "bioassay_id", "insecticide", "gene", "marker", "gene_std",
                   "variant_std", "variant_type", "phenotype_group", "rr", "rs", "ss", "n",
                   "n_carriers", "reported_allele_freq", "inconsistency_note"] + PROV_COLS

OUTPUT_FILES = ("study.yaml", "surveys.csv", "genotypes.csv", "bioassays.csv",
                "geno_pheno.csv", "README.md")


def _flat(record, extra=None):
    """Model -> flat dict: enums to values, provenance spread into PROV_COLS."""
    d = record.model_dump(mode="json")
    prov = d.pop("provenance", None) or {}
    d.update({c: prov.get(c) for c in PROV_COLS})
    cprov = d.pop("coordinates_provenance", "absent")
    if cprov != "absent":
        d.update({f"coord_{c}": (cprov or {}).get(c) for c in PROV_COLS})
    if "gene" in d and "marker" in d:
        t = targets.normalise(d["gene"], d["marker"])
        d.update(gene_std=t and t["gene"], variant_std=t and t["variant"],
                 variant_type=t and t["variant_type"], tier=t and t["tier"])
    d.update(extra or {})
    return d


def _write_csv(path, cols, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: "" if r.get(c) is None else r.get(c) for c in cols})


def write_outputs(out_dir, sid, ex: Extraction, model_id, warnings=()):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    study = {"study_id": sid, **ex.study.model_dump(mode="json"),
             "confidence": ex.confidence.value, "model": model_id,
             "extracted": date.today().isoformat()}
    (out_dir / "study.yaml").write_text(
        yaml.safe_dump(study, sort_keys=False, allow_unicode=True), encoding="utf-8")

    _write_csv(out_dir / "surveys.csv", SURVEY_COLS, [_flat(s) for s in ex.surveys])
    _write_csv(out_dir / "genotypes.csv", GENOTYPE_COLS, [_flat(g) for g in ex.genotypes])
    _write_csv(out_dir / "bioassays.csv", BIOASSAY_COLS, [_flat(b) for b in ex.bioassays])
    _write_csv(out_dir / "geno_pheno.csv", GENO_PHENO_COLS, [_flat(g) for g in ex.geno_pheno])

    warn = ""
    if warnings:
        warn = "\n## Validator warnings\n\n" + "\n".join(f"- {w}" for w in warnings) + "\n"
    readme = (f"# Extraction record — {sid}\n\n"
              f"- Extracted: {date.today().isoformat()}\n"
              f"- Model: {model_id}\n"
              f"- Confidence (model's own): {ex.confidence.value}\n"
              f"- Surveys: {len(ex.surveys)} · Genotype rows: {len(ex.genotypes)} · "
              f"Bioassays: {len(ex.bioassays)} · Geno-pheno rows: {len(ex.geno_pheno)}\n\n"
              "## Decisions\n\n" + ex.decisions_readme.strip() + "\n" + warn)
    (out_dir / "README.md").write_text(readme, encoding="utf-8")
