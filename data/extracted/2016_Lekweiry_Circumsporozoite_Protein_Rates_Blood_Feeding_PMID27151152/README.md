# Extraction record — 2016_Lekweiry_Circumsporozoite_Protein_Rates_Blood_Feeding_PMID27151152

- Extracted: 2026-11-20
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 8 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

# Extraction Decisions: Mint Lekweiry et al. (2016)

### Spatial and Survey Breakdown
- Five sites were investigated across two ecological zones in Mauritania:
  1. Nouakchott (Saharan zone): Teyarett, Dar Naim, and Sebkha districts.
  2. Hodh Elgharbi (Sahelian zone): Kobeni and Tintane districts.
- Sebkha district yielded 0 Anopheles specimens in both 2009 and 2010 (Table 1, Table 3), so no survey was created for Sebkha.
- Distinct surveys were established for the remaining four sites (Teyarett, Dar Naim, Kobeni, and Tintane).
- In Nouakchott, all Anopheles gambiae s.l. were molecularly identified as Anopheles arabiensis (186 molecularly tested, all An. arabiensis).
- In Hodh Elgharbi, An. gambiae s.l. specimens comprised both An. arabiensis and An. gambiae s.s. (Table 1). Table 3 reports kdr data under 'An. gambiae (s.l.)' for Kobeni (N=13) and Tintane (N=27). Although the text on page 5 ambiguously states 'analysis of the kdr polymorphisms in 40 female An. arabiensis showed... Nevertheless, West African kdr mutation (L1014F) was found only in An. gambiae populations (4/40, 10 %)', the data in Table 3 are pooled at the An. gambiae s.l. level without separating species by site. Hence, the surveys for Kobeni and Tintane are recorded as Anopheles gambiae (s.l.).

### Genotype Class Allocation
- **Nouakchott (Teyarett and Dar Naim)**: The text on page 5 explicitly states that in Nouakchott, 51.7% (75/145) presented the wild-type allele (L1014) and 48.3% (70/145) harboured the East African kdr mutation (L1014S) 'at the homozygous status'. No L1014F mutations were detected (0/145). Therefore, all 29 mutant individuals in Teyarett and all 41 in Dar Naim were homozygous RR for L1014S, with 0 heterozygotes (RS = 0). Wild-type counts (27 in Teyarett, 48 in Dar Naim) represent homozygous SS (L/L). Per Rule 4b, SS for L1014F equals n_genotyped.
- **Hodh Elgharbi (Kobeni and Tintane)**: Table 3 lists 11 wild-type, 1 Kdr-w, and 1 Kdr-e for Kobeni (total 13), and 21 wild-type, 3 Kdr-w, and 3 Kdr-e for Tintane (total 27). The text does not explicitly specify whether these mutant individuals were homozygous or heterozygous. To avoid assumptions, mutant counts are captured under `n_carriers` per Rule 2b.
- **Ace-1 G119S**: The authors screened for the ace-1 G119S mutation using PCR-RFLP and reported its complete absence ('No ace-1 mutation was observed in mosquito specimens from the two study zones'). However, the exact number of individuals tested for ace-1 per site is not reported, so ace-1 records were not extracted.

### Bioassays and Genotype-Phenotype Links
- No WHO tube or CDC bottle insecticide bioassays were performed in this study (mosquitoes were sampled via indoor pyrethrum spray catch for vector bionomics, sporozoite detection, and resistance marker screening). Therefore, `bioassays` and `geno_pheno` are empty.
