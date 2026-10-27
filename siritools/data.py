"""Load the poem's data files (data/*.csv) and rebuild the reading stream, verses and units with provenance.

    grids.csv    chapter, page, row, c1..c27: the numbers of every page (? = unreadable, read here as 0)
    order.csv    the same layout: the reading rank of each cell within its chapter (0 = read first)
    verses.csv   chapter, verse, title, first_rank, last_rank: each verse as a run of reading ranks
    symbols.csv  code, kannada, roman, kind
    siribhuvalaya.csv  chapter, verse, kannada, kannada_words_romanised, english_draft

Positions are reported as (page, row, col) with row and col counted from 1, as in the CSV files (c1..c27).
The data folder is ../data next to this package; set SIRI_DATA to use another copy.
"""
from __future__ import annotations

import csv
import os
from collections import namedtuple
from functools import lru_cache

from . import script

DATA_DIR = os.environ.get('SIRI_DATA') or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
SIZE = 27

Page = namedtuple('Page', 'chapter page index cells ranks')
Page.__doc__ = """One 27 x 27 page: chapter, page id (as in the CSV), index (1-based position within the chapter),
cells (729 numbers, row by row, 0 = unreadable) and ranks (729 reading ranks within the chapter)."""
Verse = namedtuple('Verse', 'chapter number title first last')
Verse.__doc__ = """One verse: chapter, verse number (row order in verses.csv), printed title, first and last rank."""
Location = namedtuple('Location', 'page row col')


def _rows(name, data_dir=None):
    with open(os.path.join(data_dir or DATA_DIR, name), encoding='utf-8-sig', newline='') as f:
        yield from csv.DictReader(f)


def _num(x):
    return int(x) if x.isdigit() else 0


class Corpus:
    """All chapters of the poem, loaded once from a data folder."""

    def __init__(self, data_dir=None):
        self.data_dir = data_dir or DATA_DIR
        self._pages = {}
        self._verses = {}
        self._load()

    def _load(self):
        def raw(name):
            with open(os.path.join(self.data_dir, name), encoding='utf-8-sig', newline='') as f:
                rd = csv.reader(f)
                next(rd)
                for r in rd:
                    yield int(r[0]), r[1], r[3:3 + SIZE]
        cells, order = {}, []
        for ch, pg, vals in raw('grids.csv'):
            key = (ch, pg)
            if key not in cells:
                cells[key] = []
                order.append(key)
            cells[key].extend([int(x) if x.isdigit() else 0 for x in vals])
        ranks = {}
        for ch, pg, vals in raw('order.csv'):
            ranks.setdefault((ch, pg), []).extend(map(int, vals))
        for ch, pg in order:
            pages = self._pages.setdefault(ch, [])
            c, k = cells[(ch, pg)], ranks[(ch, pg)]
            if len(c) != SIZE * SIZE or len(k) != SIZE * SIZE:
                raise ValueError(f'chapter {ch} page {pg}: expected 729 cells and ranks, got {len(c)} and {len(k)}')
            pages.append(Page(ch, pg, len(pages) + 1, c, k))
        for n, r in enumerate(_rows('verses.csv', self.data_dir)):
            ch = int(r['chapter'])
            self._verses.setdefault(ch, []).append(
                Verse(ch, int(r['verse']), r['title'], int(r['first_rank']), int(r['last_rank'])))

    # ---- pages and the reading stream ----
    def chapters(self):
        """Chapter numbers, in order."""
        return sorted(self._pages)

    def pages(self, chapter):
        """The pages of a chapter in book order."""
        return self._pages[chapter]

    def page(self, chapter, page):
        """One page, by its 1-based index within the chapter (int) or by its page id (str, as in the CSV)."""
        pages = self._pages[chapter]
        if isinstance(page, int):
            if not 1 <= page <= len(pages):
                raise IndexError(f'chapter {chapter} has pages 1..{len(pages)}')
            return pages[page - 1]
        for p in pages:
            if p.page == str(page):
                return p
        raise KeyError(f'chapter {chapter} has no page id {page}')

    @lru_cache(maxsize=None)
    def _index(self, chapter):
        """(codes, where) for one chapter: the number and the (page id, cell index 0-728) read at each rank."""
        pages = self._pages[chapter]
        n = len(pages) * SIZE * SIZE
        codes, where = [None] * n, [None] * n
        for p in pages:
            pid = p.page
            for i, (num, k) in enumerate(zip(p.cells, p.ranks)):
                if not 0 <= k < n or where[k] is not None:
                    raise ValueError(f'chapter {chapter}: reading ranks are not 0..{n - 1} without repeats')
                codes[k] = num
                where[k] = (pid, i)
        return codes, where

    @lru_cache(maxsize=None)
    def stream(self, chapter):
        """All numbers of a chapter in reading order (tuple; index = reading rank)."""
        return tuple(self._index(chapter)[0])

    def location(self, chapter, rank):
        """(page, row, col) of the cell read at this rank."""
        pid, i = self._index(chapter)[1][rank]
        return Location(pid, i // SIZE + 1, i % SIZE + 1)

    def stream_units(self, chapter):
        """The whole chapter as written units, each carrying its ranks."""
        s = self.stream(chapter)
        return script.units(s, list(range(len(s))))

    # ---- verses ----
    def verses(self, chapter):
        """The verses of a chapter (list of Verse)."""
        return self._verses.get(chapter, [])

    def verse(self, chapter, number):
        for v in self.verses(chapter):
            if v.number == number:
                return v
        raise KeyError(f'chapter {chapter} has no verse {number}')

    def verse_codes(self, verse):
        """The numbers of one verse, in reading order."""
        return self.stream(verse.chapter)[verse.first:verse.last + 1]

    @lru_cache(maxsize=None)
    def verse_units(self, chapter):
        """[(Verse, [Unit, ...]), ...] for a chapter; every unit carries the ranks of the cells it is made of."""
        s = self.stream(chapter)
        return [(v, script.units(s[v.first:v.last + 1], list(range(v.first, v.last + 1))))
                for v in self.verses(chapter)]

    def unit_locations(self, chapter, unit):
        """(page, row, col) of each cell of a grid unit."""
        return [self.location(chapter, k) for k in unit.ranks]


@lru_cache(maxsize=None)
def corpus(data_dir=None):
    """The shared Corpus (loaded on first use, about a second)."""
    return Corpus(data_dir)


@lru_cache(maxsize=None)
def symbols(data_dir=None):
    """code -> (kannada, roman, kind), from symbols.csv."""
    return {int(r['code']): (r['kannada'], r['roman'], r['kind']) for r in _rows('symbols.csv', data_dir)}


@lru_cache(maxsize=None)
def readings(data_dir=None):
    """(chapter, verse) -> dict(kannada, words, english) from siribhuvalaya.csv (the printed letters, a word split
    in Roman letters and a machine English draft that no reader has checked)."""
    return {(int(r['chapter']), int(r['verse'])): {'kannada': r['kannada'], 'words': r['kannada_words_romanised'],
                                                   'english': r['english_draft']}
            for r in _rows('siribhuvalaya.csv', data_dir)}


def hidden_texts(data_dir=None):
    """The rows of hidden_texts.csv, as dicts."""
    return list(_rows('hidden_texts.csv', data_dir))
