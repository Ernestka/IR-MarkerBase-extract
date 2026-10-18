# Extraction record — 2012_Overgaard_Malaria_Transmission_After_Five_Years_PMID23146423

- Extracted: 2026-10-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 11 · Genotype rows: 11 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Survey and Genotype Extraction Decisions
- **Study Context**: Overgaard et al. (2012) report entomological indicators and insecticide resistance allele frequencies for Anopheles mosquitoes collected on Bioko Island, Equatorial Guinea, in 2009.
- **Collection Methods**: Adult mosquitoes were sampled using two separate methods:
  1. Human Landing Catch (HLC) conducted bimonthly (March, May, July, September, November 2009) in three sentinel sites (Mongola, Arena Blanca, Riaba).
  2. CDC Light Trap Collections (LTC) conducted biweekly from February to December 2009 in ten locations.
- **Species and Form**: All An. gambiae s.s. specimens analyzed by PCR-RFLP belonged to the M molecular form (Anopheles coluzzii). No S molecular form specimens were found.
- **Screened Markers**: Populations were screened for Vgsc L1014F (kdr-west), L1014S (kdr-east), and Ace-1 G119S (ace-1R). Only L1014F was detected, and only in An. gambiae s.s. (M form). No resistance alleles were detected in An. melas.
- **HLC Genotype Data (Table 4)**: Exact counts of homozygous susceptible (S/S), heterozygous (S/R), and homozygous resistant (R/R) individuals along with total numbers genotyped (n) are extracted directly for Mongola (n=1195), Arena Blanca (n=136), and Riaba (n=423). Calculated allele frequencies from these counts perfectly match the reported values (51.3%, 39.0%, and 16.9%, respectively).
- **LTC Genotype Data (Table 3)**: Table 3 reports L1014F allele frequencies for An. gambiae s.s. across 8 sites (Mongola, Biabia, Cacahual, Arena Blanca, Riaba, Bakake Grande, Semu, Santa Maria). As individual genotype counts and sample sizes genotyped were not printed for LTC, count fields are set to null and frequencies are recorded in `reported_allele_freq` per Rule 2. Bilelipa (where 0 An. gambiae s.s. were collected) and Basacato del Oeste (0 mosquitoes collected) are excluded. The 'TOTAL / Average' row was omitted per Rule 7.
- **L1014S and ace-1R**: Because the paper states L1014S and ace-1R were absent but does not provide site-specific sample sizes or genotype tables for them, they are not extracted as separate genotype rows.
- **Bioassays and Genotype-Phenotype**: No insecticide susceptibility bioassays or phenotype-stratified genotyping were conducted in this study; both lists are empty.

## Validator warnings

- genotype #4 (2012_Overgaard_Malaria_Transmission_After_Five_Years_PMID23146423_mongola_ltc_col, kdr L1014F): frequency only (no raw counts)
- genotype #5 (2012_Overgaard_Malaria_Transmission_After_Five_Years_PMID23146423_biabia_ltc_col, kdr L1014F): frequency only (no raw counts)
- genotype #6 (2012_Overgaard_Malaria_Transmission_After_Five_Years_PMID23146423_cacahual_ltc_col, kdr L1014F): frequency only (no raw counts)
- genotype #7 (2012_Overgaard_Malaria_Transmission_After_Five_Years_PMID23146423_arena_blanca_ltc_col, kdr L1014F): frequency only (no raw counts)
- genotype #8 (2012_Overgaard_Malaria_Transmission_After_Five_Years_PMID23146423_riaba_ltc_col, kdr L1014F): frequency only (no raw counts)
- genotype #9 (2012_Overgaard_Malaria_Transmission_After_Five_Years_PMID23146423_bakake_grande_ltc_col, kdr L1014F): frequency only (no raw counts)
- genotype #10 (2012_Overgaard_Malaria_Transmission_After_Five_Years_PMID23146423_semu_ltc_col, kdr L1014F): frequency only (no raw counts)
- genotype #11 (2012_Overgaard_Malaria_Transmission_After_Five_Years_PMID23146423_santa_maria_ltc_col, kdr L1014F): frequency only (no raw counts)
