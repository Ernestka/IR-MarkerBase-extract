# IR MarkerBase — extraction pipeline

A pipeline that builds a database of **insecticide-resistance (IR) markers in
African *Anopheles*** from the literature: genotype counts at target markers
(kdr/Vgsc, Ace-1, Rdl, GSTe2, Cyp6p9a/b, Cyp6aa1, Cyp9k1) plus linked bioassays
and genotype–phenotype data, for spatial and temporal models of marker frequencies.

PDFs go into a Google Drive folder (or a local folder for testing). The pipeline
reads each one, decides whether it is eligible, extracts the data with an LLM,
checks it in code, and builds one combined table.

_Adapted from PfDR-MarkerBase-extract (P. falciparum drug resistance). The old
Pf data is preserved in git history (commit `7acfa7c`)._

## Status

![pipeline status](docs/stats.svg)

<sub>Updates automatically on every run.</sub>

## Roster

<!-- ROSTER:START -->

**19 paper(s) · estimated spend $0.00** (eligibility $0.00 · extraction $0.00) · updated 2026-10-08

| id | source | status | eligible | confidence | duplicate_risk | needs_supplement | spec_version | first_seen | last_assessed | supp_attempts | supplement_fp | elig_model | elig_tok_in | elig_tok_out | extract_model | extract_tok_in | extract_tok_out | notes | est_$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1-s2.0-S0001706X19317632-main | master | EXTRACTED | True | high | none | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 5472 | 3401 | gemini:gemini-3.5-flash | 27742 | 56306 | 10 survey(s), 21 genotype, 19 bioassay, 0 geno-pheno rows; 23 warning(s) | 0.0000 |
| 1756-3305-5-127 | master | EXTRACTED | True | high | none | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 6552 | 3606 | gemini:gemini-3.5-flash | 8246 | 37022 | 6 survey(s), 11 genotype, 37 bioassay, 0 geno-pheno rows | 0.0000 |
| 1756-3305-6-352 | master | EXTRACTED | True | high | low | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 8172 | 1632 | gemini:gemini-3.5-flash | 9816 | 31601 | 10 survey(s), 6 genotype, 8 bioassay, 7 geno-pheno rows | 0.0000 |
| Newpaper | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 9492 | 1967 |  |  |  |  | 0.0000 |
| file | master | EXTRACTED | True | high | low | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 7932 | 5837 | gemini:gemini-3.5-flash | 9624 | 17765 | 3 survey(s), 3 genotype, 0 bioassay, 0 geno-pheno rows; 3 warning(s) | 0.0000 |
| isabelleborloz,+5362_NTONGA_AKONO | master | EXTRACTED | True | high | low | False | 1 | 2026-10-05 | 2026-10-05 | 0 |  | gemini:gemini-3.5-flash | 6861 | 3893 | gemini:gemini-3.5-flash | 8696 | 16853 | 2 survey(s), 0 genotype, 12 bioassay, 4 geno-pheno rows; 4 warning(s) | 0.0000 |
| jmedent40-0195 | master | ELIGIBLE | True | high | none | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 3820 | 3030 |  |  |  |  | 0.0000 |
| journal.pone.0332497 | master | AWAIT_SUPPLEMENT | True | high | low | True | 1 | 2026-10-05 | 2026-10-05 | 0 |  | gemini:gemini-3.5-flash | 7781 | 3736 |  |  |  |  | 0.0000 |
| molecules-27-06343 | master | AWAIT_SUPPLEMENT | True | high | low | True | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 9140 | 4250 |  |  |  |  | 0.0000 |
| s12889-019-7767-0 | master | ELIGIBLE | True | high | low | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 7632 | 3442 |  |  |  |  | 0.0000 |
| s12936-017-2156-6 | master | ELIGIBLE | True | high | low | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 6552 | 2884 |  |  |  |  | 0.0000 |
| s12936-018-2285-6 | master | ELIGIBLE | True | high | low | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 8712 | 3589 |  |  |  |  | 0.0000 |
| s12936-021-03606-4 | master | EXTRACTED | True | high | none | False | 1 | 2026-10-05 | 2026-10-05 | 0 |  | gemini:gemini-3.5-flash | 9101 | 4765 | gemini:gemini-3.5-flash | 10905 | 13432 | 1 survey(s), 2 genotype, 1 bioassay, 0 geno-pheno rows | 0.0000 |
| s12936-025-05696-w | master | INELIGIBLE | False | high | low | False | 1 | 2026-10-05 | 2026-10-05 | 0 |  | gemini:gemini-3.5-flash | 7481 | 2103 |  |  |  |  | 0.0000 |
| s13071-014-0500-z | master | INELIGIBLE | False | high | high | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 7092 | 4440 |  |  |  |  | 0.0000 |
| s13071-016-1923-5 | master | ELIGIBLE | True | high | none | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 6012 | 5172 |  |  |  |  | 0.0000 |
| s13071-017-2361-8 | master | INELIGIBLE | False | high | high | False | 1 | 2026-10-06 | 2026-10-06 | 0 |  | gemini:gemini-3.6-flash | 8712 | 2091 |  |  |  |  | 0.0000 |
| s13071-021-04706-5 | master | EXTRACTION_FAILED | True | high | none | False | 1 | 2026-10-05 | 2026-10-05 | 0 |  | gemini:gemini-3.5-flash | 6941 | 1706 |  | 0 | 0 | extractor error: Server disconnected without sending a response. | 0.0000 |
| s13071-021-04833-z | master | ELIGIBLE | True | high | low | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 7092 | 3784 |  |  |  |  | 0.0000 |

_The table above is a static snapshot. For a searchable, filterable view (paginated for large sets), open [`data/roster.csv`](data/roster.csv) — GitHub renders CSV files as an interactive table._

<!-- ROSTER:END -->

## How it works

**Stage 1 — eligibility.** Each new PDF is checked against the spec in
`src/eligibility.py`: *Anopheles*; ≥1 target marker (`config/target_loci.csv`);
extractable genotype counts; field-collected (F0/F1) African mosquitoes; primary
study. Sub-country location and ≤3-year time window are recorded but not required.
Papers become *eligible*, *ineligible*, or **flagged** (possible duplicate /
needs supplementary files).

**Stage 2 — extraction.** For eligible papers the LLM fills five linked tables
(`study`, `surveys`, `genotypes`, `bioassays`, `geno_pheno`). It gives **raw counts
and text as reported**, with provenance (sentence/table, page, figure, supplement)
on every record. Then code:

- maps marker names to *An. gambiae* numbering (`L1014F` → `Vgsc L995F`);
- validates the data (`src/validate.py`: RR+RS+SS = N, dead ≤ exposed, IDs link,
  markers are targets, coordinates in Africa…), sending errors back to the LLM
  for repair;
- looks up the PMID from the DOI (Europe PMC) and geocodes sites that have no
  printed coordinates (OpenStreetMap; `src/enrich.py`) — the LLM never does either;
- computes every derived value (allele/genotype frequencies, mortality, WHO
  phenotype, pyrethroid subtype…) and writes the final table
  **`data/final/ir_extraction.csv` / `.xlsx`** (`src/export.py`).

**LLM provider.** All model calls go through `src/llm.py`. The default is Google
Gemini (free tier, throttled and retried). Claude and OpenAI-compatible models
work by changing the model spec, e.g. `--model sonnet`.

## How to use it

**1. Add papers.** Upload PDFs to Google Drive → `IR_papers/master/` (or a
contributor's subfolder). Name each one uniquely, ideally `PMID_<number>.pdf` —
the name becomes the paper's ID everywhere.

**2. Start it.** GitHub's 4-hourly schedule is best-effort (often hours late), so
start a run yourself after adding papers — **Actions → Pipeline → Run workflow**,
or from a terminal in this folder (one-time: `sudo apt install gh && gh auth login`):

```bash
gh workflow run pipeline.yml                     # start (add -f max_papers=40 for big batches)
gh run watch                                     # follow it until it finishes
git pull                                         # get the results
```

Each run checks eligibility of new papers, then extracts every eligible one (15
per stage by default). The Gemini free tier allows a few dozen papers a day; when
the daily quota runs out the run stops cleanly — start another run the next day
and it continues where it stopped.

**3. Get the results.** Download **`data/final/ir_extraction.xlsx`** from the repo
(or `git pull`). One row per data point (`Record type` = genotype / bioassay /
geno_pheno), with page/table provenance for every number. Per-paper details and
the model's decisions are in `data/extracted/<id>/README.md`.

**4. Handle what needs you.** Every Friday a GitHub issue lists papers waiting on
you:
- **AWAIT_SUPPLEMENT** — upload the supplementary files to Drive →
  `IR_supplements/master/<paper id>/`; the next run picks them up.
- **REVIEW_DUPLICATE** — add `id: duplicate` or `id: unique` to
  `data/duplicate_decisions.yaml`.
- **EXTRACTION_FAILED** — see `data/extracted/<id>/EXTRACTION_FAILED.md`.

To skip a paper entirely, add its ID to `data/exclude.txt`. To re-extract a paper,
change its status in `data/roster.csv` back to `ELIGIBLE`.

**Status of every paper:** `data/roster.csv` (GitHub shows it as a searchable table).

## Running on your own computer (optional)

Edit on GitHub or `git pull` before working locally — the bot commits to `data/`
after every run. Local runs need a `.env` file with `GEMINI_API_KEY` (and the Drive
settings to use Drive); check it with `python src/check_setup.py`.

```bash
.venv/bin/python src/run_local.py papers/   # a local folder of PDFs → local_output/
```

## Checking accuracy against a gold standard

1. `.venv/bin/python src/evaluate.py --template gold.xlsx` — an empty sheet with
   the final-table columns.
2. Extract your gold papers by hand into it: one row per data point, as in the
   final table (genotype, bioassay or geno-pheno row). Leave unreported cells empty.
3. Run the pipeline on the same PDFs (`src/run_local.py gold_papers/ --skip-eligibility`), then
   `.venv/bin/python src/evaluate.py gold.xlsx local_output/final/ir_extraction.csv`.

It prints, per record type, how many of your rows were found (recall) and how
many extracted rows are real (precision), and per column how often the value is
right. Every disagreement is listed in `local_output/eval/eval_mismatches.csv`.

## What humans edit

- `config/target_loci.csv` — the target markers and their aliases.
- `data/exclude.txt` — papers to skip.
- `data/duplicate_decisions.yaml` — `duplicate` / `unique` rulings on flagged papers.
- `Human verified` / `Coordinates verified` columns are for humans only; the
  pipeline always writes `FALSE`.

## More detail

Design notes, the file and secret reference, and how Drive access works:
**[docs/NOTES.md](docs/NOTES.md)**.
