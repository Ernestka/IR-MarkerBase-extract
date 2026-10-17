# Extraction record — 2010_Yadouleton_Impact_Expansion_Urban_Vegetable_Farming_PMID21143999

- Extracted: 2026-10-17
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 6 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Survey Division and Species Identification
- Three distinct urban agricultural survey sites were studied from January to December 2009 in Benin: Houeyiho (Cotonou), Acron (Porto-Novo), and Azèrèkè (Parakou).
- Adult mosquitoes used for resistance genotyping were sampled via indoor pyrethrum spray catches (PSC) across 12 monthly visits (averaging 30 mosquitoes analyzed per month = 360 mosquitoes tested per site).
- At Houeyiho and Acron, 100% of tested An. gambiae s.l. were identified by PCR-RFLP as An. gambiae s.s. M form (now designated Anopheles coluzzii).
- At Azèrèkè, the tested An. gambiae s.l. population was a mixture (85% An. gambiae s.s. [composed of 65% S form and 35% M form] and 15% An. arabiensis). Because Table 5 presents genotypes for the site as a whole without reporting RR/RS/SS counts per molecular species or form, molecular_species is left null for Azèrèkè.

### Coordinates
- Coordinates were extracted from Figure 1 on page 3, which explicitly displays decimal degrees: Houeyiho (6.36 N, 2.41 E), Acron (6.45 N, 2.63 E), and Azèrèkè (9.31 N, 2.63 E). Page 2 also mentions coordinates in degrees and minutes (6°45'N, 2°31'E; 6°30'N, 2°47'E; 9°22'N, 2°40'E).

### Genotypes and Inconsistency Notes
- All genotype counts were extracted strictly from Table 5 (Page 7).
- The Leu-Phe kdr marker was named 'L1014F' as listed in target marker aliases.
- For kdr (L1014F), counts reconcile exactly with N = 360 at all three sites.
- For ace-1 (G119S, printed as ace-1 / ace-1R), Table 5 prints SS = 0 across all sites with RS counts of 2, 1, and 3. As instructed by extraction rule 8, the printed counts (RR=0, RS=2/1/3, SS=0) are preserved exactly as published, and the mismatch with N = 360 is documented in inconsistency_note.
- Text on page 6 mentions kdr frequencies in S (75%) vs M form (25%) at Azèrèkè, but gives no genotype counts; these percentages are not extracted as separate rows.

### Bioassays
- No insecticide susceptibility bioassays (WHO tube assays or CDC bottle assays) were performed in this study.

## Validator warnings

- genotype #2 (2010_Yadouleton_Impact_Expansion_Urban_Vegetable_Farming_PMID21143999_houeyiho, ace-1 ace-1R): inconsistent in the paper (values kept as printed) — Table 5 reports RR=0, RS=2, SS=0 for Total tested=360 (RR+RS+SS = 2 != 360). SS=0 is likely a misprint for 358 homozygous susceptible individuals, which gives an allele frequency of 2/(2*360) = 0.0028, consistent with the printed frequency 0.002 (page 6 text also mistakenly writes 0.02).
- genotype #2 (2010_Yadouleton_Impact_Expansion_Urban_Vegetable_Farming_PMID21143999_houeyiho, ace-1 ace-1R): RR+RS+SS = 0+2+0 = 2 but n_genotyped = 360
- genotype #2 (2010_Yadouleton_Impact_Expansion_Urban_Vegetable_Farming_PMID21143999_houeyiho, ace-1 ace-1R): computed allele freq 0.500 differs from reported 0.002
- genotype #4 (2010_Yadouleton_Impact_Expansion_Urban_Vegetable_Farming_PMID21143999_acron, ace-1 ace-1R): inconsistent in the paper (values kept as printed) — Table 5 reports RR=0, RS=1, SS=0 for Total tested=360 (RR+RS+SS = 1 != 360). SS=0 is likely a misprint for 359 homozygous susceptible individuals, which gives an allele frequency of 1/(2*360) = 0.0014, consistent with the printed frequency 0.001 (page 6 text also mistakenly writes 0.01).
- genotype #4 (2010_Yadouleton_Impact_Expansion_Urban_Vegetable_Farming_PMID21143999_acron, ace-1 ace-1R): RR+RS+SS = 0+1+0 = 1 but n_genotyped = 360
- genotype #4 (2010_Yadouleton_Impact_Expansion_Urban_Vegetable_Farming_PMID21143999_acron, ace-1 ace-1R): computed allele freq 0.500 differs from reported 0.001
- genotype #6 (2010_Yadouleton_Impact_Expansion_Urban_Vegetable_Farming_PMID21143999_azereke, ace-1 ace-1R): inconsistent in the paper (values kept as printed) — Table 5 reports RR=0, RS=3, SS=0 for Total tested=360 (RR+RS+SS = 3 != 360). SS=0 is likely a misprint for 357 homozygous susceptible individuals, which gives an allele frequency of 3/(2*360) = 0.0042, consistent with the printed frequency 0.004 (page 6 text also mistakenly writes 0.04).
- genotype #6 (2010_Yadouleton_Impact_Expansion_Urban_Vegetable_Farming_PMID21143999_azereke, ace-1 ace-1R): RR+RS+SS = 0+3+0 = 3 but n_genotyped = 360
- genotype #6 (2010_Yadouleton_Impact_Expansion_Urban_Vegetable_Farming_PMID21143999_azereke, ace-1 ace-1R): computed allele freq 0.500 differs from reported 0.004
