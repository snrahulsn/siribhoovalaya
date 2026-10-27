"""Rebuild every passage in data/hidden_texts.csv from its rule and score it again.

For each row: read the rule in words, rebuild the column from the raw numbers, parse the source text into written
units, align (see align.py) and compare with the stored letters_matched. Nothing is tuned: the alignment is the
same for every row. Each row is reported as

    exact      our match count equals letters_matched at the certified ('exact') level
    loose      equal only when long/short vowels and ṃ ḥ are ignored (reported, not counted as exact)
    mismatch   our count differs; both numbers are given
    error      the rule or source could not be read

`grid_found` says whether the stored grid_letters (gap marks '-' removed) occur as one unbroken run of the rebuilt column (a check on the
column itself); `span_equal` says whether the stretch of the column our alignment uses is exactly that run
(informational: the stored run often differs from ours by edge letters while the match count agrees).
For the passage with no source text in the file (the five verses headed Śrutāvatāra) the stored source_letters are used
as the source.
"""
from __future__ import annotations

from collections import namedtuple

from . import align, columns, data, script, stats

Result = namedtuple('Result', 'index text verse chapters status stored ours ours_loose source_len span_equal grid_found shuffle_max error')


def source_units(row):
    st = row['source_text']
    if st.startswith('As printed in'):         # no text in the file: use the stored letters (gaps removed)
        return [x for x in row['source_letters'].split() if x != '-']
    return script.text_units(st)


def audit_row(index, row, corpus=None, shuffles=0, seed=1):
    stored = int(row['letters_matched'])
    base = dict(index=index, text=row['text'], verse=row['verse'], chapters=row['chapters'], stored=stored,
                ours=None, ours_loose=None, source_len=int(row['letters_in_source']), span_equal=None, grid_found=None,
                shuffle_max=None, error=None)
    try:
        rule = columns.parse_rule(row['rule'], row['chapters'])
        ents = columns.rule_column(rule, corpus)
        src = source_units(row)
        a = align.align(ents, src, 'exact')
        al = align.align(ents, src, 'loose')
    except Exception as e:                      # report, never hide
        return Result(status='error', **{**base, 'error': repr(e)})
    col = [e.text for e in ents]
    stored_run = [x for x in row['grid_letters'].split() if x != '-']
    found = any(col[k:k + len(stored_run)] == stored_run for k in range(len(col) - len(stored_run) + 1))
    base.update(ours=a.matches, ours_loose=al.matches, source_len=len(src), grid_found=found,
                span_equal=col[a.start:a.end] == stored_run)
    if shuffles:
        base['shuffle_max'] = stats.shuffle_test(ents, src, shuffles, seed)['shuffle_max']
    status = 'exact' if a.matches == stored else 'loose' if al.matches == stored else 'mismatch'
    return Result(status=status, **base)


def audit(corpus=None, shuffles=0, seed=1, rows=None, progress=None):
    """Audit all rows (or the given list of row indexes). Returns a list of Result."""
    c = corpus or data.corpus()
    allrows = data.hidden_texts()
    idx = rows if rows is not None else range(len(allrows))
    out = []
    for i in idx:
        out.append(audit_row(i, allrows[i], c, shuffles, seed))
        if progress:
            progress(out[-1])
    return out


def tally(results):
    t = {}
    for r in results:
        t[r.status] = t.get(r.status, 0) + 1
    return t


def decoy_pool(chapters, rows=None):
    """Source units of every passage that is NOT already known to be in the given chapters: a passage is left out
    if it, or any passage with the same text and verse, is listed for one of those chapters. These serve as decoys
    for a column of those chapters."""
    rows = rows or data.hidden_texts()
    mine = set(chapters)
    known = {(r['text'], r['verse']) for r in rows if mine & set(int(x) for x in r['chapters'].split())}
    return [source_units(r) for r in rows if (r['text'], r['verse']) not in known]
