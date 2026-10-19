"""Contrat temporaire du catalogue Gestes pendant la reconstruction."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('patch_0099', ROOT / 'tools/patches/0099-suspendre-gestes.py')
patch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(patch)


class GestesSuspendus(unittest.TestCase):
    def test_cle_et_ordre_conserves(self):
        app = (ROOT / 'app_v2.html').read_text()
        start, end, regions = patch.ges_span(app)
        self.assertEqual(patch.sha(app[start:end]), patch.GES_NEW_SHA)
        self.assertEqual(len(regions), 22)
        items = [item for region in regions for item in region['items']]
        self.assertEqual(len(items), 315)
        keys = [item['k'] for item in items]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertTrue(all(isinstance(item['s'], str) and item['s'] and item['g'] == item['n'] == '' for item in items))
        self.assertTrue(all('p' in item for item in items))
        self.assertEqual(patch.transform(app, (ROOT / 'assets/config/fonctions.js').read_text())[0], app)

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
