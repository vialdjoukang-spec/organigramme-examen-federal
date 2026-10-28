#!/usr/bin/env python3
"""Tient harnais/etat/etat.json : etat.py set NNN etape|pr|captures|note valeur"""
import json, sys
from pathlib import Path
p = Path(__file__).resolve().parent / "etat.json"
d = json.load(open(p)) if p.exists() else {}
if len(sys.argv) >= 5 and sys.argv[1] == "set":
    v = sys.argv[4]; d.setdefault(sys.argv[2], {})[sys.argv[3]] = int(v) if v.isdigit() else v
    json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)
print(json.dumps(d, ensure_ascii=False))
