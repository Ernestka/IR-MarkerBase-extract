# Extraction record — 2009_Yadouleton_Development_Vegetable_Farming_Cause_Emergence_PMID19442297

- Extracted: 2026-11-12
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 0 · Bioassays: 8 · Geno-pheno rows: 6

## Decisions

### Data Extraction Decisions

1. **Surveys**: Three surveys were created for the three study sites in Benin: Houeyiho (Cotonou), Acron (Porto-Novo), and Azèrèkè (Parakou). Coordinates reported in DMS were converted to decimal degrees.
2. **Target Marker**: The kdr west mutation (Vgsc L995F) is identified using gene `kdr` and marker `kdr-west` as reported in text and tables.
3. **Genotypes vs. Geno-Pheno**: Table 5 reports kdr genotype counts (RR, RS, SS) stratified by bioassay outcome ('Survivors' and 'Dead'). Per Rule 6, all genotype data were extracted under `geno_pheno` to avoid double counting, and the standard `genotypes` array is left empty.
4. **Inconsistency Notes**: 
   - Added `inconsistency_note` to `2009_Yadouleton_houeyiho_ddt` bioassay because Table 3 reports n_dead = 165 and n_alive = 1045 (sum = 1210), which contradicts n_exposed = 1200.
   - Added `inconsistency_note` to `geno_pheno` records because Table 5 printed 'Kdr Frequency' corresponds to carrier percentage ((RR+RS)/N), not allele frequency ((2RR+RS)/2N).
5. **Bioassay Links**: Table 5 does not specify which specific insecticide the survivors and dead mosquitoes were tested against. Thus, `bioassay_id` and `insecticide` are set to `null` in `geno_pheno` as per Rule 6.

## Validator warnings

- bioassay 2009_Yadouleton_houeyiho_ddt: inconsistent in the paper (values kept as printed) — Printed n_dead (165) + n_alive (1045) = 1210, which exceeds reported n_exposed (1200).
- bioassay 2009_Yadouleton_houeyiho_ddt: n_dead + n_alive = 1210 but n_exposed = 1200
- geno_pheno #1 (no insecticide, kdr kdr-west, alive): not linked to a single bioassay (insecticide as reported: none given)
- geno_pheno #1 (no insecticide, kdr kdr-west, alive): inconsistent in the paper (values kept as printed) — Printed Kdr Frequency of 90a represents carrier percentage (60+120)/200 = 90%, whereas true calculated allele frequency is 0.60 (240/400).
- geno_pheno #2 (no insecticide, kdr kdr-west, dead): not linked to a single bioassay (insecticide as reported: none given)
- geno_pheno #2 (no insecticide, kdr kdr-west, dead): inconsistent in the paper (values kept as printed) — Printed Kdr Frequency of 27a represents carrier percentage (7+20)/100 = 27%, whereas true calculated allele frequency is 0.17 (34/200).
- geno_pheno #3 (no insecticide, kdr kdr-west, alive): not linked to a single bioassay (insecticide as reported: none given)
- geno_pheno #3 (no insecticide, kdr kdr-west, alive): inconsistent in the paper (values kept as printed) — Printed Kdr Frequency of 86a represents carrier percentage (57+115)/200 = 86%, whereas true calculated allele frequency is 0.5725 (229/400).
- geno_pheno #4 (no insecticide, kdr kdr-west, dead): not linked to a single bioassay (insecticide as reported: none given)
- geno_pheno #4 (no insecticide, kdr kdr-west, dead): inconsistent in the paper (values kept as printed) — Printed Kdr Frequency of 35a represents carrier percentage (12+23)/100 = 35%, whereas true calculated allele frequency is 0.235 (47/200).
- geno_pheno #5 (no insecticide, kdr kdr-west, alive): not linked to a single bioassay (insecticide as reported: none given)
- geno_pheno #5 (no insecticide, kdr kdr-west, alive): inconsistent in the paper (values kept as printed) — Printed Kdr Frequency of 71.5a represents carrier percentage (45+98)/200 = 71.5%, whereas true calculated allele frequency is 0.47 (188/400).
- geno_pheno #6 (no insecticide, kdr kdr-west, dead): not linked to a single bioassay (insecticide as reported: none given)
- geno_pheno #6 (no insecticide, kdr kdr-west, dead): inconsistent in the paper (values kept as printed) — Printed Kdr Frequency of 20a represents carrier percentage (5+15)/100 = 20%, whereas true calculated allele frequency is 0.125 (25/200).
