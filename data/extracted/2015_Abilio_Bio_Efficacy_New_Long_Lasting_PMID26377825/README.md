# Extraction record — 2015_Abilio_Bio_Efficacy_New_Long_Lasting_PMID26377825

- Extracted: 2026-11-17
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 5 · Genotype rows: 2 · Bioassays: 28 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Sites**:
   - Mosquitoes were collected as larvae between June and August 2012 across three districts in Mozambique: Balama (Cabo Delgado Province), Mocuba (Zambézia Province), and Milange (Zambézia Province).
   - PCR identified 415/415 An. funestus group mosquitoes as *An. funestus s.s.* and 256/256 An. gambiae s.l. mosquitoes as *An. gambiae s.s.* (S form).
   - Surveys are split by district and species: `2015_Abilio_balama_funestus`, `2015_Abilio_mocuba_gambiae`, `2015_Abilio_mocuba_funestus`, and `2015_Abilio_milange_gambiae`.
   - An additional province-level survey (`2015_Abilio_zambezia_gambiae`) was created to represent the combined sample of 256 *An. gambiae s.s.* from Zambézia Province (100 from Mocuba susceptibility tests + 156 from Milange cone bioassays) screened for kdr mutations.

2. **Genotypes**:
   - Screening for target-site kdr mutations (West/L995F and East/L995S) was conducted on 256 *An. gambiae s.s.* specimens. Zero mutant alleles were detected (all 256 were homozygous wild-type SS).
   - A minor inconsistency note was added because text on page 6 refers to '250 specimens', whereas pages 1, 6, and 10 state 256 specimens (100 from susceptibility tests + 156 from cone bioassays = 256).
   - *An. funestus* specimens were not tested for kdr (as noted in paper, kdr is not reported in *An. funestus*).

3. **Bioassays**:
   - Extracted both WHO cylinder susceptibility tests (Tables 1 & 2) and LLIN WHO cone bioassays (Tables 3 & 4).
   - Cylinder tests evaluated deltamethrin (0.05%), permethrin (0.75%), bendiocarb (0.1%), propoxur (0.1%), and DDT (4%).
   - LLIN cone tests (3 min exposure) evaluated Olyset (permethrin 20 g/kg), Permanet 2.0 (deltamethrin 55 mg/m2), NetProtect (deltamethrin 1.8 g/kg), Interceptor (alpha-cypermethrin 200 mg/m2), and Permanet 3.0 sections (lower border, upper side, and PBO-containing roof).
   - Laboratory reference strain (insectary-susceptible *A. arabiensis* Durban strain) bioassays were excluded as controls per rules.

## Validator warnings

- genotype #1 (2015_Abilio_zambezia_gambiae, kdr kdr-west): inconsistent in the paper (values kept as printed) — Page 6 text mentions '250 specimens of A. gambiae tested', whereas pages 1, 6, 10 and sample totals (100 + 156) state 256 tested.
- genotype #2 (2015_Abilio_zambezia_gambiae, kdr kdr-east): inconsistent in the paper (values kept as printed) — Page 6 text mentions '250 specimens of A. gambiae tested', whereas pages 1, 6, 10 and sample totals (100 + 156) state 256 tested.
