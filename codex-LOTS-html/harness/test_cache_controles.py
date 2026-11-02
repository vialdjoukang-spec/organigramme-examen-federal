"""Tests réels du validateur fourni, sans réseau ni écritures hors codex."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import cache_controles as c


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=c.D, prefix='.test-cache-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.lot = self.root / 'LOT_133'
        self.lot.mkdir()
        self.cache = self.root / 'cache'
        self.validator = self.root / 'validator/controle_lot.py'
        self.validator.parent.mkdir()
        self.validator.write_bytes(c.VALIDATEUR.read_bytes())
        self.canonical = self.lot / 'LISTE_DX_CANONIQUE.md'
        self.canonical.write_text('\n'.join(f'DX.{i} — Sujet{i}' for i in range(1, 11)))
        for i in range(11):
            name = 'LOT_133_Phase_A_V0.html' if i == 0 else f'LOT_133_Phase_B_V0_DX.{i}.html'
            body = (' '.join(f'Sujet{j}' for j in range(1, 11)) if i == 0 else
                    f'<h2>DX.{i} — Sujet{i}</h2>' + ''.join(
                        f'<h3 id="dx{i}-p{j}">{j}. Point</h3><p>CONTENU{j}</p>' for j in range(1, 15)))
            padding = ('<p>' + 'x' * 1000 + '</p>\n') * 80
            (self.lot / name).write_text('<!DOCTYPE html>\n<html><body>' + body +
                '<p>[S1] non validé cliniquement</p>\n' + padding +
                '</body></html>\n<!-- FIN_FICHIER test -->', encoding='utf-8')

    def test_v8_extract_includes_only_linked_windows(self):
        p = self.root / 'v8.html'
        p.write_text('<section><h2 id="a-p9">9. Examens</h2><button popovertarget="w9">source</button></section>'
                     '<div id="w9" popover>DETAIL9<button popovertarget="sub">nested</button><button popovertarget="w9" popovertargetaction="hide">close</button></div>'
                     '<div id="sub" popover>SOUSFENETRE</div><div id="w8" popover>NONDEMANDE</div>')
        text = c.extraire(p, [9])
        self.assertIn('DETAIL9', text)
        self.assertIn('SOUSFENETRE', text)
        self.assertNotIn('NONDEMANDE', text)
        with self.assertRaises(ValueError):
            c.extraire(p, [8, 9])
        p.write_text(p.read_text().replace('a-p9', 'dx6-p9'))
        self.assertIn('DETAIL9', c.extraire(p, [9], True))

    def run_check(self, **kw):
        return c.verifier(self.lot, self.cache, validateur=self.validator, **kw)

    def test_real_success_and_cache_hit_without_validator_execution(self):
        first = self.run_check()
        self.assertEqual(first['cache'], 'calcule')
        self.assertEqual(first['resultat']['critiques_lot'], [])
        self.assertTrue(all(not f['critiques'] for f in first['resultat']['fichiers']))
        with patch.object(c, 'charger', side_effect=AssertionError('exécution superflue')):
            second = self.run_check()
        self.assertEqual(second['cache'], 'reutilise')
        self.assertEqual(second['resultat'], first['resultat'])

    def test_html_and_file_inventory_invalidate(self):
        first = self.run_check()
        file = next(self.lot.glob('*DX.1.html'))
        file.write_text(file.read_text().replace('[S1]', '[S9]'))
        second = self.run_check()
        self.assertNotEqual(first['cle'], second['cle'])
        self.assertTrue(any(f['critiques'] for f in second['resultat']['fichiers']))
        file.unlink()
        third = self.run_check()
        self.assertNotEqual(second['cle'], third['cle'])
        self.assertTrue(third['resultat']['critiques_lot'])

    def test_canonical_invalidation(self):
        first = self.run_check()
        self.canonical.write_text(self.canonical.read_text().replace('Sujet1', 'Different1'))
        second = self.run_check()
        self.assertNotEqual(first['cle'], second['cle'])
        self.assertTrue(second['resultat']['critiques_lot'])

    def test_validator_change_same_version_invalidation(self):
        first = self.run_check()
        self.validator.write_text(self.validator.read_text().replace('BANDE_MIN, BANDE_MAX = 80_000',
                                                                  'BANDE_MIN, BANDE_MAX = 90_000'))
        second = self.run_check()
        self.assertNotEqual(first['cle'], second['cle'])
        self.assertTrue(second['resultat']['critiques_lot'])

    def test_dependencies_and_options_invalidate(self):
        dep = self.root / 'policy.json'
        dep.write_text('{}')
        first = self.run_check(dependances=[dep])
        dep.write_text('{"rev":2}')
        second = self.run_check(dependances=[dep])
        self.assertNotEqual(first['cle'], second['cle'])
        neighbor = self.validator.parent / 'helper.py'
        neighbor.write_text('VERSION = 1\n')
        third = self.run_check(dependances=[dep])
        self.assertNotEqual(second['cle'], third['cle'])
        fourth = self.run_check(dependances=[dep], sans_nom=True)
        self.assertNotEqual(third['cle'], fourth['cle'])

    def test_corrupt_or_modified_cache_recomputed(self):
        first = self.run_check()
        cachefile = self.cache / (first['cle'] + '.json')
        cachefile.write_text('{')
        self.assertEqual(self.run_check()['cache'], 'calcule')
        obj = json.loads(cachefile.read_text())
        obj['resultat']['critiques_lot'] = ['faux résultat']
        cachefile.write_text(json.dumps(obj))
        self.assertEqual(self.run_check()['resultat']['critiques_lot'], [])

    def test_targeted_extraction(self):
        file = next(self.lot.glob('*DX.1.html'))
        output = c.extraire(file, [2, 4], validateur=self.validator)
        self.assertIn('CONTENU2', output)
        self.assertIn('CONTENU4', output)
        self.assertNotIn('CONTENU3', output)
        with self.assertRaises(ValueError):
            c.extraire(file, [15], validateur=self.validator)

    def test_activity_attribution_and_bad_line(self):
        source = self.root / 'agents.jsonl'
        source.write_text('{"agent":"sol","statut":"termine"}\n'
                          '{"producteur":"astra","tache":"audit"}\n'
                          '{"modele":"sol"}\n{bad}\n')
        report = c.activite([source])
        self.assertEqual(set(report['agents']), {'sol', 'astra', 'non_attribue'})
        self.assertEqual(report['agents']['astra']['evenements'], 1)
        self.assertEqual(report['erreurs'][0]['ligne'], 4)


if __name__ == '__main__':
    unittest.main()
