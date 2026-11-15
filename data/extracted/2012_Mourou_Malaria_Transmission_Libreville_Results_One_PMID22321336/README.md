# Extraction record — 2012_Mourou_Malaria_Transmission_Libreville_Results_One_PMID22321336

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 5 · Genotype rows: 10 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Spatial & Temporal Resolution
- Data extracted for 5 distinct districts in Libreville, Gabon: Alibandeng, Camp des Boys, Beauséjour, Sotega, and Akébé-Poteau.
- Sampling periods: March to April 2009 for Akébé-Poteau; July 2009 to January 2010 for Sotega; December 2008 to January 2010 for the remaining three districts.
- The pooled row ('Libreville-Total') was excluded per Rule 7 to avoid double-counting.

### Marker Derivations (Rule 4b for Multi-allelic codon 1014)
Table 3 reports full tri-allelic genotype classes (ReS, ReRe, ReRw, RwRw, RwS, SS) where e = kdr-e (L1014S), w = kdr-w (L1014F), S = susceptible wildtype (1014L):
- **Alibandeng (N=240)**: ReS=1, ReRe=13, ReRw=80, RwRw=146, RwS=0, SS=0 (L/L=0).
  - kdr-w (L1014F): RR=146 (RwRw), RS=80 (ReRw+RwS), SS=14 (ReRe+ReS+SS).
  - kdr-e (L1014S): RR=13 (ReRe), RS=81 (ReRw+ReS), SS=146 (RwRw+RwS+SS).
- **Camp des Boys (N=310)**: ReS=0, ReRe=18, ReRw=120, RwRw=168, RwS=2, SS=2 (L/L=2).
  - kdr-w (L1014F): RR=168, RS=122, SS=20.
  - kdr-e (L1014S): RR=18, RS=120, SS=172.
- **Beauséjour (N=138)**: ReS=0, ReRe=7, ReRw=48, RwRw=82, RwS=0, SS=1 (L/L=1).
  - kdr-w (L1014F): RR=82, RS=48, SS=8.
  - kdr-e (L1014S): RR=7, RS=48, SS=83.
- **Sotega (N=203)**: ReS=0, ReRe=15, ReRw=63, RwRw=124, RwS=0, SS=1 (L/L=1).
  - kdr-w (L1014F): RR=124, RS=63, SS=16.
  - kdr-e (L1014S): RR=15, RS=63, SS=125.
- **Akébé-Poteau (N=129)**: ReS=0, ReRe=8, ReRw=44, RwRw=77, RwS=0, SS=0 (L/L=0).
  - kdr-w (L1014F): RR=77, RS=44, SS=8.
  - kdr-e (L1014S): RR=8, RS=44, SS=77.

### Ace-1 G280S
- Text on page 7 notes: "The Ace 1 mutation was not identified in any of the 783 members of the An. gambiae complex collected in the five areas of Libreville". Because the paper names the gene/mutation only as "Ace 1" without explicit codon notation, and to satisfy schema target marker validation, these 0-carrier observations were omitted from the genotypes array and documented here in the README.

### Bioassays & Genotype-Phenotype
- No WHO/CDC bioassays were performed in this study (only mosquito collection, parasite index/EIR, and molecular genotyping). Arrays are left empty.
