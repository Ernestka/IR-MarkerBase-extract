# Extraction record — 2006_Akogbeto_Screening_Pesticide_Residues_Soil_Water_PMID16563153

- Extracted: 2026-10-17
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 2 · Bioassays: 6 · Geno-pheno rows: 0

## Decisions

### Survey and Data Extraction Decisions
1. **Surveys**: Two field sites were surveyed in Benin: Houeyiho (Cotonou, Littoral) and Parakou (Borgou). At Houeyiho, PCR species identification showed 100% An. gambiae M form (An. coluzzii). At Parakou, PCR identification showed a mixed population (87.5% An. arabiensis, 12.5% An. gambiae s.s.).
2. **Genotypes**: Updated marker mapping to standard Vgsc L1014F (L995F) assayed using Martinez-Torres et al. (1998) PCR. Frequencies reported as percentages (90% at Houeyiho and 10% at Parakou) in Table 1, saved in `reported_allele_freq` (0.90 and 0.10).
3. **Bioassays**: WHO standard susceptibility bioassay results (permethrin 0.75%, deltamethrin 0.05%, DDT 4%) reported in Table 1 for both sites. Dead and alive raw counts were not printed, so `dead_alive_printed` is set to false and mortality percentage stored in `reported_mortality_pct`.
4. **Excluded Data**: Indirect bioassay experiments simulating reconstituted soil/water breeding sites with laboratory reference strains (Kisumu and Ladji) were excluded per Rule 5.

## Validator warnings

- genotype #1 (2006_Akogbeto_Screening_Pesticide_Residues_Soil_Water_PMID16563153_houeyiho, Vgsc L1014F): frequency only (no raw counts)
- genotype #2 (2006_Akogbeto_Screening_Pesticide_Residues_Soil_Water_PMID16563153_parakou, Vgsc L1014F): frequency only (no raw counts)
