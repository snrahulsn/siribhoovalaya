"""Tests with real data. Run from the repository root:  python -m unittest"""
import contextlib
import io
import json
import unittest

from siritools import align, audit, cli, columns, data, find, routes, script, search, soundmap, stats

C = None


def setUpModule():
    global C
    C = data.corpus()


class TestScript(unittest.TestCase):
    def test_sounds(self):
        self.assertEqual(script.sound(1), 'a')
        self.assertEqual(script.sound(28), 'k')
        self.assertEqual(script.sound(60), 'h')
        self.assertEqual(script.sound(61), 'ṃ')
        self.assertEqual(script.kind(0), 'unreadable')

    def test_units_and_roman(self):
        # k+a, bare m, then vowel with anusvara
        self.assertEqual([u.text for u in script.units([28, 1, 52, 4, 61])], ['ka', 'mi' + 'ṃ'])
        self.assertEqual(script.roman([28, 28, 1]), 'kka')
        self.assertEqual(script.roman([0, 1]), '?a')

    def test_kannada(self):
        self.assertEqual(script.kannada([28, 1]), 'ಕ')
        self.assertEqual(script.kannada([28, 2]), 'ಕಾ')
        self.assertEqual(script.kannada([28]), 'ಕ್')

    def test_parse_roundtrip(self):
        us = script.text_units('buddhiyukto jahātīha')
        self.assertEqual([u.text for u in us][:6], ['bu', 'd', 'dhi', 'yu', 'k', 'to'])
        self.assertEqual([u.text for u in script.text_units('ಕಾವ್ಯ')], ['kā', 'v', 'ya'])

    def test_norm_levels(self):
        self.assertEqual(script.norm('tō'), 'to')
        self.assertEqual(script.norm('hāṃ', 'loose'), 'ha')
        self.assertEqual(script.norm('hāṃ', 'exact'), 'hāṃ')
        self.assertEqual(script.norm('…'), '?')


class TestData(unittest.TestCase):
    def test_shape(self):
        self.assertEqual(len(C.chapters()), 59)
        self.assertEqual(len(C.pages(15)), 14)
        self.assertEqual(len(C.stream(15)), 14 * 729)

    def test_ranks_and_alphabet(self):
        p = C.page(15, 1)
        self.assertEqual(sorted(p.ranks)[0] >= 0, True)
        self.assertEqual(len(set(C.stream(15))) > 30, True)

    def test_location_matches_grid(self):
        for rank in (0, 1, 500, 10000):
            loc = C.location(15, rank)
            page = C.page(15, loc.page)
            self.assertEqual(page.cells[(loc.row - 1) * 27 + loc.col - 1], C.stream(15)[rank])

    def test_verses_cover_stream(self):
        vs = C.verses(15)
        self.assertEqual(len(vs), 275)
        self.assertEqual(vs[0].first, 0)
        self.assertEqual(sum(v.last - v.first + 1 for v in vs), len(C.stream(15)))

    def test_verse_units_carry_ranks(self):
        v, us = C.verse_units(15)[0]
        self.assertEqual(us[0].ranks[0], v.first)
        self.assertTrue(all(isinstance(l, tuple) for l in C.unit_locations(15, us[0])))

    def test_readings_and_symbols(self):
        self.assertEqual(len(data.symbols()), 64)
        self.assertIn((15, 1), data.readings())


class TestRoutes(unittest.TestCase):
    def test_rows_equals_page(self):
        r = routes.read(15, 1, 'rows')
        self.assertEqual(r.numbers, C.page(15, 1).cells)
        self.assertEqual(r.cells[0], (1, 1))
        self.assertEqual(r.cells[28], (2, 2))

    def test_shapes_cover_every_cell_once(self):
        for name in ('rows', 'columns', 'snake', 'diagonals', 'antidiagonals', 'spiral-in', 'spiral-out'):
            cells = routes.route_cells(name, 9)
            self.assertEqual(len(cells), 81, name)
            self.assertEqual(len(set(cells)), 81, name)

    def test_snake_and_spiral(self):
        s = routes.route_cells('snake', 3)
        self.assertEqual(s, [(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2)])
        self.assertEqual(routes.route_cells('spiral-in', 3)[-1], (1, 1))
        self.assertEqual(routes.route_cells('spiral-out', 3)[0], (1, 1))

    def test_knight_moves_are_knight_moves(self):
        k = routes.route_cells('knight', 8)
        self.assertGreater(len(k), 50)
        for (a, b), (c, d) in zip(k, k[1:]):
            self.assertEqual(sorted((abs(a - c), abs(b - d))), [1, 2])

    def test_custom_and_region_and_units(self):
        r = routes.read(15, 1, 'custom', custom='0,0 0,1 1,1', region=(9, 9, 9))
        self.assertEqual(r.cells, [(10, 10), (10, 11), (11, 11)])
        p = C.page(15, 1)
        self.assertEqual(r.numbers, [p.cells[9 * 27 + 9], p.cells[9 * 27 + 10], p.cells[10 * 27 + 10]])
        self.assertEqual(r.roman, script.roman(r.numbers))
        with self.assertRaises(ValueError):
            routes.read(15, 1, 'custom', custom='0,9', region=(0, 0, 9))

    def test_reverse(self):
        self.assertEqual(routes.route_cells('rows', 4, reverse=True)[0], (3, 3))


class TestColumnsAndRules(unittest.TestCase):
    def test_parse_rule(self):
        r = columns.parse_rule('second-to-last letter of every verse, read up', '18')
        self.assertEqual((r.segments[0].pos, r.segments[0].group, r.direction), ('E2', 'all', 'up'))
        r = columns.parse_rule('first letter of every long verse, read down', '33')
        self.assertEqual((r.segments[0].pos, r.segments[0].group), ('S1', 'long'))
        r = columns.parse_rule('fifth letter from the end of every long verse, chapters 49, 48 and 47, read up', '49 48 47')
        self.assertEqual([s.chapter for s in r.segments], [49, 48, 47])
        self.assertEqual(r.segments[0].pos, 'E5')
        r = columns.parse_rule('last letter of every short verse of chapter 57, running on into every verse of chapter 58, read down', '57 58')
        self.assertEqual([(s.chapter, s.group) for s in r.segments], [(57, 'short'), (58, 'all')])
        with self.assertRaises(ValueError):
            columns.parse_rule('nonsense', '1')

    def test_ch15_last_column_contains_stored_run(self):
        row = data.hidden_texts()[0]
        run = [x for x in row['grid_letters'].split() if x != '-']
        col = columns.texts(columns.column(15, 'all', 'E1', 'down'))
        self.assertTrue(any(col[k:k + len(run)] == run for k in range(len(col))))

    def test_provenance(self):
        e = columns.column(15, 'all', 'E1', 'down')[0]
        self.assertEqual((e.chapter, e.verse), (15, 1))
        v = C.verse(15, 1)
        self.assertEqual(e.unit.ranks[-1], v.last)
        self.assertEqual(e.locations[-1], C.location(15, v.last))

    def test_up_is_reverse_and_groups_split(self):
        down = columns.column(15, 'all', 'E1', 'down')
        up = columns.column(15, 'all', 'E1', 'up')
        self.assertEqual([e.text for e in down], [e.text for e in up][::-1])
        n = len(columns.column(15, 'long', 'E1')) + len(columns.column(15, 'short', 'E1'))
        self.assertEqual(n, len(down))


class TestAlignStats(unittest.TestCase):
    def test_simple_alignment(self):
        a = align.align(['x', 'a', 'b', 'c', 'y'], ['a', 'b', 'c'])
        self.assertEqual((a.matches, a.score, a.start, a.end), (3, 6, 1, 4))
        a = align.align(['a', 'c'], ['a', 'b', 'c'])
        self.assertEqual((a.matches, a.score), (2, 2))          # 2 + 2 - gap 2

    def test_unreadable_never_matches(self):
        self.assertEqual(align.align(['?'], ['?']).matches, 0)

    def test_passage_zero_matches_stored(self):
        row = data.hidden_texts()[0]
        ents = columns.rule_column(columns.parse_rule(row['rule'], row['chapters']))
        src = audit.source_units(row)
        a = align.align(ents, src)
        self.assertEqual(a.matches, int(row['letters_matched']))
        self.assertEqual(a.matches, 32)
        self.assertEqual(a.source_len, 41)

    def test_shuffle_and_decoy_tests(self):
        rows = data.hidden_texts()
        row = rows[0]
        ents = columns.rule_column(columns.parse_rule(row['rule'], row['chapters']))
        src = audit.source_units(row)
        sh = stats.shuffle_test(ents, src, trials=20, seed=3)
        self.assertEqual(sh['matches'], 32)
        self.assertEqual(sh['shuffle_ge'], 0)
        self.assertLess(sh['shuffle_max'], 20)
        dec = stats.decoy_test(ents, src, audit.decoy_pool([15], rows))
        self.assertEqual(dec['decoy_ge'], 0)
        self.assertGreater(dec['decoys'], 10)
        self.assertIn('beats every shuffle and decoy', stats.summary(32, 41, sh, dec))

    def test_decoy_record(self):
        recs = stats.decoy_record()
        self.assertEqual(len(recs), 42)
        self.assertTrue(all(r['decoys_ge'] == 0 for r in recs))


class TestSearch(unittest.TestCase):
    def test_stream_hit_has_location(self):
        # take 4 units from the middle of chapter 15's first verse and find them again
        v, us = C.verse_units(15)[0]
        q = ''.join(u.text for u in us[5:9])
        r = search.search(q, 'stream', [15])
        hit = next(h for h in r['hits'] if h.index == 5)
        self.assertEqual(hit.verse, 1)
        self.assertEqual(hit.locations[0], C.location(15, us[5].ranks[0]))

    def test_column_hit(self):
        r = search.search('yukto jahātīha', 'columns', [15])
        places = {h.place for h in r['hits']}
        self.assertIn('all E1 down', places)

    def test_kannada_query_and_levels(self):
        r1 = search.search('ಜಿನೇನ್ದ್ರ', 'stream', [1, 2, 3])
        self.assertEqual(r1['query_units'], ['ji', 'ne', 'n', 'd', 'ra'])
        self.assertGreaterEqual(len(r1['hits']), 3)
        loose = search.search('jinendra', 'stream', [1], level='loose')
        self.assertGreaterEqual(len(loose['hits']), 1)


class TestFind(unittest.TestCase):
    def test_chapter_15_walk_and_key(self):
        f, n = find.find(15)
        self.assertEqual(n, 3888)
        w = f.walks[0]
        self.assertEqual((w.start, w.step, w.brk), ((0, 4), (-1, 1), (1, 0)))
        self.assertEqual(f.key, [5, 6, 7, 1, 4, 8, 3, 2, 9])
        self.assertEqual(f.key, f.stored_key)
        self.assertLess(w.entropy, f.rows_entropy - 0.5)


class TestSoundmap(unittest.TestCase):
    def test_real_table_beats_shuffled_tables(self):
        r = soundmap.test([15, 25], trials=200, seed=2)
        self.assertEqual(r['shuffles']['legal']['beaten'], 200)
        self.assertGreater(r['real']['cv_rate'], 0.7)


class TestAudit(unittest.TestCase):
    def test_all_68_rows(self):
        res = audit.audit()
        self.assertEqual(len(res), 68)
        self.assertEqual(audit.tally(res), {'exact': 68})
        self.assertTrue(all(r.grid_found for r in res))

    def test_known_passage_reproduces_letters_matched(self):
        r = audit.audit(rows=[27])[0]
        self.assertEqual((r.verse, r.stored, r.ours, r.status), ('11.28', 47, 47, 'exact'))


class TestCli(unittest.TestCase):
    def run_cli(self, *argv):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            cli.main(list(argv))
        return buf.getvalue()

    def test_column_json(self):
        out = json.loads(self.run_cli('column', '15', '--json'))
        self.assertEqual(out[0]['chapter'], 15)
        self.assertEqual(out[0]['verse'], 1)

    def test_read_verse(self):
        out = self.run_cli('read', '15', '--verse', '1')
        self.assertTrue(out.startswith('15.1'))

    def test_route_json(self):
        out = json.loads(self.run_cli('route', '15', '1', '--route', 'snake', '--json'))
        self.assertEqual(len(out['numbers']), 729)

    def test_align_passage(self):
        out = self.run_cli('align', '--passage', '0')
        self.assertIn('32 of 41', out)

    def test_audit_rows_and_search_and_soundmap(self):
        self.assertIn('tally: {\'exact\': 2}', self.run_cli('audit', '--rows', '0,1'))
        self.assertIn('hits:', self.run_cli('search', 'jinendra', '--chapters', '1'))
        self.assertIn('legal', self.run_cli('soundmap', '--chapters', '15', '--trials', '20'))

    def test_help_lists_all_commands(self):
        h = cli.build_parser().format_help()
        for cmd in ('read', 'route', 'walk', 'column', 'align', 'search', 'audit', 'soundmap'):
            self.assertIn(cmd, h)


if __name__ == '__main__':
    unittest.main()
