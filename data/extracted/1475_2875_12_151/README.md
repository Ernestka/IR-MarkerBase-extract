# Extraction record — 1475_2875_12_151

- Extracted: 2026-10-14
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 6 · Bioassays: 18 · Geno-pheno rows: 0

## Decisions

### Study Decisions
- **Surveys**: Mosquitoes were collected as larvae in May 2012 from rice paddies in M'Bé valley, Bandama department, Côte d'Ivoire. Following Rule 7, genotypes are extracted at the finest species resolution reported: M-form (*Anopheles coluzzii*, n=223) and S-form (*Anopheles gambiae s.s.*, n=3). A third survey representing the unsplit field-collected *Anopheles gambiae s.s.* population was created to host the WHO bioassays, which were carried out on wild-reared adult batches prior to molecular form identification.
- **Target Markers**: Assayed for `kdr` `L1014F`, `kdr` `L1014S`, and `ace-1` `G119S`. Exact counts are given on page 5: for M-form, L1014F had 16 RR, 114 RS, 93 SS (N=223); for S-form, L1014F had 1 RR, 1 RS, 1 SS (N=3). Neither L1014S nor G119S was detected in any of the 226 tested mosquitoes (all SS). The pooled sample total (N=226) is omitted to avoid double-counting.
- **Bioassays**: 18 WHO tube tests (10 without synergist, 8 with 1-h PBO pre-exposure) are reported in Figure 1 with N exposed and 24-h mortality percentages. Raw dead/alive counts are not printed (`dead_alive_printed` = false; `n_dead` and `n_alive` left null per Rule 2). Minor textual discrepancies with Figure 1 mortality values for permethrin and dieldrin, and etofenprox concentration discrepancy between methods and figures/tables, are flagged in `inconsistency_note`.
- **Excluded Data**: Susceptible laboratory reference strain (*An. gambiae s.s.* Kisumu) bioassays and knockdown rates are excluded per Rule 5. Biochemical enzyme activity assays (MFO, NSE, GST) do not represent target marker mutations and are not extractable. No genotype-phenotype splits were reported.

## Validator warnings

- bioassay 1475_2875_12_151_mbe_gambiass_et05: inconsistent in the paper (values kept as printed) — Page 3 methods list etofenprox concentration as 0.05%, whereas Table 1 and Figure 1 list 0.5%.
- bioassay 1475_2875_12_151_mbe_gambiass_et05_pbo: inconsistent in the paper (values kept as printed) — Page 3 methods list etofenprox concentration as 0.05%, whereas Table 1 and Figure 1 list 0.5%.
- bioassay 1475_2875_12_151_mbe_gambiass_per075: inconsistent in the paper (values kept as printed) — Page 4 text states 50.8% mortality for permethrin, whereas Figure 1 prints 51.2% (201).
- bioassay 1475_2875_12_151_mbe_gambiass_dld4: inconsistent in the paper (values kept as printed) — Page 4 text states 21.8% mortality in one sentence and 27.3% in another, whereas Figure 1 prints 27.2% (297).
