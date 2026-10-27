"""Apply one correction issue to the text, for the correction workflow.

Reads the issue from the GitHub event file (GITHUB_EVENT_PATH, or a path given as the first argument), finds the
verse, and writes the suggested Kannada, Roman words or English into:
  data/siribhuvalaya.csv          the downloadable text
  site/data/verses_*.json         the website's chapter pages (and the reader is credited on the verse)
  site/data/search_index.json     the website's search
  data/corrections.csv            one row per changed field: date, issue, reader, chapter, verse, field, old, new
Writes `branch`, `title` and `summary` to GITHUB_OUTPUT. Exits 1 with a message (summary.md) if the issue is unusable.
Issue text is untrusted: it is only ever read as data here, never passed to a shell.
"""
import csv, datetime, glob, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIELDS = {  # issue form label -> (csv column, site json key)
    'Corrected Kannada': ('kannada', 'kannada'),
    'Corrected Roman words': ('kannada_words_romanised', 'restored'),
    'Corrected English': ('english_draft', 'translation'),
}
MAX = 3000


def fail(msg):
    open(os.path.join(ROOT, 'summary.md'), 'w', encoding='utf-8').write(msg + '\n')
    print(msg, file=sys.stderr); sys.exit(1)


def clean(s):
    s = unicodedata.normalize('NFC', s or '').replace('\r\n', '\n').strip()
    s = ''.join(ch for ch in s if ch in '\n\t' or unicodedata.category(ch)[0] != 'C' or ch in '‌‍')
    s = re.sub(r'\s+', ' ', s).strip()
    return '' if s in ('_No response_', 'None') else s


def sections(body):
    """Issue-form bodies are '### Label' followed by the answer."""
    out, cur = {}, None
    for line in (body or '').splitlines():
        m = re.match(r'^###\s+(.+?)\s*$', line)
        if m: cur = m.group(1); out[cur] = []
        elif cur: out[cur].append(line)
    return {k: clean('\n'.join(v)) for k, v in out.items()}


def main():
    ev = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.environ['GITHUB_EVENT_PATH'], encoding='utf-8'))
    issue = ev['issue']; num = int(issue['number']); user = issue['user']['login']
    f = sections(issue.get('body'))
    m = re.fullmatch(r'(\d{1,2})\s*[.:,]\s*(\d{1,4})', f.get('Chapter and verse', ''))
    if not m: fail('Could not read "Chapter and verse". Please write it as chapter.verse, for example 15.1.')
    ch, vn = int(m.group(1)), int(m.group(2))
    new = {k: f.get(k, '') for k in FIELDS if f.get(k)}
    if not new: fail('No correction given. Fill in at least one of: ' + ', '.join(FIELDS) + '.')
    for k, t in new.items():
        if len(t) > MAX: fail(f'"{k}" is longer than {MAX} characters.')

    # Downloadable text.
    path = os.path.join(ROOT, 'data', 'siribhuvalaya.csv')
    with open(path, encoding='utf-8-sig', newline='') as fh:
        rd = csv.DictReader(fh); cols = rd.fieldnames; rows = list(rd)
    row = next((r for r in rows if int(r['chapter']) == ch and int(r['verse']) == vn), None)
    if row is None: fail(f'There is no verse {vn} in chapter {ch}.')
    changes = []
    for k, t in new.items():
        col = FIELDS[k][0]
        if row[col] != t: changes.append((k, row[col], t)); row[col] = t
    if not changes: fail('The suggested text is the same as the current text.')
    with open(path, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, cols); w.writeheader(); w.writerows(rows)

    # Website chapter data and search.
    for jp in glob.glob(os.path.join(ROOT, 'site', 'data', 'verses_*.json')):
        V = json.load(open(jp, encoding='utf-8')); hit = False
        for v in V:
            if v['chapter'] == ch and v['n'] == vn:
                for k, _, t in changes: v[FIELDS[k][1]] = t
                v['corrected_by'] = sorted(set(v.get('corrected_by', [])) | {user}); hit = True
        if hit: json.dump(V, open(jp, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    sp = os.path.join(ROOT, 'site', 'data', 'search_index.json')
    if os.path.exists(sp):
        S = json.load(open(sp, encoding='utf-8'))
        for h in S:
            if h[0] == ch and h[1] == vn: h[2], h[3] = row['kannada'], row['english_draft']
        json.dump(S, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))

    # Log.
    lp = os.path.join(ROOT, 'data', 'corrections.csv'); first = not os.path.exists(lp)
    with open(lp, 'a', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        if first: w.writerow(['date', 'issue', 'reader', 'chapter', 'verse', 'field', 'old', 'new'])
        for k, old, t in changes: w.writerow([datetime.date.today().isoformat(), num, user, ch, vn, FIELDS[k][0], old, t])

    summary = '\n'.join(f'**{k}**\n\nWas: {old or "(empty)"}\n\nNow: {t}\n' for k, old, t in changes)
    open(os.path.join(ROOT, 'summary.md'), 'w', encoding='utf-8').write(
        f'Correction to chapter {ch}, verse {vn}, suggested by @{user} in #{num}.\n\n{summary}\nCloses #{num}\n')
    out = os.environ.get('GITHUB_OUTPUT')
    if out:
        with open(out, 'a') as fh:
            fh.write(f'branch=correction-{num}\ntitle=Correction: chapter {ch}, verse {vn} (#{num})\n')
    print(f'chapter {ch} verse {vn}: ' + ', '.join(k for k, _, _ in changes))


if __name__ == '__main__':
    main()
