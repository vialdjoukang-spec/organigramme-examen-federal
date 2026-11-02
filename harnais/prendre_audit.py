#!/usr/bin/env python3
"""Prend la prochaine tâche d'audit d'un territoire en ATTENDANT (zéro token) qu'un fichier arrive. Sortie : TACHE ... | FINI.
  prendre_audit.py <LOT> <label> <territoire 1|2|3> [attente_max_s=900]"""
import subprocess, sys, time
from pathlib import Path
R = Path(__file__).resolve().parent.parent; lot, lab, w = sys.argv[1:4]; t0 = time.time(); mx = int(sys.argv[4]) if len(sys.argv) > 4 else 900
while True:
    o = subprocess.run([sys.executable, "harnais/tableau_taches.py", "prendre", "audit-med", lot, lab, w], capture_output=True, text=True, cwd=R).stdout.strip()
    if o.startswith(("TACHE", "FINI")): print(o.replace(f".cache/travail/LOT_{lot}/", f".cache/travail/LOT_{lot}/B{w}/entree/")); break
    if time.time() - t0 > mx: print("FINI (délai)"); break
    time.sleep(15)
