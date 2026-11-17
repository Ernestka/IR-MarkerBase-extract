# Extraction record — 2015_Matowo_Trends_Selection_Insecticide_Resistance_Anopheles_PMID25537754

- Extracted: 2026-11-17
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 7 · Genotype rows: 8 · Bioassays: 27 · Geno-pheno rows: 0

## Decisions

### Decisions Readme

1. **Surveys**:
   - Surveys were split by village (Kiteme and Kyamyorwa) and collection time points (November 2011, May 2012, December 2012) for WHO tube bioassays.
   - A separate survey (`2015_Matowo_muleba_f1`) was created for the CDC bottle bioassays conducted on F1 progeny pooled from Muleba District.
   - Exact coordinates reported in text for Kiteme (02°03'20.9"S, 31°27'16.8"E -> lat -2.055806, lon 31.454667) and Kyamyorwa (02°04'27.5"S, 31°34'10.8"E -> lat -2.074306, lon 31.569667) were parsed to decimal degrees.

2. **Genotypes**:
   - The text reports that `kdr-e` (L1014S) had an allele frequency of 0.98 in both villages at baseline (2011) and during the intervention year (2012).
   - No `Ace-1` G119S mutation was detected in any of the screened mosquitoes (frequency 0.0).
   - Exact genotype counts (RR/RS/SS or N genotyped) were not printed; therefore, reported allele frequencies were extracted and counts left null.

3. **Bioassays**:
   - WHO susceptibility test data from Table 1 were extracted for each village and collection period.
   - Synergy bioassay data from Table 2 were extracted for the F1 wild progeny. Laboratory reference strain (Kisumu) tests were excluded as control data.
   - Number exposed and reported mortality percentages were extracted exactly as printed in Table 1 and Table 2. Since raw dead/alive counts were not printed explicitly, `dead_alive_printed` was set to `false` and counts left null per rules.

4. **Geno-Pheno**:
   - Text mentions that DNA was extracted from both survivors and dead mosquitoes, but no separate genotype frequencies or counts for survivors vs dead were reported. `geno_pheno` is empty.

## Validator warnings

- genotype #1 (2015_Matowo_kiteme_2011_11, kdr kdr-e): frequency only (no raw counts)
- genotype #2 (2015_Matowo_kiteme_2011_11, Ace-1 G119S): frequency only (no raw counts)
- genotype #3 (2015_Matowo_kyamyorwa_2011_11, kdr kdr-e): frequency only (no raw counts)
- genotype #4 (2015_Matowo_kyamyorwa_2011_11, Ace-1 G119S): frequency only (no raw counts)
- genotype #5 (2015_Matowo_kiteme_2012_05, kdr kdr-e): frequency only (no raw counts)
- genotype #6 (2015_Matowo_kiteme_2012_05, Ace-1 G119S): frequency only (no raw counts)
- genotype #7 (2015_Matowo_kyamyorwa_2012_05, kdr kdr-e): frequency only (no raw counts)
- genotype #8 (2015_Matowo_kyamyorwa_2012_05, Ace-1 G119S): frequency only (no raw counts)
