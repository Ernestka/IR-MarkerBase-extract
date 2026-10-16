# Extraction record — 2015_Lee_Peer_Review_Report_Absence_Kdr_DOI_10_5256_f1000research_7052_r8978

- Extracted: 2026-10-16
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 15 · Genotype rows: 15 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Survey and Genotype Extraction Decisions
- **Sites**: 15 distinct sampling sites were extracted directly from Table 1 (14 sites in the Union of the Comoros and 1 site in Dar es Salaam, Tanzania), collected in February-March 2011.
- **Target Markers**: Only Vgsc L995S (reported as kdr-East / L1014S, with resistant allele 'E') was extracted. The CYP9K1 'cyp3' locus reported in Table 1 was omitted because CYP9K1 in An. gambiae is not included in the target markers list (only Cyp9k1 G454A in An. funestus is targeted).
- **Mozambique Collection**: Anopheles collected in Furvela, Mozambique were found to be An. merus and An. arabiensis and were excluded from insecticide resistance genotyping by the study authors, hence not extracted.
- **Bioassays**: No insecticide bioassays were performed in this study; hence `bioassays` and `geno_pheno` arrays are empty.
- **Genotype Classes**: In Table 1, '+/+' corresponds to homozygous wild-type/susceptible (SS), 'E/+' to heterozygous (RS), and 'E/E' to homozygous resistant (RR).
