import copy, json, tempfile, unittest
from pathlib import Path
from audit_gate import verify, ROOT
from progression import validate
from validate import check

class Controls(unittest.TestCase):
    def test_queue_refuses_two_active_lots(self):
        q=json.loads((ROOT/'config/file.json').read_text()); q['lots'][1]['production_status']='ACTIF'
        with self.assertRaises(AssertionError): validate(q)
    def test_queue_refuses_skipping_predecessor(self):
        q=json.loads((ROOT/'config/file.json').read_text()); q['lots'][0]['production_status']='EN_ATTENTE'; q['lots'][1]['production_status']='ACTIF'
        with self.assertRaises(AssertionError): validate(q)
    def test_empty_file_cannot_pass_structure(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'empty.html'; p.write_text('<!doctype html><html></html>')
            r=check(p,json.loads((ROOT/'config/rubric.json').read_text()))
            self.assertFalse(r['structural_pass']); self.assertFalse(r['semantic_validation'])
    def test_unconfigured_auditor_blocks_publication(self):
        with self.assertRaisesRegex(AssertionError,'non configuré'):
            verify(Path('.'),{}, {'tunder_github_login':None},{})
    def test_self_declared_identity_does_not_prove_auditor(self):
        with self.assertRaisesRegex(AssertionError,'non relié'):
            verify(Path('.'),{'auditor_login':'tunder'}, {'tunder_github_login':'tunder'}, {'author':{'login':'author'}})
    def test_unsigned_commit_blocks_publication(self):
        with self.assertRaisesRegex(AssertionError,'Signature'):
            verify(Path('.'),{}, {'tunder_github_login':'tunder'}, {'author':{'login':'tunder'},'commit':{'verification':{'verified':False}}})
    def test_rubric_has_each_v7_question(self):
        rubric=json.loads((ROOT/'config/rubric.json').read_text())
        self.assertEqual(list(range(1,15)),[p['point'] for p in rubric['points']])
        self.assertEqual(51,sum(len(p['questions']) for p in rubric['points']))

if __name__=='__main__': unittest.main()
