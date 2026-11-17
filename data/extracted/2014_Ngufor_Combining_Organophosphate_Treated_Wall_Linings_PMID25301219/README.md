# Extraction record — 2014_Ngufor_Combining_Organophosphate_Treated_Wall_Linings_PMID25301219

- Extracted: 2026-11-17
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 0 · Bioassays: 2 · Geno-pheno rows: 40

## Decisions

1. **Surveys**: Three surveys were created: (a) larval collections from the experimental hut rice fields reared to adults for WHO tube bioassays, (b) the first 6-week experimental hut trial evaluating single interventions (wall linings and net wall hangings), and (c) the second 6-week experimental hut trial evaluating combination interventions with LLINs.
2. **Bioassays**: Two WHO tube susceptibility tests from Table 1 were extracted (deltamethrin 0.05% and pirimiphos-methyl 0.25%). Number tested was 99 for both, with 43% and 4% 24-hr mortality reported, respectively; n_dead and n_alive were left null with dead_alive_printed = false. WHO cone bioassays and susceptibility tests on the Kisumu laboratory strain were excluded as reference controls.
3. **Genotypes & Genotype-Phenotype**: All genotyped mosquitoes from the experimental huts (Tables 4 and 5) were reported categorized by hut treatment and phenotypic outcome (alive vs dead after overnight entry and 24 h holding period). Following extraction rules, these were placed entirely in `geno_pheno` to prevent double-counting with `genotypes`. Table 5 provides `% alive (live/total)` for each genotype class (SS, RS, RR); alive genotype counts correspond to the numerators, and dead genotype counts were obtained as total minus live. Minor sample size discrepancies between Table 5 sums and the n values in Table 4 are fully documented in `inconsistency_note`.

## Validator warnings

- geno_pheno #1 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #1 (deltamethrin, kdr L1014F, alive): inconsistent in the paper (values kept as printed) — Table 5 live counts sum to 74 (SS=1, RS=16, RR=57), but Table 4 reports n=75 (freq=0.87).
- geno_pheno #2 (deltamethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #2 (deltamethrin, kdr L1014F, dead): inconsistent in the paper (values kept as printed) — Table 5 total minus live counts give SS=2, RS=6, RR=31 (sum=39), but Table 4 reports n=38 (freq=0.89).
- geno_pheno #3 (pirimiphos-methyl, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #4 (pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #5 (pirimiphos-methyl, ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #6 (pirimiphos-methyl, ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #7 (pirimiphos-methyl, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #8 (pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #9 (pirimiphos-methyl, ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #10 (pirimiphos-methyl, ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #11 (pirimiphos-methyl, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #12 (pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #13 (pirimiphos-methyl, ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #14 (pirimiphos-methyl, ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #15 (pirimiphos-methyl, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #16 (pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #17 (pirimiphos-methyl, ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #18 (pirimiphos-methyl, ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #18 (pirimiphos-methyl, ace-1 G119S, dead): inconsistent in the paper (values kept as printed) — Table 5 total minus live counts give SS=9, RS=32, RR=3 (sum=44), but Table 4 reports n=45 (freq=0.44).
- geno_pheno #19 (untreated net, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: untreated net)
- geno_pheno #20 (untreated net, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: untreated net)
- geno_pheno #21 (untreated net, ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: untreated net)
- geno_pheno #22 (untreated net, ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: untreated net)
- geno_pheno #23 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #24 (deltamethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #25 (pirimiphos-methyl, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #26 (pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #27 (pirimiphos-methyl, ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #27 (pirimiphos-methyl, ace-1 G119S, alive): inconsistent in the paper (values kept as printed) — Table 5 live counts sum to 26 (SS=1, RS=23, RR=2), but Table 4 reports n=24 (freq=0.52).
- geno_pheno #28 (pirimiphos-methyl, ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #28 (pirimiphos-methyl, ace-1 G119S, dead): inconsistent in the paper (values kept as printed) — Table 5 total minus live counts give SS=5, RS=10, RR=3 (sum=18), but Table 4 reports n=24 (freq=0.50).
- geno_pheno #29 (pirimiphos-methyl, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #30 (pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #31 (pirimiphos-methyl, ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #32 (pirimiphos-methyl, ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #33 (pirimiphos-methyl + deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + deltamethrin)
- geno_pheno #34 (pirimiphos-methyl + deltamethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + deltamethrin)
- geno_pheno #34 (pirimiphos-methyl + deltamethrin, kdr L1014F, dead): inconsistent in the paper (values kept as printed) — Table 5 total minus live counts give SS=2, RS=4, RR=34 (sum=40), but Table 4 reports n=41 (freq=0.89).
- geno_pheno #35 (pirimiphos-methyl + deltamethrin, ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + deltamethrin)
- geno_pheno #36 (pirimiphos-methyl + deltamethrin, ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + deltamethrin)
- geno_pheno #37 (pirimiphos-methyl + deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + deltamethrin)
- geno_pheno #38 (pirimiphos-methyl + deltamethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + deltamethrin)
- geno_pheno #39 (pirimiphos-methyl + deltamethrin, ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + deltamethrin)
- geno_pheno #40 (pirimiphos-methyl + deltamethrin, ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl + deltamethrin)
