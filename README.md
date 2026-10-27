# Siribhūvalaya — the numbers, the letters, the hidden texts

The Siribhūvalaya is a ninth-century Kannada poem by Ācārya Kumudendu, written entirely in numbers from 1 to 64,
set in grids of 27 × 27. This repository holds an independent digital reading of the whole poem, made with
Claude: every grid, its reading order, every verse in letters with a first English draft, and the 64 hidden
verses found by reading one letter from each verse.

Website and film: [siribhoovalaya.com](https://siribhoovalaya.com)

## Data (`data/`)

| File | What it holds |
|---|---|
| `grids.csv` | Every number grid: one row per grid row (27 numbers), 1,268 pages, 59 chapters. `?` marks a cell that could not be read (about 4 in 1,000). |
| `order.csv` | The reading rank of every cell, in the same layout as `grids.csv` (0 = read first in the chapter). |
| `verses.csv` | Each verse as a run of reading ranks (`first_rank` to `last_rank`). 20,640 verses and lines. |
| `symbols.csv` | The sound of each number: 27 vowels, 33 consonants and 4 sounds that follow a vowel. |
| `siribhuvalaya.csv` | Every verse in Kannada letters, in Roman letters split into words, and a machine English draft (not checked by a reader). |
| `hidden_texts.csv` | 68 passages spelled by one letter from each verse (64 distinct verses: 34 of the Bhagavad Gītā, 25 from Jain texts, 5 headed Śrutāvatāra), with the rule, the grid letters beside the source letters, and the scores. |

`docs/certification.md` says what was confirmed and how; `docs/checks/` holds the independent audits that rebuilt
every hidden text from the raw numbers and tested it against 1,000 shuffles and 1,000 decoy verses.

## Tools (`siritools/`, Python 3.9+, standard library only)

```bash
python -m siritools read 15 --verse 1                 # a verse rebuilt from the numbers, with the cell of each letter
python -m siritools route 15 1 --route spiral-in --square 1      # read a page or square along a shape
python -m siritools walk 15                           # recover a chapter's walk and key from the raw numbers
python -m siritools column 32 --group long --pos E1   # last letter of every long verse of chapter 32, read down
python -m siritools align --passage 0 --shuffles 200 --decoys    # score a column against a known text, shuffles, decoys
python -m siritools search "ಜಿನೇನ್ದ್ರ"                  # a Kannada or Roman string in every chapter and column rule
python -m siritools audit                             # rebuild all 68 hidden passages and re-score them
python -m siritools soundmap                          # the 1-64 sound table against shuffled tables
python -m unittest                                    # run the tests
```

Every command takes `--json`. `docs/TOOLS.md` has a worked example of each, with real output, and describes the
modules for use from Python. The alignment is a plain one for exploring; the certified figures come from the audits in
`docs/checks/`.

## Sources

- National Archives of India, Abhilekh Patal, Accession 507: item NAIDLB00002349 (chapters 1-20), item NAIDLB00002350
  (chapters 21-40) and item NAIDLB00002351 (chapters 41-59). The grids in `data/grids.csv` are read from these scans.
- The printed edition of chapters 1-8, used to calibrate the reading of the numbers.

## How the reading works

Most pages are nine squares of 9 × 9. Inside each square the numbers are read along the walk that builds a magic
square: start in the middle of the top row, go up and to the right, come back in from the opposite edge, and step
down when the next cell is already read. The nine squares are read in an order that changes from chapter to chapter
(the chapter's key). Each number is one of the 64 sounds, in the traditional order: vowels, then consonants, then
the four sounds that follow a vowel.

## Help

The English is a first draft and is weakest in the last chapters. If you read Old Kannada, please
[suggest a correction](../../issues/new?template=correction.yml). Found another reading shape or hidden text?
[Tell us](../../issues/new?template=finding.yml).

## Licence

Data and documents: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — please credit siribhoovalaya.com.
Code: MIT.
