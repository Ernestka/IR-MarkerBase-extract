# Extraction record — 2011_Mathias_Spatial_Temporal_Variation_Kdr_Allele_PMID21235783

- Extracted: 2026-11-13
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 43 · Genotype rows: 31 · Bioassays: 49 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Genotypes (Table 1)**:
   - Extracted 31 location-and-time specific genotype records for *Anopheles gambiae s.s.* testing for the Vgsc L1014S mutation using RT-PCR.
   - In Table 1, S/S represents homozygous susceptible wild type (ss), S/E represents heterozygous (rs), and E/E represents homozygous East African kdr L1014S (rr).
   - Single occurrences of L1014S in *A. arabiensis* (e.g. 1 of 44 in Busia) mentioned in the text without detailed site/date-specific sample totals were omitted as population genotype counts.
   - Table 3 records genotype frequencies in relation to *Plasmodium falciparum* sporozoite infection (ELISA positive vs. negative), not insecticide bioassay outcomes, so it was excluded from `geno_pheno`.

2. **Bioassays (Table 4)**:
   - Extracted WHO tube bioassay records from Table 4 for 2009 *A. gambiae s.l.*, 2009-2010 *A. gambiae s.s.*, and 2009-2010 *A. arabiensis* across seven sites (Bungoma, Busia, Kakamega, Kisian, Malaba, Asembo, Budalangi).
   - Standard WHO discriminating concentrations reported in Methods: bendiocarb 0.1%, DDT 4%, deltamethrin 0.05%, malathion 5%, permethrin 0.75%.
   - Only total exposed ($n$) and mortality % were printed in Table 4; exact number dead/alive were not printed. Per Rule 2, `dead_alive_printed` is set to `false` and `n_dead` / `n_alive` are left `null`.

3. **Genotype-Phenotype**:
   - The paper notes that post-bioassay mosquitoes were genotyped for species ID and kdr, but does not print raw counts or separate frequencies of genotypes split by bioassay outcome (dead vs alive). Therefore, `geno_pheno` is empty.
