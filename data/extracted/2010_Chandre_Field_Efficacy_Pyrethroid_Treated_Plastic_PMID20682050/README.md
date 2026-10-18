# Extraction record — 2010_Chandre_Field_Efficacy_Pyrethroid_Treated_Plastic_PMID20682050

- Extracted: 2026-10-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 0 · Bioassays: 0 · Geno-pheno rows: 19

## Decisions

# Extraction Decisions Chandre et al. 2010 (PMID: 20682050)

## Surveys and Species Breakdown
- Collections took place in experimental huts in Vallée du Kou near Bobo-Dioulasso, Burkina Faso, between mid-September and late December 2005.
- A total of 202 Anopheles gambiae s.s. females sampled from the experimental huts were genotyped and molecularly identified to molecular forms using the PCR assay of Favia et al. (2001):
  - M form (Anopheles coluzzii): n = 131 (64.9%)
  - S form (Anopheles gambiae s.s.): n = 71 (35.1%)
- Two surveys are created corresponding to the molecular species.

## Bioassays vs. Genotype-Phenotype Data
- The study is an experimental hut trial testing ITPS (permethrin-treated durable lining) and Olyset nets (permethrin-treated LN). Table 1 presents pooled hut results for An. gambiae s.l. over 80 nights, which are field trial efficacy endpoints, not standard bioassays. In situ cone bioassays were conducted only on the laboratory susceptible Kisumu strain (controls, excluded per Rule 5). Thus `bioassays` is empty.
- In Table 2, all 202 genotyped mosquitoes are presented categorized by mortality outcome (dead vs alive/total collected) for each hut treatment arm. Per Rule 6, these are extracted in `geno_pheno` and omitted from `genotypes` to avoid double counting.
- For S form in the Control arm, 0 mosquitoes died (0/12 kdr/kdr and 0/1 kdr/+); since n = 0, no dead row is extracted.

## Target Marker
- The paper genotyped mosquitoes using the PCR assay of Martinez-Torres et al. (1998) [reference 13], which detects the Vgsc L1014F (L995F, kdr-west) mutation. In the previous iteration, `gene` was entered as 'kdr' and `marker` as 'kdr', which failed validation as 'kdr kdr' is not a recognized marker. Corrected to `gene`: 'Vgsc' and `marker`: 'L1014F'.

## Validator warnings

- geno_pheno #1 (Control, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: Control)
- geno_pheno #2 (Control, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: Control)
- geno_pheno #3 (permethrin (Olyset), Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin (Olyset))
- geno_pheno #4 (permethrin (Olyset), Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin (Olyset))
- geno_pheno #5 (permethrin (ITPS), Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin (ITPS))
- geno_pheno #6 (permethrin (ITPS), Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin (ITPS))
- geno_pheno #7 (permethrin (ITPS) + untreated net, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin (ITPS) + untreated net)
- geno_pheno #8 (permethrin (ITPS) + untreated net, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin (ITPS) + untreated net)
- geno_pheno #9 (permethrin (ITPS + Olyset), Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin (ITPS + Olyset))
- geno_pheno #10 (permethrin (ITPS + Olyset), Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin (ITPS + Olyset))
- geno_pheno #11 (Control, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: Control)
- geno_pheno #12 (permethrin (Olyset), Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin (Olyset))
- geno_pheno #13 (permethrin (Olyset), Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin (Olyset))
- geno_pheno #14 (permethrin (ITPS), Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin (ITPS))
- geno_pheno #15 (permethrin (ITPS), Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin (ITPS))
- geno_pheno #16 (permethrin (ITPS) + untreated net, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin (ITPS) + untreated net)
- geno_pheno #17 (permethrin (ITPS) + untreated net, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin (ITPS) + untreated net)
- geno_pheno #18 (permethrin (ITPS + Olyset), Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin (ITPS + Olyset))
- geno_pheno #19 (permethrin (ITPS + Olyset), Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin (ITPS + Olyset))
