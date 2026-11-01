# Extraction record — 2014_Riveron_Single_Mutation_GSTe2_Gene_Allows_PMID24565444

- Extracted: 2026-11-01
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 9 · Bioassays: 6 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys**:
   - Created 10 distinct surveys representing field sampling locations across 9 African countries: Pahou (Benin), Kpome (Benin), Obuasi (Ghana), Bobo-Dioulasso (Burkina Faso), Gounougou (Cameroon), Tororo (Uganda), Kisumu (Kenya), Chikwawa (Malawi), Katete district (Zambia), and Chokwe (Mozambique).
   - Geographic coordinates printed for Pahou (6°23′N, 2°13′E), Kpome (6°55′N, 2°19′E), and Gounougou (9°05′N, 13°40′E) were converted to decimal degrees.

2. **Target Markers**:
   - Extracted `GSTe2` `L119F` as reported in the text.

3. **Genotypes**:
   - Extracted 9 population-level genotyping records (30 field females per country) assayed by TaqMan for the 119F mutation. Per Rule 2, reported allele frequencies were recorded directly as printed (e.g., 48.2% -> 0.482, fixed -> 1.0, absent -> 0.0) without back-calculating genotype counts.

4. **Bioassays**:
   - Extracted WHO bioassays reported for field mosquito populations (Kpome 4% DDT for females and males; Gounougou 4% DDT for females and males; Pahou deltamethrin and permethrin). Laboratory strain controls (FANG) and Drosophila transgenic contact bioassays were excluded per rules.

5. **Geno-Pheno**:
   - Genotypes split by phenotype (alive vs dead) in Gounougou (Cameroon) for DDT, permethrin, and lambda-cyhalothrin are reported only via odds ratios and proportion plots by genotype class in the main text/figures (e.g., 72.5% of T/T resistant, 54.5% of C/T resistant, 10% of C/C resistant). Because exact RR/RS/SS counts or explicit allele frequencies per phenotype class are not printed in the main text (and per Rule 8 we must not back-calculate or guess counts without explicit data), `geno_pheno` is left empty to avoid unpopulated/empty records.

## Validator warnings

- genotype #1 (2014_riveron_benin_pahou, GSTe2 L119F): frequency only (no raw counts)
- genotype #2 (2014_riveron_ghana_obuasi, GSTe2 L119F): frequency only (no raw counts)
- genotype #3 (2014_riveron_burkina_bobo, GSTe2 L119F): frequency only (no raw counts)
- genotype #4 (2014_riveron_cameroon_gounougou, GSTe2 L119F): frequency only (no raw counts)
- genotype #5 (2014_riveron_uganda_tororo, GSTe2 L119F): frequency only (no raw counts)
- genotype #6 (2014_riveron_kenya_kisumu, GSTe2 L119F): frequency only (no raw counts)
- genotype #7 (2014_riveron_malawi_chikwawa, GSTe2 L119F): frequency only (no raw counts)
- genotype #8 (2014_riveron_zambia_katete, GSTe2 L119F): frequency only (no raw counts)
- genotype #9 (2014_riveron_mozambique_chokwe, GSTe2 L119F): frequency only (no raw counts)
