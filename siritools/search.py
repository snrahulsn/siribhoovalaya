"""Search a Roman or Kannada string in the poem.

The query is turned into written units (script.text_units) and compared unit for unit after `script.norm`
(level exact by default; loose also ignores vowel length, ṃ and ḥ). The letters of the query must equal the letters of consecutive units, starting and ending on a unit boundary (so
'bu' finds a column holding 'b' then 'u').

Two kinds of place are searched:

    stream   the chapter read in order, verse by verse (a hit may run over a verse boundary; this is reported)
    column   every hidden-text column: group (all, long, short) x position (S1-S5, E1-E5) x direction (down, up)

Every hit carries chapter, where it was found, the first verse it touches and the (page, row, col) of each cell of
its first unit. Short queries will hit by chance: a hit list says nothing without the expected number of chance
hits, so `search` also returns `chance`, an estimate from the letter frequencies of the searched text (the
chance that a random stretch of that text equals the query, times the number of places).
"""
from __future__ import annotations

from collections import Counter, namedtuple

from . import columns, data, script

Hit = namedtuple('Hit', 'where chapter place index length verse locations text')
Hit.__doc__ = """where: 'stream' or 'column'. place: 'verses' or e.g. 'long E1 down'. index: first unit (position in
the stream or column). length: units in the hit. verse: first verse touched. locations: (page, row, col) of the first
unit's cells. text: the matched units."""

POSITIONS = [f'S{k}' for k in range(1, 6)] + [f'E{k}' for k in range(1, 6)]


def _query_units(query, level):
    us = [script.norm(u.text, level) for u in script.text_units(query)]
    return [u for u in us if u and u != '?']


def _find_all(hay, needle):
    """Hits of the query in a list of normalised unit texts: (first index, number of units) for every place where the
    letters of the query equal the letters of consecutive units, starting and ending on a unit boundary. Comparing
    letters rather than units lets a query 'bu' find the two column units 'b', 'u' taken from different verses."""
    q = ''.join(needle)
    if not q:
        return []
    starts, pos = {}, 0
    ends = {}
    for i, t in enumerate(hay):
        starts[pos] = i
        pos += len(t)
        ends[pos] = i
    text = ''.join(hay)
    out, k = [], text.find(q)
    while k != -1:
        e = k + len(q)
        if k in starts and e in ends:
            out.append((starts[k], ends[e] - starts[k] + 1))
        k = text.find(q, k + 1)
    return out


def search_stream(query, chapters=None, level='exact', corpus=None):
    c = corpus or data.corpus()
    q = _query_units(query, level)
    hits = []
    for ch in chapters or c.chapters():
        flat, owner = [], []
        for v, us in c.verse_units(ch):
            for u in us:
                flat.append(script.norm(u.text, level))
                owner.append((v.number, u))
        for k, n in _find_all(flat, q):
            v, u = owner[k]
            hits.append(Hit('stream', ch, 'verses', k, n, v, c.unit_locations(ch, u),
                            ' '.join(o[1].text for o in owner[k:k + n])))
    return hits, q


def search_columns(query, chapters=None, level='exact', corpus=None):
    c = corpus or data.corpus()
    q = _query_units(query, level)
    hits = []
    for ch in chapters or c.chapters():
        for g in columns.GROUPS:
            for pos in POSITIONS:
                cu = columns.column_units(ch, g, pos, c)
                norm = [script.norm(u.text, level) for _, u in cu]
                for d in columns.DIRECTIONS:
                    flat = norm if d == 'down' else norm[::-1]
                    seq = cu if d == 'down' else cu[::-1]
                    for k, n in _find_all(flat, q):
                        vn, u = seq[k]
                        hits.append(Hit('column', ch, f'{g} {pos} {d}', k, n, vn, c.unit_locations(ch, u),
                                        ' '.join(x[1].text for x in seq[k:k + n])))
    return hits, q


def chance(query_units, counts, places):
    """Expected hits by chance: places * product of the unit frequencies (independent draws)."""
    total = sum(counts.values())
    p = 1.0
    for u in query_units:
        p *= counts.get(u, 0) / total if total else 0.0
    return p * places


def search(query, where='both', chapters=None, level='exact', corpus=None):
    """Search stream and/or columns. Returns dict(query_units, hits, chance_stream, chance_columns, places)."""
    c = corpus or data.corpus()
    out = {'hits': [], 'query_units': None}
    freq, n_places = Counter(), 0
    for ch in chapters or c.chapters():
        for _, us in c.verse_units(ch):
            for u in us:
                freq[script.norm(u.text, level)] += 1
                n_places += 1
    if where in ('stream', 'both'):
        h, q = search_stream(query, chapters, level, c)
        out['hits'] += h
        out['query_units'] = q
        out['chance_stream'] = chance(q, freq, n_places)
    if where in ('columns', 'both'):
        h, q = search_columns(query, chapters, level, c)
        out['hits'] += h
        out['query_units'] = q
        n_col = len(chapters or c.chapters()) * len(columns.GROUPS) * len(POSITIONS) * 2 * 150
        out['chance_columns'] = chance(q, freq, n_col)
    return out
