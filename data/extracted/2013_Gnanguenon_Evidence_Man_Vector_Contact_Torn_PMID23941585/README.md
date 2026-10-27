# Extraction record — 2013_Gnanguenon_Evidence_Man_Vector_Contact_Torn_PMID23941585

- Extracted: 2026-10-27
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 9 · Genotype rows: 9 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Survey and Genotype Extraction Decisions

1. **Marker Corrected**: Updated `marker` from `'kdr'` to `'L1014F'` so that the target marker (Vgsc L995F / L1014F) is correctly identified by the database schema.
2. **Surveys**: Partitioned by site (Abomey-Takplikpo, Bame, Malanville) and net type arm (non-insecticidal control, PE-150D LLIN, PET-75D LLIN) to preserve the finest breakdown reported in Table 2 and Table 3. Total sample sizes (`total_sample_size`) correspond to the density of *Anopheles gambiae s.l.* collected in each net arm as reported in Table 2.
3. **Genotypes**: Extracted exact genotype counts (SS, RS, RR), total genotyped numbers (N = 320 total across all arm/site combinations), and reported Kdr allele frequencies from Table 3.
4. **Bioassays / Geno_pheno**: No standard WHO bioassays or bioassay-phenotype splits were conducted; field mosquitoes entering torn nets were directly genotyped. Thus, `bioassays` and `geno_pheno` arrays are empty.
