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

## Tools (`tools/`, Python 3, standard library only)

```bash
python tools/read.py 15 --verse 1                       # a verse rebuilt from the numbers, with its numbers
python tools/column.py 32 --group long --pos E1         # last letter of every long verse of chapter 32, read down
python tools/column.py 49 --group long --pos E5 --dir up
python tools/check.py 32 --group long --pos E1 --source "saṃ ni ya m ye n d ri ya g rā maṃ"   # score against a text and shuffles
```

`tools/siri.py` is the small library behind them: load a chapter, put its numbers in reading order, group them
into written units, take a column, align it with a known text and compare with shuffled copies. Its alignment is a
simple one for exploring; the certified figures come from the audits in `docs/checks/`.

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
