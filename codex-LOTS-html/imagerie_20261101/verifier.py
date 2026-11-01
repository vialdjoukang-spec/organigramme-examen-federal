import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone
from lxml import html

D = Path(__file__).resolve().parent
B = D.parent
data = json.loads((D/'INVENTAIRE.json').read_text())
doc = html.parse(str(B/'BILAN_IMAGERIE_ECG.html'))
before = json.loads((B/'LOT_018/illustrations/acquisition/LECONS_AVANT.json').read_text())
current = {str(p.relative_to(B.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in B.glob('LOT_*/*.html')}
assert current == before and len(current) == 244
assert len(data['lots']) == 116 and [x['lot'] for x in data['lots']] == list(range(18,134))
assert len(doc.xpath('//tr[@data-lot]')) == 116
assert len(doc.xpath('//details[@class="lecon"]')) == data['totaux']['lecons_avec_mentions']
assert len(doc.xpath('//blockquote')) == data['totaux']['passages']
links = 0
for row in data['lecons']:
    p = B/row['fichier']
    assert hashlib.sha256(p.read_bytes()).hexdigest() == row['sha256']
    source = html.parse(str(p))
    for passage in row['passages']:
        assert source.xpath('//*[@id=$id]',id=passage['ancre'])
        links += 1
manifeste = json.loads((B.parent/'harnais/HARNAIS_MANIFESTE.json').read_text())['fichiers']
assert all(hashlib.sha256((B.parent/p).read_bytes()).hexdigest()==sha for p,sha in manifeste.items())
result = {'date':datetime.now(timezone.utc).isoformat(timespec='seconds'), 'lecons_inchangees':244,
          'lots_sans_saut':116,'liens_extraits_verifies':links,'harnais_intacts':len(manifeste),
          'statut':'contrôles mécaniques réussis','validation_clinique':False}
(D/'CONTROLE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
