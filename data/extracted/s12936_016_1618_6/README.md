# Extraction record — s12936_016_1618_6

- Extracted: 2026-10-09
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 38 · Genotype rows: 14 · Bioassays: 25 · Geno-pheno rows: 0

## Decisions

### Extraction Decisions

- **Surveys**: Split by site, year, and species. For bioassays, we have 2011 and 2013 surveys of *Anopheles gambiae* s.l. For genotypes, we have 2011-2013 pooled surveys of *An. gambiae* s.s. and *An. arabiensis*, as reported in Table 3.
- **Genotypes**: Only 7 sites had genotype data reported in Table 3. For Busoro *An. arabiensis*, N is printed as 0 in Table 3, which is an inconsistency since SS=12, RS=28, RR=0. We recorded N=0 as printed and added an inconsistency note.
- **Bioassays**: Bioassay counts (dead/alive) were not printed, so we left them null and set `dead_alive_printed` to false. Synergist bioassays with PBO were extracted from Table 4 and Table 5.

## Validator warnings

- genotype #2 (s12936_016_1618_6_busoro_2011_2013_ar, Vgsc L1014S): inconsistent in the paper (values kept as printed) — An. arabiensis N is printed as 0, but SS (12) + RS (28) + RR (0) = 40, which matches the total tested of 44 minus 4 An. gambiae s.s.
- genotype #2 (s12936_016_1618_6_busoro_2011_2013_ar, Vgsc L1014S): RR+RS+SS = 0+28+12 = 40 but n_genotyped = 0
