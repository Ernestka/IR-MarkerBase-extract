# Extraction record — 2010_Cuamba_High_Level_Pyrethroid_Resistance_Anopheles_PMID20544036

- Extracted: 2026-11-12
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 1 · Bioassays: 15 · Geno-pheno rows: 2

## Decisions

### Decisions Readme

1. **Surveys**:
   - Main survey `2010_Cuamba_tihuquine_2009` covers indoor-resting *Anopheles funestus s.s.* collections from Tihuquine (Chokwe District, Mozambique) in February 2009 (F1 adults reared from wild females).
   - Reference survey `2010_Cuamba_cameroon` covers 5 reference *An. funestus* mosquitoes from Cameroon sequenced for AChE (G119S).

2. **Markers Extracted**:
   - *Ace-1* G280S (reported as AChE G119S in paper). Sequenced in 15 mosquitoes from Tihuquine, Mozambique (8 bendiocarb resistant/alive and 7 bendiocarb susceptible/dead) and 5 from Cameroon. No G119S mutations were detected (all wild-type SS).
   - AChE F455W mutation was also analyzed in text but is not in the schema target marker list, so it was omitted.
   - Quantitative P450 gene expression profiling (qPCR for CYP6P9a, CYP6P9b, CYP6P4a, CYP6P4b) measures RNA expression levels, not target allele marker frequencies, and is thus excluded from target genotype tables.

3. **Genotype vs Geno-Pheno**:
   - The 15 Mozambique samples sequenced for AChE G119S were split by bendiocarb bioassay phenotype (8 alive/resistant, 7 dead/susceptible) and recorded in `geno_pheno` to prevent double-counting.
   - The 5 Cameroon samples were recorded in `genotypes` as they were not split by bioassay outcome in this study.

4. **Bioassays**:
   - Extracted all WHO susceptibility tests for 1–3 day old F1 *An. funestus s.s.* from Table 1 (permethrin 0.75%, deltamethrin 0.05%, lambda-cyhalothrin 0.05%, bendiocarb 0.01%, DDT 4%, malathion 5%).
   - Exposure durations range from 60 to 210 minutes as reported. For multitimepoint tests where only total N for the insecticide row was given (e.g., 440 for permethrin across 4 exposure times), `n_exposed` is set to null per time point record to avoid back-calculating unknown per-time-point sample sizes.
