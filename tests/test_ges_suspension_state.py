"""Contrat du catalogue Gestes : réécriture sourcée et datée, non traités vides."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('patch_0099', ROOT / 'tools/patches/0099-suspendre-gestes.py')
patch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(patch)


class GestesSuspendus(unittest.TestCase):
    def test_gestes_reecrits_sources_et_dates(self):
        """Réécriture ordonnée par Vial (20.10.2026) : tout geste réécrit porte une source lue et datée ;
        tout geste non traité reste vide (g == n == '')."""
        import re
        app = (ROOT / 'app_v2.html').read_text()
        _, _, regions = patch.ges_span(app)
        self.assertEqual(len(regions), 22)
        items = [item for region in regions for item in region['items']]
        self.assertEqual(len(items), 315)
        keys = [item['k'] for item in items]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertTrue(all(isinstance(i['s'], str) and i['s'] and 'p' in i for i in items))
        lu = re.compile(r'lu le \d{2}\.\d{2}\.\d{4}')
        for i in items:
            if i['g'] or i['n']:
                self.assertTrue(i['g'] and i['n'], i['k'])
                self.assertRegex(i.get('src', ''), lu, i['k'])

    def test_renvois_et_identifiants_resolus(self):
        _, _, regions = patch.ges_span((ROOT / 'app_v2.html').read_text())
        by_id = {region['id']: region for region in regions}
        self.assertEqual(len(by_id), 22)
        by_key = {item['k']: item for region in regions for item in region['items']}
        self.assertIn('peau_0', by_key)
        for region in regions:
            for item in region['items']:
                for rid, title in item.get('x', []):
                    self.assertTrue(any(peer['s'] == title for peer in by_id[rid]['items']))

    def test_pluriel_reconnu_par_reference_singuliere(self):
        spec = importlib.util.spec_from_file_location('lyncee', ROOT / 'tools/lyncee.py')
        lyncee = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(lyncee)
        pending = {'intra-articulaires': ['intra-articulaires', 2, 'TIP.S8.4.c[7]'],
                   'autres-termes': ['autres-termes', 1, 'test']}
        result = lyncee.rattacher_pluriels_reference(pending, {'intra-articulaire'})
        self.assertIn('intra-articulaire', result)
        self.assertNotIn('intra-articulaires', result)
        self.assertIn('autres-termes', result)
        self.assertEqual(result['intra-articulaire'][1], 2)

    def test_asset_revisable_et_statut_visible(self):
        app = (ROOT / 'app_v2.html').read_text()
        asset = (ROOT / 'assets/config/fonctions.js').read_text()
        self.assertEqual(patch.sha(asset), patch.ASSET_NEW_SHA)
        self.assertEqual(patch.sha(patch.restore_asset(asset)), patch.ASSET_OLD_SHA)
        self.assertIn(patch.NEW_PANEL, app)
        self.assertIn(patch.NEW_SOURCE, app)
        self.assertIn('coches historiques conservées', asset)
        self.assertIn('disabled aria-label=', asset)
        self.assertIn('Gestes · contenu en reconstruction', asset)


if __name__ == '__main__':
    unittest.main()
