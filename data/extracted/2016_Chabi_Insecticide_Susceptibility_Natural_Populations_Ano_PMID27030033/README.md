# Extraction record — 2016_Chabi_Insecticide_Susceptibility_Natural_Populations_Ano_PMID27030033

- Extracted: 2026-11-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 4 · Bioassays: 7 · Geno-pheno rows: 24

## Decisions

### Survey and Species Stratification
- Larvae were collected from water pools around irrigated rice fields in Okyereko, Ghana (05°24’57.68”N, 00°35’53.99”W) and reared to F1 adults for WHO susceptibility bioassays.
- A subset of 200 mosquitoes sampled from the bioassays were identified molecularly to species (193 An. coluzzii, 7 An. gambiae s.s.). Genotypes are reported broken down by molecular species in Table 1, and broken down by bioassay phenotypic outcome (alive vs dead for 7 insecticides) for An. gambiae s.l. in Table 2.
- Three surveys were defined:
  1. `2016_Chabi_Insecticide_Okyereko_coluzzii` for An. coluzzii (N=193).
  2. `2016_Chabi_Insecticide_Okyereko_gambiae_ss` for An. gambiae (s.s.) (N=7).
  3. `2016_Chabi_Insecticide_Okyereko_gambiae_sl` for the population-level bioassays and phenotype-stratified genotyping in Table 2.

### Genotypes (Table 1)
- Table 1 reports raw counts for kdr L1014F (Vgsc L995F) and ace-1 G119S (Ace-1 G280S) for An. coluzzii (N=193) and An. gambiae s.s. (N=7).
- Text on page 5 incorrectly states the ace-1 frequency as '2 %' and '0.2 %' for An. coluzzii and '0.3 %' for An. gambiae s.s. Table 1 correctly reports 0.2 and 0.3 as proportions/frequencies (70/386 = 0.181 and 4/14 = 0.286), which are captured exactly as printed.

### Bioassays
- Seven standard diagnostic WHO tube assays were tested: deltamethrin 0.05%, permethrin 0.75%, DDT 4%, bendiocarb 0.1%, propoxur 0.1%, fenitrothion 1% (2 h exposure), and malathion 5%. Mortality was recorded at 24 h.
- n_exposed is printed only for deltamethrin (157) and permethrin (132); the text describes 'an average of 100 mosquitoes for all other insecticides', so n_exposed is recorded as null for DDT, bendiocarb, propoxur, fenitrothion, and malathion. Synergist bioassays were reported only in a bar chart without printed counts or percentages in text and were omitted.

### Genotype-Phenotype (Table 2)
- 12 phenotype groups across 7 insecticides (Deltamethrin alive/dead, Permethrin alive/dead, DDT alive, Bendiocarb alive/dead, Propoxur alive/dead, Fenitrothion alive/dead, Malathion dead) were extracted for kdr L1014F and ace-1 G119S, each linked to their respective bioassay.
- Total rows and negative control mosquitoes (N=5) from Table 2 were excluded per extraction rules.

## Validator warnings

- genotype #1 (2016_Chabi_Insecticide_Okyereko_coluzzii, kdr L1014F): computed allele freq 0.860 differs from reported 0.9
- genotype #2 (2016_Chabi_Insecticide_Okyereko_coluzzii, ace-1 G119S): inconsistent in the paper (values kept as printed) — Table 1 reports Freq/species of 0.2 (70/386 = 0.181), whereas the text on page 5 erroneously reports 'frequency of 2 % ace-1 mutation' and '0.2 % in An. coluzzii'.
- genotype #3 (2016_Chabi_Insecticide_Okyereko_gambiae_ss, kdr L1014F): computed allele freq 0.857 differs from reported 0.9
- genotype #4 (2016_Chabi_Insecticide_Okyereko_gambiae_ss, ace-1 G119S): inconsistent in the paper (values kept as printed) — Table 1 reports Freq/species of 0.3 (4/14 = 0.286), whereas the text on page 5 erroneously reports '0.3 % in An. gambiae (s.s.)'.
