"""Le JS externalisé garde ses corps et son chargement synchrone."""
import importlib.util
from pathlib import Path
import tempfile
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('check_fonctions_asset', ROOT / 'tools/check_fonctions_asset.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class FonctionsAsset(unittest.TestCase):
    def test_source_et_ordre_du_chargement(self):
        count, gain = module.check()
        self.assertEqual(count, 165)
        self.assertGreaterEqual(gain, 65_000)

    def test_corruption_detectee(self):
        with tempfile.TemporaryDirectory() as tmp:
            app = Path(tmp) / 'app_v2.html'
            asset = Path(tmp) / 'fonctions.js'
            app.write_bytes((ROOT / 'app_v2.html').read_bytes())
            raw = (ROOT / module.patch.ASSET_REL).read_text()
            asset.write_text(raw.replace('function monday(', 'function mondayX(', 1))
            with self.assertRaisesRegex(ValueError, 'monday'):
                module.check(app, asset)
            asset.write_text(raw)
            app.write_text(app.read_text().replace(module.patch.marker('monday'), '', 1))
            with self.assertRaisesRegex(ValueError, 'monday'):
                module.check(app, asset)

    def test_asynchronous_load_and_extra_code_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            app=Path(tmp)/'app.html';asset=Path(tmp)/'fonctions.js'
            original=(ROOT/'app_v2.html').read_text();raw=(ROOT/module.patch.ASSET_REL).read_text()
            asset.write_text(raw);app.write_text(original.replace(module.patch.SCRIPT_INSERT,module.patch.SCRIPT_INSERT.replace('<script ','<script defer ')))
            with self.assertRaisesRegex(ValueError,'asynchrone'):
                module.check(app,asset)
            app.write_text(original);asset.write_text(raw+'window.sideEffect=true;')
            with self.assertRaisesRegex(ValueError,'supplémentaire'):
                module.check(app,asset)

    def test_cross_script_lexical_collision_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            app=Path(tmp)/'app.html';asset=Path(tmp)/'fonctions.js'
            original=(ROOT/'app_v2.html').read_text();start=original.index(module.patch.SCRIPT_ANCHOR);end=original.index('</script>',start)
            app.write_text(original[:end]+'\nconst monday = 1;\n'+original[end:])
            asset.write_bytes((ROOT/module.patch.ASSET_REL).read_bytes())
            with self.assertRaises(subprocess.CalledProcessError):
                module.check(app,asset)


if __name__ == '__main__':
    unittest.main()
