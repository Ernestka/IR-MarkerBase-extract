# IR MarkerBase pipeline — notes

## How the Google Drive access works

There are **two separate worlds**, linked by one deliberate act:

- **Google Cloud** — where *automation* lives (the robot identity + its credentials).
- **Google Drive** — where the *data* (PDFs) lives.

The Cloud project does **not** contain your Drive. They are connected **only** by
**sharing a folder** with the robot's email. Without that share, the robot is a
valid identity that can see none of your files.

### The elements

| Element | What it is | Analogy |
|---|---|---|
| Google account (`<project-account>@gmail.com`) | A *human* login that owns things | You, the person |
| Cloud project (`<your-project>`) | Container for APIs + identities you create | A company you registered |
| Drive API (enabled) | Switch allowing the project to talk to Drive | Permission to do Drive work at all |
| Service account (`markerbase-reader`) | A *non-human* robot identity scripts log in as | A robot employee you hired |
| Service-account email | The robot's address; how Drive grants it access | The name on the room's access list |
| JSON key file | The robot's credential ("this script IS that robot") | The employee's keycard |
| Scope (`drive.readonly`) | What the robot may do — read only | A read-only badge |
| Drive folder (`inbox_test`) | A normal folder holding the PDFs | A room you own |
| The share (folder → robot, Viewer) | Adds the robot to that folder's access list | Putting the robot on the entry list |

### How they nest

```
YOUR GOOGLE ACCOUNT  (a human login)
│
├── GOOGLE CLOUD
│     └── Project: <your-project>
│           ├── Drive API: ENABLED
│           └── Service account: markerbase-reader
│                 ├── email:  markerbase-reader@<your-project>.iam.gserviceaccount.com  ← its "name"
│                 └── JSON key (downloaded)          ← its "password"
│
└── GOOGLE DRIVE
      └── Folder: <inbox folder>
            ├── example.pdf
            └── Shared with → markerbase-reader@…  (Viewer)   ← THE LINK
```

(The project and the Drive can even live on different Google accounts — they're
only ever linked by the share. The real project ID, service-account email, and
folder ID are kept out of this public repo — they live in your local env vars
and GitHub secrets.)

### The key idea: identity vs. access

Two separate questions, both must be true:

- **Authentication — "who is making this request?"** → answered by the **JSON key**.
- **Authorization — "is that identity allowed to see this folder?"** → answered by the **share**.

The key proves *who*; the share grants *what*. Neither alone is enough.

### Runtime flow (what a Drive script does)

1. Read `GOOGLE_APPLICATION_CREDENTIALS` → find the JSON key.
2. Use the key to prove "I am `markerbase-reader`" → get a short-lived token. *(auth)*
3. Ask the Drive API to list/read files in folder X.
4. Drive checks the share: is `markerbase-reader` allowed? Yes, Viewer, read-only. *(authz)*
5. Drive returns the file. No browser login, no personal password used.

### Why this structure

- Your personal Google login is never in the code.
- Least privilege: the robot can only *read*, only the folders you *shared*.
- Small blast radius: a leaked key = read access to one folder; delete/rotate the
  key in the Cloud console without touching your account.

## The two credentials in the pipeline

The full pipeline talks to two external services, each with its own credential:

| Credential | Env var | Used for | Billed to |
|---|---|---|---|
| Google service-account key | `GOOGLE_APPLICATION_CREDENTIALS` | *Fetching* papers from Drive | Free (Drive API) |
| LLM API key | `GEMINI_API_KEY` (default) or `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` | *Assessing + extracting* papers | Gemini free tier (rate-limited); others per token |

A terminal running the whole flow needs **both** set. They're independent
accounts, credentials, and bills.

## The pipeline structure

Two scheduled GitHub Actions, decoupled so day-to-day processing never pings you:

- **`process.yml`** (every 4h, silent) — discovers new PDFs, runs the two gates,
  assesses eligible-stage papers, and updates `roster.csv`. Capped at 100
  assessments per run so a sudden dump of PDFs can't run up an unbounded bill;
  the rest are picked up on later runs. Cadence is 4h rather than 30 min only to
  be frugal with Actions minutes — the API cost is driven by *new* papers, not by
  how often we poll, so empty runs are nearly free.
- **`digest.yml`** (Friday 06:00 UTC) — reads the roster and maintains one
  GitHub issue listing everything outstanding. Because it reads *current roster
  state*, the digest is the complete standing queue, not "what changed this week".

### State, not stages-as-files

`roster.csv` is a single state machine: every paper has exactly one row and one
`status`. We deliberately avoided per-stage files (a paper would have to be moved
between them atomically, and bot+human edits would collide). The terminal states
(`EXCLUDED`, `INELIGIBLE`, `DUPLICATE`) are the "don't look again" guarantee —
discovery only assesses filenames not already in the roster.

### Who edits what (the no-shared-files rule)

The bot owns `roster.csv`; you own `exclude.txt` and `decisions.yaml`. No file is
written by both, which is what keeps the bot's pushes from clobbering your edits.
Your edits are line-based text (plain lines / flat YAML), never CSV — so opening
them can't mangle an all-digit PubMed-ID key (Excel turns `12345678` into
`1.23E+07`). The roster *is* CSV, but only the bot writes it and you only view it
(GitHub renders CSV as a table), so Excel never touches it.

### The two human-in-the-loop flags

- **Duplicate risk** needs your judgment and can't be auto-detected. The agent
  flags `REVIEW_DUPLICATE`; you resolve by adding `id: duplicate` / `id: unique`
  to `decisions.yaml`; the next run routes accordingly.
- **Missing supplement** resolves itself. The agent flags `AWAIT_SUPPLEMENT`; you
  upload files to Drive under a `<id>/` folder (one per paper, keyed by the PDF's
  name) beneath the supplement root; the next eligibility run re-assesses *with*
  the supplement included. It re-checks whenever the folder's **contents change**
  (a content fingerprint is stored in `supplement_fp`), so a corrected re-upload
  gets another chance while an unchanged folder never re-bills. `src/supplements.py`
  converts the files for the model: PDFs pass through natively; **spreadsheets
  (xlsx/xls), CSV/TSV/text, and Word (docx/doc)** are converted to text. Legacy
  `.doc` uses LibreOffice (preinstalled on the runner); unsupported types are
  skipped with a note. If a supplement IS examined but still doesn't contain the
  needed data, the paper is flagged `SUPPLEMENT_INSUFFICIENT` — distinct from
  `AWAIT_SUPPLEMENT` (nothing uploaded yet) so you can tell "waiting on you" from
  "what you gave us wasn't enough". Both re-check when the folder contents change.

### Spec versioning

`markerbase.SPEC_VERSION` is stamped on every assessed row. Bump it when the
eligibility spec changes; rows then show which spec judged them. (Re-assessing
old papers under a new spec is a deliberate manual action — not automatic, so a
spec tweak can't silently re-bill the whole back-catalogue.)

## A note on committed paper text

The repo is **public** on purpose, for transparency of the code. `roster.csv` is
lightweight — status + a few booleans, no paper text at all. The reasoning
(per-criterion evidence quotes, exclusion reasons, the model's summary) lives in
`data/eligibility/<id>.json`. Those are short snippets, which is fine — a journal
owns the typesetting, not the underlying facts or a sentence of text. The firm
rule is simply: **never store a whole paper's text** (and the PDFs themselves are
never committed — they're fetched in memory, and `papers/` is gitignored).

## Secret hygiene

- Both secrets live **outside** the repo (`~/.secrets/…`), referenced via env vars.
- `.gitignore` is a backstop (excludes key files, `.env`, `papers/`).
- The real protection is keeping the JSON key out of the project folder entirely.

## Repository reference

The README is deliberately high-level; the detail lives here.

### Two stages

Both stages run in ONE workflow, `.github/workflows/pipeline.yml` — every 4 hours,
or on demand (Actions → Pipeline → Run workflow, with a choice of stage).

- **Stage 1 — eligibility** (`run_eligibility.py`): triage new Drive PDFs against
  the eligibility spec, and re-check papers whose supplement folder changed.
- **Stage 2 — extraction** (`run_extraction.py`): extract every ELIGIBLE paper into
  the five tables, validate in Python, repair up to `EXTRACT_MAX_REPAIRS` (3) times
  before giving up (EXTRACTION_FAILED), then rebuild `data/final/`.
- Gemini quota exhausted mid-run → the run stops cleanly; the next run continues.
- **Local** (`run_local.py`): both stages on a local folder of PDFs. Writes to
  `local_output/` (git-ignored). Use it for the gold set and prompt iteration.

### Layout

```
config/  target_loci.csv — target IR markers + aliases (you maintain)
src/     all the code
data/    roster.csv, eligibility/<id>.json, extracted/<id>/, final/ (bot);
         exclude.txt, duplicate_decisions.yaml (you)
docs/    NOTES.md + the generated stats.svg
.github/ pipeline.yml (both stages), digest.yml (weekly attention issue)
```

### Code

| File | Role |
|---|---|
| `src/llm.py` | The only LLM interface: Gemini / Anthropic / OpenAI-compatible, PDF input, Pydantic structured output, throttle + retry. |
| `src/eligibility.py` | Eligibility spec + schema + the assessment call. `REQUIRED_CHECKS` sets the rule. |
| `src/extraction.py` | Extraction schema (5 tables + provenance), prompt, per-study writers. |
| `src/validate.py` | Deterministic checks → errors (repair loop) / warnings (README). |
| `src/export.py` | Builds `data/final/ir_extraction.{csv,xlsx}`; computes all derived values. |
| `src/targets.py` | Loads `config/target_loci.csv`; `normalise()` maps aliases / Musca numbering. |
| `src/run_eligibility.py`, `src/run_extraction.py` | Drive-based drivers (GitHub Actions). |
| `src/run_local.py` | Local-folder driver. |
| `src/supplements.py` | Converts supplementary files (xlsx/xls/csv/docx/doc/pdf) to LLM parts. |
| `src/pricing.py` | Cost estimates (Gemini free tier = $0). |
| `src/digest.py`, `src/stats.py`, `src/drive.py`, `src/store.py` | Weekly issue, status SVG, Drive access, state files. |

### Data model

| table | one row = |
|---|---|
| `study.yaml` | one paper |
| `surveys.csv` | site × time window × species × collection method |
| `genotypes.csv` | survey × marker (RR/RS/SS or allele counts; `pooled` flag) |
| `bioassays.csv` | survey × insecticide × concentration × synergist |
| `geno_pheno.csv` | bioassay × marker × alive/dead → RR/RS/SS |

The final table is long format: one row per genotype, bioassay or geno-pheno
record (`Record type`), with paper and survey fields repeated, and `NA` for
missing values. Where your column list had duplicate names, they are
disambiguated as `Country` / `Country (site)` and `Evidence location (data
source)` / `Evidence location (coordinates)`.

Rules: the LLM gives raw counts only, and frequencies are computed in code
(allele freq = (2RR+RS)/2N). A frequency the paper prints without counts is used
only as a fallback, flagged `Raw counts available = no (reported frequency only)`.
Vgsc codon 995 (1014) is multi-allelic (L/F/S): L995F and L995S are separate
rows, and for each, SS = mosquitoes with no copy of *that* allele (so it
includes carriers of the other mutation); the true L/L count goes in the study
README. Coordinates are only those the paper states. Geocoding place names
(GeoNames/OSM) is **not built yet**, so `Coordinates reported or inferred` is
`reported` or `NA`. The WHO phenotype uses raw mortality (no Abbott correction),
only for diagnostic-dose assays without synergist.

### State / config files

| File | Owner | Purpose |
|---|---|---|
| `config/target_loci.csv` | you | Target markers, aliases, variant type, tier (draft — verify). |
| `data/roster.csv` | bot | One row per paper — status + flags + model/tokens. |
| `data/eligibility/<id>.json` | bot | Full eligibility decision per paper. |
| `data/extracted/<id>/` | bot | The five tables + README (decisions, validator warnings). |
| `data/final/` | bot | Combined CSV + Excel. |
| `data/exclude.txt` | you | Papers to skip entirely. |
| `data/duplicate_decisions.yaml` | you | `duplicate` / `unique` rulings. |

### Secrets (repo settings → Secrets and variables → Actions)

| Secret / variable | Used for |
|---|---|
| `GEMINI_API_KEY` | Default model provider. |
| `ANTHROPIC_API_KEY` | Only if you run with a Claude model spec (optional). |
| `DRIVE_SA_KEY` | Drive service-account JSON key (full file contents). |
| `DRIVE_FOLDER_ID` | Top `papers` folder — **point this at the IR papers folder**. |
| `DRIVE_SUPPLEMENT_FOLDER_ID` | Top supplements folder (optional). |
| `DIGEST_ASSIGNEES` (variable) | GitHub username(s) to assign the weekly issue to. |

### Drive layout & contributor access

```
papers/                ← shared with the SERVICE ACCOUNT (Viewer)
├── master/            ←   your own PDFs (incl. institutional-access ones)
│     └── 111.pdf
├── alice/             ← shared with alice only (Editor) — she sees ONLY this
│     └── 222.pdf
└── bob/               ← shared with bob only (Editor)
      └── 333.pdf
```

The pipeline walks this tree read-only (never moves files), tagging each PDF with
its source folder. Contributors see only their own folder, so institutional PDFs
in `master/` stay private. Supplements mirror this shape, with a `<paper-id>/`
folder inside any contributor's subfolder. Adding a contributor = create + share
their subfolder; no secret or code change needed.

### Running locally

Without Drive: see the README quick start (`src/run_local.py`). With Drive:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=~/.secrets/<key>.json
export DRIVE_FOLDER_ID=...            # and DRIVE_SUPPLEMENT_FOLDER_ID if used
export GEMINI_API_KEY=...
python src/run_eligibility.py && python src/run_extraction.py
```
