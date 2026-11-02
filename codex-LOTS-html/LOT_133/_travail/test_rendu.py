import unittest
from rendre_dx import Markdown, references, clean_source_labels
class Citations(unittest.TestCase):
 def test_references_apres_point_virgule(self):
  self.assertEqual(references('[S3 ; S6, définition]'), ['S3','S6'])
  t=Markdown({'S3':3,'S6':6}).inline('[S3 ; S6, définition]')
  self.assertIn('href="#s6"',t);self.assertIn('définition',t)
 def test_qualification_sans_point_virgule(self):
  t=Markdown({'S5':5}).inline('[S5 extrait indexé sur l’oxygénothérapie]')
  self.assertIn('extrait indexé sur l’oxygénothérapie',t)
 def test_comparateurs_et_gras(self):
  t=Markdown({}).inline('**PaO₂ < 60 mmHg** et **PaCO₂ > 45 mmHg**')
  self.assertEqual(t.count('<strong>'),2)
  self.assertIn('&lt; 60',t);self.assertIn('&gt; 45',t)
  self.assertNotIn('**',t)
 def test_identifiants_sources(self):
  t='<p><abbr title="allemand">S3</abbr></p><sup class="s"><a href="#s3"><abbr title="allemand">S3</abbr></a></sup>'
  r=clean_source_labels(t)
  self.assertIn('<p><abbr title="allemand">S3</abbr></p>',r)
  self.assertIn('<a href="#s3">S3</a>',r)
if __name__=='__main__':unittest.main()
