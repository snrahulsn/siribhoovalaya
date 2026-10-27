"""Read the Siribhūvalaya from its number grids.

Everything here works from the files in data/:
  grids.csv    the numbers on every page (27 rows of 27; ? = could not be read)
  order.csv    the reading rank of every cell, in the same layout (0 = read first in the chapter)
  verses.csv   each verse as a run of reading ranks (first_rank .. last_rank)
  symbols.csv  the sound of each number, 1–64

No other source is used. Standard library only.
"""
import csv
import os
import random
from functools import lru_cache

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')

# Codes 1–27 are vowels (short, long, three-beat), 28–60 consonants, 61–64 the sounds that follow a vowel.
VOWELS = ['a', 'ā', 'ā', 'i', 'ī', 'ī', 'u', 'ū', 'ū', 'ṛ', 'ṝ', 'ṝ', 'ḷ', 'ḷ', 'ḷ',
          'e', 'ē', 'ē', 'ai', 'ai', 'ai', 'o', 'ō', 'ō', 'au', 'au', 'au']
CONSONANTS = ['k', 'kh', 'g', 'gh', 'ṅ', 'c', 'ch', 'j', 'jh', 'ñ', 'ṭ', 'ṭh', 'ḍ', 'ḍh', 'ṇ',
              't', 'th', 'd', 'dh', 'n', 'p', 'ph', 'b', 'bh', 'm', 'y', 'r', 'l', 'v', 'ś', 'ṣ', 's', 'h']


def _rows(name):
    with open(os.path.join(DATA, name), encoding='utf-8-sig') as f:
        yield from csv.DictReader(f)


@lru_cache(maxsize=None)
def symbols():
    """code -> (kannada, roman, kind)"""
    return {int(r['code']): (r['kannada'], r['roman'], r['kind']) for r in _rows('symbols.csv')}


@lru_cache(maxsize=None)
def pages(chapter):
    """The pages of a chapter in book order: list of (page id, cells, ranks), each a flat list of 729 (row by row)."""
    cells, ranks, order = {}, {}, []
    for r in _rows('grids.csv'):
        if int(r['chapter']) == chapter:
            p = r['page']
            if p not in cells: cells[p] = []; order.append(p)
            cells[p] += [int(x) if x.isdigit() else 0 for x in (r[f'c{i}'] for i in range(1, 28))]
    for r in _rows('order.csv'):
        if int(r['chapter']) == chapter:
            ranks.setdefault(r['page'], []).extend(int(r[f'c{i}']) for i in range(1, 28))
    return [(p, cells[p], ranks[p]) for p in order]


@lru_cache(maxsize=None)
def stream(chapter):
    """All numbers of a chapter in reading order (0 = unreadable)."""
    by_rank = {}
    for _, cells, ranks in pages(chapter):
        for n, k in zip(cells, ranks): by_rank[k] = n
    return [by_rank[k] for k in sorted(by_rank)]


def units(codes):
    """Group numbers into written units: a consonant joins the vowel after it; ṃ and ḥ join the unit before."""
    out, pend = [], None
    for n in codes:
        if 1 <= n <= 27:
            out.append((pend or '') + VOWELS[n - 1]); pend = None
        elif 28 <= n <= 60:
            if pend: out.append(pend)
            pend = CONSONANTS[n - 28]
        elif n in (61, 62):
            if pend: out.append(pend); pend = None
            mark = 'ṃ' if n == 61 else 'ḥ'
            if out: out[-1] += mark
            else: out.append(mark)
        else:
            if pend: out.append(pend); pend = None
            out.append('?')
    if pend: out.append(pend)
    return out


@lru_cache(maxsize=None)
def verses(chapter):
    """Each verse of a chapter as (verse number, title, list of written units), rebuilt from the numbers."""
    s = stream(chapter)
    return [(int(r['verse']), r['title'], units(s[int(r['first_rank']):int(r['last_rank']) + 1]))
            for r in _rows('verses.csv') if int(r['chapter']) == chapter]


def column(chapter, group='all', pos='E1', direction='down'):
    """One letter from each verse of a chapter.
    group: all | long (30 units or more) | short;  pos: E1 = last unit, E2 = second from last, S1 = first, ...;
    direction: down (first verse to last) or up."""
    vs = [u for _, _, u in verses(chapter)]
    if group in ('long', 'short'): vs = [u for u in vs if (len(u) >= 30) == (group == 'long')]
    k = int(pos[1:])
    col = [(u[k - 1] if pos[0] == 'S' else u[-k]) for u in vs if len(u) >= k]
    return col[::-1] if direction == 'up' else col


def _norm(u):
    """Loose match: long and short vowels alike, ṃ ignored (the grid and printed texts differ in both)."""
    t = u.replace('ṃ', '').replace('ḥ', '')
    for a, b in (('ā', 'a'), ('ī', 'i'), ('ū', 'u'), ('ē', 'e'), ('ō', 'o'), ('ṝ', 'ṛ')): t = t.replace(a, b)
    return t


def identity(grid, source):
    """Best local alignment (match +2, mismatch or gap -1) of two unit lists.
    Returns (matching units, units of the source covered by the alignment)."""
    a, b = [_norm(x) for x in grid], [_norm(x) for x in source]
    H = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    best, end = 0, (0, 0)
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            H[i][j] = max(0, H[i - 1][j - 1] + (2 if a[i - 1] == b[j - 1] else -1), H[i - 1][j] - 1, H[i][j - 1] - 1)
            if H[i][j] > best: best, end = H[i][j], (i, j)
    i, j = end; m = 0; j_end = j
    while i > 0 and j > 0 and H[i][j] > 0:
        if H[i][j] == H[i - 1][j - 1] + (2 if a[i - 1] == b[j - 1] else -1):
            m += a[i - 1] == b[j - 1]; i -= 1; j -= 1
        elif H[i][j] == H[i - 1][j] - 1: i -= 1
        else: j -= 1
    return m, j_end - j


def shuffle_test(grid, source, trials=1000, seed=1):
    """How many letters match, and the best of `trials` shuffles of the same letters."""
    m, n = identity(grid, source)
    rng, best = random.Random(seed), 0
    g = list(grid)
    for _ in range(trials):
        rng.shuffle(g); best = max(best, identity(g, source)[0])
    return m, n, best
