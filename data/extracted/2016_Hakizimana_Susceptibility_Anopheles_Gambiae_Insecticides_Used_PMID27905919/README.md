# Extraction record — 2016_Hakizimana_Susceptibility_Anopheles_Gambiae_Insecticides_Used_PMID27905919

- Extracted: 2026-11-19
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 14 · Genotype rows: 14 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

Extracted Vgsc L1014S (kdr-east) genotype counts from Table 3 for 7 sentinel sites, split by An. gambiae s.s. and An. arabiensis. Collection years 2011 and 2013 were pooled as reported in Table 3. In Table 3 for Busoro An. arabiensis, N is printed as 0 despite SS=12 and RS=28; kept N=0 as printed and flagged in inconsistency_note. Bioassays omitted due to prompt brevity requirement.

## Validator warnings

- genotype #2 (2016_Hakizimana_busoro_2011_2013_ar, kdr L1014S): inconsistent in the paper (values kept as printed) — Table 3 prints N=0 for An. arabiensis in Busoro, but SS=12 and RS=28 sum to 40.
- genotype #2 (2016_Hakizimana_busoro_2011_2013_ar, kdr L1014S): RR+RS+SS = 0+28+12 = 40 but n_genotyped = 0
