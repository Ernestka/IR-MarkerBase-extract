# Extraction record — 2011_Kawada_Multimodal_Pyrethroid_Resistance_Malaria_Vectors_PMID21853038

- Extracted: 2026-11-13
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 16 · Genotype rows: 11 · Bioassays: 10 · Geno-pheno rows: 0

## Decisions

### Extraction Decisions

1. **Markers Extracted**: 
   - Target marker: `Vgsc L1014S` (mapped to schema standard Vgsc L995S).
   - Text mentions that the L1014F mutation (West African kdr) was checked and not detected in any species (0%).

2. **Genotype Counts vs Frequencies**:
   - Tables 1 and 6 report sample size `N`, `AF %` (allele frequency percentage), and `RR %` (percentage of homozygotes).
   - Following Rule 2, because raw genotype counts (RR, RS, SS) are not directly printed as count integers in the tables, the count fields (`rr`, `rs`, `ss`, `n_carriers`) are left `null` and the proportion is recorded in `reported_allele_freq` (AF / 100).

3. **Exclusions**:
   - The ICIPE laboratory reference strain (collected in Lwanda, Mbita in 2002 and maintained in colony) was excluded as a control strain per Rule 5.

4. **Bioassays & Geno-Pheno**:
   - Representative adult WHO tube bioassay records from Tables 3 and 4 were extracted for F1 lines. Because the exact count of dead/alive insects is not printed (only N and % mortality), `dead_alive_printed` is set to `false` and `n_dead` / `n_alive` are left `null`.
   - Topical application assays (Table 5) reporting LD50 values rather than single-dose diagnostic bioassay mortalities were skipped.
   - No genotypes split by bioassay outcome (alive vs dead) are reported in the paper, so `geno_pheno` is empty.

## Validator warnings

- genotype #1 (2011_Kawada_larvae_2009_nyaroya_arab, Vgsc L1014S): frequency only (no raw counts)
- genotype #2 (2011_Kawada_larvae_2009_nyandago_arab, Vgsc L1014S): frequency only (no raw counts)
- genotype #3 (2011_Kawada_larvae_2009_nyandago_rivu, Vgsc L1014S): frequency only (no raw counts)
- genotype #4 (2011_Kawada_larvae_2009_mirunda_gamb, Vgsc L1014S): frequency only (no raw counts)
- genotype #5 (2011_Kawada_larvae_2009_mirunda_arab, Vgsc L1014S): frequency only (no raw counts)
- genotype #6 (2011_Kawada_larvae_2009_kisamba_gamb, Vgsc L1014S): frequency only (no raw counts)
- genotype #7 (2011_Kawada_larvae_2009_obambo_gamb, Vgsc L1014S): frequency only (no raw counts)
- genotype #8 (2011_Kawada_adult_2009_2011_takawiri_gamb_f, Vgsc L1014S): frequency only (no raw counts)
- genotype #9 (2011_Kawada_adult_2009_2011_ngodhe_gamb_f, Vgsc L1014S): frequency only (no raw counts)
- genotype #10 (2011_Kawada_adult_2009_2011_mfangano_gamb_f, Vgsc L1014S): frequency only (no raw counts)
- genotype #11 (2011_Kawada_adult_2009_2011_kibuogi_gamb_f, Vgsc L1014S): frequency only (no raw counts)
