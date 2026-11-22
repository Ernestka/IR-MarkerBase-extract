# Extraction record — 2018_Lynd_Insecticide_Resistance_Anopheles_Gambiae_Northern_PMID30400885

- Extracted: 2026-11-22
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 16 · Bioassays: 16 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Sites**: Mosquito collections were carried out in March–April 2016 in three villages surrounding Gbadolite in Nord Ubangi province, Democratic Republic of Congo: Bassa, Pambwa, and Fiwa. Molecular identification via SINE PCR showed that *Anopheles gambiae s.s.* predominated across all three sites, while *Anopheles coluzzii* was detected at low frequency (N=4) in Fiwa. Four distinct survey records were created: three for *An. gambiae s.s.* (Bassa, Pambwa, Fiwa) and one for *An. coluzzii* (Fiwa).

2. **Markers Extracted**: 
   - **Vgsc L1014F (L995F)** and **Vgsc L1014S (L995S)**: Extracted from Table 2. Because codon 1014 is tri-allelic (L, F, S), separate genotype records were produced for L1014F and L1014S per survey according to Rule 4b. Raw diploid genotype counts (FF, FS, SS, LF) reported as proportions in Table 2 were converted to counts using reported total N (Bassa N=100: 79 FF, 20 FS, 1 SS; Pambwa N=92: 75 FF, 16 FS, 1 SS; Fiwa gambiae N=161: 103 FF, 47 FS, 11 SS; Fiwa coluzzii N=4: 2 FF, 2 LF).
   - **Vgsc N1575Y (N1570Y)**: Reported on page 6 text at low frequencies in Pambwa (0.01, 1 carrier out of 92), Fiwa *An. gambiae s.s.* (0.02, 3 carriers out of 161), and Fiwa *An. coluzzii* (0.25, 1 carrier out of 4); absent in Bassa.
   - **Ace-1 G119S (G280S)**: Text on page 6 explicitly confirms 0 mutant alleles out of 368 total specimens tested across all sites.

3. **Bioassays**: WHO tube bioassay results presented in Figure 1 provide sample sizes (`n_exposed`) above each bar and mortality percentages on the y-axis. `dead_alive_printed` is set to `false` and counts are left `null` as exact integer numbers of dead/alive are not printed in text or tables. Estimated mortality percentages were read from Figure 1.

4. **Genotype-Phenotype**: Phenotype association analysis is reported in text as Chi-square statistics and odds ratios, but raw genotype counts split by alive/dead mosquitoes are not printed. Thus, `geno_pheno` is empty.

5. **Validation Samples**: 172 *An. gambiae s.s.* samples from Eastern Uganda mentioned on page 4 were used for blind validation of the LNA assay; these were excluded as they represent secondary reference test samples from a separate country without granular survey details in the main text.

## Validator warnings

- genotype #15 (2018_Lynd_Insecticide_Resistance_Anopheles_Gambiae_Northern_PMID30400885_fiwa_coluzzii, Vgsc N1575Y): computed allele freq 0.125 differs from reported 0.25
