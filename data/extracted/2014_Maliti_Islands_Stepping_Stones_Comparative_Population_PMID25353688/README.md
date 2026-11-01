# Extraction record — 2014_Maliti_Islands_Stepping_Stones_Comparative_Population_PMID25353688

- Extracted: 2026-11-01
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 20 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions
- **Target Markers**: Paper reports genotyping for Vgsc 1014F (`L1014F` / `Vgsc L995F`) and Vgsc 1014S (`L1014S` / `Vgsc L995S`) using TaqMan qPCR.
- **Species and Surveys**:
  - Defined eight wild *An. gambiae s.s.* surveys corresponding to the sampling locations with microsatellite/kdr data (Unguja, Ilala, Kinondoni, Temeke, Bagamoyo, Kwadoli, Kilombero, Njage).
  - Defined one pooled survey for wild *An. arabiensis* across Tanzania (N=693 genotyped for kdr, with 1 RS detected in Dar es Salaam).
  - Defined one survey for the two *An. gambiae s.s.* x *An. arabiensis* hybrids found in Dar es Salaam collections.
  - Insectary colony samples (IHI out-groups) were excluded per Rule 5.
- **Genotype Counts vs Frequencies**:
  - Page 3 specifies that 20 individuals were randomly selected from each collection site for kdr qPCR genotyping.
  - For *An. gambiae s.s.*, kdr 1014F was completely absent across all sites (rr=0, rs=0, allele freq=0.0).
  - Kdr 1014S was absent from Kwadoli, Kilombero, and Njage (rr=0, rs=0, allele freq=0.0). In Unguja, allele frequency was reported as 16% with only heterozygotes present (rr=0). For Dar es Salaam sites (Ilala, Kinondoni, Temeke) and Bagamoyo, allele frequency was reported to exceed 70% with ~50% homozygotes.
  - For *An. arabiensis*, total N=693 genotyped across all wild sites; 1 RS was detected for 1014S (rr=0, rs=1, ss=692), while 1014F was completely absent (rr=0, rs=0, ss=693).
- **Bioassays & Geno-Pheno**: No bioassays or phenotype-split genotype data were performed/reported in this paper.

## Validator warnings

- genotype #3 (2014_Maliti_Ilala_2008_gambiae, kdr 1014S): frequency only (no raw counts)
- genotype #5 (2014_Maliti_Kinondoni_2008_gambiae, kdr 1014S): frequency only (no raw counts)
- genotype #7 (2014_Maliti_Temeke_2008_gambiae, kdr 1014S): frequency only (no raw counts)
- genotype #9 (2014_Maliti_Bagamoyo_2008_gambiae, kdr 1014S): frequency only (no raw counts)
