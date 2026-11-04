# Extraction record — 2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583

- Extracted: 2026-11-04
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 24 · Genotype rows: 24 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Extraction Decisions

1. **Surveys & Spatial Breakdown**: Defined per study site (Buliisa, Hoima, Kyankwanzi, Rubirizi/Muhorro in Kibaale district), collection year (2009 to 2012), and molecularly identified species (*An. gambiae s.s.* and *An. arabiensis*). Coordinates given in the paper were converted from degrees-minutes-seconds to decimal degrees. In Kibaale, the collection site changed from Rubirizi village in 2009 to Muhorro village in May 2010 onwards.
2. **Genotype Counts vs Percentages**: Table 5 reports percent allele frequency, total sample size N, and percentage homozygous resistant (RR). Per Rule 2, count fields (`rr`, `rs`, `ss`) are left `null` because raw counts are not explicitly printed, and frequencies are recorded in `reported_allele_freq` (converted to a 0-1 scale).
3. **kdr L1014F Data**: The paper mentions testing a small subset of samples for *kdr* L1014F (N=47 for *An. gambiae s.s.* and N=19 for *An. arabiensis*), but reports results only pooled across all sites and years combined (overall genotype frequencies 24.5% and 31.6%, respectively). Because site/year resolution is unavailable for L1014F, these pooled counts were dropped to adhere to Rule 7.
4. **Bioassays & Genotype-Phenotype**: The manuscript mentions that phenotypic resistance assays were not part of this study (only unpublished 2013 WHO tube bioassay data mentioned in Discussion), so no bioassays or genotype-phenotype association data were extracted.

## Validator warnings

- genotype #1 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_hoima_2009_gam, kdr L1014S): frequency only (no raw counts)
- genotype #2 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_hoima_2010_gam, kdr L1014S): frequency only (no raw counts)
- genotype #3 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_hoima_2011_gam, kdr L1014S): frequency only (no raw counts)
- genotype #4 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_hoima_2011_ara, kdr L1014S): frequency only (no raw counts)
- genotype #5 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_hoima_2012_gam, kdr L1014S): frequency only (no raw counts)
- genotype #6 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_kyankwanzi_2009_gam, kdr L1014S): frequency only (no raw counts)
- genotype #7 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_kyankwanzi_2009_ara, kdr L1014S): frequency only (no raw counts)
- genotype #8 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_kyankwanzi_2010_gam, kdr L1014S): frequency only (no raw counts)
- genotype #9 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_kyankwanzi_2011_gam, kdr L1014S): frequency only (no raw counts)
- genotype #10 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_kyankwanzi_2011_ara, kdr L1014S): frequency only (no raw counts)
- genotype #11 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_kyankwanzi_2012_gam, kdr L1014S): frequency only (no raw counts)
- genotype #12 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_kyankwanzi_2012_ara, kdr L1014S): frequency only (no raw counts)
- genotype #13 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_buliisa_2009_gam, kdr L1014S): frequency only (no raw counts)
- genotype #14 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_buliisa_2009_ara, kdr L1014S): frequency only (no raw counts)
- genotype #15 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_buliisa_2010_gam, kdr L1014S): frequency only (no raw counts)
- genotype #16 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_buliisa_2010_ara, kdr L1014S): frequency only (no raw counts)
- genotype #17 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_buliisa_2011_gam, kdr L1014S): frequency only (no raw counts)
- genotype #18 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_buliisa_2011_ara, kdr L1014S): frequency only (no raw counts)
- genotype #19 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_buliisa_2012_gam, kdr L1014S): frequency only (no raw counts)
- genotype #20 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_buliisa_2012_ara, kdr L1014S): frequency only (no raw counts)
- genotype #21 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_rubirizi_2009_gam, kdr L1014S): frequency only (no raw counts)
- genotype #22 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_muhorro_2010_gam, kdr L1014S): frequency only (no raw counts)
- genotype #23 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_muhorro_2011_gam, kdr L1014S): frequency only (no raw counts)
- genotype #24 (2015_Helinski_Entomological_Surveillance_Following_Long_Lasting_PMID26382583_muhorro_2012_gam, kdr L1014S): frequency only (no raw counts)
