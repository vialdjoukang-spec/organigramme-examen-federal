#!/usr/bin/env python3
"""Bail du coordinateur sur une branche d'état séparée, écriture CAS GitHub."""
import argparse, base64, datetime, json, subprocess

REPO='vialdjoukang-spec/organigramme-examen-federal'
BRANCH='lot-pilotage/etat'
PATH='phase_lot_lease.json'

def utc(): return datetime.datetime.now(datetime.timezone.utc)

def allowed(lease, owner, now):
    return not lease or lease.get('owner')==owner or datetime.datetime.fromisoformat(lease['expires_at'])<=now

def main():
    p=argparse.ArgumentParser();p.add_argument('--owner',required=True);p.add_argument('--seconds',type=int,default=600)
    p.add_argument('--release',action='store_true');a=p.parse_args(); assert 60<=a.seconds<=900
    endpoint=f'repos/{REPO}/contents/{PATH}'
    read=subprocess.run(['gh','api',endpoint+'?ref='+BRANCH],capture_output=True,text=True)
    if read.returncode:
        assert '404' in read.stderr,read.stderr
        old=None;sha=None
    else:
        obj=json.loads(read.stdout);sha=obj['sha'];old=json.loads(base64.b64decode(obj['content']))
    now=utc()
    if a.release:
        assert old and old.get('owner')==a.owner,'Un autre coordinateur possède le bail'
        new={'owner':None,'expires_at':now.isoformat(),'released_at':now.isoformat()}
    else:
        assert allowed(old,a.owner,now),f"Bail actif détenu par {old.get('owner')} jusqu'à {old.get('expires_at')}"
        new={'owner':a.owner,'expires_at':(now+datetime.timedelta(seconds=a.seconds)).isoformat(),'renewed_at':now.isoformat(),'purpose':'travail réel du coordinateur Phase LOT'}
    body={'branch':BRANCH,'message':'Phase LOT : bail du coordinateur actif','content':base64.b64encode((json.dumps(new)+'\n').encode()).decode()}
    if sha:body['sha']=sha
    # Un rival qui écrit après notre lecture fait échouer ce PUT (409/422), sans retry aveugle.
    result=subprocess.run(['gh','api','--method','PUT',endpoint,'--input','-'],input=json.dumps(body),capture_output=True,text=True)
    assert result.returncode==0,result.stderr
    print(json.dumps(new,ensure_ascii=False))

if __name__=='__main__': main()
