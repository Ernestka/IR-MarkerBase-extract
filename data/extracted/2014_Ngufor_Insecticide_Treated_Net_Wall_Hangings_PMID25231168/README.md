# Extraction record — 2014_Ngufor_Insecticide_Treated_Net_Wall_Hangings_PMID25231168

- Extracted: 2026-11-01
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 1 · Bioassays: 7 · Geno-pheno rows: 0

## Decisions

### Data Extraction Notes

1. **Surveys**:
   - `2014_Ngufor_Zeneti_2011_reared_gambiae`: Represents wild-reared *Anopheles gambiae* s.l. adult females emerging from larvae collected in Zeneti/Muheza, used for WHO susceptibility cylinder bioassays.
   - `2014_Ngufor_Zeneti_2011_wild_gambiae`: Represents wild-caught adult *Anopheles gambiae* s.l. females collected from the experimental huts, a subset (n=47) of which was genotyped for *kdr* (L1014S).

2. **Genotypes**:
   - Marker name written as `kdr (L1014S)` in paper text; extracted as gene `kdr`, marker `L1014S`.
   - Genotype breakdown (RR, RS, SS) was not printed; the paper reported an overall frequency of 0.22 in 47 genotyped mosquitoes. Genotype counts were left null as per extraction rules.

3. **Bioassays**:
   - WHO cylinder susceptibility tests were performed on 3–5 day old wild-reared female *An. gambiae* s.l. (95–100 exposed per test).
   - Mortalities for deltamethrin (74%), lambda-cyhalothrin (80%), and permethrin (50%) were read from Figure 1. Mortalities for pirimiphos-methyl (100%), fenitrothion (100%), propoxur (100%), and DDT (100%) were stated in text and Figure 1.
   - In situ WHO cone bioassays on netting materials were performed exclusively on laboratory reference strain (*An. gambiae* Kisumu) and were excluded as controls.

## Validator warnings

- genotype #1 (2014_Ngufor_Zeneti_2011_wild_gambiae, kdr L1014S): frequency only (no raw counts)
