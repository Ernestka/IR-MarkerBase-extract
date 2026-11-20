# Extraction record — 2016_Opondo_Does_Insecticide_Resistance_Contribute_Heterogenei_PMID26980461

- Extracted: 2026-11-20
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 16 · Bioassays: 12 · Geno-pheno rows: 0

## Decisions

1. Markers target-matched: Vgsc-1014F (Vgsc L995F), Vgsc-1014S (Vgsc L995S), Vgsc-1575Y (Vgsc N1570Y), and Ace1-119S (Ace-1 G280S). Gste2-114T was ignored as it is not in the list of target markers.
2. Allele frequencies reported in Table 2 were extracted per species (An. gambiae s.s., An. arabiensis, An. coluzzii, and An. coluzzii x An. gambiae hybrids) across The Gambia. Total genotyped sample sizes per species were only reported as percentages in the text, so counts/sample sizes were left null per Rule 2, with reported_allele_freq set directly.
3. Ace1-119S carrier count (n_carriers = 2) for An. gambiae s.s. was recorded from Page 8 text ('the two mosquitoes that had a carbamate/organophosphate resistance allele, Ace1-119S').
4. Bioassay data from Table 1 were extracted for East vs West regions by species for 4% DDT and 0.05% deltamethrin. Mortality percentages were reported directly; raw counts were not printed in Table 1 so count fields were left null per Rule 2.
5. Genotype-phenotype association analysis in Table 3 was reported as Odds Ratios without explicit raw genotype counts or genotype frequencies for alive/dead groups in the main text, so geno_pheno array is empty.

## Validator warnings

- genotype #1 (2016_Opondo_gambia_2013_gambiae, Vgsc Vgsc-1014F): frequency only (no raw counts)
- genotype #2 (2016_Opondo_gambia_2013_gambiae, Vgsc Vgsc-1014S): frequency only (no raw counts)
- genotype #3 (2016_Opondo_gambia_2013_gambiae, Vgsc Vgsc-1575Y): frequency only (no raw counts)
- genotype #5 (2016_Opondo_gambia_2013_arab, Vgsc Vgsc-1014F): frequency only (no raw counts)
- genotype #6 (2016_Opondo_gambia_2013_arab, Vgsc Vgsc-1014S): frequency only (no raw counts)
- genotype #7 (2016_Opondo_gambia_2013_arab, Vgsc Vgsc-1575Y): frequency only (no raw counts)
- genotype #8 (2016_Opondo_gambia_2013_arab, Ace-1 Ace1-119S): frequency only (no raw counts)
- genotype #9 (2016_Opondo_gambia_2013_coluzzii, Vgsc Vgsc-1014F): frequency only (no raw counts)
- genotype #10 (2016_Opondo_gambia_2013_coluzzii, Vgsc Vgsc-1014S): frequency only (no raw counts)
- genotype #11 (2016_Opondo_gambia_2013_coluzzii, Vgsc Vgsc-1575Y): frequency only (no raw counts)
- genotype #12 (2016_Opondo_gambia_2013_coluzzii, Ace-1 Ace1-119S): frequency only (no raw counts)
- genotype #13 (2016_Opondo_gambia_2013_hybrid, Vgsc Vgsc-1014F): frequency only (no raw counts)
- genotype #14 (2016_Opondo_gambia_2013_hybrid, Vgsc Vgsc-1014S): frequency only (no raw counts)
- genotype #15 (2016_Opondo_gambia_2013_hybrid, Vgsc Vgsc-1575Y): frequency only (no raw counts)
- genotype #16 (2016_Opondo_gambia_2013_hybrid, Ace-1 Ace1-119S): frequency only (no raw counts)
