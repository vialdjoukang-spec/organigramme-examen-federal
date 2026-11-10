from pathlib import Path
import urllib.request,urllib.parse,json,hashlib,zipfile,io,xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
D=Path(__file__).resolve().parent
H={'Language':'fr','Accept-Language':'fr-CH,fr;q=0.9','X-Requested-With':'XMLHttpRequest','User-Agent':'Mozilla/5.0'}
def fetch(name):
 u='https://www.swissmedicinfo-pro.ch/api/Medication/Export?'+urllib.parse.urlencode({'Praeparatname':name,'MedizinBereich':'HAM'})
 b=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=45).read();z=zipfile.ZipFile(io.BytesIO(b));ns={'x':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
 strings=[]
 if 'xl/sharedStrings.xml'in z.namelist():
  strings=[''.join(e.itertext())for e in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('x:si',ns)]
 rows=[]
 for row in ET.fromstring(z.read('xl/worksheets/sheet1.xml')).findall('.//x:row',ns):
  d={}
  for c in row.findall('x:c',ns):
   v=c.find('x:v',ns);t=v.text if v is not None else ''.join(c.itertext());t=strings[int(t)]if c.get('t')=='s'else t;d[c.get('r')]=t
  rows.append(d)
 return name,u,b,rows
with ThreadPoolExecutor(max_workers=2)as pool:
 results=list(pool.map(fetch,['Kevzara']))
for name,u,b,rows in results:
 (D/f'AIPS_Export_{name}.xlsx').write_bytes(b)
 (D/f'AIPS_Export_{name}.json').write_text(json.dumps({'url':u,'date':'2026-11-10','headers_publics':H,'sha256_xlsx':hashlib.sha256(b).hexdigest(),'lignes':rows},ensure_ascii=False,indent=2)+'\n')
 print(name,'lignes',len(rows))
 for row in rows[1:]:
  print(' | '.join(str(v)for k,v in row.items()if k.startswith(('A','B','F'))))
