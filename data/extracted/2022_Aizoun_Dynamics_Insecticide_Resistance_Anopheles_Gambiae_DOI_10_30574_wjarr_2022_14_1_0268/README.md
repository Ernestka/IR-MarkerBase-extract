# Extraction record — 2022_Aizoun_Dynamics_Insecticide_Resistance_Anopheles_Gambiae_DOI_10_30574_wjarr_2022_14_1_0268

- Extracted: 2026-10-16
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 0 · Bioassays: 4 · Geno-pheno rows: 1

## Decisions

### Extraction Notes

1. **Surveys**:
   - Field collections were split into two separate surveys by collection year: 2015 (`2022_Aizoun_Bohicon_2015`) and 2020 (`2022_Aizoun_Bohicon_2020`), both collected between April and June in Bohicon district, Zou department, Benin.

2. **Bioassays**:
   - Reference strain Kisumu bioassays were excluded per Rule 5.
   - WHO bioassays for permethrin (0.75%) and DDT (4%) were extracted for 2015 and 2020. As only total exposed (100) and percentage mortality were reported, `dead_alive_printed` was set to `false` and `n_dead`/`n_alive` left as `null` per Rule 2.

3. **Genotypes & Geno-Pheno**:
   - Genotype data for the Vgsc L1014F (`kdr`) mutation (Table 2) was explicitly stated to come from surviving (alive) mosquitoes 24h post-exposure to permethrin and DDT in 2015. Per Rule 6, these counts were recorded in `geno_pheno` (`phenotype_group` = 'alive') rather than `genotypes` to avoid double counting.
   - Because survivors were combined across permethrin and DDT exposures, `bioassay_id` was set to `null` and `insecticide` recorded as 'permethrin and DDT'.

## Validator warnings

- geno_pheno #1 (permethrin and DDT, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin and DDT)
