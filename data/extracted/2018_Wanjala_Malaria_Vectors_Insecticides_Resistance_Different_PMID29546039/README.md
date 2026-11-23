# Extraction record — 2018_Wanjala_Malaria_Vectors_Insecticides_Resistance_Different_PMID29546039

- Extracted: 2026-11-23
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 20 · Genotype rows: 13 · Bioassays: 16 · Geno-pheno rows: 0

## Decisions

### Survey & Genotype Mapping Decisions
1. **Surveys**: Created separate survey records for each study site and molecular species (*An. gambiae s.s.* and *An. arabiensis*) for genotype extraction, as well as an *An. gambiae s.l.* survey per site for bioassays conducted on pooled wild-reared mosquitoes.
2. **Target Marker**: `Vgsc L1014S` (L995S) genotyped via Real-time PCR.
3. **Genotype Class Mapping (Table 2)**:
   - LL = wild-type homozygote (mapped to `ss`)
   - LS = heterozygote (mapped to `rs`)
   - SS = mutant homozygote (mapped to `rr`)
4. **Inconsistency Notes**: The paper printed 'Frequency (%)' in Table 2 calculated as the SS genotype proportion (`SS / N * 100`) rather than allele frequency (`(2*SS + LS) / (2*N)`) for most *An. gambiae s.s.* populations. These mismatches are flagged in `inconsistency_note` for each affected row without changing any printed value.
5. **Bioassays**: Extracted bioassay records for tests where exact mortality percentages were stated in the paper text (Bendiocarb across all 7 sites, Malathion across all 7 sites, DDT in Ahero, and Lambdacyhalothrin in Ahero). Other bioassay results shown only as bar charts in Figure 2 were omitted as exact counts or percentages were not printed in tables or text.
6. **Geno-Pheno**: No genotype-phenotype breakdown (separate genotype counts for survivors and dead) was presented in the text or tables.

## Validator warnings

- genotype #2 (2018_Wanjala_kisian_gambiae, Vgsc L1014S): inconsistent in the paper (values kept as printed) — Printed allele frequency is 30.0%, but calculated from genotype counts (RR=15, RS=3, SS=32, N=50) is 33.0%.
- genotype #2 (2018_Wanjala_kisian_gambiae, Vgsc L1014S): computed allele freq 0.330 differs from reported 0.3
- genotype #3 (2018_Wanjala_chulaimbo_gambiae, Vgsc L1014S): inconsistent in the paper (values kept as printed) — Printed allele frequency is 0.893 (89.3%), which matches the SS genotype frequency (50/56) rather than true allele frequency (104/112 = 0.929).
- genotype #3 (2018_Wanjala_chulaimbo_gambiae, Vgsc L1014S): computed allele freq 0.929 differs from reported 0.893
- genotype #4 (2018_Wanjala_emutete_gambiae, Vgsc L1014S): inconsistent in the paper (values kept as printed) — Printed allele frequency is 0.873 (87.3%), which matches the SS genotype frequency (76/87) rather than true allele frequency (156/174 = 0.897).
- genotype #4 (2018_Wanjala_emutete_gambiae, Vgsc L1014S): computed allele freq 0.897 differs from reported 0.873
- genotype #5 (2018_Wanjala_emakakha_gambiae, Vgsc L1014S): inconsistent in the paper (values kept as printed) — Printed allele frequency is 0.859 (85.9%), which matches the SS genotype frequency (49/57) rather than true allele frequency (105/114 = 0.921).
- genotype #5 (2018_Wanjala_emakakha_gambiae, Vgsc L1014S): computed allele freq 0.921 differs from reported 0.859
- genotype #6 (2018_Wanjala_iguhu_gambiae, Vgsc L1014S): inconsistent in the paper (values kept as printed) — Printed allele frequency is 0.843 (84.3%), which matches the SS genotype frequency (91/108) rather than true allele frequency (189/216 = 0.875).
- genotype #6 (2018_Wanjala_iguhu_gambiae, Vgsc L1014S): computed allele freq 0.875 differs from reported 0.843
- genotype #7 (2018_Wanjala_kabula_gambiae, Vgsc L1014S): inconsistent in the paper (values kept as printed) — Printed allele frequency is 0.811 (81.1%), which matches the SS genotype frequency (43/53) rather than true allele frequency (91/106 = 0.858).
- genotype #7 (2018_Wanjala_kabula_gambiae, Vgsc L1014S): computed allele freq 0.858 differs from reported 0.811
- genotype #8 (2018_Wanjala_ahero_arabiensis, Vgsc L1014S): inconsistent in the paper (values kept as printed) — Printed allele frequency is 0.0%, but 4 LS heterozygotes are reported (calculated allele frequency = 4/100 = 0.04).
- genotype #8 (2018_Wanjala_ahero_arabiensis, Vgsc L1014S): computed allele freq 0.040 differs from reported 0.0
- genotype #9 (2018_Wanjala_kisian_arabiensis, Vgsc L1014S): inconsistent in the paper (values kept as printed) — Printed allele frequency is 0.0%, but 1 LS heterozygote is reported (calculated allele frequency = 1/84 = 0.012).
