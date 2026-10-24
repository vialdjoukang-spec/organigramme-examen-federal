#!/usr/bin/env python3
"""Corrige uniquement les métadonnées de copies neuves ; préserve tout le body."""
import argparse,datetime,hashlib,html,json,re,shutil
from pathlib import Path
from progression import selected_diagnostics
from validate import Structure,check_input
from check_selfcheck import check_selfcheck

def sha(data):return hashlib.sha256(data).hexdigest()
def body(data):
    match=re.search(br'<body\b[^>]*>.*?</body\s*>',data,re.I|re.S)
    assert match,'Corps HTML introuvable'
    return match.group(0)

def main():
    p=argparse.ArgumentParser();p.add_argument('--lot',type=int,required=True)
    p.add_argument('--work',type=Path,required=True);p.add_argument('--selection',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    assert not a.output.exists(),'Préserver les copies existantes'
    selection=json.loads(a.selection.read_text());rows=selected_diagnostics(selection)
    names={x['id']:x.get('name',x.get('name_exact')) for x in rows};ssp=selection['ssp']
    control=Path(__file__).resolve().parents[1];rubric=json.loads((control/'config/rubric.json').read_text())
    a.output.mkdir(parents=True);summary=[]
    for number in range(1,6):
        role=f'B{number}';source=a.work/f'lot{a.lot:03d}-{role.lower()}';dest=a.output/source.name
        cp=json.loads((source/'checkpoint.json').read_text())
        assert cp['lot']==a.lot and cp['role']==role and cp['production_complete'] is True
        dest.mkdir();archive=dest/'internal/author_metadata';archive.mkdir(parents=True)
        for name in ['HELP.json','selfcheck.json','checkpoint.json','handoff_redaction.md','evidence.json']:
            shutil.copyfile(source/name,dest/name)
            if name!='evidence.json':shutil.copyfile(source/name,archive/name)
        records=[]
        for original in sorted(source.glob('*.html')):
            old=original.read_bytes();text=old.decode('utf-8');parsed=Structure();parsed.feed(text);parsed.close()
            assert not parsed.errors and not parsed.stack
            title=f'LOT {a.lot:03d} — PROFILES {ssp} — '+' ; '.join(names[x] for x in parsed.monographs)
            if parsed.title_count==0:
                head=re.search(r'<head\b[^>]*>',text,re.I);assert head,'head absent'
                text=text[:head.end()]+'\n<title>'+html.escape(title)+'</title>'+text[head.end():]
            else:
                assert parsed.title_count==1 and ''.join(parsed.title_text).strip(),'Titre ambigu : correction explicite requise'
            new=text.encode('utf-8');assert body(old)==body(new),'Le corps clinique doit rester identique'
            (dest/original.name).write_bytes(new)
            records.append({'file':original.name,'old_sha256':sha(old),'sha256':sha(new),'bytes':len(new),
                            'clinical_body_sha256':sha(body(new)),'clinical_body_unchanged':True})
        report=check_input(dest,rubric);assert report['structural_pass'],report['errors']
        assert check_selfcheck(dest,role,a.lot,rubric)['questions']==102
        patch={'kind':'HTML_TITLE_METADATA_ONLY','lot':a.lot,'role':role,
               'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'original_author_folder':str(source),'clinical_body_unchanged':True,'files':records,
               'semantic_validation':False,'human_approval':False,'transmitted':False}
        (dest/'technical_metadata_patch.json').write_text(json.dumps(patch,ensure_ascii=False,indent=2)+'\n')
        current={'lot':a.lot,'ssp':ssp,'role':role,'production_complete':True,
                 'production_complete_meaning':'Rédaction intégrale constatée ; métadonnées corrigées, corps clinique identique.',
                 'structural_pass':True,'semantic_validation':False,'human_approval':False,'external_transmission':False,
                 'html_files':records,'technical_metadata_patch':patch,'author_checkpoint':cp}
        (dest/'checkpoint.json').write_text(json.dumps(current,ensure_ascii=False,indent=2)+'\n')
        selfcheck=json.loads((dest/'selfcheck.json').read_text());assert isinstance(selfcheck,dict)
        selfcheck['coordinator_metadata_patch']=patch
        (dest/'selfcheck.json').write_text(json.dumps(selfcheck,ensure_ascii=False,indent=2)+'\n')
        with (dest/'handoff_redaction.md').open('a') as handle:
            handle.write('\n\n## Métadonnées HTML corrigées par le coordinateur\n\nLes titres de page manquants ont été ajoutés dans cette copie. Le body clinique est identique octet pour octet. Les empreintes de la passation d’auteur ci-dessus sont historiques ; le checkpoint courant et technical_metadata_patch.json donnent les nouvelles empreintes. Cette opération ne réalise aucun audit médical ou linguistique.\n')
        (dest/'structure_patch.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        summary.append(patch)
    (a.output/'TITRES_METADATA_PATCH.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'roles':5,'html_files':sum(len(x['files']) for x in summary),'all_clinical_bodies_identical':True,'transmitted':False}))

if __name__=='__main__':main()
