# Extraction record — 2018_Agossa_Efficacy_Novel_Mode_Action_Indoor_PMID29747684

- Extracted: 2026-11-21
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 2 · Bioassays: 3 · Geno-pheno rows: 0

## Decisions

### Decisions & Assumptions
- **Marker Naming**: Corrected marker naming strings so that `gene` and `marker` map directly to standard target marker aliases (`kdr` / `L1014F` for Vgsc L995F and `Ace-1` / `G119S` for Ace-1 G280S).
- **Survey Scope**: Extracted one survey corresponding to the baseline population characterisation at the experimental hut station in Covè, Benin (October 2015).
- **Genotypes**: Extracted exact target site mutation counts from Table 2 for kdr L1014F (Vgsc L995F) and Ace-1 G119S (Ace-1 G280S) from N=30 untested wild mosquitoes.
- **Bioassays**: Extracted baseline WHO tube bioassays performed prior to IRS spraying in October 2015 against wild Anopheles gambiae (s.l.) for deltamethrin 0.05%, pirimiphos-methyl 0.25%, and bendiocarb 0.1%. Sample sizes (n_exposed) are printed in Fig 2; mortality percentages for deltamethrin and pirimiphos-methyl are printed in the text. Bendiocarb percentage was presented as a bar chart without printed numerical text, so `reported_mortality_pct` is set to null per rule 2.
- **Exclusions**: Laboratory Kisumu strain bioassays and monthly experimental hut wall cone bioassay residual mortality figures (which present percentages only in graphs without exact numerical tables) were excluded per guidelines.
