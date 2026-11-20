# Extraction record — 2016_Lekweiry_Circumsporozoite_Protein_Rates_Blood_Feeding_PMID27151152

- Extracted: 2026-11-20
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 12 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

- **Surveys**: Split by sampling site (Teyarett, Dar Naim, Kobeni, Tintane). Coordinates for all four sites were explicitly reported in the text (Page 2).
- **Species Breakdown**: In Nouakchott (Teyarett and Dar Naim), 100% of tested specimens were confirmed as *An. arabiensis* by PCR. In Hodh Elgharbi (Kobeni and Tintane), species composition included both *An. arabiensis* and *An. gambiae s.s.* (Table 1), but Table 3 reports kdr genotypes aggregated under *An. gambiae (s.l.)* (with text mentioning *An. arabiensis* and *An. gambiae*).
- **Target Markers**: 
  - `kdr` / `L1014S` (Vgsc L995S / East African kdr)
  - `kdr` / `L1014F` (Vgsc L995F / West African kdr)
  - `ace-1` / `G119S` (Ace-1 G280S)
- **Genotype Counts**: 
  - In Nouakchott (Teyarett and Dar Naim), page 5 text specifies that all L1014S mutants were homozygous. Thus, RR and SS counts are extracted directly (RR=29, RS=0, SS=27 for Teyarett; RR=41, RS=0, SS=48 for Dar Naim).
  - In Hodh Elgharbi (Kobeni and Tintane), Table 3 reports counts for wild-type L1014, Kdr-w L1014F, and Kdr-e L1014S. Since individual zygosity (homozygote vs heterozygote) is not separately detailed for Hodh Elgharbi in Table 3, mutation counts are assigned to `n_carriers`.
  - `ace-1 G119S`: The text explicitly notes that no ace-1 mutations were observed across both study zones; thus RR=0, RS=0, SS=N.
- **Bioassays & Geno-Pheno**: No WHO/CDC bioassays were performed; mosquitoes were collected via pyrethrum spray catch (PSC) for vector surveillance.
