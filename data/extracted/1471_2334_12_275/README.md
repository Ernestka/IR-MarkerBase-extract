# Extraction record — 1471_2334_12_275

- Extracted: 2026-10-14
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 0 · Bioassays: 3 · Geno-pheno rows: 2

## Decisions

### Survey and Bioassay Extraction
- Adult Anopheles gambiae s.l. were reared from field-collected larvae sampled from breeding sites in Ndogpassi, Douala, Cameroon across 2011.
- WHO susceptibility bioassays were conducted with 4% DDT, 0.75% permethrin, and 0.05% deltamethrin.
- Mortality percentages and sample sizes (N exposed) were printed in Table 2, but dead and alive counts were not explicitly printed for the field tests; per extraction rules, n_dead and n_alive are left null and dead_alive_printed is set to false.
- Kisumu control data were excluded per instructions.

### Genotype-Phenotype Data
- 61 survivors from DDT, permethrin, and deltamethrin bioassays were genotyped for kdr L1014F and L1014S using HOLA.
- Because these genotyped mosquitoes were survivors pooled across three bioassays rather than a random population sample, they were extracted into `geno_pheno` with bioassay_id = null and insecticide = 'DDT + permethrin + deltamethrin', leaving `genotypes` empty.
- For L1014F, 27 samples were homozygous (RR), 11 were heterozygous (RS), 38 carried the allele, and 23 were homozygous susceptible (SS = 61 - 38). For L1014S, no carriers or resistant alleles were found (RR = 0, RS = 0, SS = 61).

## Validator warnings

- geno_pheno #1 (DDT + permethrin + deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin + deltamethrin)
- geno_pheno #2 (DDT + permethrin + deltamethrin, kdr L1014S, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin + deltamethrin)
