# Extraction record — 2011_Norris_Efficacy_Long_Lasting_Insecticidal_Nets_PMID21880143

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 4 · Bioassays: 4 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Samples**:
   - Two field target samples are reported for *An. arabiensis*:
     1) F1 progeny of wild-collected *An. arabiensis* collected in January 2010 in the Macha area (Chidakwa and Namwala, pooled, total n=170).
     2) Archived wild adult *An. arabiensis* from the field in Macha (total n=50).
   - Bioassays and net degradation tests conducted using the MIAM laboratory *An. arabiensis* colony or the Keele laboratory strain of *An. gambiae s.s.* were excluded as lab reference strain controls per Rule 5.

2. **Markers**:
   - Both `L1014F` and `L1014S` (`kdr`) were genotyped in 170 F1 mosquitoes and 50 archived field mosquitoes. All 220 field mosquitoes were homozygous wild-type (L1014/L1014).
   - As per multi-allelic site handling rules, L1014F and L1014S are recorded as separate rows with RR=0, RS=0, SS=N, allele frequency=0.0.

3. **Bioassays**:
   - Four bioassays on F1 field *An. arabiensis* were extracted:
     - Permethrin 60 ug/bottle CDC bottle bioassay (100% mortality at 24h).
     - Deltamethrin 20 ug/bottle CDC bottle bioassay (100% mortality at 24h).
     - DDT 100 ug/bottle CDC bottle bioassay (100% mortality at 3h/24h).
     - Deltamethrin (Permanet LLIN material) 5-minute ITN bioassay (n=33, 88% mortality at 24h).
   - Bioassay counts (`n_dead`/`n_alive`) were left null where not literally printed as counts.
