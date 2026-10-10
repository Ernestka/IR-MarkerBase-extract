# Extraction record — s12936_020_03388_1

- Extracted: 2026-10-10
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 26 · Bioassays: 8 · Geno-pheno rows: 24

## Decisions

1. Study Sites & Pooling: Mosquitoes were sampled in two villages in Northern Ghana: Kpalsogu (9.33° N, 1.02° W) and Libga (9.35° N, 0.51° W). Because the authors pooled all data from both study sites ('Data from both study sites were pooled together as there was no significant difference in the results obtained', page 5), surveys are established at the pooled village level ('Kpalsogu and Libga') with null point coordinates (reported village coordinates noted in provenance and this README).
2. Surveys: Split by resting location (indoor aspirator vs outdoor pit traps), molecular species (An. arabiensis, An. coluzzii, An. gambiae s.s., An. coluzzii/gambiae s.s. hybrids), and generation (wild adult F0 vs reared F1 progeny).
3. Markers extracted: Target markers evaluated were Vgsc-1014F (L995F), Vgsc-1014S (L995S), Vgsc-1575Y (N1570Y), and Ace1-119S (G280S). GSTe2-114T was excluded as it is not an extraction target.
4. Genotypes table: Table 2 reports allele frequencies (proportions) and sample sizes (N) for wild F0 populations. Since genotype class counts (RR/RS/SS) were not provided, counts are left null and frequencies recorded in reported_allele_freq. For indoor An. arabiensis Vgsc-1575Y and Ace1-119S, N was omitted in Table 2 and is left null.
5. Inconsistency notes: In Table 2, Ace1-119S frequency for An. coluzzii is printed as 0.01 for both indoor and outdoor, whereas the text on page 7 states the prevalence was 0.1.
6. Bioassays: WHO tube test mortalities (24h post-exposure) for F1 An. coluzzii exposed to 4% DDT, 0.05% deltamethrin, 0.1% bendiocarb, and 5% malathion are reported as percentages in the text and Figure 2. Exact counts per insecticide were in Additional file 1 (not provided in main text), so n_exposed, n_dead, and n_alive are null, with dead_alive_printed = false.
7. Geno-pheno: Table 1 reports allele frequencies for bioassay dead and alive F1 An. coluzzii. Genotype class counts and arm-specific sample sizes are not reported, so raw counts and n are left null, with reported_allele_freq capturing the printed proportions, each linked to the corresponding bioassay.

## Validator warnings

- genotype #1 (s12936_020_03388_1_f0_arabiensis_indoor, Vgsc Vgsc-1014F): frequency only (no raw counts)
- genotype #2 (s12936_020_03388_1_f0_arabiensis_indoor, Vgsc Vgsc-1014S): frequency only (no raw counts)
- genotype #3 (s12936_020_03388_1_f0_arabiensis_indoor, Vgsc Vgsc-1575Y): frequency only (no raw counts)
- genotype #4 (s12936_020_03388_1_f0_arabiensis_indoor, Ace1 Ace1-119S): frequency only (no raw counts)
- genotype #5 (s12936_020_03388_1_f0_arabiensis_outdoor, Vgsc Vgsc-1014F): frequency only (no raw counts)
- genotype #6 (s12936_020_03388_1_f0_arabiensis_outdoor, Vgsc Vgsc-1014S): frequency only (no raw counts)
- genotype #7 (s12936_020_03388_1_f0_arabiensis_outdoor, Vgsc Vgsc-1575Y): frequency only (no raw counts)
- genotype #8 (s12936_020_03388_1_f0_arabiensis_outdoor, Ace1 Ace1-119S): frequency only (no raw counts)
- genotype #9 (s12936_020_03388_1_f0_coluzzii_indoor, Vgsc Vgsc-1014F): frequency only (no raw counts)
- genotype #10 (s12936_020_03388_1_f0_coluzzii_indoor, Vgsc Vgsc-1014S): frequency only (no raw counts)
- genotype #11 (s12936_020_03388_1_f0_coluzzii_indoor, Vgsc Vgsc-1575Y): frequency only (no raw counts)
- genotype #12 (s12936_020_03388_1_f0_coluzzii_indoor, Ace1 Ace1-119S): inconsistent in the paper (values kept as printed) — Table 2 reports allele frequency 0.01 with N=364 for indoor An. coluzzii, but page 7 text states the prevalence was 0.1 in indoor and outdoor An. coluzzii.
- genotype #12 (s12936_020_03388_1_f0_coluzzii_indoor, Ace1 Ace1-119S): frequency only (no raw counts)
- genotype #13 (s12936_020_03388_1_f0_coluzzii_outdoor, Vgsc Vgsc-1014F): frequency only (no raw counts)
- genotype #14 (s12936_020_03388_1_f0_coluzzii_outdoor, Vgsc Vgsc-1014S): frequency only (no raw counts)
- genotype #15 (s12936_020_03388_1_f0_coluzzii_outdoor, Vgsc Vgsc-1575Y): frequency only (no raw counts)
- genotype #16 (s12936_020_03388_1_f0_coluzzii_outdoor, Ace1 Ace1-119S): inconsistent in the paper (values kept as printed) — Table 2 reports allele frequency 0.01 with N=401 for outdoor An. coluzzii, but page 7 text states the prevalence was 0.1 in indoor and outdoor An. coluzzii.
- genotype #16 (s12936_020_03388_1_f0_coluzzii_outdoor, Ace1 Ace1-119S): frequency only (no raw counts)
- genotype #17 (s12936_020_03388_1_f0_gambiae_indoor, Vgsc Vgsc-1014F): frequency only (no raw counts)
- genotype #18 (s12936_020_03388_1_f0_gambiae_indoor, Vgsc Vgsc-1014S): frequency only (no raw counts)
- genotype #19 (s12936_020_03388_1_f0_gambiae_indoor, Vgsc Vgsc-1575Y): frequency only (no raw counts)
- genotype #20 (s12936_020_03388_1_f0_gambiae_indoor, Ace1 Ace1-119S): frequency only (no raw counts)
- genotype #21 (s12936_020_03388_1_f0_gambiae_outdoor, Vgsc Vgsc-1014F): frequency only (no raw counts)
- genotype #22 (s12936_020_03388_1_f0_gambiae_outdoor, Vgsc Vgsc-1014S): frequency only (no raw counts)
- genotype #23 (s12936_020_03388_1_f0_gambiae_outdoor, Vgsc Vgsc-1575Y): frequency only (no raw counts)
- genotype #24 (s12936_020_03388_1_f0_gambiae_outdoor, Ace1 Ace1-119S): frequency only (no raw counts)
- genotype #25 (s12936_020_03388_1_f0_hybrid_indoor, Vgsc Vgsc-1014F): frequency only (no raw counts)
- genotype #26 (s12936_020_03388_1_f0_hybrid_outdoor, Vgsc Vgsc-1014F): frequency only (no raw counts)
