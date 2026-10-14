# Extraction record — 1_s2_0_S0001706X21004691_main

- Extracted: 2026-10-14
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 3 · Bioassays: 9 · Geno-pheno rows: 0

## Decisions

### Survey and Sampling
- Surveys were created for each of the three Local Government Areas (LGAs) in Lagos State, Nigeria: Kosofe (Ajegunle), Ojo (Iyana-Iba), and Lagos Mainland (Oko-Baba).
- Coordinates reported in Section 2.1 ('longitude 3° 24′ E and latitude 6° 27′ N', decimal: 6.45 N, 3.40 E) represent the general coordinates given for the Lagos study area and are assigned across the three LGA surveys.
- Larvae were sampled between May and September 2019 and reared to adults in the insectary.
- Molecular identification with PCR-RFLP confirmed that all successfully amplified specimens (179/241; the remaining did not amplify) were *Anopheles coluzzii*.

### Genotype Data
- Only target marker *kdr-west* (*Vgsc* L1014F / L995F) was assayed via AS-PCR.
- Exact genotype counts (RR, Rr, rr) and total examined are reported in Table 2 for Kosofe (N=69: RR=8, RS=0, SS=61), Ojo (N=68: RR=4, RS=1, SS=63), and Lagos Mainland (N=104: RR=17, RS=0, SS=87).

### Bioassays
- Standard WHO susceptibility tube assays (4 batches of 25 = 100 mosquitoes exposed per test) for 4% DDT and 0.75% permethrin were extracted from Table 1.
- PBO synergist assays (pre-exposure to PBO followed by 0.75% permethrin) were extracted from Fig 2 and Section 3.1; exact sample sizes were not reported for the synergist cohorts, so `n_exposed`, `n_dead`, and `n_alive` were left as null.
- Genotypes were reported only for the overall random samples per site and not disaggregated by bioassay survivors/dead, hence `geno_pheno` is empty.
