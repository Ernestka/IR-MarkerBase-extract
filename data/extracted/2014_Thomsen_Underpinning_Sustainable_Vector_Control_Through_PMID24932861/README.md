# Extraction record — 2014_Thomsen_Underpinning_Sustainable_Vector_Control_Through_PMID24932861

- Extracted: 2026-11-01
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 6 · Bioassays: 9 · Geno-pheno rows: 0

## Decisions

### Survey and Marker Extraction Decisions
- **Surveys defined**: Two surveys were created for the Anopheles gambiae s.s. populations genotyped for target-site resistance markers in Table 3: Kitwe (Copperbelt Province) and Kasama (Northern Province). All tested An. gambiae s.l. were molecularly confirmed to be An. gambiae s.s. (page 7).
- **Scope of bioassays**: Linked WHO tube bioassays conducted on F1 adults reared from these populations during the same collection window (March 2011–April 2012, reported in Table 1) were extracted. Other districts from Table 1 and Table 2 (as well as An. funestus s.s. populations) where no target-site resistance markers were genotyped were excluded to focus strictly on the marker-characterized populations and their linked bioassays.
- **Target markers**: Table 3 provides explicit genotype counts for `kdr` (1014F) and `iACE` (G119S). In addition, text on page 9 states that assays were performed for both 1014S and 1014F, and that 1014S was not detected. Consequently, L1014S was recorded with RR=0, RS=0, and SS=N for both Kitwe (N=41) and Kasama (N=26). Wild-type L/L count in Kasama was 2, and no F/S heterozygotes were observed. For Kasama, iACE had N=25 (0 rr, 0 rs, 25 ss).
- **Bioassay counts**: In Table 1, only the number exposed (`n`) and percent mortality are reported. In accordance with extraction rules, `dead_alive_printed` was set to `false`, and `n_dead` and `n_alive` were left null.
- **Transcriptomic data**: Microarray and qRT-PCR fold changes in expression of CYP6P9a, CYP6P9b, CYP6AA1, etc., were excluded as they represent gene expression assays rather than DNA target-site mutations or structural variants.
