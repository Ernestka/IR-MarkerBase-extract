# Extraction record — 2015_Wanjala_Pyrethroid_DDT_Resistance_Organophosphate_Suscepti_PMID26583525

- Extracted: 2026-11-18
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 17 · Genotype rows: 20 · Bioassays: 8 · Geno-pheno rows: 0

## Decisions

### Data Extraction Notes

- **Surveys**: Mosquito larvae were collected across 7 sentinel sites in western Kenya between April 2012 and July 2013, then wild-reared to adults for susceptibility bioassays. Species identification was carried out on a randomly selected subset using 16S rDNA PCR. Surveys for genotypes were split at the finest resolution per site and molecular species (*An. gambiae s.s.* and *An. arabiensis*) as presented in Table 2. Separate site-level surveys for *An. gambiae s.l.* were created for bioassay records, as bioassays were conducted on the unseparated field population prior to species identification.
- **Genotypes**: Raw genotype counts (LL, LS, SS) for kdr position L1014 (gene: `kdr`, marker: `L1014S`) were extracted directly from Table 2. LL corresponds to wildtype susceptible (`ss`), LS to heterozygous (`rs`), and SS to homozygous resistant (`rr`). The text explicitly notes that the `L1014F` mutation was not detected at any site in either species; corresponding `L1014F` entries with 0 carriers and 0.0 frequency are included.
- **Bioassays**: Bioassay mortality data are displayed graphically in Figure 2. Exact numerical mortality values explicitly printed in the text (100% for malathion across all 7 sites, and 50% for permethrin at Bungoma) were extracted. Bioassays only presented as bar charts without printed exact figures were omitted per rule 8 to avoid digitizing errors. Exposure size is 160 mosquitoes per test (8 exposure replicates of 20 mosquitoes).
