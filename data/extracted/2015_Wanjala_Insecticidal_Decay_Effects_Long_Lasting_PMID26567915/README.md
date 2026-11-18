# Extraction record — 2015_Wanjala_Insecticidal_Decay_Effects_Long_Lasting_PMID26567915

- Extracted: 2026-11-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 13 · Genotype rows: 13 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

# Decisions and Extraction Notes

- **Study Design & Populations**: Mosquitoes were reared to adults from field-collected larvae from 7 study sites in western Kenya: Ahero, Kisian, Chulaimbo, Emutete, Emakakha, Iguhu, and Bungoma. Molecular identification (Scott et al. 1993 rDNA PCR) separated An. gambiae s.s. and An. arabiensis.
- **Surveys**: Surveys were split by site and molecular species. At Emutete, 0 An. arabiensis were genotyped (N=0, N/A in Table 2), so no survey was created for Emutete An. arabiensis. A total of 13 surveys were created (7 for An. gambiae s.s., 6 for An. arabiensis).
- **Genotypes (Table 2)**: Genotyping was performed using a TaqMan assay targeting the L1014S mutation (probe for wild type L, probe for mutant S). In Table 2, the authors denote:
  - `LL`: wild type (homozygous L1014) -> recorded as `ss`
  - `LS`: heterozygote (L1014S) -> recorded as `rs`
  - `SS`: homozygous mutant (1014S/1014S) -> recorded as `rr`
  All genotype counts and allele frequencies reconcile perfectly with this notation.
- **Bioassays**: WHO tube susceptibility tests (deltamethrin 0.05%, permethrin 0.75%, lambda-cyhalothrin 0.05%) were performed on An. gambiae s.l. populations, but mortality results are reported only in a bar chart (Figure 2) without exact numerical values or dead/alive counts in the text or tables. Similarly, cone bioassays on field-collected LLINs and mud slabs were decay monitoring experiments with results presented as graphs or ranges. Therefore, per extraction rules, no bioassay records could be extracted.
- **Genotype-Phenotype**: Genotypes were not reported separately by bioassay outcome (alive vs dead); thus `geno_pheno` is empty.
