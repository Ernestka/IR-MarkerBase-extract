# Extraction record — 2018_Poda_Targeted_Application_Organophosphate_Based_Paint_PMID29609597

- Extracted: 2026-11-23
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 4 · Bioassays: 4 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Sampling**: 
   - Field collections were conducted in VK3 village, Kou Valley, southwestern Burkina Faso (11° 23′ 14″N, 4° 24′ 42″W; converted to decimal degrees: 11.387222, -4.411667) between August and December 2013.
   - Mosquitoes were identified molecularly as 100% *Anopheles coluzzii* using SINE-PCR.
   - Separate surveys were created for mosquitoes collected in control vs IP+LLIN treated house arms to accurately link genotype counts from Table 4.
   - A third survey was created for larvae-reared wild *An. coluzzii* used in WHO standard susceptibility tube tests.

2. **Markers Extracted**:
   - **Vgsc L1014F** (gene: `kdr`, marker: `L1014F`): Genotype counts (SS, RS, RR) reported in Table 4 for Control houses (n=52) and IP+LLIN treated houses (n=49).
   - **Ace-1 G119S** (gene: `ace-1R`, marker: `G119S`): Genotype counts (SS, RS, RR) reported in Table 4.
   - An inconsistency note was logged for the IP+LLIN treated group on kdr L1014F because the printed allele frequency F=0.929 slightly differs from the frequency calculated from printed counts (92/98 = 0.9388).

3. **Bioassays**:
   - Standard 1 h WHO tube susceptibility tests reported in Fig. 3 for wild *An. coluzzii* (fenitrothion 0.1%, pirimiphos-methyl 0.05%, deltamethrin 0.05%, permethrin 0.75%) were extracted. Fenitrothion and pirimiphos-methyl mortalities (100%) were stated in the text. Deltamethrin (~67%) and permethrin (~59%) mortality values were read from Figure 3.
   - Laboratory reference strain Kisumu bioassays were omitted per rules.
   - Residual efficacy cone tests and spatial bioassays evaluating the multi-component insecticide paint (Inesfly 5A IGR: chlorpyrifos + diazinon + pyriproxyfen) were omitted as they evaluate a multi-active formulation product rather than standard single-insecticide bioassays.

## Validator warnings

- genotype #3 (2018_Poda_Targeted_Application_Organophosphate_Based_Paint_PMID29609597_vk3_treated, kdr L1014F): inconsistent in the paper (values kept as printed) — Printed genotype counts (RR=44, RS=4, SS=1, N=49) yield an allele frequency of (2*44+4)/(2*49) = 92/98 = 0.9388, which differs slightly from the printed allele frequency F(L1014F) = 0.929.
