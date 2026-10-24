# Extraction record — 2011_Hunt_Insecticide_Resistance_Malaria_Vector_Mosquitoes_PMID21679391

- Extracted: 2026-10-24
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 6 · Genotype rows: 1 · Bioassays: 26 · Geno-pheno rows: 8

## Decisions

### Extraction Summary
- **Surveys**: Created distinct surveys for each of the four mining localities (Obuasi, Tarkwa, Ahafo, Akyem) separated by molecular form (S form, M form, and M/S hybrid for Tarkwa).
- **Bioassays**: Extracted all WHO diagnostic tube susceptibility bioassays reported in Table 2 for An. gambiae S form. Dead/alive counts were left null because only sample size (N) and percentage mortality were explicitly printed in Table 2 (`dead_alive_printed: false`).
- **Genotype-Phenotype**: Extracted all pyrethroid-exposed kdr (L1014F) genotype frequencies split by phenotype (Resistant / Susceptible) from Table 3 into `geno_pheno`. `bioassay_id` is set to null because mosquitoes were pooled across pyrethroid tests. Insecticide is set to 'pyrethroids'.
- **Genotypes**: Extracted non-phenotype split kdr data for Tarkwa An. gambiae M form mentioned in page 4 text into `genotypes` (5 genotyped, 1 RS, 4 SS).
- **Excluded Data**: Bioassay results for *An. funestus* mentioned in the text were pooled across all four localities (n=166 for deltamethrin, n=251 for malathion) without site-level breakdowns, so they were excluded according to Rule 7.

## Validator warnings

- geno_pheno #1 (pyrethroids, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #2 (pyrethroids, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #3 (pyrethroids, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #4 (pyrethroids, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #5 (pyrethroids, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #6 (pyrethroids, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #7 (pyrethroids, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #8 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
