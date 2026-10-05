# IR-MarkerBase — project context for Claude Code

## What this repo is becoming
This repo started as **PfDR-MarkerBase-extract** (P. falciparum drug-resistance
extraction pipeline, Imperial). We are adapting it to **insecticide resistance (IR)
in African *Anopheles***: AI extraction of genetic-marker (and linked bioassay) data
from the literature, to feed spatial + temporal models of IR marker frequencies.

Internship project with Alfred. Owner: Ernest Katembo Muhasa.
Ernest wants to learn as we go — explain changes briefly.

## Decisions already made
- **LLM provider: Google Gemini (free tier)** instead of Anthropic. All model calls go
  through one wrapper `src/llm.py` so the provider is swappable. Respect free-tier
  rate limits (throttle + retry/backoff). Env var: `GEMINI_API_KEY`.  but you make better so that it can be adapte to each LLM API. 
- **Scope: genotypes AND phenotypes** (bioassays + genotype–phenotype association).
- **Eligibility (proposed, pending confirmation):** paper must report ≥1 target genetic
  marker in field *Anopheles*; bioassays are extracted only from those papers
  (bioassay-only papers are out — phenotype data come from IR Mapper / Vector Atlas later).
- **Geography: Africa only** (incl. Madagascar and islands).
- **Populations:** field-collected F0 or F1 progeny of field mosquitoes. Exclude lab
  colonies (e.g. Kisumu, FANG) except as noted controls (not extracted).
- **Markers:** kdr is core (tier 1); other markers extracted when present (tier 2).

## Target markers (draft — verify against MalariaGEN / Vector Atlas)
Tier 1 — Vgsc (kdr): L995F, L995S, N1570Y, I1527T, V402L, P1874S/L
Tier 2 — Ace-1 G280S (+ duplication); Rdl A296G/S; GSTe2 L119F (funestus);
Cyp6p9a/b resistance alleles (funestus); 6.5 kb SV between Cyp6p9a/b (funestus);
Cyp6aa1 duplication (gambiae/coluzzii); Cyp9k1 G454A (funestus).

**Numbering trap:** older papers use *Musca domestica* numbering
(L1014F = L995F, L1014S = L995S, N1575Y = N1570Y, G119S = G280S).
`config/target_loci.csv` needs an `aliases` column and extraction must normalise
to *An. gambiae* numbering.

## Data model (replaces STAVE study/survey/counts)
Relational, one row = one unit:
| table | one row = |
|---|---|
| `study` | one paper |
| `survey` | site × time window × species × collection method |
| `genotypes` | survey × marker (RR, RS, SS counts or allele counts; pooled flag) |
| `bioassays` | survey × insecticide × concentration × synergist (exposed, dead, timepoint) |
| `geno_pheno` | bioassay × marker × outcome (alive/dead) → RR, RS, SS |
Every table carries provenance: source quote/table, page, figure, supplement.

Rules:
- Mosquitoes are **diploid** — store genotype classes; allele freq = (2RR+RS)/2N.
- The LLM extracts **raw counts only**; derived values (frequencies, mortality %)
  are computed in code. Reported percentages go in `reported_pct` with a flag.
- Need `variant_type` (SNP / CNV / SV) and `pooled` fields.
- LLM extracts place names + any **reported** coordinates; geocoding is done in code
  (GeoNames/OSM) with a precision field. Do not let the LLM invent coordinates.
- Fields set by humans, never the LLM: `human_verified`, `coordinates_verified`.
- The full data dictionary is being written by Ernest (Step 1) — wait for it before
  finalising the Pydantic schema.

## data cleaning
clean everything related to drug resitence because now this code is for Insecticide resistence. 

## Final data extraction:
final data extraction must be in the csv file or excel contenir these columns:"there are my papers, i need you to extract  carefully these informations including their locations in papers, if there isn't information you put NA all in a table. each paper new row in the table. make sure theese information contains in these papers :
Paper/ Study ID 	DOI	PMID	Publication year	Country 	Data source	Evidence location 	Species reported	Species Complex/group	Molecular species 	Country	Samplite site 	Admin Level 1	Admin level 2	Latitude 	Longitude 	Coordonates reported or infered 	Evidence Location	Spatial precision / Uncertainty	Collection start date 	Collection end date 	Collection year	Temporal precision	Mosquito collection method	Mosquito life stage	Wild/laboratory population	Generation	Total sample size 	Insecticde name 	Pyrethroid subtype	insecticde concentration	Exposure duration 	Assay method	Assay type 	Synergit used 	Number Exposed 	Number Surviving	Number dead 	Survival proportion	Mortality proportion	Phenotype	Mortality Assessment time	Gene 	Variant/marker	Amino-acid change	Nucleotide change	Resistant allele	Genotyping method	Number genotyped	Resistant allele count	Allele frequency 	Homozygous resistant(RR)	Heterozygous(RS)	Homozygous susceptible (SS)	RR Frequency	RS frequency 	SS frequency	Phenotype group	VGSC variant in survivors	VGSC Variant in dead moquitoes	RR Survivors	RS survivors 	SS survivors	RR dead 	RS dead 	SS dead 	Coordinates verified 	Species identification method	sample size reported	Raw counts available	AI extraction confidence	Human verified 	source sentence/table 	page number	figure number	supplementary material

## Work plan
0. ✅ Scope confirmed (above).
1. Data dictionary (Ernest drafting `survey` + `genotypes` first).
2. Gold-standard set: 10–20 papers extracted by hand (mix easy/hard, incl. DRC / Great Lakes).
3. Adapt pipeline:
   a. `src/llm.py` Gemini wrapper (PDF input + structured output via Pydantic schema);
      replace `client.messages.parse` in `eligibility.py` / `extraction.py`, adapt
      content blocks in `supplements.py`, update `pricing.py` (free tier ≈ $0).
   b. New `config/target_loci.csv` (gene, variant, aliases, variant_type, species, tier).
   c. Rewrite eligibility criteria for *Anopheles* / Africa / IR markers.
   d. Rewrite extraction schema + writers for the 5 tables.
   e. Replace `stave_validate.R` with a Python validator (RR+RS+SS = N, dead ≤ exposed,
      survey_ids link, markers in target list, ...). Keep the repair loop.
   f. Update workflows/secrets (`GEMINI_API_KEY`), README, docs/NOTES.md.
4. Evaluate on gold set: field-level precision/recall; iterate prompts.
5. Systematic search (PubMed / Web of Science) → Drive → full run.
Then Point 2: merge with IR Mapper, Vector Atlas, MalariaGEN Vector Observatory.

## Repo conventions to keep
- `roster.csv` single state machine; bot-owned vs human-owned files never overlap.
- Never commit paper PDFs or full paper text; secrets stay outside the repo.
- The existing `data/` (Pf papers) is from the old project — archive or clear it
  before running on IR papers.
