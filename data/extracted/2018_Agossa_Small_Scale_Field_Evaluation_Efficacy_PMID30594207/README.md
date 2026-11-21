# Extraction record — 2018_Agossa_Small_Scale_Field_Evaluation_Efficacy_PMID30594207

- Extracted: 2026-11-21
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 1 · Bioassays: 3 · Geno-pheno rows: 0

## Decisions

### Study & Survey Design
- Wild Anopheles gambiae s.s. were collected monthly as larvae from Dangbo district, Benin, and reared to 2-5 day old adults for baseline WHO tube tests, wall cone bioassays, and resistance mechanism characterization.
- No exact sampling start and end dates were reported; ethical clearance was issued in May/June 2015 and the manuscript was received in February 2018.

### Genotypes
- The paper reports the 'Leu-Phe kdr mutation' detected by PCR (Martinez-Torres et al. 1998), which corresponds to target marker Vgsc L995F (L1014F). The marker is recorded with gene 'Vgsc' and marker 'L995F' as specified in the target markers list.
- The text states: 'Molecular analysis of the wild Anopheles population from Dangbo showed very high frequency of kdr mutation (0.99) (49/50)'. Per extraction instructions, n_carriers is set to 49, n_genotyped to 50, and reported_allele_freq to 0.99, with an inconsistency note explaining the potential interpretations.

### Bioassays
- Standard baseline WHO tube tests against wild An. gambiae s.s. are extracted from Figure 2 (deltamethrin 0.05%, bendiocarb 0.1%, pirimiphos-methyl 0.25%). Number exposed and reported mortality percentages are provided, but exact numbers of dead/alive are not printed, so dead_alive_printed is false and n_dead/n_alive are null.
- Wall cone bioassays across multiple substrate formulations and months (Figures 4–9 and Additional files 1 and 2) are not extracted as numerical counts are only presented in graphs or supplementary tables not included in the main text.
- Susceptible Kisumu control tests were excluded as laboratory controls.
- No genotype-phenotype associations were reported.

## Validator warnings

- genotype #1 (2018_Agossa_Small_Scale_Field_Evaluation_Efficacy_PMID30594207_dangbo, Vgsc L995F): inconsistent in the paper (values kept as printed) — The paper states 'frequency of kdr mutation (0.99) (49/50)'. It is not explicitly stated whether 49/50 represents carriers (which would give a carrier frequency of 0.98) or if there were 49 RR homozygotes and 1 RS heterozygote ((49*2 + 1)/100 = 0.99 allele frequency).
