import copy
from datetime import datetime,timezone,timedelta,date
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.coordination.calculer import calculer,empreinte,CONFIG
from tools.coordination.relance import decision
from tools.prevalences.moteur import Client,FetchError,Societes
from tools.prevalences.jauges import valid_published
from tools.jauge.binomes import mono_ok,prev_ok,MONO_REQ
import tools.porte as porte

class CoordinationTests(unittest.TestCase):
    def fixture(self,root):
        (root/'data/ck/mono').mkdir(parents=True)
        mono={k:'Une phrase complète.' for k in ['def','epi','phy','cli','exp','dia','but','mes','pha']};mono.update(n='Maladie',src='SRC',lu='18.10.2026')
        (root/'data/ck/mono/m.json').write_text(json.dumps({'maladie':mono}))
        (root/'data/ck/src.json').write_text(json.dumps([{'id':'SRC'}]))
        item={'i':0,'nom':'Maladie','prev_pct':5,'src':'SRC','date_lu':'2026-01-01','loc':'Tableau1'}
        (root/'data/ck/prev.json').write_text(json.dumps({'G1':{'items':[item]},'G2':{'items':[dict(item)]}}))
        report=root/'audit.json';report.write_text('Relecture indépendante.');rh=hashlib.sha256(report.read_bytes()).hexdigest()
        def proof(value):return {'statut':'revue_documentaire','validation_clinique':False,'date_lu':'2026-01-01','sha256':empreinte(value),'rapport':'audit.json','rapport_sha256':rh,'sources':['SRC'],'reserves_levees':True}
        tasks=[{'key':f'G{i}#0','ssp':f'G{i}','title_ssp':f'Plainte{i}','secteur':'G','categorie':'G','i':0,'diagnostic':'Maladie','fingerprint':f'fp{i}'} for i in (1,2)]
        ledger={'monographies':{'maladie':proof(mono)},'prevalences':{'G1#0':dict(proof(item),fingerprint='fp1',applicable_au_dd_dans_ce_cadre=True,population_cible='Plainte1')}}
        return tasks,ledger,mono
    def test_same_monograph_does_not_transfer_prevalence_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);tasks,ledger,_=self.fixture(root)
            with patch('tools.coordination.calculer.catalog',return_value=([('G1','Plainte1','G'),('G2','Plainte2','G')],tasks)):
                m=calculer(root,ledger=ledger)['mesure'];self.assertEqual(m['monographies_structure'],1);self.assertEqual(m['couples_documentes'],1);self.assertFalse(m['maturite_documentaire_complete'])
    def test_structured_unreviewed_monograph_still_gets_maturation_work(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);tasks,ledger,_=self.fixture(root)
            with patch('tools.coordination.calculer.catalog',return_value=([('G1','Plainte1','G')],tasks[:1])):
                result=calculer(root,ledger={});self.assertEqual(len(result['plan']['prochain_lot9']),1);self.assertFalse(result['mesure']['maturite_documentaire_complete'])
    def test_corrupt_runtime_disables_dispatch_and_does_not_crash(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);tasks,ledger,_=self.fixture(root)
            for row in [None,dict(tasks[0],candidates=[None])]:
                states={c:{'tasks':{}} for c in 'GSFO'};states['G']['tasks']['G1#0']=row
                with patch('tools.coordination.calculer.catalog',return_value=([('G1','Plainte1','G')],tasks[:1])):
                    result=calculer(root,states=states,ledger=ledger);self.assertTrue(result['plan']['anomalies_etat']);self.assertFalse(result['mesure']['maturite_documentaire_complete']);self.assertFalse(decision({'workflow_runs':[]},result['plan'])['lancer'])
    def test_changed_monograph_or_report_revokes_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);tasks,ledger,mono=self.fixture(root);mono['def']='Une définition modifiée.';(root/'data/ck/mono/m.json').write_text(json.dumps({'maladie':mono}))
            with patch('tools.coordination.calculer.catalog',return_value=([('G1','Plainte1','G')],tasks[:1])):
                self.assertEqual(calculer(root,ledger=ledger)['mesure']['couples_documentes'],0)
    def test_reserve_and_ssp_without_dd_block_completion(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);tasks,ledger,_=self.fixture(root)
            with patch('tools.coordination.calculer.catalog',return_value=([('G1','Plainte1','G'),('S8.1','Trauma','S8')],tasks[:1])):
                m=calculer(root,ledger=ledger)['mesure'];self.assertEqual(m['couples_documentes'],1);self.assertFalse(m['maturite_documentaire_complete']);self.assertEqual(m['ssp_sans_dd'],['S8.1'])
            ledger['monographies']['maladie']['reserves_levees']=False
            with patch('tools.coordination.calculer.catalog',return_value=([('G1','Plainte1','G')],tasks[:1])):
                self.assertEqual(calculer(root,ledger=ledger)['mesure']['couples_documentes'],0)
    def test_null_bool_nonfinite_future_and_locations_rejected(self):
        self.assertFalse(mono_ok({k:None for k in MONO_REQ}))
        task={'diagnostic':'Maladie'};base={'nom':'Maladie','prev_pct':5,'date_lu':'2026-01-01','loc':'Tableau1','src':'SRC'}
        for key,value in [('prev_pct',True),('prev_pct',float('nan')),('date_lu','2099-01-01'),('loc',None),('src','absente')]:
            d=dict(base,**{key:value});self.assertFalse(valid_published(d,task,{'SRC'},date.today().isoformat()))
        self.assertFalse(prev_ok(dict(base,prev_pct=True)))
        self.assertFalse(prev_ok(dict(base,date_lu='2099-01-01')))
        self.assertFalse(valid_published(dict(base,prev_pct=0),task,{'SRC'},date.today().isoformat()))
    def test_rounding_to_100_does_not_close_step(self):
        response=type('Response',(),{'stdout':json.dumps({'prevalences':{'ok':2575,'total':2587,'pct':100}})})()
        with patch('tools.porte.subprocess.run',return_value=response):self.assertFalse(porte.critere(8,bavard=False))
    def test_scheduler_respects_running_cooldown_and_unknown(self):
        now=datetime.now(timezone.utc);plan={'intervalle_recherche_minutes':240,'limite_recherche':1}
        self.assertFalse(decision(None,plan,now)['lancer'])
        self.assertFalse(decision({'workflow_runs':[{'status':'queued'}]},plan,now)['lancer'])
        self.assertFalse(decision({'workflow_runs':[{'status':'completed','created_at':now.isoformat()}]},plan,now)['lancer'])
        self.assertTrue(decision({'workflow_runs':[{'status':'completed','created_at':(now-timedelta(hours=5)).isoformat()}]},plan,now)['lancer'])
    def test_circuit_breaker_persists_and_does_not_fabricate_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            client=Client(tmp,interval=0)
            with patch('tools.prevalences.moteur.urlopen',side_effect=HTTPError('https://example.org/a',503,'unavailable',{},None)) as fetch,patch('tools.prevalences.moteur.time.sleep'):
                with self.assertRaises(FetchError):client.fetch('https://example.org/a')
                with self.assertRaises(FetchError) as error:client.fetch('https://example.org/b')
                self.assertEqual(fetch.call_count,3);self.assertEqual(error.exception.details['tentatives'],0)
                other=Client(tmp,interval=0)
                with self.assertRaises(FetchError):other.fetch('https://example.org/c')
                self.assertEqual(fetch.call_count,3)
    def test_direct_society_document_retains_provenance(self):
        registry={'sources':[{'id':'SPILF','verified':True,'domaines':['infectiologie.com'],'reference_reconnaissance':'https://infectiologie.com/doc','documents_recherche':[{'url':'https://infectiologie.com/doc','titre':'Infections','mots_cles':['epidurite']}]}]}
        class Fake:
            def fetch(self,url):return b'<p>Epidurite prevalence 5% among patients.</p>'
        with patch('tools.prevalences.moteur.load_registry',return_value=registry):
            _,docs=Societes(Fake()).search({'diagnostic':'Epidurite','title_ssp':'Douleur'})
        self.assertEqual(docs[0]['source_editoriale_id'],'SPILF');self.assertFalse(docs[0]['population_verifiee'])

if __name__=='__main__':unittest.main()
