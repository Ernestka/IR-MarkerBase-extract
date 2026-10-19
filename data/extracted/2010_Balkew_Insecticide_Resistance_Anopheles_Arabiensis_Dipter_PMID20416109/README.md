# Extraction record — 2010_Balkew_Insecticide_Resistance_Anopheles_Arabiensis_Dipter_PMID20416109

- Extracted: 2026-10-19
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 0 · Bioassays: 9 · Geno-pheno rows: 10

## Decisions

### Survey and Sampling Decisions
- Three field sites in Ethiopia were sampled as larvae/pupae and reared to adults between November 2005 and April 2007: Gorgora, Ghibe River Valley, and Sodere. Coordinates provided in the text (DMS) were converted to decimal degrees.
- Molecular identification confirmed all tested specimens (N=300) were *Anopheles arabiensis*.
- Table 4 presents bioassay data on an F8 DDT-selected laboratory colony maintained in the insectary at ALIPB. Following extraction rules, this artificially selected laboratory line was excluded.

### Bioassays
- Standard WHO susceptibility tests were conducted for 4% DDT, 0.75% permethrin, and 0.05% deltamethrin (1 h exposure, 24 h holding). Results from Table 1 are extracted for each site x insecticide combination.
- Because Table 1 reports only `Number tested` and `Percent mortality` without raw counts of dead or alive individuals, `dead_alive_printed` is set to `false`, and `n_dead` and `n_alive` are left null.

### Genotypes and Genotype-Phenotype
- All genotyped field mosquitoes (N=70: 32 from Gorgora, 38 from Ghibe) were tested after bioassay exposure and reported split by bioassay outcome ('Susceptible' = dead, 'Resistant' = alive) in Table 2.
- In accordance with Rule 6, all genotype counts are entered in `geno_pheno` linked to their respective bioassay IDs, and `genotypes` is left empty to avoid double-counting.
- Sequencing data for 14 randomly chosen specimens reported in Table 3 was performed as a PCR validation subsample and is not extracted separately.
