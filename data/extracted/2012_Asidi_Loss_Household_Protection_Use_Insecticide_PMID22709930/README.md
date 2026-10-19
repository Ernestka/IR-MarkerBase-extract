# Extraction record — 2012_Asidi_Loss_Household_Protection_Use_Insecticide_PMID22709930

- Extracted: 2026-10-19
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 2 · Bioassays: 2 · Geno-pheno rows: 0

## Decisions

### Extraction Summary
- **Surveys**: Split into two distinct geographical/temporal site surveys:
  1. Northern Benin (Malanville, July–August 2008)
  2. Southern Benin (Cotonou suburbs: Ladji, Fifadji, Abomey Calavi; May–June 2008)
- **Genotypes**: Extracted counts for kdr (Vgsc L1014F / L995F) from Table 3:
  - Northern site: 34 genotyped (28 SS, 5 RS, 1 RR, frequency = 0.10).
  - Southern site: 58 genotyped (10 SS, 3 RS, 45 RR, frequency = 0.80).
- **Bioassays**: Extracted exit trap 24-hour mortality following treatment of nets with lambdacyhalothrin (18 mg/m2). Because exact numbers of exposed or dead mosquitoes were not explicitly printed in the text/tables (only mortality percentages: 70% in North, max 12% in South), count fields (`n_exposed`, `n_dead`, `n_alive`) were left null per rule 2.
- **Geno-pheno**: Genotypes were not reported separately for dead and surviving mosquitoes, so `geno_pheno` is empty.
