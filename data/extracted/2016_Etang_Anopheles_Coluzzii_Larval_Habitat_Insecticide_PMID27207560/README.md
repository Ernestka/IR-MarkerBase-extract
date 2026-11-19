# Extraction record — 2016_Etang_Anopheles_Coluzzii_Larval_Habitat_Insecticide_PMID27207560

- Extracted: 2026-11-19
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 0 · Bioassays: 14 · Geno-pheno rows: 4

## Decisions

### Data Extraction Decisions

1. **Surveys**:
   - Split by study site (Manoka island vs Youpwe quarter) and sampling period (December 2013 dry season vs April 2014 rainy season).
   - Geographic coordinates reported in text (03°47' N, 09°39' E for Manoka; 04°00' N, 09°42' E for Youpwe) were converted to decimal degrees (3.7833, 9.65 and 4.0, 9.7).
   - All mosquitoes analyzed by PCR-RFLP were confirmed as *Anopheles coluzzii*.

2. **Bioassays**:
   - 14 wild mosquito bioassays extracted from Table 2 and Figure 3.
   - Bioassay sample sizes (N_exposed) are taken directly from Table 2.
   - Control tests on the Kisumu reference strain were excluded per Rule 5.
   - Percent mortality values printed in text (deltamethrin Dec 2013/Apr 2014 for both sites) or read from Figure 3 bar charts were assigned to `reported_mortality_pct`. Count fields `n_dead` and `n_alive` remain null per Rule 2.

3. **Genotype-Phenotype Data**:
   - A total of 120 bioassay survivors (44 from Manoka, 76 from Youpwe) from December 2013 were genotyped at the kdr L1014 locus using HOLA (Table 3, Figure 4).
   - Because survivors were randomly pooled across bioassays testing DDT, permethrin, and deltamethrin, `bioassay_id` is set to null, and `insecticide` is listed as 'DDT + permethrin + deltamethrin' per Rule 6.
   - Frequencies reported in Table 3 (75% L1014F in Manoka, 88% L1014F in Youpwe; 0% L1014S in both) are captured under `reported_allele_freq`.

## Validator warnings

- geno_pheno #1 (DDT + permethrin + deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin + deltamethrin)
- geno_pheno #2 (DDT + permethrin + deltamethrin, kdr L1014S, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin + deltamethrin)
- geno_pheno #3 (DDT + permethrin + deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin + deltamethrin)
- geno_pheno #4 (DDT + permethrin + deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin + deltamethrin)
