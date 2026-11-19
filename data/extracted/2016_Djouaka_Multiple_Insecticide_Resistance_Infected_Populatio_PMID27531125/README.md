# Extraction record — 2016_Djouaka_Multiple_Insecticide_Resistance_Infected_Populatio_PMID27531125

- Extracted: 2026-11-19
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 2 · Bioassays: 18 · Geno-pheno rows: 2

## Decisions

### Data Extraction Notes

1. **Surveys**:
   - Two surveys were created for the location of Kpome (6°23′N, 2°13′E), southern Benin:
     - `kpome_funestus_f0`: Wild F0 adult females collected indoors between December 2013 and February 2014, used for species identification and genotyping of population resistance markers.
     - `kpome_funestus_f1`: F1 progeny reared from the F0 females, used for WHO bioassays and genotype-phenotype association assays.
   - Anopheles coluzzii samples collected in Kpome were analyzed only for Plasmodium infectivity in Table 1; no target insecticide resistance markers or bioassays were reported for An. coluzzii, so no survey/genotype records were created for An. coluzzii.

2. **Genotypes (Population level)**:
   - Target markers genotyped in 92 wild F0 female An. funestus s.s.:
     - `GSTe2 L119F`: 84 RR, 8 RS, 0 SS out of 92 genotyped.
     - `Rdl A296S`: 0 RR, 1 RS, 91 SS out of 92 genotyped.

3. **Bioassays**:
   - Standard WHO tube bioassays and synergist (PBO) assays were conducted on F1 adults.
   - Percentages were recorded as printed. Exact numbers of exposed mosquitoes per standard bioassay tube were not printed individually (total 713 exposed across all standard assays), so `n_exposed`, `n_dead`, and `n_alive` were left null and `reported_mortality_pct` recorded.
   - For synergist assays, text states 50 females and 50 males were exposed per test (`n_exposed` = 50).

4. **Genotype-Phenotype Associations**:
   - 25 DDT-alive (resistant) and 25 DDT-dead (susceptible) F1 females were genotyped for `GSTe2 L119F`.
   - As stated on page 7, dead mosquitoes were obtained by conducting several additional DDT bioassays, so these mosquitoes were pooled across bioassays; `bioassay_id` is set to null and `insecticide` set to 'DDT'.
   - Genotype breakdown from Figure 4:
     - Alive (DDT-resistant): 23 RR, 0 RS, 2 SS (N=25).
     - Dead (DDT-susceptible): 20 RR, 3 RS, 2 SS (N=25).

## Validator warnings

- geno_pheno #1 (DDT, GSTe2 L119F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #1 (DDT, GSTe2 L119F, alive): inconsistent in the paper (values kept as printed) — Text on page 7 states '23 RR/RS out of 25 alive mosquitoes screened', but 23/25 = 92% corresponds to the RR count in Figure 4 where RR=23, RS=0, SS=2.
- geno_pheno #2 (DDT, GSTe2 L119F, dead): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #2 (DDT, GSTe2 L119F, dead): inconsistent in the paper (values kept as printed) — Text on page 7 states '20 RR/RS out of 25 dead mosquitoes screened', but 20/25 = 80% corresponds to the RR count in Figure 4 where RR=20, RS=3, SS=2.
