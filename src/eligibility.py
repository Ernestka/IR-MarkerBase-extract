"""
Stage 1 core: the eligibility spec, the structured schema the model fills in, and
the single assessment call.

The schema does three jobs in one call:
  1. Eligibility — does the paper meet the IR extraction criteria?
  2. Duplicate risk — might its samples overlap with / be a subset of another study?
  3. Supplement check — does data we'd need live in supplementary files not provided?

This module is imported (by run_eligibility.py / run_local.py), not run directly.
"""
from enum import Enum

from pydantic import BaseModel

import llm
import targets

# Bump this when the eligibility spec/schema changes materially. It's stamped on
# every assessed row so we can tell which papers were judged under an old spec.
SPEC_VERSION = 1


# --- The schema ------------------------------------------------------------

class Confidence(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class RiskLevel(str, Enum):
    none = "none"
    low = "low"
    medium = "medium"
    high = "high"


class Criterion(BaseModel):
    met: bool
    evidence: str  # a short quote or paraphrase justifying the call (with page/table)


class EligibilityChecks(BaseModel):
    # REQUIRED (see REQUIRED_CHECKS below)
    is_anopheles: Criterion
    reports_target_markers: Criterion           # >=1 marker from config/target_loci.csv
    reports_extractable_genotype_data: Criterion
    african_field_population: Criterion         # field F0, or F1 progeny of field females
    is_primary_study: Criterion
    # RECORDED ONLY (useful for modelling, not required to be eligible)
    sub_country_location: Criterion
    temporal_resolution_within_3y: Criterion


# Which checks must ALL be met. Edit here to tighten/loosen the rule — e.g. add
# "sub_country_location" if country-only papers should be excluded.
REQUIRED_CHECKS = ("is_anopheles", "reports_target_markers", "reports_extractable_genotype_data",
                   "african_field_population", "is_primary_study")


class DuplicateRisk(BaseModel):
    level: RiskLevel
    evidence: str


class SupplementNeed(BaseModel):
    needed: bool
    evidence: str


class Assessment(BaseModel):
    eligible: bool                  # True only if ALL required checks are met
    confidence: Confidence
    checks: EligibilityChecks
    duplicate_risk: DuplicateRisk
    supplement: SupplementNeed
    markers_found: list[str]        # as written in the paper, e.g. "L1014F (kdr-west)"
    species: list[str]              # e.g. "An. coluzzii", "An. funestus s.s."
    countries: list[str]
    collection_years: list[int]
    has_bioassays: bool
    has_genotype_phenotype: bool    # genotypes reported separately for alive vs dead
    sample_size: int | None
    summary: str
    exclusion_reasons: list[str]


# --- The spec the model is judged against ----------------------------------

CRITERIA = (
    "A paper is ELIGIBLE only if ALL of the following REQUIRED checks are true:\n"
    "1. is_anopheles — studies Anopheles mosquitoes (not only Aedes, Culex or other genera).\n"
    "2. reports_target_markers — genotypes at least ONE of these insecticide-resistance markers "
    "(papers may use older Musca domestica numbering, e.g. L1014F = L995F, or names like "
    "'kdr-west'/'kdr-east'):\n" + targets.summary() + "\n"
    "3. reports_extractable_genotype_data — gives, for at least one population, genotype counts "
    "(RR/RS/SS), allele counts, or an allele/genotype frequency WITH the number of mosquitoes "
    "genotyped — not merely that a mutation was 'present' or 'detected'. Figures with readable "
    "values count.\n"
    "4. african_field_population — mosquitoes collected in the field in an AFRICAN country "
    "(including Madagascar and the islands), tested as field-caught adults (F0), adults reared "
    "from field larvae/pupae, or F1 progeny of field-caught females. A paper whose ONLY genotyped "
    "mosquitoes are laboratory colonies (e.g. Kisumu, FANG, Ngousso, FUMOZ) or non-African "
    "populations FAILS.\n"
    "5. is_primary_study — a primary empirical study (exclude reviews, meta-analyses, "
    "commentaries, pure modelling papers, and papers that only re-analyse previously published "
    "genotype data).\n\n"
    "Also RECORD (these do NOT affect `eligible`):\n"
    "- sub_country_location — data can be tied to a location below country level (site, village, "
    "town, district, or coordinates). Judge the FINEST resolution found anywhere in the paper.\n"
    "- temporal_resolution_within_3y — data can be tied to a collection window of at most three "
    "years (a stated collection year or range <=3 years is enough).\n\n"
    "Bioassay-only papers (no marker genotyping) are NOT eligible. Note in `has_bioassays` whether "
    "the paper reports bioassays (WHO tube, CDC bottle, cone tests), and in "
    "`has_genotype_phenotype` whether genotypes are given separately for survivors vs dead "
    "mosquitoes.\n\n"
    "Read the ENTIRE paper before judging — main text and EVERY table and figure (plus any "
    "supplement provided). Assess each check independently and cite the evidence (with page/table). "
    "Set `eligible` to true only when EVERY required check is met. Record unmet or unclear checks "
    "in `exclusion_reasons`. Prefer low confidence over guessing."
)

DUPLICATE_GUIDANCE = (
    "DUPLICATE RISK: judge whether this study's mosquito samples may overlap with, or be a subset "
    "of, a LARGER or previously-published dataset — e.g. the paper states the samples come from a "
    "previous study, a named surveillance network (e.g. PMI VectorLink), the MalariaGEN Ag1000G / "
    "Vector Observatory, or a multi-country consortium. Set `duplicate_risk.level` to `high` only "
    "with concrete textual evidence of such overlap, and quote it. Routine new collections are "
    "`none`/`low`."
)

SUPPLEMENT_GUIDANCE = (
    "SUPPLEMENT CHECK: decide whether data we'd need appears to live in SUPPLEMENTARY materials NOT "
    "included in the document(s) provided — e.g. per-site genotype counts, bioassay counts, or site "
    "coordinates in 'Additional file 2' / 'Table S3'. Set `supplement.needed` to true and quote the "
    "pointer in `supplement.evidence`. If supplementary files ARE included below and contain the "
    "data, set it false."
)

SYSTEM = (
    "You are a meticulous curator for a database of insecticide-resistance marker frequencies "
    "(and linked bioassays) in African Anopheles malaria vectors. " + CRITERIA + "\n\n"
    + DUPLICATE_GUIDANCE + "\n\n" + SUPPLEMENT_GUIDANCE
)


def enforce_required(a: Assessment) -> Assessment:
    """The model sets `eligible`, but the rule lives in code: eligible == all
    REQUIRED_CHECKS met. Disagreements are noted in exclusion_reasons."""
    required_ok = all(getattr(a.checks, c).met for c in REQUIRED_CHECKS)
    if a.eligible != required_ok:
        a.exclusion_reasons.append(
            f"(code) model said eligible={a.eligible} but required checks give {required_ok}; "
            "using the checks.")
        a.eligible = required_ok
    return a


def assess_pdf_bytes(pdf_bytes, model="flash", supplement_parts=None):
    """Send the paper (and any supplementary files) to the model.

    Returns an llm.LLMResult; `.parsed` is the validated `Assessment` (or None).
    """
    supplement_parts = supplement_parts or []
    parts = [llm.Pdf(pdf_bytes), *supplement_parts]
    if supplement_parts:
        note = (f"The main paper PDF is provided, along with {len(supplement_parts)} "
                "supplementary file(s) (spreadsheets/CSV/Word are included as text). ")
    else:
        note = "The main paper PDF is provided. "
    parts.append(llm.Text(note + "Assess it against the eligibility criteria, the duplicate-risk "
                                 "check, and the supplementary-data check."))
    res = llm.call(model, SYSTEM, parts, Assessment, max_tokens=8000)
    if res.parsed is not None:
        res.parsed = enforce_required(res.parsed)
    return res


# --- Local debugging helpers -----------------------------------------------

def print_assessment(a: Assessment) -> None:
    verdict = "ELIGIBLE" if a.eligible else "NOT ELIGIBLE"
    print(f"\n=== {verdict}  (confidence: {a.confidence.value}) ===\n")
    for name, c in a.checks.model_dump().items():
        tick = "✓" if c["met"] else "✗"
        req = "" if name in REQUIRED_CHECKS else "  (recorded only)"
        print(f"  {tick} {name}{req}\n      {c['evidence']}")
    print(f"\n  duplicate risk: {a.duplicate_risk.level.value}"
          + (f" — {a.duplicate_risk.evidence}" if a.duplicate_risk.evidence else ""))
    print(f"  needs supplement: {a.supplement.needed}"
          + (f" — {a.supplement.evidence}" if a.supplement.evidence else ""))
    print(f"  markers found : {', '.join(a.markers_found) or '—'}")
    print(f"  species       : {', '.join(a.species) or '—'}")
    print(f"  countries     : {', '.join(a.countries) or '—'}")
    print(f"  years         : {', '.join(str(y) for y in a.collection_years) or '—'}")
    print(f"  bioassays     : {a.has_bioassays} · geno-pheno: {a.has_genotype_phenotype}")
    print(f"  sample size   : {a.sample_size if a.sample_size is not None else '—'}")
    if a.exclusion_reasons:
        print("\n  exclusion reasons:")
        for r in a.exclusion_reasons:
            print(f"    - {r}")
    print(f"\n  summary: {a.summary}")
