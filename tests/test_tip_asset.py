"""Identité du corpus TIP, corruption, migration et lecture des publications anciennes."""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from tip_data import ASSET, TAG, SHARDS, from_js, load, render


class TipAsset(unittest.TestCase):
    def test_sources_et_asset_identiques_apres_edition(self):
        after = (ROOT / 'app_v2.html').read_text()
        asset = (ROOT / ASSET).read_text()
        original = from_js(asset)
        self.assertEqual(load(ROOT, after), original)
        self.assertEqual(asset, render(original))
        self.assertEqual((len(original), sum(len(x['c']) for x in original.values())), (248, 3472))

    def test_corruption_et_perte_dun_fichier_bloquent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'assets/config').mkdir(parents=True)
            shutil.copytree(ROOT / SHARDS, root / SHARDS)
            shutil.copy2(ROOT / 'app_v2.html', root / 'app_v2.html')
            shutil.copy2(ROOT / ASSET, root / ASSET)
            self.assertEqual(len(load(root)), 248)
            path = root / SHARDS / 'G1.json'
            data = json.loads(path.read_text()); data['c'][0] += ' corruption'
            path.write_text(json.dumps(data, ensure_ascii=False))
            with self.assertRaisesRegex(ValueError, 'divergence'):
                load(root)
            path.unlink()
            with self.assertRaisesRegex(ValueError, 'manquants'):
                load(root)

    def test_chargement_invalide_et_structure_bloquent(self):
        from tip_data import check_loading
        app = TAG + '\n<script>\nconst SSP=[["G1"]];\n</script>'
        check_loading(app)
        for altered in (app.replace(TAG, '<!--'+TAG+'-->'),
                        app.replace(TAG, '') + TAG,
                        app.replace('<script src=', '<script defer src='),
                        app + '<script>var TIP = {};</script>'):
            with self.assertRaises(ValueError):
                check_loading(altered)
        with self.assertRaises(ValueError):
            from_js('const unrelated = {};')

    def test_injection_fusionne_ssp_distincts_et_refuse_structure_avant_ecriture(self):
        import json_inject
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/SHARDS).mkdir(parents=True);(root/'assets/config').mkdir(parents=True)
            tip={code: {'c':['Original']*14, 'd':['DD intact']} for code in ('G1','G2')}
            app=TAG+'\n<script>\nconst SSP=[["G1"],["G2"]];\n</script>'
            (root/'app_v2.html').write_text(app)
            def save():
                for code,item in tip.items():
                    (root/SHARDS/(code+'.json')).write_text(json.dumps(item))
                (root/ASSET).write_text(render(tip))
            save()
            with patch.object(json_inject,'ROOT',str(root)), patch.object(json_inject,'read',return_value=app):
                json_inject.main('extract','TIP')
                draft=root/'data/TIP.json';proposal=json.loads(draft.read_text())
                proposal['G1']['c'][0]='Proposé';draft.write_text(json.dumps(proposal))
                tip['G2']['c'][0]='Concurrent';save()
                json_inject.main('inject','TIP')
                merged=load(root)
                self.assertEqual(merged['G1']['c'][0],'Proposé')
                self.assertEqual(merged['G2']['c'][0],'Concurrent')
                self.assertEqual(merged['G1']['d'],['DD intact'])
                json_inject.main('extract','TIP')
                proposal=json.loads(draft.read_text());proposal['G1']['c']='x'*14
                draft.write_text(json.dumps(proposal))
                before={path:path.read_bytes() for path in [root/ASSET,*sorted((root/SHARDS).glob('*.json'))]}
                with self.assertRaisesRegex(ValueError,'14 parties'):
                    json_inject.main('inject','TIP')
                self.assertTrue(all(path.read_bytes()==value for path,value in before.items()))

    def test_flux_inline_historique(self):
        app = '\nconst TIP={"G1":{"c":["historique"]}};\n'
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(load(tmp, app)['G1']['c'], ['historique'])

    def test_injection_refuse_un_conflit_par_ssp(self):
        import json_inject
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root / SHARDS).mkdir(parents=True)
            (root / 'assets/config').mkdir(parents=True)
            tip = {'G1': {'c': ['Original'] * 14}}
            app = TAG + '\n<script>\nconst SSP=[["G1","Cours",null]];\n</script>\n'
            (root / 'app_v2.html').write_text(app)
            (root / SHARDS / 'G1.json').write_text(json.dumps(tip['G1']))
            (root / ASSET).write_text(render(tip))
            def local_read(path=None):
                return Path(path or root / 'app_v2.html').read_text()
            with patch.object(json_inject, 'ROOT', str(root)), patch.object(json_inject, 'read', local_read):
                json_inject.main('extract', 'TIP')
                draft = root / 'data/TIP.json'
                proposal = json.loads(draft.read_text());proposal['G1']['c'][0] = 'Proposé'
                draft.write_text(json.dumps(proposal))
                tip['G1']['c'][0] = 'Concurrent'
                (root / SHARDS / 'G1.json').write_text(json.dumps(tip['G1']))
                (root / ASSET).write_text(render(tip))
                with self.assertRaisesRegex(ValueError, 'conflit'):
                    json_inject.main('inject', 'TIP')
                self.assertEqual(load(root)['G1']['c'][0], 'Concurrent')

    def test_lot_cours_ecrit_le_json_canonique_sans_toucher_aux_dd(self):
        from cours.appliquer import appliquer
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root / SHARDS).mkdir(parents=True)
            (root / 'assets/config').mkdir(parents=True)
            (root / 'tools/cours/lots').mkdir(parents=True)
            item = {'c': ['Avant'] * 14, 'd': ['DD conservé'], 'f': ['Fondamental conservé']}
            (root / 'app_v2.html').write_text(TAG + '\n<script>\nconst SSP=[["G1","Cours",null]];\n</script>\n')
            (root / SHARDS / 'G1.json').write_text(json.dumps(item))
            (root / ASSET).write_text(render({'G1': item}))
            import hashlib
            lot = {'version': 1, 'ssp': 'G1', 'parties': ['Après'] * 14,
                   'avant_sha256': [hashlib.sha256(b'Avant').hexdigest()] * 14,
                   'references_par_partie': [[1]] * 14,
                   'sources_ajoutees': [{'id': 1, 't': 'Source lue'}]}
            (root / 'tools/cours/lots/G1.json').write_text(json.dumps(lot))
            legacy = root / 'legacy'
            (legacy / 'tools/cours/lots').mkdir(parents=True)
            (legacy / 'tools/cours/lots/G1.json').write_text(json.dumps(lot))
            (legacy / 'app_v2.html').write_text('\nconst TIP=' + json.dumps({'G1': item}) + ';\n')
            appliquer('G1', legacy)
            appliquer('G1', root)
            updated = load(root)['G1']
            self.assertEqual(load(root), load(legacy))
            self.assertEqual(updated['c'], ['Après'] * 14)
            self.assertEqual((updated['d'], updated['f']), (item['d'], item['f']))
            self.assertNotIn('const TIP=', (root / 'app_v2.html').read_text())


if __name__ == '__main__':
    unittest.main()
