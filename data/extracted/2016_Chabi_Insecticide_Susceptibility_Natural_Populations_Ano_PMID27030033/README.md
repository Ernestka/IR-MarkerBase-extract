# Extraction record — 2016_Chabi_Insecticide_Susceptibility_Natural_Populations_Ano_PMID27030033

- Extracted: 2026-11-19
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 4 · Bioassays: 7 · Geno-pheno rows: 24

## Decisions

# Extraction Decisions for Chabi et al. (2016)

## Survey Structure
- Mosquito larvae were sampled from water pools in the irrigated rice area of Okyereko, Ghana (05°24’57.68”N, 00°35’53.99”W), and reared to adult F1 progeny.
- Three surveys were defined:
  1. `2016_Chabi_Okyereko_coluzzii`: An. coluzzii identified molecularly (N = 193), corresponding to the species-specific baseline genotype data in Table 1.
  2. `2016_Chabi_Okyereko_gambiae_ss`: An. gambiae s.s. identified molecularly (N = 7), corresponding to the species-specific baseline genotype data in Table 1.
  3. `2016_Chabi_Okyereko_gambiae_sl`: An. gambiae (s.l.) representing the mosquitoes tested in standard WHO susceptibility assays and the phenotype-stratified genotyping in Table 2.
- Dates of collection are not reported in the manuscript (article was submitted November 2015, published March 2016); start and end dates are left null.

## Genotypes (Table 1)
- Table 1 reports kdr L1014F (Vgsc L995F) and ace-1 G119S (Ace-1 G280S) counts for An. coluzzii and An. gambiae s.s.
- Both markers were extracted exactly as printed for both species.
- The text in the abstract and results refers to ace-1 frequency as '0.2 %' and '0.3 %', but Table 1 lists '0.2' and '0.3' as proportions, which closely match the allele frequencies calculated from the counts (70/386 = 0.181 and 4/14 = 0.286). An inconsistency note was added to document this.

## Bioassays
- Seven diagnostic dose bioassays against An. gambiae (s.l.) were extracted from page 4 text:
  - Deltamethrin 0.05% (N = 157, mortality = 34.1%)
  - Permethrin 0.75% (N = 132, mortality = 18.4%)
  - DDT 4% (mortality = 0%; text states 'an average of 100 mosquitoes for all other insecticides', exact N exposed left null)
  - Bendiocarb 0.1% (mortality = 64.0%, N exposed left null)
  - Propoxur 0.1% (mortality = 57.0%, N exposed left null)
  - Fenitrothion 1% (2 h exposure, mortality = 86.0%, N exposed left null)
  - Malathion 5% (mortality = 100.0%, N exposed left null)
- Control bioassays and synergist tests presented only as bar charts without exact printed numerical values were not extracted.

## Genotype-Phenotype Data (Table 2)
- Table 2 reports kdr L1014F and ace-1 G119S counts for bioassay survivors ('Alive') and non-survivors ('Dead') across the tested insecticides.
- Each condition was extracted into `geno_pheno` linked to its corresponding single bioassay ID.
- Negative control mosquitoes (N = 5) and pooled summary rows ('Total tested') were omitted in accordance with Rule 6 (enum restricted to alive/dead) and Rule 7 (no pooled totals).

## Validator warnings

- genotype #1 (2016_Chabi_Okyereko_coluzzii, kdr kdr L1014F): computed allele freq 0.860 differs from reported 0.9
- genotype #2 (2016_Chabi_Okyereko_coluzzii, ace-1 ace-1 G119S): inconsistent in the paper (values kept as printed) — Text on pages 1 and 5 states 0.2 %, but Table 1 reports Freq/species as 0.2 (proportion), which matches rounded allele frequency (70/386 = 0.181).
- genotype #3 (2016_Chabi_Okyereko_gambiae_ss, kdr kdr L1014F): computed allele freq 0.857 differs from reported 0.9
- genotype #4 (2016_Chabi_Okyereko_gambiae_ss, ace-1 ace-1 G119S): inconsistent in the paper (values kept as printed) — Text on page 5 states 0.3 %, but Table 1 reports Freq/species as 0.3 (proportion), matching rounded allele frequency (4/14 = 0.286).
