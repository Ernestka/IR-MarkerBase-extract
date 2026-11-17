# Extraction record — 2015_Ndiath_Emerging_Knock_Down_Resistance_Anopheles_PMID26395241

- Extracted: 2026-11-17
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): medium
- Surveys: 4 · Genotype rows: 0 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

# Extraction Decisions for Ndiath et al. (2015) Malar J 14:364

### Study Design & Surveys
- **Longitudinal Adult Survey (2007-2010)**: Human landing catches (indoor and outdoor) were conducted across 44/45 areas in Dakar and its satellite cities (Pikine, Thiaroye, Guediawaye). 3753 *An. gambiae* s.l. were molecularly identified, comprising 3496 *An. arabiensis* (93.15%) and 257 *An. melas* (6.84%). Coordinates for Dakar (14°40′20″ N, 17°25′22″ W -> 14.6722, -17.4228) are converted from degrees-minutes-seconds.
- **Larval Surveys (2010-2012)**: Larval collections took place in August 2010, 2011, and 2012 from 10 breeding sites in three areas: Almadies, Pikine, and Yarakh. F0 adults were reared for standard WHO tube tests and synergist bioassays.

### Genotype Data
- *Vgsc* L995F (*kdr-w*) and L995S (*kdr-e*): Genotype distribution across 44 sites is presented exclusively in Figure 1 as a stacked bar chart (6 genotype classes: ReRe, ReRw, ReS, RwRw, RwS, SS). No exact numeric counts or frequency tables are printed in the main text; the numerical data reside in Additional file 1, which was not provided. Following extraction rules, raw counts cannot be accurately or reliably read from stacked bar charts without guessing integer values.
- *Ace-1* G280S: The paper notes that "All the mosquitoes genotyped and identified are An. arabiensis. None of them had the ace-1 resistant allele" (page 5) and mentions "Although a high frequency of ace1 was not found" (page 8), but the exact sample size tested for *ace-1* is not printed in the text or tables.

### Bioassay Data
- Table 1 reports exclusively knockdown kinetics (KDT50 and KDT95) for the six tested insecticides (bendiocarb, fenitrothion, lambda-cyhalothrin, deltamethrin, permethrin, DDT) across Almadies, Pikine, and Yarakh from 2010 to 2012. In accordance with Rule 8b ("If the paper reports only knockdown times (KDT50) and no mortality, skip that bioassay"), Table 1 bioassays are skipped.
- 24-hour mortality values for the bioassays (Figure 2) and synergism assays with PBO (Figure 3) are provided only as graphical line plots with overlapping error bars. Specific per-insecticide mortality percentages or dead/alive counts are not printed in the main text; full numerical values are in Additional files 2 and 4. Broad mortality ranges in the text (e.g. 42-55% in Pikine after PBO) pool across insecticides and cannot be used for individual bioassays.

### Genotype-Phenotype Data
- Dataset 2b analyzed a subset of 25 mosquitoes per site/year/insecticide split roughly evenly between alive and dead. However, results are reported only as model odds ratios from logistic regression (OR = 0.225 for EE, OR = 1418 for SS, OR = 3.192 for SW relative to SE) and predicted mortalities in Additional file 3. Raw genotype counts split by dead/alive phenotype are not printed in the text or main tables.
