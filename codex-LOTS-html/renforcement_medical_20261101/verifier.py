"""Contrôles mécaniques de la première tranche de renforcement ; aucun score médical."""
import hashlib
import importlib.util
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from lxml import html

D=Path(__file__).resolve().parent
B=D.parent
R=B.parent
TARGETS={f'codex-LOTS-html/LOT_{n:03}/LOT_{n:03}_{suffix}.html' for n in [18,29] for suffix in ['Phase_A_V0','Phase_B_V0_DX.1','Phase_B_V0_DX.2']}
def sha(raw):return hashlib.sha256(raw).hexdigest()
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def windows(doc):
    result=[]
    for section in doc.xpath('//section[h2[contains(@id,"-p")]]'):
        h=section.find('h2');targets=section.xpath('.//button[not(@popovertargetaction="hide")]/@popovertarget')
        words=sum(len(doc.get_element_by_id(t).text_content().split()) for t in targets)
        result.append({'partie':int(h.get('id').split('-p')[-1]),'cibles':targets,'mots_directs_indicatifs':words})
    return result
def main():
    base=json.loads((D/'BASELINE.json').read_text());before=base['lecons']
    current={str(p.relative_to(R)):sha(p.read_bytes()) for p in B.glob('LOT_*/*.html')}
    changed={k for k in before if current.get(k)!=before[k]}
    assert set(current)==set(before) and changed==TARGETS, sorted(changed)
    v8=module('controle_v8',B/'outils/verifier_lot_generique_v8.py')
    reports={n:v8.verifier(B/f'LOT_{n:03}') for n in [18,29]}
    for n,report in reports.items():
        (D/f'V8_{n}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        assert report['statique_ok'], [(f['fichier'],[c for c in f['controles'] if not c['ok']]) for f in report['fichiers'] if not f['statique_ok']]
    rows=[]
    for name in sorted(changed):
        raw_before=subprocess.check_output(['git','show',base['commit']+':'+name],cwd=R)
        raw_after=(R/name).read_bytes();a=html.fromstring(raw_before);b=html.fromstring(raw_after)
        ids_before=set(a.xpath('//*[@id]/@id'));ids_after=set(b.xpath('//*[@id]/@id'))
        assert ids_before<=ids_after, sorted(ids_before-ids_after)
        figures_a=a.xpath('//*[@data-illustration]');figures_b={e.get('data-illustration'):e for e in b.xpath('//*[@data-illustration]')}
        for fig in figures_a:
            assert html.tostring(fig,with_tail=False)==html.tostring(figures_b[fig.get('data-illustration')],with_tail=False), fig.get('data-illustration')
        wa,wb=windows(a),windows(b)
        assert len(wb)==14 and all(w['cibles'] for w in wb)
        for i in range(14):
            assert wa[i]['partie']==wb[i]['partie']==i+1
        report=next(f for f in reports[int(Path(name).parent.name[4:])]['fichiers'] if f['fichier']==Path(name).name)
        rows.append({'fichier':name.removeprefix('codex-LOTS-html/'),'sha256_avant':sha(raw_before),'sha256_apres':sha(raw_after),'octets_avant':len(raw_before),'octets_apres':len(raw_after),'texte_fiche_octets':report['texte_fiche_octets'],'texte_fenetres_octets':report['texte_fenetres_octets'],'figures_anterieures_preservees':len(figures_a),'identifiants_anterieurs_preserves':True,'fenetres_avant':wa,'fenetres_apres':wb})
    shared=json.loads((R/'harnais/HARNAIS_MANIFESTE.json').read_text())['fichiers']
    assert all(sha((R/p).read_bytes())==h for p,h in shared.items())
    out={'date':datetime.now(timezone.utc).isoformat(timespec='seconds'),'base':base['commit'],'lecons':rows,'lecons_non_modifiees':len(current)-len(changed),'harnais_intacts':len(shared),'conditions_v8_reussies':sum(len(f['controles']) for rep in reports.values() for f in rep['fichiers']),'portee':'Structure, conservation et tailles. Le nombre de mots est descriptif et ne constitue pas un score de qualité médicale.','audit_medical_independant':False,'validation_clinique_humaine':False}
    (D/'CONTROLE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='lecons'},ensure_ascii=False))
if __name__=='__main__':main()
