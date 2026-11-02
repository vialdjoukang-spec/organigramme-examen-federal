#!/usr/bin/env python3
"""AUDIT AVANT SORTIE (porte du commit) : Harnais sain + forme du LOT + contrôle médical + contrôle de langue, tout par scripts.
  python3 harnais/audit_sortie.py <LOT_XXX> [--dossier <chemin>]   → code 0 = sortie autorisée"""
import subprocess, sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent; lot = sys.argv[1].replace("LOT_", "")
def run(*a): return subprocess.run([sys.executable, *a], capture_output=True, text=True, cwd=R)
v = run("harnais/dispositif/veille.py", "--once"); print("HARNAIS :", "OK" if v.returncode == 0 else "KO " + v.stdout[-300:])
args = ["harnais/audit_lot.py", lot] + (["--dossier", sys.argv[sys.argv.index("--dossier") + 1]] if "--dossier" in sys.argv else [])
d = sys.argv[sys.argv.index("--dossier") + 1] if "--dossier" in sys.argv else f".cache/travail/LOT_{lot}"
cl = run("harnais/controle_lot.py", "verifier", d); print("FORME :", cl.stdout.strip().splitlines()[0] if cl.stdout.strip() else cl.stderr[-200:])
a = run(*args); print(a.stdout[-1500:])
ok = v.returncode == 0 and "CONFORME" in cl.stdout and "NON CONFORME" not in cl.stdout and a.returncode == 0
print("SORTIE AUTORISÉE" if ok else "SORTIE REFUSÉE"); sys.exit(0 if ok else 1)
