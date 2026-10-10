# Extraction record — s13071_016_1923_5

- Extracted: 2026-10-10
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 3 · Bioassays: 10 · Geno-pheno rows: 0

## Decisions

# Extraction Decisions

1. **Surveys**:
   - Larvae and pupae of *Anopheles gambiae* s.l. were collected from open-spaced irrigated vegetable farms across the Asokwa submetropolis of Kumasi Metropolis, Ashanti Region, Ghana, and reared to adults for bioassays.
   - Bioassays in Table 1 were conducted on *Anopheles gambiae* (s.l.) before molecular identification. Therefore, survey `s13071_016_1923_5_asokwa_sl` represents this overall wild-reared population.
   - Downstream molecular identification was conducted on mosquitoes exposed to pyrethroids and organochlorides (619 specimens: 537 *An. gambiae* s.s. and 82 *An. coluzzii*). Separate surveys `s13071_016_1923_5_asokwa_gambiae_ss` and `s13071_016_1923_5_asokwa_coluzzii` were created for these molecular species to report species-specific genotypes.
   - Collection dates/years were not reported in the paper; ethics clearance was obtained in 2014 and the paper was published in 2016.

2. **Genotypes**:
   - Table 2 reports *kdr* (L1014F) carrier status as `kdr-resistant` (329 carriers / 537 tested for *An. gambiae* s.s., 75 carriers / 82 tested for *An. coluzzii*) and `kdr-sensitive` (208 non-carriers in *An. gambiae* s.s., 7 non-carriers in *An. coluzzii*). Genotype classes (RR, RS, SS) were not reported, so raw counts are entered in `n_carriers` and `n_genotyped` with `rr`, `rs`, and `ss` left as null.
   - Ace-1 G119S was assayed by PCR-RFLP on mosquitoes subjected to organophosphates and carbamates; the mutation was completely absent (0% resistant). Individual class counts rr = 0 and rs = 0 are recorded with n_genotyped = null as the exact number genotyped for this marker was not explicitly printed.

3. **Bioassays**:
   - Extracted all 10 bioassays for the wild population from Table 1 (malathion 5%, pirimiphos-methyl 0.25%, propoxur 0.1%, bendiocarb 0.1%, cyfluthrin 0.15%, deltamethrin 0.05%, lambda-cyhalothrin 0.05%, permethrin 0.75%, DDT 4%, dieldrin 4%).
   - Kisumu susceptible laboratory control assays were omitted per extraction rules.

4. **Geno-pheno vs Table 3**:
   - Table 3 reports `kdr-resistant (alive)` and `kdr-resistant (dead)` counts per insecticide and species, but groups all sensitive mosquitoes into a single `kdr-sensitive` column that does not distinguish alive from dead individuals.
   - Because the sensitive group is not split by phenotype, neither the alive group nor the dead group has a complete genotype distribution or a uniquely defined denominator (n). Consequently, complete geno-pheno rows cannot be constructed without guessing or deriving counts. Table 2 provides the complete population sample genotype counts, and per rule 6 no double-counting is permitted.
