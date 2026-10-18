# Extraction record — 2013_Oxborough_ITN_Mixtures_Chlorfenapyr_Pyrrole_Alphacypermethri_PMID23409042

- Extracted: 2026-10-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 2 · Bioassays: 4 · Geno-pheno rows: 0

## Decisions

# Data Extraction Decisions

- **Target Species:** Only data for *Anopheles arabiensis* were extracted. *Culex quinquefasciatus* data were excluded per project scope.
- **Surveys:** Split into two surveys:
  1. `..._lower_moshi_f1`: Wild adult females collected from cattle sheds in Lower Moshi in November 2011 and reared to F1 progeny for WHO cylinder resistance testing (Table 4).
  2. `..._lower_moshi_hut`: Wild adult *An. arabiensis* entering experimental huts at KCMUCo Field Station in Lower Moshi Rice Irrigation Zone (3°22'S, 37°19'E), from which 80 survivors from the alphacypermethrin ITN hut were genotyped for *kdr* mutations.
- **Marker Names:** The text prints: 'tested for the presence of L1014F and L10145S kdr variants. No kdr mutations were detected'. The typographical error 'L10145S' in the text was recorded as `L1014S` for the marker name to match the target list alias for Vgsc L995S.
- **Genotypes vs. Geno-Pheno:** Only 80 surviving mosquitoes from the alphacypermethrin hut were screened to test for the presence of *kdr* in the population (no dead mosquitoes were genotyped, and no phenotype association analysis was conducted). Consequently, `geno_pheno` is empty and the 80 genotyped mosquitoes (all wild-type SS = 80, RR = 0, RS = 0) are placed in `genotypes`.
- **Bioassays:** WHO cylinder bioassays for lambdacyhalothrin, permethrin, DDT, and fenitrothion are reported in Table 4 with sample sizes and mortality percentages. Experimental hut trials (Table 6) and ITN ball bioassays (Figure 5) were excluded as experimental huts are field trials and ball bioassays did not report sample sizes.
