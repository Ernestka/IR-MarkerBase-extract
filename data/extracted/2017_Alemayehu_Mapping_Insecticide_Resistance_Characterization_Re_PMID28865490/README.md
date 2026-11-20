# Extraction record — 2017_Alemayehu_Mapping_Insecticide_Resistance_Characterization_Re_PMID28865490

- Extracted: 2026-11-20
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 9 · Genotype rows: 8 · Bioassays: 16 · Geno-pheno rows: 32

## Decisions

### Data Extraction Decisions

1. **Surveys & Sites**: Nine study sites in Ethiopia were sampled between 2013 and 2015 during the wet season (July–September). All mosquitoes were collected as larvae ('larval dipping') and wild-reared to adults ('wild_reared', F0 generation). Species PCR confirmed 99.4% were *An. arabiensis* (no other *An. gambiae* s.l. species detected).
2. **Target Markers**: 
   - `kdr L1014F`: Genotyped in survivors and dead mosquitoes from Deltamethrin and DDT bioassays across 8 sites (Table 2). Extracted into `geno_pheno` to avoid double counting, linked to the corresponding bioassays.
   - `kdr L1014S`: Tested in all specimens and reported as absent across all tested populations. Included in `genotypes` as SS = n_genotyped, RS = 0, RR = 0 for each of the 8 sites where sample counts were reported.
   - `Ace-1 G119S`: Tested on 20 propoxur/bendiocarb survivors and pooled samples across sites; confirmed absent. Not split by individual survey, documented in text.
   - `Vgsc N1575Y`: Screened on 20 unexposed pooled specimens across populations; confirmed absent.
3. **Bioassays**: Extracted from Table 1 for DDT (4%) and Deltamethrin (0.05%) across all sites where mean mortality rates were reported. Per-bioassay sample size counts were not printed in Table 1 (only overall experimental protocol batch sizes of 20-25 x 4 replicates mentioned in text), so count fields (`n_exposed`, `n_dead`, `n_alive`) are set to `null` and `dead_alive_printed` is `false`, with `reported_mortality_pct` set to the printed mean.
4. **Inconsistencies Noted**:
   - Sodore Deltamethrin Survived: Table 2 lists SS=0, RS=7, RR=13 (N=20), which calculates to R=0.825, but printed R=0.85.
   - Goro DDT Survived: Table 2 lists SS=2, RS=6, RR=12 (N=20), which calculates to R=0.75, but printed R=0.79.

## Validator warnings

- geno_pheno #21 (2017_Alemayehu_sodore_delta, kdr L1014F, alive): inconsistent in the paper (values kept as printed) — Printed allele frequency R = 0.85, but calculated from SS=0, RS=7, RR=13 is 33/40 = 0.825.
- geno_pheno #27 (2017_Alemayehu_goro_ddt, kdr L1014F, alive): inconsistent in the paper (values kept as printed) — Printed allele frequency R = 0.79, but calculated from SS=2, RS=6, RR=12 is 30/40 = 0.75.
