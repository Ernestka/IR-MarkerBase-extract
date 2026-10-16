# Extraction record — 2022_Sagbohan_Intensity_Different_Genes_Involved_Resistance_DOI_10_22271_23487941_2022_v9_i2a_596

- Extracted: 2026-10-16
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 13 · Genotype rows: 9 · Bioassays: 12 · Geno-pheno rows: 8

## Decisions

### Study & Survey Decisions
- **Study sites**: 4 districts in Northern Benin (Parakou, N'Dali, Kandi, Malanville).
- **Temporal range**: October 2019 to December 2020 as stated in 'Study sites'.
- **Surveys**: Created distinct surveys per district and per molecular species (An. arabiensis, An. coluzzii, An. gambiae s.s.) for genotype reporting (Table 1), plus an An. gambiae s.l. survey per district for WHO susceptibility bioassays and geno_pheno reporting.

### Bioassays
- Excluded Kisumu control strains.
- Extracted WHO tube test bioassay results for 5x concentration of deltamethrin (0.25%), permethrin (3.75%), and alpha-cypermethrin (0.25%) across all 4 districts from Fig 2.
- Fig 2 reports N exposed and percentage mortality; dead_alive_printed set to false and n_dead / n_alive left null as specified by Rule 2.

### Genotypes & Geno_Pheno
- Marker evaluated: Vgsc L1014F (reported as `kdr L1014F`).
- Genotype counts in Table 1 (species-specific per district) were extracted into `genotypes`. Pooled district/species totals were excluded per Rule 7.
- Table 2 reports genotype counts split by dead (Mort) and alive (Vivant) status following exposure to deltamethrin 5x (50 dead + 50 alive per district). These were extracted into `geno_pheno` and linked directly to the corresponding deltamethrin 5x bioassay ID.
- General biochemical enzyme assays (non-specific esterases, MFOs, GSTs) were ignored as they are non-target markers.
