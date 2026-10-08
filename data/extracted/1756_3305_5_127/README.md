# Extraction record — 1756_3305_5_127

- Extracted: 2026-10-08
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 6 · Genotype rows: 11 · Bioassays: 37 · Geno-pheno rows: 0

## Decisions

- **Surveys**: Split by site (Kodeni, Dioulassoba) and molecular species (An. arabiensis, An. gambiae S form, An. gambiae M form) to achieve the finest taxonomic resolution.
- **Species Mapping**: S form is mapped to `An. gambiae s.s.` and M form is mapped to `An. coluzzii`.
- **Bioassays**: Extracted from Table 3, which provides species-specific counts of survivors and dead for each site and month (September and November 2008). This represents the finest taxonomic resolution, so the pooled totals in Table 2 were not extracted to avoid double counting.
- **Genotypes**: Vgsc L1014F genotypes are extracted from Table 4. Ace-1 G119S genotypes are extracted from Table 5. Both are pooled across bioassays as described in the text.
- **Geno-Pheno**: No geno_pheno data was extracted because the exact genotype counts split by phenotype (survivors vs dead) were not uniquely determined for all groups in the text.
