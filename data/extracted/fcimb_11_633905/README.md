# Extraction record — fcimb_11_633905

- Extracted: 2026-10-15
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 0 · Bioassays: 15 · Geno-pheno rows: 12

## Decisions

### Survey and Bioassay Extraction Decisions
- **Surveys**: Three sentinel districts/counties on São Tomé island were sampled between September and December 2018: Agua Grande, Caue, and Lemba. Exact decimal degree coordinates from Table 1 were recorded. All mosquitoes tested by PCR for species ID (n=1009 total across the three sites) were Anopheles gambiae s.s. (100%). The total sample sizes for the three sites match the sum of mosquitoes exposed in WHO susceptibility assays: Agua Grande = 336, Caue = 338, Lemba = 335 (total = 1009).
- **Bioassays**: WHO standard tube assays (1-h exposure, 24-h mortality) were performed for five insecticides: 4% DDT, 0.05% deltamethrin, 0.75% cypermethrin, 1% fenitrothion, and 5% malathion across the three sites (Table 4). Only sample size N and percentage mortality are printed in Table 4 (dead and alive counts are not printed), so `dead_alive_printed` is set to `false` and `n_dead`/`n_alive` are left null.
- **Genotypes and Genotype-Phenotype**: All genotyped mosquitoes were sampled from WHO tube bioassay outcomes (Table 5: 24 resistant/alive and 24 susceptible/dead per site). Hence, to prevent double-counting, no records are added to `genotypes` (which is kept empty), and all genotype records are captured under `geno_pheno` linked to their respective bioassay IDs.
  - For cypermethrin 0.75%, kdr L1014F was genotyped. Only heterozygous TTA/TTT (RS) and wild-type TTA/TTA (SS) were detected; no homozygous resistant TTT/TTT (RR) was observed.
  - For malathion 5%, ace-1 G119S was genotyped. All individuals tested across all sites in both alive and dead groups were wild-type GGC/GGC (SS=24, RS=0, RR=0).
  - L1014S was screened according to Methods, but no mutation was detected and no separate counts are tabulated in Table 5.
