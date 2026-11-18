# Extraction record — 2016_Coulibaly_Malaria_Vector_Populations_Ecological_Zones_PMID27059057

- Extracted: 2026-11-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 4 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

# Extraction Decisions - Coulibaly et al. (2016)

### 1. Scope & Target Markers
- Target marker extracted: Vgsc L1014F (reported as `para` `L1014F` / `kdr-w`).
- Vgsc L1014S (kdr-e) was tested in a subset of samples (text states 'not detected in 15–18 samples per site'), but because site-specific exact sample sizes and species breakdowns are not stated, it was not extractable into distinct survey records.
- The 2La chromosomal inversion was genotyped in this study, but is not one of the target resistance markers.
- No bioassays or genotype-phenotype association assays were performed in this study.

### 2. Surveys & Site Breakdown
- Four ecological sites were sampled across Mali and Guinea in October–November 2012: Takan (arid savannah, Mali), Toumani Oulena (humid savannah, Mali), Koraboh (semi-forest, Guinea), and Koundara (deep forest, Guinea).
- At each site, mosquitoes were collected using a combination of indoor pyrethroid spray catches, human-landing catches (indoor and outdoor), and larval collections (both larvae directly preserved and larvae reared to adults).
- In Figure 4, kdr-w genotype frequencies are reported per site and per species (An. gambiae and An. coluzzii).
- Data for Koraboh and Koundara are extractable because:
  - Semi-forest (Koraboh): Text explicitly states that kdr-w is fixed in all samples assayed (Fig. 4 gives An. gambiae n=211, An. coluzzii n=2; hence 100% RR).
  - Deep forest (Koundara): For An. gambiae, the text states frequency was 0.997 with only one heterozygous mosquito ('of 384 mosquitoes, only one was heterozygous', where 384 is a typo for 184 as shown by n=184 in Fig. 4 and (183*2+1)/(184*2) = 0.99728). For An. coluzzii (n=11), the bar in Fig. 4 is 100% kdr/kdr.
- For Takan (Arid Savanna: An. gambiae n=25, An. coluzzii n=175) and Toumani Oulena (Humid Savanna: An. gambiae n=170, An. coluzzii n=22), genotype classes segregate, but only a stacked bar chart without printed counts or site-specific numeric tables is provided in the main text. Per Rule 8, these populations were dropped from `genotypes` rather than guessing counts from figure bars, and orphan survey entries for them were not created.

## Validator warnings

- genotype #3 (2016_Coulibaly_Malaria_Vector_Populations_Ecological_Zones_PMID27059057_koundara_gam, para L1014F): inconsistent in the paper (values kept as printed) — Text on page 6 states that A. gambiae in deep forest displayed 'kdr-w frequency of 0.997 in A. gambiae 6 years later in 2012 (of 384 mosquitoes, only one was heterozygous)', but Fig. 4 gives n=184 for Deep Forest A. gambiae. With 183 RR and 1 RS out of 184, the resistant allele frequency is (183*2 + 1)/(184*2) = 367/368 = 0.99728, exactly matching the printed 0.997, indicating 384 in the text was a typographical error for 184.
