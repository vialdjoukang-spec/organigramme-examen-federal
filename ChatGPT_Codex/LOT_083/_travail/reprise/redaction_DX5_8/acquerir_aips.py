from pathlib import Path
import urllib.request,json,concurrent.futures,re,html,hashlib
B=Path(__file__).parent;H={'X-Requested-With':'XMLHttpRequest','Language':'fr','Accept-Language':'fr-CH,fr;q=0.9'}
def run(item):
 name,pack=item;u=f'https://www.swissmedicinfo-pro.ch/api/Medication/{pack}/GetDokumentSectionItems';data=urllib.request.urlopen(urllib.request.Request(u,headers=H)).read();x=json.loads(data);(B/f'AIPS_{name}_officielle.json').write_bytes(data);out={'url_api':u,'dokumentStorageUrl':x.get('dokumentStorageUrl'),'date':'2026-11-10','sha256_json_primaire':hashlib.sha256(data).hexdigest(),'sections':[]}
 for s in x['sections']:
  t=re.sub(r'<(?:style|script)\b[^>]*>.*?</(?:style|script)>','',s['content'],flags=re.S|re.I);t=re.sub(r'</(?:p|div|tr|li|h[1-6])>','\n',t);t=html.unescape(re.sub('<[^>]+>',' ',t));t=re.sub('[ \t]+',' ',t);out['sections'].append({'titre':s['heading'],'texte':t.strip()})
 (B/f'AIPS_{name}_texte.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));return name,[(i,s['titre'],len(s['texte'])) for i,s in enumerate(out['sections'])]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(run,[('tamiflu','55196001'),('xofluza','67426001'),('prednisone_galepharm','69640003')]):print(json.dumps(r,ensure_ascii=False))
