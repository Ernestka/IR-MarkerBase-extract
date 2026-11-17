# Extraction record — 2015_Riveron_Rise_Multiple_Insecticide_Resistance_Anopheles_PMID26370361

- Extracted: 2026-11-17
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 2 · Bioassays: 14 · Geno-pheno rows: 4

## Decisions

### Study and Survey Structure
- Mosquitoes were collected in Chikwawa district (16°1′S; 34°47′E), southern Malawi, in January 2014.
- Three surveys were defined to clearly distinguish wild adults from reared F1 progeny and separate species:
  1. `..._funestus_f0`: Field-collected F0 Anopheles funestus s.s. females (wild_adult) used for population genotyping.
  2. `..._funestus_f1`: Reared F1 adult progeny of An. funestus s.s. (f1_progeny) used for WHO susceptibility bioassays and genotype-phenotype evaluations.
  3. `..._arabiensis_f1`: Reared F1 progeny of An. arabiensis (f1_progeny) tested in bioassays.
- Previous 2009 data discussed in the paper for longitudinal comparison (from Wondji et al. 2012 / Riveron et al. 2013) were not re-extracted, strictly focusing on the 2014 empirical collections.

### Genotypes (Population Samples)
- **Rdl A296S**: 38 field-collected F0 females were genotyped; resistant allele frequency is reported as 10.52% (page 8) and 10.5% (page 7), all occurring as heterozygotes. Following Rule 2, genotype counts are left null because the absolute count (8) was not explicitly printed.
- **GSTe2 L119F**: 40 field-collected F0 females were genotyped; all 40 were homozygous susceptible (L119/L119, codon CTT; RR=0, RS=0, SS=40).

### Genotype-Phenotype Data
- **Rdl A296S on dieldrin**: 16 F1 dieldrin survivors (resistant) and 20 F1 dieldrin dead (susceptible) were genotyped. All 16 resistant were heterozygous (RR=0, RS=16, SS=0), and all 20 susceptible were homozygous susceptible (RR=0, RS=0, SS=20). These are linked directly to the dieldrin bioassay.
- **GSTe2 L119F on DDT**: 20 F1 DDT survivors (resistant) and 20 F1 DDT dead (susceptible) were genotyped. All were homozygous susceptible (RR=0, RS=0, SS=20). These are linked directly to the DDT bioassay.

### Bioassays
- Standard WHO tube bioassays (60 min exposure, 24 h holding period) are reported in the text with exact mortality percentages for females across 10 insecticides plus 1 synergist assay (DDT + PBO 4%) for An. funestus s.s., and 3 insecticides for An. arabiensis.
- Exact numbers of mosquitoes exposed per test are not explicitly printed in the text (described generally as at least four replicates of 25 individuals per tube for An. funestus, and 1 replicate for An. arabiensis); hence `n_exposed`, `n_dead`, and `n_alive` are left null with `dead_alive_printed = false`.

### Markers Excluded / Not Reported
- Exon 20 of VGSC in An. funestus was sequenced (10 resistant, 10 susceptible to permethrin and DDT), but no kdr mutation was found; kdr L1014 is not an established target marker in An. funestus.
- VGSC 1014F was tested in An. arabiensis by TaqMan and sequencing of 10 field-collected specimens, and no mutation was detected, but detailed genotype breakdown/counts were not reported.

## Validator warnings

- genotype #1 (2015_Riveron_Rise_Multiple_Insecticide_Resistance_Anopheles_PMID26370361_chikwawa_2014_funestus_f0, Rdl A296S): frequency only (no raw counts)
