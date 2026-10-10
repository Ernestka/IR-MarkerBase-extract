# Extraction record — s41598_025_14239_x

- Extracted: 2026-10-10
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 6 · Genotype rows: 42 · Bioassays: 34 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys**: Six surveys were established for the six study sites in Ghana sampled between January 2023 and July 2024: Tamale Fitam, Abossey Okai, Kokompe, Obuasi, Tema Community 1, and Accra Industrial Area. Accurate point coordinates reported on pages 7-8 were extracted for each location.
2. **Genotypes**: Allele frequencies for seven target markers (Vgsc N1570Y, V402L, I1527T, L995F, L995S, P1874L, and Ace-1 G280S) were extracted directly from Table 1 for sample size N=30 at each site. Note that Table 1 prints the column header for Ace-1 as G208S, which is a typo for G280S (described as Ace-1R G280S in the text on pages 2 and 9). The standard marker name Ace-1 G280S was used and the typo noted in `inconsistency_note`.
3. **Species Resolution**: Species discrimination was conducted on a subsample of 40 mosquitoes per site in Table 2, but target-site genotyping in Table 1 was reported at the overall *An. gambiae s.l.* level.
4. **Bioassays**: Bioassay tests were extracted from the text and Figures 1 & 2 for test conditions with reported mortality percentages. Methodological descriptions (page 8) specify 4 replicates of 25 females (n_exposed = 100 per test). Exact dead/alive mosquito counts were not explicitly printed, so `dead_alive_printed` was set to `false` and counts left `null`.

## Validator warnings

- genotype #1 (s41598_025_14239_x_tamale_fitam, Vgsc N1570Y): frequency only (no raw counts)
- genotype #2 (s41598_025_14239_x_tamale_fitam, Vgsc V402L): frequency only (no raw counts)
- genotype #3 (s41598_025_14239_x_tamale_fitam, Vgsc I1527T): frequency only (no raw counts)
- genotype #4 (s41598_025_14239_x_tamale_fitam, Vgsc L995F): frequency only (no raw counts)
- genotype #5 (s41598_025_14239_x_tamale_fitam, Vgsc L995S): frequency only (no raw counts)
- genotype #6 (s41598_025_14239_x_tamale_fitam, Ace-1 G280S): inconsistent in the paper (values kept as printed) — Table 1 header printed as G208S, which is a typographical error for Ace-1 G280S as described in the text.
- genotype #6 (s41598_025_14239_x_tamale_fitam, Ace-1 G280S): frequency only (no raw counts)
- genotype #7 (s41598_025_14239_x_tamale_fitam, Vgsc P1874L): frequency only (no raw counts)
- genotype #8 (s41598_025_14239_x_abossey_okai, Vgsc N1570Y): frequency only (no raw counts)
- genotype #9 (s41598_025_14239_x_abossey_okai, Vgsc V402L): frequency only (no raw counts)
- genotype #10 (s41598_025_14239_x_abossey_okai, Vgsc I1527T): frequency only (no raw counts)
- genotype #11 (s41598_025_14239_x_abossey_okai, Vgsc L995F): frequency only (no raw counts)
- genotype #12 (s41598_025_14239_x_abossey_okai, Vgsc L995S): frequency only (no raw counts)
- genotype #13 (s41598_025_14239_x_abossey_okai, Ace-1 G280S): inconsistent in the paper (values kept as printed) — Table 1 header printed as G208S, which is a typographical error for Ace-1 G280S as described in the text.
- genotype #13 (s41598_025_14239_x_abossey_okai, Ace-1 G280S): frequency only (no raw counts)
- genotype #14 (s41598_025_14239_x_abossey_okai, Vgsc P1874L): frequency only (no raw counts)
- genotype #15 (s41598_025_14239_x_kokompe, Vgsc N1570Y): frequency only (no raw counts)
- genotype #16 (s41598_025_14239_x_kokompe, Vgsc V402L): frequency only (no raw counts)
- genotype #17 (s41598_025_14239_x_kokompe, Vgsc I1527T): frequency only (no raw counts)
- genotype #18 (s41598_025_14239_x_kokompe, Vgsc L995F): frequency only (no raw counts)
- genotype #19 (s41598_025_14239_x_kokompe, Vgsc L995S): frequency only (no raw counts)
- genotype #20 (s41598_025_14239_x_kokompe, Ace-1 G280S): inconsistent in the paper (values kept as printed) — Table 1 header printed as G208S, which is a typographical error for Ace-1 G280S as described in the text.
- genotype #20 (s41598_025_14239_x_kokompe, Ace-1 G280S): frequency only (no raw counts)
- genotype #21 (s41598_025_14239_x_kokompe, Vgsc P1874L): frequency only (no raw counts)
- genotype #22 (s41598_025_14239_x_obuasi, Vgsc N1570Y): frequency only (no raw counts)
- genotype #23 (s41598_025_14239_x_obuasi, Vgsc V402L): frequency only (no raw counts)
- genotype #24 (s41598_025_14239_x_obuasi, Vgsc I1527T): frequency only (no raw counts)
- genotype #25 (s41598_025_14239_x_obuasi, Vgsc L995F): frequency only (no raw counts)
- genotype #26 (s41598_025_14239_x_obuasi, Vgsc L995S): frequency only (no raw counts)
- genotype #27 (s41598_025_14239_x_obuasi, Ace-1 G280S): inconsistent in the paper (values kept as printed) — Table 1 header printed as G208S, which is a typographical error for Ace-1 G280S as described in the text.
- genotype #27 (s41598_025_14239_x_obuasi, Ace-1 G280S): frequency only (no raw counts)
- genotype #28 (s41598_025_14239_x_obuasi, Vgsc P1874L): frequency only (no raw counts)
- genotype #29 (s41598_025_14239_x_tema_c1, Vgsc N1570Y): frequency only (no raw counts)
- genotype #30 (s41598_025_14239_x_tema_c1, Vgsc V402L): frequency only (no raw counts)
- genotype #31 (s41598_025_14239_x_tema_c1, Vgsc I1527T): frequency only (no raw counts)
- genotype #32 (s41598_025_14239_x_tema_c1, Vgsc L995F): frequency only (no raw counts)
- genotype #33 (s41598_025_14239_x_tema_c1, Vgsc L995S): frequency only (no raw counts)
- genotype #34 (s41598_025_14239_x_tema_c1, Ace-1 G280S): inconsistent in the paper (values kept as printed) — Table 1 header printed as G208S, which is a typographical error for Ace-1 G280S as described in the text.
- genotype #34 (s41598_025_14239_x_tema_c1, Ace-1 G280S): frequency only (no raw counts)
- genotype #35 (s41598_025_14239_x_tema_c1, Vgsc P1874L): frequency only (no raw counts)
- genotype #36 (s41598_025_14239_x_accra_ind, Vgsc N1570Y): frequency only (no raw counts)
- genotype #37 (s41598_025_14239_x_accra_ind, Vgsc V402L): frequency only (no raw counts)
- genotype #38 (s41598_025_14239_x_accra_ind, Vgsc I1527T): frequency only (no raw counts)
- genotype #39 (s41598_025_14239_x_accra_ind, Vgsc L995F): frequency only (no raw counts)
- genotype #40 (s41598_025_14239_x_accra_ind, Vgsc L995S): frequency only (no raw counts)
- genotype #41 (s41598_025_14239_x_accra_ind, Ace-1 G280S): inconsistent in the paper (values kept as printed) — Table 1 header printed as G208S, which is a typographical error for Ace-1 G280S as described in the text.
- genotype #41 (s41598_025_14239_x_accra_ind, Ace-1 G280S): frequency only (no raw counts)
- genotype #42 (s41598_025_14239_x_accra_ind, Vgsc P1874L): frequency only (no raw counts)
