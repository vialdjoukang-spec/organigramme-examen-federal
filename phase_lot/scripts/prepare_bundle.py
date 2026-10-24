#!/usr/bin/env python3
"""Assemble un candidat LOCAL complet ; n'envoie rien et n'attribue aucun audit."""
import argparse, datetime, hashlib, json, shutil
from pathlib import Path
from validate import check_input
from publish_evidence import compact
from check_selfcheck import check_selfcheck
from progression import selected_diagnostics

ROOT=Path(__file__).resolve().parents[1]

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser();p.add_argument('--lot',type=int,required=True)
    p.add_argument('--work',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--role-folder',action='append',default=[],metavar='ROLE=CHEMIN',help='Dossier actif d’une reprise isolée, sans écraser le travail précédent')
    a=p.parse_args();overrides={}
    for value in a.role_folder:
        role,folder=value.split('=',1)
        assert role in {'A','B1','B2','B3','B4','B5'} and role not in overrides,'Rôle inconnu ou dossier déclaré deux fois'
        overrides[role]=Path(folder)
    assert not a.output.exists(),'Destination existante : préserver le candidat précédent'
    rubric=json.loads((ROOT/'config/rubric.json').read_text())
    entries=[];all_monographs=[];sources={};question_count=0
    for role in ['A','B1','B2','B3','B4','B5']:
        folder=overrides.get(role,a.work/f'lot{a.lot:03d}-{role.casefold()}')
        checkpoint=json.loads((folder/'checkpoint.json').read_text())
        assert checkpoint['lot']==a.lot and checkpoint['role']==role and checkpoint['production_complete'] is True,f'Lot, rôle ou fin rédactionnelle incorrects : {role}'
        for name in ['HELP.json','selfcheck.json','handoff_redaction.md','evidence.json']:
            assert (folder/name).is_file(),f'Pièce de relecture absente : {role}/{name}'
        question_count+=check_selfcheck(folder,role,a.lot,rubric)['questions']
        report=check_input(folder,rubric)
        assert report['structural_pass'],f'Écarts structurels : {role} : {report["errors"]}'
        sources[role]=folder
        role_monographs=[]
        for file_report in report['files']:
            source=Path(file_report['file']);ids=list(file_report['monographs'])
            all_monographs.extend(ids)
            role_monographs.extend(ids)
            entries.append({'path':f'{role}/{source.name}','role':role,'source':str(source),
                            'bytes':source.stat().st_size,'sha256':digest(source),'monographs':ids})
        wanted=[f'G{a.lot}'] if role=='A' else [f'DX.{2*int(role[1])-1}',f'DX.{2*int(role[1])}']
        assert sorted(role_monographs)==sorted(wanted),f'Diagnostics hors attribution : {role}'
    required={f'G{a.lot}'}|{f'DX.{i}' for i in range(1,11)}
    assert len(all_monographs)==11 and set(all_monographs)==required,'Monographies absentes ou dupliquées'
    selection=json.loads((sources['A']/'selection.json').read_text())
    selected_diagnostics(selection)
    manifest={'lot':a.lot,'ssp':f'G{a.lot}','status':'CANDIDAT_LOCAL_NON_AUDITE',
              'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'human_auditor':'Thunder — utilisateur humain','transmission_authorized':False,
              'medical_validation':False,'linguistic_acceptance':False,'structural_checks_passed':True,
              'rubric_questions_traced':question_count,
              'monographs':len(all_monographs),'files':[{k:v for k,v in x.items() if k!='source'} for x in entries]}
    canonical=json.dumps(manifest['files'],sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()
    manifest['html_manifest_sha256']=hashlib.sha256(canonical).hexdigest()
    a.output.mkdir(parents=True)
    for entry in entries:
        dest=a.output/entry['path'];dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(entry['source'],dest);assert digest(dest)==entry['sha256']
    excerpt_budget={}
    for role,folder in sources.items():
        for name in ['HELP.json','selfcheck.json','checkpoint.json','handoff_redaction.md','technical_metadata_patch.json']:
            source=folder/name
            if source.exists():shutil.copyfile(source,a.output/role/name)
        index=compact(json.loads((folder/'evidence.json').read_text()),budget=excerpt_budget)
        (a.output/role/'sources_index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
    shutil.copyfile(sources['A']/'selection.json',a.output/'A/selection.json')
    (a.output/'MANIFESTE_RELECTURE.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    (a.output/'README.md').write_text('# LOT candidat pour relecture humaine\n\nCe paquet local contient le SSP et dix diagnostics. Les contrôles automatiques portent sur la structure ; ils ne valent pas audit médical ou linguistique. Les questions HELP et les réserves de chaque rédacteur restent à examiner par Thunder. Aucune autorisation de transmission ni acceptation clinique n’est présumée.\n')
    print(json.dumps({'output':str(a.output),'html_files':len(entries),'monographs':11,
                      'html_manifest_sha256':manifest['html_manifest_sha256'],'transmitted':False},ensure_ascii=False))

if __name__=='__main__': main()
