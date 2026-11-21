# Extraction record — 2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 8 · Genotype rows: 20 · Bioassays: 6 · Geno-pheno rows: 0

## Decisions

### Survey and Genotype Splitting
- Indoor-resting Anopheles females (F0) were collected across three sites in Togo: Kovié (December 2013), Nangbéto (April 2015), and Mango (April 2015).
- Molecular species identification was performed on F0 control mosquitoes (88 in Kovié, 70 in Nangbéto, 58 in Mango). In Kovié, 100% were *An. coluzzii*. In Nangbéto, 41% were *An. coluzzii* (n=29) and 59% *An. gambiae s.s.* (n=41). In Mango, 3% were *An. coluzzii* (n=2) and 97% *An. gambiae s.s.* (n=56).
- Surveys were created per site, collection date, and molecular species to accommodate the species-specific genotype data reported in Table 2.
- Additional `An. gambiae s.l.` surveys were created for the WHO bioassays conducted on F1 progeny, where species breakdown of the bioassay batches was not individually determined.

### Genotype Counts
- Table 2 reports sample sizes (N) and allele frequencies (percentage ± SD) for kdr L1014F, L1014S, N1575Y, and ace-1 G119S. Genotype counts (RR, RS, SS) were not printed; following extraction rules, allele frequencies are reported as 0-1 proportions in `reported_allele_freq` and count fields are left null.

### Bioassays
- Bioassay sample sizes (n_exposed) are obtained from Figure 3 labels. Mortality percentages reported in the text (0% for Kovié permethrin, 8.54% for Nangbéto permethrin, 81.53% for Nangbéto deltamethrin, and 28.67% for Mango deltamethrin) are recorded in `reported_mortality_pct` with `dead_alive_printed = false`.

## Validator warnings

- genotype #1 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_kovie_2013_col, kdr L1014F): frequency only (no raw counts)
- genotype #2 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_kovie_2013_col, kdr L1014S): frequency only (no raw counts)
- genotype #3 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_kovie_2013_col, kdr N1575Y): frequency only (no raw counts)
- genotype #4 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_kovie_2013_col, ace-1 G119S): frequency only (no raw counts)
- genotype #5 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_nangbeto_2015_col, kdr L1014F): frequency only (no raw counts)
- genotype #6 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_nangbeto_2015_col, kdr L1014S): frequency only (no raw counts)
- genotype #7 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_nangbeto_2015_col, kdr N1575Y): frequency only (no raw counts)
- genotype #8 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_nangbeto_2015_col, ace-1 G119S): frequency only (no raw counts)
- genotype #9 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_mango_2015_col, kdr L1014F): frequency only (no raw counts)
- genotype #10 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_mango_2015_col, kdr L1014S): frequency only (no raw counts)
- genotype #11 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_mango_2015_col, kdr N1575Y): frequency only (no raw counts)
- genotype #12 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_mango_2015_col, ace-1 G119S): frequency only (no raw counts)
- genotype #13 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_nangbeto_2015_gam, kdr L1014F): frequency only (no raw counts)
- genotype #14 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_nangbeto_2015_gam, kdr L1014S): frequency only (no raw counts)
- genotype #15 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_nangbeto_2015_gam, kdr N1575Y): frequency only (no raw counts)
- genotype #16 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_nangbeto_2015_gam, ace-1 G119S): frequency only (no raw counts)
- genotype #17 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_mango_2015_gam, kdr L1014F): frequency only (no raw counts)
- genotype #18 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_mango_2015_gam, kdr L1014S): frequency only (no raw counts)
- genotype #19 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_mango_2015_gam, kdr N1575Y): frequency only (no raw counts)
- genotype #20 (2018_Djegbe_First_Report_Presence_L1014S_Knockdown_PMID29707654_mango_2015_gam, ace-1 G119S): frequency only (no raw counts)
