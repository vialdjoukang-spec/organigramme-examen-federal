#!/usr/bin/env python3
"""Ordonnanceur léger : observe les exécutions, évite doublons et respecte le budget."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from tools.coordination.calculer import CONFIG
REPO='vialdjoukang-spec/organigramme-examen-federal'
ACTIVE={'queued','in_progress','waiting','pending','requested'}

def decision(runs,plan,now=None,amorcer=False):
    now=now or datetime.now(timezone.utc)
    if plan.get('mission_exclusive') == 'infobulles_prototype6':
        return {'lancer':False,'motif':'mission infobulles : recherches automatiques transversales suspendues ; rechercher manuellement dans le lot courant'}
    if plan.get('etat_recherche_fiable') is False:return {'lancer':False,'motif':'état documentaire inconnu : corriger avant recherche'}
    if not isinstance(runs,dict) or not isinstance(runs.get('workflow_runs'),list): return {'lancer':False,'motif':'état des exécutions inconnu'}
    history=runs['workflow_runs']
    if any(r.get('status') in ACTIVE for r in history):return {'lancer':False,'motif':'recherche déjà active'}
    times=[]
    for run in history:
        try:
            stamp=datetime.fromisoformat(run['created_at'].replace('Z','+00:00'))
            if stamp.tzinfo is None:raise ValueError('date sans fuseau')
            times.append(stamp)
        except (ValueError,KeyError,TypeError):return {'lancer':False,'motif':'horodatage inconnu'}
    if not amorcer and times and (now-max(times)).total_seconds()<60*plan['intervalle_recherche_minutes']:return {'lancer':False,'motif':'temporisation de recherche'}
    return {'lancer':True,'motif':'recherche arrivée à échéance','limite':plan['limite_recherche']}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--plan',type=Path,required=True);p.add_argument('--lancer',action='store_true');p.add_argument('--amorcer',action='store_true',help='Activation explicite après déploiement de la configuration, sans ignorer état inconnu ou recherche active');args=p.parse_args();plan=json.loads(args.plan.read_text())
    # Current configuration overrides a stale plan. No API call or dispatch,
    # even with --amorcer, until the research engine supports strict scope.
    if CONFIG.get('mission_exclusive') == 'infobulles_prototype6':
        plan['mission_exclusive']='infobulles_prototype6'
    if plan.get('mission_exclusive') == 'infobulles_prototype6':
        print(json.dumps(decision(None,plan),ensure_ascii=False));return
    command=['gh','api',f'repos/{REPO}/actions/workflows/prevalences-recherche.yml/runs?branch=main&per_page=20']
    try:
        raw=subprocess.run(command,capture_output=True,text=True,check=True,timeout=30);result=decision(json.loads(raw.stdout),plan,amorcer=args.amorcer)
    except (subprocess.SubprocessError,ValueError):result={'lancer':False,'motif':'accès aux exécutions indisponible : aucune action aveugle'}
    if args.lancer and result['lancer']:
        launch=subprocess.run(['gh','workflow','run','prevalences-recherche.yml','--repo',REPO,'--ref','main','-f',f'limite={result["limite"]}'],capture_output=True,text=True,timeout=30)
        result['demande_enregistree']=launch.returncode==0;result['execution_prouvee']=False
    print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
