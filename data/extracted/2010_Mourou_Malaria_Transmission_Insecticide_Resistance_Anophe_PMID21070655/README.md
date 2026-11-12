# Extraction record — 2010_Mourou_Malaria_Transmission_Insecticide_Resistance_Anophe_PMID21070655

- Extracted: 2026-11-12
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 9 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Extraction Decisions
1. **Surveys**: Split into 3 distinct surveys by site and species: 
   - Libreville (`camp de Gaulle`), An. gambiae s.s. (S form), collected Dec 2006 – Apr 2007.
   - Port-Gentil (`camp N'tchorere`), An. gambiae s.s. (S form), collected Feb 2007.
   - Port-Gentil (`camp N'tchorere`), An. melas, collected Feb 2007.
2. **Multi-allelic Vgsc codon 995/1014 (kdr-w and kdr-e)**: Parsed into separate rows for `kdr-w` (L1014F) and `kdr-e` (L1014S) per Rule 4b.
   - In Libreville (n = 248 successfully genotyped for kdr out of 250 tested):
     - Raw genotypes: S/S=0, S/Rw=1, S/Re=0, Rw/Rw=80, Re/Re=33, Rw/Re=134.
     - kdr-w: RR (Rw/Rw) = 80; RS (S/Rw + Rw/Re) = 1 + 134 = 135; SS (Re/Re + S/Re + S/S) = 33.
     - kdr-e: RR (Re/Re) = 33; RS (S/Re + Rw/Re) = 0 + 134 = 134; SS (Rw/Rw + S/Rw + S/S) = 81.
   - In Port-Gentil An. gambiae s.s. (n = 50 successfully genotyped for kdr out of 54 tested):
     - Raw genotypes: S/S=0, S/Rw=1, S/Re=0, Rw/Rw=21, Re/Re=3, Rw/Re=25.
     - kdr-w: RR = 21; RS = 1 + 25 = 26; SS = 3.
     - kdr-e: RR = 3; RS = 0 + 25 = 25; SS = 22.
3. **Ace-1 G280S (G119S)**: Renamed marker from `ace1` to `G119S` so it maps cleanly to target marker `Ace-1 G280S` (which lists `G119S` as an alias). Assay used is Weill et al. 2004 (ref 24).
4. **An. melas**: Text explicitly states that 96 An. melas from Port-Gentil were tested for kdr and ace-1 and all were wildtype/susceptible (0 kdr mutations, 0 ace1 mutations). Thus RR=0, RS=0, SS=96 for all three target markers.
5. **Bioassays**: No WHO or CDC insecticide susceptibility bioassays were performed in this study (only HBR, EIR, species PCR, and molecular marker assays).
