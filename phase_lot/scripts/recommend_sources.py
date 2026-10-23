#!/usr/bin/env python3
"""Réutilise les ouvertures documentées ; n'invente aucun accès HTTP réussi."""
import argparse, json, re
from pathlib import Path
from urllib.parse import urlparse

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('evidence',type=Path);p.add_argument('--query',default='');a=p.parse_args()
    terms=a.query.casefold().split(); results=[]
    for source in json.loads(a.evidence.read_text()).get('sources',[]):
        hay=' '.join(str(source.get(k,'')) for k in ['key','title','url']).casefold()
        if terms and not any(t in hay for t in terms): continue
        results.append({k:source.get(k) for k in ['id','key','title','url','consulted_at','publication_date']})
    print(json.dumps({'recommendations':results,'route':'MCP de lecture documentaire','basis':'sources consignées comme ouvertes par le rédacteur ; à relire pour audit','live_http_probe':False},ensure_ascii=False,indent=2))
