#!/usr/bin/env python3
"""Passage utile d'un long texte (Chonkie) : découpe en morceaux et ne rend que ceux qui contiennent les mots demandés.
  python3 harnais/grille14/passage.py <fichier_texte> "<mots clés>" [n=3]"""
import re, sys
from pathlib import Path
from chonkie import TokenChunker
f, mots = Path(sys.argv[1]), [m.lower() for m in sys.argv[2].split()]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 3
t = f.read_text(encoding="utf-8", errors="replace"); t = re.sub(r"<[^>]+>", " ", t)
ch = TokenChunker(chunk_size=300, chunk_overlap=30).chunk(t)
sc = sorted(((sum(c.text.lower().count(m) for m in mots), i, c.text) for i, c in enumerate(ch)), reverse=True)[:n]
for s, i, x in sc:
    if s: print(f"--- morceau {i} (score {s}) ---\n{re.sub(chr(10)+'+', chr(10), x.strip())}")
