"""
Load the curated target IR markers (config/target_loci.csv) and normalise the
names papers use to our canonical ones (An. gambiae numbering).

Both stages use this: eligibility checks a paper reports >=1 target marker;
extraction and the validator map every reported marker through `normalise()`.
Normalisation is done HERE, in code, rather than trusted to the LLM — e.g. a
paper's 'L1014F' (Musca domestica numbering) becomes Vgsc L995F.
"""
import csv
import re
from pathlib import Path

TARGETS_CSV = Path(__file__).resolve().parent.parent / "config" / "target_loci.csv"

_cache = None


def _key(s):
    """Loose match key: lowercase, drop spaces / '-' / '_' / '.'."""
    return re.sub(r"[\s\-_.]", "", str(s or "")).lower()


def _split(s):
    return [x.strip() for x in str(s or "").split(";") if x.strip()]


def load(path=TARGETS_CSV):
    """Return the target markers as a list of dicts, ignoring '#' comment lines."""
    global _cache
    if _cache is not None and path == TARGETS_CSV:
        return _cache
    with open(path, newline="", encoding="utf-8") as f:
        lines = [ln for ln in f if not ln.lstrip().startswith("#")]
    rows = list(csv.DictReader(lines))
    for r in rows:
        r["tier"] = int(r["tier"])
        r["gene_keys"] = {_key(r["gene"])} | {_key(a) for a in _split(r["gene_aliases"])}
        r["variant_keys"] = {_key(r["variant"])} | {_key(a) for a in _split(r["aliases"])}
    if path == TARGETS_CSV:
        _cache = rows
    return rows


def normalise(gene, marker):
    """Map a reported (gene, marker) to the target row, or None if not a target.

    Tries a gene-scoped match first (so generic aliases like 'duplication' are
    unambiguous), then a marker-only match if exactly one target fits.
    """
    loci = load()
    g, m = _key(gene), _key(marker)
    # Papers sometimes put both in one string, e.g. "kdr L1014F".
    candidates = [r for r in loci if g in r["gene_keys"]] if g else []
    for r in candidates:
        if m in r["variant_keys"] or any(m.endswith(k) and len(k) >= 4 for k in r["variant_keys"]):
            return r
    hits = [r for r in loci if m in r["variant_keys"]]
    if len({(r["gene"], r["variant"]) for r in hits}) == 1:
        return hits[0]
    return None


def canonical_gene(gene):
    """'kdr' -> 'Vgsc', 'ace1' -> 'Ace-1'; unknown names are returned unchanged."""
    g = _key(gene)
    for r in load():
        if g in r["gene_keys"]:
            return r["gene"]
    return gene


def label(row):
    return f"{row['gene']} {row['variant']}"


def summary(loci=None):
    """Compact list for prompts, with aliases, e.g.
    'Vgsc L995F (aka L1014F, kdr-west) [tier 1]; ...'."""
    loci = loci or load()
    out = []
    for r in loci:
        aka = _split(r["aliases"])
        out.append(f"{r['gene']} {r['variant']}"
                   + (f" (aka {', '.join(aka)})" if aka else "")
                   + f" [{r['variant_type']}, {r['species']}, tier {r['tier']}]")
    return "\n".join(f"  - {x}" for x in out)
