#!/usr/bin/env python3
"""Réservation CAS d'un lancement CLI, distincte d'une preuve de travail IA."""
import argparse
import math
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import uuid

ROOT=Path(os.environ.get('OEF_REPO',Path(__file__).resolve().parents[2]))
sys.path.insert(0,str(ROOT))
from tools.garde.permanence import Store, live, busy_now

STATUS='demande_cli_non_execution_prouvee'
NOTIFICATION='demande_non_execution_prouvee'
FINISHED='tentative_cli_terminee_non_travail_prouve'
PROCESS_TTL=180  # lecture30s + écriture35s + attente30s + marge d'arrêt du groupe


def valide(state):
    if not isinstance(state,dict):raise ValueError('état partagé invalide')
    for key in ('agent','worker','demande'):
        if key not in state:continue
        lease=state[key]
        if (not isinstance(lease,dict) or not isinstance(lease.get('owner'),str)
            or not lease['owner'] or type(lease.get('expires')) not in (int,float)
            or not math.isfinite(lease['expires'])):
            raise ValueError('bail partagé invalide')
        if key=='demande' and lease.get('statut') not in (STATUS,NOTIFICATION,FINISHED):
            raise ValueError('type de demande inconnu')


def occupe(state, now):
    valide(state)
    # Le worker est une veille ; une notification n'est pas un exécuteur.
    request=state.get('demande',{})
    return (live(state.get('agent'),now)
            or request.get('statut') in (STATUS,FINISHED) and live(request,now))


def reserver(store, now=None):
    state=store.read()
    if occupe(state,time.time() if now is None else now) or busy_now():return None
    owner=uuid.uuid4().hex
    # La date n'est pas prise avant les lectures réseau, qui peuvent être lentes.
    stamp=time.time() if now is None else now
    state['demande']={'owner':owner,'expires':stamp+PROCESS_TTL,'statut':STATUS}
    store.write(state)  # Un conflit CAS interdit le lancement, sans nouvelle lecture aveugle.
    return owner


def liberer(store, owner, now=None):
    state=store.read();valide(state)
    if state.get('demande',{}).get('owner')==owner:
        stamp=time.time() if now is None else now
        state['demande']={'owner':owner,'expires':stamp+120,'statut':FINISHED}
        if state.get('agent',{}).get('owner')==owner:state.pop('agent')
        store.write(state)


def renouveler(store, owner, now=None):
    state=store.read();valide(state)
    if state.get('demande',{}).get('owner')!=owner or state['demande'].get('statut')!=STATUS:
        raise RuntimeError('réservation perdue')
    stamp=time.time() if now is None else now
    state['demande']['expires']=stamp+PROCESS_TTL
    store.write(state)


def executer(store, owner, command):
    """Bail de processus renouvelé, sans le présenter comme un bail d'activité IA.

    La perte d'état ou de réservation termine ce groupe de processus avant de
    laisser expirer sa réservation. Un autre hôte ne peut donc pas profiter
    d'une réservation périmée pendant une CLI longue encore supervisée.
    """
    renouveler(store,owner)
    def interrupted(signum,_frame):raise SystemExit(128+signum)
    signals=(signal.SIGTERM,signal.SIGHUP,signal.SIGINT)
    previous={s:signal.signal(s,interrupted) for s in signals}
    process=None
    try:
        process=subprocess.Popen(command,start_new_session=True)
        while True:
            try:return process.wait(timeout=30)
            except subprocess.TimeoutExpired:renouveler(store,owner)
    finally:
        for s in signals:signal.signal(s,signal.SIG_IGN)
        try:
            if process is not None and process.poll() is None:
                try:os.killpg(process.pid,signal.SIGTERM)
                except ProcessLookupError:pass
                try:process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    try:os.killpg(process.pid,signal.SIGKILL)
                    except ProcessLookupError:pass
                    process.wait()
        finally:
            for s,handler in previous.items():signal.signal(s,handler)


def main():
    p=argparse.ArgumentParser();p.add_argument('action',choices=['observer','reserver','liberer','executer'])
    p.add_argument('--owner');p.add_argument('command',nargs=argparse.REMAINDER);args=p.parse_args()
    store=Store(ROOT/'.etat_local/permanence',remote=True)
    try:
        if args.action=='executer':
            command=args.command
            if command and command[0]=='--':command=command[1:]
            if not args.owner or not command:raise ValueError('exécuteur incomplet')
            return executer(store,args.owner,command)
        if args.action=='liberer':
            if not args.owner:raise ValueError('propriétaire manquant')
            liberer(store,args.owner);return 0
        if args.action=='reserver':
            owner=reserver(store)
            if not owner:return 1
            print(owner);return 0
        state=store.read()
        return 0 if occupe(state,time.time()) or busy_now() else 1
    except Exception:
        print('état ou réservation distante indisponible ; aucune relance',file=sys.stderr)
        return 2


if __name__=='__main__':sys.exit(main())
