# Extraction record — trab116

- Extracted: 2026-10-12
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 2 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Survey & Genotyping Decisions
- **Site & Species:** Mosquitoes were collected as larvae in Tchonka, Shabunda territory, Sud-Kivu, DRC between April and November 2018. Molecular identification confirmed An. gambiae s.s. (n=139) and An. funestus s.s. (n=97).
- **Genotypes:**
  - kdr: Tested using the Martinez-Torres et al. 1998 protocol specific to the kdr-west (L1014F / L995F) mutation. The paper reports the resistant allele frequency as 98% (n=99) without genotype class counts (RR/RS/SS), so counts were left null and reported_allele_freq recorded as 0.98.
  - ace-1R: Tested via Weill et al. 2004 (Ace-1 G119S / G280S) on 101 An. gambiae s.s. individuals; no resistant individuals were detected (0 carriers out of 101 tested, frequency = 0.0).
  - An. funestus s.s. was not screened for kdr or ace-1 mutations ('As no kdr mutation has been found in A. funestus to date, this was not evaluated').
- **Bioassays:** While bioassays were conducted with multiple insecticides and PBO synergism, only pooled mortality ranges across species and GLM estimated marginal means (Figures 2 and 3) are reported in the main text; raw test counts and mortality percentages per species are in Supplementary File 2. Following rule 8b, bioassays were therefore omitted.

## Validator warnings

- genotype #1 (trab116_tchonka_2018_gambiae, Vgsc L1014F): frequency only (no raw counts)
