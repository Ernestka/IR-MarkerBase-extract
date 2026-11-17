# Extraction record — 2014_Nkya_Insecticide_Resistance_Mechanisms_Associated_Diffe_PMID24460952

- Extracted: 2026-11-17
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 20 · Genotype rows: 11 · Bioassays: 27 · Geno-pheno rows: 0

## Decisions

# Data Extraction Decisions

### 1. Study and Sites
Nine field populations were collected in Tanzania in 2011 across three environmental zones:
- **Urban (Dar es Salaam)**: Ilala (ILA), Temeke (TEM), Kinondoni (KIN)
- **Low pesticide (Muheza district, Tanga region)**: Zeneti (ZEN), Kilulu (KIL), Muheza estate (MUH)
- **Intense agriculture (Hai district, Kilimanjaro region)**: Rundugai (RUN), Kikafu (KIK), Kawaya (KAW)
F0 larvae were collected and reared in standard laboratory conditions to obtain F1 progeny used for both bioassays and molecular analyses.

### 2. Survey Structure and Species
- **Bioassays**: Table 3 explicitly notes that adult bioassays were performed on mixed *Anopheles gambiae sensu lato* adults. Hence, nine survey records with `species_reported: 'Anopheles gambiae sensu lato'` and `molecular_species: null` (`_sl`) were created to link the bioassay data.
- **Genotypes**: In Table 4, kdr genotyping is reported separately by molecular species (*An. gambiae s.s.* and *An. arabiensis*). Per extraction rules, separate surveys were defined for each molecular species present and genotyped (11 surveys: 2 for *An. gambiae s.s.* in ILA and KIN, and 9 for *An. arabiensis* across all nine sites). In TEM, no *An. gambiae s.s.* individuals were found/genotyped (N=0 in Table 4), so no survey was created for that species at that site.

### 3. Target Markers
- Only **Vgsc L1014S (L995S)** was detected and tabulated in Table 4. While L1014F was also screened using TaqMan qPCR, the paper reports that only L1014S was detected; no separate counts or table are provided for L1014F.
- Other candidate genes mentioned in the study (such as Ace-1 AGAP001356, CYP6P3, etc.) were investigated via transcriptomic microarrays and RT-qPCR, not target-site PCR genotyping.

### 4. Table 4 Inconsistencies
- **KIN *An. arabiensis***: Table 4 prints `LL = 7`, `LS = 0`, `SS = 0`, `S frequency (%) = 0`, `N = 79`. The value `LL = 7` does not reconcile with `N = 79` and is almost certainly a typographical error for 79. The values were preserved exactly as printed, and an `inconsistency_note` was added.
- **KIL *An. arabiensis***: Table 4 prints `LL = 79`, `LS = 1`, `SS = 0`, `S frequency (%) = 0.6`, `N = 79`. The genotype counts sum to 80 (79+1+0), but N is printed as 79. Values were preserved as printed with an `inconsistency_note`.

### 5. Bioassays
- Adult bioassays for deltamethrin (0.05%, 60 min exposure), DDT (4%, 60 min exposure), and bendiocarb (0.1%, 10 min exposure) with 24-hour mortality are reported in Table 3. Because the text states 'Four replicates of 10-25 mosquitoes were exposed' rather than printing exact counts of dead/alive, `n_exposed`, `n_dead`, and `n_alive` are left null, and `dead_alive_printed` is set to `false`, with `reported_mortality_pct` recorded.
- Larval bioassays (Table 2) reported only LC50 and RR50 across six-concentration series rather than diagnostic concentrations with mortality, so they were not extracted as discrete bioassay tests.
- Susceptible laboratory control strains (Kisumu, Ifakara) were omitted per rule 5.
- No genotype-phenotype splits were conducted.

## Validator warnings

- genotype #5 (nkya_2014_kin_ar, kdr L1014S): inconsistent in the paper (values kept as printed) — Table 4 prints LL=7, LS=0, SS=0, but N=79 and S frequency (%)=0. LL=7 is likely a typographical error for 79.
- genotype #5 (nkya_2014_kin_ar, kdr L1014S): RR+RS+SS = 0+0+7 = 7 but n_genotyped = 79
- genotype #7 (nkya_2014_kil_ar, kdr L1014S): inconsistent in the paper (values kept as printed) — Table 4 prints LL=79, LS=1, SS=0, but N=79 (sum of genotypes is 80). LL may be a typo for 78, or N a typo for 80.
- genotype #7 (nkya_2014_kil_ar, kdr L1014S): RR+RS+SS = 0+1+79 = 80 but n_genotyped = 79
