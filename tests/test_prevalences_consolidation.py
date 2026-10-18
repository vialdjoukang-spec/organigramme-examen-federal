import copy
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.prevalences.consolider import combine


class ConsolidationTests(unittest.TestCase):
    def state(self,date):
        return {'version':1,'category':'G','maj':date,'tasks':{'G1#0':{'fingerprint':'same','date_recherche':date,'candidates':[{'id':'a','url':'https://example.org','extrait':'10%','sha256':'abc','provenance':'hug','requete':'CH:documents_hug'}]}}}
    def test_agent_reading_added_after_search_is_preserved(self):
        old=self.state('2026-01-01');new=self.state('2026-01-02')
        old['tasks']['G1#0']['candidates'][0]['relecture_agent']={'verdict':'À vérifier','statut':'terminee'}
        before=copy.deepcopy(old)
        result=combine(old,new)
        self.assertEqual(result['tasks']['G1#0']['candidates'][0]['relecture_agent'],old['tasks']['G1#0']['candidates'][0]['relecture_agent'])
        self.assertEqual(old,before)
    def test_different_fingerprint_never_inherits_proof(self):
        old=self.state('2026-01-01');new=self.state('2026-01-02')
        old['tasks']['G1#0']['candidates'][0]['statistique']={'pct':10}
        new['tasks']['G1#0']['fingerprint']='different'
        result=combine(old,new)
        self.assertNotIn('statistique',result['tasks']['G1#0']['candidates'][0])
    def test_missing_category_preserves_old_tasks_and_never_mutates_inputs(self):
        old=self.state('2026-01-01');new=self.state('2026-01-02');new['tasks']={}
        self.assertEqual(combine(old,new)['tasks'],old['tasks'])
    def test_stale_artifact_cannot_replace_newer_source_or_agent_reading(self):
        old=self.state('2026-01-02');new=self.state('2026-01-01')
        c=old['tasks']['G1#0']['candidates'][0]
        c.update(sha256='new-source',relecture_agent={'verdict':'À vérifier'})
        result=combine(old,new)
        candidate=result['tasks']['G1#0']['candidates'][0]
        self.assertEqual(candidate['sha256'],'new-source')
        self.assertIn('relecture_agent',candidate)
        self.assertEqual(result['tasks']['G1#0']['artefacts_obsoletes_ignores'],1)
    def test_transport_metrics_follow_latest_run_and_survive_consolidation(self):
        old=self.state('2026-01-01');new=self.state('2026-01-02')
        old['transport']={'requetes_http':20};new['transport']={'requetes_http':3,'requetes_evitees':7,'cache_lu':8}
        result=combine(old,new);self.assertEqual(result['transport'],new['transport'])
        self.assertEqual(combine(new,old)['transport'],new['transport'])
        self.assertEqual(old['transport'],{'requetes_http':20})
    def test_category_mismatch_refused(self):
        old=self.state('2026-01-01');new=self.state('2026-01-02');new['category']='S'
        with self.assertRaises(ValueError):combine(old,new)


if __name__=='__main__':unittest.main()
