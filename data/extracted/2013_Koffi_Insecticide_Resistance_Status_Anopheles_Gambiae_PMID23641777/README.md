# Extraction record — 2013_Koffi_Insecticide_Resistance_Status_Anopheles_Gambiae_PMID23641777

- Extracted: 2026-11-15
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 6 · Bioassays: 18 · Geno-pheno rows: 0

## Decisions

### Study Decisions
- **Surveys**: Three surveys were created: two for molecular forms (M form = An. coluzzii, N=223; S form = An. gambiae s.s., N=3) as genotypes are reported separated by molecular form, and one survey for the bioassay population (tested as An. gambiae s.s., wild-reared from larvae collected in May 2012 in M'Bé).
- **Genotypes**: Exactly reported in text (Page 5) and Table 2. For M-form: kdr L1014F (RR=16, RS=114, SS=93, N=223, freq=0.33); kdr L1014S (RR=0, RS=0, SS=223, N=223, freq=0.0); ace-1 G119S (RR=0, RS=0, SS=223, N=223, freq=0.0). For S-form: kdr L1014F (1 SS, 1 RS, 1 RR, N=3); kdr L1014S (0 detected, SS=3); ace-1 G119S (0 detected, SS=3). The pooled sample (N=226) from Table 2 was not extracted to avoid double-counting per Rule 7.
- **Bioassays**: Extracted from Figure 1 and Table 1 for all 10 diagnostic concentrations tested alone and 8 tested with PBO pre-exposure. Because raw dead and alive counts were not printed in the paper or figure (only percentage mortality and total exposed N are given), dead_alive_printed is set to false, and n_dead and n_alive are left null. Kisumu reference strain controls were omitted per Rule 5.
- **Geno-Pheno**: No genotype-phenotype links were reported (mosquitoes were not genotyped separately by bioassay outcome).

## Validator warnings

- bioassay 2013_Koffi_Mbe_2012_bioassay_dieldrin: inconsistent in the paper (values kept as printed) — Figure 1 reports 27.2% mortality (N=297); page 4 text mentions 21.8% in one paragraph and 27.3% in another.
- bioassay 2013_Koffi_Mbe_2012_bioassay_permethrin: inconsistent in the paper (values kept as printed) — Figure 1 reports 51.2% mortality (N=201), whereas page 4 text reports 50.8% mortality.
- bioassay 2013_Koffi_Mbe_2012_bioassay_deltamethrin: inconsistent in the paper (values kept as printed) — Figure 1 reports N=264 exposed for deltamethrin alone, whereas Table 1 reports N=208 for knockdown evaluation.
- bioassay 2013_Koffi_Mbe_2012_bioassay_alphacypermethrin: inconsistent in the paper (values kept as printed) — Figure 1 reports N=240 exposed for alpha-cypermethrin alone, whereas Table 1 reports N=197 for knockdown evaluation.
- bioassay 2013_Koffi_Mbe_2012_bioassay_etofenprox: inconsistent in the paper (values kept as printed) — Concentration is printed as 0.05% on page 3, but as 0.5% in Table 1 and Figure 1.
- bioassay 2013_Koffi_Mbe_2012_bioassay_etofenprox_pbo: inconsistent in the paper (values kept as printed) — Figure 1 reports 58.2% mortality (N=91), whereas page 4 text states mortalities increased to 63.3%.
