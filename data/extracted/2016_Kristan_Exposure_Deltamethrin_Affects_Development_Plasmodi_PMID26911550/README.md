# Extraction record — 2016_Kristan_Exposure_Deltamethrin_Affects_Development_Plasmodi_PMID26911550

- Extracted: 2026-11-19
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 4 · Bioassays: 1 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions
- **Surveys**: Mosquitoes were collected as larvae around Butemba Health Centre III in Kyankwanzi District, Uganda between August 2013 and June 2014 and reared to adults. PCR identified *An. gambiae s.s.* (763) and *An. arabiensis* (73). A separate survey was created for *An. gambiae s.l.* for the WHO bioassay (n=87).
- **Target Markers**: 
  - `kdr-L1014S` (exact paper notation for Vgsc L995S): Extracted exact genotype counts (SS, RS, RR) from Table 1 for both *An. gambiae s.s.* (732 genotyped: 4 SS, 34 RS, 694 RR) and *An. arabiensis* (73 genotyped: 72 SS, 0 RS, 1 RR).
  - `ace-1 G119S` (exact paper notation for Ace-1 G280S): Paper explicitly reports all specimens were homozygous susceptible at the ace-1 locus.
  - `kdr-L1014F` was mentioned in the methods PCR panel description, but no results/counts were reported in the text or tables, so no genotype record was generated for it.
- **Bioassays**: Extracted the standard WHO susceptibility test for deltamethrin 0.05% in *An. gambiae s.l.* (n=87, 71.9% mortality). Set `dead_alive_printed = false` since exact numbers of dead/alive were not printed. Experimental net exposures for *Plasmodium falciparum* sporogonic development were performed on a pre-selected RR subset and are non-standard experimental exposures, so they were excluded from bioassays per extraction rules.
