# Extraction record — 2017_Kafy_Impact_Insecticide_Resistance_Anopheles_Arabiensis_PMID29229808

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 6 · Genotype rows: 0 · Bioassays: 6 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions
- **Study Design**: Cluster randomized trial in Galabat, Gedarif State, Sudan, comparing LLIN-only arm vs LLIN + IRS arm (deltamethrin IRS in 2012, bendiocarb IRS in 2013-2014).
- **Surveys**: Six arm-and-year specific surveys were created to capture the deltamethrin WHO tube bioassay mean mortalities reported in Table 1 across 2012, 2013, and 2014.
- **Genotypes Dropped**: The paper notes that 1,847 of 1,872 specimens were successfully genotyped for Vgsc-1014F (L995F). However, no exact overall or arm-level numerical allele frequencies or genotype class counts (RR, RS, SS) are printed in the text or tables (they are presented only as cluster-level boxplots in Figure 1). Per extraction Rule 2 and Rule 8, no counts were back-calculated or visually estimated from figures, so no genotype records were added (`genotypes` is `[]`).
- **Bioassays**: Deltamethrin 0.05% discriminating dose bioassays were extracted per year and study arm as presented in Table 1. Number exposed per arm/year was not printed (only the overall study total of 4,680 mosquitoes phenotyped across all 3 years is stated), so n_exposed, n_dead, and n_alive are left null and dead_alive_printed is set to false.
- **Genotype-Phenotype**: The study analyzed ecological correlation between cluster bioassay mortality and cluster allele frequency, but did not publish individual genotype breakdowns by survivor/dead status, so `geno_pheno` is empty.
