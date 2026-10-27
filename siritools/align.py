"""Align a grid column with a known text, unit against unit.

The alignment is the one used for the figures in data/hidden_texts.csv: the whole source text must be placed
(a source unit that finds no partner is a gap), while the column may start and end anywhere (free flanks).
Scores: match +2, substitution -1, gap -2. Units are compared after `script.norm` at a chosen level:

    exact   the default: e = ē and o = ō only
    loose   also long = short vowels, ṃ and ḥ ignored
    strict  as written

A unit that is '?' (an unreadable cell or a rare sign) never matches. Among alignments with the same score the
one with more matches is kept. Standard library only; the matrix is kept so the path can be traced back.
"""
from __future__ import annotations

from collections import namedtuple

from . import script

MATCH, MISMATCH, GAP = 2, -1, -2
_B = 4096                  # score and match count share one integer: score * _B + matches

Alignment = namedtuple('Alignment', 'matches score source_len start end pairs')
Alignment.__doc__ = """matches: units that agree. score: alignment score. source_len: units in the source.
start, end: the span of the column used (python slice of the column). pairs: list of (column index or None,
source index or None) in order; None marks a gap."""


def _prep(seq, level):
    return [script.norm(x if isinstance(x, str) else x.text, level) for x in seq]


def _fill(g, s):
    """Dynamic-programming matrix; rows = column units (free start), columns = source units (global)."""
    n, m = len(g), len(s)
    H = [[j * GAP * _B for j in range(m + 1)]]
    for i in range(1, n + 1):
        gi = g[i - 1]
        prev = H[-1]
        row = [0]
        left = 0
        for j in range(1, m + 1):
            d = prev[j - 1] + (MATCH * _B + 1 if gi == s[j - 1] and gi != '?' and gi else MISMATCH * _B)
            u = prev[j] + GAP * _B
            l = left + GAP * _B
            left = d if d >= u and d >= l else (u if u >= l else l)
            row.append(left)
        H.append(row)
    return H


def align(column, source, level='exact'):
    """Align a column (list of Entry, Unit or str) with a source (list of Unit or str). Returns an Alignment."""
    g, s = _prep(column, level), _prep(source, level)
    m = len(s)
    if not g or not m:
        return Alignment(0, 0, m, 0, 0, [])
    H = _fill(g, s)
    bi = max(range(len(g) + 1), key=lambda i: H[i][m])
    v = H[bi][m]
    score, matches = divmod(v, _B)
    i, j, pairs = bi, m, []
    while j > 0:
        cur = H[i][j]
        if i > 0 and cur == H[i - 1][j - 1] + (MATCH * _B + 1 if g[i - 1] == s[j - 1] and g[i - 1] not in ('', '?') else MISMATCH * _B):
            pairs.append((i - 1, j - 1))
            i -= 1
            j -= 1
        elif i > 0 and cur == H[i - 1][j] + GAP * _B:
            pairs.append((i - 1, None))
            i -= 1
        else:
            pairs.append((None, j - 1))
            j -= 1
    pairs.reverse()
    return Alignment(matches, score, m, i, bi, pairs)


def score_only(g, s):
    """(matches, score) of already-normalised lists, fast path for shuffle tests."""
    m = len(s)
    if not g or not m:
        return 0, 0
    prev = [j * GAP * _B for j in range(m + 1)]
    best = prev[m]
    gap, mat, mis = GAP * _B, MATCH * _B + 1, MISMATCH * _B
    for gi in g:
        row = [0]
        left = 0
        ok = gi != '?' and gi != ''
        for j in range(1, m + 1):
            d = prev[j - 1] + (mat if ok and gi == s[j - 1] else mis)
            u = prev[j] + gap
            l = left + gap
            left = d if d >= u and d >= l else (u if u >= l else l)
            row.append(left)
        prev = row
        if left > best:
            best = left
    score, matches = divmod(best, _B)
    return matches, score


def render(column, source, aln):
    """Two aligned lines of text (column letters over source letters, '-' for a gap) and the matches line."""
    top, bot, mid = [], [], []
    for gi, sj in aln.pairs:
        a = column[gi] if gi is not None else '-'
        b = source[sj] if sj is not None else '-'
        a = a if isinstance(a, str) else a.text
        b = b if isinstance(b, str) else b.text
        w = max(len(a), len(b))
        top.append(a.ljust(w))
        bot.append(b.ljust(w))
        mid.append(('|' if (gi is not None and sj is not None and script.norm(a) == script.norm(b) and a != '?') else ' ').ljust(w))
    return ' '.join(top), ' '.join(mid), ' '.join(bot)
