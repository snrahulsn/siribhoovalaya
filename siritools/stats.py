"""Is a match better than chance? Shuffle test, decoy test and a plain-words summary.

shuffle_test   align the real column, then many shuffles of the same units (same letters, random order) with the
               same source; the real column must beat every shuffle.
decoy_test     align the real column against other texts of similar length (decoys) instead of the true source.
               A column that merely fits Sanskrit-like letter frequencies will score on decoys too.
decoy_record   look up the decoy results that were published with the audits (docs/checks/decoys_jain_texts.json).

All functions are deterministic for a given seed.
"""
from __future__ import annotations

import json
import os
import random

from . import align as _align
from . import data, script


def _norm_list(seq, level):
    return [script.norm(x if isinstance(x, str) else x.text, level) for x in seq]


def shuffle_test(column, source, trials=1000, seed=1, level='exact'):
    """dict(matches, shuffle_max, shuffle_mean, shuffle_ge, trials, p): shuffle_ge counts shuffles scoring at least
    as many matches as the real column; p = (shuffle_ge + 1) / (trials + 1), the smallest p this many trials allow."""
    g, s = _norm_list(column, level), _norm_list(source, level)
    real, _ = _align.score_only(g, s)
    rng = random.Random(seed)
    scores, ge = [], 0
    h = list(g)
    for _ in range(trials):
        rng.shuffle(h)
        m, _ = _align.score_only(h, s)
        scores.append(m)
        ge += m >= real
    return {'matches': real, 'shuffle_max': max(scores) if scores else None,
            'shuffle_mean': sum(scores) / len(scores) if scores else None,
            'shuffle_ge': ge, 'trials': trials, 'p': (ge + 1) / (trials + 1)}


def decoy_test(column, source, decoys, level='exact', window=0.25):
    """Align the column with each decoy whose length is within `window` of the source length.
    Returns dict(matches, decoy_max, decoy_ge, decoys): matches is for the true source."""
    g, s = _norm_list(column, level), _norm_list(source, level)
    real, _ = _align.score_only(g, s)
    best, ge, used = 0, 0, 0
    for d in decoys:
        dn = _norm_list(d, level)
        if not dn or abs(len(dn) - len(s)) > window * len(s):
            continue
        m, _ = _align.score_only(g, dn)
        used += 1
        best = max(best, m)
        ge += m >= real
    return {'matches': real, 'decoy_max': best, 'decoy_ge': ge, 'decoys': used}


def decoy_record(location=None, data_dir=None):
    """Published decoy results (list of dicts); filtered by a substring of the 'location' or 'claim' field."""
    path = os.path.join(data_dir or os.path.dirname(data.DATA_DIR), 'docs', 'checks', 'decoys_jain_texts.json')
    with open(path, encoding='utf-8') as f:
        rows = json.load(f)
    if location:
        rows = [r for r in rows if location in r['location'] or location in r['claim']]
    return rows


def summary(matched, source_len, shuffle=None, decoy=None):
    """A plain-words verdict. Identity is matches / source units. 'above chance' needs the real column to beat
    every shuffle (and every decoy, if given); identity of 75 % over 40 units is the certification bar."""
    ident = matched / source_len if source_len else 0.0
    lines = [f'{matched} of {source_len} source units match ({ident:.0%}).']
    ok = True
    if shuffle:
        pv = f"p < {shuffle['p']:.4f}" if shuffle['shuffle_ge'] == 0 else f"p = {shuffle['p']:.4f}"
        lines.append(f"best of {shuffle['trials']} shuffles: {shuffle['shuffle_max']} (mean {shuffle['shuffle_mean']:.1f}); "
                     f"shuffles at or above the real column: {shuffle['shuffle_ge']}; {pv}")
        ok = ok and shuffle['shuffle_ge'] == 0
    if decoy:
        lines.append(f"{decoy['decoys']} decoy texts: best {decoy['decoy_max']}; at or above the real score: {decoy['decoy_ge']}")
        ok = ok and decoy['decoy_ge'] == 0
    if not (shuffle or decoy):
        lines.append('no shuffle or decoy test run')
    else:
        lines.append('beats every shuffle and decoy tried' if ok else 'does NOT beat every shuffle and decoy tried')
    lines.append('meets the 75 % / 40-unit bar' if ident >= 0.75 and source_len >= 40 else 'below the 75 % / 40-unit bar')
    return ' | '.join(lines)
