"""Take one letter from each verse of a chapter and read them in order.
    python tools/column.py 32 --group long --pos E1            last letter of every long verse, read down
    python tools/column.py 25 --pos E2 --dir up                second-to-last letter, read up
"""
import argparse, siri

ap = argparse.ArgumentParser(); ap.add_argument('chapter', type=int)
ap.add_argument('--group', default='all', choices=['all', 'long', 'short']); ap.add_argument('--pos', default='E1')
ap.add_argument('--dir', default='down', choices=['down', 'up'])
a = ap.parse_args()
print(' '.join(siri.column(a.chapter, a.group, a.pos, a.dir)))
