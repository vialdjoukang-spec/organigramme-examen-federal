"""Garde-fous licences et provenance ; aucune validation clinique automatique."""
import copy,importlib.util,json,sys,unittest
from pathlib import Path
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('illustrer',Path(__file__).with_name('illustrer.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Licences(unittest.TestCase):
 def setUp(self):self.s=json.loads((m.BASE/'LOT_018/illustrations/optique.json').read_text())
 def test_licences_interdites(self):
  for lic in ['CC BY-NC 4.0','CC BY-ND 4.0','CC BY-NC-ND 4.0','inconnue','CC BY 4.0 ou NC']:
   with self.subTest(lic=lic),self.assertRaises(ValueError):m.validate(dict(self.s,licence=lic))
 def test_licences_permises(self):
  for lic,url in [('CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),('Domaine public','https://creativecommons.org/publicdomain/mark/1.0/'),('CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),('CC BY 2.5','https://creativecommons.org/licenses/by/2.5/')]:m.validate(dict(self.s,licence=lic,licence_url=url))
 def test_attribution_incomplete(self):
  for key in ['auteur','acces_le','source_url','legende','pieges']:
   with self.subTest(key=key),self.assertRaises(ValueError):m.validate(dict(self.s,**{key:''}))
 def test_url_licence_incoherente(self):
  with self.assertRaises(ValueError):m.validate(dict(self.s,licence_url='https://creativecommons.org/licenses/by-nc/4.0/'))
 def test_domaine_non_autorise(self):
  with self.assertRaises(ValueError):m.validate(dict(self.s,source_url='https://example.com/image.jpg'))
 def test_empreinte_modifiee(self):
  with self.assertRaises(ValueError):m.render(dict(self.s,sha256_original='0'*64))
 def test_contour_hors_image(self):
  s=copy.deepcopy(self.s);s['annotations'][0]['contour'][0]=[-1,0]
  with self.assertRaises(ValueError):m.render(s)
 def test_sortie_hors_codex(self):
  with self.assertRaises(ValueError):m.ensure_output(m.BASE.parent/'autre.svg')
if __name__=='__main__':unittest.main()
