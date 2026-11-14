# Extraction record — 2011_Ngufor_Combining_Indoor_Residual_Spraying_Chlorfenapyr_PMID22087506

- Extracted: 2026-11-14
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 1 · Bioassays: 0 · Geno-pheno rows: 8

## Decisions

# Extraction Decisions for Ngufor et al. 2011 (Malaria Journal)

## Marker Identification
- The paper evaluates the *kdr* mutation using the PCR assay described by Martinez-Torres et al. 1998 (reference 18), which identifies the Vgsc L1014F (*kdr-west*) mutation. In accordance with the target marker list, `gene` is set to `Vgsc` and `marker` to `L1014F`.

## Surveys
- **Site**: Akron, a village on the periphery of Porto Novo, Benin. Latitude and longitude were not provided in the paper.
- Two surveys were created:
  1. `..._akron_larval`: Baseline larval collection from Akron reared to adulthood (100 adults genotyped for kdr frequency).
  2. `..._akron_huts`: Wild adults collected during the experimental hut trial conducted between June and September 2010 (total 865 An. gambiae s.l. females caught).

## Bioassays vs. Experimental Hut Interventions
- The study reports results of an experimental hut trial with 7 arms (untreated nets, deltamethrin-treated LLINs, chlorfenapyr IRS, and combinations). These are Phase II intervention trials measuring hut entry, blood feeding inhibition, induced exiting, and mortality, not standardized WHO or CDC susceptibility bioassays. Furthermore, combination treatments violate the rule of 'one specific insecticide each' for bioassays (Rule 8b). Therefore, no bioassays were extracted into `bioassays`.

## Genotypes & Genotype-Phenotype Data
- **Genotypes (`genotypes`)**: Extracted the baseline larval sample (N = 100, kdr frequency = 0.91) which was not split by bioassay outcome.
- **Genotype-Phenotype (`geno_pheno`)**: Table 3 reports kdr allele frequencies for live and dead mosquitoes across 4 experimental hut treatments. In accordance with Rule 6 ('or the bioassay itself is not extractable — leave bioassay_id null and give insecticide as reported'), these are extracted into `geno_pheno` with `bioassay_id: null`.
- Table 3 provides allele counts in parentheses: `kdr alleles / total kdr and susceptibility alleles`. Diploid mosquito counts (n) and genotype classes (RR, RS, SS) are not printed, so `n`, `rr`, `rs`, and `ss` are left as `null` while `reported_allele_freq` contains the printed proportion.
- Note that for Chlorfenapyr IRS + LLIN (alive), the paper reports `1.0 (25/25)`, which represents an odd number of alleles (25). This is noted in the `inconsistency_note`.

## Validator warnings

- genotype #1 (2011_Ngufor_Combining_Indoor_Residual_Spraying_Chlorfenapyr_PMID22087506_akron_larval, Vgsc L1014F): frequency only (no raw counts)
- geno_pheno #1 (chlorfenapyr, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: chlorfenapyr)
- geno_pheno #2 (chlorfenapyr, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: chlorfenapyr)
- geno_pheno #3 (chlorfenapyr + deltamethrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: chlorfenapyr + deltamethrin)
- geno_pheno #3 (chlorfenapyr + deltamethrin, Vgsc L1014F, alive): inconsistent in the paper (values kept as printed) — Reported as 1.0 (25/25) kdr alleles/total alleles; 25 total alleles is an odd number for diploid mosquitoes.
- geno_pheno #4 (chlorfenapyr + deltamethrin, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: chlorfenapyr + deltamethrin)
- geno_pheno #5 (deltamethrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #6 (deltamethrin, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #7 (untreated net, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: untreated net)
- geno_pheno #8 (untreated net, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: untreated net)
