"""Search-wide null for the Bhagavad Gita hidden-text search (paper, section 4).

The real search: every column of chapters 10-59 (positions S1-S3 and E1-E3; all, long and short verses; read
down and up) against every Gita verse of 40 letters or more, using the alignment of siritools/align.py
(match +2, mismatch -1, gap -2; whole verse placed, column free at both ends). A pair counts when at least
75 % of the verse's letters match.

The null: the same complete search, with the letters of every column shuffled within that column.
If the hidden passages were chance, shuffled searches would reach the bar about as often as the real one.

    python scripts/search_null.py            # real search + 20 shuffled searches (about 30 minutes, 4 cores)
    python scripts/search_null.py --reps 5 --procs 8

Needs a C++ compiler (c++ or g++); the alignment core in align_hits.cpp is compiled on first run.
The Gita text is the GRETIL edition, downloaded once and checked against its SHA-256.
"""
import argparse, ctypes, hashlib, json, os, random, re, subprocess, sys, tempfile, urllib.request
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from siritools import data, columns, script  # noqa: E402

GITA_URL = 'https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/2_epic/mbh/ext/bhgce__u.htm'
GITA_SHA = 'f797fb6d64009cebb11e1cf75041b3bf0a2e6735da331dc473342a8bebcdec25'
CACHE = os.path.join(tempfile.gettempdir(), 'siri_search_null')
VOWELS = ('ai', 'au', 'ā', 'ī', 'ū', 'ṝ', 'ḷ', 'ṛ', 'ē', 'ō', 'a', 'i', 'u', 'e', 'o')
CONSONANTS = ('kh', 'gh', 'ch', 'jh', 'ṭh', 'ḍh', 'th', 'dh', 'ph', 'bh',
              'k', 'g', 'ṅ', 'c', 'j', 'ñ', 'ṭ', 'ḍ', 'ṇ', 't', 'd', 'n', 'p', 'b', 'm',
              'y', 'r', 'l', 'v', 'ś', 'ṣ', 's', 'h')


def roman_units(s):
    """Split IAST text into written units (consonants + vowel; ṃ and ḥ attach to the unit before)."""
    s = re.sub(r'<[^>]*>', ' ', s.lower())
    out, pending, i = [], '', 0
    while i < len(s):
        if s[i] in 'ṃṁḥ':
            if out:
                out[-1] += 'ṃ' if s[i] in 'ṃṁ' else 'ḥ'
            i += 1
            continue
        t = next((v for v in VOWELS if s.startswith(v, i)), None)
        if t:
            out.append(pending + t); pending = ''; i += len(t); continue
        t = next((c for c in CONSONANTS if s.startswith(c, i)), None)
        if t:
            if pending:
                out.append(pending)
            pending = t; i += len(t); continue
        if pending:
            out.append(pending); pending = ''
        i += 1
    if pending:
        out.append(pending)
    return out


def gita():
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, 'bhgce__u.htm')
    if not os.path.exists(path):
        urllib.request.urlretrieve(GITA_URL, path)
    raw = open(path, 'rb').read()
    if hashlib.sha256(raw).hexdigest() != GITA_SHA:
        sys.exit(f'{path}: SHA-256 differs from the edition used in the paper; delete it and retry')
    verses = {}
    for line in re.split(r'(?i)<br\s*/?>', raw.decode('utf-8', 'replace')):
        m = re.search(r'Bhg_(\d+)\.(\d+)([a-z]) ', line)
        if m:
            verses.setdefault(f'{int(m[1])}.{int(m[2])}', []).append(re.sub(r'<[^>]+>', '', line[:m.start()]).strip())
    return {k: roman_units(' '.join(v)) for k, v in verses.items()}


def library():
    so = os.path.join(CACHE, 'align_hits.so')
    if not os.path.exists(so):
        os.makedirs(CACHE, exist_ok=True)
        cxx = next((c for c in ('c++', 'g++', 'clang++') if subprocess.call(['which', c], stdout=subprocess.DEVNULL) == 0), None)
        if not cxx:
            sys.exit('no C++ compiler found (c++, g++ or clang++)')
        subprocess.check_call([cxx, '-O3', '-shared', '-fPIC', '-o', so, os.path.join(HERE, 'align_hits.cpp')])
    lib = ctypes.CDLL(so)
    lib.align_hits.restype = ctypes.c_int
    return lib


def build():
    corpus = data.corpus()
    cols = []
    for ch in range(10, 60):
        for group in ('all', 'long', 'short'):
            for pos in ('S1', 'S2', 'S3', 'E1', 'E2', 'E3'):
                seq = [script.norm(u.text) for _, u in columns.column_units(ch, group, pos, corpus)]
                if len(seq) < 40:
                    continue
                cols.append((f'{ch}:{group}:{pos}:down', seq))
                cols.append((f'{ch}:{group}:{pos}:up', seq[::-1]))
    refs = [(k, [script.norm(t) for t in v]) for k, v in gita().items() if len(v) >= 40]
    vocab = {}
    enc = lambda s: [vocab.setdefault(x, len(vocab)) if x != '?' else -1 for x in s]
    return [(k, enc(s)) for k, s in cols], [(k, enc(v)) for k, v in refs]


COLS = REFS = None


def init():
    global COLS, REFS
    COLS, REFS = build()


def run(rep):
    lib = library()
    rng = random.Random(1000 + rep)
    passes, best = [], 0.0
    for key, s in COLS:
        s = s[:]
        if rep:
            rng.shuffle(s)
        a = (ctypes.c_int * len(s))(*s)
        for vk, v in REFS:
            b = (ctypes.c_int * len(v))(*v)
            hits = lib.align_hits(a, len(s), b, len(v))
            best = max(best, hits / len(v))
            if hits / len(v) >= .75:
                passes.append([key, vk, hits, len(v)])
    return rep, best, passes


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--reps', type=int, default=20, help='shuffled searches (default 20)')
    ap.add_argument('--procs', type=int, default=4)
    ap.add_argument('--out', default='search_null_results.json')
    a = ap.parse_args()
    library(); init()
    print(f'{len(COLS)} columns x {len(REFS)} Gita verses = {len(COLS) * len(REFS):,} comparisons per search', flush=True)
    res = {}
    with Pool(a.procs, initializer=init) as p:
        for rep, best, passes in p.imap_unordered(run, range(a.reps + 1)):
            res[rep] = {'best_identity': best, 'pairs_at_75': len(passes), 'pairs': passes}
            name = 'real' if rep == 0 else f'shuffled {rep}'
            print(f'{name:12s} best identity {best:.1%}  pairs >= 75 %: {len(passes)}  distinct verses: {len({x[1] for x in passes})}', flush=True)
    json.dump(res, open(a.out, 'w'), indent=1)


if __name__ == '__main__':
    main()
