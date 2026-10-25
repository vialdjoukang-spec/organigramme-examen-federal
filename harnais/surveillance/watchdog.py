#!/usr/bin/env python3
"""Contrôle distant en lecture seule. N'exécute jamais le code des branches surveillées."""
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

TOOLS=('chonkie','llmlingua','gptcache')
EXPECTED_VERSIONS={'chonkie':'1.7.0','llmlingua':'0.2.2','gptcache':'0.1.44','torch':'2.14.1+cpu','transformers':'5.20.2'}
MODEL='microsoft/llmlingua-2-bert-base-multilingual-cased-meetingbank'
REVISION='5f0c82792b7ea14c6484e015b6a072009496b7f2'
MAX_JSON=200_000
class GitHub:
    def __init__(self, repository, token=None):
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repository):raise ValueError('Dépôt invalide')
        self.root='https://api.github.com/repos/'+repository
        self.headers={'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'harnais-watchdog'}
        if token:self.headers['Authorization']='Bearer '+token
    def request(self,path):
        req=urllib.request.Request(self.root+path,headers=self.headers)
        with urllib.request.urlopen(req,timeout=20) as response:
            data=response.read(MAX_JSON*8+1)
        if len(data)>MAX_JSON*8:raise ValueError('Réponse trop volumineuse')
        return json.loads(data)
    def head(self,branch):return self.request('/git/ref/heads/'+urllib.parse.quote(branch,safe=''))['object']['sha']
    def file(self,path,sha):
        data=self.request('/contents/'+urllib.parse.quote(path,safe='/')+'?ref='+urllib.parse.quote(sha,safe=''))
        if data.get('encoding')!='base64' or data.get('size',1_000_001)>1_000_000:raise ValueError('Fichier non lisible ou trop volumineux')
        return base64.b64decode(data['content'],validate=False)

def sha(data):return hashlib.sha256(data).hexdigest()
def age(iso,now):
    if not isinstance(iso,str):raise ValueError('Horodatage non textuel')
    parsed=datetime.fromisoformat(iso.replace('Z','+00:00'))
    if parsed.tzinfo is None:raise ValueError('Horodatage sans fuseau')
    return (now-parsed).total_seconds()
def json_object(data):
    if len(data)>MAX_JSON:raise ValueError('Preuve trop volumineuse')
    obj=json.loads(data)
    if not isinstance(obj,dict):raise ValueError('Un objet JSON est requis')
    return obj

def assess_agent(config, agent, api, now, trusted_hashes=None):
    result={'agent':agent['id'],'branch':agent['branch'],'ok':False,'activity':'unknown','errors':[]}
    try:
        head=api.head(agent['branch']);result['head']=head
        directory=PurePosixPath(agent['directory'])
        proof=json_object(api.file(str(directory/'HARNAIS_ACTIVITE.json'),head))
        if type(proof.get('schema_version')) is not int or proof.get('schema_version')!=1 or proof.get('agent')!=agent['id']:raise ValueError('Identité ou schéma de preuve incorrect')
        if proof.get('state') not in ('working','paused','blocked','finished'):raise ValueError('État non reconnu')
        seconds=age(proof['recorded_at'],now);result['age_seconds']=round(seconds)
        if seconds < -config['clock_skew_seconds']:raise ValueError('Preuve située dans le futur')
        state=proof['state']
        result['activity']=state if state!='working' else ('recent' if seconds<=config['activity_max_age_seconds'] else 'stale')
        if result['activity']=='stale':result['errors'].append('Activité de travail non prouvée récemment; le contrôleur ne renouvelle pas ce signal.')
        allowed=str(directory/'PREUVE_RUNTIME_HARNAIS.json')
        if proof.get('runtime_proof')!=allowed:raise ValueError('Preuve runtime hors périmètre')
        raw=api.file(allowed,head)
        if sha(raw)!=proof.get('runtime_sha256'):raise ValueError('Empreinte de preuve runtime différente')
        runtime=json_object(raw)
        if runtime.get('agent')!=agent['id'] or type(runtime.get('schema_version')) is not int or runtime.get('schema_version')!=1 or runtime.get('complete') is not True:
            raise ValueError('Test fonctionnel complet propre à cet agent absent')
        tests=runtime.get('tests')
        if not isinstance(tests,dict):raise ValueError('Tests runtime non structurés')
        for name in TOOLS:
            if not isinstance(tests.get(name),dict) or tests[name].get('ok') is not True:raise ValueError('Test réel absent ou échoué: '+name)
        versions=runtime.get('versions')
        if not isinstance(versions,dict) or any(versions.get(k)!=v for k,v in EXPECTED_VERSIONS.items()):raise ValueError('Versions runtime non attestées ou différentes des versions testées')
        if not isinstance(runtime.get('run_id'),str) or not runtime['run_id']:raise ValueError('Identifiant du test runtime absent')
        if runtime.get('medical_source_compressed') is not False:raise ValueError('Le périmètre synthétique du test doit être attesté')
        chunks=tests['chonkie'].get('chunks')
        if type(chunks) is not int or chunks<2 or tests['chonkie'].get('exact_reconstruction') is not True:raise ValueError('Découpage réel et reconstruction Chonkie non démontrés')
        cached=tests['gptcache']
        if cached.get('mode')!='exact-match' or cached.get('write_read') is not True or cached.get('distinct_key_miss') is not True:raise ValueError('Cache exact non démontré')
        compression=tests['llmlingua']
        if compression.get('model')!=MODEL or compression.get('revision')!=REVISION:raise ValueError('Modèle de compression non canonique')
        before,after=compression.get('origin_tokens'),compression.get('compressed_tokens')
        if type(before) is not int or type(after) is not int or not 0<after<before:raise ValueError('Compression réelle non démontrée')
        tested_age=age(runtime['tested_at'],now);result['runtime_age_seconds']=round(tested_age)
        if tested_age < -config['clock_skew_seconds']:raise ValueError('Test runtime situé dans le futur')
        if state=='working' and tested_age>config['runtime_max_age_seconds']:result['errors'].append('Test runtime trop ancien pour attester le travail courant.')
        required=('harnais/bracelet/bracelet_suggest.py','harnais/bracelet/catalog.json','harnais/ARSENAL.md')
        hashes=proof.get('harness_sha256')
        if not isinstance(hashes,dict):raise ValueError('Empreintes du harnais absentes')
        for path in required:
            expected=hashes.get(path)
            if trusted_hashes is not None and expected!=trusted_hashes.get(path):raise ValueError('Harnais différent de la référence exécutée sur le runner: '+path)
            if not expected or sha(api.file(path,head))!=expected:raise ValueError('Empreinte du harnais différente: '+path)
        artifacts=proof.get('artifacts')
        if not isinstance(artifacts,list) or not 1<=len(artifacts)<=8:raise ValueError('Un à huit artefacts réels sont requis')
        for item in artifacts:
            if not isinstance(item,dict):raise ValueError('Artefact non structuré')
            path=PurePosixPath(item['path'])
            if path.is_absolute() or '..' in path.parts or not path.is_relative_to(directory):raise ValueError('Artefact hors du lot')
            # Le contenu est lu uniquement pour son empreinte, jamais exécuté.
            raw=api.file(str(path),head)
            if sha(raw)!=item.get('sha256'):raise ValueError('Artefact modifié depuis le signal: '+str(path))
        result['runtime_tools']=list(TOOLS);result['ok']=not result['errors']
        result['scope']='Preuves publiées de cet agent; aucune lecture de son processus distant.'
    except (KeyError,TypeError,ValueError,OSError,urllib.error.URLError) as exc:
        result['errors'].append(type(exc).__name__+': '+str(exc)[:400])
    return result

def selector(repo):
    task='LOT O7 Appel B evidence web html document long cache'
    run=subprocess.run([sys.executable,str(repo/'harnais/bracelet/bracelet_suggest.py'),task],capture_output=True,text=True,timeout=20)
    expected=[('Chonkie','1.6'),('LLMLingua','1.3'),('GPTCache','1.3')]
    lines=run.stdout.splitlines()
    ok=run.returncode==0 and len(lines)>=3 and all(name in lines[i] and 'score='+score in lines[i] for i,(name,score) in enumerate(expected))
    return {'ok':ok,'exit_code':run.returncode,'output':lines[:3],'scope':'Sélecteur seulement; les scores ne sont pas des versions.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--config',type=Path,default=Path('harnais/surveillance/config.json'))
    p.add_argument('--output',type=Path,default=Path('/tmp/harnais-watchdog.json'));a=p.parse_args()
    config=json.loads(a.config.read_text());repo=Path.cwd();now=datetime.now(timezone.utc)
    api=GitHub(config['repository'],os.environ.get('GH_TOKEN'))
    result={'checked_at':now.isoformat(),'selector':selector(repo),
            'agents':[assess_agent(config,agent,api,now, trusted_hashes={name:sha((repo/name).read_bytes()) for name in ('harnais/bracelet/bracelet_suggest.py','harnais/bracelet/catalog.json','harnais/ARSENAL.md')}) for agent in config['agents']],
            'limitation':'GitHub vérifie des preuves publiées et les outils sur son runner; il ne voit pas directement les processus des sessions ChatGPT.'}
    result['ok']=result['selector']['ok'] and all(x['ok'] for x in result['agents'])
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
    summary=os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary,'a') as out:
            out.write('## Contrôle des harnais\n\n| Agent | État des preuves | Activité | Motifs |\n|---|---|---|---|\n')
            for agent in result['agents']:
                reasons='; '.join(agent['errors']).replace('|','/').replace('\n',' ')
                out.write('| '+agent['agent']+' | '+('Vérifié' if agent['ok'] else 'À corriger')+' | '+agent['activity']+' | '+reasons+' |\n')
            out.write('\n'+result['limitation']+'\n')
    return 0 if result['ok'] else 1
if __name__=='__main__':raise SystemExit(main())
