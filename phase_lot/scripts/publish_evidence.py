#!/usr/bin/env python3
"""Publie l'index de preuves sans recopier les documents sources complets."""
import argparse, json, re
from pathlib import Path

def excerpt_text(value):
    if isinstance(value,str): return value
    if isinstance(value,list): return ' '.join(excerpt_text(item) for item in value)
    if isinstance(value,dict):
        if value.get('found') is False or value.get('read') is False:return ''
        return ' '.join(excerpt_text(value[key]) for key in ['excerpt','text','quote','passage'] if key in value)
    return ''

def compact(data,budget=None):
    # Les formats de recherche diffèrent selon l'auteur. Une liste autorisée
    # empêche qu'un champ nouveau emporte un paquet brut ou un texte intégral.
    metadata={'lot','ssp','role','phase','consulted_at','clinical_validation',
              'human_auditor','publication_authorized'}
    source_metadata={'id','key','url','title','organisation','version',
                     'publication_date','publication_date_reported',
                     'version_or_document_date','consulted_at','scope','access'}
    result={k:v for k,v in data.items() if k in metadata}
    result['sources']=[]
    if budget is None: budget={}
    for source in data['sources']+data.get('inherited_sources',[]):
        row={k:v for k,v in source.items() if k in source_metadata}
        url=source.get('url',''); remaining=max(0,75-budget.get(url,0))
        passages=source.get('excerpts',source.get('passages_read',[]))
        locators=[]
        if isinstance(passages,list):
            for item in passages:
                if isinstance(item,dict):
                    locator=next((item[k] for k in ['locator','anchor','label'] if isinstance(item.get(k),str)),None)
                    if locator and locator not in locators:locators.append(locator)
        row['passage_locators']=locators
        excerpt=excerpt_text(passages); words=excerpt.split()
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
