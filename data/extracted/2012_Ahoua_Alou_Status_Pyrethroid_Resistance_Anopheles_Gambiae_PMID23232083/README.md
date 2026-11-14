# Extraction record — 2012_Ahoua_Alou_Status_Pyrethroid_Resistance_Anopheles_Gambiae_PMID23232083

- Extracted: 2026-11-14
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 0 · Bioassays: 6 · Geno-pheno rows: 4

## Decisions

### Data Extraction Summary

1. **Surveys**:
   - Two sampling locations in Adzopé district, Eastern Côte d'Ivoire: Port-Bouët and Tsassodji.
   - Collections took place between May and June 2007.
   - All collected Anopheles gambiae s.l. were identified molecularly as An. gambiae s.s. M form (Anopheles coluzzii).
   - Coordinates printed as (6°10 N, 3°85 W). Latitude 6°10' N converted to 6.166667. Longitude printed as 3°85 W, which likely represents 3.85° W, recorded as -3.85.

2. **Bioassays**:
   - 6 bioassay records extracted from Table 1 covering WHO standard cylinder susceptibility tests for permethrin 1%, deltamethrin 0.05%, and lambda-cyhalothrin 0.05% across both sites.
   - Laboratory susceptible Kisumu reference strain was excluded per Rule 5.
   - `dead_alive_printed` set to false as only N exposed and % mortality were printed in Table 1.

3. **Genotypes & Geno_Pheno**:
   - All genotyped specimens in Table 2 (N=56 for Port-Bouët and N=34 for Tsassodji) were split into Alive and Dead phenotype groups after exposure to pyrethroid-treated filter papers.
   - Per Rule 6, these records are placed in `geno_pheno` with `bioassay_id` set to null (since specimens were pooled across the pyrethroid bioassays) and `insecticide` set to 'pyrethroids'.
   - To avoid double counting, the `genotypes` array is kept empty.

## Validator warnings

- geno_pheno #1 (pyrethroids, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #2 (pyrethroids, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #3 (pyrethroids, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #4 (pyrethroids, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pyrethroids)
