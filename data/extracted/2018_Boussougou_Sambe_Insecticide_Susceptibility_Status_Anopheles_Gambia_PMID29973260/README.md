# Extraction record — 2018_Boussougou_Sambe_Insecticide_Susceptibility_Status_Anopheles_Gambia_PMID29973260

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 9 · Genotype rows: 12 · Bioassays: 8 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys**:
   - Larval collections were performed between November and December 2015 across three sites in South-West Cameroon: Limbe, Tiko, and Buea (Fako Division).
   - Created 3 site-level surveys for *An. gambiae* (s.l.) to link the WHO tube susceptibility bioassays, which were conducted prior to molecular species identification.
   - Created 6 site x species surveys (*An. coluzzii* and *An. gambiae* s.s.) to accurately link the molecular species-specific genotyping results from Table 3.

2. **Markers & Genotypes**:
   - Screened markers are `kdr` `L1014F` and `kdr` `L1014S` via HOLA.
   - `L1014S` was screened in all 134 specimens across all sites and found to be entirely absent (0% allele frequency, all SS). Recorded explicit zero counts (SS = n_genotyped) for all site/species surveys as stated in text.
   - Genotype class counts (SS, RS, RR) for `L1014F` were taken directly from Table 3 and match reported allele frequencies perfectly.

3. **Bioassays**:
   - WHO standard susceptibility tube tests (60 min exposure, 24 h post-exposure mortality) were conducted for deltamethrin (0.05%), permethrin (0.75%), and malathion (5%).
   - Sample sizes `n_exposed` for pyrethroids were taken from Table 1, and 24 h mortality percentages were taken from Fig. 1 and text.
   - Because exact counts of dead/alive were not explicitly printed, `dead_alive_printed` is set to `false` and `n_dead` / `n_alive` left `null` per rule 2.
   - Malathion tests for Limbe and Buea are reported with 100% mortality with a combined sample size of n=228 across both sites; site-specific n_exposed is left `null`.
