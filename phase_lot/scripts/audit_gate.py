#!/usr/bin/env python3
"""Prépare un final seulement après audit externe identifié et lié aux octets."""
import argparse, hashlib, json, shutil, subprocess
from pathlib import Path
from validate import check

ROOT=Path(__file__).resolve().parents[1]

def verify(bundle, report, policy, commit):
    login=policy.get('tunder_github_login')
    for rel in report.get('files',{}):
        assert not Path(rel).is_absolute() and '..' not in Path(rel).parts, 'Chemin hors périmètre' 
    assert login, 'Identifiant GitHub de Tunder non configuré'
    assert (commit.get('author') or {}).get('login')==login, 'Auteur du commit non relié à Tunder par GitHub'
    assert commit.get('commit',{}).get('verification',{}).get('verified') is True, 'Signature du commit non vérifiée par GitHub'
    assert report['auditor_login']==login and report['decision']=='ACCEPTE'
    assert report['medical_review'] is True and report['linguistic_review'] is True
    assert type(report['critical_errors']) is int and report['critical_errors']==0
    assert report['candidate_commit'] and len(report['candidate_commit'])==40
    rubric=json.loads((ROOT/'config/rubric.json').read_text())
    questions={q['id'] for p in rubric['points'] for q in p['questions']}
    files=sorted(bundle.rglob('*.html')); expected={str(p.relative_to(bundle)) for p in files}
    assert files and expected==set(report['files']), 'Périmètre du rapport différent des HTML candidats'
    selection=json.loads((bundle/'A/selection.json').read_text())
    assert selection['complete'] is True
    assert [d['id'] for d in selection['diagnostics']]==[f'DX.{i}' for i in range(1,11)]
    all_monographs=[]
    for p in files:
        rel=str(p.relative_to(bundle)); entry=report['files'][rel]
        assert hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'],f'Empreinte périmée {rel}'
        structure=check(p,rubric); assert structure['structural_pass'],f'Structure non conforme {rel}'
        assert entry.get('final_question_6_2')=='OUI' and entry.get('section_16_complete') is True, 'Contrôle final V7 incomplet'
        assert set(entry['monographs'])==set(structure['monographs']),f'Monographies manquantes {rel}'
        all_monographs.extend(structure['monographs'])
        for mono, answers in entry['monographs'].items():
            assert set(answers)==questions, f'Questions manquantes {rel}/{mono}'
            for key,value in answers.items():
                assert value.get('evidence'), f'Preuve absente {key}'
                assert value['score']==2 or (value['score']=='NA' and value.get('justification')),f'Question non satisfaite {key}'
    required={f'G{int(report["lot"])}'} | {f'DX.{i}' for i in range(1,11)}
    assert len(all_monographs)==11 and set(all_monographs)==required, 'SSP ou diagnostics manquants/dupliqués'
    return files

def main():
    p=argparse.ArgumentParser(); p.add_argument('bundle',type=Path); p.add_argument('report',help='chemin du rapport dans le commit audit')
    p.add_argument('--audit-commit',required=True); p.add_argument('--destination',type=Path,required=True)
    a=p.parse_args(); policy=json.loads((ROOT/'config/policy.json').read_text()); repo=policy['repository']
    commit=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/commits/{a.audit_commit}']))
    # Lire le rapport du commit attribué, jamais une copie locale auto-déclarée.
    subprocess.run(['git','fetch','origin',a.audit_commit],check=True,stdout=subprocess.DEVNULL)
    report=json.loads(subprocess.check_output(['git','show',f'{a.audit_commit}:{a.report}']))
    subprocess.run(['git','fetch','origin',report['candidate_commit']],check=True,stdout=subprocess.DEVNULL)
    prefix=policy['candidate_prefix'].format(lot=int(report['lot']))
    # Les HTML locaux doivent égaler ceux du commit candidat déclaré.
    candidate_paths=subprocess.check_output(['git','ls-tree','-r','--name-only',report['candidate_commit'],'--',prefix],text=True).splitlines()
    candidate_html={str(Path(x).relative_to(prefix)) for x in candidate_paths if x.endswith('.html')}
    assert candidate_html==set(report['files']), 'Rapport ne couvrant pas le commit candidat exact'
    for rel in report['files']:
        data=subprocess.check_output(['git','show',f"{report['candidate_commit']}:{prefix}/{rel}"])
        assert hashlib.sha256(data).hexdigest()==report['files'][rel]['sha256'], 'Empreinte différente du commit candidat'
    files=verify(a.bundle,report,policy,commit)
    assert not a.destination.exists(), 'Destination existante : refus de remplacer'
    # Préparer en répertoire neuf ; aucun push ou effacement automatique.
    a.destination.mkdir(parents=True)
    for source in files:
        target=a.destination/source.relative_to(a.bundle); target.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(source,target)
    (a.destination/'AUDIT_TUNDER.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'prepared':str(a.destination),'files':len(files),'pushed':False}))

if __name__=='__main__': main()
