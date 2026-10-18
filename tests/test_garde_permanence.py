import copy
import json
from pathlib import Path
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch
from tools.garde.permanence import complete,policy,Store,claim,release,lock,stopped,worker,live,report_for


def report():
    return {'protocole':{'version':2,'rubriques':6,'chronologie_obligatoire':True},'plan':{'mission_exclusive':'infobulles_prototype6'},'mesure':{
        'diagnostics_uniques':2287,'prototype_structure':3,'prototype_relecture':3,
        'ssp_total':248,'ssp_prototype_structure':1,'ssp_prototype_relecture':1,
        'chronologie_structures':3,'chronologie_relectures':3,'ssp_chronologie_structures':1,'ssp_chronologie_relectures':1,
        'monographies_structure':257,'doublons_monographies':[]}}


class PermanenceTests(unittest.TestCase):
    def test_legacy_or_three_records_never_complete_all(self):
        r=report();self.assertFalse(complete(r))
        r['mesure'].update(prototype_structure=2287,prototype_relecture=2287,
                          ssp_prototype_structure=248,ssp_prototype_relecture=248,
                          chronologie_structures=2287,chronologie_relectures=2287,
                          ssp_chronologie_structures=248,ssp_chronologie_relectures=248)
        self.assertTrue(complete(r))
        r['mesure']['ssp_sans_dd']=['G1'];self.assertFalse(complete(r))
        r['mesure']['ssp_sans_dd']=[]
        r['mesure']['ssp_prototype_relecture']=247;self.assertFalse(complete(r))
        r['mesure']['ssp_prototype_relecture']=True;self.assertFalse(complete(r))

    def test_old_protocol_or_missing_chronology_proof_cannot_close(self):
        r=report();r['mesure'].update(prototype_structure=2287,prototype_relecture=2287,
            ssp_prototype_structure=248,ssp_prototype_relecture=248,
            chronologie_structures=2287,chronologie_relectures=2287,
            ssp_chronologie_structures=248,ssp_chronologie_relectures=248)
        self.assertTrue(complete(r))
        old=copy.deepcopy(r);old.pop('protocole');self.assertFalse(complete(old))
        old=copy.deepcopy(r);old['protocole']['chronologie_obligatoire']=1;self.assertFalse(complete(old))
        old=copy.deepcopy(r);old['mesure']['chronologie_relectures']=2286;self.assertFalse(complete(old))
        old=copy.deepcopy(r);old['mesure'].pop('ssp_chronologie_relectures');self.assertFalse(complete(old))

    def test_progress_and_regression_revoke_completion_and_expired_lease(self):
        state={};r=report();self.assertEqual(policy(state,r,0),'progression')
        self.assertEqual(policy(state,r,120),'relancer')
        state['agent']={'expires':200};self.assertEqual(policy(state,r,150),'occupe')
        self.assertEqual(policy(state,r,201),'relancer')
        state['complet']=True;r['mesure']['prototype_relecture']=2
        self.assertEqual(policy(state,r,250),'relancer');self.assertFalse(state['complet'])
        r['mesure']['prototype_relecture']=4;self.assertEqual(policy(state,r,260),'progression')

    def test_request_is_not_agent_execution_but_prevents_duplicate_notification(self):
        state={'dernier_progres':0,'mesure':{k:v for k,v in report()['mesure'].items() if k in ['prototype_structure','prototype_relecture','ssp_prototype_structure','ssp_prototype_relecture']},'demande':{'expires':120,'statut':'demande_non_execution_prouvee'}}
        self.assertEqual(policy(state,report(),119),'occupe')
        self.assertEqual(policy(state,report(),120),'relancer')
        self.assertEqual(policy(state,report(),700,busy=True),'occupe')

    def test_restart_cas_and_worker_lease(self):
        with tempfile.TemporaryDirectory() as tmp:
            a=Store(tmp);claim(a,'a',0,360)
            with self.assertRaises(RuntimeError):claim(Store(tmp),'b',120,360)
            b=Store(tmp);b.read();value=a.read();value['x']=1;a.write(value)
            with self.assertRaises(RuntimeError):b.write({'x':2})
            release(a,'a');claim(Store(tmp),'b',240,360)
            with lock(tmp):
                with self.assertRaises(RuntimeError):
                    with lock(tmp):pass

    def test_non_finite_agent_lease_is_never_activity(self):
        for expiry in (float('inf'),float('nan'),True):
            self.assertFalse(live({'expires':expiry},0))

    def test_snapshot_reads_the_existing_runtime_instead_of_empty_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            output=Path(tmp);(output/'coordination.json').write_text(json.dumps(report()))
            with patch('tools.garde.permanence.run') as command:
                report_for(Path('/snapshot'),output)
                args=command.call_args.args[0]
                self.assertIn('--state-dir',args)
                self.assertNotEqual(args[args.index('--state-dir')+1],'/snapshot/.etat_local/prevalences')

    def test_stop_controls_are_independent_of_completion(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertFalse(stopped({},tmp));self.assertTrue(stopped({'permanence_enabled':False},tmp))
            Path(tmp,'STOP').touch();self.assertTrue(stopped({},tmp))

    def test_bounded_window_ticks_and_short_waits_with_simulated_clock(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'tools/garde').mkdir(parents=True)
            (root/'tools/garde/config.json').write_text('{}')
            args=SimpleNamespace(state_dir=root/'state',github_state=False,refresh_main=False,notifier=False,window=240,daemon=False)
            clock=[0];ticks=[];waits=[]
            def sleep(seconds):waits.append(seconds);clock[0]+=seconds
            def measure(*_):ticks.append(clock[0]);return report()
            with patch('tools.garde.permanence.snapshot',return_value=root),patch('tools.garde.permanence.report_for',side_effect=measure),patch('tools.garde.permanence.log'):
                worker(args,clock=lambda:clock[0],wall=lambda:clock[0],sleeper=sleep)
            self.assertEqual(ticks,[0,120,240]);self.assertLessEqual(max(waits),25)
            state=json.loads((args.state_dir/'etat.json').read_text());self.assertFalse(state['complet']);self.assertNotIn('worker',state)

    def test_twenty_minute_window_provides_eleven_checks_without_extra_workers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'tools/garde').mkdir(parents=True)
            (root/'tools/garde/config.json').write_text('{}')
            args=SimpleNamespace(state_dir=root/'state',github_state=False,refresh_main=False,notifier=False,window=1200,daemon=False)
            clock=[0];ticks=[]
            def measure(*_):ticks.append(clock[0]);return report()
            with patch('tools.garde.permanence.snapshot',return_value=root),patch('tools.garde.permanence.report_for',side_effect=measure),patch('tools.garde.permanence.log'):
                worker(args,clock=lambda:clock[0],wall=lambda:clock[0],sleeper=lambda delay:clock.__setitem__(0,clock[0]+delay))
            self.assertEqual(ticks,list(range(0,1201,120)))

    def test_report_timeout_never_claims_completion_or_sends_notification(self):
        import subprocess
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'tools/garde').mkdir(parents=True)
            (root/'tools/garde/config.json').write_text('{}')
            args=SimpleNamespace(state_dir=root/'state',github_state=False,refresh_main=False,notifier=True,window=240,daemon=False)
            with patch('tools.garde.permanence.snapshot',return_value=root),patch('tools.garde.permanence.report_for',side_effect=subprocess.TimeoutExpired('calculer',35)),patch('tools.garde.permanence.busy_now') as activity:
                with self.assertRaises(subprocess.TimeoutExpired):worker(args)
                activity.assert_not_called()
            state=json.loads((args.state_dir/'etat.json').read_text())
            self.assertFalse(state.get('complet',False));self.assertNotIn('worker',state)

    def test_bounded_window_restart_does_not_cache_completed_verdict(self):
        with tempfile.TemporaryDirectory() as tmp:
            store=Store(tmp);s=store.read();s['complet']=True;s['dernier_progres']=0;store.write(s)
            state=Store(tmp).read();policy(state,report(),999)
            self.assertFalse(state['complet'])

if __name__=='__main__':unittest.main()
