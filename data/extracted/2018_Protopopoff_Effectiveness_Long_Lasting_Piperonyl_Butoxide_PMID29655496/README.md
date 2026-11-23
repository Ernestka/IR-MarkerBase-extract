# Extraction record — 2018_Protopopoff_Effectiveness_Long_Lasting_Piperonyl_Butoxide_PMID29655496

- Extracted: 2026-11-23
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 2 · Bioassays: 2 · Geno-pheno rows: 0

## Decisions

### Data Extraction Notes

- **Study Design**: Cluster randomized controlled trial evaluating PBO-LLINs and pirimiphos-methyl IRS in Muleba district, Kagera region, Tanzania (March 2015 to December 2016).
- **Genotypes**:
  - `An. arabiensis`: 247 tested by TaqMan PCR; zero mutations detected for either Vgsc 1014F or 1014S, yielding RR=0, RS=0, SS=247 for both markers.
  - `An. gambiae s.s.`: Page 9 states: 'The Vgsc gene mutation was found in all tested A gambiae with co-occurrence of Vgsc-1014F and Vgsc-1014S in 22 (9%) of 234 A gambiae mosquitoes.' Because specific single-allele carrier counts or genotype splits (RR, RS, SS) for Vgsc 1014F and 1014S separately are not reported, genotype rows for An. gambiae s.s. were omitted to avoid creating empty records without counts or frequencies.
- **Bioassays**:
  - WHO cylinder tests using 0.75% permethrin were reported on page 9 for `An. gambiae s.l.` (54 dead / 613 exposed, 8.8% mortality) and `An. funestus` (59 dead / 108 exposed, 54.5% mortality). Exact dead and exposed counts were printed (`n/N=54/613` and `n/N=59/108`), so `dead_alive_printed` is set to true and `n_alive` derived by subtraction.
  - CDC bottle bioassay LC50 ratios were mentioned in text without individual test sample sizes or mortality counts, so no CDC bottle bioassay records were extracted.
