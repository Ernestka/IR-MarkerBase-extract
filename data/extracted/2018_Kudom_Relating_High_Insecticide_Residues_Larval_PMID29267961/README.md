# Extraction record — 2018_Kudom_Relating_High_Insecticide_Residues_Larval_PMID29267961

- Extracted: 2026-11-22
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 0 · Bioassays: 14 · Geno-pheno rows: 1

## Decisions

### Data Extraction Notes

- **Surveys**: Created three collection-date specific surveys corresponding to the distinct sampling dates/breeding site groups (21/07/2016 site H, 10/08/2016 site A, 06/10/2016 sites B-G) for linking bioassay records, and one overall survey for the pooled Akim Oda 2016 population used for kdr genotyping.
- **Bioassays**: Extracted all date-specific WHO tube bioassay records from Table 3. Pooled summary rows ('Mean % mortality ± SEM') were omitted to avoid double counting as per Rule 7. `dead_alive_printed` is set to `false` because Table 3 only printed `% mortality` and `(N)` exposed count.
- **Genotypes & Geno-Pheno**: Methods state that mosquitoes termed resistant (bioassay survivors) were used for molecular analysis of L1014F kdr mutation (20 RR, 9 RS, 2 SS out of N=31). As these mosquitoes represent bioassay survivors pooled across pyrethroids, they are recorded in `geno_pheno` with `phenotype_group = alive`, `bioassay_id = null`, and omitted from `genotypes` to avoid double counting.
- **Target Markers**: Only Vgsc L1014F (L995F) was extracted. Mention of Ace-1 in discussion is a literature reference to previous studies and not primary data from this study.

## Validator warnings

- geno_pheno #1 (deltamethrin + cyfluthrin + permethrin + etofenprox, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin + cyfluthrin + permethrin + etofenprox)
