# Extraction record — 2013_Diabate_Environmentally_Friendly_Tool_Control_Mosquito_PMID23758904

- Extracted: 2026-10-17
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 10 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Study and Survey Structure
- The study evaluates the physical efficacy of Lehmann's window funnel entry trap against indoor mosquito entry in two study sites in Burkina Faso: Soumousso and VK3 (Bama).
- Mosquitoes were sampled between July and September 2012 by two methods: window entry traps and indoor manual aspiration (referred to as 'House').
- A total of 10 surveys were created to capture the finest resolution across 2 sites (Soumousso, VK3) x 2 collection methods (window trap, indoor house aspiration) x molecular species/forms (M form [An. coluzzii], S form [An. gambiae s.s.], and An. arabiensis).

### Genotype Data
- Table 1 reports the number of individuals genotyped for each molecular form/species and the allelic frequencies of the kdr mutation (Vgsc L1014F / L995F, based on citation [1] Diabate et al. 2004 referring to the Leu-Phe kdr mutation).
- Target marker is specified as gene: 'Vgsc', marker: 'L1014F' (alias for Vgsc L995F).
- Because genotype classes (RR, RS, SS) are not reported in the text or table, only reported_allele_freq and n_genotyped are extracted; count fields (rr, rs, ss, n_carriers, resistant_allele_count) are left as null per Extraction Rule 2.

### Bioassays and Genotype-Phenotype Links
- No standard insecticide susceptibility bioassays (WHO tube or CDC bottle) were conducted; the study evaluated a non-insecticidal mechanical trap. Therefore, `bioassays` and `geno_pheno` arrays are empty.

## Validator warnings

- genotype #1 (2013_Diabate_Environmentally_Friendly_Tool_Control_Mosquito_PMID23758904_soumousso_trap_m, Vgsc L1014F): frequency only (no raw counts)
- genotype #2 (2013_Diabate_Environmentally_Friendly_Tool_Control_Mosquito_PMID23758904_soumousso_trap_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #3 (2013_Diabate_Environmentally_Friendly_Tool_Control_Mosquito_PMID23758904_soumousso_trap_ara, Vgsc L1014F): frequency only (no raw counts)
- genotype #4 (2013_Diabate_Environmentally_Friendly_Tool_Control_Mosquito_PMID23758904_soumousso_house_m, Vgsc L1014F): frequency only (no raw counts)
- genotype #5 (2013_Diabate_Environmentally_Friendly_Tool_Control_Mosquito_PMID23758904_soumousso_house_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #6 (2013_Diabate_Environmentally_Friendly_Tool_Control_Mosquito_PMID23758904_soumousso_house_ara, Vgsc L1014F): frequency only (no raw counts)
- genotype #7 (2013_Diabate_Environmentally_Friendly_Tool_Control_Mosquito_PMID23758904_vk3_trap_m, Vgsc L1014F): frequency only (no raw counts)
- genotype #8 (2013_Diabate_Environmentally_Friendly_Tool_Control_Mosquito_PMID23758904_vk3_trap_s, Vgsc L1014F): frequency only (no raw counts)
- genotype #9 (2013_Diabate_Environmentally_Friendly_Tool_Control_Mosquito_PMID23758904_vk3_house_m, Vgsc L1014F): frequency only (no raw counts)
- genotype #10 (2013_Diabate_Environmentally_Friendly_Tool_Control_Mosquito_PMID23758904_vk3_house_s, Vgsc L1014F): frequency only (no raw counts)
