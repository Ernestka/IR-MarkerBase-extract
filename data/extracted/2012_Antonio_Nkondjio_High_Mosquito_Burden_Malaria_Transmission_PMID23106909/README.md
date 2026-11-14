# Extraction record — 2012_Antonio_Nkondjio_High_Mosquito_Burden_Malaria_Transmission_PMID23106909

- Extracted: 2026-11-14
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 0 · Bioassays: 3 · Geno-pheno rows: 2

## Decisions

### Decisions & Extraction Rationale
- **Surveys**: Single survey created for wild-reared *An. gambiae s.l.* collected as larvae in Ndogpassi, Douala, Cameroon during 2011 for bioassays and kdr genotyping.
- **Bioassays**: Extracted WHO tube bioassays for 4% DDT, 0.75% permethrin, and 0.05% deltamethrin from Table 2 and text. Because Table 2 reports only total exposed and mortality percentage without explicit dead/alive counts, `dead_alive_printed` is set to `false` and count fields `n_dead` and `n_alive` are left `null` per Rule 2.
- **Genotypes / Geno-Pheno**: All genotyped specimens (N=61) were selected specifically from mosquitoes that survived exposure to DDT, permethrin, and deltamethrin. Per Rule 6, these are recorded exclusively in `geno_pheno` (and omitted from `genotypes` to prevent double-counting). Since the genotyped survivors were pooled across three insecticides, `bioassay_id` is set to `null` and `insecticide` is recorded as 'DDT + permethrin + deltamethrin'.
- **Markers**: Extracted `L1014F` and `L1014S` for Vgsc as named in paper. For L1014F, 27 RR and 11 RS are reported; SS = 23 is derived by subtraction per Rule 4b (61 - 27 - 11). For L1014S, zero presence was reported (0 RR, 0 RS, 61 SS).

## Validator warnings

- geno_pheno #1 (DDT + permethrin + deltamethrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin + deltamethrin)
- geno_pheno #2 (DDT + permethrin + deltamethrin, Vgsc L1014S, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin + deltamethrin)
