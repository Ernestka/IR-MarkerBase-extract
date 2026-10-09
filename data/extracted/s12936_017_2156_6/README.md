# Extraction record — s12936_017_2156_6

- Extracted: 2026-10-09
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 5 · Genotype rows: 0 · Bioassays: 7 · Geno-pheno rows: 2

## Decisions

# Decisions and Extraction Notes

- **Sites and Spatial Pooling**: Mosquitoes were collected in July and August 2015 in two villages in Kwale County, Coastal Kenya: Marigiza (lat -4.443036, long 39.461887) and Kidomaya (lat -4.578639, long 39.157574). However, as stated in the text (page 5): 'As no differences in mortality rate was observed between the two villages, Kidomaya and Marigiza mortality rate data was analysed together for both villages (Table 3).' Neither bioassay results nor genotype results were reported separately by village. Consequently, surveys are defined at the admin1 level (Kwale County, with both villages pooled) and coordinates are left null to avoid fabricating an averaged point.

- **Species Resolution**: Bioassay results in Table 3 are extracted at the molecular species level (An. arabiensis, An. gambiae s.s., An. funestus s.s., and An. vaneedeni), omitting the pooled complex/group totals per extraction rules. Unamplified PCR groups in Table 3 were not extracted as they do not represent species.

- **Table 4 Species Attribution**: Table 4 is titled 'Frequency of Knockdown resistance allele in relation to phenotypes determined by WHO susceptibility bioassay in Anopheles gambiae s.s.' However, the total number of tested individuals in Table 4 is 247 (78 resistant + 169 susceptible), which corresponds precisely to the 247 bioassay-tested An. gambiae s.l. described on page 5 ('Out of the 300 mosquitoes, 53 were from field collected adults while 247 were from the adults used for the bioassay'). Across the entire study, only 16 An. gambiae s.s. were tested in bioassays (Table 3) and only 18 were collected in total (Table 1). The text explicitly explains that among the 247 bioassay mosquitoes, only 5 individuals carried the L1014S mutation and all 5 were identified as An. gambiae s.s., with no kdr mutation detected in An. arabiensis. Therefore, Table 4 represents the bioassay-exposed An. gambiae s.l. cohort (pooled across sibling species), and is linked to survey `s12936_017_2156_6_kwale_2015_gambsl`.

- **Genotype-Phenotype Linking**: The genotyped mosquitoes in Table 4 were pooled across survivors and non-survivors of both deltamethrin and permethrin ('alive 24 h post-exposure to either deltamethrin or permethrin'). Thus, `bioassay_id` is set to null, and `insecticide` is recorded as 'deltamethrin + permethrin'. Per Rule 6, these mosquitoes are extracted in `geno_pheno` and not duplicated in `genotypes`.

- **Field-Collected Adult Genotypes**: The paper notes that 53 field-collected adult An. gambiae s.l. were also genotyped (total 300 genotyped) and no kdr alleles were detected in them (all 5 mutant carriers were in the bioassay cohort). However, no table or raw genotype counts specifically breaking down these 53 individuals are provided, so they are not included in `genotypes`.

## Validator warnings

- geno_pheno #1 (deltamethrin + permethrin, kdr L1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin + permethrin)
- geno_pheno #2 (deltamethrin + permethrin, kdr L1014S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + permethrin)
