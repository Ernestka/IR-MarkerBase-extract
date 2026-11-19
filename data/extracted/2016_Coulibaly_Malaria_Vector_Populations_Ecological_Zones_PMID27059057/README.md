# Extraction record — 2016_Coulibaly_Malaria_Vector_Populations_Ecological_Zones_PMID27059057

- Extracted: 2026-11-19
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 8 · Genotype rows: 5 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

# Decisions Summary

- **Study Design and Survey Division**: Mosquitoes were collected across four sites in Mali (Takan, Toumani Oulena) and Guinea Conakry (Koraboh, Koundara) in October–November 2012. Both *Anopheles gambiae* and *Anopheles coluzzii* were collected across all sites. Surveys were defined per site and molecular species (8 surveys total).
- **Bioassays**: No insecticide bioassays were conducted; `bioassays` and `geno_pheno` arrays are empty.
- **Target Markers**: 
  - `para` L1014F: Genotyped by PCR diagnostic assay and confirmed in 70 samples by Sanger sequencing. Genotype records are included ONLY for surveys that have explicitly printed allele frequencies or genotype counts in the text (Takan *A. gambiae*, Takan *A. coluzzii*, Koraboh *A. gambiae*, Koraboh *A. coluzzii*, and Koundara *A. gambiae*). Surveys that only appear as stacked bar charts without explicit printed numbers in text (Toumani Oulena *A. gambiae*, Toumani Oulena *A. coluzzii*, and Koundara *A. coluzzii*) were omitted from the `genotypes` array to avoid empty records with null counts and null reported frequencies.
  - `para` L1014S: Tested in a subset (15–18 samples/site) and not detected. Specific sample breakdowns per site/species were not given for this marker, so no separate records were created.
- **Inconsistency Note**: Page 6 notes that in Deep Forest *A. gambiae*, 1 mosquito was heterozygous out of 384 mosquitoes (or alleles), yielding a reported frequency of 0.997. Figure 4 gives $n=184$ for that bar. Both values are retained as printed.

## Validator warnings

- genotype #1 (2016_Coulibaly_Malaria_Vector_Populations_Ecological_Zones_PMID27059057_takan_gambiae, para L1014F): frequency only (no raw counts)
- genotype #2 (2016_Coulibaly_Malaria_Vector_Populations_Ecological_Zones_PMID27059057_takan_coluzzii, para L1014F): frequency only (no raw counts)
- genotype #3 (2016_Coulibaly_Malaria_Vector_Populations_Ecological_Zones_PMID27059057_koraboh_gambiae, para L1014F): frequency only (no raw counts)
- genotype #4 (2016_Coulibaly_Malaria_Vector_Populations_Ecological_Zones_PMID27059057_koraboh_coluzzii, para L1014F): frequency only (no raw counts)
- genotype #5 (2016_Coulibaly_Malaria_Vector_Populations_Ecological_Zones_PMID27059057_koundara_gambiae, para L1014F): inconsistent in the paper (values kept as printed) — Page 6 states: 'displayed kdr-w frequency of 0.997 in A. gambiae 6 years later in 2012 (of 384 mosquitoes, only one was heterozygous)', but Figure 4 reports A. gambiae (n=184) for Deep Forest.
