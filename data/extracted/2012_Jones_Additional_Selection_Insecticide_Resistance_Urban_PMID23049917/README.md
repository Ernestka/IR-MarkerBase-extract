# Extraction record — 2012_Jones_Additional_Selection_Insecticide_Resistance_Urban_PMID23049917

- Extracted: 2026-10-24
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 3 · Bioassays: 2 · Geno-pheno rows: 2

## Decisions

- Bioassay records are extracted per season (Rainy August-September 2009 and Dry January 2010) as reported for An. gambiae s.l.
- Genotype data from Table 1 for An. arabiensis combine collections across 2009-2010 and are separated into 'genotypes' (unexposed controls, N=63) and 'geno_pheno' (DDT 4% survivors, N=76, phenotype_group='alive'). Dead mosquitoes were not genotyped.
- In Table 1, LL represents wild-type homozygous (1014L/1014L = SS), LS is heterozygous (1014L/1014S = RS), and SS is mutant homozygous (1014S/1014S = RR).
- Page 5 text contains a minor typographical swap between N=63 and N=76 for exposed vs unexposed ('surviving N=63 and non-exposed N=76'). Table 1 values (Non-exposed N=63, DDT 4% N=76) were extracted as printed.
- An. gambiae s.s. kdr 1014F data are extracted into genotypes as a frequency record (freq = 0.88, N=17) as genotype breakdown counts are not reported.
- Microarray and RT-qPCR expression data are excluded as they do not measure target marker frequencies.

## Validator warnings

- genotype #3 (2012_Jones_dioulassoba_2009_2010_gamb_ss, kdr 1014F): frequency only (no raw counts)
- geno_pheno #1 (DDT, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #2 (DDT, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
