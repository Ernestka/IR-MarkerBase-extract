"""
The guardrail outside the LLM (replaces the old STAVE R validator).

`check(extraction)` returns (errors, warnings):
  errors   — the extraction is wrong/inconsistent; fed back to the model for a
             repair attempt (run_extraction.extract_one). Hitting the retry
             limit sets EXTRACTION_FAILED.
  warnings — worth a human look but not blocking; written to the study README.

Deterministic, no LLM, no network.
"""
import re
import unicodedata

import targets

# Rough bounding box for Africa incl. Madagascar, Cabo Verde, Mauritius, Seychelles.
LAT_RANGE = (-36.0, 38.0)
LON_RANGE = (-26.0, 64.0)

AFRICAN_COUNTRIES = {
    "algeria", "angola", "benin", "botswana", "burkina faso", "burundi", "cabo verde",
    "cape verde", "cameroon", "central african republic", "car", "chad", "comoros", "congo",
    "republic of the congo", "republic of congo", "congo-brazzaville", "congo brazzaville",
    "democratic republic of the congo", "democratic republic of congo", "dr congo", "drc",
    "congo-kinshasa", "cote d'ivoire", "ivory coast", "djibouti", "egypt", "equatorial guinea",
    "bioko", "eritrea", "eswatini", "swaziland", "ethiopia", "gabon", "gambia", "the gambia",
    "ghana", "guinea", "guinea-bissau", "guinea bissau", "kenya", "lesotho", "liberia", "libya",
    "madagascar", "malawi", "mali", "mauritania", "mauritius", "mayotte", "morocco",
    "mozambique", "namibia", "niger", "nigeria", "reunion", "rwanda", "sao tome and principe",
    "sao tome", "senegal", "seychelles", "sierra leone", "somalia", "somaliland",
    "south africa", "south sudan", "sudan", "tanzania", "united republic of tanzania",
    "zanzibar", "togo", "tunisia", "uganda", "western sahara", "zambia", "zimbabwe",
}

INSECTICIDE_CLASSES = {"pyrethroid", "organophosphate", "carbamate", "organochlorine",
                       "neonicotinoid", "pyrrole", "insecticide"}

DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")


def _norm_country(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", s.replace("’", "'")).strip().lower()


def _nonneg(errors, where, **vals):
    for k, v in vals.items():
        if v is not None and v < 0:
            errors.append(f"{where}: {k} is negative ({v})")


def _sink(rec, errors, warnings):
    """Where a count mismatch goes. The extractor must keep printed values as they
    are; if it flagged the record (inconsistency_note), the mismatch is the paper's
    and a human decides — a warning. Unflagged, it is probably a misreading — an
    error, sent back for repair."""
    return warnings if rec.inconsistency_note else errors


def _flagged(where, rec, warnings):
    if rec.inconsistency_note:
        warnings.append(f"{where}: inconsistent in the paper (values kept as printed) — "
                        f"{rec.inconsistency_note}")


def _classes(where, rr, rs, ss, n, sink, n_name="n_genotyped"):
    if None not in (rr, rs, ss) and n is not None and rr + rs + ss != n:
        sink.append(f"{where}: RR+RS+SS = {rr}+{rs}+{ss} = {rr + rs + ss} but {n_name} = {n}")


def _carriers(where, rec, n, sink):
    c = rec.n_carriers
    if c is None:
        return
    if n is not None and c > n:
        sink.append(f"{where}: n_carriers {c} > {n} tested")
    if rec.rr is not None and rec.rs is not None and c != rec.rr + rec.rs:
        sink.append(f"{where}: n_carriers {c} != RR+RS = {rec.rr + rec.rs}")


def check(ex):
    errors, warnings = [], []

    # --- surveys
    survey_ids = [s.survey_id for s in ex.surveys]
    dups = {i for i in survey_ids if survey_ids.count(i) > 1}
    if dups:
        errors.append(f"duplicate survey_id(s): {sorted(dups)}")
    if not ex.surveys:
        errors.append("no surveys extracted")
    for s in ex.surveys:
        w = f"survey {s.survey_id}"
        if _norm_country(s.country) not in AFRICAN_COUNTRIES:
            warnings.append(f"{w}: country '{s.country}' not recognised as African")
        lat, lon = s.latitude_reported, s.longitude_reported
        if (lat is None) != (lon is None):
            errors.append(f"{w}: only one of latitude/longitude given")
        if lat is not None and lon is not None:
            if not (LAT_RANGE[0] <= lat <= LAT_RANGE[1] and LON_RANGE[0] <= lon <= LON_RANGE[1]):
                errors.append(f"{w}: coordinates ({lat}, {lon}) are outside Africa — check sign "
                              "(S/W negative) and DMS conversion")
            if not (s.coordinates_provenance and (s.coordinates_provenance.source_text
                                                  or s.coordinates_provenance.table)):
                warnings.append(f"{w}: coordinates given without provenance — were they stated in "
                                "the paper?")
        for name, d in (("collection_start", s.collection_start), ("collection_end", s.collection_end)):
            if d and not DATE_RE.match(d):
                errors.append(f"{w}: {name} '{d}' must be YYYY, YYYY-MM or YYYY-MM-DD")
        if (s.collection_start and s.collection_end and DATE_RE.match(s.collection_start)
                and DATE_RE.match(s.collection_end) and s.collection_start[:len(s.collection_end)]
                > s.collection_end[:len(s.collection_start)]):
            errors.append(f"{w}: collection_start {s.collection_start} is after "
                          f"collection_end {s.collection_end}")
        if s.population_type.value == "laboratory":
            warnings.append(f"{w}: laboratory population — normally excluded")
        _nonneg(errors, w, total_sample_size=s.total_sample_size)

    # --- genotypes
    seen = set()
    for i, g in enumerate(ex.genotypes):
        w = f"genotype #{i + 1} ({g.survey_id}, {g.gene} {g.marker})"
        if g.survey_id not in survey_ids:
            errors.append(f"{w}: survey_id not found among surveys")
        t = targets.normalise(g.gene, g.marker)
        if t is None:
            errors.append(f"{w}: '{g.gene} {g.marker}' is not a target marker — drop it, or name it "
                          "as in the target list if it is one")
        else:
            key = (g.survey_id, t["gene"], t["variant"])
            if key in seen:
                errors.append(f"{w}: duplicate genotype record for {targets.label(t)} in this survey "
                              "(double counting?)")
            seen.add(key)
        _nonneg(errors, w, n_genotyped=g.n_genotyped, rr=g.rr, rs=g.rs, ss=g.ss,
                n_carriers=g.n_carriers, resistant_allele_count=g.resistant_allele_count)
        _flagged(w, g, warnings)
        _classes(w, g.rr, g.rs, g.ss, g.n_genotyped, _sink(g, errors, warnings))
        _carriers(w, g, g.n_genotyped, _sink(g, errors, warnings))
        if (not g.pooled and g.resistant_allele_count is not None and g.n_genotyped
                and t and t["variant_type"] == "SNP" and g.resistant_allele_count > 2 * g.n_genotyped):
            _sink(g, errors, warnings).append(
                f"{w}: resistant_allele_count {g.resistant_allele_count} > 2 x n_genotyped")
        if g.reported_allele_freq is not None and not 0 <= g.reported_allele_freq <= 1:
            errors.append(f"{w}: reported_allele_freq {g.reported_allele_freq} must be a 0-1 proportion")
        has_counts = any(v is not None for v in (g.rr, g.rs, g.ss, g.n_carriers,
                                                 g.resistant_allele_count))
        if not has_counts and g.reported_allele_freq is None:
            errors.append(f"{w}: no counts and no reported frequency — empty record (if the paper "
                          "gives only how many mosquitoes carry the mutation, use n_carriers)")
        if not has_counts and g.reported_allele_freq is not None:
            warnings.append(f"{w}: frequency only (no raw counts)")
        if None not in (g.rr, g.rs, g.ss) and g.reported_allele_freq is not None:
            n = g.rr + g.rs + g.ss
            if n and abs((2 * g.rr + g.rs) / (2 * n) - g.reported_allele_freq) > 0.02:
                warnings.append(f"{w}: computed allele freq {(2 * g.rr + g.rs) / (2 * n):.3f} differs "
                                f"from reported {g.reported_allele_freq}")
        if not g.provenance.page and not g.provenance.table and not g.provenance.supplement:
            warnings.append(f"{w}: no page/table/supplement provenance")

    # --- bioassays
    bio_ids = [b.bioassay_id for b in ex.bioassays]
    dups = {i for i in bio_ids if bio_ids.count(i) > 1}
    if dups:
        errors.append(f"duplicate bioassay_id(s): {sorted(dups)}")
    bio = {b.bioassay_id: b for b in ex.bioassays}
    for b in ex.bioassays:
        w = f"bioassay {b.bioassay_id}"
        if b.survey_id not in survey_ids:
            errors.append(f"{w}: survey_id '{b.survey_id}' not found among surveys")
        _nonneg(errors, w, n_exposed=b.n_exposed, n_dead=b.n_dead, n_alive=b.n_alive)
        _flagged(w, b, warnings)
        sink = _sink(b, errors, warnings)
        if b.n_exposed is not None and b.n_dead is not None and b.n_dead > b.n_exposed:
            sink.append(f"{w}: n_dead {b.n_dead} > n_exposed {b.n_exposed}")
        if None not in (b.n_exposed, b.n_dead, b.n_alive) and b.n_dead + b.n_alive != b.n_exposed:
            sink.append(f"{w}: n_dead + n_alive = {b.n_dead + b.n_alive} but n_exposed = {b.n_exposed}")
        if b.reported_mortality_pct is not None and not 0 <= b.reported_mortality_pct <= 100:
            errors.append(f"{w}: reported_mortality_pct {b.reported_mortality_pct} outside 0-100")
        if b.n_exposed and b.n_dead is not None and b.reported_mortality_pct is not None:
            comp = 100 * b.n_dead / b.n_exposed
            if abs(comp - b.reported_mortality_pct) > 2:
                warnings.append(f"{w}: computed mortality {comp:.1f}% differs from reported "
                                f"{b.reported_mortality_pct}% (Abbott correction?)")
        if b.n_exposed is None and b.reported_mortality_pct is None:
            errors.append(f"{w}: neither n_exposed nor reported mortality — empty record")

    for b in ex.bioassays:
        if _norm_country(b.insecticide).rstrip("s") in INSECTICIDE_CLASSES:
            errors.append(f"bioassay {b.bioassay_id}: insecticide '{b.insecticide}' is a class, not a "
                          "compound — give the specific insecticide (one record each), or drop it if "
                          "the paper only reports a pooled result")

    # --- double counting: the same mosquitoes in genotypes AND geno_pheno
    gp_n = {}
    for gp in ex.geno_pheno:
        t = targets.normalise(gp.gene, gp.marker)
        if t and gp.n is not None:
            key = (gp.survey_id, t["gene"], t["variant"])
            gp_n[key] = gp_n.get(key, 0) + gp.n
    for i, g in enumerate(ex.genotypes):
        t = targets.normalise(g.gene, g.marker)
        n = g.n_genotyped or (sum(x for x in (g.rr, g.rs, g.ss) if x is not None) or None)
        if t and n and gp_n.get((g.survey_id, t["gene"], t["variant"])) == n:
            errors.append(f"genotype #{i + 1} ({g.survey_id}, {g.gene} {g.marker}): these {n} mosquitoes "
                          "are the same ones already in geno_pheno (alive + dead) — remove this genotype "
                          "row to avoid double counting")

    # --- genotype x phenotype
    for i, gp in enumerate(ex.geno_pheno):
        test = gp.bioassay_id or gp.insecticide or "no insecticide"
        w = f"geno_pheno #{i + 1} ({test}, {gp.gene} {gp.marker}, {gp.phenotype_group.value})"
        if gp.survey_id not in survey_ids:
            errors.append(f"{w}: survey_id '{gp.survey_id}' not found among surveys")
        b = bio.get(gp.bioassay_id) if gp.bioassay_id else None
        if gp.bioassay_id and not b:
            errors.append(f"{w}: bioassay_id not found among bioassays — use an existing one, or "
                          "null + `insecticide` if these mosquitoes are pooled across tests")
        if b and b.survey_id != gp.survey_id:
            errors.append(f"{w}: survey_id '{gp.survey_id}' differs from its bioassay's survey "
                          f"'{b.survey_id}'")
        if not gp.bioassay_id:
            warnings.append(f"{w}: not linked to a single bioassay (insecticide as reported: "
                            f"{gp.insecticide or 'none given'})")
        if targets.normalise(gp.gene, gp.marker) is None:
            errors.append(f"{w}: '{gp.gene} {gp.marker}' is not a target marker")
        _nonneg(errors, w, rr=gp.rr, rs=gp.rs, ss=gp.ss, n=gp.n, n_carriers=gp.n_carriers)
        _flagged(w, gp, warnings)
        _classes(w, gp.rr, gp.rs, gp.ss, gp.n, _sink(gp, errors, warnings), n_name="n")
        _carriers(w, gp, gp.n, _sink(gp, errors, warnings))
        if gp.reported_allele_freq is not None and not 0 <= gp.reported_allele_freq <= 1:
            errors.append(f"{w}: reported_allele_freq {gp.reported_allele_freq} must be a 0-1 proportion")
        if all(v is None for v in (gp.rr, gp.rs, gp.ss, gp.n_carriers, gp.reported_allele_freq)):
            errors.append(f"{w}: no genotype counts and no reported frequency — empty record")
        if b and gp.n is not None:
            cap = b.n_alive if gp.phenotype_group.value == "alive" else b.n_dead
            if cap is not None and gp.n > cap:
                warnings.append(f"{w}: n = {gp.n} genotyped exceeds {cap} {gp.phenotype_group.value} "
                                "in the bioassay (different bioassay?)")

    return errors, warnings


def format_errors(errors, limit=40):
    out = errors[:limit]
    if len(errors) > limit:
        out.append(f"... and {len(errors) - limit} more")
    return "\n".join(f"- {e}" for e in out)
