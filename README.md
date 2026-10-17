# IR MarkerBase — extraction pipeline

A pipeline that builds a database of **insecticide-resistance (IR) markers in
African *Anopheles*** from the literature: genotype counts at target markers
(kdr/Vgsc, Ace-1, Rdl, GSTe2, Cyp6p9a/b, Cyp6aa1, Cyp9k1) plus linked bioassays
and genotype–phenotype data, for spatial and temporal models of marker frequencies.

PDFs go into a Google Drive folder (or a local folder for testing). The pipeline
reads each one, decides whether it is eligible, extracts the data with an LLM,
checks it in code, and builds one combined table.

_Adapted from PfDR-MarkerBase-extract (P. falciparum drug resistance). The old
Pf data is preserved in git history (commit `7acfa7c`)._

## Status

![pipeline status](docs/stats.svg)

<sub>Updates automatically on every run.</sub>

## Roster

<!-- ROSTER:START -->

**123 paper(s) · estimated spend $0.00** (eligibility $0.00 · extraction $0.00) · updated 2026-10-17

| id | source | status | eligible | confidence | duplicate_risk | needs_supplement | spec_version | first_seen | last_assessed | supp_attempts | supplement_fp | elig_model | elig_tok_in | elig_tok_out | extract_model | extract_tok_in | extract_tok_out | notes | est_$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 07-1575 | master | EXTRACTED | True | high | none | False | 1 | 2026-10-13 | 2026-10-13 | 0 |  | gemini:gemini-3.7-flash | 5852 | 1799 | gemini:gemini-3.7-flash | 20693 | 50422 | 3 survey(s), 4 genotype, 0 bioassay, 12 geno-pheno rows; 16 warning(s) | 0.0000 |
| 1-s2.0-S0001706X19317632-main | master | EXTRACTED | True | high | none | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 5472 | 3401 | gemini:gemini-3.5-flash | 27742 | 56306 | 10 survey(s), 21 genotype, 19 bioassay, 0 geno-pheno rows; 23 warning(s) | 0.0000 |
| 1-s2.0-S0001706X21004691-main | master | EXTRACTED | True | high | none | False | 1 | 2026-10-13 | 2026-10-13 | 0 |  | gemini:gemini-3.7-flash | 6012 | 1558 | gemini:gemini-3.8-flash | 7681 | 14356 | 3 survey(s), 3 genotype, 9 bioassay, 0 geno-pheno rows | 0.0000 |
| 1471-2334-12-275 | master | EXTRACTED | True | high | none | False | 1 | 2026-10-13 | 2026-10-13 | 0 |  | gemini:gemini-3.7-flash | 6012 | 2128 | gemini:gemini-3.8-flash | 7873 | 10679 | 1 survey(s), 0 genotype, 3 bioassay, 2 geno-pheno rows; 2 warning(s) | 0.0000 |
| 1475-2875-12-151 | master | EXTRACTED | True | high | none | False | 1 | 2026-10-13 | 2026-10-13 | 0 |  | gemini:gemini-3.7-flash | 6012 | 1876 | gemini:gemini-3.7-flash | 7797 | 25279 | 3 survey(s), 6 genotype, 18 bioassay, 0 geno-pheno rows; 4 warning(s) | 0.0000 |
| 1475-2875-6-52 | master | INELIGIBLE |  |  |  |  | 1 | 2026-10-13 | 2026-10-13 | 0 |  | gemini:gemini-3-flash-preview | 4812 | 7985 |  |  |  | model returned no structured result — re-run or check by hand | 0.0000 |
| 1475-2875-7-178 (1) | master | EXTRACTED | True | high | none | False | 1 | 2026-10-12 | 2026-10-12 | 0 |  | gemini:gemini-3.8-flash | 7412 | 1719 | gemini:gemini-3.8-flash | 9134 | 15292 | 2 survey(s), 2 genotype, 0 bioassay, 0 geno-pheno rows | 0.0000 |
| 1475-2875-8-81 | master | EXTRACTED | True | high | none | False | 1 | 2026-10-13 | 2026-10-13 | 0 |  | gemini:gemini-3.8-flash | 5852 | 2055 | gemini:gemini-3.7-flash | 18618 | 47620 | 2 survey(s), 0 genotype, 2 bioassay, 4 geno-pheno rows; 3 warning(s) | 0.0000 |
| 1475-2875-9-83 | master | INELIGIBLE |  |  |  |  | 1 | 2026-10-13 | 2026-10-13 | 0 |  | gemini:gemini-3-flash-preview | 4932 | 7985 |  |  |  | model returned no structured result — re-run or check by hand | 0.0000 |
| 1756-3305-5-127 | master | EXTRACTED | True | high | none | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 6552 | 3606 | gemini:gemini-3.5-flash | 8246 | 37022 | 6 survey(s), 11 genotype, 37 bioassay, 0 geno-pheno rows | 0.0000 |
| 1756-3305-5-68 | master | EXTRACTED | True | high | low | False | 1 | 2026-10-13 | 2026-10-13 | 0 |  | gemini:gemini-3-flash-preview | 5472 | 3383 | gemini:gemini-3.8-flash | 7160 | 10140 | 1 survey(s), 2 genotype, 7 bioassay, 0 geno-pheno rows; 1 warning(s) | 0.0000 |
| 1756-3305-6-352 | master | EXTRACTED | True | high | low | False | 1 | 2026-10-08 | 2026-10-08 | 0 |  | gemini:gemini-3.5-flash | 8172 | 1632 | gemini:gemini-3.5-flash | 9816 | 31601 | 10 survey(s), 6 genotype, 8 bioassay, 7 geno-pheno rows | 0.0000 |
| 1756-3305-7-213 | master | INELIGIBLE |  |  |  |  | 1 | 2026-10-13 | 2026-10-13 | 0 |  | gemini:gemini-3-flash-preview | 6552 | 7985 |  |  |  | model returned no structured result — re-run or check by hand | 0.0000 |
| 1756-3305-7-450 | master | INELIGIBLE | False | high | high | False | 1 | 2026-10-13 | 2026-10-13 | 0 |  | gemini:gemini-3-flash-preview | 9252 | 3201 |  |  |  |  | 0.0000 |
| 1998_Brogdon_Insecticide_Resistance_Vector_Control_PMID9866736 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.7-flash | 6372 | 943 |  |  |  |  | 0.0000 |
| 2001_Reiter_Climate_Change_Mosquito_Borne_Disease_PMID11250812 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.5-flash | 12612 | 1346 |  |  |  |  | 0.0000 |
| 2006_Adams_Abstracts_Fifth_International_Symposium_Molecular_PMC2990333 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.5-flash | 40692 | 2008 |  |  |  |  | 0.0000 |
| 2006_Anyanwu_Health_Effects_Long_Term_Exposure_PMID17173181 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.7-flash | 7412 | 928 |  |  |  |  | 0.0000 |
| 2006_Mazzoni_Molecular_Polymorphism_Differentiation_Introgressi_PMID17069656 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.5-flash | 7412 | 1339 |  |  |  |  | 0.0000 |
| 2007_Djouaka_Quantification_Efficiency_Treatment_Anopheles_Gamb_PMID17488523 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.7-flash | 4812 | 1029 |  |  |  |  | 0.0000 |
| 2007_NoAuthor_Infectious_Disease_Safety_Net_Malaria_PMC1867985 | master | INELIGIBLE | False | high | high | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.7-flash | 3772 | 840 |  |  |  |  | 0.0000 |
| 2007_Wang-Sattler_Mosaic_Genome_Architecture_Anopheles_Gambiae_PMID18043756 | master | INELIGIBLE | False | high | low | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.7-flash | 7412 | 1725 |  |  |  |  | 0.0000 |
| 2007_Wondji_Identification_Analysis_Single_Nucleotide_Polymorp_PMID17204152 | master | INELIGIBLE | False | high | low | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.5-flash | 8452 | 2836 |  |  |  |  | 0.0000 |
| 2008_Caputo_Anopheles_Gambiae_Complex_Along_Gambia_PMID18803885 | master | INELIGIBLE | False | high | low | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 10532 | 1590 |  |  |  |  | 0.0000 |
| 2008_Esnault_High_Genetic_Differentiation_M_Molecular_PMID18414665 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 5332 | 1457 |  |  |  |  | 0.0000 |
| 2008_Greenwood_Malaria_Progress_Perils_Prospects_Eradication_PMID18382739 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 7632 | 858 |  |  |  |  | 0.0000 |
| 2008_Irish_Loss_Protection_Insecticide_Treated_Nets_PMID18564409 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 4292 | 1200 |  |  |  |  | 0.0000 |
| 2008_Sogoba_Spatial_Distribution_Chromosomal_Forms_Anopheles_PMID18847463 | master | INELIGIBLE | False | high | high | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.7-flash | 7932 | 1860 |  |  |  |  | 0.0000 |
| 2009_van_den_Berg_Global_Status_DDT_Alternatives_Use_PMID20049114 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.7-flash | 5852 | 1061 |  |  |  |  | 0.0000 |
| 2010_Ahoua_Alou_Distribution_Ace_1R_Resistance_Carbamates_PMID20553593 | master | EXTRACTED | True | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.7-flash | 5472 | 1692 | gemini:gemini-3.5-flash | 7247 | 27872 | 10 survey(s), 8 genotype, 23 bioassay, 0 geno-pheno rows | 0.0000 |
| 2010_Brooke_Larval_Time_Hatch_Insecticide_Resistance_PMC2963243 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 2772 | 1196 |  |  |  |  | 0.0000 |
| 2010_Djogbenou_Costs_Insensitive_Acetylcholinesterase_Insecticide_PMID20070891 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 6012 | 1769 |  |  |  |  | 0.0000 |
| 2010_Howard_Pyrethroid_Resistance_Anopheles_Gambiae_Leads_PMID20553597 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.7-flash | 6552 | 1263 |  |  |  |  | 0.0000 |
| 2010_Koekemoer_Characterization_Multiple_Insecticide_Resistance_A_PMC2963256 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 2232 | 1359 |  |  |  |  | 0.0000 |
| 2010_Mosqueira_Efficacy_Insecticide_Paint_Against_Malaria_PMID21108820 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 5472 | 1478 |  |  |  |  | 0.0000 |
| 2010_Rivero_Insecticide_Control_Vector_Borne_Diseases_PMID20700451 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.7-flash | 6372 | 844 |  |  |  |  | 0.0000 |
| 2011_Bai_Large_Scale_RNAi_Screen_G_PMID21806814 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.7-flash | 7632 | 799 |  |  |  |  | 0.0000 |
| 2011_Barbosa_Challenges_Estimating_Insecticide_Selection_Pressu_PMID22069506 | master | INELIGIBLE | False | high | high | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 7412 | 1315 |  |  |  |  | 0.0000 |
| 2011_Konate_Intermittent_Preventive_Treatment_Malaria_Provides_PMID21304925 | master | INELIGIBLE | False | high | none | True | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.7-flash | 8972 | 2715 |  |  |  |  | 0.0000 |
| 2012_Alout_Novel_AChE_Inhibitors_Sustainable_Insecticide_PMID23056599 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 5852 | 1254 |  |  |  |  | 0.0000 |
| 2012_Jagannathan_Increasing_Incidence_Malaria_Children_Despite_PMID23273022 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.7-flash | 6012 | 1120 |  |  |  |  | 0.0000 |
| 2012_Stuckey_Simulation_Malaria_Epidemiology_Control_Highlands_PMID23107070 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.7-flash | 9252 | 1285 |  |  |  |  | 0.0000 |
| 2012_Wong_Select_Small_Core_Structure_Carbamates_PMID23049714 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.7-flash | 7932 | 1575 |  |  |  |  | 0.0000 |
| 2013_Gatton_Importance_Mosquito_Behavioural_Adaptations_Malari_PMID23550770 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 8452 | 879 |  |  |  |  | 0.0000 |
| 2013_Hemingway_Country_Level_Operational_Implementation_Global_PMID23696658 | master | REVIEW_DUPLICATE | True | high | high | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.8-flash | 4932 | 2323 |  |  |  |  | 0.0000 |
| 2013_Stewart_Indoor_Application_Attractive_Toxic_Sugar_PMID24367638 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 5332 | 1460 |  |  |  |  | 0.0000 |
| 2014_Monteiro_Genetic_Diversity_Brazilian_Aedes_Aegypti_PMID25233218 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.7-flash | 6892 | 927 |  |  |  |  | 0.0000 |
| 2014_Temeyer_Acetylcholinesterase_Sand_Fly_Phlebotomus_Papatasi_PMID25491113 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 7092 | 1571 |  |  |  |  | 0.0000 |
| 2015_Chaccour_Establishment_Ivermectin_Research_Malaria_Eliminat_PMID26068560 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 6012 | 1015 |  |  |  |  | 0.0000 |
| 2015_Lee_Peer_Review_Report_Absence_Kdr_DOI_10_5256_f1000research_7052_r8978 | master | EXTRACTED | True | high | low | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.8-flash | 7932 | 2079 | gemini:gemini-3.8-flash | 9864 | 19237 | 15 survey(s), 15 genotype, 0 bioassay, 0 geno-pheno rows | 0.0000 |
| 2015_Lee_Peer_Review_Report_Absence_Kdr_DOI_10_5256_f1000research_7052_r8980 | master | EXTRACTED | True | high | low | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.8-flash | 7932 | 1868 | gemini:gemini-3.5-flash | 9733 | 17797 | 15 survey(s), 15 genotype, 0 bioassay, 0 geno-pheno rows | 0.0000 |
| 2015_Obala_What_Threatening_Effectiveness_Insecticide_Treated_PMID26171962 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 11052 | 1257 |  |  |  |  | 0.0000 |
| 2015_Sutherland_Transcriptomic_Responses_Emamectin_Benzoate_Pacifi_PMID25685190 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 10332 | 873 |  |  |  |  | 0.0000 |
| 2015_Wilson_Urban_Malaria_Understanding_Epidemiology_Ecology_PMID26259941 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.7-flash | 8972 | 1347 |  |  |  |  | 0.0000 |
| 2016_Bradley_Cluster_Randomized_Trial_Comparing_Deltamethrin_PMID27448667 |  | NAME_COLLISION |  |  |  |  |  | 2026-10-16 |  |  |  |  |  |  |  |  |  | 2 files share this name (in: master) — rename so each is unique | 0.0000 |
| 2016_Lynch_Evolution_Generate_Sustainable_Malaria_Control_PMID27776220 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.6-flash | 17812 | 1801 |  |  |  |  | 0.0000 |
| 2016_Randriamaherijaona_First_Evaluation_Bendiocarb_Experimental_Huts_PMID27230626 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 7092 | 1451 |  |  |  |  | 0.0000 |
| 2016_Rinker_Disease_Vectors_Era_Next_Generation_PMID27154554 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 7632 | 1175 |  |  |  |  | 0.0000 |
| 2017_Chaccour_Ivermectin_Reduce_Malaria_Transmission_II_PMID28434405 | master | INELIGIBLE | False | high | none | False | 1 | 2026-10-17 | 2026-10-17 | 0 |  | gemini:gemini-3.8-flash | 8712 | 816 |  |  |  |  | 0.0000 |
| 2017_Djenontin_Mosquitoes_Fauna_Diversity_Plasmodium_Falciparum_DOI_10_14741_ijmcr_v_5_6_23 | master | EXTRACTION_FAILED | True | high | none | False | 1 | 2026-10-16 | 2026-10-16 | 0 |  | gemini:gemini-3.8-flash | 4352 | 1881 |  | 0 | 0 | extractor error: Server disconnected without sending a response. | 0.0000 |
| … 63 more rows |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

_The table above is a static snapshot. For a searchable, filterable view (paginated for large sets), open [`data/roster.csv`](data/roster.csv) — GitHub renders CSV files as an interactive table._

<!-- ROSTER:END -->

## How it works

**Stage 1 — eligibility.** Each new PDF is checked against the spec in
`src/eligibility.py`: *Anopheles*; ≥1 target marker (`config/target_loci.csv`);
extractable genotype counts; field-collected (F0/F1) African mosquitoes; primary
study. Sub-country location and ≤3-year time window are recorded but not required.
Papers become *eligible*, *ineligible*, or **flagged** (possible duplicate /
needs supplementary files).

**Stage 2 — extraction.** For eligible papers the LLM fills five linked tables
(`study`, `surveys`, `genotypes`, `bioassays`, `geno_pheno`). It gives **raw counts
and text as reported**, with provenance (sentence/table, page, figure, supplement)
on every record. Then code:

- maps marker names to *An. gambiae* numbering (`L1014F` → `Vgsc L995F`);
- validates the data (`src/validate.py`: RR+RS+SS = N, dead ≤ exposed, IDs link,
  markers are targets, coordinates in Africa…), sending errors back to the LLM
  for repair;
- looks up the PMID from the DOI (Europe PMC) and geocodes sites that have no
  printed coordinates (OpenStreetMap; `src/enrich.py`) — the LLM never does either;
- computes every derived value (allele/genotype frequencies, mortality, WHO
  phenotype, pyrethroid subtype…) and writes the final table
  **`data/final/ir_extraction.csv` / `.xlsx`** (`src/export.py`).

**LLM provider.** All model calls go through `src/llm.py`. The default is Google
Gemini (free tier, throttled and retried). Claude and OpenAI-compatible models
work by changing the model spec, e.g. `--model sonnet`.

## How to use it

**1. Add papers.** Upload PDFs to Google Drive → `IR_papers/master/` (or a
contributor's subfolder). Name each one uniquely, ideally `PMID_<number>.pdf` —
the name becomes the paper's ID everywhere.

**2. Start it.** GitHub's 4-hourly schedule is best-effort (often hours late), so
start a run yourself after adding papers — **Actions → Pipeline → Run workflow**,
or from a terminal in this folder (one-time: `sudo apt install gh && gh auth login`):

```bash
gh workflow run pipeline.yml                     # start (add -f max_papers=40 for big batches)
gh run watch                                     # follow it until it finishes
git pull                                         # get the results
```

Each run checks eligibility of new papers, then extracts every eligible one (15
per stage by default). The Gemini free tier allows a few dozen papers a day; when
the daily quota runs out the run stops cleanly — start another run the next day
and it continues where it stopped.

**3. Get the results.** Download **`data/final/ir_extraction.xlsx`** from the repo
(or `git pull`). One row per data point (`Record type` = genotype / bioassay /
geno_pheno), with page/table provenance for every number. Per-paper details and
the model's decisions are in `data/extracted/<id>/README.md`.

**4. Handle what needs you.** Every Friday a GitHub issue lists papers waiting on
you:
- **AWAIT_SUPPLEMENT** — upload the supplementary files to Drive →
  `IR_supplements/master/<paper id>/`; the next run picks them up.
- **REVIEW_DUPLICATE** — add `id: duplicate` or `id: unique` to
  `data/duplicate_decisions.yaml`.
- **EXTRACTION_FAILED** — see `data/extracted/<id>/EXTRACTION_FAILED.md`.

To skip a paper entirely, add its ID to `data/exclude.txt`. To re-extract a paper,
change its status in `data/roster.csv` back to `ELIGIBLE`.

**Status of every paper:** `data/roster.csv` (GitHub shows it as a searchable table).

## Running on your own computer (optional)

Edit on GitHub or `git pull` before working locally — the bot commits to `data/`
after every run. Local runs need a `.env` file with `GEMINI_API_KEY` (and the Drive
settings to use Drive); check it with `python src/check_setup.py`.

```bash
.venv/bin/python src/run_local.py papers/   # a local folder of PDFs → local_output/
```

## Checking accuracy against a gold standard

1. `.venv/bin/python src/evaluate.py --template gold.xlsx` — an empty sheet with
   the final-table columns.
2. Extract your gold papers by hand into it: one row per data point, as in the
   final table (genotype, bioassay or geno-pheno row). Leave unreported cells empty.
3. Run the pipeline on the same PDFs (`src/run_local.py gold_papers/ --skip-eligibility`), then
   `.venv/bin/python src/evaluate.py gold.xlsx local_output/final/ir_extraction.csv`.

It prints, per record type, how many of your rows were found (recall) and how
many extracted rows are real (precision), and per column how often the value is
right. Every disagreement is listed in `local_output/eval/eval_mismatches.csv`.

## What humans edit

- `config/target_loci.csv` — the target markers and their aliases.
- `data/exclude.txt` — papers to skip.
- `data/duplicate_decisions.yaml` — `duplicate` / `unique` rulings on flagged papers.
- `Human verified` / `Coordinates verified` columns are for humans only; the
  pipeline always writes `FALSE`.

## More detail

Design notes, the file and secret reference, and how Drive access works:
**[docs/NOTES.md](docs/NOTES.md)**.
