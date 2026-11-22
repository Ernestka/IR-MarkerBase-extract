# Extraction record — 2018_Kiuru_Status_Insecticide_Resistance_Malaria_Vectors_PMID29304805

- Extracted: 2026-11-22
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 6 · Genotype rows: 2 · Bioassays: 7 · Geno-pheno rows: 4

## Decisions

### Key Decisions & Data Structure Summary

1. **Surveys & Pooling**:
   - Field sampling took place in July–August 2015 in two villages in Kwale County: Marigiza (-4.443036, 39.461887) and Kidomaya (-4.578639, 39.157574).
   - Bioassay data was pooled across both villages as stated on page 5 ('As no differences in mortality rate was observed between the two villages, Kidomaya and Marigiza mortality rate data was analysed together for both villages'). Bioassays are extracted at the finest molecular species resolution reported (An. arabiensis, An. gambiae s.s., An. funestus s.s., An. vaneedeni) per Rule 7.

2. **Target Markers Assayed**:
   - Vgsc L1014S (kdr-East) and Vgsc L1014F (kdr-West) were assayed by TaqMan real-time PCR in 300 An. gambiae s.l. specimens (53 field-collected wild adults and 247 bioassayed adults).
   - L1014F was 0% across all tested mosquitoes.

3. **Genotype vs. Geno-Pheno Separation**:
   - **Geno-pheno**: 247 bioassayed F0 adults (78 alive/resistant and 169 dead/susceptible, pooled across deltamethrin and permethrin tests) are extracted in `geno_pheno` with `bioassay_id` set to `null` and `insecticide` set to 'deltamethrin + permethrin' as mandated by Rule 6. Per Rule 6, these bioassayed individuals are NOT repeated in `genotypes` to avoid double counting.
   - **Genotypes**: The remaining 53 non-bioassayed wild adult An. gambiae s.l. are extracted in `genotypes` (all 53 were wild-type SS for both L1014S and L1014F, as all 5 mutant carriers were found exclusively in the bioassayed subset).

4. **Counts vs Percentages**:
   - Table 3 reports number exposed and percentage mortality for bioassays, but not explicit count of dead/alive. Therefore `dead_alive_printed` is set to `false` and `n_dead`/`n_alive` are left `null`.
   - Table 4 explicitly prints genotype counts (RR, RS, SS, n) and reported allele frequencies for the bioassayed groups.
   - Note: Text on page 5 mentions 79 mosquitoes exhibited resistance phenotype, while Table 4 lists n=78 for the resistant group (and n=169 for susceptible, summing to the stated total 247). The exact printed counts from Table 4 were extracted.

## Validator warnings

- geno_pheno #1 (deltamethrin + permethrin, kdr L1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin + permethrin)
- geno_pheno #2 (deltamethrin + permethrin, kdr L1014S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + permethrin)
- geno_pheno #3 (deltamethrin + permethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin + permethrin)
- geno_pheno #4 (deltamethrin + permethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + permethrin)
