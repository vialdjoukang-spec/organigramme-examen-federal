import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.garde import codex_cloud_120 as relay


CFG = {'requester_login':'vialdjoukang-spec','pilot_pr':94,'request_cooldown_seconds':1800}


def report():
    return {'plan':{'mission_exclusive':relay.guard.MISSION,'priorite_cours_ssp':True,
                    'diagnostics_differentiels_suspendus':True,'prochain_lot9':[{'ssp':'G2'}],
                    'anomalies_cours':[]},
            'mesure':{'cours_ssp_relus':1,'cours_parties_relues':14}}


def state():
    return {'mesure':report()['mesure'].copy(),'dernier_progres':0,
            'worker':{'owner':'worker','expires':1300},'preuve_a_conserver':{'pr':127}}


def comment(identifier, body, login='vialdjoukang-spec', second=0, kind='User'):
    return {'id':identifier,'body':body,'user':{'login':login,'type':kind},
            'created_at':f'1970-01-01T00:16:{40+second:02d}Z','html_url':f'https://example.org/{identifier}'}


class Cloud120Tests(unittest.TestCase):
    def test_missing_environment_is_not_execution_and_ignores_impostor(self):
        cloud = {}
        rows = [comment(1,'@codex continue'),
                comment(2,'To use Codex here, create an environment for this repo',relay.BOT,2,'Bot')]
        relay.feedback(rows,cloud,CFG)
        self.assertEqual(cloud['statut'],'environnement_cloud_manquant')
        self.assertFalse(cloud['execution_ia_prouvee'])
        self.assertEqual(cloud['settings_url'],relay.SETTINGS)
        forged = copy.deepcopy(rows);forged[-1]['user']['type']='User'
        other = {};relay.feedback(forged,other,CFG)
        self.assertNotIn('reply_id',other)

    def test_old_reply_does_not_acknowledge_new_request_or_a_review(self):
        rows = [comment(1,'@codex continue'),comment(2,'create an environment for this repo',relay.BOT,2,'Bot'),
                comment(3,'@codex continue',second=3),comment(4,'@codex review',second=4)]
        cloud={};relay.feedback(rows,cloud,CFG)
        self.assertEqual(cloud['request_id'],3)
        self.assertNotIn('reply_id',cloud)

    def test_cooldown_persists_but_eventually_allows_environment_probe(self):
        value=state();value['codex_cloud']={'requested_at':1000,'statut':'environnement_cloud_manquant'}
        self.assertEqual(relay.decision(value,report(),1120,False,CFG),'environnement_cloud_manquant')
        self.assertEqual(relay.decision(value,report(),2800,False,CFG),'demander_reprise')

    def test_agent_ci_progress_unknown_scope_and_no_lot_prevent_launch(self):
        for busy,agent in [(True,None),(False,{'owner':'real','expires':2000})]:
            value=state()
            if agent:value['agent']=agent
            self.assertEqual(relay.decision(value,report(),1000,busy,CFG),'occupe_ou_progression')
        value=state();r=report();r['mesure']['cours_parties_relues']=28
        self.assertEqual(relay.decision(value,r,1000,False,CFG),'occupe_ou_progression')
        r=report();r['plan']['priorite_cours_ssp']=False
        self.assertEqual(relay.decision(state(),r,1000,False,CFG),'mission_modifiee_sans_relance')
        r=report();r['plan']['anomalies_cours']=['empreinte périmée']
        self.assertEqual(relay.decision(state(),r,1000,False,CFG),'preuves_cours_invalides_sans_relance')
        r=report();r['plan']['prochain_lot9']=[]
        self.assertEqual(relay.decision(state(),r,1000,False,CFG),'jalon_cours_sans_lot_dd_toujours_suspendus')

    def test_slots_real_deadlines_stop_and_overruns_do_not_burst(self):
        now=[0];seen=[]
        def sleep(seconds):self.assertLessEqual(seconds,25);now[0]+=seconds
        for index in relay.slots(360,clock=lambda:now[0],sleeper=sleep):
            seen.append((index,now[0]))
        self.assertEqual(seen,[(0,0),(1,120),(2,240),(3,360)])
        now[0]=0;seen=[]
        for index in relay.slots(360,clock=lambda:now[0],sleeper=sleep):
            seen.append(index)
            if index==0:now[0]=300
        self.assertEqual(seen,[0,2,3])
        self.assertEqual(list(relay.slots(360,stop=lambda:True)),[])

    def test_reservation_success_preserves_state_and_never_asserts_agent_started(self):
        with tempfile.TemporaryDirectory() as tmp:
            store=relay.SharedStore(tmp);store.read();store.write(state())
            with patch.object(relay,'api',side_effect=[{'login':CFG['requester_login'],'type':'User'},comment(10,'sent')]) as api:
                action=relay.tick(store,'worker',report(),[],CFG,1000,False,wall=lambda:1000)
            self.assertEqual(action,'demander_reprise');self.assertEqual(api.call_count,2)
            final=store.read();self.assertEqual(final['preuve_a_conserver'],{'pr':127})
            self.assertNotIn('agent',final)
            self.assertFalse(final['codex_cloud']['execution_ia_prouvee'])
            self.assertEqual(final['codex_cloud']['request_id'],10)
            with patch.object(relay,'api') as api:
                relay.tick(store,'worker',report(),[],CFG,1120,False,wall=lambda:1120)
                api.assert_not_called()

    def test_post_timeout_reservation_prevents_blind_duplicate(self):
        with tempfile.TemporaryDirectory() as tmp:
            store=relay.SharedStore(tmp);store.read();store.write(state())
            with patch.object(relay,'api',side_effect=[{'login':CFG['requester_login'],'type':'User'},RuntimeError('timeout')]):
                with self.assertRaises(RuntimeError):relay.tick(store,'worker',report(),[],CFG,1000,False,wall=lambda:1000)
            with patch.object(relay,'api') as api:
                relay.tick(store,'worker',report(),[],CFG,1120,False,wall=lambda:1120)
                api.assert_not_called()

    def test_arriving_agent_prevents_post_and_retains_acknowledgement(self):
        with tempfile.TemporaryDirectory() as tmp:
            store=relay.SharedStore(tmp);store.read();store.write(state())
            def identity(*args,**kwargs):
                current=store.read();current['agent']={'owner':'real','expires':1400};store.write(current)
                return {'login':CFG['requester_login'],'type':'User'}
            with patch.object(relay,'api',side_effect=identity) as api:
                self.assertEqual(relay.tick(store,'worker',report(),[],CFG,1000,False,wall=lambda:1000),'reprise_deja_prise_en_charge')
                self.assertEqual(api.call_count,1)
            self.assertEqual(store.read()['agent']['owner'],'real')

    def test_stop_or_window_expiry_after_identity_prevents_post(self):
        with tempfile.TemporaryDirectory() as tmp:
            store=relay.SharedStore(tmp);store.read();store.write(state())
            allowed=[True]
            def identity(*args,**kwargs):
                allowed[0]=False
                return {'login':CFG['requester_login'],'type':'User'}
            with patch.object(relay,'api',side_effect=identity) as api:
                self.assertEqual(relay.tick(store,'worker',report(),[],CFG,1000,False,
                                           wall=lambda:1000,allowed=lambda:allowed[0]),'reprise_deja_prise_en_charge')
                self.assertEqual(api.call_count,1)
            with patch.object(relay,'api') as api:
                self.assertEqual(relay.tick(store,'worker',report(),[],CFG,1120,False,
                                           allowed=lambda:False),'arrete_avant_reservation')
                api.assert_not_called()

    def test_cas_failure_cannot_send_and_bot_cannot_impersonate_human(self):
        with tempfile.TemporaryDirectory() as tmp:
            store=relay.SharedStore(tmp);store.read();store.write(state())
            with patch.object(store,'write',side_effect=RuntimeError('CAS')),patch.object(relay,'api') as api:
                with self.assertRaises(RuntimeError):relay.tick(store,'worker',report(),[],CFG,1000,False)
                api.assert_not_called()
            with patch.object(relay,'api',return_value={'login':CFG['requester_login'],'type':'Bot'}) as api:
                with self.assertRaises(RuntimeError):relay.tick(store,'worker',report(),[],CFG,1000,False)
                self.assertEqual(api.call_count,1)

    def test_corrupt_shared_state_is_preserved_and_cannot_claim(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'etat.json'
            for bad in [[],{'agent':{'expires':'later'}},{'worker':{'owner':'x','expires':float('nan')}},
                        {'codex_cloud':{'reserved_at':'later'}},{'codex_cloud':{'request_id':True}}]:
                raw=json.dumps(bad);path.write_text(raw)
                with self.assertRaises(ValueError):relay.guard.claim(relay.SharedStore(tmp),'other',1000,180)
                self.assertEqual(path.read_text(),raw)

    def test_pagination_includes_late_bot_failure(self):
        page=[comment(i+1,'history') for i in range(100)]
        with patch.object(relay,'api',side_effect=[page,[comment(101,'last')]]) as api:
            self.assertEqual(len(relay.comments(94)),101);self.assertEqual(api.call_count,2)

    def test_prompt_and_workflow_keep_course_priority_and_no_token_fallback(self):
        body=relay.prompt(report(),'unique')
        self.assertIn('prochain G2',body);self.assertIn('diagnostics différentiels sont suspendus',body)
        self.assertIn('--lease-seconds 180',body)
        root=Path(__file__).resolve().parents[1]
        workflow=(root/'.github/workflows/codex-cloud-120.yml').read_text()
        self.assertIn("cron: '*/5 * * * *'",workflow)
        self.assertIn('group: garde-progres',workflow)
        self.assertNotIn('AUTO_FUSION_TOKEN ||',workflow)
        self.assertNotIn('schedule:',(root/'.github/workflows/garde-progres.yml').read_text())


if __name__=='__main__':
    unittest.main()
