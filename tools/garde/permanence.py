#!/usr/bin/env python3
"""Veille bornée : passages120s pendant une fenêtre de20min ; les notifications ne prouvent aucune exécution IA."""
import argparse
import base64
from contextlib import contextmanager
import fcntl
import hashlib
import json
import math
import os
import shutil
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import time
import uuid

ROOT = Path(__file__).resolve().parents[2]
REPO = os.environ.get('GH_REPO', 'vialdjoukang-spec/organigramme-examen-federal')
ACTIVE = {'queued', 'in_progress', 'waiting', 'pending', 'requested'}
MISSION = 'infobulles_prototype6'
REMOTE = 'veille/permanence.json'


def log(event, **values):
    print(json.dumps(dict(event=event, utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), **values), ensure_ascii=False), flush=True)


def complete(report):
    """Exact, non-rounded current hash-backed documentary counts, never legacy counts."""
    if not isinstance(report, dict) or report.get('plan', {}).get('mission_exclusive') != MISSION:
        return False
    protocol = report.get('protocole', {})
    if (not isinstance(protocol,dict) or type(protocol.get('version')) is not int or protocol['version'] != 2
            or type(protocol.get('rubriques')) is not int or protocol['rubriques'] != 6
            or protocol.get('chronologie_obligatoire') is not True):
        return False
    m = report.get('mesure', {})
    scope = report['plan'].get('perimetre_monographies')
    checks = [('diagnostics_uniques', 'prototype_structure', 'prototype_relecture'),
              ('diagnostics_uniques', 'chronologie_structures', 'chronologie_relectures')]
    if scope is None:
        # Ancien contrat conservé pour les rapports sans périmètre explicite.
        checks += [('ssp_total', 'ssp_prototype_structure', 'ssp_prototype_relecture'),
                   ('ssp_total', 'ssp_chronologie_structures', 'ssp_chronologie_relectures')]
    elif scope != 'diagnostics_differentiels':
        return False
    for total, structured, reviewed in checks:
        vals = [m.get(k) for k in (total, structured, reviewed)]
        if any(type(v) is not int for v in vals) or vals[0] <= 0 or vals != [vals[0]] * 3:
            return False
    return not m.get('doublons_monographies') and not m.get('ssp_sans_dd') and not report.get('plan', {}).get('anomalies_etat')


def digest(report):
    m = report['mesure']
    keys = ['prototype_structure', 'prototype_relecture']
    if report.get('plan', {}).get('perimetre_monographies') != 'diagnostics_differentiels':
        keys += ['ssp_prototype_structure', 'ssp_prototype_relecture']
    return {k: m[k] for k in keys}


def live(lease, now):
    return isinstance(lease, dict) and type(lease.get('expires')) in (int, float) and math.isfinite(lease['expires']) and lease['expires'] > now


def policy(state, report, now, busy=False):
    metrics = digest(report)
    prior = state.get('mesure')
    # A regression revokes completion and does not fabricate positive progress.
    progressed = prior is None or any(metrics[k] > prior.get(k, 0) for k in metrics)
    state.update(mesure=metrics, complet=complete(report), maj=now)
    if progressed:
        state['dernier_progres'] = now
    if state['complet']:
        return 'termine'
    if busy or live(state.get('agent'), now) or live(state.get('demande'), now):
        return 'occupe'
    if now - state.get('dernier_progres', now) < 120:
        return 'progression'
    return 'relancer'


def run(cmd, cwd=ROOT, timeout=35, data=None):
    result = subprocess.run(cmd, cwd=cwd, input=data, capture_output=True, text=True, timeout=timeout)
    if result.returncode:
        raise RuntimeError('commande échouée : ' + cmd[0])
    return result.stdout


class Store:
    """Local atomic state or GitHub Contents compare-and-swap; no blind overwrite."""
    def __init__(self, directory, remote=False):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.remote = remote
        self.path = self.directory / 'etat.json'
        self.sha = None

    def read(self):
        if not self.remote:
            raw = self.path.read_text() if self.path.exists() else ''
            self.sha = hashlib.sha256(raw.encode()).hexdigest()
            return json.loads(raw) if raw else {}
        response = subprocess.run(['gh','api',f'repos/{REPO}/contents/{REMOTE}?ref=garde/etat'],
                                  capture_output=True,text=True,timeout=30)
        if response.returncode:
            # Only an explicit missing file is initializable; 401/network stay unknown.
            if '404' not in response.stderr:
                raise RuntimeError('état distant indisponible')
            self.sha = None
            return {}
        value = json.loads(response.stdout)
        self.sha = value['sha']
        return json.loads(base64.b64decode(value['content']))

    def write(self, value):
        data = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
        if self.remote:
            payload = {'message':'veille : passage et baux, sans validation clinique','branch':'garde/etat',
                       'content':base64.b64encode(data.encode()).decode()}
            if self.sha:
                payload['sha'] = self.sha
            result = json.loads(run(['gh','api',f'repos/{REPO}/contents/{REMOTE}','-X','PUT','--input','-'], data=json.dumps(payload)))
            self.sha = result['content']['sha']
        with lock(self.directory, 'state.lock'):
            if not self.remote:
                current = self.path.read_text() if self.path.exists() else ''
                if hashlib.sha256(current.encode()).hexdigest() != self.sha:
                    raise RuntimeError('état local modifié simultanément')
                self.sha = hashlib.sha256(data.encode()).hexdigest()
            temporary = self.path.with_suffix('.' + uuid.uuid4().hex + '.tmp')
            temporary.write_text(data)
            temporary.replace(self.path)


@contextmanager
def lock(directory, name='worker.lock'):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    with (directory/name).open('a') as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError('veille locale déjà active')
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def claim(store, owner, now, duration):
    state = store.read()
    if live(state.get('worker'), now) and state['worker'].get('owner') != owner:
        raise RuntimeError('bail de veille déjà actif')
    state['worker'] = {'owner':owner,'expires':now + duration}
    store.write(state)  # CAS failure blocks this worker, never starts a second writer.
    return state


def snapshot(directory, refresh):
    """Never reset the interactive checkout. Snapshot current origin/main elsewhere."""
    if not refresh:
        return ROOT
    run(['git','fetch','-q','origin','main'])
    target = Path(directory)/'main'
    target.mkdir(parents=True, exist_ok=True)
    # A fresh directory avoids retaining deleted canonical files from a previous main.
    temp = Path(tempfile.mkdtemp(prefix='tick-', dir=target))
    archive = temp/'main.tar'
    with archive.open('wb') as output:
        subprocess.run(['git','archive','origin/main'],cwd=ROOT,stdout=output,check=True,timeout=30)
    with tarfile.open(archive) as handle:
        handle.extractall(temp, filter='data')
    archive.unlink()
    gitdir = run(['git','rev-parse','--absolute-git-dir']).strip()
    (temp/'.git').write_text('gitdir: ' + gitdir + '\n')
    return temp


def report_for(root, output):
    run([sys.executable,'tools/coordination/calculer.py','--state-dir',str(ROOT/'.etat_local/prevalences'),'--output',str(output)],cwd=root)
    return json.loads((output/'coordination.json').read_text())


def busy_now():
    # Process detection is a duplicate-prevention hint, not a claim of useful work.
    processes = subprocess.run(['pgrep','-f',r'(^|/)codex exec( |$)'],capture_output=True,timeout=5)
    if processes.returncode == 0:
        return True
    prs = json.loads(run(['gh','api',f'repos/{REPO}/pulls?state=open&per_page=100']))
    heads = {p['head']['sha'] for p in prs if not p.get('draft')}
    runs = json.loads(run(['gh','api',f'repos/{REPO}/actions/runs?per_page=100']))['workflow_runs']
    return any(r.get('status') in ACTIVE and r.get('head_sha') in heads
               and r.get('name') not in ('Garde du progrès',) for r in runs)


def release(store, owner):
    state = store.read()
    if state.get('worker', {}).get('owner') == owner:
        state.pop('worker', None)
        store.write(state)


def stopped(config, directory):
    return config.get('permanence_enabled') is False or (Path(directory)/'STOP').exists()


def worker(args, clock=time.monotonic, wall=time.time, sleeper=time.sleep):
    store = Store(args.state_dir, args.github_state)
    owner = uuid.uuid4().hex
    start = clock()
    index = 0
    with lock(args.state_dir):
        try:
            while True:
                due = start + index * 120
                while clock() < due:
                    if (Path(args.state_dir)/'STOP').exists():
                        log('stop_demande'); return
                    remaining = due - clock()
                    log('prochain_passage',dans_secondes=round(remaining),passage=index)
                    sleeper(min(25,remaining))
                root = None
                try:
                    root = snapshot(args.state_dir, args.refresh_main)
                    config = json.loads((root/'tools/garde/config.json').read_text())
                    if stopped(config,args.state_dir):
                        log('stop_configuration'); return
                    claim(store,owner,wall(),180)
                    output = root/'.etat_local/coordination'
                    output.mkdir(parents=True,exist_ok=True)
                    report = report_for(root,output)
                    if args.refresh_main:
                        stable = ROOT/'.etat_local/coordination'
                        stable.mkdir(parents=True,exist_ok=True)
                        for name in ('coordination.json','priorites.json','coordination.html'):
                            shutil.copy2(output/name,stable/name)
                    if report['plan'].get('mission_exclusive') != MISSION:
                        log('mission_inconnue_sans_relance'); return
                    busy = True
                    if args.notifier:
                        try:
                            busy = busy_now()
                        except (RuntimeError,ValueError,subprocess.SubprocessError):
                            log('activite_inconnue_sans_relance')
                    # Refresh after reads: preserve an agent acknowledgement received meanwhile.
                    state = store.read()
                    if state.get('worker',{}).get('owner') != owner:
                        raise RuntimeError('bail de veille perdu')
                    action = policy(state,report,wall(),busy)
                    if action == 'relancer' and args.notifier:
                        state['demande']={'owner':owner,'expires':wall()+120,'statut':'demande_non_execution_prouvee'}
                    store.write(state)
                    observed_action = action if args.notifier or action == 'termine' else 'observation_sans_notification'
                    log('passage',numero=index,action=observed_action,mesure=state['mesure'],validation_clinique=False)
                    if action == 'termine':
                        log('tous_ssp_dd_revus_empreintes_courantes'); return
                    if action == 'relancer' and args.notifier:
                        env = dict(os.environ,OEF_GARDE_RELANCE_PERMISE='1')
                        result = subprocess.run([sys.executable,'tools/garde/progres.py'],cwd=root,env=env,
                                                capture_output=True,text=True,timeout=45)
                        log('relance',code=result.returncode,execution_agent_prouvee=False)
                finally:
                    if root is not None and args.refresh_main:
                        shutil.rmtree(root,ignore_errors=True)
                if not args.daemon and (index+1)*120 > args.window:
                    log('fenetre_terminee',tache_terminee=False,prochain_declencheur='cron GitHub 5 min, retard possible'); return
                index += 1
        finally:
            try:
                release(store,owner)
            except (RuntimeError,ValueError,KeyError,OSError,subprocess.SubprocessError):
                log('liberation_bail_impossible',expiration_max_secondes=180,tache_terminee=False)


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state-dir',type=Path,default=ROOT/'.etat_local/permanence')
    p.add_argument('--window',type=int,default=1200)
    p.add_argument('--daemon',action='store_true')
    p.add_argument('--refresh-main',action='store_true')
    p.add_argument('--github-state',action='store_true')
    p.add_argument('--notifier',action='store_true')
    p.add_argument('--agent',help='déclarer/rafraîchir un bail d’agent effectivement actif, sans démarrer une IA')
    p.add_argument('--lease-seconds',type=int,default=600)
    args=p.parse_args(argv)
    if args.window < 0 or args.lease_seconds < 1:
        p.error('durées invalides')
    try:
        if args.agent:
            with lock(args.state_dir, 'agent-command.lock'):
                store=Store(args.state_dir,args.github_state);state=store.read()
                prior=state.get('agent')
                if live(prior,time.time()) and prior.get('owner')!=args.agent:
                    raise RuntimeError('autre agent déclaré actif')
                state['agent']={'owner':args.agent,'expires':time.time()+args.lease_seconds,'statut':'execution_signalee_non_validation'}
                store.write(state);log('bail_agent_enregistre');return 0
        worker(args)
    except (RuntimeError,ValueError,KeyError,OSError,subprocess.SubprocessError) as error:
        # No raw remote stderr, tokens, signed URLs or blind fallback notification.
        log('veille_interrompue',type=type(error).__name__,motif=str(error) if isinstance(error,RuntimeError) else 'voir le type d’erreur, aucun détail sensible publié',tache_terminee=False)
        return 1
    return 0


if __name__=='__main__':
    raise SystemExit(main())
