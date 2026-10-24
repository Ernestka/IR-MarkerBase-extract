# Extraction record — 2011_Yewhalaw_Multiple_Insecticide_Resistance_Impediment_Insecti_PMID21264325

- Extracted: 2026-10-24
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 0 · Bioassays: 10 · Geno-pheno rows: 11

## Decisions

### Extraction Decisions

1. **Survey Stratification**: The study evaluated mosquito populations across two groups of villages surrounding the Gilgel-Gibe hydroelectric dam in southwestern Ethiopia: 'low risk' (5–8 km from dam) and 'high risk' (<3 km from dam). Collections took place during the wet season (July–September 2009). Data are split into two corresponding surveys (`_low_risk` and `_high_risk`).
2. **Genotypes vs. Geno-Pheno**: All 280 genotyped mosquitoes for `Vgsc L1014F` (L995F) are presented in Table 2 partitioned by bioassay outcome (alive vs. dead for DDT, permethrin, and deltamethrin). To avoid double counting (Rule 6), all of these records were placed in `geno_pheno` and `genotypes` is left empty.
3. **Other Target Markers Screened**:
   - `Vgsc L1014S` (L995S): Screened via AS-PCR in the same mosquito specimens (284 tested) and found in 0 specimens across both village groups.
   - `Ace-1 G119S` (G280S): Screened via PCR-RFLP in 169 scored specimens (out of 176 tested) and found in 0 specimens.
   - Since individual survey or phenotype breakdowns for these zero-mutant screenings were not printed as distinct count tables, they are noted here rather than duplicated across surveys.
4. **Bioassays**: Extracted WHO tube test bioassays for DDT, permethrin, deltamethrin, malathion, and propoxur for both village groups. Dead/alive counts were not explicitly printed in Table 1 (only total exposed `n` and `% mortality`), so `dead_alive_printed` is set to `false` and counts are left `null` for automated derivation.
5. **Laboratory Control Strain**: Data for the reference laboratory strain from Malaria Training Centre, Nazareth, Ethiopia were excluded per Rule 5.
6. **Printed Inconsistency Note**: In Table 2, for 'Low risk' DDT survivors, the paper lists RR=28, RS=1, SS=0 (N=29) and reports R allele frequency as 0.98. The calculated allele frequency from the genotype counts is 55/58 = 0.948. The printed value of 0.98 was preserved in `reported_allele_freq` and flagged in `inconsistency_note` per Rule 8.

## Validator warnings

- geno_pheno #6 (2011_Yewhalaw_Multiple_Insecticide_Resistance_Impediment_Insecti_PMID21264325_low_risk_ddt, Vgsc L1014F, alive): inconsistent in the paper (values kept as printed) — Table 2 reports RR=28, RS=1, SS=0 (N=29) with allele frequency R=0.98, S=0.02; calculated R allele frequency from counts is 55/58 = 0.948.
