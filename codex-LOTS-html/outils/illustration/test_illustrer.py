"""Garde-fous licences et provenance ; aucune validation clinique automatique."""
import copy,importlib.util,json,re,sys,unittest
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
 def test_editeur_original_cc_by(self):
  m.validate(dict(self.s,source_url='https://medicaljournalssweden.se/actaoncologica/article/view/123',licence='CC BY 4.0',licence_url='https://creativecommons.org/licenses/by/4.0/'))
 def test_depot_original_cc_by(self):
  m.validate(dict(self.s,source_url='https://github.com/ml-workgroup/covid-19-image-repository/blob/ad7ab099/README.md',licence='CC BY 3.0',licence_url='https://creativecommons.org/licenses/by/3.0/'))
 def test_depot_original_licence_refusee(self):
  for lic in ['CC BY-NC 3.0','CC BY-ND 3.0','inconnue']:
   with self.subTest(lic=lic),self.assertRaisesRegex(ValueError,'Licence refusée'):
    m.validate(dict(self.s,source_url='https://github.com/ml-workgroup/covid-19-image-repository',licence=lic))
 def test_editeur_original_licence_refusee(self):
  for lic in ['CC BY-NC 4.0','CC BY-ND 4.0','inconnue']:
   with self.subTest(lic=lic),self.assertRaisesRegex(ValueError,'Licence refusée'):
    m.validate(dict(self.s,source_url='https://medicaljournalssweden.se/actaoncologica/article/view/123',licence=lic))
 def test_editeur_original_url_licence_incoherente(self):
  with self.assertRaisesRegex(ValueError,'URL de licence incohérente'):
   m.validate(dict(self.s,source_url='https://medicaljournalssweden.se/actaoncologica/article/view/123',licence='CC BY 4.0',licence_url='https://creativecommons.org/licenses/by-nc/4.0/'))
 def test_editeur_domaine_exact_et_https(self):
  for url in ['http://medicaljournalssweden.se/article/123','https://medicaljournalssweden.se.example.com/article/123','https://example.com/medicaljournalssweden.se','https://medicaljournalssweden.se@example.com/article/123','http://github.com/ml-workgroup/repo','https://github.com.example.com/repo','https://raw.githubusercontent.com/ml-workgroup/repo/main/image.jpg']:
   with self.subTest(url=url),self.assertRaises(ValueError):m.validate(dict(self.s,source_url=url))
 def test_empreinte_modifiee(self):
  with self.assertRaises(ValueError):m.render(dict(self.s,sha256_original='0'*64))
 def test_contour_hors_image(self):
  s=copy.deepcopy(self.s);s['annotations'][0]['contour'][0]=[-1,0]
  with self.assertRaises(ValueError):m.render(s)
 def test_sortie_hors_codex(self):
  with self.assertRaises(ValueError):m.ensure_output(m.BASE.parent/'autre.svg')
class RenduFin(unittest.TestCase):
 def setUp(self):
  Licences.setUp(self)
  self.s['crop']=[0,0,640,640]
  self.s['comparaison']=True
  self.s['trace_fin']=True
  self.s['annotations'][0]['repere']=[10,10]
  self.s['annotations'][0]['cible']=[38,38]
 def test_traits_et_rappel(self):
  out=m.render(self.s)
  self.assertIn('stroke-width="1.8"',out)
  self.assertIn('stroke-width="0.8" stroke-dasharray="2.5 2"',out)
  self.assertIn('<line x1="10" y1="10" x2="38" y2="38"',out)
  self.assertIn('width:20px;height:20px',out)
  self.assertIn('width:30px;height:30px',out)
  self.assertIn('<span class="numero">1</span>',out)
  self.assertNotIn('stroke-width="5"',out)
 def test_cible_limites_et_types(self):
  for point in [[-1,0],[0,641],[float('nan'),0],[float('inf'),0],['0',0],[True,0],[0],None]:
   with self.subTest(point=point),self.assertRaisesRegex(ValueError,'Cible hors image'):
    s=copy.deepcopy(self.s);s['annotations'][0]['cible']=point;m.render(s)
  for point in [[0,0],[640,640]]:
   s=copy.deepcopy(self.s);s['annotations'][0]['cible']=point;m.render(s)
 def test_repere_et_contour_limites(self):
  for field in ['repere','contour']:
   for point in [[641,0],[0,-1],['1" onload="alert(1)',0],[float('nan'),0]]:
    with self.subTest(field=field,point=point),self.assertRaises(ValueError):
     s=copy.deepcopy(self.s)
     if field=='contour':s['annotations'][0][field][0]=point
     else:s['annotations'][0][field]=point
     m.render(s)
 def test_textes_echappes_et_ordre(self):
  for comparison in [True,False]:
   s=dict(self.s,comparaison=comparison,cliche='<img src=x onerror="x">',interpretation=[{'titre':'<script>"étape"</script>','texte':'A & B <b>texte</b>'},{'titre':'Ensuite','texte':'Deuxième étape'}])
   out=m.render(s)
   self.assertIn('<ol class="interpretation"><li><strong>&lt;script&gt;&quot;étape&quot;&lt;/script&gt;</strong> : A &amp; B &lt;b&gt;texte&lt;/b&gt;</li><li><strong>Ensuite</strong> : Deuxième étape</li></ol>',out)
   self.assertIn('<p class="cliche">&lt;img src=x onerror=&quot;x&quot;&gt;</p>',out)
   self.assertNotIn('<script>',out)
 def test_metadonnees_optionnelles_invalides(self):
  for value in [None,[],{},['texte'],[{'titre':'Titre'}],[{'titre':' ','texte':'Texte'}],[{'titre':'Titre','texte':7}]]:
   with self.subTest(value=value),self.assertRaises(ValueError):m.validate(dict(self.s,interpretation=value))
  for fields in [{'cliche':{}},{'trace_fin':'true'}]:
   with self.assertRaises(ValueError):m.validate(dict(self.s,**fields))
 def test_pixels_et_source_inchanges(self):
  source=m.BASE/self.s['image'];before=source.read_bytes()
  fine=m.render(self.s);old=m.render(dict(self.s,trace_fin=False))
  raster=lambda html:re.findall(r'data:image/webp;base64,([A-Za-z0-9+/=]+)',html)
  self.assertEqual(len(raster(fine)),2)
  self.assertEqual(raster(fine),raster(old))
  self.assertEqual(raster(fine)[0],raster(fine)[1])
  self.assertEqual(source.read_bytes(),before)
  self.assertIn('stroke-width="5"',old)
  self.assertIn('stroke-dasharray="6 4"',old)
  self.assertNotIn('<line ',old)
  self.assertNotIn('class="numero"',old)
  self.assertIn('<ol><li><strong>',old)
if __name__=='__main__':unittest.main()
