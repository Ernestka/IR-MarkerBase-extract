# Extraction record — 2016_Yahouedo_Dynamics_Pyrethroid_Resistance_Malaria_Vectors_PMID27378358

- Extracted: 2026-11-20
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 20 · Genotype rows: 20 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

- **Surveys & Genotypes**: Extracted 105 genotype records from Table 4 across 13 villages (Adjozoume, Agbarou, Alabansa, Djohounkole, Idena3, Igbo-abikou, Itasumba, Ketougbekon, Ko-aidjedo, Ko-Dogba, Kokoumolou, Tchaada, Zihan) and 5 sampling windows (June 2012, October 2012, June 2013, October 2013, June 2014) for *Anopheles coluzzii* and *Anopheles gambiae* s.s.
- **Marker Name**: Target marker reported as `f(1014)F` / `1014F` (Vgsc L995F / L1014F).
- **Vsgc 1014S (L995S)**: Allelic discrimination TaqMan assays were run for 1014S, but text confirms 1014S was not detected in any mosquitoes in this study (page 6).
- **Counts & Frequencies**: Table 4 reports allele frequencies `f(1014)F` and `N` (total number of alleles tested). Genotype classes (RR, RS, SS) are not printed, so `rr`, `rs`, `ss`, and `resistant_allele_count` are kept null per Rule 2. Total mosquitoes genotyped (`n_genotyped`) is derived as `N / 2` because mosquitoes are diploid.
- **Bioassays**: WHO tube bioassays using 0.05% deltamethrin are reported visually in Figure 2 as scatter plots across villages and timepoints. Exact numerical counts of exposed/dead/alive or mortality percentages per village are not printed in tables or text. In accordance with Rule 8b, bioassays were omitted to avoid digitizing from plots.
- **Genotype-Phenotype**: Genotyping was performed on non-exposed field female mosquitoes, so no bioassay survivor/dead split genotype data (`geno_pheno`) were reported.
- **Typo Note**: In Table 4, row Ketougbekon June 2013 *An. gambiae*, `N` is printed as `18,00`, which is interpreted as `N = 18` alleles (9 mosquitoes) and noted in `inconsistency_note`.

## Validator warnings

- genotype #1 (2016_Yahouedo_adjozoume_2012_06_col, kdr 1014F): frequency only (no raw counts)
- genotype #2 (2016_Yahouedo_adjozoume_2012_06_gam, kdr 1014F): frequency only (no raw counts)
- genotype #3 (2016_Yahouedo_adjozoume_2012_10_col, kdr 1014F): frequency only (no raw counts)
- genotype #4 (2016_Yahouedo_adjozoume_2012_10_gam, kdr 1014F): frequency only (no raw counts)
- genotype #5 (2016_Yahouedo_adjozoume_2013_06_col, kdr 1014F): frequency only (no raw counts)
- genotype #6 (2016_Yahouedo_adjozoume_2013_06_gam, kdr 1014F): frequency only (no raw counts)
- genotype #7 (2016_Yahouedo_adjozoume_2013_10_gam, kdr 1014F): frequency only (no raw counts)
- genotype #8 (2016_Yahouedo_adjozoume_2014_06_gam, kdr 1014F): frequency only (no raw counts)
- genotype #9 (2016_Yahouedo_agbarou_2012_06_col, kdr 1014F): frequency only (no raw counts)
- genotype #10 (2016_Yahouedo_agbarou_2012_06_gam, kdr 1014F): frequency only (no raw counts)
- genotype #11 (2016_Yahouedo_agbarou_2012_10_col, kdr 1014F): frequency only (no raw counts)
- genotype #12 (2016_Yahouedo_agbarou_2012_10_gam, kdr 1014F): frequency only (no raw counts)
- genotype #13 (2016_Yahouedo_agbarou_2013_06_col, kdr 1014F): frequency only (no raw counts)
- genotype #14 (2016_Yahouedo_agbarou_2013_06_gam, kdr 1014F): frequency only (no raw counts)
- genotype #15 (2016_Yahouedo_agbarou_2013_10_col, kdr 1014F): frequency only (no raw counts)
- genotype #16 (2016_Yahouedo_agbarou_2013_10_gam, kdr 1014F): frequency only (no raw counts)
- genotype #17 (2016_Yahouedo_agbarou_2014_06_col, kdr 1014F): frequency only (no raw counts)
- genotype #18 (2016_Yahouedo_agbarou_2014_06_gam, kdr 1014F): frequency only (no raw counts)
- genotype #19 (2016_Yahouedo_itasumba_2012_06_col, kdr 1014F): frequency only (no raw counts)
- genotype #20 (2016_Yahouedo_ketougbekon_2013_06_gam, kdr 1014F): inconsistent in the paper (values kept as printed) — Table 4 prints N as 18,00, interpreted as N=18 alleles (9 mosquitoes)
- genotype #20 (2016_Yahouedo_ketougbekon_2013_06_gam, kdr 1014F): frequency only (no raw counts)
