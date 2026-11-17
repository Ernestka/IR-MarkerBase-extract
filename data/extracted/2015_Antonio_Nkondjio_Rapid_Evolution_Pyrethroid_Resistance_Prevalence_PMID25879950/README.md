# Extraction record — 2015_Antonio_Nkondjio_Rapid_Evolution_Pyrethroid_Resistance_Prevalence_PMID25879950

- Extracted: 2026-11-17
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 8 · Bioassays: 12 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Sampling Locations**:
   - Two main urban study sites in Cameroon were evaluated: Douala (3°48'N, 10°08'E) and Yaoundé (3°51'N, 11°30'E).
   - Bioassay data from Table 1 are split by city, habitat type (Unpolluted, Cultivated), and year (2010 vs 2013).
   - Intron-1 sequencing data (Table 2) were collected in 2011 and merged across Douala and Yaoundé by the authors due to small sample size; these are extracted under 2011 survey records broken down by breeding habitat (Unpolluted, Polluted, Cultivated) and molecular species (An. coluzzii, An. gambiae).
   - Generic 'kdr' frequency summaries from text/Figure 3 were dropped as 'kdr' is not an explicit target marker name (only target markers L1014F and L1014S are recorded in genotypes from Table 2).

2. **Bioassays**:
   - Bioassays were conducted using standard WHO tube assays with 0.75% permethrin and 0.05% deltamethrin (1 h exposure, 24 h mortality).
   - Mosquito sample sizes per bioassay test were described in methods as batches of 20 to 25 per tube, but exact total counts per test were not printed. Per extraction rules, count fields (`n_exposed`, `n_dead`, `n_alive`) are left null and `reported_mortality_pct` is recorded with `dead_alive_printed = false`.
   - In Table 1, for Permethrin / Yaoundé / Unpolluted / 2013, the printed 95% CI is `(48.8-61.1)` for a reported point estimate of `36.8%`. This typo/mismatch in the published paper is flagged in `inconsistency_note`.

3. **Genotypes**:
   - Table 2 reports 43 sequenced specimens collected in 2011 (N=43 mosquitoes). Mosquitoes carrying L1014F or L1014S alleles were extracted as carrier counts (`n_carriers` out of `n_genotyped` mosquitoes per habitat and species).
   - Pooled total counts across all 4 years (e.g. 1,449 total mosquitoes processed) were excluded to avoid double-counting.

4. **Genotype-Phenotype Data**:
   - No survivor vs dead phenotype-split genotype tables or counts were reported in the paper, so `geno_pheno` is empty.

## Validator warnings

- bioassay 2015_Antonio_Nkondjio_yaounde_unpolluted_2013_perm075: inconsistent in the paper (values kept as printed) — Printed 95% CI (48.8-61.1) does not contain the printed point estimate (36.8%).
