# Extraction record — 2015_Main_Complex_Genome_Evolution_Anopheles_Coluzzii_PMID26359110

- Extracted: 2026-11-17
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 4 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

# Data Extraction Decisions

### Target Markers & Exclusions
- **Target Marker Extracted**: `para` / `L1014F` (Vgsc L995F) was extracted for population surveys in Selinkenyi, Mali.
- **Ignored Markers**: Table 1 reports frequencies for CYP9K1 haplotypes (cyp-I, cyp-II, cyp-III). CYP9K1 haplotypes are not in the target markers list (the only target marker for CYP9K1 is `Cyp9k1 G454A`, which is specific to *An. funestus* and was not evaluated in this paper). Thus, Table 1 data were ignored per Rule 1.

### Bioassays & Genotype-Phenotype Data
- The bioassays described on pages 4 and 7 evaluated knockdown times ($KD_{50}$, $KD_{90}$, and % knockdown at 30 min) in Wheaton bottle bioassays rather than standard 24-hour mortality. Per Rule 8b ("If the paper reports only knockdown times (KDT50) and no mortality, skip that bioassay"), bioassay records were skipped.
- No phenotype-split mortality genotypes (survivors vs. dead at 24h) were reported for target markers.

### Spatial and Temporal Information
- Mosquitoes were collected in Selinkenyi, Mali (11.700°N, 8.2833°W). Exact coordinates printed on page 2 were converted to decimal degrees.

## Validator warnings

- genotype #3 (2015_Main_Selinkenyi_2002_2004_gam, para L1014F): frequency only (no raw counts)
- genotype #4 (2015_Main_Selinkenyi_2014_col, para L1014F): frequency only (no raw counts)
