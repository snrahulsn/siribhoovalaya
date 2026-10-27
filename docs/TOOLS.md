# siritools: a toolkit for experimenting with the text

`siritools/` is a Python package (3.9 or later, standard library only) for reading the number grids, taking hidden-text
columns, and testing whether a match is better than chance. Everything works from the files in `data/`; nothing is
downloaded. Run it from the repository root:

```bash
python -m siritools --help
python -m siritools <command> --help
python -m unittest                      # the tests (about ten seconds)
```

Every command takes `--json`. The outputs below were produced by running the commands exactly as shown.
Set `SIRI_DATA=/path/to/data` to use another copy of the data folder.

## Concepts

- **Number.** 1-27 are vowels, 28-60 consonants, 61-64 signs; 0 means "could not be read" (`?` in `grids.csv`).
- **Written unit.** A consonant joins the vowel after it (`k` + `a` = `ka`); a consonant with no vowel after it stands
  alone (`k`); ṃ, ḥ and the two rare signs join the unit before. These are the units that were scored in the audits.
- **Cell location.** `(page, row, col)`, row and col counted from 1, the page as named in `grids.csv`.
- **Reading stream.** All numbers of a chapter in reading order (`order.csv`); a verse is a run of it (`verses.csv`).
- **Column.** One unit taken from each verse of a chapter: position `S1` is the first unit, `E1` the last, `E2` the
  second from last; group `long` means 30 units or more, `short` fewer; read `down` (first verse first) or `up`.
- **Comparison level.** `exact` (the certified level: e = ē, o = ō), `loose` (also long = short vowels, ṃ ḥ ignored),
  `strict` (as written).

## Modules

| Module | What it does |
|---|---|
| `siritools.data` | `corpus()`: pages, `stream(ch)`, `verses(ch)`, `verse_units(ch)`, `location(ch, rank)`, `unit_locations`; also `symbols()`, `readings()`, `hidden_texts()` |
| `siritools.script` | `units`, `roman`, `kannada`, `parse` / `text_units` (Roman, Devanagari or Kannada text to units), `norm` |
| `siritools.routes` | `read(ch, page, route, ...)`: a page or square along rows, columns, snake, diagonals, spirals, knight's move or custom cells |
| `siritools.find` | `find(ch)`: recover a chapter's walk and key from the raw numbers |
| `siritools.soundmap` | `test(...)`: the vowel / consonant / sign split of the 1-64 table against shuffled tables |
| `siritools.columns` | `column(ch, group, pos, dir)` with provenance; `parse_rule` turns a rule in words into columns |
| `siritools.align` | `align(column, source, level)`: unit alignment (match +2, mismatch -1, gap -2; whole source placed, column ends free) |
| `siritools.stats` | `shuffle_test`, `decoy_test`, `decoy_record`, `summary` |
| `siritools.search` | `search(query, where, chapters, level)`: a string in every stream and every column rule |
| `siritools.audit` | `audit()`: rebuild all 68 rows of `hidden_texts.csv` and compare |

```python
from siritools import data, columns, align, script
c = data.corpus()
col = columns.column(15, 'all', 'E1', 'down')          # list of Entry(text, chapter, verse, unit, locations)
src = script.text_units('yukto jahātīha')
a = align.align(col, src)                               # a.matches, a.start, a.end, a.pairs
```

## read: verses rebuilt from the numbers

`read CHAPTER [--verse N] [--kannada]` prints each verse in Roman letters; with `--verse` it also prints the numbers
and the cells of the first letters.

```
$ python -m siritools read 15 --verse 1 --kannada
15.1	Verse 1	ḷkāvydōḷujñānasāgaramathanadaākāladatiśayasukhadaśrīkālabhavanavāsigaḷādadēvanivākāladahasādiavaran
	ಳೂಕಾವ್ಯ್ದೋಳುಜ್ಞಾನಸಾಗರಮಥನದಆಕಾಲದತಿಶಯಸುಖದಶ್ರೀಕಾಲಭವನವಾಸಿಗಳಾದದೇವನಿವಾಕಾಲದಹಸಾದಿಅವರನ್
15 28 3 56 53 45 24 13 7 35 37 3 47 1 59 3 30 1 54 1 52 1 44 1 47 1 45 1 3 28 3 55 1 45 1 43 4 57 1 53 1 59 7 29 1 45 1 57 54 6 28 3 55 1 51 1 56 1 47 ...
first cells: 199:r10c5 | 199:r18c6 199:r17c7 | 199:r16c8 | 199:r15c9 | 199:r14c1 199:r13c2 | 199:r12c3 ...
```

## route: read a page along a shape

`route CHAPTER [PAGE] --route NAME [--square 1-9 | --region r,c,size] [--cells "r,c r,c ..."] [--reverse]`.
Routes: rows, columns, snake, diagonals, antidiagonals, spiral-in, spiral-out, knight, custom. PAGE is the index
within the chapter from 1 (`--page-id` takes the id used in `grids.csv`). Numbers, Roman text, Kannada and the cell of
every number come back; `--json` gives all of them in full.

```
$ python -m siritools route 15 1 --route spiral-in --square 1
chapter 15 page 199 route spiral-in region (0, 0, 9) (81 cells)
numbers : 48 52 45 59 5 1 4 16 54 1 7 56 16 4 45 45 52 47 48 56 1 1 52 0 16 52 1 4 54 47 1 24 1 7 55 43 56 60 3 1 ...
roman   : pmdsīaierauveiddmnpvaam?emairnaōaultvhāavdhknaabrevyījmmdaaḷuskhbaēagaavarsrmuessaa
kannada : ಪ್ಮ್ದ್ಸೀಅಇಎರಉವೆಇದ್ದ್ಮ್ನ್ಪ್ವಅಮ್·ಎಮಇರ್ನಓಅಉಲ್ತ್ವ್ಹಾಅವ್ಧ್ಕ್ನಅಬ್ರೆವ್ಯೀಜ್ಮ್ಮ್ದಅಳುಸ್ಖ್ಬಏಅಗಅವರ್ಸ್ರ್ಮುಎಸ್ಸಅ
cells   : r1c1 r1c2 r1c3 r1c4 r1c5 r1c6 r1c7 r1c8 r1c9 r2c9 r3c9 r4c9 ...
```

```
$ python -m siritools route 15 1 --route custom --cells "0,0 1,2 2,4 3,6" --square 5
chapter 15 page 199 route custom region (9, 9, 9) (4 cells)
numbers : 1 16 37 3 
roman   : aeñā
kannada : ಅಎಞಾ
cells   : r10c10 r11c12 r12c14 r13c16 ...
```

## walk: recover the walk and the key

`walk CHAPTER [--pages ...]` tries every walk of the form "start somewhere, keep stepping one way, step another way
when the next cell is taken" (3,888 that visit all 81 cells of a 9 x 9 square) and keeps the one that makes the
numbers most predictable; it then orders the nine squares so that each runs into the next. Only the numbers are
used; the stored reading order is printed beside the result for comparison. Takes about ten seconds for a chapter.

```
$ python -m siritools walk 15
chapter 15: 14 pages, 3888 walks tried; reading rows left to right gives 4.154 bits
  3.382 bits  start (row 0, col 4), step (-1, 1), when taken (1, 0)
  3.386 bits  start (row 8, col 4), step (1, -1), when taken (-1, 0)
  3.401 bits  start (row 1, col 3), step (1, -1), when taken (-1, 0)
key found   5 6 7 / 1 4 8 / 3 2 9
key stored  5 6 7 / 1 4 8 / 3 2 9   match: True
```

## column: one letter from each verse

`column CHAPTER [--group all|long|short] [--pos E1] [--dir down|up] [--provenance]`.

```
$ python -m siritools column 32 --group long --pos E1
k ṣu ṣā di v yaṃ da dā mi tē ca k ṣu yaḥ pa ś ya mē pa da ma k ṣa ra naṃ s a n ni ya raṃ yē n d ri ya g rā ma daṃ sa r va t ra sa ma bu d dha ya yḥ tē ...
```

With `--provenance`, one line per letter: the letter, chapter and verse, and the page, row and column of each cell of the unit (lines 85-90 shown).

```
$ python -m siritools column 15 --provenance
dh	ch.15 v.85	202:r24c24
dhi	ch.15 v.86	202:r20c21 202:r19c22
yu	ch.15 v.87	203:r12c5 203:r11c6
k	ch.15 v.88	203:r11c8
tō	ch.15 v.89	203:r14c7 203:r15c7
ja	ch.15 v.90	203:r22c11 203:r21c12
```

## align: compare a column with a known text

`align CHAPTER --group G --pos P --dir D --source "text"` or `align --passage N` (row N of `data/hidden_texts.csv`,
counted from 0, rebuilt from its rule). The source may be Roman (IAST), Devanagari or Kannada, or already split into
units with spaces. The whole source must be placed; each source unit is matched, mismatched or left as a gap (`-`).
`--shuffles N` repeats the alignment on N shuffles of the same column units; `--decoys` aligns the column with the
sources of the other passages of `hidden_texts.csv` that are not listed for this chapter. `--level` picks exact,
loose or strict comparison.

The first example is a passage from `hidden_texts.csv` (the `|` marks agreeing units):

```
$ python -m siritools align --passage 46 --shuffles 200 --decoys
passage 46: 1 (Sanskrit), rule: last letter of every long verse, read down
level exact: 37 of 47 source units match (score 60); column 108 units, span 54-103
 column : dhiḥ sa si d dhā ṣ ṭa sa ha s rē d dha la k ṣa ṇa maṃ t vā ṇāṃ gi rā tēṃ pa ti na nā m nā ma ṣ ṭa sa ha s rē ṇa tō ṣ ṭu mō bhū ṣ ṭa si d dha ē 
                  |  | |   | |  |  |  |    |     |  | |         |        |  |      |  |     |  | |  |  | |  |  |  | |  |  |  | |  |      | |  |  | |     
 source : p    ra si d dhā ṣ ṭa sa ha s ra d ve  la k ṣa -  ṇaṃ t -  vāṃ gi rā m   pa ti m  nā m nā ma ṣ ṭa sa ha s re ṇa to ṣ ṭu mo bhī ṣ ṭa si d dha ye
37 of 47 source units match (79%). | best of 200 shuffles: 14 (mean 8.5); shuffles at or above the real column: 0; p < 0.0050 | 63 decoy texts: best 12; at or above the real score: 0 | beats every shuffle and decoy tried | meets the 75 % / 40-unit ba ...
```

The second is your own text and column, here a 12-unit snippet: it beats all 200 shuffles but is under the 40-unit
bar, so it is a hint, not a result.

```
$ python -m siritools align 32 --group long --pos E1 --source "saṃ ni ya m ye n d ri ya g rā maṃ" --shuffles 200
chapter 32 long E1 down
level exact: 9 of 12 source units match (score 15); column 109 units, span 27-39
 column : n   ni ya raṃ yē n d ri ya g rā ma 
              |  |      |  | | |  |  | |     
 source : saṃ ni ya m   ye n d ri ya g rā maṃ
9 of 12 source units match (75%). | best of 200 shuffles: 4 (mean 2.5); shuffles at or above the real column: 0; p < 0.0050 | beats every shuffle and decoy tried | below  ...
```

How to read the summary: the real column must beat every shuffle and decoy; the 75 % identity over 40 units bar
is the one used for certification (`docs/certification.md`). A short text can beat shuffles by luck of the
alphabet; the decoy test is the stricter one.

## search: a string in every chapter and every column rule

`search QUERY [--where stream|columns|both] [--chapters 15,16] [--level exact|loose] [--limit N]`. The query is Roman or
Kannada. It must equal the letters of consecutive units, starting and ending on a unit boundary. Each hit gives the
chapter, the stream or the column rule (`group position direction`), the verse and the cell of the first unit.
"expected by chance" is a rough estimate that treats units as independent draws from their overall frequencies; short
queries and common letters give many chance hits.

```
$ python -m siritools search ಜಿನೇನ್ದ್ರ --limit 6
query units: ji ne n d ra   hits: 17   expected by chance: stream 6.49e-05, columns 6.67e-05
  ch.1 stream verses #2170 v.49  168:r27c21  ji nē n d ra
  ch.2 stream verses #2644 v.92  192:r2c3  ji nē n d ra
  ch.3 stream verses #4112 v.175  220:r14c8  ji nē n d ra
  ch.4 stream verses #137 v.3  236:r7c24  ji nē n d ra
  ch.5 stream verses #4348 v.188  271:r22c19  ji nē n d ra
  ch.8 stream verses #573 v.24  346:r12c7  ji nē n d ra
  ... 11 more (use --limit)
```

```
$ python -m siritools search "yukto jahātīha" --where columns
query units: yu k to ja hā tī ha   hits: 4   expected by chance: stream 0, columns 3.89e-12
  ch.15 column all E1 down #86 v.87  203:r12c5  yu k tō ja hā tī ha
  ch.15 column short E1 down #69 v.87  203:r12c5  yu k tō ja hā tī ha
  ch.26 column all E1 down #278 v.279  130:r6c4  yu k tō ja hā tī ha
  ch.26 column short E1 down #197 v.279  130:r6c4  yu k tō ja hā tī ha
```

The same eight-unit stretch is found in the chapter 15 column and again in chapter 26 (the two chapters hold the same
Gītā verse); a column hit needs the letters to be exactly right, so a column with a few misread letters will not be found:
use `align` for those.

## audit: rebuild all 68 passages

`audit [--rows 0,1,2] [--shuffles N]` takes every row of `hidden_texts.csv`, reads its rule in words, rebuilds the
column from the raw numbers, parses the source text into units, aligns them and compares the match count with the
stored `letters_matched`. The same alignment is used for every row; nothing is tuned per row. Status is `exact`
(count equal at the `exact` level), `loose` (equal only when ignoring vowel length), `mismatch` or `error`. The
`grid-run` column says whether the stored `grid_letters` (gap marks removed) occur as one unbroken run of the column
we rebuilt, which checks the column itself.

```
$ python -m siritools audit
row verse   ch        stored  ours loose  src  status   grid-run
  0 2.50    15            32    32    34   41  exact    found    
  1 3.30    15            35    35    36   44  exact    found    
  2 2.67    18            33    33    35   42  exact    found    
  3 3.21    19            34    34    36   44  exact    found    
  4 18.6    19            36    36    38   46  exact    found    
...
 66 23      57 58         46    46    49   59  exact    found    
 67 1–5     49 48 47     177   177   180  275  exact    found    
tally: {'exact': 68}
mismatches: none
```

Result on this data: all 68 rows reproduce `letters_matched` exactly, and for all 68 the stored `grid_letters` is a run of the
rebuilt column. For 30 of the 68 our aligned stretch is also letter for letter the stored `grid_letters`; in the others it
differs by an edge letter or two where several alignments tie (the match count is the same). The `source_text` of the
last row (five verses headed Śrutāvatāra) is only a note, so the stored `source_letters` serve as the source there. For that row, "exact"
shows that the column and the stored letters agree, not that a published text was matched.

## soundmap: is the 1-64 table better than a shuffled one?

`soundmap [--chapters 15,25] [--trials 1000]` reads the numbers of the chapters through the real table and through
shuffled tables (the same 27 vowels, 33 consonants and 4 signs given to the 64 numbers in random order) and scores
two rules of writing: a consonant should be followed by a vowel (`cv_rate`), and ṃ ḥ should follow a vowel
(`sign_legal`). It tests the vowel / consonant / sign split of the table, not which consonant is which.

```
$ python -m siritools soundmap
chapters [15, 25, 35, 45, 55], 100602 numbers, 1000 shuffled tables
rate            real  shuffled mean  shuffled max  shuffles beaten
cv_rate        0.825          0.454         0.797     1000/1000
sign_legal     0.855          0.433         0.856      999/1000
legal          0.840          0.443         0.827     1000/1000
```

In this run one shuffled table matched the real table on `sign_legal` (999 of 1000 beaten); on the other two scores no
shuffled table reached the real table.

## Limits

- `align` and `audit` use plain Python and take a moment on long columns; shuffles are the slow part.
- Parsing a source text reads Roman `e` and `o` as short and `ḻ`, `ṟ` as the nearest sounds of the table; Devanagari
  avagraha is skipped; any other character ends a word.
- A hit or a match is evidence only against the shuffles and decoys you ran. The certified figures are in `docs/checks/`.
- The tools read the data as given. They do not correct misread numbers.
