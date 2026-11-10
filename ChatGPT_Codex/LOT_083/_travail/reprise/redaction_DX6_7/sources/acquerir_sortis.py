from pathlib import Path
import urllib.request,json,hashlib,re,html
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
D=Path(__file__).resolve().parent
H={'Language':'fr','Accept-Language':'fr-CH,fr;q=0.9','X-Requested-With':'XMLHttpRequest','User-Agent':'Mozilla/5.0'}
class Text(HTMLParser):
 def __init__(self):super().__init__();self.o=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['style','script']:self.skip+=1
  if t in ['p','tr','li','h1','h2','h3','h4']:self.o.append('\n')
 def handle_endtag(self,t):
  if t in ['style','script']:self.skip-=1
  if t in ['p','tr','li','h1','h2','h3','h4']:self.o.append('\n')
  if t in ['td','th']:self.o.append(' | ')
 def handle_data(self,t):
  if not self.skip:self.o.append(t)
def fetch(arg):
 name,pack=arg;u=f'https://www.swissmedicinfo-pro.ch/api/Medication/{pack}/GetDokumentSectionItems'
 b=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=45).read();j=json.loads(b);secs=[]
 for x in j['sections']:
  t=Text();t.feed(x['content']);s=re.sub(r'[ \t]+',' ',''.join(t.o));s=re.sub(r'\n\s*\n','\n',s).strip();secs.append({'titre':x['heading'],'texte':s})
 return name,b,{'url_api':u,'date':'2026-11-10','headers_publics':H,'dokumentStorageUrl':j.get('dokumentStorageUrl'),'sha256_json_officiel':hashlib.sha256(b).hexdigest(),'sections':secs}
name,b,j=fetch(('sortis','54085028'))
(D/'aips_sortis_sections_officielles.json').write_bytes(b)
(D/'aips_sortis_sections_lues.json').write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(j['dokumentStorageUrl'])
