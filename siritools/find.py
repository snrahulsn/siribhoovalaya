"""Recover how a chapter's pages are read, from the raw numbers alone.

Most pages are nine 9 x 9 squares. Each square is read along one path, and the nine squares are read in an order
(the chapter's key) that changes from chapter to chapter. Neither is assumed here.

Walk   Every path of the form "start at (r0, c0), keep stepping by `step` (wrapping round the 9 x 9 square); when the
       next cell is already taken, step by `break` instead" is tried: 9 * 9 * 8 * 8 = 5,184 candidates, of which
       3,888 visit all 81 cells. The right one makes the number sequence most predictable: the lowest conditional
       entropy of each number given the one before.
Key    The nine squares are put in the order where the end of each square runs most naturally into the start of
       the next (summed over the pages given). The key is printed as the rank (1-9) of each square, row by row.

Only the numbers are used; the stored reading order (order.csv) is used only by `stored_key` for comparison.
Short pages or few pages give weak evidence: use whole chapters.
"""
from __future__ import annotations

import collections
import itertools
import math
from collections import namedtuple

from . import data

Walk = namedtuple('Walk', 'entropy start step brk path')
Found = namedtuple('Found', 'chapter pages walks key stored_key rows_entropy')
STEPS = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)]


def blocks_of(grid_cells):
    """The nine 9 x 9 squares (row-major) of one page, each as 81 numbers row by row."""
    return [[grid_cells[(br * 9 + r) * 27 + bc * 9 + c] for r in range(9) for c in range(9)]
            for br in range(3) for bc in range(3)]


def candidate_walks():
    """Yield ((r0, c0), step, brk, path) for every candidate that visits all 81 cells; path = cell indexes 0-80."""
    for r0, c0 in itertools.product(range(9), range(9)):
        for st in STEPS:
            for br in STEPS:
                seen, r, c, path = set(), r0, c0, []
                for _ in range(81):
                    if (r, c) in seen:
                        break
                    seen.add((r, c))
                    path.append(r * 9 + c)
                    nr, nc = (r + st[0]) % 9, (c + st[1]) % 9
                    if (nr, nc) in seen:
                        nr, nc = (r + br[0]) % 9, (c + br[1]) % 9
                    r, c = nr, nc
                if len(path) == 81:
                    yield (r0, c0), st, br, path


def entropy(seqs):
    """Conditional entropy (bits) of a number given the one before, over sequences; 0 cells are skipped."""
    pair, first = collections.Counter(), collections.Counter()
    for s in seqs:
        for a, b in zip(s, s[1:]):
            if a and b:
                pair[(a, b)] += 1
                first[a] += 1
    n = sum(pair.values())
    if not n:
        return 0.0
    return -sum(v / n * math.log2(v / first[a]) for (a, b), v in pair.items())


def _path_entropy(cols, cache, path):
    """Entropy of a walk, counting pairs of values at consecutive path cells over all squares.
    cols[i] = the number at cell i in every square; cache holds the encoded value pairs of each cell pair."""
    keys = []
    for p, q in zip(path, path[1:]):
        lst = cache.get((p, q))
        if lst is None:
            lst = cache[(p, q)] = [a * 65 + b for a, b in zip(cols[p], cols[q]) if a and b]
        keys += lst
    pair = collections.Counter(keys)
    first = collections.Counter()
    for k, v in pair.items():
        first[k // 65] += v
    n = len(keys)
    if not n:
        return 0.0
    return -sum(v / n * math.log2(v / first[k // 65]) for k, v in pair.items())


def find_walk(blocks, top=3):
    """Rank all candidate walks over a list of 81-number squares. Returns (rows_entropy, [Walk, ...] best first,
    number of walks tried)."""
    cols = [[blk[i] for blk in blocks] for i in range(81)]
    cache = {}
    res = sorted(((_path_entropy(cols, cache, path), start, st, br, path)
                  for start, st, br, path in candidate_walks()), key=lambda x: x[0])
    return entropy(blocks), [Walk(*x) for x in res[:top]], len(res)


def find_key(page_blocks, path):
    """Order the nine squares of each page. page_blocks = [blocks of page 1, blocks of page 2, ...] (9 each).
    Returns the key as 9 ranks (1-9), one per square, row-major."""
    seq = {(p, k): [blk[i] for i in path] for p, bl in enumerate(page_blocks) for k, blk in enumerate(bl)}
    pair, first = collections.Counter(), collections.Counter()
    for v in seq.values():
        for a, b in zip(v, v[1:]):
            if a and b:
                pair[(a, b)] += 1
                first[a] += 1
    lp = lambda a, b: math.log((pair[(a, b)] + 0.1) / (first[a] + 6.4))
    n = len(page_blocks)
    J = [[sum(lp(seq[(p, i)][-1], seq[(p, j)][0]) for p in range(n)) if i != j else 0 for j in range(9)] for i in range(9)]
    order = max(itertools.permutations(range(9)), key=lambda q: sum(J[q[k]][q[k + 1]] for k in range(8)))
    key = [0] * 9
    for rank, b in enumerate(order):
        key[b] = rank + 1
    return key


def stored_key(page):
    """The key implied by the stored reading order of one Page (rank of each square's first-read cell)."""
    mins = [min(page.ranks[(br * 9 + r) * 27 + bc * 9 + c] for r in range(9) for c in range(9))
            for br in range(3) for bc in range(3)]
    srt = sorted(mins)
    return [srt.index(m) + 1 for m in mins]


def find(chapter, pages=None, corpus=None, top=3):
    """Find the walk and key of a chapter (or of the pages given, as 1-based indexes). Returns Found."""
    c = corpus or data.corpus()
    ps = c.pages(chapter)
    if pages:
        ps = [c.page(chapter, i) for i in pages]
    page_blocks = [blocks_of(p.cells) for p in ps]
    flat = [b for pb in page_blocks for b in pb]
    rows_h, walks, n = find_walk(flat, top)
    key = find_key(page_blocks, walks[0].path)
    return Found(chapter, [p.page for p in ps], walks, key, stored_key(ps[0]), rows_h), n


def format_key(key):
    return ' / '.join(' '.join(str(x) for x in key[i:i + 3]) for i in (0, 3, 6))


def find_from_grids(grids, top=3):
    """Same, for raw data: grids = list of pages, each 27 lists of 27 numbers. Returns (Found-like tuple)."""
    page_blocks = [blocks_of([x for row in g for x in row]) for g in grids]
    flat = [b for pb in page_blocks for b in pb]
    rows_h, walks, n = find_walk(flat, top)
    return walks, find_key(page_blocks, walks[0].path), rows_h
