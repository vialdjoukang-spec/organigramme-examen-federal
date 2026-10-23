#!/usr/bin/env python3
"""Coordinateur unique, sans transition implicite ni auto-validation médicale."""
import argparse, hashlib, json
from pathlib import Path
from validate import Structure

ROOT=Path(__file__).resolve().parents[1]

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
        assert selection['complete'] is True and len(selection['diagnostics'])==10
        assert [d['id'] for d in selection['diagnostics']]==[f'DX.{i}' for i in range(1,11)]
        assert len({d['name'].casefold() for d in selection['diagnostics']})==10, 'diagnostics dupliqués'
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
        row.update(production_status='PRODUIT',audit_status='EN_ATTENTE_TUNDER',files=manifest(a.bundle))
        if n<10: q['lots'][n]['production_status']='ACTIF'
        validate(q)
        assert a.file.read_bytes()==raw, 'file modifiée depuis la lecture'
        tmp=a.file.with_suffix('.tmp'); tmp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n'); tmp.replace(a.file)
    print(json.dumps({'active':[r['lot'] for r in q['lots'] if r['production_status']=='ACTIF'], 'produced':[r['lot'] for r in q['lots'] if r['production_status']=='PRODUIT'],'audited':[r['lot'] for r in q['lots'] if r['audit_status']=='FINAL_AUDITE']},ensure_ascii=False))

if __name__=='__main__': main()
