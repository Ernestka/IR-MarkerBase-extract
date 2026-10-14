# Extraction record — 07_1575

- Extracted: 2026-10-14
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 4 · Bioassays: 0 · Geno-pheno rows: 12

## Decisions

### Marker Identification Correction
- The paper refers to the knockdown resistance mutation as `kdr`, detected via Martinez-Torres et al. (1998) PCR (which specifically assays the Vgsc L1014F / L995F mutation in West Africa; confirmed by Diabaté et al. 2004 cited in the study). In the previous attempt, setting `marker: 'kdr'` caused an unrecognized marker error (`kdr kdr`). The marker has been updated to `L1014F` (gene: `kdr`, marker: `L1014F`), following Rule 1's explicit example `(e.g. 'kdr' / 'L1014F')` which maps to target marker `Vgsc L995F`.

### Study and Survey Structure
- The study evaluated nets impregnated with pirimiphos-methyl (PM) plus repellents (DEET or KBR 3023) compared to deltamethrin (Kothrin) and untreated control nets in experimental huts in VK7, Kou River valley near Bobo-Dioulasso, Burkina Faso in 2006.
- Collections were carried out in two distinct seasons: dry season (May 5 to June 3, 2006) and rainy season (September 18 to October 14, 2006).
- Table 1 reports kdr (L1014F) and Ace1R (G119S) allele frequencies and number tested from random samples collected in control huts: `07_1575_VK7_2006_dry` and `07_1575_VK7_2006_rainy_control`.
- Table 3 reports kdr and Ace1R frequencies separately for surviving and dead mosquitoes exposed to the three treatments for the S molecular form collected during the rainy season: `07_1575_VK7_2006_rainy_S`.

### Bioassays
- No standard WHO susceptibility tube or CDC bottle bioassays were conducted. The experimental hut mortality results were modeled using binomial logistic regression over 27 consecutive nights (reporting ET50 and ET90 values in Table 2, without discrete exposed/dead counts per bioassay test); following extraction guidelines, the bioassays array is empty.

### Genotypes and Genotype-Phenotype Data
- Following Rule 2, genotype classes (RR, RS, SS) are left null because only allele frequencies and numbers of individuals tested are printed in Table 1 and Table 3.

## Validator warnings

- genotype #1 (07_1575_VK7_2006_dry, kdr L1014F): frequency only (no raw counts)
- genotype #2 (07_1575_VK7_2006_dry, Ace1 Ace1R): frequency only (no raw counts)
- genotype #3 (07_1575_VK7_2006_rainy_control, kdr L1014F): frequency only (no raw counts)
- genotype #4 (07_1575_VK7_2006_rainy_control, Ace1 Ace1R): frequency only (no raw counts)
- geno_pheno #1 (pirimiphos-methyl + DEET, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + DEET)
- geno_pheno #2 (pirimiphos-methyl + DEET, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + DEET)
- geno_pheno #3 (pirimiphos-methyl + DEET, Ace1 Ace1R, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + DEET)
- geno_pheno #4 (pirimiphos-methyl + DEET, Ace1 Ace1R, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + DEET)
- geno_pheno #5 (pirimiphos-methyl + KBR 3023, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + KBR 3023)
- geno_pheno #6 (pirimiphos-methyl + KBR 3023, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + KBR 3023)
- geno_pheno #7 (pirimiphos-methyl + KBR 3023, Ace1 Ace1R, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + KBR 3023)
- geno_pheno #8 (pirimiphos-methyl + KBR 3023, Ace1 Ace1R, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + KBR 3023)
- geno_pheno #9 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #10 (deltamethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #11 (deltamethrin, Ace1 Ace1R, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #12 (deltamethrin, Ace1 Ace1R, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
