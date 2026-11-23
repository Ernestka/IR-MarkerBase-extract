# Extraction record — 2018_Okia_Insecticide_Resistance_Status_Malaria_Mosquitoes_PMID29625585

- Extracted: 2026-11-23
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 16 · Genotype rows: 16 · Bioassays: 36 · Geno-pheno rows: 0

## Decisions

### Data Extraction Notes

1. **Surveys & Species Breakdown**:
   - Surveys were split by district (Apac, Lira, Soroti, Tororo), collection method (indoor resting adult vs larval collection), and species level.
   - Genotype data from Table 6 are reported for PCR-identified *An. gambiae s.s.* and *An. arabiensis*. Separate survey records were created for each molecular species at each location.
   - Bioassay data from Tables 1, 2, 4, and 5 are reported at the level of *Anopheles gambiae s.l.* or *Anopheles funestus*, split by collection type (adult vs larval-reared adults).

2. **Genotypes & Target Markers**:
   - Table 6 presents genotype counts and allelic frequencies for *kdr-East* (L1014S / Vgsc L995S) and *kdr-West* (L1014F / Vgsc L995F).
   - Printed values in Table 6 were extracted verbatim without modification:
     - For Apac *An. arabiensis* (WEST), Table 6 prints `No. 1, RR 1, RS 0, SS 1`, resulting in `RR+RS+SS = 2` (contradicting `N = 1`), while text indicates 1 mosquito was homozygous for L1014F out of 43 tested.
     - For Lira *An. arabiensis* (EAST), Table 6 prints `RS=1`, but `R=0` and `S=1.00`, which contradicts the text statement that no L1014S mutation was detected in *An. arabiensis*.
     - For Soroti and Tororo *An. arabiensis* (EAST), Table 6 prints `RS=30` and `RS=68` under the `RS` column while printing `R=0` and `S=1.00`, likely misaligning wild-type counts into the `RS` header. Mismatches are documented in `inconsistency_note`.

3. **Bioassays & Synergists**:
   - Diagnostic CDC bottle bioassays, PBO synergist tests (Table 4), and intensity bioassays (1x, 2x, 5x, 10x in Table 5 & text) were extracted as distinct bioassay entries.
   - Duplicate reporting of Tororo permethrin control (Table 2 vs Table 4) was extracted once.
   - No genotype-phenotype breakdown (alive vs dead) was reported in the text or tables.

## Validator warnings

- genotype #10 (2018_Okia_apac_2015_arab, kdr L1014F): inconsistent in the paper (values kept as printed) — Table 6 prints No.=1, RR=1, RS=0, SS=1 for WEST in Apac An. arabiensis, so RR+RS+SS = 2 does not equal N = 1; text indicates 1 mosquito was homozygous for L1014F out of 43 tested.
- genotype #10 (2018_Okia_apac_2015_arab, kdr L1014F): RR+RS+SS = 1+0+1 = 2 but n_genotyped = 1
- genotype #10 (2018_Okia_apac_2015_arab, kdr L1014F): computed allele freq 0.500 differs from reported 1.0
- genotype #11 (2018_Okia_lira_2015_arab, kdr L1014S): inconsistent in the paper (values kept as printed) — Table 6 prints No.=1, RS=1, R=0, S=1.00 for EAST in Lira An. arabiensis; RS=1 contradicts printed R=0 and text stating no L1014S was detected in An. arabiensis.
- genotype #11 (2018_Okia_lira_2015_arab, kdr L1014S): computed allele freq 0.500 differs from reported 0.0
- genotype #13 (2018_Okia_soroti_2015_arab, kdr L1014S): inconsistent in the paper (values kept as printed) — Table 6 prints RS=30 and SS=0 for EAST in Soroti An. arabiensis, which contradicts printed R=0 and S=1.00; text states all An. arabiensis except 1 were homozygous wild-type.
- genotype #13 (2018_Okia_soroti_2015_arab, kdr L1014S): computed allele freq 0.500 differs from reported 0.0
- genotype #15 (2018_Okia_tororo_2015_arab, kdr L1014S): inconsistent in the paper (values kept as printed) — Table 6 prints RS=68 and SS=0 for EAST in Tororo An. arabiensis, which contradicts printed R=0 and S=1.00; text states all An. arabiensis except 1 were homozygous wild-type.
- genotype #15 (2018_Okia_tororo_2015_arab, kdr L1014S): computed allele freq 0.500 differs from reported 0.0
