# Extraction record — 2014_Mulamba_Widespread_Pyrethroid_DDT_Resistance_Major_PMID25333491

- Extracted: 2026-11-16
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 0 · Bioassays: 0 · Geno-pheno rows: 2

## Decisions

### Key Decisions

1. **Target Markers Extracted**:
   - **GSTe2 L119F**: 60 F1 An. funestus s.s. mosquitoes (30 alive/resistant and 30 dead/susceptible after 1 h exposure to 4% DDT) from Jinja, Uganda were genotyped. 100% of susceptible dead mosquitoes were wild-type (30 SS, 0 RS, 0 RR), while resistant alive mosquitoes showed 73.3% SS (22 SS), 13.3% RS (4 RS), and 13.3% RR (4 RR), giving 12 total 119F alleles across 60 mosquitoes (10% overall allele frequency as reported in text).
   - **VGSC**: 917 bp region sequenced across multiple locations; no target kdr mutations (L1014F/S) were detected. Non-target F1021C detected in 2 Lira mosquitoes is excluded.
   - **CYP6P9a/b**: Expression levels measured via qRT-PCR only (no SNP/CNV marker genotyped).

2. **Bioassays & Genotypes**:
   - Individual bioassay counts were provided in Supplementary Table S3 (not present in main text). Therefore, no standalone bioassays were extracted, and `bioassay_id` in `geno_pheno` remains null.

## Validator warnings

- geno_pheno #1 (DDT 4%, GSTe2 L119F, alive): not linked to a single bioassay (insecticide as reported: DDT 4%)
- geno_pheno #2 (DDT 4%, GSTe2 L119F, dead): not linked to a single bioassay (insecticide as reported: DDT 4%)
