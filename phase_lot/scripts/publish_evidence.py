#!/usr/bin/env python3
"""Publie l'index de preuves sans recopier les documents sources complets."""
import argparse, json, re
from pathlib import Path

def compact(data):
    result={k:v for k,v in data.items() if k!='sources'}
    result['sources']=[]; budget={}
    for source in data['sources']:
        row={k:v for k,v in source.items() if k not in {'excerpts','content','raw','text'}}
        url=source.get('url',''); remaining=max(0,75-budget.get(url,0))
        excerpt=' '.join(source.get('excerpts',[])); words=excerpt.split()
        selected=words[:remaining]; budget[url]=budget.get(url,0)+len(selected)
        row['bounded_excerpt']=' '.join(selected)+(' […]' if len(words)>len(selected) else '')
        row['excerpt_is_partial']=len(words)>len(selected)
        row['notice']='Index public de preuve ; le texte primaire doit être ouvert pour audit.'
        result['sources'].append(row)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    assert a.source.resolve()!=a.output.resolve(),'Préserver les données de travail originales'
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(compact(json.loads(a.source.read_text())),ensure_ascii=False,indent=2)+'\n')
