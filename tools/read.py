"""Print a chapter's verses rebuilt from the numbers.
    python tools/read.py 15            all verses of chapter 15, in Roman letters
    python tools/read.py 15 --verse 1  one verse, with its numbers
"""
import argparse, siri

ap = argparse.ArgumentParser(); ap.add_argument('chapter', type=int); ap.add_argument('--verse', type=int)
a = ap.parse_args()
for n, title, u in siri.verses(a.chapter):
    if a.verse and n != a.verse: continue
    print(f'{a.chapter}.{n}\t{title}\t{"".join(u)}')
    if a.verse:
        import csv, os
        r = next(r for r in csv.DictReader(open(os.path.join(siri.DATA, 'verses.csv'))) if int(r['chapter']) == a.chapter and int(r['verse']) == n)
        print(' '.join(str(x) for x in siri.stream(a.chapter)[int(r['first_rank']):int(r['last_rank']) + 1]))
