"""Corrige les lignes de sérialisation sans modifier le texte médical."""
from pathlib import Path
from lxml import html, etree
import re, json, hashlib

d=Path(__file__).resolve().parents[1]
preuves=[]
for n in (6,7):
    p=d/f'LOT_037_Phase_B_V0_DX.{n}.html'
    avant=p.read_text()
    apres=re.sub(r'(</(?:p|blockquote|table|div)>)(?=<)',r'\1\n',avant)
    a=html.fromstring(avant);b=html.fromstring(apres)
    for expr in ('//blockquote/p','//section[contains(@class,"ilot")]/h2','//details[@class="quiz"]'):
        assert [re.sub(r'\s+',' ',x.text_content()).strip() for x in a.xpath(expr)]==[re.sub(r'\s+',' ',x.text_content()).strip() for x in b.xpath(expr)]
    for tree in (a,b):
        for x in tree.iter():
            if x.text is not None and not x.text.strip():x.text=None
            if x.tail is not None and not x.tail.strip():x.tail=None
    assert etree.tostring(a)==etree.tostring(b)
    preuves.append({'fichier':p.name,'sha256_avant':hashlib.sha256(avant.encode()).hexdigest(),'sha256_apres':hashlib.sha256(apres.encode()).hexdigest(),'dom_hors_espaces_interbalises_identique':True,'citations_titres_questions_identiques':True,'lignes_plus_3000_avant':sum(len(x)>3000 for x in avant.splitlines()),'lignes_plus_3000_apres':sum(len(x)>3000 for x in apres.splitlines())})
    p.write_text(apres)
(d/'audits/serialisation_c23.json').write_text(json.dumps(preuves,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(preuves,ensure_ascii=False))
