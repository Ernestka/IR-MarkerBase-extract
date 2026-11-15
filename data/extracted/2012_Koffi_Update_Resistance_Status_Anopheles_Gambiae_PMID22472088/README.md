# Extraction record — 2012_Koffi_Update_Resistance_Status_Anopheles_Gambiae_PMID22472088

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 2 · Bioassays: 7 · Geno-pheno rows: 0

## Decisions

- Extracted field-collected Anopheles gambiae s.s. from Yaokoffikro (June 2008).
- Excluded Kisumu laboratory strain bioassay and biochemical data per guidelines (controls/lab reference strains).
- Bioassay mortality percentages and exposed sample sizes extracted from Table 1. Since specific dead/alive count numbers were not printed, n_dead and n_alive were set to null and dead_alive_printed set to false.
- Genotype data for L1014F (kdr) was reported as 108 carriers out of 111 genotyped (n_carriers = 108, n_genotyped = 111, reported_allele_freq = 0.94); genotype classes (RR/RS/SS) were not printed.
- Ace-1 G119S genotype frequency (0.50) and sample size (44) extracted from Table 2 and text; genotype classes were not split.
- Coordinates 5°1' W, 7°11' N converted to decimal degrees (-5.016667, 7.183333).

## Validator warnings

- genotype #2 (2012_Koffi_Yaokoffikro_2008, ace-1 G119S): frequency only (no raw counts)
