# Extraction record — 1756_3305_6_352

- Extracted: 2026-10-08
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 6 · Bioassays: 8 · Geno-pheno rows: 7

## Decisions

### Spatial and Temporal Resolution
- Surveys were split by village (Itakpako, Itassoumba, Djohounkollé, Ko-Koumolou) and molecular species (An. coluzzii for M form, An. gambiae s.s. for S form) to capture the finest resolution of genotypes.
- A pooled 'An. gambiae s.l.' survey was created for each village to hold the bioassays and the genotype-phenotype (geno_pheno) data, which are reported for the pooled M+S forms.
- Collection dates are July 2011 to June 2012.
- No coordinates were printed in the text, so latitude and longitude are left null.

### Genotypes and Bioassays
- The target marker is Vgsc L995F (kdr Leu-Phe).
- To avoid double counting in the `genotypes` table, we did not extract the pooled 'M+S' genotypes, only the separate M and S genotypes.
- The geno_pheno data are linked to the deltamethrin bioassays of the respective villages.
- In Ko-Koumolou, mortality to deltamethrin was 100%, so there were no survivors (Alive) to genotype; only the Dead group is extracted in geno_pheno.
