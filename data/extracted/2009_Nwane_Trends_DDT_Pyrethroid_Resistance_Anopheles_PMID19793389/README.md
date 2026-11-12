# Extraction record — 2009_Nwane_Trends_DDT_Pyrethroid_Resistance_Anopheles_PMID19793389

- Extracted: 2026-11-11
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 19 · Genotype rows: 32 · Bioassays: 27 · Geno-pheno rows: 18

## Decisions

### Extraction Decisions

1. **Surveys & Molecular Forms**:
   - Mosquitoes were collected as larvae across four sites in Southern Cameroon (Ipono, Nkolondom, Mangoum, Bonanloka) in 2001, 2003, 2005, and 2007.
   - Mosquitoes were identified to molecular forms (M-form = *An. coluzzii*, S-form = *An. gambiae s.s.*). Separate survey records were created for each site x year x molecular species combination when present.
   - For Mangoum, only the S-form was detected in all years (100%). For Bonanloka in 2001, only the M-form was detected (100%).

2. **Markers & Multi-allelic Codon 1014 Handling**:
   - Both `L1014F` (kdr-west) and `L1014S` (kdr-east) mutations in the `Vgsc` gene were genotyped.
   - Following Rule 4b for tri-allelic codon 1014 (alleles Leu [L], Phe [F], Ser [S]):
     - For `L1014F`: RR = Phe-Phe, RS = Leu-Phe + Phe-Ser, SS = N - RR - RS.
     - For `L1014S`: RR = Ser-Ser, RS = Leu-Ser + Phe-Ser, SS = N - RR - RS.
     - True wild-type (Leu-Leu) and heterozygous Phe-Ser counts from Table 4 for Ipono 2007:
       - M-form Control (N=19): Leu-Leu=15, Leu-Phe=4, Phe-Ser=0
       - M-form Dead DDT (N=8): Leu-Leu=6, Leu-Phe=2, Phe-Ser=0
       - M-form Dead Delta (N=6): Leu-Leu=6, Leu-Phe=0, Phe-Ser=0
       - M-form Dead Perm (N=13): Leu-Leu=8, Leu-Phe=2, Phe-Phe=3, Phe-Ser=0
       - S-form Control (N=45): Leu-Leu=4, Leu-Phe=7, Leu-Ser=2, Ser-Ser=3, Phe-Phe=20, Phe-Ser=9
       - S-form Dead DDT (N=11): Leu-Leu=2, Leu-Phe=4, Leu-Ser=3, Ser-Ser=0, Phe-Phe=1, Phe-Ser=1
       - S-form Dead Delta (N=29): Leu-Leu=2, Leu-Phe=3, Leu-Ser=3, Ser-Ser=2, Phe-Phe=18, Phe-Ser=1
       - S-form Dead Perm (N=15): Leu-Leu=2, Leu-Phe=4, Leu-Ser=1, Ser-Ser=1, Phe-Phe=4, Phe-Ser=3
       - S-form Survivor DDT (N=29): Leu-Leu=0, Leu-Phe=1, Leu-Ser=0, Ser-Ser=0, Phe-Phe=27, Phe-Ser=1
       - S-form Survivor Delta (N=6): Leu-Leu=0, Leu-Phe=0, Leu-Ser=0, Ser-Ser=0, Phe-Phe=3, Phe-Ser=3
       - S-form Survivor Perm (N=33): Leu-Leu=0, Leu-Phe=0, Leu-Ser=0, Ser-Ser=0, Phe-Phe=24, Phe-Ser=9

3. **Genotype Data vs Genotype-Phenotype Data**:
   - Control group mosquitoes in Table 4 (Ipono 2007) are unexposed baseline samples, so their genotype counts were placed in `genotypes`.
   - Control samples in Table 3 for other site/year combinations provided only sample sizes (N) and allele frequencies, so they were extracted in `genotypes` with `reported_allele_freq` filled and counts set to null.
   - Genotyped dead and survivor mosquitoes from bioassays (Table 4) were extracted into `geno_pheno`.

4. **Bioassays & Figure Reading**:
   - Bioassay sample sizes (N exposed) were extracted from Table 2.
   - 24-hour post-exposure mortality percentages were visually read from Figure 2 (bar graphs) as per Rule 8, and `dead_alive_printed` was set to `false` (n_dead and n_alive set to null).

## Validator warnings

- genotype #1 (2009_Nwane_ipono_2003_m, Vgsc L1014F): frequency only (no raw counts)
- genotype #2 (2009_Nwane_ipono_2003_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #3 (2009_Nwane_ipono_2005_m, Vgsc L1014F): frequency only (no raw counts)
- genotype #4 (2009_Nwane_ipono_2005_m, Vgsc L1014S): frequency only (no raw counts)
- genotype #5 (2009_Nwane_ipono_2005_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #6 (2009_Nwane_ipono_2005_s, Vgsc L1014S): frequency only (no raw counts)
- genotype #11 (2009_Nwane_nkolondom_2003_m, Vgsc L1014F): frequency only (no raw counts)
- genotype #12 (2009_Nwane_nkolondom_2003_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #13 (2009_Nwane_nkolondom_2005_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #14 (2009_Nwane_nkolondom_2005_s, Vgsc L1014S): frequency only (no raw counts)
- genotype #16 (2009_Nwane_nkolondom_2007_m, Vgsc L1014S): frequency only (no raw counts)
- genotype #17 (2009_Nwane_nkolondom_2007_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #18 (2009_Nwane_nkolondom_2007_s, Vgsc L1014S): frequency only (no raw counts)
- genotype #19 (2009_Nwane_mangoum_2003_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #20 (2009_Nwane_mangoum_2005_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #21 (2009_Nwane_mangoum_2005_s, Vgsc L1014S): frequency only (no raw counts)
- genotype #22 (2009_Nwane_mangoum_2007_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #23 (2009_Nwane_mangoum_2007_s, Vgsc L1014S): frequency only (no raw counts)
- genotype #24 (2009_Nwane_bonanloka_2001_m, Vgsc L1014F): frequency only (no raw counts)
- genotype #25 (2009_Nwane_bonanloka_2005_m, Vgsc L1014F): frequency only (no raw counts)
- genotype #26 (2009_Nwane_bonanloka_2005_m, Vgsc L1014S): frequency only (no raw counts)
- genotype #27 (2009_Nwane_bonanloka_2005_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #28 (2009_Nwane_bonanloka_2005_s, Vgsc L1014S): frequency only (no raw counts)
- genotype #29 (2009_Nwane_bonanloka_2007_m, Vgsc L1014F): frequency only (no raw counts)
- genotype #30 (2009_Nwane_bonanloka_2007_m, Vgsc L1014S): frequency only (no raw counts)
- genotype #31 (2009_Nwane_bonanloka_2007_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #32 (2009_Nwane_bonanloka_2007_s, Vgsc L1014S): frequency only (no raw counts)
- geno_pheno #1 (4% DDT, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: 4% DDT)
- geno_pheno #2 (4% DDT, Vgsc L1014S, dead): not linked to a single bioassay (insecticide as reported: 4% DDT)
- geno_pheno #3 (0.05% deltamethrin, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: 0.05% deltamethrin)
- geno_pheno #4 (0.05% deltamethrin, Vgsc L1014S, dead): not linked to a single bioassay (insecticide as reported: 0.05% deltamethrin)
- geno_pheno #5 (0.75% permethrin, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: 0.75% permethrin)
- geno_pheno #6 (0.75% permethrin, Vgsc L1014S, dead): not linked to a single bioassay (insecticide as reported: 0.75% permethrin)
