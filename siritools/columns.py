"""Hidden-text columns: one letter taken from each verse of a chapter and read in order.

A column is described by a chapter, a group of verses, a position and a direction:

    group      all    every verse
               long   verses of 30 written units or more
               short  verses of fewer than 30 written units
    position   E1 last unit, E2 second from last, ... S1 first unit, S2 second, ...
    direction  down (first verse to last) or up

Every entry keeps where its letter came from: chapter, verse, the reading ranks and the (page, row, col) of each
cell of the unit. Verses with fewer units than the position needs are skipped.

hidden_texts.csv states each rule in words; `parse_rule` turns those words into segments so the same rule can be
rebuilt from the numbers (see audit.py).
"""
from __future__ import annotations

import re
from collections import namedtuple

from . import data

LONG_MIN = 30
GROUPS = ('all', 'long', 'short')
DIRECTIONS = ('down', 'up')

Entry = namedtuple('Entry', 'text chapter verse unit locations')
Entry.__doc__ = """One letter of a column: its Roman text, the chapter and verse it was taken from, the Unit
(with codes and reading ranks) and the (page, row, col) of each cell of that unit."""
Segment = namedtuple('Segment', 'chapter group pos')
Rule = namedtuple('Rule', 'segments direction')


def parse_pos(pos):
    """('S'|'E', k) from 'E1', 'S3', ..."""
    m = re.fullmatch(r'([SEse])(\d+)', pos.strip())
    if not m or int(m.group(2)) < 1:
        raise ValueError(f'position must look like E1 or S1, not {pos!r}')
    return m.group(1).upper(), int(m.group(2))


def is_long(units):
    return len(units) >= LONG_MIN


def column_units(chapter, group='all', pos='E1', corpus=None):
    """[(verse number, Unit)] for a column read down, without cell locations (cheap)."""
    if group not in GROUPS:
        raise ValueError(f'group must be one of {GROUPS}')
    c = corpus or data.corpus()
    side, k = parse_pos(pos)
    out = []
    for v, us in c.verse_units(chapter):
        if group != 'all' and is_long(us) != (group == 'long'):
            continue
        if len(us) >= k:
            out.append((v.number, us[k - 1] if side == 'S' else us[-k]))
    return out


def column(chapter, group='all', pos='E1', direction='down', corpus=None):
    """The column of one chapter (list of Entry)."""
    if direction not in DIRECTIONS:
        raise ValueError(f'direction must be one of {DIRECTIONS}')
    c = corpus or data.corpus()
    out = [Entry(u.text, chapter, vn, u, c.unit_locations(chapter, u)) for vn, u in column_units(chapter, group, pos, c)]
    return out[::-1] if direction == 'up' else out


def rule_column(rule, corpus=None):
    """Entries for a Rule: each segment is read in the rule's direction, segments follow in the order listed."""
    out = []
    for s in rule.segments:
        out.extend(column(s.chapter, s.group, s.pos, rule.direction, corpus))
    return out


_ORD = {'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5, 'sixth': 6, 'seventh': 7, 'eighth': 8, 'ninth': 9, 'tenth': 10}


def parse_rule(text, chapters):
    """Turn a rule in words (as in hidden_texts.csv) and its chapter list into a Rule.

    Understood: 'last / first / second-to-last / fifth letter from the end'; 'every verse / long verse / short
    verse'; 'read up / down'; several chapters listed in the order they are read (49 48 47); and the one
    run-on rule 'short verse of chapter A, running on into every verse of chapter B'."""
    t = text.lower()
    chs = [int(x) for x in re.findall(r'\d+', str(chapters))]
    if 'running on into' in t:
        a, b = chs[0], chs[1]
        pos = 'E1'
        first, second = t.split('running on into')
        g1 = 'short' if 'short' in first else 'long' if 'long' in first else 'all'
        g2 = 'short' if 'short' in second else 'long' if 'long' in second else 'all'
        segs = [Segment(a, g1, pos), Segment(b, g2, pos)]
    else:
        m = re.search(r'(\w+)-to-last', t) or re.search(r'(\w+) letter from the end', t)
        if m and m.group(1) in _ORD:
            pos = f'E{_ORD[m.group(1)]}'
        elif 'first letter' in t:
            pos = 'S1'
        elif 'last letter' in t:
            pos = 'E1'
        else:
            raise ValueError(f'cannot read the position in rule {text!r}')
        g = 'long' if 'long' in t else 'short' if 'short' in t else 'all'
        segs = [Segment(ch, g, pos) for ch in chs]
    direction = 'up' if 'read up' in t else 'down' if 'read down' in t else None
    if direction is None:
        raise ValueError(f'cannot read the direction in rule {text!r}')
    return Rule(segs, direction)


def texts(entries):
    return [e.text for e in entries]


def describe(e):
    """One line of provenance for an entry."""
    loc = ' '.join(f'{p}:r{r}c{c}' for p, r, c in e.locations)
    return f'{e.text}\tch.{e.chapter} v.{e.verse}\t{loc}'
