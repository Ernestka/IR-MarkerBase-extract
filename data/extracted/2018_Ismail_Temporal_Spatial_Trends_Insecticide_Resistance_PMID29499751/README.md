# Extraction record — 2018_Ismail_Temporal_Spatial_Trends_Insecticide_Resistance_PMID29499751

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 20 · Genotype rows: 20 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

The paper evaluated insecticide resistance in Anopheles arabiensis across four study areas in Sudan (El Hoosh, Hag Abdalla, Galabat, and New Halfa) over 5 consecutive years (2010 to 2014). A total of 20 surveys were defined (4 study areas x 5 years). Vgsc-1014F genotype counts (LL, LF, FF) were extracted directly from Table 1 for all 20 surveys. Vgsc-1014S was detected in 2010 at very low frequency (0.001 to 0.0087) but no per-area/year counts were given. Ace-1 testing showed 0 resistant mutations out of 2653 baseline samples and 206 bendiocarb bioassay survivors, but since these counts were aggregated across all sites combined, they could not be mapped to specific per-site surveys. Individual WHO bioassay raw test counts (n_exposed, n_dead, n_alive) were not printed in the main text or main tables (only overall study totals and per-arm mean percentages in Table 2 and supplementary files were reported), so bioassays and geno_pheno arrays are left empty.
