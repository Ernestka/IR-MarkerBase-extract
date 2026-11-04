# Extraction record — 2015_Abeku_Monitoring_Changes_Malaria_Epidemiology_Effectiven_PMID26337671

- Extracted: 2026-11-04
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 4 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Extraction Summary
- **Surveys & Sites**: Extracted vector baseline data from two sites in Uganda (Aduku and Butemba) collected in October-November 2012. Ethiopian sites had too few vectors collected to allow for resistance/genotype testing.
- **Markers**: Extracted `kdr-L1014S` (Vgsc L995S) frequencies reported on page 10 for *An. gambiae s.s.* and *An. arabiensis*.
- **Genotype Counts**: Frequencies were reported as percentages along with `n`. In accordance with extraction rules against back-calculating genotype counts, individual RR/RS/SS counts were left `null` unless explicitly stated (e.g., 'no susceptible individuals were observed' -> SS = 0; 'all susceptible' -> SS = 7, RR = 0, RS = 0).
- **Bioassays**: No standard bioassays (WHO tube/CDC bottle) or genotype-phenotype splits were reported in this paper.

## Validator warnings

- genotype #3 (2015_Abeku_Monitoring_Changes_Malaria_Epidemiology_Effectiven_PMID26337671_aduku_gambiae, kdr L1014S): frequency only (no raw counts)
- genotype #4 (2015_Abeku_Monitoring_Changes_Malaria_Epidemiology_Effectiven_PMID26337671_aduku_arabiensis, kdr L1014S): frequency only (no raw counts)
