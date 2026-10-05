# Extraction record — s13071_021_04706_5

- Extracted: 2026-10-05
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 9 · Genotype rows: 2 · Bioassays: 5 · Geno-pheno rows: 0

## Decisions

- **Typo Correction in Table 3**: For the 'Susceptible to pyrethroids' row, the paper lists N = 34, RR = 2, RS = 1, SS = 33. However, 2 + 1 + 33 = 36. The reported allele frequency F is 0.0735, which corresponds to (2*2 + 1) / (2*34) = 5/68 = 0.0735. This confirms N is indeed 34, and SS is a typo for 31. We corrected SS to 31 for the overall population genotype calculation.
- **Pooled Genotypes**: Genotypes are only reported pooled across all sites in Table 3. We created a pooled survey for An. gambiae (s.s.) in Kilifi County to hold these genotypes.
- **Bioassays**: Extracted the 5 bioassays with explicit sample sizes and mortality rates reported in the text. Other bioassays with 100% mortality were not extracted because exact sample sizes per test were not uniquely determined for all sites.
- **Geno-Pheno**: No geno_pheno records were created because the genotype-phenotype data in Table 3 is pooled across 'pyrethroids' (deltamethrin and permethrin) and cannot be linked to a single specific bioassay.
