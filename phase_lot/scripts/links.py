#!/usr/bin/env python3
"""Sonde bornée d'un registre explicite ; respecte les proxys et la vérification TLS."""
import argparse, concurrent.futures, datetime, json, urllib.error, urllib.parse, urllib.request
from pathlib import Path

def probe(entry):
    url=entry['url']; result=dict(entry)
    result['checked_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    result['content_read_by_agent']=False
    if urllib.parse.urlparse(url).scheme != 'https':
        return dict(result,status=None,error='HTTPS requis')
    for method in ['HEAD','GET']:
        try:
            req=urllib.request.Request(url,method=method,headers={'User-Agent':'PhaseLOT-LinkCheck/1.0','Range':'bytes=0-1023'})
            with urllib.request.urlopen(req,timeout=15) as r:
                result.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'))
            return result
        except urllib.error.HTTPError as e:
            if method=='HEAD' and e.code in (405,501): continue
            return dict(result,status=e.code,error=str(e))
        except (OSError,ValueError) as e:
            return dict(result,status=None,error=str(e))
    return result

def main():
    p=argparse.ArgumentParser(); p.add_argument('registry',type=Path); p.add_argument('--output',type=Path,required=True)
    p.add_argument('--limit',type=int); a=p.parse_args(); entries=json.loads(a.registry.read_text())
    if a.limit: entries=entries[:a.limit]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(probe,entries))
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(results,ensure_ascii=False,indent=2))
    print(json.dumps({'checked':len(results),'http_2xx':sum(200<=(r.get('status') or 0)<300 for r in results),'clinical_validation':False}))

if __name__=='__main__': main()
