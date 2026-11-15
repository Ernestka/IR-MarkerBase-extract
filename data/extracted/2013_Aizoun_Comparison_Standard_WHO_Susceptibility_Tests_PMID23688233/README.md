# Extraction record — 2013_Aizoun_Comparison_Standard_WHO_Susceptibility_Tests_PMID23688233

- Extracted: 2026-11-15
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 0 · Bioassays: 18 · Geno-pheno rows: 16

## Decisions

### Data Extraction Decisions

1. **Surveys & Sampling**: Surveys are split into four localities in Ouémé department, southern Benin (Adjara, Dangbo, Misserete, and Seme). Larvae and pupae were sampled during the rainy seasons (March-July and September-November 2010) and reared to adults for bioassay and molecular testing. PCR identified 100% of tested specimens as *Anopheles gambiae s.s.*.
2. **Genotypes & Phenotype Split**: Tables 2 and 3 report genotype counts specifically split by bioassay outcome (Table 2: survivors 24 h post-exposure to deltamethrin; Table 3: dead mosquitoes 24 h post-exposure to deltamethrin and bendiocarb). Following Rule 6, all genotype counts are captured in `geno_pheno` to prevent double counting, and `genotypes` is left empty since no unselected/non-phenotyped population sample was genotyped.
3. **Bioassay Linkage for Geno-Pheno**: `bioassay_id` is set to `null` because Table 2 pools survivors from bioassays, and Table 3 pools dead mosquitoes from both deltamethrin and bendiocarb exposures.
4. **Bioassays**: Extracted all field population WHO tube tests (0.05% deltamethrin, 0.1% bendiocarb) and CDC bottle bioassays (12.5 µg/bottle deltamethrin, 12.5 µg/bottle bendiocarb) reported in Table 4. Reference strain (Kisumu) bioassays were excluded per Rule 5. Because Table 4 gives sample sizes (`n_exposed`) and percentage mortality rather than printed integer counts of dead and alive mosquitoes, `dead_alive_printed` is set to `false`, and `n_dead`/`n_alive` are left `null` per Rule 2.
5. **Markers**: The kdr mutation is described in text as the 'Leu-phe' mutation following Martinez-Torres et al. (1998), which represents Vgsc L1014F (L995F). The marker is recorded as `L1014F` under gene `kdr`. Ace-1 G119S (G280S) is recorded as `G119S` under gene `Ace-1`.

## Validator warnings

- geno_pheno #1 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #2 (deltamethrin, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #3 (deltamethrin + bendiocarb, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + bendiocarb)
- geno_pheno #4 (deltamethrin + bendiocarb, Ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + bendiocarb)
- geno_pheno #5 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #6 (deltamethrin, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #7 (deltamethrin + bendiocarb, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + bendiocarb)
- geno_pheno #8 (deltamethrin + bendiocarb, Ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + bendiocarb)
- geno_pheno #9 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #10 (deltamethrin, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #11 (deltamethrin + bendiocarb, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + bendiocarb)
- geno_pheno #12 (deltamethrin + bendiocarb, Ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + bendiocarb)
- geno_pheno #13 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #14 (deltamethrin, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #15 (deltamethrin + bendiocarb, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + bendiocarb)
- geno_pheno #16 (deltamethrin + bendiocarb, Ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + bendiocarb)
