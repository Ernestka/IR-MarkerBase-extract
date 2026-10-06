"""
Code-side enrichment of an extracted study — things the LLM must NOT do:

  - PMID      looked up from the DOI in Europe PMC (study.yaml: pmid, pmid_source)
  - geocoding surveys WITHOUT reported coordinates get inferred ones from
              OpenStreetMap Nominatim, from the place names the paper gives
              (surveys.csv: latitude_geocoded, longitude_geocoded, geocode_level,
              geocode_query, geocode_source)

Reported coordinates are never touched. Every geocode says which query matched
and at what level (village / town / admin2 / admin1), so a human can check it —
`Coordinates verified` stays FALSE until they do.

Nominatim's usage policy: max 1 request/s and an identifying User-Agent. Answers
are cached in data/geocode_cache.json (bot-owned; local runs use their own
output folder), so each place is asked once.
Network problems never fail an extraction: the step is skipped and can be re-run.

Run standalone (backfill every extracted study):  python src/enrich.py [extracted_dir]
"""
import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
EXTRACTED = ROOT / "data" / "extracted"
CACHE = ROOT / "data" / "geocode_cache.json"
USER_AGENT = "IR-MarkerBase-extract/0.1 (insecticide-resistance research pipeline)"
GEO_COLS = ["latitude_geocoded", "longitude_geocoded", "geocode_level", "geocode_query",
            "geocode_source"]

ISO2 = {
    "algeria": "dz", "angola": "ao", "benin": "bj", "botswana": "bw", "burkina faso": "bf",
    "burundi": "bi", "cabo verde": "cv", "cape verde": "cv", "cameroon": "cm",
    "central african republic": "cf", "chad": "td", "comoros": "km", "congo": "cg",
    "republic of the congo": "cg", "republic of congo": "cg", "congo-brazzaville": "cg",
    "democratic republic of the congo": "cd", "democratic republic of congo": "cd",
    "dr congo": "cd", "drc": "cd", "congo-kinshasa": "cd", "cote d'ivoire": "ci",
    "ivory coast": "ci", "djibouti": "dj", "egypt": "eg", "equatorial guinea": "gq",
    "bioko": "gq", "eritrea": "er", "eswatini": "sz", "swaziland": "sz", "ethiopia": "et",
    "gabon": "ga", "gambia": "gm", "the gambia": "gm", "ghana": "gh", "guinea": "gn",
    "guinea-bissau": "gw", "guinea bissau": "gw", "kenya": "ke", "lesotho": "ls",
    "liberia": "lr", "libya": "ly", "madagascar": "mg", "malawi": "mw", "mali": "ml",
    "mauritania": "mr", "mauritius": "mu", "mayotte": "yt", "morocco": "ma",
    "mozambique": "mz", "namibia": "na", "niger": "ne", "nigeria": "ng", "reunion": "re",
    "rwanda": "rw", "sao tome and principe": "st", "sao tome": "st", "senegal": "sn",
    "seychelles": "sc", "sierra leone": "sl", "somalia": "so", "somaliland": "so",
    "south africa": "za", "south sudan": "ss", "sudan": "sd", "tanzania": "tz",
    "united republic of tanzania": "tz", "zanzibar": "tz", "togo": "tg", "tunisia": "tn",
    "uganda": "ug", "zambia": "zm", "zimbabwe": "zw",
}

# Nominatim addresstype -> our spatial precision levels.
LEVEL = {
    "village": "village", "hamlet": "village", "isolated_dwelling": "village",
    "locality": "village", "neighbourhood": "village", "suburb": "village", "quarter": "village",
    "town": "town", "city": "town", "municipality": "town", "city_district": "town",
    "county": "admin2", "district": "admin2", "state_district": "admin2", "subdistrict": "admin2",
    "state": "admin1", "province": "admin1", "region": "admin1",
    "country": "country",
}


def _norm(s):
    import validate
    return validate._norm_country(s)


# --- HTTP ---------------------------------------------------------------------

_last = [0.0]


def _get_json(url, min_interval=1.1):
    wait = _last[0] + min_interval - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    _last[0] = time.monotonic()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


# --- PMID ---------------------------------------------------------------------

def pmid_for_doi(doi):
    """PMID from Europe PMC for an exact DOI match, else None."""
    doi = (doi or "").strip().lower().removeprefix("https://doi.org/")
    if not doi:
        return None
    q = urllib.parse.quote(f'DOI:"{doi}"')
    data = _get_json("https://www.ebi.ac.uk/europepmc/webservices/rest/search"
                     f"?query={q}&format=json&resultType=lite", min_interval=0.2)
    for r in data.get("resultList", {}).get("result", []):
        if (r.get("doi") or "").lower() == doi and r.get("pmid"):
            return str(r["pmid"])
    return None


# --- Geocoding ----------------------------------------------------------------

def cache_path(extracted_dir):
    """data/extracted -> data/geocode_cache.json (local runs keep their own)."""
    return Path(extracted_dir).parent / CACHE.name


def _load_cache(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _save_cache(cache, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, indent=1, sort_keys=True, ensure_ascii=False) + "\n",
                    encoding="utf-8")


def _nominatim(query, cc, cache):
    """Up to 5 candidate places for a query, restricted to one country (cached)."""
    key = f"{cc}|{query}"
    if key not in cache:
        url = ("https://nominatim.openstreetmap.org/search?format=jsonv2&limit=5"
               f"&countrycodes={cc}&q={urllib.parse.quote(query)}")
        cache[key] = [{"lat": round(float(h["lat"]), 5), "lon": round(float(h["lon"]), 5),
                       "level": LEVEL.get(h.get("addresstype"), h.get("addresstype") or "unknown"),
                       "name": h.get("display_name")} for h in _get_json(url)]
    return cache[key]


def _queries(s):
    """Most to least specific (query, kind) pairs for one survey row. kind 'site' =
    the query starts with the sampling site; 'admin' = only admin units."""
    site, a2, a1 = ((s.get(k) or "").strip() for k in ("site_name", "admin2", "admin1"))
    out = []
    for parts, kind in (((site, a2, a1), "site"), ((site, a1), "site"), ((site,), "site"),
                        ((a2, a1), "admin"), ((a2,), "admin"), ((a1,), "admin")):
        if parts[0]:
            q = ", ".join(dict.fromkeys(p for p in parts if p))
            if (q, kind) not in out:
                out.append((q, kind))
    return out


def _fits(level, kind, precision):
    """Is a candidate at `level` the right KIND of place? A county must not match a
    town of the same name (and vice versa), or the point lands in the wrong place."""
    if kind == "admin":
        return level in ("admin1", "admin2")
    if precision in ("admin1", "admin2"):          # the 'site' is itself an admin unit
        return level == precision
    return level in ("village", "town")


def geocode_survey(s, cache):
    """-> dict of GEO_COLS (empty values if not found / not needed)."""
    blank = {c: "" for c in GEO_COLS}
    if s.get("latitude_reported") not in (None, ""):
        return blank                                    # the paper's own coordinates win
    cc = ISO2.get(_norm(s.get("country")))
    precision = s.get("spatial_precision")
    if not cc or precision == "country":
        return blank
    for q, kind in _queries(s):
        for h in _nominatim(q, cc, cache):
            if _fits(h["level"], kind, precision):
                return {"latitude_geocoded": h["lat"], "longitude_geocoded": h["lon"],
                        "geocode_level": h["level"], "geocode_query": q,
                        "geocode_source": f"OSM Nominatim: {h['name']}"}
    return blank


# --- One study folder ---------------------------------------------------------

def enrich_study(folder, cache=None):
    """Fill PMID and geocodes for one data/extracted/<id>/ folder. Returns a short
    summary string. Never raises on network errors."""
    folder = Path(folder)
    own_cache = cache is None
    cpath = cache_path(folder.parent)
    cache = _load_cache(cpath) if own_cache else cache
    notes = []

    sy = folder / "study.yaml"
    study = yaml.safe_load(sy.read_text(encoding="utf-8")) or {}
    # Always checked against the DOI: a PMID the LLM gave could be invented.
    if study.get("doi") and not study.get("pmid_source"):
        try:
            pmid = pmid_for_doi(study["doi"])
            if pmid:
                if study.get("pmid") and str(study["pmid"]) != pmid:
                    notes.append(f"PMID {study['pmid']} from the model replaced by {pmid}")
                study.update(pmid=pmid, pmid_source="Europe PMC (from DOI)")
                sy.write_text(yaml.safe_dump(study, sort_keys=False, allow_unicode=True),
                              encoding="utf-8")
                notes.append(f"PMID {pmid}")
        except Exception as e:                          # network: skip, re-run later
            notes.append(f"PMID lookup skipped ({type(e).__name__})")

    sv = folder / "surveys.csv"
    if sv.exists():
        with sv.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            cols, rows = list(reader.fieldnames or []), list(reader)
        cols += [c for c in GEO_COLS if c not in cols]
        n = 0
        try:
            for s in rows:
                if not s.get("latitude_geocoded"):
                    s.update(geocode_survey(s, cache))
                    n += bool(s.get("latitude_geocoded"))
        except Exception as e:
            notes.append(f"geocoding stopped ({type(e).__name__})")
        with sv.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        if n:
            notes.append(f"{n} survey(s) geocoded")
    if own_cache:
        _save_cache(cache, cpath)
    return "; ".join(notes) or "nothing to add"


def main():
    extracted = Path(sys.argv[1]) if len(sys.argv) > 1 else EXTRACTED
    cache = _load_cache(cache_path(extracted))
    for folder in sorted(p for p in extracted.glob("*") if (p / "study.yaml").exists()):
        print(f"{folder.name}: {enrich_study(folder, cache)}")
    _save_cache(cache, cache_path(extracted))


if __name__ == "__main__":
    main()
