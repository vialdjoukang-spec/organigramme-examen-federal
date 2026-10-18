#!/usr/bin/env python3
"""Réunit les résultats catégoriels sans perdre les relectures concurrentes."""
import argparse
import copy
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from tools.prevalences.moteur import CONFIG, atomic_json, merge_candidates


def combine(current, incoming):
    if current.get('category') != incoming.get('category') or incoming.get('version') != 1:
        raise ValueError('États incompatibles')
    result=copy.deepcopy(current)
    for key,new in incoming.get('tasks',{}).items():
        old=result.setdefault('tasks',{}).get(key)
        if not old:
            result['tasks'][key]=copy.deepcopy(new);continue
        if old.get('fingerprint')!=new.get('fingerprint'):
            # La version au lancement le plus récent conserve son libellé ; les
            # preuves d'un autre diagnostic ne sont jamais transférées.
            if new.get('date_recherche','')>old.get('date_recherche',''):
                result['tasks'][key]=copy.deepcopy(new)
            continue
        latest=new if new.get('date_recherche','')>=old.get('date_recherche','') else old
        row=copy.deepcopy(latest)
        # old = branche actuelle, peut contenir une relecture arrivée après le
        # départ du job. merge_candidates préserve ses preuves liées à la source.
        current_by_id={c['id']: c for c in old.get('candidates',[])}
        incoming_candidates=[]
        ignored=0
        for c in new.get('candidates',[]):
            prior=current_by_id.get(c['id'])
            changed=prior and any(prior.get(k)!=c.get(k) for k in ('url','extrait','sha256','document_sha256'))
            if changed and prior.get('date_recherche',old.get('date_recherche',''))>=c.get('date_recherche',new.get('date_recherche','')):
                ignored+=1;continue
            incoming_candidates.append(c)
        row['candidates'],counts=merge_candidates(old.get('candidates',[]),incoming_candidates,CONFIG['max_candidates_per_task'])
        row['artefacts_obsoletes_ignores']=ignored
        row.update(counts);result['tasks'][key]=row
    for key in ('maj','providers','dernier_lot','total_catalogue'):
        if incoming.get('maj','')>=current.get('maj','') and key in incoming:
            result[key]=copy.deepcopy(incoming[key])
    return result


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state-dir',required=True);p.add_argument('--artifact-dir',required=True)
    args=p.parse_args(argv)
    for category in CONFIG['categories']:
        source=Path(args.artifact_dir)/f'{category}.json'
        target=Path(args.state_dir)/f'{category}.json'
        if not source.exists():
            print(category+' : aucun résultat reçu, état précédent conservé');continue
        new=json.loads(source.read_text())
        old=json.loads(target.read_text()) if target.exists() else {'version':1,'category':category,'tasks':{}}
        atomic_json(target,combine(old,new))
    return 0


if __name__=='__main__':raise SystemExit(main())
