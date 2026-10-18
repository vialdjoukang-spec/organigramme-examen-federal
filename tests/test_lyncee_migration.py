"""Contrôle réel CLI : une nouvelle règle ne doit pas permettre de grossir la référence."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import lyncee

class Migration(unittest.TestCase):
 def run_case(self, old_terms, same_rules=False):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);(root/'data/ck').mkdir(parents=True);(root/'qa').mkdir()
   for name in ['glo','sig','syn','hyp','nc','loc','src','doses_ch']:
    (root/'data/ck'/f'{name}.json').write_text('[]')
   (root/'app_v2.html').write_text('<html><body><script>\nconst TIP={"X":{"c":["hyperglycémie dysplasie"]}};\nconst NOT={};\nconst GES=[];\n</script></body></html>')
   ref=root/'qa/termes-baseline.json'
   ref.write_text(json.dumps({'regles':lyncee.REGLES if same_rules else 'ancienne-regle','termes':old_terms,'total':len(old_terms)}))
   for args in [['init','-q'],['config','user.name','Test'],['config','user.email','test@example.invalid'],['add','.'],['commit','-qm','ancienne référence'],['branch','-M','main']]:
    subprocess.run(['git',*args],cwd=root,check=True,capture_output=True)
   ref.unlink()
   cmd=[sys.executable,str(ROOT/'tools/lyncee.py'),'--racine',tmp]
   subprocess.run(cmd+['--init'],check=True,capture_output=True)
   return subprocess.run(cmd+['--diff','main'],capture_output=True,text=True)
 def test_growth_with_new_rules_is_blocked(self):
  result=self.run_case(['hyperglycemie'])
  self.assertNotEqual(result.returncode,0,result.stdout)
  self.assertIn('même lors d’une migration',result.stdout)
 def test_new_rules_with_smaller_total(self):
  result=self.run_case(['hyperglycemie','dysplasie','ancien-terme'])
  self.assertEqual(result.returncode,0,result.stdout)
 def test_changed_rules_equal_total_remains_reviewable(self):
  result=self.run_case(['hyperglycemie','ancien-terme'])
  self.assertEqual(result.returncode,0,result.stdout)
  self.assertIn('AVERTISSEMENT règles modifiées',result.stdout)
 def test_same_rules_still_forbid_new_members(self):
  result=self.run_case(['hyperglycemie','ancien-terme'],same_rules=True)
  self.assertNotEqual(result.returncode,0,result.stdout)

if __name__=='__main__':unittest.main()
