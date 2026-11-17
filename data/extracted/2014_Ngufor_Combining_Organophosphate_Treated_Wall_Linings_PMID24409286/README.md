# Extraction record — 2014_Ngufor_Combining_Organophosphate_Treated_Wall_Linings_PMID24409286

- Extracted: 2026-11-17
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 4 · Bioassays: 2 · Geno-pheno rows: 28

## Decisions

# Extraction Decisions: Ngufor et al. (2014)

## Survey Design and Splitting
- Mosquitoes were sampled at Valley du Kou 5 (VK5; 4°25'W, 11°24'N) near Bobo-Dioulasso, Burkina Faso, between August and November 2011.
- Three distinct surveys were extracted:
  1. `_vk5_larval`: Larvae collected from breeding sites around the hut station and reared to adults for WHO cylinder susceptibility testing (Tables 1 & 2).
  2. `_vk5_hut_trial1`: Wild adult An. gambiae s.s. collected entering experimental huts during the 6-week Single Intervention Trial (Trial 1; evaluating p-methyl durable lining and net wall hangings vs pyrethroid DL and control).
  3. `_vk5_hut_trial2`: Wild adult An. gambiae s.s. collected entering experimental huts during the 6-week First Combined Intervention Trial (Trial 2; evaluating p-methyl DL and NWH combined with LLINs vs LLIN alone, p-methyl alone, and control).

## Species Identification
- The paper notes that molecular identification by SINE-PCR on 559 randomly selected samples demonstrated 98% were the M-form of An. gambiae s.s. (now An. coluzzii) and 2% S-form. Because genotype counts are not separated by molecular form, the species is retained as `Anopheles gambiae s.s.`.

## Population Genotypes vs Genotype-Phenotype Data
- Control hut samples (untreated plastic sheeting control) were unexposed to insecticides. All genotyped mosquitoes from the control huts survived (100% alive). These untreated baseline population samples were extracted into `genotypes` for Trial 1 (kdr n=140, ace-1R n=97) and Trial 2 (kdr n=63, ace-1R n=81).
- Treated experimental hut collections were split by survival outcome (alive vs dead) in Tables 6 and 7. These were extracted into `geno_pheno`.
- Because experimental hut trials represent vector control interventions in huts rather than standard single-dose laboratory bioassays, `bioassay_id` is left `null` and the active ingredient(s) printed in the paper are assigned to `insecticide`:
  - Pyrethroid DL: `deltamethrin` (175 mg/m²)
  - P-methyl DL and NWH: `pirimiphos-methyl` (1 g/m²)
  - LLIN: `deltamethrin` (Permanet 2.0, 55 mg/m²)
  - Combined interventions: `deltamethrin + pirimiphos-methyl`
- For treatments 3-6 in Trial 2, 100% mortality was observed and footnote * in Tables 6 and 7 confirms no live mosquitoes were collected; thus only dead groups exist and are extracted.

## Inconsistencies Between Table 6 and Table 7
- Trial 1, Pyrethroid DL, dead kdr: Table 6 reports n = 51 with allele frequency 0.90. Table 7 gives RS as 7/15 alive (8 dead) and RR as 44/85 alive (41 dead), totaling 49 dead. Two dead mosquitoes are missing from Table 7 (possibly 2 SS dead).
- Trial 1, P-methyl DL (walls and ceiling), dead kdr: Table 6 reports n = 61 dead with frequency 0.94. Table 7 reports RS as 0/7 (7 dead) and RR as 18/82 (64 dead), which would sum to 71 dead. An RR total of 72 (54 dead) would reconcile n = 61 and allele frequency 0.94.
- Trial 1, P-methyl NWH (walls and ceiling), dead kdr: Table 6 reports n = 68 dead with frequency 0.96. Table 7 reports RS as 0/6 (6 dead) and RR as 3/62 (59 dead), summing to 65 dead.
These mismatches are preserved as reported and flagged in `inconsistency_note`.

## Bioassays
- Tables 1 and 2 report standard WHO cylinder bioassays on wild-reared An. gambiae s.s. exposed to deltamethrin 0.05% and pirimiphos-methyl 0.25%. Reference strain (Kisumu) tests were excluded per rules.
- Cone bioassays on treated materials were only conducted using the laboratory Kisumu strain and were therefore skipped.

## Validator warnings

- geno_pheno #1 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #2 (deltamethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #2 (deltamethrin, kdr L1014F, dead): inconsistent in the paper (values kept as printed) — Table 6 reports n = 51 dead with kdr allele frequency 0.90, but Table 7 reports genotype survival rates of 7/15 for RS and 44/85 for RR (sum of dead RS and RR is 8 + 41 = 49), suggesting 2 dead mosquitoes were SS or omitted from Table 7.
- geno_pheno #3 (pirimiphos-methyl, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #4 (pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #5 (pirimiphos-methyl, ace-1R G119S, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #6 (pirimiphos-methyl, ace-1R G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #7 (pirimiphos-methyl, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #8 (pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #9 (pirimiphos-methyl, ace-1R G119S, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #10 (pirimiphos-methyl, ace-1R G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #11 (pirimiphos-methyl, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #12 (pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #12 (pirimiphos-methyl, kdr L1014F, dead): inconsistent in the paper (values kept as printed) — Table 6 reports n = 61 dead with kdr allele frequency 0.94, but Table 7 reports RR survival as 18/82 (64 dead) and RS survival as 0/7 (7 dead), which sum to 71 dead mosquitoes. A total of 72 RR (54 dead) would reconcile both n = 61 and frequency 0.94.
- geno_pheno #12 (pirimiphos-methyl, kdr L1014F, dead): RR+RS+SS = 64+7+0 = 71 but n = 61
- geno_pheno #13 (pirimiphos-methyl, ace-1R G119S, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #14 (pirimiphos-methyl, ace-1R G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #15 (pirimiphos-methyl, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #16 (pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #16 (pirimiphos-methyl, kdr L1014F, dead): inconsistent in the paper (values kept as printed) — Table 6 reports n = 68 dead with kdr allele frequency 0.96, but Table 7 reports RR survival as 3/62 (59 dead) and RS survival as 0/6 (6 dead), summing to 65 dead mosquitoes.
- geno_pheno #16 (pirimiphos-methyl, kdr L1014F, dead): RR+RS+SS = 59+6+0 = 65 but n = 68
- geno_pheno #17 (pirimiphos-methyl, ace-1R G119S, alive): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #18 (pirimiphos-methyl, ace-1R G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #19 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #20 (deltamethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #21 (pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #22 (pirimiphos-methyl, ace-1R G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #23 (pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #24 (pirimiphos-methyl, ace-1R G119S, dead): not linked to a single bioassay (insecticide as reported: pirimiphos-methyl)
- geno_pheno #25 (deltamethrin + pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + pirimiphos-methyl)
- geno_pheno #26 (deltamethrin + pirimiphos-methyl, ace-1R G119S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + pirimiphos-methyl)
- geno_pheno #27 (deltamethrin + pirimiphos-methyl, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + pirimiphos-methyl)
- geno_pheno #28 (deltamethrin + pirimiphos-methyl, ace-1R G119S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin + pirimiphos-methyl)
