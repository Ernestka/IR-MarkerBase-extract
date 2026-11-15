# Extraction record — 2012_Antonio_Nkondjio_High_Mosquito_Burden_Malaria_Transmission_PMID23106909

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 0 · Bioassays: 3 · Geno-pheno rows: 2

## Decisions

### Summary of Decisions
- **Survey**: Created a single survey for Anopheles gambiae reared from wild larvae in Ndogpassi, Douala, Cameroon (2011).
- **Bioassays**: Extracted three WHO tube bioassay results for diagnostic concentrations of 4% DDT, 0.75% permethrin, and 0.05% deltamethrin. Mortality rates were reported as percentages, so exact dead and alive counts were left null per Rule 2.
- **Kisumu reference strain**: Omitted as per Rule 5 (control strain).
- **Genotypes & Geno-Pheno**: All genotyped mosquitoes (N=61) were selected specifically from survivors of exposure to DDT, permethrin, and deltamethrin. Because these survivors were pooled across multiple bioassays, they are recorded in `geno_pheno` with `bioassay_id` set to null per Rule 6. No unselected population genotype dataset was reported, leaving `genotypes` empty.
- **Markers**: Recorded Vgsc L1014F (kdr-west) and L1014S (kdr-east) as written in the text. L1014S was tested and not detected.

## Validator warnings

- geno_pheno #1 (DDT + permethrin + deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin + deltamethrin)
- geno_pheno #2 (DDT + permethrin + deltamethrin, kdr L1014S, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin + deltamethrin)
