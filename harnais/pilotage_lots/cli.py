#!/usr/bin/env python3
"""Bilan gratuit en lecture seule depuis GitHub Actions; aucune relance IA simulée."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
import urllib.error

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from harnais.pilotage_lots.engine import (validate_state,evaluate_lot,CONTROL_BRANCH,LEDGER_PATH)
from harnais.surveillance.watchdog import GitHub, assess_agent, sha

class Reader(GitHub):
    def file(self,path,head):
        try:return super().file(path,head)
        except urllib.error.HTTPError as exc:
            if exc.code==404: raise FileNotFoundError(path) from exc
            raise

def collect(api,state,now,repo):
    validate_state(state)
    result={'checked_at':now.isoformat(),'campaign':state['campaign'],'campaign_status':state['status'],
      'stop_requested':state['stop_requested'],'clinical_validation':False,'jobs':[],
      'completed_registered_not_reaudited':[{'lot':j['lot'],'validated_head':j['validated_head']} for j in state['jobs'] if j['state']=='completed'],
      'quota_remaining':'Non accessible; aucune estimation inventée.',
      'scope':'Contrôle de preuves publiées; ni audit médical automatique ni observation directe des processus GPT.'}
    hashes={name:sha((repo/name).read_bytes()) for name in ('harnais/bracelet/bracelet_suggest.py','harnais/bracelet/catalog.json','harnais/ARSENAL.md')}
    for job in state['jobs']:
        if job['state']=='completed': continue  # Historique explicite; lectures bornées aux deux agents actifs.
        evaluation=evaluate_lot(api,job,now)
        agent={'id':job['lot'],'branch':job['branch'],'directory':'lot en cours de production/'+job['lot']}
        evaluation['harness']=assess_agent({'activity_max_age_seconds':900,'runtime_max_age_seconds':3600,'clock_skew_seconds':120},agent,api,now,hashes)
        result['jobs'].append(evaluation)
    result['checked_jobs_complete']=all(j['complete'] for j in result['jobs'])
    result['may_resume']=state['status']=='active' and not state['stop_requested']
    return result

def main():
    p=argparse.ArgumentParser();p.add_argument('--repository',default='vialdjoukang-spec/organigramme-examen-federal')
    p.add_argument('--state-branch',default=CONTROL_BRANCH);p.add_argument('--output',type=Path,default=Path('/tmp/lots-pilotage.json'));a=p.parse_args()
    api=Reader(a.repository,os.environ.get('GH_TOKEN'));now=datetime.now(timezone.utc)
    state_head=api.head(a.state_branch)
    state=json.loads(api.file(LEDGER_PATH,state_head));result=collect(api,state,now,ROOT)
    result['registry_head']=state_head
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'],'a') as out:
            out.write('\n## Pilotage inverse — état réel\n\n')
            out.write('Le contrôleur ne rédige pas de médecine et ne démarre pas une session GPT. La tâche GPT horaire assure la reprise, sous réserve de ses outils et du forfait.\n\n')
            for job in result['jobs']:
                out.write('- '+job['lot']+': '+('portes complètes' if job['complete'] else 'brouillon / contrôles incomplets')+'; prochaine action: '+json.dumps(job['next_action'],ensure_ascii=False)+'\n')
            out.write('\nQuota restant: non accessible. Une absence de preuve n’est jamais un succès clinique.\n')
    return 0

if __name__=='__main__':
    try:raise SystemExit(main())
    except (ValueError,TypeError,KeyError,OSError,urllib.error.URLError) as exc:
        print('Pilotage non vérifiable: '+str(exc),file=sys.stderr);raise SystemExit(1)
