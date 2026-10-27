"""Command line: python -m siritools <command> [options]. Add --json to any command for machine-readable output."""
from __future__ import annotations

import argparse
import json
import sys

from . import align as _align
from . import audit as _audit
from . import columns as _columns
from . import data, find as _find, routes as _routes, script, search as _search, soundmap as _soundmap, stats


def _plain(x):
    """Make namedtuples, tuples and sets JSON-friendly."""
    if hasattr(x, '_asdict'):
        return {k: _plain(v) for k, v in x._asdict().items()}
    if isinstance(x, dict):
        return {str(k): _plain(v) for k, v in x.items()}
    if isinstance(x, (list, tuple, set)):
        return [_plain(v) for v in x]
    return x


def _emit(args, obj, text_fn):
    if args.json:
        print(json.dumps(_plain(obj), ensure_ascii=False, indent=1))
    else:
        text_fn(obj)


def _loc(l):
    return f'{l[0]}:r{l[1]}c{l[2]}'


# ---- read -------------------------------------------------------------------------------------------------------
def cmd_read(a):
    c = data.corpus()
    if a.chapter not in c.chapters():
        sys.exit(f'chapter {a.chapter} not found (1-{max(c.chapters())})')
    out = []
    for v, us in c.verse_units(a.chapter):
        if a.verse and v.number != a.verse:
            continue
        codes = c.verse_codes(v)
        row = {'chapter': a.chapter, 'verse': v.number, 'title': v.title, 'roman': ''.join(u.text for u in us),
               'units': len(us)}
        if a.kannada:
            row['kannada'] = script.kannada(codes)
        if a.verse:
            row['numbers'] = list(codes)
            row['locations'] = [[_loc(l) for l in c.unit_locations(a.chapter, u)] for u in us]
            row['unit_list'] = [u.text for u in us]
        out.append(row)
    if a.verse and not out:
        sys.exit(f'chapter {a.chapter} has no verse {a.verse}')

    def show(rows):
        for r in rows:
            print(f"{r['chapter']}.{r['verse']}\t{r['title']}\t{r['roman']}")
            if 'kannada' in r:
                print(f"\t{r['kannada']}")
            if 'numbers' in r:
                print(' '.join(map(str, r['numbers'])))
                print('first cells:', ' | '.join(' '.join(x) for x in r['locations'][:6]), '...')
    _emit(a, out, show)


# ---- route ------------------------------------------------------------------------------------------------------
def cmd_route(a):
    region = None
    if a.square:
        br, bc = divmod(a.square - 1, 3)
        region = (br * 9, bc * 9, 9)
    elif a.region:
        region = tuple(int(x) for x in a.region.split(','))
    page = a.page_id if a.page_id else a.page
    r = _routes.read(a.chapter, page, a.route, region, a.cells, a.reverse)

    def show(r):
        print(f'chapter {r.chapter} page {r.page} route {r.route} region {r.region} ({len(r.cells)} cells)')
        print('numbers :', ' '.join(map(str, r.numbers[:a.limit])), '...' if len(r.numbers) > a.limit else '')
        print('roman   :', r.roman[:a.limit * 3])
        print('kannada :', r.kannada[:a.limit * 3])
        print('cells   :', ' '.join(f'r{x}c{y}' for x, y in r.cells[:12]), '...')
    _emit(a, r, show)


# ---- walk -------------------------------------------------------------------------------------------------------
def cmd_walk(a):
    f, n = _find.find(a.chapter, a.pages)

    def show(f):
        print(f'chapter {f.chapter}: {len(f.pages)} pages, {n} walks tried; reading rows left to right gives {f.rows_entropy:.3f} bits')
        for w in f.walks:
            print(f'  {w.entropy:.3f} bits  start (row {w.start[0]}, col {w.start[1]}), step {w.step}, when taken {w.brk}')
        print('key found  ', _find.format_key(f.key))
        print('key stored ', _find.format_key(f.stored_key), '  match:', f.key == f.stored_key)
    f = f._replace(walks=[w._replace(path=w.path if a.json else None) for w in f.walks])
    _emit(a, f, show)


# ---- column -----------------------------------------------------------------------------------------------------
def cmd_column(a):
    ents = _columns.column(a.chapter, a.group, a.pos, a.dir)

    def show(ents):
        if a.provenance:
            for e in ents:
                print(_columns.describe(e))
        else:
            print(' '.join(e.text for e in ents))
    if a.json:
        _emit(a, [{'text': e.text, 'chapter': e.chapter, 'verse': e.verse, 'codes': e.unit.codes,
                   'ranks': e.unit.ranks, 'locations': [_loc(l) for l in e.locations]} for e in ents], None)
    else:
        show(ents)


# ---- align ------------------------------------------------------------------------------------------------------
def cmd_align(a):
    rows = data.hidden_texts()
    if a.passage is not None:
        row = rows[a.passage]
        rule = _columns.parse_rule(row['rule'], row['chapters'])
        ents = _columns.rule_column(rule)
        src = _audit.source_units(row)
        chs = [int(x) for x in row['chapters'].split()]
        label = f"passage {a.passage}: {row['verse']} ({row['language']}), rule: {row['rule']}"
    else:
        if a.chapter is None or not a.source:
            sys.exit('give --passage N, or a chapter with --source "text"')
        ents = _columns.column(a.chapter, a.group, a.pos, a.dir)
        src = script.text_units(a.source)
        chs = [a.chapter]
        label = f'chapter {a.chapter} {a.group} {a.pos} {a.dir}'
    aln = _align.align(ents, src, a.level)
    shuffle = stats.shuffle_test(ents, src, a.shuffles, a.seed, a.level) if a.shuffles else None
    decoy = None
    if a.decoys:
        pool = _audit.decoy_pool(chs, rows)
        decoy = stats.decoy_test(ents, src, pool, a.level)
    res = {'label': label, 'level': a.level, 'matches': aln.matches, 'score': aln.score, 'source_units': aln.source_len,
           'column_units': len(ents), 'span': [aln.start, aln.end], 'shuffle': shuffle, 'decoy': decoy,
           'summary': stats.summary(aln.matches, aln.source_len, shuffle, decoy)}
    top, mid, bot = _align.render(ents, src, aln)
    res['alignment'] = {'column': top, 'match': mid, 'source': bot}
    first = ents[aln.start] if aln.end > aln.start else None
    if first:
        res['first_unit'] = {'chapter': first.chapter, 'verse': first.verse, 'locations': [_loc(l) for l in first.locations]}

    def show(r):
        print(label)
        print(f"level {r['level']}: {r['matches']} of {r['source_units']} source units match (score {r['score']}); "
              f"column {r['column_units']} units, span {r['span'][0]}-{r['span'][1]}")
        print(' column :', top)
        print('         ', mid)
        print(' source :', bot)
        print(r['summary'])
    _emit(a, res, show)


# ---- search -----------------------------------------------------------------------------------------------------
def cmd_search(a):
    chs = [int(x) for x in a.chapters.split(',')] if a.chapters else None
    r = _search.search(a.query, a.where, chs, a.level)
    hits = r['hits']

    def show(r):
        print(f"query units: {' '.join(r['query_units'])}   hits: {len(hits)}   "
              f"expected by chance: stream {r.get('chance_stream', 0):.3g}, columns {r.get('chance_columns', 0):.3g}")
        for h in hits[:a.limit]:
            print(f'  ch.{h.chapter} {h.where} {h.place} #{h.index} v.{h.verse}  {_loc(h.locations[0])}  {h.text}')
        if len(hits) > a.limit:
            print(f'  ... {len(hits) - a.limit} more (use --limit)')
    _emit(a, r, show)


# ---- audit ------------------------------------------------------------------------------------------------------
def cmd_audit(a):
    idx = [int(x) for x in a.rows.split(',')] if a.rows else None
    res = _audit.audit(shuffles=a.shuffles, rows=idx)
    t = _audit.tally(res)

    def show(res):
        print(f"{'row':>3} {'verse':<7} {'ch':<9} {'stored':>6} {'ours':>5} {'loose':>5} {'src':>4}  status   grid-run"
              + ('  shuffle-max' if a.shuffles else ''))
        for r in res:
            print(f'{r.index:>3} {r.verse:<7} {r.chapters:<9} {r.stored:>6} {r.ours if r.ours is not None else "-":>5} '
                  f'{r.ours_loose if r.ours_loose is not None else "-":>5} {r.source_len:>4}  {r.status:<8} '
                  f"{'found' if r.grid_found else 'NOT FOUND':<9}{'' if not r.error else ' ' + r.error}"
                  + (f'  {r.shuffle_max}' if a.shuffles else ''))
        print('tally:', t)
        bad = [r for r in res if r.status != 'exact']
        print('mismatches:', 'none' if not bad else ', '.join(f'row {r.index} stored {r.stored} ours {r.ours}' for r in bad))
    _emit(a, {'tally': t, 'rows': res}, lambda o: show(res))


# ---- soundmap ---------------------------------------------------------------------------------------------------
def cmd_soundmap(a):
    chs = [int(x) for x in a.chapters.split(',')] if a.chapters else None
    r = _soundmap.test(chs, a.trials, a.seed)

    def show(r):
        print(f"chapters {r['chapters']}, {r['numbers']} numbers, {r['trials']} shuffled tables")
        print(f"{'rate':<12} {'real':>7} {'shuffled mean':>14} {'shuffled max':>13} {'shuffles beaten':>16}")
        for k in ('cv_rate', 'sign_legal', 'legal'):
            s = r['shuffles'][k]
            print(f"{k:<12} {r['real'][k]:>7.3f} {s['mean']:>14.3f} {s['max']:>13.3f} {s['beaten']:>8}/{r['trials']}")
    _emit(a, r, show)


def build_parser():
    p = argparse.ArgumentParser(prog='python -m siritools', description='Read, test and search the Siribhuvalaya number grids.')
    sub = p.add_subparsers(dest='cmd', required=True, metavar='command')

    def add(name, fn, help_, desc=None):
        sp = sub.add_parser(name, help=help_, description=desc or help_)
        sp.add_argument('--json', action='store_true', help='print JSON instead of text')
        sp.set_defaults(fn=fn)
        return sp

    s = add('read', cmd_read, 'verses of a chapter rebuilt from the numbers',
            'Print the verses of a chapter in Roman letters; with --verse, also its numbers and the cell of each letter.')
    s.add_argument('chapter', type=int)
    s.add_argument('--verse', type=int, help='one verse, with its numbers and cell locations')
    s.add_argument('--kannada', action='store_true', help='also print Kannada script')

    s = add('route', cmd_route, 'read a page along a route or shape',
            'Read a page (or a 9 x 9 square) along a route. Routes: ' + ', '.join(_routes.ROUTES) + '.')
    s.add_argument('chapter', type=int)
    s.add_argument('page', type=int, nargs='?', default=1, help='page index within the chapter, from 1 (default 1)')
    s.add_argument('--page-id', help='page id as in grids.csv instead of the index')
    s.add_argument('--route', default='rows', choices=_routes.ROUTES)
    s.add_argument('--square', type=int, choices=range(1, 10), help='read only 9 x 9 square 1-9 (row-major)')
    s.add_argument('--region', help='row,col,size of a square region, counted from 0')
    s.add_argument('--cells', help='custom route: "r,c r,c ..." counted from 0 inside the region')
    s.add_argument('--reverse', action='store_true')
    s.add_argument('--limit', type=int, default=40, help='numbers to show in text output')

    s = add('walk', cmd_walk, "recover a chapter's walk and key from the numbers",
            "Try all 3,888 square-walks and pick the one that makes the numbers most predictable, then find the key (order of the nine squares). Takes about ten seconds.")
    s.add_argument('chapter', type=int)
    s.add_argument('--pages', type=int, nargs='+', help='only these page indexes (weaker evidence)')

    s = add('column', cmd_column, 'one letter from each verse of a chapter',
            'Take one letter from each verse (position S1 = first, E1 = last, E2 = second from last ...) and read them in order.')
    s.add_argument('chapter', type=int)
    s.add_argument('--group', default='all', choices=_columns.GROUPS)
    s.add_argument('--pos', default='E1')
    s.add_argument('--dir', default='down', choices=_columns.DIRECTIONS)
    s.add_argument('--provenance', action='store_true', help='one line per letter: chapter, verse, cells')

    s = add('align', cmd_align, 'align a column with a known text and test it',
            'Align a column with a source text (units, match +2 / mismatch -1 / gap -2), with optional shuffle and decoy tests. '
            'Use --passage N for row N of data/hidden_texts.csv, or give a chapter and --source.')
    s.add_argument('chapter', type=int, nargs='?')
    s.add_argument('--passage', type=int, help='row of hidden_texts.csv, from 0')
    s.add_argument('--source', help='source text (Roman, Devanagari or Kannada)')
    s.add_argument('--group', default='all', choices=_columns.GROUPS)
    s.add_argument('--pos', default='E1')
    s.add_argument('--dir', default='down', choices=_columns.DIRECTIONS)
    s.add_argument('--level', default='exact', choices=script.LEVELS)
    s.add_argument('--shuffles', type=int, default=0, help='shuffle trials (0 = none)')
    s.add_argument('--decoys', action='store_true', help='also align against the sources of the passages of hidden_texts.csv not known to be in this chapter, as decoys')
    s.add_argument('--seed', type=int, default=1)

    s = add('search', cmd_search, 'search a string in every chapter and every column rule',
            'Search a Roman or Kannada string in the reading stream of every chapter and in every column rule.')
    s.add_argument('query')
    s.add_argument('--where', default='both', choices=['stream', 'columns', 'both'])
    s.add_argument('--chapters', help='comma list, e.g. 15,16 (default all)')
    s.add_argument('--level', default='exact', choices=script.LEVELS)
    s.add_argument('--limit', type=int, default=20)

    s = add('audit', cmd_audit, 'rebuild and re-score every passage in hidden_texts.csv',
            'Rebuild all 68 passages from their rules and the raw numbers and compare with the stored letters_matched.')
    s.add_argument('--rows', help='comma list of row numbers (default all)')
    s.add_argument('--shuffles', type=int, default=0, help='also run this many shuffles per row (slow)')

    s = add('soundmap', cmd_soundmap, 'test the 1-64 sound table against shuffled tables',
            'Compare how legal the stream is under the real vowel / consonant / sign split and under shuffled splits.')
    s.add_argument('--chapters', help='comma list (default 15,25,35,45,55)')
    s.add_argument('--trials', type=int, default=1000)
    s.add_argument('--seed', type=int, default=1)
    return p


def main(argv=None):
    a = build_parser().parse_args(argv)
    a.fn(a)


if __name__ == '__main__':
    main()
