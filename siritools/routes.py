"""Read a page (or a square of it) along any route.

A route is a list of (row, col) cells, counted from 0 inside the region read. Built-in routes:

    rows        left to right, top to bottom
    columns     top to bottom, left to right
    snake       rows, every second row reversed
    diagonals   down-right diagonals, from the top-right corner to the bottom-left
    antidiagonals  down-left diagonals
    spiral-in   clockwise from the top-left corner towards the middle
    spiral-out  the same path reversed, from the middle outwards
    knight      a knight's tour (Warnsdorff's rule, ties broken by scan order) from the top-left corner
    custom      a list of cells you give, as "r,c r,c ..." or [(r, c), ...]

Any route can be reversed. `region` = (row, col, size) reads the size x size square whose top-left cell is (row, col)
(counted from 0); the default is the whole 27 x 27 page. Squares of the usual 9 x 9 layout are region=(9*br, 9*bc, 9).

A Reading holds the numbers in route order, their written units, Kannada, Roman text, and for every cell its
(page, row, col) with row and col counted from 1 on the page, as in grids.csv.
"""
from __future__ import annotations

from collections import namedtuple

from . import data, script

ROUTES = ('rows', 'columns', 'snake', 'diagonals', 'antidiagonals', 'spiral-in', 'spiral-out', 'knight', 'custom')

Reading = namedtuple('Reading', 'chapter page route region cells numbers units kannada roman')
Reading.__doc__ = """cells: [(page row, page col)] counted from 1, in route order; numbers: the numbers there (0 =
unreadable); units: written units (script.Unit), each carrying the route positions of its numbers in `ranks`;
kannada, roman: the numbers rendered as script."""


def route_cells(name, size=27, custom=None, reverse=False):
    """The cells of a named route over a size x size square, as (row, col) from 0."""
    n = size
    if name == 'rows':
        cells = [(r, c) for r in range(n) for c in range(n)]
    elif name == 'columns':
        cells = [(r, c) for c in range(n) for r in range(n)]
    elif name == 'snake':
        cells = [(r, c) for r in range(n) for c in (range(n) if r % 2 == 0 else range(n - 1, -1, -1))]
    elif name == 'diagonals':
        cells = [(r, r - d) for d in range(n - 1, -n, -1) for r in range(n) if 0 <= r - d < n]
    elif name == 'antidiagonals':
        cells = [(r, s - r) for s in range(2 * n - 1) for r in range(n) if 0 <= s - r < n]
    elif name in ('spiral-in', 'spiral-out'):
        cells = _spiral(n)
        if name == 'spiral-out':
            cells = cells[::-1]
    elif name == 'knight':
        cells = _knight(n)
    elif name == 'custom':
        if not custom:
            raise ValueError('a custom route needs cells')
        cells = parse_cells(custom) if isinstance(custom, str) else [tuple(x) for x in custom]
        for r, c in cells:
            if not (0 <= r < n and 0 <= c < n):
                raise ValueError(f'cell ({r}, {c}) is outside the {n} x {n} region')
    else:
        raise ValueError(f'unknown route {name!r}; use one of {ROUTES}')
    return cells[::-1] if reverse else cells


def parse_cells(text):
    """'0,0 0,1 1,1' -> [(0, 0), (0, 1), (1, 1)]"""
    out = []
    for tok in text.replace(';', ' ').split():
        r, c = tok.split(',')
        out.append((int(r), int(c)))
    return out


def _spiral(n):
    top, bot, left, right = 0, n - 1, 0, n - 1
    out = []
    while top <= bot and left <= right:
        out += [(top, c) for c in range(left, right + 1)]
        out += [(r, right) for r in range(top + 1, bot + 1)]
        if top < bot:
            out += [(bot, c) for c in range(right - 1, left - 1, -1)]
        if left < right:
            out += [(r, left) for r in range(bot - 1, top, -1)]
        top, bot, left, right = top + 1, bot - 1, left + 1, right - 1
    return out


_KM = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


def _knight(n):
    """Knight's tour by Warnsdorff's rule (fewest onward moves first, then fixed move order). If the walk gets stuck
    it stops, so on some sizes the route is shorter than n * n; the length is reported by the Reading."""
    seen = {(0, 0)}
    path = [(0, 0)]

    def moves(r, c):
        return [(r + a, c + b) for a, b in _KM if 0 <= r + a < n and 0 <= c + b < n and (r + a, c + b) not in seen]
    while True:
        cand = moves(*path[-1])
        if not cand:
            break
        nxt = min(cand, key=lambda x: len(moves(*x)))
        seen.add(nxt)
        path.append(nxt)
    return path


def read(chapter, page, route='rows', region=None, custom=None, reverse=False, corpus=None):
    """Read one page along a route. `page` is the 1-based index within the chapter or the page id (as in grids.csv)."""
    c = corpus or data.corpus()
    p = c.page(chapter, page)
    r0, c0, size = region or (0, 0, data.SIZE)
    if r0 < 0 or c0 < 0 or r0 + size > data.SIZE or c0 + size > data.SIZE:
        raise ValueError('region must lie inside the 27 x 27 page')
    cells = [(r0 + r, c0 + k) for r, k in route_cells(route, size, custom, reverse)]
    nums = [p.cells[r * data.SIZE + k] for r, k in cells]
    us = script.units(nums, list(range(len(nums))))
    return Reading(chapter, p.page, route, (r0, c0, size), [(r + 1, k + 1) for r, k in cells], nums, us,
                   script.kannada(nums), script.roman(nums))


def unit_cells(reading, unit):
    """(page, row, col) of each cell of one unit of a Reading."""
    return [(reading.page,) + reading.cells[i] for i in unit.ranks]
