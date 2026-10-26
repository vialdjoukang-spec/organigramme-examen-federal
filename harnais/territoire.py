#!/usr/bin/env python3
"""Territoires B1/B2/B3 : chaque agent Opus reste STRICTEMENT dans le sien (5 chapitres). Détecte tout mouvement hors territoire.
  territoire.py init <LOT>                       crée .cache/travail/LOT_XXX/B1|B2|B3/{entree,sortie}
  territoire.py garde <LOT> <W> <fichier>        photographie le LOT avant l'audit-correctif
  territoire.py controle <LOT> <W> <fichier>     VIOLATION si autre chose que <fichier> (et son rapport) a changé ; sinon OK
  territoire.py etat <LOT>                       fichiers par territoire (entree / sortie)"""
import hashlib, json, sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent; a = sys.argv[1:]; D = R / ".cache/travail" / f"LOT_{a[1]}"
def snap():
    return {str(p.relative_to(D)): p.stat().st_mtime_ns for p in D.rglob("*") if p.is_file() and "audits" not in p.parts and not p.name.endswith((".lock", ".json"))}
S = lambda w: R / f".cache/verrous/snap_{a[1]}_{w}.json"
if a[0] == "init":
    for w in "123": (D / f"B{w}/entree").mkdir(parents=True, exist_ok=True); (D / f"B{w}/sortie").mkdir(parents=True, exist_ok=True)
    print("territoires B1 B2 B3 créés")
elif a[0] == "garde": S(a[2]).write_text(json.dumps(snap())); print("garde posée")
elif a[0] == "controle":
    avant = json.loads(S(a[2]).read_text()); apres = snap(); mien = f"B{a[2]}/"
    bad = [k for k in set(avant) | set(apres) if avant.get(k) != apres.get(k) and not (k.startswith(mien) and (Path(k).name == Path(a[3]).name or k.endswith((".src",))))]
    print("OK : aucun mouvement hors territoire" if not bad else "VIOLATION de territoire : " + ", ".join(sorted(bad)[:8])); sys.exit(1 if bad else 0)
elif a[0] == "etat":
    for w in "123": print(f"B{w}", "entrée", len(list((D / f'B{w}/entree').glob('*.html'))), "· sortie", len(list((D / f'B{w}/sortie').glob('*.html'))))
