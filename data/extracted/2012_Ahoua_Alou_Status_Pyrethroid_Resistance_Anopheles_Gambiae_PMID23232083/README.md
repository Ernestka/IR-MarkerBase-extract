# Extraction record — 2012_Ahoua_Alou_Status_Pyrethroid_Resistance_Anopheles_Gambiae_PMID23232083

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 0 · Bioassays: 6 · Geno-pheno rows: 4

## Decisions

### Data Extraction Decisions Summary

1. **Surveys & Sites**:
   - Two survey sites in Adzopé district, Côte d'Ivoire: Port-Bouët and Tsassodji.
   - Mosquitoes collected as larvae in May-June 2007 and reared to adults (wild_reared, F0).
   - Identified molecularly as *Anopheles gambiae s. s. M form*.
   - Coordinates provided as `6°10 N, 3°85 W` (6.166667, -3.85).

2. **Bioassays**:
   - Extracted 6 WHO cylinder susceptibility tests (3 pyrethroids x 2 sites).
   - Kisumu laboratory reference strain bioassays were excluded as controls.
   - Only `N` exposed and `Mortality (%)` are reported in Table 1; explicit counts of dead/alive were not printed, so `n_dead` and `n_alive` are left null with `dead_alive_printed = false` as per rules.

3. **Genotype vs Geno-Pheno Data**:
   - Genotyping for Vgsc L1014F (L995F) was performed on mosquitoes randomly selected from survivors (alive) and dead post-exposure across pyrethroid bioassays (pooled across pyrethroids).
   - Since all genotyped mosquitoes were split by phenotype outcome, they are extracted into `geno_pheno` (Rule 6). `bioassay_id` is left null because mosquitoes were pooled across multiple pyrethroid exposures. `genotypes` is left empty to avoid double counting.
   - Pooled total rows in Table 2 are omitted as per Rule 7.

## Validator warnings

- geno_pheno #1 (permethrin, deltamethrin, lambda-cyhalothrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin, deltamethrin, lambda-cyhalothrin)
- geno_pheno #2 (permethrin, deltamethrin, lambda-cyhalothrin, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin, deltamethrin, lambda-cyhalothrin)
- geno_pheno #3 (permethrin, deltamethrin, lambda-cyhalothrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin, deltamethrin, lambda-cyhalothrin)
- geno_pheno #4 (permethrin, deltamethrin, lambda-cyhalothrin, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin, deltamethrin, lambda-cyhalothrin)
