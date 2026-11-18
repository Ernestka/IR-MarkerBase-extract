# Extraction record — 2015_Weetman_Contemporary_Evolution_Resistance_Major_Insecticid_PMID25865270

- Extracted: 2026-11-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 2 · Bioassays: 2 · Geno-pheno rows: 6

## Decisions

### Survey and Genotype Splitting
- Samples from Accra collected in May 2008 and May 2010 were separated into distinct surveys by year and molecular species (Anopheles gambiae s.s. and Anopheles coluzzii).
- Coordinates for Accra suburbs (Dzorwulu, Madina, Labadi, Roman Ridge) were reported on page 3 as 5.55°N, 0.20°W.
- Table 1A gives genotype counts for unexposed population controls ('Pop freq') and bioassay survivors ('Alive') from 2008. The unexposed controls were placed into `genotypes`, while the survivors were placed into `geno_pheno`.
- For 2008 bioassays, only estimated mortalities across a subset diagnosed to species were reported (0.39 for gambiae, 0.99 for coluzzii out of 561 exposed s.l.), without printed raw dead/alive/exposed counts per species. Therefore, no 2008 bioassays were extracted, and the 2008 survivors in `geno_pheno` have `bioassay_id: null` with `insecticide: 'bendiocarb'`.
- Table 1B gives genotype counts for both survivors ('Alive') and non-survivors ('Dead') from the 2010 collections in Madina. These were extracted as WHO tube bioassays with 0.1% bendiocarb and linked to the corresponding `geno_pheno` records.

### Additional Data / Excluded Data
- Archived samples from 2002, 2007, and 2011 were mentioned in the text and plotted in Figure 2 / Figure 5, but raw counts (RR/RS/SS or sample N) were not reported in the text or tables and were therefore not extracted.
- Ace-1 copy number variation (CNV) was evaluated using qPCR on pre-selected subsets of homozygous/heterozygous specimens rather than unselected population samples, so Ace-1 DUP was not extracted as a population frequency.

## Validator warnings

- geno_pheno #1 (bendiocarb, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: bendiocarb)
- geno_pheno #2 (bendiocarb, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: bendiocarb)
