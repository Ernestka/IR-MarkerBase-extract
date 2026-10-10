# Extraction record — s12936_024_05069_9

- Extracted: 2026-10-10
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 6 · Genotype rows: 18 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Study and Surveys
- Collections were conducted longitudinally in Goden village, central region of Burkina Faso, in three distinct years: 2011 (pyrethrum spray catches and sticky resting boxes indoors/outdoors) and 2015 and 2020 (indoor/outdoor human landing catches).
- Two species from the Anopheles gambiae complex were analyzed: Anopheles coluzzii and Anopheles arabiensis. Each year x species combination forms a distinct survey (6 surveys total).

### Genotypes
- Genotyping investigated three VGSC target-site mutations: L1014F (L995F), L1014S (L995S), and V402L.
- Tables 1 and 2 report sample sizes (N) and genotype percentages rather than integer counts. In accordance with Rule 2, RR, RS, and SS integer fields were left null to avoid calculating counts from percentages; the reported allele frequencies printed in Figures 1 and 2 and in the text are captured in `reported_allele_freq`.
- For An. arabiensis V402L in 2011, the text explicitly notes: 'Finally, 402L mutation is detected in heterozygosis in a single An. arabiensis specimen collected in 2011 (Table 2)', so `n_carriers = 1` was recorded for that survey.
- L1014S was genotyped in An. coluzzii but not observed in any year (`reported_allele_freq = 0.0`, `n_carriers = 0`).

### Bioassays & Genotype-Phenotype
- No bioassays were conducted in this study; therefore, the `bioassays` and `geno_pheno` arrays are empty.

## Validator warnings

- genotype #1 (s12936_024_05069_9_goden_2011_col, Vgsc L1014F): frequency only (no raw counts)
- genotype #3 (s12936_024_05069_9_goden_2011_col, Vgsc V402L): frequency only (no raw counts)
- genotype #4 (s12936_024_05069_9_goden_2015_col, Vgsc L1014F): frequency only (no raw counts)
- genotype #6 (s12936_024_05069_9_goden_2015_col, Vgsc V402L): frequency only (no raw counts)
- genotype #7 (s12936_024_05069_9_goden_2020_col, Vgsc L1014F): frequency only (no raw counts)
- genotype #9 (s12936_024_05069_9_goden_2020_col, Vgsc V402L): frequency only (no raw counts)
- genotype #10 (s12936_024_05069_9_goden_2011_ara, Vgsc L1014F): frequency only (no raw counts)
- genotype #11 (s12936_024_05069_9_goden_2011_ara, Vgsc L1014S): frequency only (no raw counts)
- genotype #13 (s12936_024_05069_9_goden_2015_ara, Vgsc L1014F): frequency only (no raw counts)
- genotype #14 (s12936_024_05069_9_goden_2015_ara, Vgsc L1014S): frequency only (no raw counts)
- genotype #16 (s12936_024_05069_9_goden_2020_ara, Vgsc L1014F): frequency only (no raw counts)
- genotype #17 (s12936_024_05069_9_goden_2020_ara, Vgsc L1014S): frequency only (no raw counts)
