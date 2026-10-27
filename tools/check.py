"""Score a column against a known text, and against shuffles of the same letters.
    python tools/check.py 32 --group long --pos E1 --source "saṃ ni ya mye ndri ya grā maṃ ..."
The source is given as written units separated by spaces (as in data/hidden_texts.csv, column source_letters).
A text counts only if the real letters score far above every shuffled copy.
"""
import argparse, siri

ap = argparse.ArgumentParser(); ap.add_argument('chapter', type=int)
ap.add_argument('--group', default='all', choices=['all', 'long', 'short']); ap.add_argument('--pos', default='E1')
ap.add_argument('--dir', default='down', choices=['down', 'up']); ap.add_argument('--source', required=True)
ap.add_argument('--trials', type=int, default=1000)
a = ap.parse_args()
src = [x for x in a.source.split() if x != '-']
m, n, best = siri.shuffle_test(siri.column(a.chapter, a.group, a.pos, a.dir), src, a.trials)
print(f'{m} of {n} letters match; best of {a.trials} shuffles: {best}')
