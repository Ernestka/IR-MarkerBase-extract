# Extraction record — s12936_017_2156_6

- Extracted: 2026-10-09
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 5 · Genotype rows: 0 · Bioassays: 7 · Geno-pheno rows: 2

## Decisions

### Survey and Bioassay Resolution
- Mosquitoes were collected in July-August 2015 from two villages in Kwale County, Coastal Kenya: Marigiza (-4.443036, 39.461887) and Kidomaya (-4.578639, 39.157574). As the authors explicitly noted that no differences in mortality rate were observed between the two villages, all bioassay and genotype data were analysed and reported pooled across both villages (Table 3, Table 4). Consequently, surveys are represented at the Kwale County level (spatial_precision: admin1) with coordinates left null.
- In Table 3, bioassay results are reported for both species complexes (pooled) and individual sibling species (identified post-assay by PCR). Per Rule 7, bioassays are extracted at the finest taxonomic resolution (An. arabiensis, An. gambiae s.s., An. funestus s.s., An. vaneedeni), omitting the pooled complex totals (An. gambiae s.l. and An. funestus s.l.) and unamplified specimens. Kisumu laboratory strain positive controls and silicone oil negative controls are excluded.
- In Table 3, only n_exposed and mortality percentages are reported; dead_alive_printed is set to false, and n_dead / n_alive are left null.

### Genotype-Phenotype Data (Table 4)
- Table 4 is titled 'in Anopheles gambiae s.s.', but the sample size of 247 (78 resistant + 169 susceptible) represents all bioassay-tested An. gambiae s.l. mosquitoes genotyped for kdr. In total, only 16 An. gambiae s.s. were tested in bioassays (Table 3), while the remainder were An. arabiensis and unamplified. All five kdr-mutant individuals were An. gambiae s.s., which explains why the table was labelled as such. This dataset is assigned to survey `s12936_017_2156_6_kwale_2015_gambiae_sl`.
- Because survivors and dead mosquitoes were pooled across both deltamethrin and permethrin exposures ('alive 24 h post-exposure to either deltamethrin or permethrin'), bioassay_id is set to null, and insecticide is set to 'deltamethrin + permethrin'.
- In the text on page 5, the authors mention that 79 mosquitoes had exhibited the resistance phenotype, whereas Table 4 reports n = 78 resistant (0 RR, 1 RS, 77 SS). All numbers within Table 4 reconcile internally.
- While 53 field-collected adults were also tested for kdr (and all were wild-type), their genotype counts are not reported in a dedicated table and are not split by phenotype, so they are not extracted to avoid double-counting or deriving counts by subtraction.
- The L1014F mutation was tested in the same 300 mosquitoes, but no L1014F alleles were detected. Because counts are not broken down by phenotype class in Table 4, L1014F is omitted from geno_pheno.

## Validator warnings

- geno_pheno #1 (deltamethrin + permethrin, kdr L1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin + permethrin)
- geno_pheno #2 (deltamethrin + permethrin, kdr L1014S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + permethrin)
