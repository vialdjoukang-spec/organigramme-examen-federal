#!/usr/bin/env python3
"""Vérifie la traçabilité des questions du V7, jamais leur réponse médicale."""
import json,re
from pathlib import Path

def check_selfcheck(folder,role,lot,rubric):
    expected={q['id']:q['text'] for p in rubric['points'] for q in p['questions']}
    wanted=[f'G{lot}'] if role=='A' else [f'DX.{2*int(role[1])-1}',f'DX.{2*int(role[1])}']
    found={key:{} for key in wanted}
    data=json.loads((Path(folder)/'selfcheck.json').read_text())
    def visit(value,context=None):
        if isinstance(value,list):
            for child in value:visit(child,context)
        elif isinstance(value,dict):
            context=next((value[k] for k in ['dx','diagnosis','diagnostic','monograph'] if isinstance(value.get(k),str)),context)
            ident=next((value[k] for k in ['question_id','id','question'] if isinstance(value.get(k),str) and re.search(r'(?:^|\.)(P\d{2}\.Q\d{2})$',value[k])),None)
            if ident:
                qid=re.search(r'(P\d{2}\.Q\d{2})$',ident).group(1)
                if context is None and ident.startswith('DX.'):
                    context='.'.join(ident.split('.')[:2])
                assert context in found,f'Monographie de grille hors attribution : {context}'
                assert qid in expected,f'Question inconnue : {qid}'
                assert qid not in found[context],f'Question dupliquée : {context}/{qid}'
                text=next((value[k] for k in ['question_exacte','question_text','question'] if isinstance(value.get(k),str) and value[k]==expected[qid]),None)
                assert text is not None,f'Libellé V7 différent ou absent : {context}/{qid}'
                found[context][qid]=True
            for child in value.values():
                if isinstance(child,(dict,list)):visit(child,context)
    visit(data,f'G{lot}' if role=='A' else None)
    for mono,questions in found.items():
        assert set(questions)==set(expected),f'Questions manquantes : {mono} : {sorted(set(expected)-set(questions))}'
    return {'questions':sum(map(len,found.values())),'monographs':{k:len(v) for k,v in found.items()},'semantic_validation':False}

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('folder',type=Path);p.add_argument('--role',required=True);p.add_argument('--lot',type=int,required=True);a=p.parse_args()
    root=Path(__file__).resolve().parents[1]
    print(json.dumps(check_selfcheck(a.folder,a.role,a.lot,json.loads((root/'config/rubric.json').read_text()))))
