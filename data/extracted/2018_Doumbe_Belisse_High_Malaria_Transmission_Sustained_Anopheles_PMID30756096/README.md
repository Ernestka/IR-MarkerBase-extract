# Extraction record — 2018_Doumbe_Belisse_High_Malaria_Transmission_Sustained_Anopheles_PMID30756096

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 1 · Bioassays: 4 · Geno-pheno rows: 2

## Decisions

### Decisions & Data Extraction Notes
1. **Surveys Split**: Two main surveys were created:
   - `2018_Doumbe_Belisse_Yaounde_2017_2018_adult`: Adults collected via HLC and CDC light traps in Yaoundé, used for malaria transmission and Plasmodium infection analysis.
   - `2018_Doumbe_Belisse_Yaounde_2017_2018_reared`: Wild-reared mosquitoes from larval collections in Yaoundé, used for WHO tube bioassays and genotype-phenotype analysis.
2. **Coordinates**: Given in text (3° 52' 12 N; 11° 31' 12 E) which converts to 3.87° N, 11.52° E.
3. **Target Marker**: Only `kdr L1014F` (Vgsc L995F) was reported and extracted. Marker name kept as `L1014F` under gene `kdr` as printed in paper.
4. **Genotypes**: 
   - Table 3 reports L1014F genotypes for 143 wild adult mosquitoes split by Plasmodium infection status. The overall row (143 total, RR=102, RS=39, SS=2) was placed in `genotypes`. An inconsistency note was logged because the printed frequency (0.79) differs from the calculated frequency (0.85).
   - Table 5 reports L1014F genotypes for bioassay survivors and dead mosquitoes. These were placed into `geno_pheno` to prevent double-counting.
5. **Bioassays**: Extracted 4 WHO tube susceptibility bioassays (deltamethrin 0.05%, permethrin 0.75%, DDT 4%, bendiocarb 0.1%) from Table 4 for field populations. The Kisumu reference strain was omitted as per guidelines. Counts of dead/alive were not explicitly printed, so `dead_alive_printed = false` and `n_dead` and `n_alive` set to null.

## Validator warnings

- genotype #1 (2018_Doumbe_Belisse_Yaounde_2017_2018_adult, kdr L1014F): inconsistent in the paper (values kept as printed) — Printed reported_allele_freq 0.79 does not match calculated allele frequency 0.8496 from RR=102, RS=39, SS=2.
- genotype #1 (2018_Doumbe_Belisse_Yaounde_2017_2018_adult, kdr L1014F): computed allele freq 0.850 differs from reported 0.79
- geno_pheno #1 (no insecticide, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: none given)
- geno_pheno #2 (no insecticide, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: none given)
