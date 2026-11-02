#!/usr/bin/env python3
"""Inventaire mécanique des brouillons ; aucune validation clinique."""
import argparse, hashlib, json, re
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('fichiers',nargs='+');a=p.parse_args();rows=[]
for name in a.fichiers:
 f=Path(name);raw=f.read_bytes();t=raw.decode();sections=list(re.finditer(r'^## (\d+)\. (.+)$',t,re.M)); ids=[int(m[1]) for m in sections]
 q=t[sections[-1].end():] if ids and ids[-1]==14 else ''
 questions=[int(x) for x in re.findall(r'^(\d+)\.\s+',q,re.M)]
 rows.append(dict(fichier=str(f),sha256=hashlib.sha256(raw).hexdigest(),octets=len(raw),parties=ids,questions=questions,structure_attendue=ids==list(range(1,15)) and questions==list(range(1,15))))
print(json.dumps(dict(portee='Structure Markdown uniquement ; aucun verdict médical, linguistique, sources ou rendu.',fichiers=rows),ensure_ascii=False,indent=2))
raise SystemExit(0 if all(r['structure_attendue'] for r in rows) else 1)
