import copy, json, tempfile, unittest
import datetime
from pathlib import Path
from audit_gate import verify, ROOT
from progression import validate
from validate import check,check_input
from check_ownership import validate as ownership
from publish_evidence import compact
from lease import allowed

class Controls(unittest.TestCase):
    def test_empty_author_folder_never_counts_as_complete(self):
        with tempfile.TemporaryDirectory() as d:
            r=check_input(Path(d),json.loads((ROOT/'config/rubric.json').read_text()))
            self.assertFalse(r['structural_pass']);self.assertFalse(r['semantic_validation'])
    def test_second_coordinator_blocked_until_lease_expires(self):
        now=datetime.datetime.now(datetime.timezone.utc)
        lease={'owner':'first','expires_at':(now+datetime.timedelta(minutes=5)).isoformat()}
        self.assertFalse(allowed(lease,'second',now))
        self.assertTrue(allowed(lease,'first',now))
        self.assertTrue(allowed(lease,'second',now+datetime.timedelta(minutes=6)))
    def test_author_cannot_touch_coordinator_or_neighbor(self):
        for path in ['phase_lot/config/file.json','LOT_Candidats/LOT_001/B2/Cours.html','LOT_Candidats/LOT_001/B1/../A/Appel_A.html']:
            with self.assertRaises(AssertionError): ownership([path],1,'B1')
    def test_public_excerpt_budget_shared_across_duplicate_source(self):
        raw={'sources':[{'url':'https://example.test','excerpts':['mot '*200]},{'url':'https://example.test','excerpts':['autre '*200]}]}
        out=compact(raw)
        self.assertEqual(out['sources'][1]['bounded_excerpt'],' […]')
        self.assertEqual(len(raw['sources'][0]['excerpts'][0].split()),200)
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
        with self.assertRaisesRegex(AssertionError,'Validation humaine'):
            verify(Path('.'),{'auditor_login':'tunder'}, {'tunder_github_login':'tunder'}, {'author':{'login':'author'}})
    def test_signed_commit_does_not_replace_human_approval(self):
        with self.assertRaisesRegex(AssertionError,'Validation humaine'):
            verify(Path('.'),{}, {'tunder_github_login':'tunder'}, {'author':{'login':'tunder'},'commit':{'verification':{'verified':True}}})
    def test_human_approval_does_not_apply_to_other_candidate(self):
        policy={'tunder_github_login':'tunder','human_approval':{'accepted':True,'reference':'human-review','candidate_commit':'first','files':{}}}
        with self.assertRaisesRegex(AssertionError,'périmée'):
            verify(Path('.'),{'candidate_commit':'second'},policy,{})
    def test_rubric_has_each_v7_question(self):
        rubric=json.loads((ROOT/'config/rubric.json').read_text())
        self.assertEqual(list(range(1,15)),[p['point'] for p in rubric['points']])
        self.assertEqual(51,sum(len(p['questions']) for p in rubric['points']))

if __name__=='__main__': unittest.main()
