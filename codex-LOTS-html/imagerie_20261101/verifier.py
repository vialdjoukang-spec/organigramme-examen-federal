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
# Nouvelle campagne clinique : témoin du checkpoint précédent conservé,
# six fichiers autorisés et préservation des figures antérieures contrôlés.
import subprocess
campaign=B/'renforcement_medical_20261101'
subprocess.run(['python3','-B',str(campaign/'verifier.py')],check=True)
expected=json.loads((campaign/'BASELINE.json').read_text())['lecons']
transitions=json.loads((campaign/'CONTROLE.json').read_text())['lecons']
for change in transitions:
    key='codex-LOTS-html/'+change['fichier']
    assert expected[key]==change['sha256_avant']
    expected[key]=change['sha256_apres']
assert current == expected and len(current) == 244
assert len(data['lots']) == 116 and [x['lot'] for x in data['lots']] == list(range(18,134))
assert len(doc.xpath('//tr[@data-lot]')) == 116
assert len(doc.xpath('//details[@class="lecon"]')) == data['totaux']['lecons_avec_mentions']
assert len(doc.xpath('//blockquote')) == data['totaux']['passages']
triage = json.loads((D/'TRIAGE.json').read_text())
assert len(triage['lecons']) == triage['lecons_triees'] == len(doc.xpath('//*[@data-triage="effectue"]'))
assert sum(len(x['passages_lus']) for x in triage['lecons']) == triage['passages_lus']
assert len({x['fichier'] for x in triage['lecons']}) == triage['lecons_triees']
assert triage['reste_lecons_avec_mentions'] == data['totaux']['lecons_avec_mentions'] - sum(bool(x['passages_lus']) for x in triage['lecons'])
for revue in triage['lecons']:
    row = next(x for x in data['lecons'] if x['fichier']==revue['fichier'])
    assert revue['sha256_lecon']==row['sha256']
    assert [x['sha256_texte'] for x in revue['passages_lus']] == [hashlib.sha256(x['extrait_exact_normalise'].encode()).hexdigest() for x in row['passages']]
    if 'extrait_supplementaire_lu' in revue:
        extra = revue['extrait_supplementaire_lu']
        source = html.fromstring((B/revue['fichier']).read_bytes()).get_element_by_id(extra['ancre'])
        assert extra['texte_normalise'] == ' '.join(' '.join(source.itertext()).split())
for acquisition in json.loads((D/'sources_orl/ACCES.json').read_text()):
    if acquisition.get('contenu_conserve') is False:
        assert acquisition['fichier']=='PMC11150114.xml'
        assert not (D/'sources_orl'/acquisition['fichier']).exists()
        assert json.loads((D/'sources_orl/REFUS_NC.json').read_text())['decision']=='exclu_NC'
    else:
        raw=(D/'sources_orl'/acquisition['fichier']).read_bytes()
        assert len(raw)==acquisition['octets'] and hashlib.sha256(raw).hexdigest()==acquisition['sha256']
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
result = {'date':datetime.now(timezone.utc).isoformat(timespec='seconds'), 'lecons_inchangees':238, 'lecons_renforcees':6, 'lecons_avec_nouvelle_image_reelle':2,
          'lots_sans_saut':116,'liens_extraits_verifies':links,'harnais_intacts':len(manifeste),
          'lecons_triees':triage['lecons_triees'],'passages_tries':triage['passages_lus'],'acquisitions_documentaires_sources_orl':5,
          'statut':'contrôles mécaniques réussis','validation_clinique':False}
(D/'CONTROLE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
