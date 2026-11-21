# Extraction record — 2017_Messenger_Insecticide_Resistance_Anopheles_Arabiensis_Ethiop_PMID29151024

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 18 · Genotype rows: 0 · Bioassays: 36 · Geno-pheno rows: 69

## Decisions

### Data Extraction Decisions Summary

- **Surveys & Sampling**: Mosquitoes were collected as larvae by dipping from various breeding sites in study sites across Ethiopia and reared to adults during the long rainy season (June–September) in 2015 and 2016. Molecular identification confirmed *Anopheles arabiensis* as the target species.
- **Genotypes vs Geno_Pheno**: All genotyped mosquitoes reported in Table 2 (2015, 8 sentinel sites) and Table 3 (2016, 10 sentinel sites) were sub-sampled directly from WHO bioassays (DDT 4% or Deltamethrin 0.05%) and split into bioassay survivors ('Alive') and dead ('Dead'). Therefore, all genotype data were extracted into `geno_pheno` (and none into `genotypes` to prevent double counting).
- **Markers**: West African *kdr* mutation L1014F was extracted (`gene`: `kdr`, `marker`: `L1014F`). The East African *kdr* mutation L1014S was screened for but not detected in any sample.
- **Bioassays**: Extracted WHO tube test bioassays corresponding to the bioassay cohorts tested for *kdr* in Tables 1, 2, and 3. `dead_alive_printed` is set to `false` because only `n_exposed` and `% mortality` were printed in the tables.
- **Data Integrity**: All genotype counts (RR, RS, SS) and sample sizes match mathematically across all rows in Tables 2 and 3.
