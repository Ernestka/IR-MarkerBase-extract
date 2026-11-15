# Extraction record — 2013_Protopopoff_High_Level_Resistance_Mosquito_Anopheles_PMID23638757

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 18 · Genotype rows: 18 · Bioassays: 27 · Geno-pheno rows: 0

## Decisions

### Data Extraction Summary

1. **Surveys**:
   - Created village-level surveys for morning indoor resting catches used for WHO bioassays (in May and November 2011 across 11 villages).
   - Created district-wide surveys for light-trap collections across 40 villages in Muleba district (April-December 2011) separated by species (*Anopheles gambiae s.s.* and *Anopheles arabiensis*).
   - Created district-wide resting catch surveys to capture the pooled raw genotype count totals reported in text for *An. gambiae s.s.* and *An. arabiensis*.

2. **Genotypes**:
   - Extracted exact genotype counts (RR, RS, SS) for kdr-east (Vgsc L995S) from text for light trap collections (2,049 *An. gambiae s.s.*: 1983 RR, 62 RS, 4 SS; 297 *An. arabiensis*: 0 RR, 0 RS, 297 SS).
   - Extracted exact genotype counts for indoor resting catches exposed to WHO tests (772 *An. gambiae s.s.*: 747 RR, 24 RS, 1 SS; 31 *An. arabiensis*: 0 RR, 0 RS, 31 SS).
   - Extracted reported kdr-east allele frequencies (percentages converted to proportions 0-1) per village from Table 1.
   - Extracted kdr-west (Vgsc L995F) testing result (176 mosquitoes tested, 0 carriers).

3. **Bioassays**:
   - Extracted all WHO tube test results from Table 1 (lambdacyhalothrin 0.05%) and Table 2 (bendiocarb 0.1%, DDT 4%, deltamethrin 0.05%, permethrin 0.75%) per village and date.
   - Skipped laboratory reference Kisumu control strain tests as per Rule 5.
   - `dead_alive_printed` set to false as only total exposed and mortality percentages were printed in Tables 1 and 2.

4. **Geno-Pheno**:
   - No numerical genotype counts or frequencies split by bioassay outcome (dead vs alive) were reported in the text/tables, so `geno_pheno` is empty.

## Validator warnings

- genotype #1 (2013_protopopoff_kikagate_2011_05, Vgsc kdr east): frequency only (no raw counts)
- genotype #2 (2013_protopopoff_kyamyorwa_2011_05, Vgsc kdr east): frequency only (no raw counts)
- genotype #3 (2013_protopopoff_kishuro_2011_11, Vgsc kdr east): frequency only (no raw counts)
- genotype #4 (2013_protopopoff_ngenge_2011_11, Vgsc kdr east): frequency only (no raw counts)
- genotype #5 (2013_protopopoff_rwigembe_2011_11, Vgsc kdr east): frequency only (no raw counts)
- genotype #6 (2013_protopopoff_buhuma_2011_11, Vgsc kdr east): frequency only (no raw counts)
- genotype #7 (2013_protopopoff_kangoma_2011_11, Vgsc kdr east): frequency only (no raw counts)
- genotype #8 (2013_protopopoff_kikagate_2011_11, Vgsc kdr east): frequency only (no raw counts)
- genotype #9 (2013_protopopoff_kiteme_2011_11, Vgsc kdr east): frequency only (no raw counts)
- genotype #10 (2013_protopopoff_kyamyorwa_2011_11, Vgsc kdr east): frequency only (no raw counts)
- genotype #11 (2013_protopopoff_nyakahama_2011_11, Vgsc kdr east): frequency only (no raw counts)
- genotype #12 (2013_protopopoff_buhanga_2011_11, Vgsc kdr east): frequency only (no raw counts)
- genotype #13 (2013_protopopoff_kimbuga_2011_11, Vgsc kdr east): frequency only (no raw counts)
