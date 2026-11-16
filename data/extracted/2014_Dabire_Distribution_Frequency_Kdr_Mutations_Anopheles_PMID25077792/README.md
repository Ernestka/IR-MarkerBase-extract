# Extraction record — 2014_Dabire_Distribution_Frequency_Kdr_Mutations_Anopheles_PMID25077792

- Extracted: 2026-11-16
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 43 · Genotype rows: 25 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions
- **Surveys**: Created 43 survey entries corresponding to each site and molecular species combination with N > 0 in Burkina Faso ( Gaoua, Banfora, Sindou, Orodara, Dioulassoba, Soumousso, Boromo, Dédougou, Koudougou, Nanoro, Koupela, Fada, Kaya, Ouahigouya, Dori ). Banfora An. arabiensis and Boromo An. coluzzii were excluded because zero specimens were collected/genotyped (N=0).
- **Multi-allelic Vgsc Codon 1014**: Followed Rule 4b by treating Vgsc L1014F and Vgsc L1014S as separate genotype rows. RR = homozygotes for that allele, RS = heterozygotes for that allele, SS = derived by subtracting RR + RS from n_genotyped (which correctly includes non-carriers and carriers of the alternative mutation).
- **Coordinates**: Table 1 prints `10°40'N; 3°15'W` for all 15 sites across Burkina Faso (an obvious template copy-paste typo in the published paper). Exactly converted to decimal degrees (10.6667, -3.25) and cited as printed.
- **Inconsistencies**: Documented instances in `inconsistency_note` where printed frequencies deviated from counts (e.g. Gaoua An. arabiensis printed allele frequency 0.66 vs 0.20 calculated; Dédougou An. coluzzii Ace-1 printed frequency 0.5 vs 2 RR out of N=2).

## Validator warnings

- genotype #1 (2014_Dabire_Gaoua_gambiae, kdr L1014F): computed allele freq 0.284 differs from reported 0.53
- genotype #2 (2014_Dabire_Gaoua_gambiae, kdr L1014S): computed allele freq 0.236 differs from reported 0.92
- genotype #7 (2014_Dabire_Gaoua_arabiensis, kdr L1014F): inconsistent in the paper (values kept as printed) — Printed freq 0.66 equals 4/6 (for N=3), but N=5 is printed.
- genotype #7 (2014_Dabire_Gaoua_arabiensis, kdr L1014F): computed allele freq 0.400 differs from reported 0.66
- genotype #8 (2014_Dabire_Gaoua_arabiensis, kdr L1014S): inconsistent in the paper (values kept as printed) — Printed freq 0.66 contradicts 2 L/S out of N=5 (0.20).
- genotype #8 (2014_Dabire_Gaoua_arabiensis, kdr L1014S): computed allele freq 0.200 differs from reported 0.66
- genotype #10 (2014_Dabire_Banfora_gambiae, kdr L1014F): computed allele freq 0.466 differs from reported 0.56
- genotype #11 (2014_Dabire_Banfora_gambiae, kdr L1014S): computed allele freq 0.034 differs from reported 0.14
- genotype #13 (2014_Dabire_Banfora_coluzzii, kdr L1014F): computed allele freq 0.786 differs from reported 0.91
- genotype #14 (2014_Dabire_Banfora_coluzzii, kdr L1014S): computed allele freq 0.071 differs from reported 0.16
- genotype #16 (2014_Dabire_Sindou_gambiae, kdr L1014F): computed allele freq 0.315 differs from reported 0.6
- genotype #17 (2014_Dabire_Sindou_gambiae, kdr L1014S): computed allele freq 0.185 differs from reported 0.81
- genotype #19 (2014_Dabire_Sindou_coluzzii, kdr L1014F): computed allele freq 0.375 differs from reported 0.75
- genotype #20 (2014_Dabire_Sindou_coluzzii, kdr L1014S): computed allele freq 0.208 differs from reported 0.91
- genotype #25 (2014_Dabire_Dedougou_coluzzii, ace-1 G119S): inconsistent in the paper (values kept as printed) — Printed freq 0.5 contradicts 2 RR out of N=2 (1.0).
- genotype #25 (2014_Dabire_Dedougou_coluzzii, ace-1 G119S): computed allele freq 1.000 differs from reported 0.5
