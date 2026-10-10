# Extraction record — s12936_017_2156_6

- Extracted: 2026-10-10
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 5 · Genotype rows: 0 · Bioassays: 7 · Geno-pheno rows: 2

## Decisions

### Survey and Bioassay Splitting
- Sampling was carried out in July–August 2015 in Kwale County (two villages: Marigiza [-4.443036, 39.461887] and Kidomaya [-4.578639, 39.157574]).
- As stated on page 5, because no differences in mortality were observed between the two villages, data was analysed together for both villages. Hence, surveys are represented at the Kwale County level (precision: admin1).
- Per Rule 7, bioassays are extracted at the finest species resolution (molecular species: An. arabiensis, An. gambiae s.s., An. funestus s.s., and An. vaneedeni) rather than the pooled complex totals (An. gambiae s.l. and An. funestus s.l.). 'Not amplified' individuals are omitted as they do not constitute a taxon.

### Genotype-Phenotype Data (Table 4)
- Table 4 presents L1014S kdr genotypes broken down by bioassay phenotype: alive (resistant) vs dead (susceptible) 24 hours post-exposure to either deltamethrin or permethrin.
- Although Table 4's title reads 'in Anopheles gambiae s.s.', the text and sample sizes make clear that the 247 genotyped bioassay mosquitoes are Anopheles gambiae s.l. (in the entire study, only 18 An. gambiae s.s. were identified). Footnote and text note that L1014S was only detected in 5 individuals, all confirmed as An. gambiae s.s.
- Because these genotypes are split by bioassay phenotype across pooled insecticides, they are extracted in `geno_pheno` with `bioassay_id = null` and `insecticide = 'deltamethrin or permethrin'`. In accordance with Rule 6, they are not duplicated in `genotypes`.
- The 53 field-collected adults genotyped for kdr (making up the total of 300) are not broken down with explicit counts in any table or text, so they are not extracted in `genotypes` to avoid back-calculating.
- All 300 An. gambiae s.l. tested negative for L1014F (no resistant alleles detected).

## Validator warnings

- geno_pheno #1 (deltamethrin or permethrin, kdr L1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin or permethrin)
- geno_pheno #1 (deltamethrin or permethrin, kdr L1014S, alive): inconsistent in the paper (values kept as printed) — Page 5 text states 79 mosquitoes exhibited the resistance phenotype, but Table 4 prints n = 78 (RR=0, RS=1, SS=77).
- geno_pheno #2 (deltamethrin or permethrin, kdr L1014S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin or permethrin)
