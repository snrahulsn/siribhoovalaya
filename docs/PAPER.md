# Reading the Siribhūvalaya by machine: observations, methods, and an invitation to check them

Rahul Natarajan, independent researcher

Draft v3, 15 November 2026. Not peer reviewed.

---

## Abstract

The Siribhūvalaya is a Kannada Jain poem written entirely in numbers. Each of its 1,268 surviving pages is a grid of 27 by 27 cells, and each cell holds a number from 1 to 64 that stands for one sound. This paper reports what we observed when we read every page with machines, and exactly how we did it, so that others can repeat or refute each step.

1. The reading walk can be recovered from the raw numbers alone, by choosing the order in which neighbouring numbers are most predictable. It is found, up to its direction, in 50 of the 52 block-read chapters. The key is found too in 28 of them.
2. Hidden texts appear down the edges of the verses. Read down a chapter, the first, last or second-to-last letter of each verse spells passages from known works. 67 passages pass four fixed checks, including 42 from the Bhagavad Gītā and 13 from Jinasena's Jinasahasranāma.
3. The same full search was run 20 times on shuffled data. Real data gives 46 matches (36 distinct verses) at 75 % letter identity or better; no shuffled search gives any, and the best shuffled match reaches 36 %.
4. Several popular claims did not survive testing, including running text in Tamil or Telugu and a temple-shaped figure said to spell the author's name.

All data and code are public. We ask readers to try to break these results.

## 1. The object

Each page of the poem is a grid of 729 numbers. A number stands for one sound of Kannada: a vowel, a consonant, or a sign. The numbers are not read row by row. In most chapters the grid is cut into nine blocks of 9 by 9. Each block is read along a fixed diagonal walk that wraps around its edges, and a small key gives the order of the nine blocks. Seven chapters (1, 18, 19, 27, 36, 55 and 59) are read along a single path across the whole page instead.

This reading method was worked out in the 1950s by Yellappa Shastri, Karlamangalam Srikantaiah and K. Ananthasubba Rao. They printed chapters 1 to 33 in 1953 and 1955. A copyist of the same period wrote out chapters 34 to 59 by hand, and a note in the papers dated 16 March 1956 says those chapters "are not printed". Aruhant Mehta published the reading path as computer code in 2025.

## 2. Data

- **Chapters 1 to 8**: numbers taken from the editors' printed number sheets (85 sheets).
- **Chapters 9 to 59**: numbers transcribed by machine from scans of the manuscript papers held by the National Archives of India. Each page was read twice by separate readers, and cells where they disagreed were read again. About 0.4 % of cells could not be read with confidence. These are marked unknown, not guessed. Two outside checks compared about 420 cells with the scans and found no errors.
- **Reference texts**: public digital editions. The Gītā is the GRETIL edition, with 700 numbered verses. The Jain hymns and Jinasena come from public web editions. Every file is recorded with its URL and SHA-256 hash.

The scans themselves are not reproduced, because permission from the archive is pending. Everything derived from them is released.

## 3. Reading the numbers

**How we do it.** A wrong reading order turns a page into noise, and the right one turns it into language. Language has a simple fingerprint: some sounds follow others far more often than chance. In the right order, the next number is easier to predict from the one before.

We use that as the test. Inside a 9 by 9 block there are 3,888 possible wrapping walks, given every start cell, every step direction and every break step. For each walk we read every block of a chapter and measure how predictable each number is from the one before (the conditional entropy). We keep the walk with the lowest value.

The block key is found the same way. For every pair of blocks we score how well the end of one runs into the start of the other, across all pages of the chapter. We then take the order of the nine blocks with the best total.

**What we observed.** Of the 52 chapters read block by block, the blind test picks the editors' walk and the stored key in 28. In 20 more it picks the editors' walk run backwards, which scores within 0.005 bits of the forward walk; the measure cannot tell the two directions apart, so the direction has to be settled some other way. In chapters 26 and 38 the walk is right and the key is wrong. In chapters 45 and 50 the test picks a different walk. The seven whole-page chapters fail, as they should, because they do not use blocks. Once the walk and key are fixed, the text of chapters 34 to 59 agrees with the copyist's handwritten version, and the reading path agrees cell for cell with Mehta's code.

**What this does not show.** Inside one page, a wrong key scores almost as well as the right one, because the key only reorders whole blocks. The key is decided by the joins between blocks, which is a much weaker signal than the walk. Readers should check the key for each chapter rather than trust one success.

## 4. Hidden texts

**The claim.** The 1950s editors said the poem hides other works inside its verses. A letter from the same place in each verse, read through a chapter, would spell a second text. Srikanta Sastri wrote about Gītā strands in 1955, and Sudharthi of Hassan later published books on them. We have not been able to obtain those books, so we do not know which passages they already found. We claim priority for none.

**How we do it.**

1. *Columns.* For each chapter, take one letter from each verse, read in verse order:
   - the first, second or third letter (S1–S3), or the last, second-to-last or third-to-last letter (E1–E3);
   - from all verses, only long verses (30 or more letters), or only short ones;
   - read down the chapter or up it.
2. *Alignment.* Compare each column with each reference verse using a standard alignment: match +2, mismatch −1, gap −2. The column may start and end anywhere, but the whole reference verse must be covered. Identity is the number of matching letters divided by the length of the reference verse.
3. *Four checks.* A passage counts only if all four hold:
   - separate code, written without access to earlier results, rebuilt it from the raw numbers;
   - identity is at least 75 % over at least 40 letters;
   - it beats all 1,000 shuffles of its own column;
   - it beats all 1,000 other verses of the same length from the same source.

**What we observed.** 67 passages pass all four checks.

| Source | Passages | Distinct verses | Chapters |
|---|---:|---:|---|
| Bhagavad Gītā | 42 | 34 | 15–35 |
| Jinasena, Jinasahasranāma | 13 | 13 | 34, 43–47 |
| Caityabhakti (Sanskrit) | 4 | 4 | 51, 56, 58 |
| Nirvāṇabhakti (Prakrit) | 3 | 3 | 33–35 |
| Śāntibhakti (Sanskrit) | 2 | 2 | 53, 57 |
| Samādhibhakti (Sanskrit) | 1 | 1 | 50 |
| Amitagati, Sāmāyikapāṭha | 1 | 1 | 57–58 |
| Kundakunda, Samayasāra | 1 | 1 | 37 |

Seven Gītā verses appear in more than one chapter: 2.50, 3.11, 3.21, 3.30, 4.9, 11.28 and 14.25.

Here are two examples. In chapter 25, the second-to-last letters read up the chapter give Gītā 14.25 with 39 of 42 letters correct; the best of 1,000 shuffles gets 11. In chapter 32, the last letters of the long verses read down the chapter give Gītā 12.4 with 37 of 44 correct; the best shuffle gets 13.

Two further observations fall short of the four checks and are reported as weak:

- five verses that the editors headed "Śrutāvatāra", read upward through chapters 49 to 47 (64 % identity against the noisy print);
- 467 rows that beat every shuffle but miss the length or identity bar.

**The search-wide check.** Shuffling one column tests only that column. We searched many columns and many verses, so a reader should ask how good the best match would be by chance across the whole search. We therefore re-ran the complete Gītā search, 20 times, with every column shuffled. The search covered 1,800 columns (chapters 10–59, S1–S3 and E1–E3, three verse groups, two directions) against every one of the 636 Gītā verses of 40 letters or more, which is 1,144,800 comparisons each time.

| | Pairs at ≥ 75 % identity | Best identity |
|---|---:|---:|
| Real columns | 46 (36 distinct verses) | 93 % |
| 20 shuffled searches | 0 in every run | 36 % (highest of all 20) |

The shuffled searches never come near the bar. This is the single result we most want others to attack.

**The poem copies itself.** Some hidden columns carry the poem's own earlier verses rather than outside works:

- The first letters of the short verses of chapter 26, read in groups of three, give chapter 1, verse 80, with 93 % identity.
- The last letters of chapter 24, read upward, match the second-to-last letters of chapter 27, with 89 % identity.

Both pass the same four checks.

**The poem counts its own cells.** Two verses state numbers that are exact multiples of a page:

- chapter 3, verse 173 gives 7,290, which is 10 × 729;
- chapter 17, verse 268 gives 10,935, which is 15 × 729.

**The copyist's marks.** In chapters 42 to 59, the 1950s copyist set some letters apart on his pages. The marked letters are in non-random order in all 18 chapters tested. This is a signal in the layout. It does not show that the marked letters form texts.

## 5. What did not hold up

- **Other languages.** The poem is often said to contain 718 languages. We searched every page and every reading direction we could define for running text in 13 languages, including Tamil, Telugu, Marathi, Hindi and Pali. We found none. The search did find test passages that we had deliberately planted in the text, including 200 of 200 Tamil passages and 200 of 200 Telugu passages. Every apparent hit traced back to Sanskrit Gītā verses quoted in books in those languages. The editors printed a Telugu line and a Tamil line in one chapter, but no rule we found produces them from the numbers.
- **The temple figure.** A widely shared slide shows a temple-shaped figure laid on the first page of chapter 1, said to spell *muni kumudendu guruḥ kṛta siri bhūvalaya*. The phrase needs ḥ and ṛ, and neither sound occurs on that page. We laid the same figure on all 85 printed pages, at every position, in all eight rotations and reflections, read in both directions: 373,388 readings in all. None scored like text. The best scored 0.31 on a letter-pair measure where real text scores 0.36 or more in 95 % of cases.
- **Other reading figures.** The poem names figures such as a wheel, a lotus, a swan and a peacock as ways to read a page. We found no definition of them. We also tested a conch spiral printed in a 2021 book on all 1,268 pages: the longest shared run was 7 to 8 sounds, the same as for shuffles.
- **Withdrawn.** A passage we had earlier reported in chapter 15 failed when the separate code rebuilt it (8 of 86 letters). It is withdrawn.
- **Translation.** Our machine translations were compared with a printed Hindi meaning for 110 lines. They gave the full sense of only 2 lines. They are not results, and this paper makes no claim about the poem's meaning.

## 6. Where we may be wrong

These are the weak points as we see them. We would rather hear about them than defend them.

1. **Search size.** The search-wide check covers the Gītā only. The Jain texts were searched with similar but not identical column families, and have not had their own whole-search null.
2. **Decoys.** Decoy verses are drawn from the same source, at the same length. Because the claimed verse was the best of a search, beating the decoys is partly a selection effect. The search-wide shuffle above is the stronger control.
3. **Shuffles break structure.** A within-column shuffle destroys rhyme and repeated formulas. A shuffle that keeps those might set a higher bar. We have not built one.
4. **Not pre-registered.** Some gates were set after early results were seen. We say so rather than claim otherwise.
5. **Transcription.** About 0.4 % of cells are unknown, and the machine transcription was checked only on samples. Chapters 1 to 8 rely on the printed sheets, not the manuscript.
6. **Reference editions.** We compared against the public editions we could get, not critical editions. Some witnesses have known variant readings.
7. **Letter units.** How Kannada letters map onto Sanskrit letters (long and short vowels, nasal signs) affects identity scores. Our normalisation is in the code and can be changed.

## 7. How to check this work

- Everything is in the repository: the numbers for every page, the letter text of every chapter, every column, every alignment with the position of each letter in the grid, and the code that produces them.
- The blind walk and key test for one chapter: `python -m siritools walk 15` (about ten seconds).
- The search-wide check: `python scripts/search_null.py` (about half an hour on four cores; needs a C++ compiler).
- Rebuild and re-score every hidden passage: `python -m siritools audit`.
- Any result in this paper can be falsified by:
  - a shuffled or otherwise random search that reaches 75 % identity over 40 letters as often as the real data;
  - a transcription error that removes a passage;
  - a better reference edition that lowers a match below the bar.

Corrections and challenges can be filed as issues on the repository. We will list every successful challenge in the next version, with credit.

## Data and code

Edition: https://siribhoovalaya.com · Code and data: https://github.com/snrahulsn/siribhoovalaya

## Credits

The reading method and the text of chapters 1 to 33 are the work of Yellappa Shastri, Karlamangalam Srikantaiah and K. Ananthasubba Rao. Chapters 34 to 59 were first read by an unnamed copyist. Srikanta Sastri and Sudharthi of Hassan studied the hidden texts before us. Aruhant Mehta published the reading path as code. Anil Kumar Jain described further reading figures. The manuscript papers are held by the National Archives of India.

Transcription, analysis and drafting were done with AI models from OpenAI, Anthropic and xAI. The author directed the work and is responsible for it.
