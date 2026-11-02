#!/usr/bin/env python3
"""Veille de relance (gratuit) : ACTIF si des agents tournent ou si le dépôt a bougé depuis moins de 15 min ; sinon ARRÊT.
Ajoute RÉSUMÉ DÛ si le dernier résumé date de plus de 60 min. Sortie : une ligne."""
import json, os, subprocess, time
from pathlib import Path
R = Path(__file__).resolve().parents[2]
def sh(c): return subprocess.run(c, shell=True, cwd=R, capture_output=True, text=True).stdout.strip()
agents = len([l for l in sh("pgrep -fa 'agents/(B|R|A)[0-9]*\\.py|cerveau.py|orchestre.py|grille_agent|claude' | grep -v pgrep").splitlines()])
dernier = int(sh("git log -1 --format=%ct") or 0)
chg = int(max([os.path.getmtime(p) for p in R.glob(".cache/travail/**/*.html")] + [0]))
age = (time.time() - max(dernier, chg)) / 60
res = R / "harnais/etat/resumes.jsonl"
age_res = (time.time() - res.stat().st_mtime) / 60 if res.exists() else 999
etat = "ACTIF" if agents > 1 or age < 15 else "ARRÊT"
print(etat, f"· agents {agents} · dernier mouvement il y a {age:.0f} min" + (" · RÉSUMÉ DÛ" if age_res > 60 else ""))
