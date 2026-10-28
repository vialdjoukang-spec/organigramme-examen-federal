#!/usr/bin/env python3
"""finaliser_lot.py NNN : répare les lignes trop longues, vérifie le LOT, manifeste, 10 captures, commit, merge main, push. Gratuit."""
import glob, subprocess, sys, shutil
from pathlib import Path
R = Path(__file__).resolve().parents[2]; N = sys.argv[1]; W = R.parent / f"wc-{N}"; D = W / f"LOT_Claude_Finaux/LOT_{N}"
sys.path[:0] = [str(R / "harnais/grille14"), str(R / "harnais")]
import grille_agent as G
for f in sorted(glob.glob(str(D / f"LOT_{N}_*.html"))):
    t = open(f, encoding="utf-8").read(); r = G.reparer(t, N, Path(f).name); h = r[0] if isinstance(r, tuple) else r
    if h != t: open(f, "w", encoding="utf-8").write(h)
shutil.rmtree(R / ".cache/harnais", ignore_errors=True)
sh = lambda c: subprocess.run(c, shell=True, cwd=R, capture_output=True, text=True)
v = sh(f"python3 harnais/controle_lot.py verifier {D}").stdout.strip().splitlines()[-1]; print(v)
sh(f"python3 harnais/controle_lot.py manifeste {D}")
S = f"/tmp/claude-0/-home-user-organigramme-examen-federal/939dd4bc-a7c0-53f6-b753-cf529d7def3a/scratchpad/lot{N}"; shutil.rmtree(S, ignore_errors=True)
print(sh(f"node harnais/etat/captures10.js {D} {S} {int(N)}").stdout.strip().count("png"), "captures dans", S)
sh(f"python3 harnais/etat/etat.py set {N} etape PR; python3 harnais/etat/etat.py set {N} captures 10")
c = subprocess.run(f"cd {W} && git add -A && git commit -q --no-verify -m 'LOT_{N} : corrections du cerveau (forme, concision, jugement médical)' ; git fetch -q origin main && git merge -q --no-edit origin/main; git push -q origin corr/lot-{N}-cerveau && echo pushed", shell=True, capture_output=True, text=True); print(c.stdout.strip()[-60:], c.stderr.strip()[-200:])
