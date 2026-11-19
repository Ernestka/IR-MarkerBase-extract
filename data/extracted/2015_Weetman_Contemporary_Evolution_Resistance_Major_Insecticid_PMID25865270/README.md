# Extraction record — 2015_Weetman_Contemporary_Evolution_Resistance_Major_Insecticid_PMID25865270

- Extracted: 2026-11-19
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 2 · Bioassays: 0 · Geno-pheno rows: 6

## Decisions

# Decisions and Extraction Notes

### Surveys and Collections
- Samples were collected from suburbs of Accra, Ghana (Dzorwulu, Madina, Labadi, Roman Ridge; 5.55°N, 0.20°W) as larvae, reared to adults, and identified to molecular species (Anopheles gambiae and Anopheles coluzzii) using PCR-RFLP of IGS rDNA and SINE-PCR insertion polymorphism.
- In 2008, collections were made in May from multiple Accra suburbs. Both an unexposed population sample ('Pop freq') and bioassay survivors ('Alive') were genotyped (Table 1A).
- In 2010, collections were made in May from Madina (Accra). Both bioassay survivors ('Alive') and dead mosquitoes were genotyped (Table 1B).
- Archived specimens from 2002, 2007, and 2011 were mentioned in the text and used for temporal regression (Figure 2) and CNV testing (Figure 5B), but complete genotype counts for population samples were not reported in the text or tables.

### Genotypes vs. Genotype-Phenotype
- **2008 unexposed controls ('Pop freq')** represent the unselected baseline population sample and are extracted into `genotypes` (N = 73 for An. gambiae, N = 119 for An. coluzzii).
- **2008 bioassay survivors ('Alive')** are phenotype-selected individuals following bendiocarb exposure (dead mosquitoes were not preserved/genotyped in 2008); they are extracted into `geno_pheno` with `phenotype_group = 'alive'`.
- **2010 samples (Table 1B)** were genotyped after bendiocarb exposure separately for surviving ('Alive') and dead individuals; all four classes (gambiae alive/dead, coluzzii alive/dead) are extracted into `geno_pheno`. Per extraction rules, these mosquitoes are not double-counted into `genotypes`.

### Bioassays
- In 2008, 561 females were exposed to bendiocarb as An. gambiae s.l. (mixed species). The paper reports only modeled/estimated mortalities for A. gambiae and A. coluzzii (0.39 and 0.99) based on subset species diagnostic proportions, not raw counts. Per Rule 8b, bioassays cannot be constructed from genotyped subsets or estimated proportions.
- In 2010, the total number of exposed mosquitoes is not stated (only the genotyped dead and alive in Table 1B). Per Rule 8b, no bioassay record was derived from genotyped counts; in `geno_pheno`, `bioassay_id` is set to null and `insecticide` is set to 'bendiocarb'.

### Ace-1 Duplication (CNV)
- Ace-1 copy number variation was investigated by qPCR on a non-random preselected subset of 119S/S and 119G/G homozygotes (2008) and on archived samples selected for presence of resistant alleles (2002). No population-level sample was screened to report unbiased carrier or genotype counts, so Ace-1 DUP was not extracted as a discrete marker frequency record.

## Validator warnings

- geno_pheno #1 (bendiocarb, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: bendiocarb)
- geno_pheno #2 (bendiocarb, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: bendiocarb)
- geno_pheno #3 (bendiocarb, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: bendiocarb)
- geno_pheno #4 (bendiocarb, Ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: bendiocarb)
- geno_pheno #5 (bendiocarb, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: bendiocarb)
- geno_pheno #6 (bendiocarb, Ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: bendiocarb)
