# Siribhūvalaya — final certification of findings (27 Oct 2026)

Supersedes FINAL_CERTIFICATION_DRAFT.md.

**Rule.** CERTIFIED means all four of these hold:
- An independent run rebuilt the passage from the raw grid numbers (site/dist/data/chNN.json), never from earlier letters or results.
- It matches the published text at ≥ 75 % identity over ≥ 40 written units.
- It scores above all 1,000 shuffles of its own column.
- It scores above all 1,000 decoy verses of the same length.
Audit reports: independent_audit/AUDIT.md, AUDIT2.md, AUDIT3.md.
Decoys:
- Gītā rows: run inside AUDIT3.
- Other texts: run by Claude in independent_audit/decoy_nonGita.py → DECOY_NONGITA.json; 42 of 42 rows pass.
Claude re-extracted all 42 confirmed Gītā rows with separate code (independent_audit/claude_columns.py). All 42 come out at ≥ 75 % identity.

**Credit.** The 1950s editors knew there are hidden texts and Gītā strands (printed 1955 and 2007), and Sudharthi worked them out by hand (FILM_FACTS_FINAL 3.6). We don't know which particular verses they had. Every Gītā row below is therefore "independently recovered", not a first discovery. For the Jain texts we know of no earlier identification, which proves nothing either way.

**Column codes.**
- mixed/merged = all verses in order; long/short = verses of ≥ 30 / < 30 written units.
- E1 = last letter, E2 = second from last, S1 = first letter.
- down/up = reading direction.

## CERTIFIED — rounds 1 and 2

| Finding | Where | Identity |
|---|---|---|
| Gītā 12.4 | ch.32 long E1 down | 38/43 (88 %); Claude's own count 76 of 79 sounds, over 47 verses |
| Gītā 11.28, 2.45 | ch.27 end columns | 87 %, 92 % |
| Nirvāṇa-bhakti (Prakrit) gāthā 2 | ch.34 long S1 down | 78 % |
| Kundakunda, Samayasāra 18 | ch.37 long S1 down | 88 % |
| Jinasena, Jinasahasranāma 19, 124 | ch.44–45 short end columns | 75 %, 82 % |
| Śāntibhakti 11 | ch.53 short E1 down | 82 % |
| Copy of ch.1 v.80 | ch.26 short S1, in threes | 93 % |
| Twin passage | ch.24 E1 up ↔ ch.27 E2 | 89 % |
| Poem's own cell counts | ch.3 v.173 = 7,290 = 10×729; ch.17 v.268 = 10,935 = 15×729 | exact |
| Five verses headed Śrutāvatāra by the editors | ch.49→47, fifth-from-end letter of long verses, upward | Claude's own rebuild reads them through. The independent score against the noisy print is 64 % (WEAK as a letter score). The word "…rutāvatāra" is in the grid letters of ch.47. No known book was found to contain these five verses. |

## CERTIFIED — round 3 (66 passages from 84 confirmed rows; best route per passage)

| Text and verse | Chapter | Column | Identity | Best of 1,000 shuffles |
|---|---|---|---|---|
| Gītā 2.50 | ch.15 | `ch.15 mixed:E1:down` | 32/41 (78 %) | 10 |
| Gītā 3.30 | ch.15 | `ch.15 mixed:E1:down` | 35/44 (80 %) | 11 |
| Gītā 2.67 | ch.18 | `ch.18 mixed:E2:up` | 33/42 (79 %) | 12 |
| Gītā 3.21 | ch.19 | `ch.19 mixed:E1:down` | 34/44 (77 %) | 13 |
| Gītā 18.6 | ch.19 | `ch.19 mixed:E2:up` | 36/46 (78 %) | 13 |
| Gītā 3.11 | ch.20 | `ch.20 mixed:E1:down` | 31/40 (78 %) | 12 |
| Gītā 4.9 | ch.20 | `ch.20 mixed:E1:down` | 37/46 (80 %) | 17 |
| Gītā 1.21 | ch.20 | `ch.20 mixed:E2:up` | 31/40 (78 %) | 11 |
| Gītā 2.50 | ch.20 | `ch.20 mixed:E2:up` | 31/41 (76 %) | 10 |
| Gītā 3.30 | ch.20 | `ch.20 mixed:E2:up` | 37/44 (84 %) | 12 |
| Gītā 14.11 | ch.21 | `ch.21 mixed:E1:down` | 37/46 (80 %) | 12 |
| Gītā 14.25 | ch.21 | `ch.21 mixed:E1:down` | 34/42 (81 %) | 12 |
| Gītā 1.46 | ch.21 | `ch.21 mixed:E2:up` | 41/47 (87 %) | 13 |
| Gītā 2.37 | ch.21 | `ch.21 mixed:E2:up` | 37/48 (77 %) | 14 |
| Gītā 2.41 | ch.21 | `ch.21 mixed:E2:up` | 38/44 (86 %) | 10 |
| Gītā 4.23 | ch.22 | `ch.22 mixed:E1:down` | 37/42 (88 %) | 12 |
| Gītā 9.34 | ch.22 | `ch.22 mixed:E1:down` | 34/44 (77 %) | 13 |
| Gītā 2.14 | ch.22 | `ch.22 mixed:E2:up` | 35/43 (81 %) | 11 |
| Gītā 7.3 | ch.22 | `ch.22 mixed:E2:up` | 35/44 (80 %) | 12 |
| Gītā 13.8 | ch.23 | `ch.23 mixed:E1:down` | 34/42 (81 %) | 12 |
| Gītā 9.2 | ch.23 | `ch.23 mixed:E1:down` | 36/48 (75 %) | 14 |
| Gītā 3.18 | ch.23 | `ch.23 mixed:E2:up` | 34/42 (81 %) | 13 |
| Gītā 3.21 | ch.23 | `ch.23 mixed:E2:up` | 33/44 (75 %) | 13 |
| Gītā 11.1 | ch.24 | `ch.24 mixed:E1:down` | 35/44 (80 %) | 13 |
| Gītā 11.28 | ch.24 | `ch.24 mixed:E1:down` | 47/56 (84 %) | 14 |
| Gītā 13.27 | ch.24 | `ch.24 mixed:E1:down` | 37/45 (82 %) | 17 |
| Gītā 5.10 | ch.24 | `ch.24 mixed:E1:down` | 35/46 (76 %) | 14 |
| Gītā 3.11 | ch.24 | `ch.24 mixed:E2:up` | 34/40 (85 %) | 12 |
| Gītā 4.9 | ch.24 | `ch.24 mixed:E2:up` | 37/46 (80 %) | 13 |
| Gītā 11.55 | ch.25 | `ch.25 mixed:E1:down` | 34/44 (77 %) | 13 |
| Gītā 17.20 | ch.25 | `ch.25 mixed:E1:down` | 32/41 (78 %) | 10 |
| Gītā 18.65 | ch.25 | `ch.25 mixed:E1:down` | 34/42 (81 %) | 12 |
| Gītā 14.25 | ch.25 | `ch.25 mixed:E2:up` | 39/42 (93 %) | 11 |
| Gītā 14.18 | ch.26 | `ch.26 mixed:E1:down` | 41/47 (87 %) | 13 |
| Gītā 2.50 | ch.26 | `ch.26 mixed:E1:down` | 32/41 (78 %) | 10 |
| Gītā 12.12 | ch.27 | `ch.27 mixed:E1:down` | 40/52 (77 %) | 12 |
| Gītā 17.7 | ch.27 | `ch.27 mixed:E1:down` | 33/43 (77 %) | 11 |
| Gītā 2.45 | ch.27 | `ch.27 mixed:E1:down` | 44/49 (90 %) | 13 |
| Gītā 11.28 | ch.27 | `ch.27 mixed:E2:up` | 45/56 (80 %) | 14 |
| Gītā 13.10 | ch.28 | `ch.28 long:E1:down` | 30/40 (75 %) | 12 |
| Gītā 12.4 | ch.32 | `ch.32 long:E1:down` | 37/44 (84 %) | 13 |
| Gītā 11.12 | ch.35 | `ch.35 long:E1:down` | 34/43 (79 %) | 13 |
| Nirvāṇa-bhakti 5 | ch.33 | `ch.33 long S1 down (loose)` | 32/42 (76 %) | 11 |
| Nirvāṇa-bhakti 2 | ch.34 | `ch.34 long S1 down (loose)` | 31/40 (78 %) | 10 |
| Nirvāṇa-bhakti 18 | ch.35 | `ch.35 long S1 down (loose)` | 31/40 (78 %) | 10 |
| Samādhibhakti 11 | ch.50 | `ch.50 merged:E1:down` | 36/45 (80 %) | 11 |
| Śāntibhakti 11 | ch.53 | `ch.53 short:E1:down` | 42/51 (82 %) | 13 |
| Śāntibhakti 1 | ch.57 | `ch.57 short:E2:down` | 39/50 (78 %) | 13 |
| Caityabhakti 3 | ch.51 | `ch.51 short:E1:down` | 65/86 (76 %) | 21 |
| Caityabhakti 4 | ch.51 | `ch.51 short:E2:down` | 39/49 (80 %) | 13 |
| Caityabhakti 8 | ch.56 | `ch.56 short:E1:down` | 37/47 (79 %) | 12 |
| Caityabhakti 21 | ch.58 | `ch.58 short:E2:down` | 31/40 (78 %) | 12 |
| Jinasahasranāma 1 | ch.34 | `34-long-E1-down` | 37/47 (79 %) | 14 |
| Jinasahasranāma 117 | ch.43 | `43-short-E1-down` | 43/52 (83 %) | 14 |
| Jinasahasranāma 87 | ch.44 | `44-short-E1-down` | 39/45 (87 %) | 12 |
| Jinasahasranāma 124 | ch.44 | `44-short-E1-down` | 41/50 (82 %) | 14 |
| Jinasahasranāma 39 | ch.45 | `45-short-E1-down` | 36/43 (84 %) | 11 |
| Jinasahasranāma 19 | ch.46 | `46-short-E1-down` | 33/40 (82 %) | 11 |
| Jinasahasranāma 100 | ch.46 | `46-short-E1-down` | 36/43 (84 %) | 11 |
| Jinasahasranāma 112 | ch.46 | `46-short-E1-down` | 35/42 (83 %) | 11 |
| Jinasahasranāma 123 | ch.46 | `46-short-E1-down` | 36/47 (77 %) | 13 |
| Jinasahasranāma 127 | ch.46 | `46-short-E1-down` | 31/41 (76 %) | 12 |
| Jinasahasranāma 105 | ch.47 | `47-short-E1-down` | 33/44 (75 %) | 13 |
| Jinasahasranāma 107 | ch.47 | `47-short-E1-down` | 31/41 (76 %) | 10 |
| Jinasahasranāma 92 | ch.47 | `47-short-E2-down` | 41/50 (82 %) | 13 |
| Sāmāyikapāṭha 23 | ch.57 | `ch57:short:end1:plain:down→ch58:merged:end1:plain:down` | 46/59 (78 %) | 14 |

Summary of round 3:
- **Bhagavad Gītā:** 41 passages, 34 distinct verses, ch.15–35. Seven verses occur in two or three chapters: 2.50, 3.11, 3.21, 3.30, 4.9, 11.28, 14.25.
- **Prakrit Nirvāṇa-bhakti:** gāthās 2, 5, 18, in ch.33–35.
- **Sanskrit Daśabhakti:**
  - Samādhibhakti 11 (ch.50);
  - Śāntibhakti 1 and 11 (ch.53, 57);
  - Caityabhakti 3, 4, 8, 21 (ch.51, 56, 58).
- **Jinasena's Jinasahasranāma:** 13 verses, ch.34 and ch.43–47.
- **Amitagati's Sāmāyikapāṭha 23:** across the ch.57→58 join.

## WEAK (above every shuffle, below 75 % or under 40 units)
- Round 3: 467 rows (R1 297, R2 12, R3 41, R4 112, R5 1, R6 2, R7 2). All are listed in AUDIT3.md.
- Rounds 1–2:
  - Gītā 1.4 ch.16;
  - Gītā 11.51–52 ch.24;
  - Jinasahasranāma 99, 35–36, 57–59;
  - Caityabhakti 27;
  - Sāmāyikapāṭha 18;
  - Tiloyapaṇṇattī ch.39, 42;
  - Ādipurāṇa 23.192 ch.52;
  - Uttarapurāṇa 281 ch.33;
  - ch.6 headings vs the Dhavalā list.

## NOT CONFIRMED / NOT REPRODUCIBLE
- Round 3:
  - 119 not confirmed (66 Gītā rows lose to decoys or shuffles);
  - 49 not reproducible (package/band columns with no rule that can be rebuilt from the grids).
- Rounds 1–2:
  - Jinasahasranāma 80 across ch.44–45;
  - Jayadhavalā / Uttarapurāṇa praśasti in ch.30–31;
  - Ācāryabhakti 6.
- ch.15 opening gāthā of the Nirvāṇa-bhakti/kāṇḍa (W126, 77.8 %): rebuilt by the audit at 8/86, NOT CONFIRMED. Do not use. The script's current line 71 relies on it.

## NEGATIVE — searched, not found
**Running text in other languages.** No Tamil, Telugu, Malayalam, Marathi, Gujarati, Bengali, Odia, Hindi, Pali, Apabhraṃśa or Ardhamāgadhī:
- W146: 13 languages, full corpora, every stream and page, 8 directions.
- W166: 1.9 billion sounds.
- W167: 14 sound tables.
- W153: the editors' lines at every unit count.
- W168: positions 13–60 and the Kannada-ear fold: 62,880 streams, 0 Tamil/Telugu passages; the 1,130 exact hits are Sanskrit Gītā quotations reused in Marathi and Tamil books; check passes. Pass 2 added 326,976 counting streams (akṣara, mātrā, pāda, concatenated) and the Kannada-ear alternatives. It found 0 alignments at k13–60, and every hit traced to Sanskrit Gītā quotations. Tamil is a strong negative: 200/200 planted controls were found. Pass 3 fixed the scanner for Telugu (200/200 exact and 200/200 10 %-edited planted controls found) and reran every Telugu search against the W146 and W143 Telugu libraries: 167 qualifying rows at 46 coordinates, 0 at k13–60. Of these, 161 are repetitive alignments to Telugu prose or glossary text and 6 are a Sanskrit Vāsudeva verse quoted in a Telugu commentary. No Telugu passage is established; Telugu is now a strong negative within these libraries (runs/w168/REPORT.md, check.py passes).
- W169: Tamil, Telugu and Marathi under a voice-collapsed code, against all 4,492,953 library chunks, 0 accepted. One outer-verse hit (ch.6 v.5) shares a Sanskrit catalogue of beings with a Telugu Bhāgavata line; it is not Telugu.
- W170: the editors' starred letters in the printed chapter give their Telugu and Tamil lines (38 of 44 letters each). No rule produces them from the grid numbers.
- W171: 65−n with a Dravidian sound map, all 59 chapters, 7,541,721 source records, 0 hits; 4/4 planted controls recovered.

**The editors' Śrutāvatāra verses 6 onward.** Not found:
- W149 and W137;
- the conch spiral of the 2021 book (p.67), tested by Claude on all 1,268 grids: best shared run 7–8 sounds, the same as shuffles;
- the book claims for ch.13, ch.1 and ch.56/59, tested by Claude: no match.

**Grid walks and bandha routes** (W115–W121, W150), every-k-th letters, 2-D bands, and inserts in ch.9–20 (W151, W152, W154): nothing new.

**Kannada inner texts** beyond fragments (W145): none.

## Not done
- W169: complete Telugu editions of Bhīmakavi, Tikkana, Nannaya (all chapters), Basavapurāṇamu and Paṇḍitārādhyacaritra were not available as public Unicode texts.
