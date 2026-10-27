"""Test the 1-64 sound table against shuffled tables.

The table gives every number a kind: 1-27 vowel, 28-60 consonant, 61-64 sign. If it is the poem's real key, the
number stream should obey the rules of writing when read through it:

    cv_rate        share of consonants (28-60) that are followed by a vowel (a consonant joins the vowel after it)
    sign_legal     share of signs (61-64) that directly follow a vowel (ṃ ḥ attach to a vowel)
    legal          the mean of the two: one number between 0 and 1

A shuffled table gives the 64 kinds (27 vowels, 33 consonants, 4 signs) to the numbers in random order. Because
only the kinds matter for these rules, this tests the vowel / consonant / sign split of the table, not which exact
consonant is which; a table can pass this and still have consonants in the wrong order. The statistics come from the
counts of number pairs, so a thousand shuffles take a moment.

Unreadable cells (0) are left out and break a run.
"""
from __future__ import annotations

import random
from collections import Counter

from . import data, script

KINDS = ['V'] * 27 + ['C'] * 33 + ['S'] * 4        # index = code - 1


def real_kinds():
    return list(KINDS)


def counts(streams):
    """Counts of adjacent readable number pairs (a, b) over streams of numbers."""
    pairs = Counter()
    for s in streams:
        prev = 0
        for n in s:
            if n and prev:
                pairs[(prev, n)] += 1
            prev = n
    return pairs


def score(pairs, kinds):
    """The two rates and their mean for a table (list of 64 kind letters, index = code - 1)."""
    c_tot = c_v = s_tot = s_ok = 0
    for (a, b), n in pairs.items():
        ka, kb = kinds[a - 1], kinds[b - 1]
        if ka == 'C':
            c_tot += n
            c_v += n * (kb == 'V')
        if kb == 'S':
            s_tot += n
            s_ok += n * (ka == 'V')
    cv = c_v / c_tot if c_tot else 0.0
    sg = s_ok / s_tot if s_tot else 0.0
    return {'cv_rate': cv, 'sign_legal': sg, 'legal': (cv + sg) / 2}


def test(chapters=None, trials=1000, seed=1, corpus=None):
    """Score the real table and `trials` shuffled tables on the streams of the given chapters (default: 15, 25, 35,
    45, 55). Returns dict(real=..., shuffles=dict(min, mean, max per rate), beaten=shuffles the real table beats,
    trials, chapters, numbers)."""
    c = corpus or data.corpus()
    chapters = chapters or [15, 25, 35, 45, 55]
    streams = [c.stream(ch) for ch in chapters]
    pairs = counts(streams)
    real = score(pairs, KINDS)
    rng = random.Random(seed)
    k = list(KINDS)
    rows = []
    for _ in range(trials):
        rng.shuffle(k)
        rows.append(score(pairs, k))
    summ = {}
    for key in real:
        vals = [r[key] for r in rows]
        summ[key] = {'min': min(vals), 'mean': sum(vals) / len(vals), 'max': max(vals),
                     'beaten': sum(v < real[key] for v in vals)}
    return {'real': real, 'shuffles': summ, 'trials': trials, 'chapters': chapters,
            'numbers': sum(len(s) for s in streams)}


def render_sample(codes, table=None, n=40):
    """Roman text of the first n numbers through the real table (a quick look)."""
    return script.roman(codes[:n])
