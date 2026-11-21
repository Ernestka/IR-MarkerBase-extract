# Extraction record — 2018_Dia_Insecticide_Resistance_Anopheles_Arabiensis_Popula_PMID29544491

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 15 · Genotype rows: 2 · Bioassays: 61 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Sites**:
   - Surveys were split by locality (neighborhood/district) and sampling round/season (RS 2013: July–October 2013; DS 2014: November 2013–June 2014; RS 2015: July–October 2015).
   - All collections were wild larvae/pupae reared to 3–5 day old F0 adult females (`wild_reared`).
   - Molecular identification showed 100% *Anopheles arabiensis* across all sites and years.
   - No explicit latitude/longitude coordinates in decimal degrees were printed in the paper text or tables (only projected UTM coordinates in meters on Fig. 1), so coordinates were left `null` per Rule 9.

2. **Genotypes**:
   - Target site mutations reported: Vgsc L1014F (kdr-West) and L1014S (kdr-East).
   - Site-specific genotype breakdown counts/frequencies are presented as pie charts on a map without printed numbers in Figure 5.
   - Only pooled overall frequencies across Dakar (2013–2014) are given numerically in the text/abstract/Fig. 5 inset: L1014F = 10.24% (0.1024) and L1014S = 89.53% (0.8953).
   - Total N genotyped for kdr is not stated in the paper, so `n_genotyped` and count fields are left `null` per Rule 2.

3. **Bioassays**:
   - Table 2 reports WHO tube bioassays for organochlorines and pyrethroids (24h mortality).
   - Table 3 reports WHO tube bioassays for carbamates and organophosphates (24h mortality).
   - Table 4 reports CDC bottle bioassays conducted in RS 2015.
   - Synergist assays (PBO and EA pre-exposure) described in text and Figures 2–4 are included as synergist bioassay records.
   - In Tables 2–4, numbers in parentheses represent total mosquitoes exposed (`n_exposed`), while numbers outside parentheses are reported mortality percentages (`reported_mortality_pct`). Dead and alive counts were not explicitly printed as integers in tables, so `dead_alive_printed` is set to `false` and `n_dead`/`n_alive` left `null` per Rule 2.

4. **Geno-Pheno**:
   - Mosquitoes were not genotyped separately by bioassay survival status (dead vs alive), so `geno_pheno` is empty.

## Validator warnings

- genotype #1 (2018_Dia_Dakar_2013_2014, kdr L1014F): frequency only (no raw counts)
- genotype #2 (2018_Dia_Dakar_2013_2014, kdr L1014S): frequency only (no raw counts)
