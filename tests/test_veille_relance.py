"""Contrat du relanceur shell : faux exécuteur local, aucune requête de modèle.

Les helpers de détection distante ont leurs propres tests dans
test_garde_permanence.py. Ici leurs réponses sont injectées pour vérifier
les décisions, les arguments de la CLI et les mutations du vrai script shell.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

SCRIPT = Path(__file__).resolve().parents[1]/'tools/veille_relance.sh'
HELPER = SCRIPT.parent/'garde/relance_bail.py'


class RelanceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.bin = self.root/'bin'
        self.bin.mkdir()
        (self.root/'tools/garde').mkdir(parents=True)
        (self.root/'tools/garde/config.json').write_text('{"permanence_enabled":true}')
        (self.root/'tools/garde/relance_bail.py').write_text(HELPER.read_text())
        (self.root/'ETAT.json').write_text('{"etape_courante":9,"statut":"en_cours"}\n')
        os.utime(self.root/'ETAT.json', (time.time()-120,)*2)
        (self.root/'tools/etapes.json').write_text('{"etapes":[{"n":9,"modele":"defaut"}]}')
        (self.root/'shared.json').write_text('{}')
        (self.root/'tools/garde/permanence.py').write_text('''
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class Store:
    def __init__(self,*args,**kwargs): pass
    def read(self): return json.loads((ROOT/'shared.json').read_text())
    def write(self,value): (ROOT/'shared.json').write_text(json.dumps(value))
def live(lease, now): return isinstance(lease,dict) and lease['expires']>now
def busy_now(): return Store().read().get('ci',False)
''')
        (self.root/'tools/porte.py').write_text('''
import sys
if sys.argv[1]=='critere':sys.exit(1)
if sys.argv[1]=='ordre':print('Reprends la mission au point enregistré.')
''')
        self.executable('git', '#!/bin/sh\nexit 0\n')
        self.executable('pgrep', '#!/bin/sh\nexit 1\n')
        self.executable('codex', '''#!/usr/bin/env python3
import json,os,sys,time
from pathlib import Path
with Path(os.environ['FAKE_CALLS']).open('a') as h:
 h.write(json.dumps({'simulation':True,'args':sys.argv[1:]})+'\\n')
print(os.environ.get('FAKE_ERROR',''),file=sys.stderr)
time.sleep(float(os.environ.get('FAKE_DELAY','0')))
sys.exit(int(os.environ.get('FAKE_EXIT','0')))
''')
        self.env = dict(os.environ, OEF_REPO=str(self.root),
                        PATH=str(self.bin)+os.pathsep+os.environ['PATH'],
                        FAKE_CALLS=str(self.root/'calls.jsonl'))
        for name in ('INACTIF_SECONDES','INACTIF_MIN'):
            self.env.pop(name,None)

    def executable(self, name, text):
        p=self.bin/name;p.write_text(text);p.chmod(0o755)

    def run_once(self,*args):
        return subprocess.run(['bash',str(SCRIPT),'--une-fois','--sans-fusion',*args],
                              env=self.env,capture_output=True,text=True,timeout=8)

    def calls(self):
        p=self.root/'calls.jsonl'
        return [json.loads(s) for s in p.read_text().splitlines()] if p.exists() else []

    def test_idle_120_launches_executor_with_supported_cli_and_preserves_state(self):
        p=self.root/'ETAT.json';before=(p.read_bytes(),p.stat().st_mtime_ns)
        r=self.run_once();self.assertEqual(r.returncode,0,r.stderr)
        args=self.calls()[0]['args']
        self.assertNotIn('--full-auto',args)
        self.assertEqual(args[0],'exec')
        self.assertEqual(args[args.index('-s')+1],'workspace-write')
        self.assertIn('approval_policy="never"',args)
        self.assertTrue(any(s.startswith('Reprends la mission au point enregistré.') for s in args))
        self.assertEqual((p.read_bytes(),p.stat().st_mtime_ns),before)
        self.assertIn('code0',r.stderr)
        self.assertIn('résultat à contrôler',r.stderr)

    def test_recent_work_does_not_launch(self):
        os.utime(self.root/'ETAT.json',None)
        r=self.run_once();self.assertEqual(r.returncode,0)
        self.assertEqual(self.calls(),[])

    def test_live_agent_or_ci_blocks_before_mutating_finished_stage(self):
        for state in ({'agent':{'owner':'agent-actif','expires':time.time()+180}},{'ci':True}):
            with self.subTest(state=state):
                (self.root/'shared.json').write_text(json.dumps(state))
                (self.root/'ETAT.json').write_text('{"etape_courante":9,"statut":"terminee"}')
                before=(self.root/'ETAT.json').read_bytes()
                r=self.run_once();self.assertEqual(r.returncode,0,r.stderr)
                self.assertEqual(self.calls(),[])
                self.assertEqual((self.root/'ETAT.json').read_bytes(),before)
                self.assertFalse((self.root/'PROCHAINE_ACTION.md').exists())

    def test_unknown_remote_state_fails_closed(self):
        (self.root/'shared.json').write_text('bad json')
        r=self.run_once();self.assertEqual(r.returncode,0)
        self.assertEqual(self.calls(),[])
        self.assertIn('inconnue',r.stderr)

    def test_existing_codex_prevents_all_step_mutations(self):
        self.executable('pgrep','#!/bin/sh\nexit 0\n')
        r=self.run_once();self.assertEqual(r.returncode,0)
        self.assertEqual(self.calls(),[])
        self.assertFalse((self.root/'PROCHAINE_ACTION.md').exists())

    def test_corrupt_state_is_preserved_without_merging_or_restarting(self):
        p=self.root/'ETAT.json';p.write_text('partial json')
        r=self.run_once();self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(p.read_text(),'partial json')
        self.assertEqual(self.calls(),[])
        self.assertFalse((self.root/'PROCHAINE_ACTION.md').exists())

    def test_malformed_agent_lease_is_unknown_not_expired(self):
        (self.root/'shared.json').write_text('{"agent":{"owner":"a","expires":"bad"}}')
        r=self.run_once();self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(self.calls(),[])
        self.assertIn('inconnue',r.stderr)

    def test_suspended_stage_cannot_override_exclusive_mission(self):
        (self.root/'ETAT.json').write_text('{"etape_courante":8,"statut":"en_cours","mission_exclusive":{"id":"infobulles_prototype6"}}')
        os.utime(self.root/'ETAT.json',(time.time()-120,)*2)
        r=self.run_once();self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(self.calls(),[])
        self.assertIn('incohérente',r.stderr)

    def test_old_model_error_cannot_trigger_fallback_of_current_failure(self):
        p=self.root/'.etat_local';p.mkdir()
        (p/'codex_exec.log').write_text('old model invalid\n')
        (self.root/'tools/etapes.json').write_text('{"etapes":[{"n":9,"modele":"luna"}]}')
        self.env['FAKE_EXIT']='23'
        r=self.run_once();self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(len(self.calls()),1)

    def test_fusion_is_disabled_by_default(self):
        (self.root/'tools/file_fusion.sh').write_text('exit 99\n')
        r=subprocess.run(['bash',str(SCRIPT),'--une-fois'],env=self.env,
                         capture_output=True,text=True,timeout=8)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertNotIn('file_fusion a échoué',r.stderr)

    def test_failed_attempt_does_not_fake_activity_or_repeat_within_120s(self):
        p=self.root/'ETAT.json';before=p.stat().st_mtime_ns
        self.env['FAKE_EXIT']='23'
        r=self.run_once();self.assertEqual(r.returncode,0)
        self.assertIn('code23',r.stderr)
        self.assertEqual(p.stat().st_mtime_ns,before)
        self.run_once();self.assertEqual(len(self.calls()),1)

    def test_concurrent_watchers_cannot_start_two_executors(self):
        self.env['FAKE_DELAY']='0.5'
        first=subprocess.Popen(['bash',str(SCRIPT),'--une-fois','--sans-fusion'],
                               env=self.env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        try:
            deadline=time.monotonic()+3
            while not self.calls() and time.monotonic()<deadline:time.sleep(0.01)
            self.assertEqual(len(self.calls()),1)
            self.run_once()
            first.communicate(timeout=8)
            self.assertEqual(len(self.calls()),1)
        finally:
            if first.poll() is None:first.kill();first.communicate()

    def test_stop_and_default_tick_120(self):
        p=self.root/'.etat_local/permanence';p.mkdir(parents=True)
        (p/'STOP').touch()
        r=subprocess.run(['bash',str(SCRIPT),'--boucle','--sans-fusion'],env=self.env,
                         capture_output=True,text=True,timeout=3)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertIn('120 s',r.stderr)
        self.assertEqual(self.calls(),[])

    def test_dry_run_never_starts_executor(self):
        r=self.run_once('--dry-run');self.assertEqual(r.returncode,0)
        self.assertEqual(self.calls(),[])
        self.assertFalse((self.root/'PROCHAINE_ACTION.md').exists())

    def test_common_stop_disables_executor(self):
        (self.root/'tools/garde/config.json').write_text('{"permanence_enabled":false}')
        r=self.run_once();self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(self.calls(),[])
        self.assertIn('arrêt commun',r.stderr)

    def test_finished_exclusive_lot_never_advances_into_suspended_stage(self):
        p=self.root/'ETAT.json'
        p.write_text('{"etape_courante":9,"statut":"terminee","mission_exclusive":{"id":"infobulles_prototype6"}}')
        before=p.read_bytes()
        (self.root/'tools/porte.py').write_text('''
import sys
from pathlib import Path
if sys.argv[1]=='avancer':Path(__file__).parents[1].joinpath('ETAT.json').write_text('{"etape_courante":10}')
if sys.argv[1]=='ordre':print('Reprends la mission au point enregistré.')
''')
        r=self.run_once();self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(len(self.calls()),1)
        self.assertEqual(p.read_bytes(),before)

    def test_agent_arriving_during_fetch_prevents_every_write(self):
        self.executable('git','''#!/usr/bin/env python3
import os,json,time
from pathlib import Path
Path(os.environ['OEF_REPO'],'shared.json').write_text(json.dumps({'agent':{'owner':'arrive-pendant-fetch','expires':time.time()+180}}))
''')
        p=self.root/'ETAT.json';before=p.read_bytes()
        r=self.run_once();self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(self.calls(),[])
        self.assertEqual(p.read_bytes(),before)
        self.assertFalse((self.root/'PROCHAINE_ACTION.md').exists())

    def test_sigterm_supervisor_stops_actual_child_without_model_call(self):
        state={'demande':{'owner':'test','expires':time.time()+180,'statut':'demande_cli_non_execution_prouvee'}}
        (self.root/'shared.json').write_text(json.dumps(state))
        childpid=self.root/'child.pid'
        code='import os,time;from pathlib import Path;Path('+repr(str(childpid))+').write_text(str(os.getpid()));time.sleep(60)'
        supervisor=subprocess.Popen([sys.executable,str(self.root/'tools/garde/relance_bail.py'),'--owner','test','executer','--',sys.executable,'-c',code],env=self.env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        child=None
        try:
            deadline=time.monotonic()+4
            while not childpid.exists() and time.monotonic()<deadline:time.sleep(0.01)
            self.assertTrue(childpid.exists())
            child=int(childpid.read_text())
            supervisor.terminate();supervisor.communicate(timeout=8)
            self.assertEqual(supervisor.returncode,143)
            with self.assertRaises(ProcessLookupError):os.kill(child,0)
        finally:
            if supervisor.poll() is None:supervisor.kill();supervisor.communicate()
            if child:
                try:os.kill(child,9)
                except ProcessLookupError:pass


if __name__=='__main__':unittest.main()
