# Extraction record — s12936_020_03388_1

- Extracted: 2026-10-10
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 26 · Bioassays: 8 · Geno-pheno rows: 24

## Decisions

### Survey and Study Design Decisions
- **Site pooling**: Mosquitoes were collected in two rural villages in Northern Ghana: Kpalsogu (9.33° N, 1.02° W) and Libga (9.35° N, 0.51° W). Because the authors pooled data across both study sites for all subsequent analyses ('Data from both study sites were pooled together as there was no significant difference in the results obtained', page 5), surveys are established at the pooled level ('Kpalsogu and Libga') with spatial precision 'admin2' and null coordinates.
- **Stratification**: Data are split by resting behavior (indoor vs outdoor) and molecular species (An. arabiensis, An. coluzzii, An. gambiae s.s., and An. coluzzii/gambiae s.s. hybrids).
- **Target markers**: Screened markers included Vgsc-1014F (L995F), Vgsc-1014S (L995S), Vgsc-1575Y (N1570Y), Ace1-119S (G280S), and GSTe2-114T. GSTe2-114T is not in the predefined target marker list (which only includes GSTe2 L119F in An. funestus) and was excluded.
- **Genotypes vs Geno_pheno**: Table 2 contains baseline allele frequencies and sample sizes for wild-caught F0 adults not split by bioassay status; these are recorded in `genotypes`. Table 1 contains allele frequencies of F1 An. coluzzii split by bioassay phenotype (dead vs alive); these are extracted into `geno_pheno` and linked directly to the corresponding bioassays.
- **Counts vs Frequencies**: The paper reports only allele frequencies and total N per group without diploid genotype class breakdowns (RR, RS, SS counts); per extraction rules, count fields are left null and only reported_allele_freq is recorded. For bioassays, individual counts per insecticide were in supplementary Table S1, so only reported mortality percentages are extracted, leaving n_exposed/n_dead/n_alive null and dead_alive_printed false.

## Validator warnings

- genotype #1 (s12936_020_03388_1_f0_arabiensis_indoor, Vgsc 1014F): frequency only (no raw counts)
- genotype #2 (s12936_020_03388_1_f0_arabiensis_indoor, Vgsc 1014S): frequency only (no raw counts)
- genotype #3 (s12936_020_03388_1_f0_arabiensis_indoor, Vgsc 1575Y): frequency only (no raw counts)
- genotype #4 (s12936_020_03388_1_f0_arabiensis_indoor, Ace1 119S): frequency only (no raw counts)
- genotype #5 (s12936_020_03388_1_f0_arabiensis_outdoor, Vgsc 1014F): frequency only (no raw counts)
- genotype #6 (s12936_020_03388_1_f0_arabiensis_outdoor, Vgsc 1014S): frequency only (no raw counts)
- genotype #7 (s12936_020_03388_1_f0_arabiensis_outdoor, Vgsc 1575Y): frequency only (no raw counts)
- genotype #8 (s12936_020_03388_1_f0_arabiensis_outdoor, Ace1 119S): frequency only (no raw counts)
- genotype #9 (s12936_020_03388_1_f0_coluzzii_indoor, Vgsc 1014F): frequency only (no raw counts)
- genotype #10 (s12936_020_03388_1_f0_coluzzii_indoor, Vgsc 1014S): frequency only (no raw counts)
- genotype #11 (s12936_020_03388_1_f0_coluzzii_indoor, Vgsc 1575Y): frequency only (no raw counts)
- genotype #12 (s12936_020_03388_1_f0_coluzzii_indoor, Ace1 119S): frequency only (no raw counts)
- genotype #13 (s12936_020_03388_1_f0_coluzzii_outdoor, Vgsc 1014F): frequency only (no raw counts)
- genotype #14 (s12936_020_03388_1_f0_coluzzii_outdoor, Vgsc 1014S): frequency only (no raw counts)
- genotype #15 (s12936_020_03388_1_f0_coluzzii_outdoor, Vgsc 1575Y): frequency only (no raw counts)
- genotype #16 (s12936_020_03388_1_f0_coluzzii_outdoor, Ace1 119S): frequency only (no raw counts)
- genotype #17 (s12936_020_03388_1_f0_gambiae_indoor, Vgsc 1014F): frequency only (no raw counts)
- genotype #18 (s12936_020_03388_1_f0_gambiae_indoor, Vgsc 1014S): frequency only (no raw counts)
- genotype #19 (s12936_020_03388_1_f0_gambiae_indoor, Vgsc 1575Y): frequency only (no raw counts)
- genotype #20 (s12936_020_03388_1_f0_gambiae_indoor, Ace1 119S): frequency only (no raw counts)
- genotype #21 (s12936_020_03388_1_f0_gambiae_outdoor, Vgsc 1014F): frequency only (no raw counts)
- genotype #22 (s12936_020_03388_1_f0_gambiae_outdoor, Vgsc 1014S): frequency only (no raw counts)
- genotype #23 (s12936_020_03388_1_f0_gambiae_outdoor, Vgsc 1575Y): frequency only (no raw counts)
- genotype #24 (s12936_020_03388_1_f0_gambiae_outdoor, Ace1 119S): frequency only (no raw counts)
- genotype #25 (s12936_020_03388_1_f0_hybrid_indoor, Vgsc 1014F): frequency only (no raw counts)
- genotype #26 (s12936_020_03388_1_f0_hybrid_outdoor, Vgsc 1014F): frequency only (no raw counts)
