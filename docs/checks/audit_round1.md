# Independent audit

I reconstructed the reading stream from `cells` sorted by each cell’s global `order` rank, split it by the supplied verse `s/e` rank bounds, and decoded numbers 1–64 using only the wheel and sound rules in `01_HOW_TO_READ.md`. I did not use any `runs/` file or the JSON `letters`, `kn`, `ro`, or `en` fields. A written unit here is a vowel alone, a consonant followed by a vowel, or a bare consonant; following anusvāra/visarga attaches to that unit. Long verses have at least 30 such units. I normalized e/ē and o/ō, punctuation, case, and spacing, but no other sound substitutions.

Each identity is exact matches divided by published reference units in a semiglobal unit alignment (match +2, substitution −1, gap −2; free column flanks). The 1,000 controls shuffle the selected column’s units with seed 20261026 and rerun the same search; “shuffle max” is the most exact matches in one control. Identity is **not** the best ungapped substring score. C4 uses the last 80 short verses of ch.44 plus the first 80 of ch.45 to test the stated boundary; full chapter concatenation was also checked and gave the same four matches. C9 was tested in both directions and both three-verse phases; the displayed rule is the strongest one.

| Claim | Verdict | Identity | Shuffle max | Note |
|---|---|---:|---:|---|
| C1 | **CONFIRMED** | 38/43 (88.4%) | 13 | Clear passage with five nonidentical or missing units. |
| C2 | WEAK | 13/38 (34.2%) | 8 | The source has only 38 units, so the ≥40 rule cannot be met; an identifiable phrase survives. |
| C3 | WEAK | 55/82 (67.1%) | 16 | Runs across both verse types, but only 67.1% of the 82 units agree. |
| C4 | **NOT CONFIRMED** | 4/41 (9.8%) | 7 | No passage at the chapter boundary; null shuffles equal or exceed it 116/1,000 times. |
| C5 | **NOT CONFIRMED** | N/A | N/A | B3_1 is not defined by ranks or line marks in the permitted JSON; midpoint is only a proxy. |
| C6 | WEAK | 50/71 (70.4%) | 15 | The published page OCR is imperfect; its 70.4% alignment is below threshold. |
| C7 | **CONFIRMED** | 31/40 (77.5%) | 11 | The first line is divergent; the remaining run yields 31/40 exact units. |
| C8 | **CONFIRMED** | 36/41 (87.8%) | 12 | The Prakrit passage agrees at 36/41 units. |
| C9 | **CONFIRMED** | 53/57 (93.0%) | 14 | Requires reading upward and reversing alternate groups of three (phase 1). |
| C10 | WEAK | 177/275 (64.4%) | 55 | The scanned print has marked and uncertain letters; my transcription yields 64.4%, not confirmation. |

The brief’s CONFIRMED rule requires at least 75% exact identity across at least 40 reference units and a score above every shuffle. All scored claims except C4 exceed their shuffle maximum; that alone does not confirm the textual identity. “WEAK” marks a recognizable passage that misses the identity or length threshold. C5 cannot be scored under the permitted inputs.

## Side-by-side evidence

Cells are aligned **written units**. `—` is an insertion/deletion, not a guessed letter. The grid text is shown without post hoc correction. Each section links its independently downloaded comparison source.

### C1 — Gītā 12.4, ch.32 long verse ends

Reference: [IIT Kanpur Gītā 12.4](https://heritage.iitk.ac.in/SBG/12.4).

Column positions 27–71 of 109; 38/43 matches, shuffle max 13 (0/1,000 controls reached the observed score).

| Grid sounds | Published sounds |
|---|---|
| `n·ni·ya·raṃ·yē·n·d·ri·ya·g·rā·ma·daṃ·sa·r·va·t·ra·sa·ma` | `saṃ·ni·ya·m·ye·n·d·ri·ya·g·rā·—·maṃ·sa·r·va·t·ra·sa·ma` |
| `bu·d·dha·ya·yḥ·tē·p·rā·p·nu·va·n·ti·mā·mē·va·sa·r·va·bhū` | `bu·d·dha·—·yaḥ·te·p·rā·p·nu·va·n·ti·mā·me·va·sa·r·va·bhū` |
| `ta·hi·tē·ra·tā` | `ta·hi·te·ra·tāḥ` |

### C2 — Gītā 1.4, ch.16 short verse ends

Reference: [IIT Kanpur Gītā 1.4](https://heritage.iitk.ac.in/SBG/1.4).

Column positions 13–56 of 227; 13/38 matches, shuffle max 8 (0/1,000 controls reached the observed score).

| Grid sounds | Published sounds |
|---|---|
| `da·t·r·ka·ś·rā·ma·h·e·ṣ·v·?·s·e·n·m·a·s·śa·mā` | `a·t·—·ra·śū·rā·ma·—·he·ṣ·—·vā·sā·bhī·mā·r·ju·na·sa·mā` |
| `yu·dhī·yu·yu·dhā·nō·vu·vi·r·?·n·yā·g·ṭ·b·ta·da·vā·ś·c` | `yu·dhi·yu·yu·dhā·no·—·vi·—·rā·ṭa·ś·ca·d·ru·pa·da·—·ś·ca` |
| `ba·d·r·ś` | `ma·hā·ra·thaḥ` |

### C3 — Gītā 11.51–52, ch.24 all verse ends

Reference: [IIT Kanpur Gītā 11.51](https://heritage.iitk.ac.in/SBG/11.51) and [11.52](https://heritage.iitk.ac.in/SBG/11.52).

Column positions 184–282 of 436; 55/82 matches, shuffle max 16 (0/1,000 controls reached the observed score).

| Grid sounds | Published sounds |
|---|---|
| `r·ṣ·ṭ·vē·da·m·mā·nu·ṣa·m·rū·pa·m·ta·va·s·va·m·ya·m` | `dṛ·ṣ·ṭ·ve·—·daṃ·mā·nu·—·ṣaṃ·rū·—·paṃ·ta·va·—·sau·m·—·yaṃ` |
| `ja·nā·ā·r·dha·na·mi·dā·ni·ma·s·mi·sa·m·v·ru·t·ta·ha·sa` | `ja·nā·—·r·da·na·i·dā·nī·ma·s·mi·—·—·saṃ·vṛ·t·—·taḥ·sa` |
| `cē·tā·h·p·ra·k·ru·ti·m·ga·ta·ha·ṣa·du·r·da·r·śa·mi·da` | `ce·—·tāḥ·p·ra·—·—·kṛ·tiṃ·ga·—·taḥ·su·du·r·da·r·śa·mi·—` |
| `m·rū·pa·m·d·ru·ṣ·ṭ·vā·na·si·ya·n·ma·ma·dē·va·a·p·ya` | `daṃ·rū·—·—·paṃ·dṛ·ṣ·ṭa·vā·na·si·ya·n·ma·ma·de·vā·a·p·ya` |
| `s·ya·rū·p·s·ya·ni·t·ya·m·da·r·śa·na·kā·ñ·k·ṇa·ha` | `s·ya·rū·pa·s·ya·ni·t·—·yaṃ·da·r·śa·na·kā·ṅ·k·ṣi·ṇaḥ` |

### C4 — Jinasahasranāma 80, ch.44–45 short verse starts

Reference: [Jinasena Jinasahasranāma](https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html).

Column positions 39–82 of 160; 4/41 matches, shuffle max 7 (116/1,000 controls reached the observed score).

| Grid sounds | Published sounds |
|---|---|
| `gu·ru·tu·ṣ·pu·da·ṃ·ta·r·pū·ru·ma·va·ru·baṃ·ō·ṣa·t·tu·gaṃ` | `su·gho·ṣaḥ·su·mu·khaḥ·sau·m·yaḥ·su·kha·daḥ·su·hi·taḥ·su·hṛ·t·—·su` |
| `du·ai·ḷṃ·gu·ru·vaṃ·n·ra·vaṃ·ka·p·rṃ·ga·ṃ·vāṃ·a·ru·hṃ·ḷ·dē` | `gu·p·to·gu·—·p·ti·bhṛ·d·go·p·—·tā·lo·kā·dh·ya·k·ṣo·da` |
| `ōṃ·na·va·mū` | `mī·ś·va·raḥ` |

The displayed best alignment is away from a recognizable boundary phrase; the actual ch.44/ch.45 join reads `aiḷṃguruvaṃnravaṃkaprṃgaṃvāṃaruhṃḷdēōṃnavamūremūrṃṭuevavāṣararnavamūlnāre`. The three-verse serpentine variants also fail.

### C5 — Jayadhavalā praise 8, ch.31 band B3_1

Reference: [Jayadhavalā quotation in Pārśvābhyudayam introduction](https://jainqq.org/booktext/Parshvabhyudayam/090345).

| Grid (middle-unit proxy; **not** B3_1) | Published opening |
|---|---|
| `pākliamōghadiṇitrāvihidvadajārayalriraguṇnuyaravikānakpdaliyaevāadākalrpēḍamana` | `amoghavarṣa-rājendra … prājya-rājya-guṇodayā …` |

The allowed JSON has no line break or insertion-band flags. I tried the first unit and the middle unit of each long verse. The middle-unit proxy contains `amōgha` but cannot identify the **first inserted** unit of line 3; varying the index per verse would fit the target by construction. No valid identity or shuffle control is possible. The linked print is an OCR quotation with variant order/spelling.

### C6 — Uttarapurāṇa 281, ch.33 long verse ends

Reference: [Uttarapurāṇa scan, p.454](https://jainqq.org/explore/002728/454).

Column positions 33–108 of 109; 50/71 matches, shuffle max 15 (0/1,000 controls reached the observed score).

| Grid sounds | Published sounds |
|---|---|
| `āṃ·bhā·bhā·sa·bhū·n·mu·ra·ri·pu·saḥ·k·ru·ta·sa·phaṃ·ni·dhā·nā·ś` | `ta·s·mā·da·bhū·n·mu·ra·ri·—·—·puḥ·kṛ·ta·—·du·niṃ·dā·nā·—` |
| `ca·k·rē·ś·va·rō·ha·ta·vi·ru·d·dha·ja·rā·dhi·sa·—·nāṃṃ·dha·kḥ` | `ca·k·re·ś·va·ro·ha·ta·vi·ru·d·dha·ja·rā·di·sa·n·dhaḥ·dha·—` |
| `ha·r·mō·d·bha·vā·da·nu·bha·va·n·su·kha·du·bhīḥ·kha·ma·s·mā·n` | `—·r·mo·d·bha·vā·da·nu·bha·va·n·—·ba·hu·duḥ·kha·ma·s·mā·—` |
| `ni·r·ga·t·ya·tī·r·tha·k·ru·da·na·r·tha·vi·ghā·—·—·—·tā` | `ni·r·ga·s·ya·tī·r·tha·—·kṛ·da·na·r·tha·vi·ghā·ta·kṛ·t·saḥ` |

### C7 — Nirvāṇa-bhakti gāthā 2, ch.34 long verse starts

Reference: [Prakrit Nirvāṇa-bhakti](https://encyclopediaofjainism.com/निर्वाण_भक्ति/).

Column positions 39–79 of 108; 31/40 matches, shuffle max 11 (0/1,000 controls reached the observed score).

| Grid sounds | Published sounds |
|---|---|
| `i·la·k·kha·ṇa·jā·sā·dā·a·ma·rā·su·ra·va·n·di·dā·dhu·da·ki` | `vī·saṃ·tu·ji·ṇa·viṃ·ra·dā·a·ma·rā·su·ra·—·vaṃ·di·dā·dhu·da·ki` |
| `lē·sā·sa·m·mē·dē·gi·ri·si·ha·rē·ṇi·v·vā·ṇa·ga·yā·ṇa·mū·tē` | `le·sā·sa·m·me·de·gi·ri·si·ha·re·ṇi·v·vā·ṇa·ga·yā·ṇa·mo·te` |
| `si` | `siṃ` |

### C8 — Samayasāra 18, ch.37 long verse starts

Reference: [Samayasāra gāthā 18](https://nikkyjain.github.io/jainDataBase/shastra/01_%E0%A4%A6%E0%A5%8D%E0%A4%B0%E0%A4%B5%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%A8%E0%A5%81%E0%A4%AF%E0%A5%8B%E0%A4%97/01_%E0%A4%B8%E0%A4%AE%E0%A4%AF%E0%A4%B8%E0%A4%BE%E0%A4%B0--%E0%A4%95%E0%A5%81%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%95%E0%A5%81%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BE%E0%A4%9A%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF/html/020-021.html).

Column positions 50–90 of 108; 36/41 matches, shuffle max 12 (0/1,000 controls reached the observed score).

| Grid sounds | Published sounds |
|---|---|
| `va·ṃ·hi·jī·va·rā·yā·ṇā·da·v·vō·ta·ha·yaṃ·sa·d·da·hē·da·v` | `e·vaṃ·hi·jī·va·rā·yā·ṇā·da·v·vo·ta·ha·ya·sa·d·da·he·da·v` |
| `ō·a·ṇu·sa·ri·da·v·vō·ya·pu·ṇō·so·cē·va·du·mō·k·kha·kā·mē` | `vo·a·ṇu·ca·ri·da·v·vo·ya·pu·ṇo·so·ce·va·du·mo·k·kha·kā·me` |
| `ṇa` | `ṇa` |

### C9 — ch.1 verse 80 in ch.26 short verse starts

Reference: ch.1 verse 80 recomputed from `site/dist/data/ch01.json`.

Column positions 188–243 of 249; 53/57 matches, shuffle max 14 (0/1,000 controls reached the observed score).

| Grid sounds | Published sounds |
|---|---|
| `ma·re·ti·ha·dē·hā·bhi·mā·na·dō·ḷ·—·dh·yā·t·ma·sa·ra·mā·le` | `ma·re·ti·ha·dē·hā·bhi·mā·na·do·ḷ·a·dh·yā·t·ma·sa·ra·mā·le` |
| `yō·ḷ·—·ba·n·dha·ka·ra·ge·a·ra·ha·n·ta·rū·pi·na·d·r·v` | `yo·ḷ·u·ba·n·dha·ka·ra·ge·a·ra·ha·n·ta·rū·pi·na·d·r·v` |
| `yā·ga·ma·tā·v·ya·si·ri·yi·ra·pa·si·d·dha·bhū·va·la·ya` | `yā·ga·ma·kā·v·ya·si·ri·—·r·pa·si·d·dha·bhū·va·la·ya` |

The ch.1 reference comes directly from raw ranks of its verse labelled “Verse 80”. Downward/phase-0 gives 9/57; upward/phase-0 gives 20/57; downward/phase-1 gives 9/57; upward/phase-1 gives 53/57.

### C10 — printed Śrutāvatāra 1–5, ch.49→47 fifth-from-end up

Reference: [Editors’ Śrutāvatāra page](https://jainqq.org/explore/023254/496/).

Column positions 35–314 of 321; 177/275 matches, shuffle max 55 (0/1,000 controls reached the observed score).

| Grid sounds | Published sounds |
|---|---|
| `da·r·va·j·ña·vā·ṇi·—·da·tō·sa·ga·ja·ma·ta·kāṃ·ne·dha·—·ma` | `sa·r·va·—·—·vā·ṇi·yu·da·—·yā·ga·—·ma·kā·v·ya·dha·r·ma` |
| `n·sā·mā·n·ya·vi·sē·ṣa·sa·r·va·ya·va·vā·t·ma·ne·sa·de·saṃ` | `—·sā·mā·n·ya·vi·śe·ṣa·sa·r·va·s·va·vā·t·ma·ne·n·de·nu` |
| `va·ś·ru·ta·da·r·na·ga·r·ma·la·ga·ma·ta·?·va·la·—·rī·u` | `va·ś·ru·ta·j·ñā·na·ni·r·ma·la·ga·ṇi·ta·bhū·va·la·ya·a·u` |
| `sa·mṛ·ji·rē·n·d·r·bhō·si·l·la·sa·?·ge·mu·k·pa·d·ma·di` | `sa·ha·ji·ne·n·d·ra·a·i·l·la·sa·mā·na·mu·kha·pa·d·ma·di` |
| `śe·yi·ḷṃ·da·va·saṃ·vā·dhaṃ·ku·mē·ra·ma·di·ho·ya·va·ṇaṃ·ka·vi·du` | `śe·yi·—·n·sa·r·vā·n·ka·k·ra·ma·de·ho·sa·da·n·ka·vi·du` |
| `ṣ·ru·ō·da·ma·tā·ra·ga·ṇi·ta·da·ra·se·ṇaṃ·t·tha·ta·t·thā·ṇu` | `ś·ru·ta·da·va·tā·ra·ga·ṇi·ta·da·ra·se·ja·t·tha·ta·t·thā·ṇu` |
| `ka·v·vi·a·da·k·ṣi·ṇa·dē·a·da·di·ma·pa·dh·va·ni·yu·sā·ra` | `—·pu·vi·gha·da·k·khi·ṇa·de·śa·du·di·—·v·ya·va·ni·—·sā·r` |
| `ṇa·?·ṣe·yā·ga·ma·vi·du·ti·ka·la·śi·k·ṣe·ya·nī·a·va·?·ṇi` | `śi·k·ṣe·yā·ga·ma·vi·du·sa·ka·la·ra·k·ṣe·ya·nī·ḍu·va·ga·ṇi` |
| `tā·ra·ṣa·ra·vi·ha·śi·k·ṣa·ṇa·dā·nu·pū·r·vi·ya·—·ṇ·śa·vā` | `tā·k·ṣa·ra·vi·ha·śi·k·ṣa·ṇa·dā·nu·pū·r·vi·ya·ra·pā·ś·vā` |
| `gu·va·e·l·la·da·ya·ga·na·de·ko·ṭ·ṭu·ya·śa·ra·raṃ·tā·ma·va` | `gu·va·e·l·la·va·ya·t·na·de·ko·ṭ·ṭu·ī·śa·ra·n·tā·gu·va` |
| `tā·nu·na·śā·bhū·rā·ye·ta·n·nā·t·ma·vā·ṇi·ve·rā·ṭa·ya·yāṃ·ka` | `tā·nu·ā·śā·bhū·mi·ye·ta·—·nā·t·ma·vā·ṇi·ya·rā·śi·ya·n·ka` |
| `mā·a·hu·ṭ·p·si·da·m·ya·va·ra·n·ka·r·gi·ta·ī·gī·g·ṇi` | `ga·ḷa·hu·ṭ·ṭi·si·da·m·pā·va·da·n·ka·vā·gi·sa·ī·gī·s·vā` |
| `g·ke·ṇi·ya·?·vi·yu·ta·ru·tā·va·tā·—·ra·sā·nu·ja·va·mā·ri` | `ga·vā·ṇi·ya·ka·vi·ya·ś·ru·tā·va·tā·r·a·va·nu·a·va·ta·ri` |
| `dhā·r·t·dū·ka·bhā·ta·śē·va·tā·gi·r·ā·sa·vi·ya·m·ś·ga·ṇa` | `si·r·du·a·na·n·ta·t·va·tā·gi·ri·ya·sa·vi·ya·n·ka·ga·ṇa` |
| `ne·ya·pa·da·vu` | `ne·ya·pa·da·u` |

The comparison transcription is in `sources/srutavatara_1_5_transcription.txt`, made from the downloaded page image. Asterisks and crowded Kannada-in-Devanagari letters introduce uncertainty. Even giving this visible five-verse reading a semiglobal alignment, the result stays below 75%.

## Downloaded reference checksums

SHA-256 hashes are of the exact downloaded bytes retained under `sources/`. The ch.1 comparison for C9 is a permitted raw grid, not a web edition.

| Local file | SHA-256 | URL |
|---|---|---|
| `gita_12_4.html` | `9011cdd22887f15532d66131f7d8fa4a02e0f894eec6798acee5a46591b3f15d` | https://heritage.iitk.ac.in/SBG/12.4 |
| `gita_1_4.html` | `ba1d5a0ecd11fa6f6752660c24c066ca0fb3588ad0a44cbb3112e17e4236c4a8` | https://heritage.iitk.ac.in/SBG/1.4 |
| `gita_11_51.html` | `aa39bd8dea92a68ff670742cfc298f3562e843ee52154633edf0f1deaf27854b` | https://heritage.iitk.ac.in/SBG/11.51 |
| `gita_11_52.html` | `f367a8ddc6b5317ccd03b2ca0cb80caeba3bc7c00faaf95315008ce2adc62a11` | https://heritage.iitk.ac.in/SBG/11.52 |
| `jinasahasranama.html` | `f5347270c66524f3435463b5de24903e21332995b5ea1d5bb2d5c6959f374ed8` | https://sanskritdocuments.org/doc_deities_misc/jinasahasranAmastotramjinasenakRRitam.html |
| `uttarapurana_p454.html` | `82c9076dcd90a0dab4737a44bd93c755e2700034758440a9557d8469860a167b` | https://jainqq.org/explore/002728/454 |
| `parshvabhyudayam.html` | `2a1ef70ae991a26a8c26f69edd1e5a6eaed6b7ac5874d4c0657b7c2323c0ace6` | https://jainqq.org/booktext/Parshvabhyudayam/090345 |
| `nirvana_bhakti.html` | `51ecd61509d0714d92a8739cb807a393bdc260464b6861db993e1bfffd8d9347` | https://encyclopediaofjainism.com/निर्वाण_भक्ति/ |
| `samayasara_gatha18.html` | `1cdb7234413a779f6567fdca80bf13b014bb22c7fe73c792182924f570d86a99` | https://nikkyjain.github.io/jainDataBase/shastra/01_%E0%A4%A6%E0%A5%8D%E0%A4%B0%E0%A4%B5%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%A8%E0%A5%81%E0%A4%AF%E0%A5%8B%E0%A4%97/01_%E0%A4%B8%E0%A4%AE%E0%A4%AF%E0%A4%B8%E0%A4%BE%E0%A4%B0--%E0%A4%95%E0%A5%81%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%95%E0%A5%81%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BE%E0%A4%9A%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF/html/020-021.html |
| `siribhuvalaya_p496.html` | `8d018450d056124ba5515dd9c33aee907db56e4a2be63c94ea0a167379682d68` | https://jainqq.org/explore/023254/496/ |
| `siribhuvalaya_p496.jpg` | `a575a6e8be7a02cbb60094a31bf30c00696cb56abea7a63f9d75d520c05cce7d` | https://s3.us-east-2.wasabisys.com/jainqq-hq/b2c64bdc27647ab79f1980f02f5c0d9f022f50fcccae18c0b0c8af6cd5ea48de.jpg |

## Reproduction

`python3 reports/independent_audit/run_audit.py` reruns every scored claim. `audit.py` contains the grid decoding, alignment, and shuffle procedures. C10 uses `sources/srutavatara_1_5_transcription.txt`; all numerical results are saved in `RESULTS.json`. `make_report.py` renders this document from those saved measurements.
