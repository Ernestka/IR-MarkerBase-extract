# Extraction record — 2011_Himeidan_Extensive_Permethrin_DDT_Resistance_Anopheles_PMID21812972

- Extracted: 2026-10-24
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 7 · Genotype rows: 0 · Bioassays: 13 · Geno-pheno rows: 19

## Decisions

### Decisions Readme

1. **Surveys**: Seven distinct mosquito populations were sampled across 5 states in central and eastern Sudan during July - November 2009. Sennar, Damazin, Khartoum, and Kosti represent pooled state samples (combining 2-3 nearby breeding sites <10 km apart), while Mayirno, Al Faw, and Al Shuwak were treated as distinct populations due to greater spatial separation as defined by the authors.
2. **Coordinates**: Reported in text for specific sites (Mayirno, Al Faw, Al Shuwak). For multi-site composite populations (Sennar, Damazin, Khartoum, Kosti), lat/long are set to null and precision is set to town/admin2.
3. **Bioassays**: WHO standard tube assays (0.75% permethrin and 4% DDT, 1-hour exposure, 24-hour mortality) reported in Table 1 and Table 2. Percent mortalities are extracted; raw dead/alive counts were not printed in Table 1 & 2 and are left null in accordance with Rule 2.
4. **Genotypes vs Geno-Pheno**: All 248 genotyped mosquitoes were sampled from bioassay exposures and are reported split by outcome (Dead / Alive) per population in Table 3. Therefore, all genotype data are placed in `geno_pheno` linked to their bioassay IDs, and `genotypes` is left empty to avoid double counting.
5. **Markers**: Paper reports Vgsc 1014F (L1014F/1014F kdr allele). The 1014S allele was screened for in all 248 specimens and was completely absent (0 copies detected). Table 4 gives overall pooled counts across sites, which were excluded to avoid double counting given the site-specific breakdown in Table 3.
