import importlib.util, unittest
from pathlib import Path
s = importlib.util.spec_from_file_location('v', Path(__file__).resolve().parents[1] / 'tools/arsenal/ci_verdict.py')
v = importlib.util.module_from_spec(s); s.loader.exec_module(v)
class Verdict(unittest.TestCase):
    def test_rouge_si_un_echec(self):
        self.assertEqual(v.verdict('[{"name":"garde","bucket":"fail"},{"name":"t","bucket":"pass"}]')[1], 1)
    def test_rouge_echec_meme_si_attente(self):
        self.assertEqual(v.verdict('[{"name":"garde","bucket":"fail"},{"name":"t","bucket":"pending"}]')[1], 1)
    def test_jamais_vert_sans_controle_ou_sortie_vide(self):
        self.assertNotEqual(v.verdict('')[1], 0); self.assertNotEqual(v.verdict('[]')[1], 0)
        self.assertEqual(v.verdict('oops')[1], 1)
    def test_attente_puis_vert(self):
        self.assertEqual(v.verdict('[{"name":"t","bucket":"pending"}]')[1], 2)
        self.assertEqual(v.verdict('[{"name":"t","bucket":"pass"},{"name":"s","bucket":"skipping"}]')[1], 0)
if __name__ == '__main__': unittest.main()
