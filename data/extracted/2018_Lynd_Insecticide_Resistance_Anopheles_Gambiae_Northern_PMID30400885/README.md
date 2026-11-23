# Extraction record — 2018_Lynd_Insecticide_Resistance_Anopheles_Gambiae_Northern_PMID30400885

- Extracted: 2026-11-23
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 16 · Bioassays: 16 · Geno-pheno rows: 0

## Decisions

### Data Extraction & Decision Notes

- **Surveys**: Split by survey location (Pambwa, Fiwa, Bassa) and molecular species. An. coluzzii was detected only at Fiwa (N=4, 12.5% of larval collections at that site) and was extracted as a distinct survey.
- **Target Markers Extracted**:
  - `Vgsc L1014F` (gene: `Vgsc`, marker: `L1014F`)
  - `Vgsc L1014S` (gene: `Vgsc`, marker: `L1014S`)
  - `Vgsc N1575Y` (gene: `Vgsc`, marker: `N1575Y`)
  - `Ace-1 G119S` (gene: `Ace-1`, marker: `G119S`)
- **Genotypes & Frequencies**:
  - Table 2 prints genotype frequencies (proportions) for L1014 (FF, FS, SS, LF). Per Rule 2, since only frequencies are printed for An. gambiae s.s., genotype counts (`rr`, `rs`, `ss`) are left null and calculated allele frequencies are reported in `reported_allele_freq`.
  - For Fiwa *An. coluzzii* (N=4), the text explicitly states that 2 were FF and 2 were LF (wild type/1014F heterozygotes), so exact counts are provided.
  - `Ace-1 G119S` was screened in 368 specimens and zero mutants were found (all wild-type SS).
  - `Vgsc N1575Y` allele frequencies are recorded from text (Pambwa 0.01, Fiwa s.s. 0.02, Fiwa coluzzii 0.25, Bassa 0.00).
- **Bioassays**:
  - Extracted per site from Figure 1 for standard WHO tube tests (deltamethrin 0.05%, permethrin 0.75%, bendiocarb 0.1%, DDT 4%, and pyrethroids pre-exposed to 4% PBO).
  - `n_exposed` values are printed above each bar in Figure 1. Mortality percentages were read directly from Figure 1.
  - Control bioassays were excluded as standard reference/negative controls.
- **Genotype-Phenotype**:
  - The main text mentions statistical associations (odds ratios, chi-square P-values) between 1014F and pyrethroid survival, but individual genotype counts per survivor/dead group are not printed in the paper text/tables, so `geno_pheno` is left empty.

## Validator warnings

- genotype #1 (2018_Lynd_bassa_2016_ss, Vgsc L1014F): frequency only (no raw counts)
- genotype #2 (2018_Lynd_bassa_2016_ss, Vgsc L1014S): frequency only (no raw counts)
- genotype #5 (2018_Lynd_pambwa_2016_ss, Vgsc L1014F): frequency only (no raw counts)
- genotype #6 (2018_Lynd_pambwa_2016_ss, Vgsc L1014S): frequency only (no raw counts)
- genotype #7 (2018_Lynd_pambwa_2016_ss, Vgsc N1575Y): frequency only (no raw counts)
- genotype #9 (2018_Lynd_fiwa_2016_ss, Vgsc L1014F): frequency only (no raw counts)
- genotype #10 (2018_Lynd_fiwa_2016_ss, Vgsc L1014S): frequency only (no raw counts)
- genotype #11 (2018_Lynd_fiwa_2016_ss, Vgsc N1575Y): frequency only (no raw counts)
- genotype #15 (2018_Lynd_fiwa_2016_col, Vgsc N1575Y): frequency only (no raw counts)
