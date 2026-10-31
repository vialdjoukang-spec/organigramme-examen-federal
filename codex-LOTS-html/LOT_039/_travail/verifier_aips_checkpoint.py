"""Compare les citations finales aux paragraphes des notices fraîches archivées."""
from pathlib import Path
from lxml import html
from datetime import datetime, timezone
import json, hashlib, re
P=Path(__file__).resolve().parents[1]
def norm(s):return re.sub(r'\s+',' ',s).strip()
notices={}
for name in ('cyclogyl','aprokam','eylea2','diamox','timoptic','dexafree','atropine','solumedrol'):
 raw=(P/'evidence'/f'{name}_frais.html').read_bytes()
 paras=[]
 for e in html.fromstring(raw).xpath('//p'):
  paras.extend([norm(e.text_content()),norm(' '.join(e.itertext()))])
 notices[name]={'paragraphes':paras,'sha256_html':hashlib.sha256(raw).hexdigest()}
mapping={1:['cyclogyl'],2:['aprokam'],5:['eylea2'],6:['diamox','timoptic'],7:['dexafree','atropine'],8:['solumedrol']}
out=[]
for n,names in mapping.items():
 f=P/f'LOT_039_Phase_B_V0_DX.{n}.html';raw=f.read_bytes()
 quotes=[norm(e.text_content().strip().removeprefix('« ').removesuffix(' »')) for e in html.fromstring(raw).xpath('//blockquote/p')]
 bad=[q for q in quotes if not any(q in p for name in names for p in notices[name]['paragraphes'])]
 out.append({'fichier':f.name,'sha256':hashlib.sha256(raw).hexdigest(),'citations':len(quotes),'notices':{name:notices[name]['sha256_html'] for name in names},'non_retrouvees':bad,'ok':not bad})
report={'date':datetime.now(timezone.utc).isoformat(),'methode':'Citations finales, retrait des guillemets ajoutés, normalisation des espaces ; paragraphes officiels frais réextraits selon deux sérialisations DOM : text_content et jonction des nœuds textuels avec espace (notamment exposant mm² et frontière span). Aucun rapprochement approximatif de mots. Échec initial de deux sérialisations Aprokam conservé, sans modification de DX2.','fichiers':out,'citations_total':sum(x['citations'] for x in out),'ok':all(x['ok'] for x in out),'validation_clinique':False}
(P/'audits/aips_checkpoint_dx8.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
assert report['ok']
