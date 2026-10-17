# Extraction record — 2013_Aikpon_Bendiocarb_Resistance_Anopheles_Gambiae_Population_PMID23803527

- Extracted: 2026-10-17
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 14 · Genotype rows: 9 · Bioassays: 20 · Geno-pheno rows: 0

## Decisions

### Survey and Genotype Extraction Decisions
- **Target Marker**: Only `Ace-1 G280S` (reported as `ace-1R` / `G119S` by PCR-RFLP) was assayed in field populations in this paper. Pyrethroid kdr frequencies mentioned in the background (page 2) were cited as 'Aïkpon, personal communication' from a previous survey, not primary data from this study.
- **Resolution**: In Table 2, genotypes are reported per district (Kouandé, Matéri, Natitingou, Péhunco, Tanguiéta) and per molecular form (S form = *Anopheles gambiae s.s.*, M form = *Anopheles coluzzii*). In Péhunco, 0 M-form specimens were found, so only an S-form genotype survey was created. In total, 9 fine-scale genotype records were extracted (representing all 252 genotyped mosquitoes).
- **Bioassays**: Table 1 reports WHO tube bioassays with 4 insecticides (bendiocarb 0.1%, propoxur 0.1%, pirimiphos-methyl 0.25%, and fenitrothion 1%) across the 5 districts. Kisumu susceptible strain controls were excluded per Rule 5. Because bioassays were conducted on wild-reared adult *An. gambiae s.s.* before molecular form discrimination, district-level surveys for *An. gambiae s.s.* were created to link the 20 bioassays. Exact counts of dead/alive were not printed in Table 1 (only n_exposed and % mortality), so `dead_alive_printed` was set to `false` and counts left null.
- **Figure 2 / Genotype-Phenotype**: Figure 2 shows the ace-1R genotype breakdown between bendiocarb survivors (n=109) and dead (n=143) mosquitoes pooled across all 5 districts and both molecular forms. Exact genotype counts (RR/RS/SS) were not printed (only an unlabelled stacked bar chart with allele frequencies 0.206 and 0.045). Because these are the exact same 252 individuals already extracted at fine resolution (by district and molecular form) in Table 2, and Figure 2 is an overall pooled summary that violates Rule 7 and Rule 6 (no double counting), Figure 2 was not duplicated into `geno_pheno`.
