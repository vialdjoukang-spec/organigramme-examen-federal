"""Les recherches ne gonflent jamais la couverture clinique et restent traçables."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.prevalences.moteur import catalog, CONFIG, queries, due, search_task, Client, Hug
from tools.prevalences.jauges import measure, valid_published, page


class ProgressTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ssps,cls.tasks=catalog();cls.task=cls.tasks[0]
    def state(self, query_list=None):
        t=self.task
        qs=[{'provider':p,'id':i,'ok':True} for p in CONFIG['providers'] for i in (['CH:documents_hug'] if p=='hug' else ['CH:consultation','CH:population','Europe:consultation','Europe:population'])]
        row=dict(t,queries=qs if query_list is None else query_list,statut='recherchee',candidates=[],date_recherche='2026-01-01T00:00:00+00:00')
        return {'G':{'tasks':{t['key']:row}}}
    def test_real_categories_partition_catalogue_and_counts(self):
        r=measure();self.assertEqual(sum(v['total'] for v in r['secteurs'].values()),r['total']['total'])
        self.assertEqual(sum(v['ssp'] for v in r['categories'].values()),len(self.ssps))
        self.assertEqual(set(r['categories']),{'G','S','F','O'})
        self.assertEqual(r['total']['total'],len(self.tasks))
    def test_candidate_is_never_published_coverage(self):
        base=measure();state=self.state();state['G']['tasks'][self.task['key']]['candidates']=[{'audit':{'corrections':[]},'extrait':'50%'}]
        r=measure(states=state)
        self.assertEqual(r['total']['chiffres_sources'],base['total']['chiffres_sources'])
        self.assertEqual(r['categories']['G']['avec_candidats'],1)
        self.assertEqual(r['categories']['G']['audits_statistiques'],1)
    def test_partial_protocol_cannot_count_as_successful_search(self):
        for qs in ([],[{'provider':'hug','id':'CH:documents_hug','ok':True}]):
            r=measure(states=self.state(qs));self.assertEqual(r['total']['recherches_abouties'],0)
            self.assertEqual(r['total']['tentes'],r['total']['recherches_abouties']+r['total']['partiels']+r['total']['erreurs'])
    def test_complete_protocol_required_and_duplicate_queries_rejected(self):
        s=self.state();self.assertEqual(measure(states=s)['total']['recherches_abouties'],1)
        row=s['G']['tasks'][self.task['key']];row['queries'].append(row['queries'][0].copy())
        self.assertEqual(measure(states=s)['total']['recherches_abouties'],0)
    def test_error_and_stale_label_do_not_mark_complete(self):
        s=self.state();r=s['G']['tasks'][self.task['key']];r['queries'][0]['ok']=False
        self.assertEqual(measure(states=s)['total']['recherches_abouties'],0)
        r['fingerprint']='changed';r['candidates']=[{}]
        result=measure(states=s);self.assertEqual(result['total']['tentes'],0);self.assertEqual(result['total']['candidats'],0)
        self.assertEqual(result['total']['etats_obsoletes'],1)
    def test_published_invalid_numbers_and_sources_are_rejected(self):
        t=self.task;base={'nom':t['diagnostic'],'prev_pct':12,'src':'source','date_lu':'2026-01-01','loc':'Table1'}
        self.assertTrue(valid_published(base,t,{'source'},'2026-10-18'))
        for key,value in [('prev_pct',True),('prev_pct',0),('prev_pct',101),('prev_pct',float('nan')),('src','missing'),('date_lu','2027-01-01'),('date_lu','bad'),('nom','Other')]:
            with self.subTest(key=key,value=value):
                item=dict(base);item[key]=value
                self.assertFalse(valid_published(item,t,{'source'},'2026-10-18'))
    def test_ch_europe_and_consultation_population_queries(self):
        qs=queries(self.task);self.assertEqual({q['id'] for q in qs},{'CH:consultation','CH:population','Europe:consultation','Europe:population'})
    def test_failed_provider_is_not_zero_results(self):
        class FailClient:
            deadline=float('inf')
            def get_json(self,url):raise ValueError('API forbidden')
        row=search_task(self.task,FailClient(),None,['europepmc'])
        self.assertEqual(row['statut'],'erreur');self.assertEqual(len(row['queries']),4)
        self.assertTrue(all(not q['ok'] and q['erreur'] for q in row['queries']))
    def test_retry_respects_fingerprint_and_ttl(self):
        old=dict(self.task,statut='recherchee',date_recherche='2026-01-01T00:00:00+00:00')
        self.assertTrue(due(self.task,old,30,12));old['fingerprint']='old';self.assertTrue(due(self.task,old,30,12))
    def test_dashboard_and_wrapper_plan_work_without_network(self):
        report=measure();rendered=page(report)
        self.assertIn('prevalences.json',rendered);self.assertIn('validation clinique',rendered)
        for category in 'gsfo':
            r=subprocess.run([sys.executable,str(ROOT/f'tools/prevalences/{category}.py'),'--plan','--limit','1'],capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stderr)
            data=json.loads(r.stdout);self.assertEqual(data['category'],category.upper());self.assertEqual(len(data['tasks']),1)


if __name__=='__main__':unittest.main()
