#!/usr/bin/env python3
"""Invocation explicite par l'agent pendant du travail réel, jamais depuis le watcher."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import uuid

HARNESS_FILES=('harnais/bracelet/bracelet_suggest.py','harnais/bracelet/catalog.json','harnais/ARSENAL.md')
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def record(repo, lot, phase, state, artifacts):
    if lot not in ('LOT_225','LOT_226'): raise ValueError('Lot hors périmètre')
    directory=Path('lot en cours de production')/lot
    proof=directory/'PREUVE_RUNTIME_HARNAIS.json'
    runtime=json.loads((repo/proof).read_text())
    if runtime.get('agent') != lot or runtime.get('complete') is not True:
        raise ValueError('Le test fonctionnel canonique propre à cet agent doit réussir avant le signal')
    if any(runtime.get('tests',{}).get(n,{}).get('ok') is not True for n in ('chonkie','llmlingua','gptcache')):
        raise ValueError('Les trois tests réels doivent être présents')
    entries=[]
    for name in artifacts:
        rel=Path(name)
        if rel.is_absolute() or '..' in rel.parts or not rel.is_relative_to(directory):
            raise ValueError('Un artefact doit rester dans le lot de cet agent')
        target=repo/rel
        if target.is_symlink() or not target.resolve().is_relative_to((repo/directory).resolve()):
            raise ValueError('Lien ou chemin externe interdit')
        entries.append({'path':rel.as_posix(),'sha256':digest(target)})
    if not entries: raise ValueError('Au moins un artefact réel est requis')
    result={'schema_version':1,'agent':lot,'activity_id':str(uuid.uuid4()),
            'recorded_at':datetime.now(timezone.utc).isoformat(),'state':state,'phase':phase,
            'runtime_proof':proof.as_posix(),'runtime_sha256':digest(repo/proof),
            'harness_sha256':{name:digest(repo/name) for name in HARNESS_FILES},'artifacts':entries,
            'declaration':'Invocation explicite pendant le travail réel; ce signal ne prouve pas une activité future.'}
    (repo/directory/'HARNAIS_ACTIVITE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    return result

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,default=Path.cwd());p.add_argument('--agent',required=True)
    p.add_argument('--phase',required=True);p.add_argument('--state',choices=['working','paused','blocked','finished'],default='working')
    p.add_argument('--artifact',action='append',required=True);a=p.parse_args()
    print(json.dumps(record(a.repo.resolve(),a.agent,a.phase,a.state,a.artifact),ensure_ascii=False))
if __name__=='__main__':main()
