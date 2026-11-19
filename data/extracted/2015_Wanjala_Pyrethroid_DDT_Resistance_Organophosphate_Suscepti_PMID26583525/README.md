# Extraction record — 2015_Wanjala_Pyrethroid_DDT_Resistance_Organophosphate_Suscepti_PMID26583525

- Extracted: 2026-11-19
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 20 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Survey and Genotype Extraction Decisions
- **Surveys**: Samples were collected as larvae across 7 sentinel sites in western Kenya between April 2012 and July 2013 and reared to adulthood. 10 surveys were created corresponding to the specific molecular species (An. gambiae s.s. or An. arabiensis) genotyped at each site where sufficient specimens were available (Table 2). Populations marked 'ND' in Table 2 (Ahero An. gambiae s.s., Emutete An. arabiensis, Emakakha An. arabiensis, Bungoma An. arabiensis) were not genotyped due to low specimen counts and are therefore not extracted.
- **Codon 1014 Genotyping**: The TaqMan assay was used to genotype L1014S and L1014F. Table 2 provides raw counts for LL (wild type L/L), LS (L/S heterozygotes), and SS (S/S homozygotes) for L1014S. In accordance with extraction rule 4b, both L1014S and L1014F are reported per survey. Since the paper explicitly states that 'The L1014F mutation was not detected in An. gambiae s.s or An. arabiensis mosquitoes at any sites', L1014F has RR = 0, RS = 0, and SS = n_genotyped across all surveys.
- **Bioassays**: WHO tube bioassays were conducted on wild-reared An. gambiae s.l. prior to molecular identification. Mortality results for 6 insecticides across the 7 sites are reported exclusively as bar graphs in Figure 2 without exact numerical values or tables (except for general text descriptions of ranges, 100% mortality to malathion, and 50% permethrin mortality in Bungoma). Due to the lack of numerical values and because tests were conducted on mixed s.l. populations, bioassays were not extracted.
- **Genotype-Phenotype**: Genotypes were not reported separately by bioassay outcome (dead vs alive); thus geno_pheno is empty.
