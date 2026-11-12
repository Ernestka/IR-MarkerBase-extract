# Extraction record — 2010_Choi_Comparison_DNA_Sequencing_Hydrolysis_Probe_PMID20937156

- Extracted: 2026-11-12
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 2 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

- **Survey**: Single survey of 52 *Anopheles gambiae* mosquitoes collected indoors in Pointe-Noire, Republic of the Congo in April 2009. Molecular identification revealed 51 S-form individuals and 1 M/S hybrid (which carried both *kdr* mutations).
- **Genotypes**: DNA sequencing results from Table 1 are extracted as the reference genotype data. Hydrolysis probe (TaqMan) results before and after axis adjustment are also reported in Table 1 but excluded from `genotypes` to prevent double counting.
- **Multi-allelic Codon Breakdown (Rule 4b)**: Total genotyped = 52. Printed DNA sequence counts in Table 1:
  - Phe-Phe (F/F) = 14
  - Ser-Ser (S/S) = 7
  - Ser-Phe (F/S) = 29
  - Phe-Leu (F/L) = 1
  - Ser-Leu (S/L) = 1
  - Leu-Leu (L/L, wild-type) = 0
  - **For Vgsc L1014F**: RR = 14 (Phe-Phe), RS = 30 (29 Ser-Phe + 1 Phe-Leu), SS = 8 (7 Ser-Ser + 1 Ser-Leu + 0 Leu-Leu).
  - **For Vgsc L1014S**: RR = 7 (Ser-Ser), RS = 30 (29 Ser-Phe + 1 Ser-Leu), SS = 15 (14 Phe-Phe + 1 Phe-Leu + 0 Leu-Leu).
  - True wild-type count (L/L) = 0.
- **Bioassays & Geno-Pheno**: Bioassay mortalities are mentioned in the discussion as cited from another study (Koekemoer et al., submitted), so no bioassays or genotype-phenotype links were extracted for this paper.
