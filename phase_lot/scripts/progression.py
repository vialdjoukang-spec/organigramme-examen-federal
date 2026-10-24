#!/usr/bin/env python3
"""Coordinateur unique, sans transition implicite ni auto-validation médicale."""
import argparse, hashlib, json
from pathlib import Path
from validate import Structure

ROOT=Path(__file__).resolve().parents[1]

def selected_diagnostics(selection):
    assert selection.get('complete') is True,'Sélection incomplète'
    if 'diagnostics' in selection and 'diagnoses' in selection:
        assert selection['diagnostics']==selection['diagnoses'],'Listes diagnostiques contradictoires'
    rows=selection.get('diagnostics',selection.get('diagnoses'))
    assert isinstance(rows,list) and len(rows)==10 and all(isinstance(x,dict) for x in rows),'Dix diagnostics requis'
    assert [x.get('id') for x in rows]==[f'DX.{i}' for i in range(1,11)],'Identifiants ou ordre incohérents'
    names=[x.get('name',x.get('name_exact')) for x in rows]
    assert all(isinstance(x,str) and x.strip() for x in names),'Nom diagnostique absent'
    assert len({x.casefold() for x in names})==10,'Diagnostics dupliqués'
    return rows

def validate(q):
    assert [r['lot'] for r in q['lots']]==list(range(1,11)), 'file 1..10 requise'
    active=[r for r in q['lots'] if r['production_status']=='ACTIF']
    assert len(active)<=1, 'plusieurs LOTS actifs interdits'
    valid={'EN_ATTENTE','ACTIF','PRODUIT'}
    assert all(r['production_status'] in valid for r in q['lots'])
    if active:
        n=active[0]['lot']; assert all(r['production_status']=='PRODUIT' for r in q['lots'][:n-1]),'ordre de production rompu'

def manifest(root):
    files=sorted(root.rglob('*.html'))
    return {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--file',type=Path,default=ROOT/'config/file.json')
    p.add_argument('--complete',type=int); p.add_argument('--bundle',type=Path); a=p.parse_args()
    raw=a.file.read_bytes(); q=json.loads(raw); validate(q)
    if a.complete:
        assert a.bundle and a.bundle.is_dir(),'bundle requis'
        n=a.complete; row=q['lots'][n-1]; assert row['production_status']=='ACTIF'
        selection=json.loads((a.bundle/'A/selection.json').read_text())
        selected_diagnostics(selection)
        for role in ['A','B1','B2','B3','B4','B5']:
            cp=json.loads((a.bundle/role/'checkpoint.json').read_text())
            assert cp['production_complete'] is True and cp['role']==role
            assert list((a.bundle/role).glob('*.html')), f'HTML absent {role}'
            found=[]
            for html in (a.bundle/role).glob('*.html'):
                parsed=Structure(); parsed.feed(html.read_text()); parsed.close()
                assert not parsed.errors and not parsed.stack,f'HTML incomplet {html}'
                for ident,mono in parsed.monographs.items():
                    assert mono['points']==list(map(str,range(1,15))),f'14 points incomplets {ident}'
                    found.append(ident)
            wanted=[f'G{n}'] if role=='A' else [f'DX.{2*int(role[1])-1}',f'DX.{2*int(role[1])}']
            assert sorted(found)==sorted(wanted),f'Diagnostics hors réservation ou manquants {role}'
        row.update(production_status='PRODUIT',audit_status='NON_SOUMIS',files=manifest(a.bundle),
                   stage='CANDIDAT_LOCAL_ATTENTE_AUTORISATION_TRANSMISSION',
                   production_complete_locally=True,clinical_transmission_authorized=False)
        if n<10: q['lots'][n]['production_status']='ACTIF'
        validate(q)
        assert a.file.read_bytes()==raw, 'file modifiée depuis la lecture'
        tmp=a.file.with_suffix('.tmp'); tmp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n'); tmp.replace(a.file)
    print(json.dumps({'active':[r['lot'] for r in q['lots'] if r['production_status']=='ACTIF'], 'produced':[r['lot'] for r in q['lots'] if r['production_status']=='PRODUIT'],'audited':[r['lot'] for r in q['lots'] if r['audit_status']=='FINAL_AUDITE']},ensure_ascii=False))

if __name__=='__main__': main()
