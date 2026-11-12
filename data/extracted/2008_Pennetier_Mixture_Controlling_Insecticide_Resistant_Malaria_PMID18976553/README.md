# Extraction record — 2008_Pennetier_Mixture_Controlling_Insecticide_Resistant_Malaria_PMID18976553

- Extracted: 2026-11-11
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 4 · Bioassays: 0 · Geno-pheno rows: 12

## Decisions

### Study & Methodology Decisions
- The study evaluated repellent + organophosphate insecticide mixtures versus deltamethrin (Kothrin) impregnated nets in experimental huts in VK7 village, southwestern Burkina Faso.
- Target markers extracted: `kdr` (Vgsc L995F / L1014F, detected by PCR per Martinez-Torres et al. 1998) and `Ace1R` (Ace-1 G280S / G119S, detected by PCR-RFLP per Weill et al. 2004).
- Changed marker naming for `kdr` to `L1014F` to meet standard mapping target requirement.

### Surveys & Population Genotyping
- Two baseline sampling collections were reported in Table 1 from untreated control huts:
  1. `2008_Pennetier_VK7_dry_ctrl`: May 5 to June 3, 2006 (dry season), Anopheles gambiae s.s.
  2. `2008_Pennetier_VK7_rainy_ctrl`: September 18 to October 14, 2006 (rainy season), Anopheles gambiae s.s.
- A third survey was created for the treated experimental hut collections:
  3. `2008_Pennetier_VK7_rainy_treated_S`: September 18 to October 14, 2006 (rainy season), molecular S form of An. gambiae s.s. used for testing selection pressure in Table 3.
- Genotype counts (RR, RS, SS) were not explicitly provided in Table 1 or Table 3 (only allele frequencies and N tested are given), so count fields are left null and `reported_allele_freq` is filled as per Rule 2.

### Bioassays & Genotype-Phenotype
- No standard WHO tube/CDC bottle bioassays were conducted; experimental hut daily mortality data were modeled using logistic regressions. Following Rule 8b, no bioassay records were derived from hut trials.
- Genotype-phenotype data from Table 3 were extracted into `geno_pheno` with `bioassay_id: null` and insecticide names as reported.

## Validator warnings

- genotype #1 (2008_Pennetier_VK7_dry_ctrl, kdr L1014F): frequency only (no raw counts)
- genotype #2 (2008_Pennetier_VK7_dry_ctrl, Ace1 Ace1R): frequency only (no raw counts)
- genotype #3 (2008_Pennetier_VK7_rainy_ctrl, kdr L1014F): frequency only (no raw counts)
- genotype #4 (2008_Pennetier_VK7_rainy_ctrl, Ace1 Ace1R): frequency only (no raw counts)
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
