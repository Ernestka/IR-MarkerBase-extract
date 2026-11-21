# Extraction record — 2017_Ole_Sangba_Evidence_Multiple_Insecticide_Resistance_Mechanism_PMID28086840

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 7 · Genotype rows: 21 · Bioassays: 24 · Geno-pheno rows: 0

## Decisions

### Key Extraction Decisions
1. **Surveys**: Mosquito larvae were collected in 7 districts of Bangui (Gbanikola, PK10, Ouango, Cattin, Centre-ville, Yapele, Petevo) between September and November 2014, and reared to adults. Each district represents a separate survey record. All genotyped specimens were confirmed by PCR-RFLP to be *Anopheles gambiae* s.s. (S-form).
2. **Genotypes**: Exactly 3 target markers were tested across 30 mosquitoes per district (total N=210):
   - *kdr* L1014F (Vgsc L995F): Exact counts of RwRw (RR) and RwS (RS) provided in Table 1.
   - *kdr* L1014S (Vgsc L995S): Zero carriers of ReRe or ReS were detected; per multi-allelic rule (Rule 4b), SS count is set to 30 for all sites.
   - *Ace-1* G119S (Ace-1 G280S): Text explicitly states no Ace-1R mutation was detected in any tested mosquito (n=30 per district; RR=0, RS=0, SS=30).
3. **Bioassays**: WHO standard diagnostic dose tube tests were conducted using 4 batches of 25 females (100 exposed per insecticide per district). Bioassays with exact mortality percentages printed in text are extracted. Per Rule 2, since mortality percentages are given in the text, `n_exposed` is set to 100, `reported_mortality_pct` is recorded, and `dead_alive_printed` is set to `false` with `n_dead` and `n_alive` left `null`. Reference strain control tests (Kisumu) were omitted per Rule 5.
4. **Geno-Pheno**: No genotype data broken down separately by bioassay survivors vs dead were reported in the text or tables.
