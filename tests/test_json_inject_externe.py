"""Le routage externe conserve les commandes JSON et le fichier principal."""
import contextlib,importlib.util,io,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
SPEC=importlib.util.spec_from_file_location('json_inject',Path(__file__).resolve().parents[1]/'tools/json_inject.py')
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
MOD=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(MOD)

class ExternalJsonTest(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name);(self.root/'data').mkdir();(self.root/'assets/config').mkdir(parents=True);self.app=self.root/'app_v2.html';self.asset=self.root/'assets/config/interface.js'
  self.app.write_text('<script src="assets/config/interface.js"></script>\n<script>\nconst TIP={"intact":true};\n</script>')
  self.asset.write_text('\nconst SESSION={"annee":2027};\nconst EXI={"items":[1,2]};\nconst ATT=[ ["barème",1] ];\n')
 def call(self,cmd,name):
  def rd(path=None):return Path(path or self.app).read_text()
  def wr(value,path=None):Path(path or self.app).write_text(value)
  with patch.object(MOD,'ROOT',str(self.root)),patch.object(MOD,'read',rd),patch.object(MOD,'write',wr),contextlib.redirect_stdout(io.StringIO()):return MOD.main(cmd,name)
 def test_extract_external(self):
  self.call('extract','EXI');self.assertEqual(json.loads((self.root/'data/EXI.json').read_text()),{'items':[1,2]})
 def test_inject_changes_only_selected_external_value(self):
  before=self.app.read_bytes();(self.root/'data/EXI.json').write_text('{"items":[3]}');self.call('inject','EXI');self.assertEqual(self.app.read_bytes(),before);self.assertEqual(self.asset.read_text(),'\nconst SESSION={"annee":2027};\nconst EXI={"items":[3]};\nconst ATT=[ ["barème",1] ];\n')
 def test_check_external_compact_value(self):
  with self.assertRaises(SystemExit) as c:self.call('check','SESSION')
  self.assertEqual(c.exception.code,0)
 def test_inline_constant_stays_inline(self):
  (self.root/'data/TIP.json').write_text('{"intact":false}');before=self.asset.read_bytes();self.call('inject','TIP');self.assertIn('const TIP={"intact":false};',self.app.read_text());self.assertEqual(self.asset.read_bytes(),before)
 def test_missing_external_asset_fails(self):
  self.asset.unlink()
  with self.assertRaises(FileNotFoundError):self.call('extract','EXI')
 def test_preexisting_noncompact_value_remains_reported(self):
  with self.assertRaises(SystemExit) as c:self.call('check','ATT')
  self.assertEqual(c.exception.code,1)

if __name__=='__main__':unittest.main()
