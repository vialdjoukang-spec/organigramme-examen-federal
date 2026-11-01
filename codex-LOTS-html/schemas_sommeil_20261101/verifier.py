"""Contrôles des deux ajouts autorisés ; conserve les empreintes historiques."""
import gzip
import hashlib
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from lxml import html

D=Path(__file__).resolve().parent
B=D.parent
R=B.parent
sys.path.insert(0,str(R/'harnais'))
import audit_langue
from produire import charger
v8=charger('v8_sommeil',B/'outils/verifier_lot_generique_v8.py')
def sha(b):return hashlib.sha256(b).hexdigest()
def normal(t):return re.sub(r'\s+',' ',t).strip()
def verifier():
    mod=json.loads((D/'MODIFICATIONS.json').read_text())
    assert {x['fichier'] for x in mod}=={f'LOT_{n:03}/LOT_{n:03}_Phase_B_V0_DX.1.html' for n in [34,40]}
    before=json.loads((B/'LOT_018/illustrations/acquisition/LECONS_AVANT.json').read_text())
    expected=dict(before)
    for row in mod:
        p=B/row['fichier']; old=gzip.decompress((D/(p.name+'.avant.gz')).read_bytes());new=p.read_bytes()
        assert sha(old)==row['sha256_avant']==before[str(p.relative_to(R))]
        assert sha(new)==row['sha256_apres']
        expected[str(p.relative_to(R))]=sha(new)
        a=html.fromstring(old);b=html.fromstring(new)
        for doc in [a,b]:
            doc.get_element_by_id('taille').text='TAILLE MESURÉE SÉPARÉMENT'
        b.get_element_by_id('sommeil-signaux-fenetre').drop_tree()
        b.xpath('//button[@popovertarget="sommeil-signaux-fenetre"]')[0].drop_tag()
        assert normal(html.tostring(a,encoding='unicode'))==normal(html.tostring(b,encoding='unicode')), 'Modification hors ajout prévu'
        for label,src in [('avant',old.decode()),('apres',new.decode())]:
            r=audit_langue.audit(p,src=src)
            (D/f'LANGUE_{int(p.parent.name[4:])}_{label}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    current={str(p.relative_to(R)):sha(p.read_bytes()) for p in B.glob('LOT_*/*.html')}
    assert len(current)==244 and current==expected
    total=0
    for n in [34,40]:
        r=v8.verifier(B/f'LOT_{n:03}')
        (D/f'V8_{n}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
        assert all(f['statique_ok'] for f in r['fichiers'])
        total+=sum(len(f['controles']) for f in r['fichiers'])
    shared=json.loads((R/'harnais/HARNAIS_MANIFESTE.json').read_text())['fichiers']
    assert all(sha((R/p).read_bytes())==h for p,h in shared.items())
    result={'date':datetime.now(timezone.utc).isoformat(timespec='seconds'),'lecons_controlees':244,'lecons_inchangees':242,'lecons_illustrees_modifiees':2,'textes_anterieurs_preserves':True,'fichiers_harnais_intacts':len(shared),'v8_conditions_positives':total,'lot040_incomplet':True,'audit_langue_historique_conforme':False,'validation_clinique':False,'audit_independant':False}
    (D/'CONTROLE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    return result

if __name__=='__main__':print(json.dumps(verifier(),ensure_ascii=False))
