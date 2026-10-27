"""Sounds, written units and scripts.

The poem's numbers are sounds:

    1-27   vowels: a ā ā i ī ī u ū ū ṛ ṝ ṝ ḷ ḷ ḷ e ē ē ai ai ai o ō ō au au au
           (short, long and three-beat forms of each vowel)
    28-60  consonants: k kh g gh ṅ c ch j jh ñ ṭ ṭh ḍ ḍh ṇ t th d dh n p ph b bh m y r l v ś ṣ s h
    61     ṃ        62  ḥ        63, 64  two rare signs (shown as … and ::)
    0      a cell that could not be read (? in data/grids.csv)

A *written unit* (akṣara) groups numbers the way they are written: a consonant joins the vowel after it, a consonant
with no vowel after it stands alone, and ṃ, ḥ and the two rare signs join the unit before. These are the rules used
by the certified audits (docs/checks/), so units built here are the units that were scored.

Source texts typed by users (IAST / ISO 15919 Roman, Devanagari or Kannada script) are turned into the same codes
and then into units with the same rules, so a grid column and a published verse are compared unit for unit.
"""
from __future__ import annotations

import unicodedata
from functools import lru_cache
from collections import namedtuple

VOWELS = ['a', 'ā', 'ā', 'i', 'ī', 'ī', 'u', 'ū', 'ū', 'ṛ', 'ṝ', 'ṝ', 'ḷ', 'ḷ', 'ḷ',
          'e', 'ē', 'ē', 'ai', 'ai', 'ai', 'o', 'ō', 'ō', 'au', 'au', 'au']
CONSONANTS = ['k', 'kh', 'g', 'gh', 'ṅ', 'c', 'ch', 'j', 'jh', 'ñ', 'ṭ', 'ṭh', 'ḍ', 'ḍh', 'ṇ',
              't', 'th', 'd', 'dh', 'n', 'p', 'ph', 'b', 'bh', 'm', 'y', 'r', 'l', 'v', 'ś', 'ṣ', 's', 'h']
MARKS = {61: 'ṃ', 62: 'ḥ', 63: '…', 64: '::'}
BREAK = -1          # word boundary in a parsed source text: ends a bare consonant, never becomes a unit
UNREADABLE = '?'

Unit = namedtuple('Unit', 'text codes ranks')
Unit.__doc__ = """One written unit: its Roman text, the numbers it is made of, and (for grid units) the reading
rank of each of those numbers within its chapter (None for units parsed from a source text)."""


def is_vowel(n):
    return 1 <= n <= 27


def is_consonant(n):
    return 28 <= n <= 60


def sound(n):
    """Roman sound of one number (code)."""
    if is_vowel(n):
        return VOWELS[n - 1]
    if is_consonant(n):
        return CONSONANTS[n - 28]
    return MARKS.get(n, UNREADABLE)


def kind(n):
    """'vowel', 'consonant', 'sign' or 'unreadable'."""
    return 'vowel' if is_vowel(n) else 'consonant' if is_consonant(n) else 'sign' if n in MARKS else 'unreadable'


def units(codes, ranks=None):
    """Group numbers into written units (list of Unit).

    ranks, if given, is a parallel list of reading ranks kept with each unit for provenance. BREAK codes (from parsed
    source texts) end a pending bare consonant and are otherwise dropped. Numbers outside 1-64 become a '?' unit."""
    out, pend = [], None            # pend = (code, rank) of a consonant waiting for its vowel

    def flush():
        nonlocal pend
        if pend:
            out.append(Unit(CONSONANTS[pend[0] - 28], (pend[0],), (pend[1],)))
            pend = None

    for k, n in enumerate(codes):
        r = ranks[k] if ranks is not None else None
        if n == BREAK:
            flush()
        elif is_vowel(n):
            if pend:
                out.append(Unit(CONSONANTS[pend[0] - 28] + VOWELS[n - 1], (pend[0], n), (pend[1], r)))
                pend = None
            else:
                out.append(Unit(VOWELS[n - 1], (n,), (r,)))
        elif is_consonant(n):
            flush()
            pend = (n, r)
        elif n in MARKS:
            flush()
            if out:
                last = out[-1]
                out[-1] = Unit(last.text + MARKS[n], last.codes + (n,), last.ranks + (r,))
            else:
                out.append(Unit(MARKS[n], (n,), (r,)))
        else:
            flush()
            out.append(Unit(UNREADABLE, (n,), (r,)))
    flush()
    if ranks is None:
        out = [Unit(u.text, u.codes, None) for u in out]
    return out


def texts(us):
    """Roman text of each unit."""
    return [u.text if isinstance(u, Unit) else u for u in us]


def roman(codes, sep=''):
    """Roman text of a number sequence, unit by unit."""
    return sep.join(u.text for u in units(codes))


# ---- Kannada script -------------------------------------------------------------------------------------------
KN_VOWEL = {1: 'ಅ', 2: 'ಆ', 3: 'ಆ', 4: 'ಇ', 5: 'ಈ', 6: 'ಈ', 7: 'ಉ', 8: 'ಊ', 9: 'ಊ', 10: 'ಋ', 11: 'ೠ', 12: 'ೠ',
            16: 'ಎ', 17: 'ಏ', 18: 'ಏ', 19: 'ಐ', 20: 'ಐ', 21: 'ಐ', 22: 'ಒ', 23: 'ಓ', 24: 'ಓ', 25: 'ಔ', 26: 'ಔ', 27: 'ಔ'}
KN_SIGN = {1: '', 2: 'ಾ', 3: 'ಾ', 4: 'ಿ', 5: 'ೀ', 6: 'ೀ', 7: 'ು', 8: 'ೂ', 9: 'ೂ', 10: 'ೃ', 11: 'ೄ', 12: 'ೄ',
           16: 'ೆ', 17: 'ೇ', 18: 'ೇ', 19: 'ೈ', 20: 'ೈ', 21: 'ೈ', 22: 'ೊ', 23: 'ೋ', 24: 'ೋ', 25: 'ೌ', 26: 'ೌ', 27: 'ೌ'}
KN_CONSONANT = 'ಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲವಶಷಸಹ'   # codes 28-60 in order
KN_OTHER = {13: 'ಳ', 14: 'ಳು', 15: 'ಳೂ', 61: 'ಂ', 62: 'ಃ', 63: '...', 64: '::'}
VIRAMA = '್'


def glyph(n):
    """Kannada for one number on its own (as printed in a grid cell)."""
    if not n:
        return '·'
    if n in KN_VOWEL:
        return KN_VOWEL[n]
    if is_consonant(n):
        return KN_CONSONANT[n - 28] + VIRAMA
    return KN_OTHER.get(n, '?')


def kannada(codes):
    """Kannada script for a number sequence: a consonant followed by a vowel takes the vowel's sign, otherwise it
    is written with a virama. Code 13 is written ಳ and behaves as a consonant here, as in the poem's printed letters
    (data/siribhuvalaya.csv, column kannada)."""
    s, k = [], 0
    while k < len(codes):
        n = codes[k]
        if n == 13 or is_consonant(n):
            base = 'ಳ' if n == 13 else KN_CONSONANT[n - 28]
            nxt = codes[k + 1] if k + 1 < len(codes) else None
            if nxt in KN_SIGN:
                s.append(base + KN_SIGN[nxt])
                k += 1
            else:
                s.append(base + VIRAMA)
        elif n != BREAK:
            s.append(glyph(n))
        k += 1
    return ''.join(s)


# ---- parsing source texts into codes ----------------------------------------------------------------------------
_RO_VOWELS = [('ai', 19), ('au', 25), ('ā', 2), ('ī', 5), ('ū', 8), ('ṝ', 11), ('ḹ', 14), ('ḷ', 13), ('ṛ', 10),
              ('ē', 17), ('ō', 23), ('a', 1), ('i', 4), ('u', 7), ('e', 16), ('o', 22)]
_RO_CONS = sorted(((c, 28 + i) for i, c in enumerate(CONSONANTS)), key=lambda x: -len(x[0])) + [('ḻ', 13), ('ṟ', 54)]
_RO_FIX = [('r̥̄', 'ṝ'), ('r̥', 'ṛ'), ('l̥̄', 'ḹ'), ('l̥', 'ḷ'), ('ṁ', 'ṃ'), ('m̐', 'ṃ')]

_DV_CONS = dict(zip('कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह', range(28, 61)))
_DV_CONS['ळ'] = 13
_DV_VOW = dict(zip('अआइईउऊऋॠऌएऐओऔ', [1, 2, 4, 5, 7, 8, 10, 11, 13, 16, 19, 22, 25]))
_DV_MAT = dict(zip('ािीुूृॄॢेैोौ', [2, 4, 5, 7, 8, 10, 11, 13, 16, 19, 22, 25]))
_DV_MARK = {'ं': 61, 'ँ': 61, 'ः': 62}

_KN_CONS = dict(zip(KN_CONSONANT, range(28, 61)))
_KN_CONS.update({'ಳ': 13, 'ೞ': 13, 'ಱ': 54})
_KN_VOW = {'ಅ': 1, 'ಆ': 2, 'ಇ': 4, 'ಈ': 5, 'ಉ': 7, 'ಊ': 8, 'ಋ': 10, 'ೠ': 11, 'ಌ': 13, 'ಎ': 16, 'ಏ': 17, 'ಐ': 19,
           'ಒ': 22, 'ಓ': 23, 'ಔ': 25}
_KN_MAT = {'ಾ': 2, 'ಿ': 4, 'ೀ': 5, 'ು': 7, 'ೂ': 8, 'ೃ': 10, 'ೄ': 11, 'ೆ': 16, 'ೇ': 17, 'ೈ': 19, 'ೊ': 22, 'ೋ': 23,
           'ೌ': 25}
_KN_MARK = {'ಂ': 61, 'ಃ': 62}


def detect_script(text):
    """'kannada', 'devanagari' or 'roman', by the first letter found."""
    for c in text:
        if 'ಀ' <= c <= '೿':
            return 'kannada'
        if 'ऀ' <= c <= 'ॿ':
            return 'devanagari'
    return 'roman'


def _parse_indic(text, cons, vow, mat, marks, virama, virama_breaks):
    out, i = [], 0
    while i < len(text):
        c = text[i]
        if c in cons:
            out.append(cons[c])
            nxt = text[i + 1] if i + 1 < len(text) else ''
            if nxt == '़':                       # nukta: same sound for our purposes
                i += 1
                nxt = text[i + 1] if i + 1 < len(text) else ''
            if nxt == virama:
                if virama_breaks:
                    out.append(BREAK)
                i += 2
                continue
            if nxt in mat:
                out.append(mat[nxt])
                i += 2
                continue
            out.append(1)                        # inherent a
        elif c in vow:
            out.append(vow[c])
        elif c in marks:
            out.append(marks[c])
        elif c not in 'ऽ‌‍':            # avagraha and joiners are skipped; anything else ends a word
            out.append(BREAK)
        i += 1
    return out


def _parse_roman(text):
    s = unicodedata.normalize('NFC', text.lower())
    for a, b in _RO_FIX:
        s = s.replace(a, b)
    out, i = [], 0
    while i < len(s):
        if s[i] in 'ṃḥ':
            out.append(61 if s[i] == 'ṃ' else 62)
            i += 1
            continue
        hit = next(((t, n) for t, n in _RO_VOWELS if s.startswith(t, i)), None) or \
            next(((t, n) for t, n in _RO_CONS if s.startswith(t, i)), None)
        if hit:
            out.append(hit[1])
            i += len(hit[0])
        else:
            out.append(BREAK)
            i += 1
    return out


def parse(text, script=None):
    """Codes for a source text in IAST / ISO 15919 Roman, Devanagari or Kannada (detected if not given).

    Spaces and punctuation become BREAK, so a word-final consonant stays a unit of its own ("tad asya" gives
    ta d a s ya), as in the certified audits. In Devanagari a virama always ends the unit. Roman 'ḻ' and Kannada ೞ
    are read as ḷ (13), the nearest of the poem's sounds; 'e' and 'o' are read as the short forms (16, 22)."""
    script = script or detect_script(text)
    if script == 'devanagari':
        return _parse_indic(text, _DV_CONS, _DV_VOW, _DV_MAT, _DV_MARK, '्', True)
    if script == 'kannada':
        return _parse_indic(text, _KN_CONS, _KN_VOW, _KN_MAT, _KN_MARK, VIRAMA, False)
    return _parse_roman(text)


def text_units(text, script=None):
    """Written units of a source text (list of Unit, ranks None). Text already split into units with spaces
    (e.g. 'saṃ ni ya m ye') parses to the same units; '-' (a gap mark in data/hidden_texts.csv) is ignored."""
    return units(parse(text, script))


# ---- normalisation for comparison ---------------------------------------------------------------------------------
LEVELS = ('strict', 'exact', 'loose')
_LOOSE = str.maketrans({'ā': 'a', 'ī': 'i', 'ū': 'u', 'ṝ': 'ṛ', 'ḹ': 'ḷ', 'ē': 'e', 'ō': 'o', 'ṃ': None, 'ḥ': None})


@lru_cache(maxsize=None)
def norm(text, level='exact'):
    """Comparison form of one unit's text.

    strict  as written (Unicode NFC, lower case).
    exact   the certified level: ē = e and ō = o (Sanskrit e/o are always long; the grid marks length), letters only;
            the rare signs and unreadable cells become '?', which never equals a source letter.
    loose   exact, and also long = short vowels and ṃ, ḥ ignored."""
    s = unicodedata.normalize('NFC', text.lower())
    if level == 'strict':
        return s
    s = s.replace('…', '?').replace('::', '?').replace('ē', 'e').replace('ō', 'o')
    s = ''.join(c for c in s if c.isalpha() or c == '?')
    if level == 'loose':
        s = s.translate(_LOOSE)
    elif level != 'exact':
        raise ValueError(f'unknown level {level!r}; use one of {LEVELS}')
    return s
