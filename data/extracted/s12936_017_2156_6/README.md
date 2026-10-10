# Extraction record — s12936_017_2156_6

- Extracted: 2026-10-10
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 6 · Genotype rows: 2 · Bioassays: 7 · Geno-pheno rows: 2

## Decisions

### Survey and Sampling Decisions
- Mosquito collections took place in July and August 2015 in two villages in Kwale County, Kenya: Marigiza (-4.443036, 39.461887) and Kidomaya (-4.578639, 39.157574).
- The authors pooled data from Marigiza and Kidomaya for bioassay and resistance analysis because no significant difference was observed between villages ('Kidomaya and Marigiza mortality rate data was analysed together for both villages (Table 3)'). Consequently, surveys covering bioassays and resistance testing represent Kwale County at the admin2 level.
- Bioassays in Table 3 were extracted at the molecular species level (An. arabiensis, An. gambiae s.s., An. funestus s.s., and An. vaneedeni) following Rule 7. Unamplified specimens and pooled complex totals were omitted to avoid double counting.
- In Table 3, only total exposed and mortality percentages are printed (e.g. '95 (61.05)'). Per Rule 2, n_exposed and reported_mortality_pct are retained while n_dead and n_alive are set to null and dead_alive_printed = false.

### Genotypes and Geno-Pheno Decisions
- 300 An. gambiae s.l. were genotyped for Vgsc L1014S and L1014F (53 wild-caught adults, 247 bioassay-exposed mosquitoes).
- Table 4 reports L1014S genotypes split by bioassay phenotype (resistant/alive vs susceptible/dead). These are extracted into `geno_pheno`. Note that Table 4 is titled 'in Anopheles gambiae s.s.' but the sample size N = 247 (78 + 169) encompasses An. gambiae s.l. across both permethrin and deltamethrin tests (only 18 An. gambiae s.s. were collected in total across the entire study, of which 16 were bioassayed). The 5 detected L1014S mutants were molecularly confirmed as An. gambiae s.s., whereas all An. arabiensis were wild-type SS.
- Because survivors and dead in Table 4 are pooled across deltamethrin and permethrin, bioassay_id is set to null with insecticide = 'deltamethrin or permethrin'.
- There is a minor discrepancy noted in `inconsistency_note`: the text on page 5 states 79 exhibited the resistance phenotype, whereas Table 4 gives N = 78 resistant.
- The 53 wild adults not exposed to bioassays were genotyped for L1014S and L1014F. Since all 5 L1014S mutant carriers in the study were in the bioassay group (Table 4), 0 mutant alleles were found in the 53 adults (RR=0, RS=0, SS=53). No L1014F was detected in any of the 300 mosquitoes, so L1014F is also RR=0, RS=0, SS=53.

## Validator warnings

- geno_pheno #1 (deltamethrin or permethrin, Vgsc L1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin or permethrin)
- geno_pheno #1 (deltamethrin or permethrin, Vgsc L1014S, alive): inconsistent in the paper (values kept as printed) — Text on page 5 states 79 mosquitoes exhibited the resistance phenotype, but Table 4 reports n = 78 resistant mosquitoes. Table 4 title states 'in Anopheles gambiae s.s.' but n = 78 reflects An. gambiae s.l. resistant across bioassays.
- geno_pheno #2 (deltamethrin or permethrin, Vgsc L1014S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin or permethrin)
- geno_pheno #2 (deltamethrin or permethrin, Vgsc L1014S, dead): inconsistent in the paper (values kept as printed) — Table 4 title states 'in Anopheles gambiae s.s.' but n = 169 reflects An. gambiae s.l. susceptible across bioassays.
