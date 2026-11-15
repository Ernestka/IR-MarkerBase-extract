# Extraction record — 2013_Sovi_Impact_Land_Use_Malaria_Transmission_PMID24330734

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 0 · Bioassays: 8 · Geno-pheno rows: 7

## Decisions

### Decisions Readme

- **Surveys**: Four distinct survey records were created corresponding to the four study villages in the Plateau region of southeastern Benin: Itakpako, Itassoumba, Ko-Koumolou (all in Ifangni district) and Djohounkollé (Sakété district). Mosquitoes were collected as larvae and pupae from July 2011 to June 2012 and reared to adults for bioassays.
- **Marker Identification**: Updated marker to `L1014F` under `gene` `kdr` (corresponding to Vgsc L995F) to match standard schema target marker alias. Protocol cited is Martinez-Torrez et al. (1998) for West African kdr (Leu-Phe substitution at codon 1014).
- **Bioassays**: Extracted 8 WHO tube bioassay records (60 min exposure, 24 h mortality) covering permethrin 0.75% and deltamethrin 0.05% across all 4 villages. Numbers exposed, dead, alive, and mortality percentages were reported in text (Page 7) and Figure 3.
- **Geno_Pheno vs Genotypes**: All 148 genotyped mosquitoes originated from deltamethrin susceptibility tests. Table 4 reports genotypes split by bioassay outcome (dead/alive). To avoid double-counting, these records are placed strictly in `geno_pheno` (linked to the respective deltamethrin bioassay IDs), leaving `genotypes` empty.
- **Table 4 Discrepancy Note**: The total genotyped count for Djohounkollé is listed as 43 in the table header, but the sum of genotyped M-form mosquitoes is 37 (and dead [34] + alive [3] = 37). The printed genotype counts (RR=20, RS=14, SS=0 for dead; RR=2, RS=1, SS=0 for alive) match N=34 and N=3 exactly with their reported allele frequencies (79.41% and 83.33%).
