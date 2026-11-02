import unittest
from rendre_dx import Markdown, references
class Citations(unittest.TestCase):
 def test_references_apres_point_virgule(self):
  self.assertEqual(references('[S3 ; S6, définition]'), ['S3','S6'])
  t=Markdown({'S3':3,'S6':6}).inline('[S3 ; S6, définition]')
  self.assertIn('href="#s6"',t);self.assertIn('définition',t)
 def test_qualification_sans_point_virgule(self):
  t=Markdown({'S5':5}).inline('[S5 extrait indexé sur l’oxygénothérapie]')
  self.assertIn('extrait indexé sur l’oxygénothérapie',t)
if __name__=='__main__':unittest.main()
