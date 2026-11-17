# Extraction record — 2014_Mulamba_Widespread_Pyrethroid_DDT_Resistance_Major_PMID25333491

- Extracted: 2026-11-17
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 0 · Bioassays: 1 · Geno-pheno rows: 2

## Decisions

### Data Extraction Decisions

1. **Study Design & Scope**:
   - Anopheles funestus collections were conducted across six districts in Uganda and one in western Kenya between December 2011 and June 2012.
   - Bioassay data for the full study are provided in Supplementary Table S3 (not included in the main publication text). Only Jinja DDT 4% bioassay is directly linked to target marker genotyping data.
   - Target marker genotyping for GSTe2 L119F was carried out exclusively on 60 mosquitoes (30 DDT-resistant survivors and 30 DDT-susceptible dead) from Jinja, Uganda.

2. **Target Markers**:
   - **GSTe2 L119F**: Tested using TaqMan assay on 30 alive (resistant) and 30 dead (susceptible) F1 adult females following 1 h exposure to 4% DDT. All 30 dead mosquitoes were wild-type (SS), giving an 119F allele frequency of 0.0. In alive mosquitoes, 73.3% were reported as susceptible homozygotes (SS), and the reported 119F frequency in Jinja was 10% (0.10). Because exact counts were not printed in tabular form (only percentages were reported in text and bar plots), `reported_allele_freq` is recorded (0.10 for alive, 0.0 for dead) while `rr`, `rs`, and `ss` count fields remain null per Rule 2.
   - **VGSC**: Exon 20 and intron 19 were sequenced in 79 mosquitoes. Codon 1014 was completely wild-type (no kdr mutations). The substitution F1021C was found in 2 DDT-susceptible mosquitoes from Lira but is not on the target marker list.
   - **CYP6P9a/b**: Assessed only by qRT-PCR gene expression profiling, not DNA marker genotyping.

3. **Genotype-Phenotype Allocation**:
   - Because the 60 genotyped mosquitoes were split according to bioassay outcome (alive vs. dead after DDT exposure), they are recorded under `geno_pheno` and linked to the Jinja DDT bioassay, rather than duplicated under `genotypes`.
