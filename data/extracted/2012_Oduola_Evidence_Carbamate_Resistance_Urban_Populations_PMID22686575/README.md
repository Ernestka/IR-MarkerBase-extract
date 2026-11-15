# Extraction record — 2012_Oduola_Evidence_Carbamate_Resistance_Urban_Populations_PMID22686575

- Extracted: 2026-11-15
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 11 · Genotype rows: 11 · Bioassays: 33 · Geno-pheno rows: 0

## Decisions

### Survey Structure and Species Identification
- Mosquito larvae were collected across 11 urban communities in Lagos State between June and August 2010.
- Molecular identification by PCR-RFLP confirmed that all tested individuals were An. gambiae s.s. molecular M form (now classified as Anopheles coluzzii).
- Coordinates are stated for Lagos State as a whole (3° 24' E, 6° 27' N) but site-specific coordinates are not reported, so latitude and longitude are left null.

### Genotypes
- Genotype counts for kdr-w (Vgsc L995F) are taken from Table 3 (20 mosquitoes analysed per locality).
- In Table 3 for Bariga, printed counts SS=10, RS=0, RR=8 sum to 18, whereas N is printed as 20; this mismatch is documented in the inconsistency_note.
- In Table 3 for Ikoyi, printed counts SS=11, RS=0, RR=8 sum to 19, whereas N is printed as 20; this mismatch is documented in the inconsistency_note.
- The authors report calculating allelic frequencies using the Hardy-Weinberg equation (specifically sqrt(RR/N)), which yields the reported frequencies (e.g. sqrt(8/20) = 0.63 for Bariga and Ikoyi).
- The paper notes that kdr-e (Vgsc L995S) and ace-1R (Ace-1 G280S) were assayed in 'at least 20 sub-samples selected from each population' and found to be absent in all populations. Because site-specific exact sample sizes are not uniquely stated beyond 'at least 20', individual genotype rows for these negative markers are omitted.

### Bioassays
- Standard WHO tube bioassays with 4% DDT, 0.05% deltamethrin, and 0.1% propoxur are extracted. n_exposed values are reported in Table 1 and 24-hour mortality percentages are reported in Figure 2. Numbers dead/alive are not printed, so n_dead and n_alive are left null with dead_alive_printed = false.
- In Table 1, n_exposed for Bariga DDT is left blank, but Figure 2 shows 5% mortality; n_exposed is recorded as null.
- Synergist assays with PBO and bendiocarb tests are presented only as pooled boxplots in Figure 3 without site-specific numerical data and could not be extracted.
- Laboratory control tests using the Kisumu reference strain are excluded.

### Genotype-Phenotype
- No genotype data stratified by bioassay outcome (alive vs dead) are reported in the paper (Table 2 reports only molecular species/form breakdown of resistant vs susceptible samples, not target resistance markers).

## Validator warnings

- genotype #1 (oduola_2012_badagry, Vgsc kdr-w): computed allele freq 0.300 differs from reported 0.55
- genotype #2 (oduola_2012_mile2, Vgsc kdr-w): computed allele freq 0.300 differs from reported 0.55
- genotype #3 (oduola_2012_isaga, Vgsc kdr-w): computed allele freq 0.600 differs from reported 0.77
- genotype #4 (oduola_2012_bariga, Vgsc kdr-w): inconsistent in the paper (values kept as printed) — Printed genotype counts do not sum to N: SS (10) + RS (0) + RR (8) = 18, whereas N is printed as 20.
- genotype #4 (oduola_2012_bariga, Vgsc kdr-w): RR+RS+SS = 8+0+10 = 18 but n_genotyped = 20
- genotype #4 (oduola_2012_bariga, Vgsc kdr-w): computed allele freq 0.444 differs from reported 0.63
- genotype #5 (oduola_2012_ikorodu, Vgsc kdr-w): computed allele freq 0.550 differs from reported 0.74
- genotype #6 (oduola_2012_ikoyi, Vgsc kdr-w): inconsistent in the paper (values kept as printed) — Printed genotype counts do not sum to N: SS (11) + RS (0) + RR (8) = 19, whereas N is printed as 20.
- genotype #6 (oduola_2012_ikoyi, Vgsc kdr-w): RR+RS+SS = 8+0+11 = 19 but n_genotyped = 20
- genotype #6 (oduola_2012_ikoyi, Vgsc kdr-w): computed allele freq 0.421 differs from reported 0.63
- genotype #7 (oduola_2012_mile12, Vgsc kdr-w): computed allele freq 0.300 differs from reported 0.55
- genotype #8 (oduola_2012_egbeda, Vgsc kdr-w): computed allele freq 0.350 differs from reported 0.59
- genotype #9 (oduola_2012_iyana_iba, Vgsc kdr-w): computed allele freq 0.250 differs from reported 0.45
- genotype #10 (oduola_2012_okokomaiko, Vgsc kdr-w): computed allele freq 0.300 differs from reported 0.55
- genotype #11 (oduola_2012_isheri_ikotun, Vgsc kdr-w): computed allele freq 0.250 differs from reported 0.45
