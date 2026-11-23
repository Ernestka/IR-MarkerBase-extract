# Extraction record — 2018_Mint_Mohamed_Lemine_Pyrethroid_Resistance_Major_Malaria_Vector_PMID29895314

- Extracted: 2026-11-23
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 0 · Bioassays: 8 · Geno-pheno rows: 2

## Decisions

### Data Extraction Decisions

1. **Surveys & Sampling Locations**:
   - Larval collections were conducted in two sites in Nouakchott (Lycée de Teyarett and Carrefour Ould Badou) during August-September in 2015 and 2016.
   - Bioassay data (Table 2) and molecular data (SINE PCR and kdr genotyping) are reported for the combined Nouakchott population, so surveys are established at the town level for Nouakchott per year (2015 and 2016).
   - An. arabiensis was confirmed by SINE PCR to be 100% of the An. gambiae (s.l.) collected (250/250 tested).

2. **Bioassays**:
   - Extracted 8 WHO tube bioassays from Table 2 (4 in 2015, 4 in 2016).
   - Exact exposed numbers and reported percentage mortalities were recorded. Since dead/alive individual counts were not literally printed in Table 2/text, `dead_alive_printed` is set to `false` and counts are left `null` as per rule 2.
   - Discrepancy noted: Text on page 4 describes malathion at 5% concentration, whereas Table 2 lists Malathion (2%). The 2% listed in Table 2 was extracted into the bioassay concentration field and documented in `inconsistency_note`.

3. **Genotype Data & Multi-Allelic Codon Handling (Rule 4b)**:
   - A total of 70 pyrethroid bioassay survivors were genotyped for kdr mutations (L1014F / West kdr and L1014S / East kdr).
   - Genotype breakdown among survivors (N=70):
     - RwRw (homozygous L1014F): 38
     - ReRe (homozygous L1014S): 15
     - RwS (heterozygous L1014F / wild-type): 1
     - SS (homozygous wild-type L/L): 16
   - Per Rule 4b, L1014F and L1014S are split into separate rows in `geno_pheno`:
     - For `L1014F`: RR = 38 (RwRw), RS = 1 (RwS), SS = 31 (70 - 38 - 1, comprising 15 ReRe + 16 SS).
     - For `L1014S`: RR = 15 (ReRe), RS = 0 (ReS was 0), SS = 55 (70 - 15 - 0, comprising 38 RwRw + 1 RwS + 16 SS).
   - Because these genotypes represent bioassay survivors pooled across pyrethroids and sampling years (2015-2016), they are placed in `geno_pheno` with `bioassay_id` = null and `insecticide` = 'deltamethrin + permethrin'. Per Rule 6, they are not duplicated into `genotypes`.

## Validator warnings

- bioassay 2018_Mint_Mohamed_Lemine_Pyrethroid_Resistance_Major_Malaria_Vector_PMID29895314_nouakchott_2015_mal_2: inconsistent in the paper (values kept as printed) — Table 2 lists Malathion concentration as 2%, whereas page 4 text describes malathion (5%).
- bioassay 2018_Mint_Mohamed_Lemine_Pyrethroid_Resistance_Major_Malaria_Vector_PMID29895314_nouakchott_2016_mal_2: inconsistent in the paper (values kept as printed) — Table 2 lists Malathion concentration as 2%, whereas page 4 text describes malathion (5%).
- geno_pheno #1 (deltamethrin + permethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin + permethrin)
- geno_pheno #2 (deltamethrin + permethrin, kdr L1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin + permethrin)
