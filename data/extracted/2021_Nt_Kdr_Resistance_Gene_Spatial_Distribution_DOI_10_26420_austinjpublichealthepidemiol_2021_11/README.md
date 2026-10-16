# Extraction record — 2021_Nt_Kdr_Resistance_Gene_Spatial_Distribution_DOI_10_26420_austinjpublichealthepidemiol_2021_11

- Extracted: 2026-10-16
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 0 · Bioassays: 6 · Geno-pheno rows: 2

## Decisions

### Extraction Summary
- **Surveys**: Two field surveys created for Akoun (urban) and Ebabodo (peri-urban) in Ayos city, Cameroon, sampled December 2019 - February 2020 as wild-reared larvae.
- **Bioassays**: Extracted 6 WHO tube test bioassays (3 per site for permethrin 0.75%, deltamethrin 0.05%, and DDT 4%). Kisumu control bioassays were excluded per schema rules.
- **Genotypes vs Geno_pheno**: Genotype testing for kdr (1014F) was performed exclusively on bioassay survivors (100 from Akoun, 100 from Ebabodo). Because these were phenotype-selected survivors pooled across insecticides, they are placed in `geno_pheno` with `bioassay_id: null` and `insecticide: 'DDT + permethrin + deltamethrin'`. The `genotypes` array is empty to prevent double counting.
- **Coordinates**: Converted from reported decimal-minute coordinates (e.g. 3°54’ 102N = 3° 54.102' N = 3.9017, 12°31’ 054E = 12° 31.054' E = 12.517567).
- **Inconsistencies noted in paper**: Table 4 prints 'Total' N=100 (matching individual row Ns instead of summing to 200); pooled Total row was not extracted.

## Validator warnings

- geno_pheno #1 (DDT + permethrin + deltamethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin + deltamethrin)
- geno_pheno #2 (DDT + permethrin + deltamethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin + deltamethrin)
