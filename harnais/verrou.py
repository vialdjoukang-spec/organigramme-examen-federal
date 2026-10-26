#!/usr/bin/env python3
"""Verrou anti-collision (fichier = un seul agent). Création atomique (O_EXCL) dans .cache/verrous/.
  verrou.py claim <fichier> <agent>   → 0 si pris, 3 si déjà détenu par un autre (STOP : ne pas écrire)
  verrou.py release <fichier> <agent> · verrou.py liste · verrou.py nettoyer-lot <LOT_XXX>"""
import hashlib, json, os, sys, time
from pathlib import Path
V = Path(__file__).resolve().parent.parent / ".cache" / "verrous"; V.mkdir(parents=True, exist_ok=True)
def f(p): return V / (hashlib.sha256(os.path.abspath(p).encode()).hexdigest()[:20] + ".lock")
a = sys.argv[1:]
if a[:1] == ["claim"]:
    try:
        fd = os.open(f(a[1]), os.O_CREAT | os.O_EXCL | os.O_WRONLY); os.write(fd, json.dumps({"fichier": a[1], "agent": a[2], "t": time.time()}).encode()); os.close(fd); print("OK verrou pris")
    except FileExistsError:
        d = json.loads(f(a[1]).read_text()); print("COLLISION :", d["fichier"], "détenu par", d["agent"]); sys.exit(0 if d["agent"] == a[2] else 3)
elif a[:1] == ["release"]:
    try:
        d = json.loads(f(a[1]).read_text())
        if d["agent"] == a[2]: f(a[1]).unlink(); print("OK libéré")
        else: print("REFUS : détenu par", d["agent"]); sys.exit(3)
    except FileNotFoundError: print("aucun verrou")
elif a[:1] == ["liste"]:
    for p in V.glob("*.lock"):
        d = json.loads(p.read_text()); print(d["agent"], d["fichier"], int(time.time() - d["t"]), "s")
elif a[:1] == ["nettoyer-lot"]:
    n = 0
    for p in V.glob("*.lock"):
        if a[1] in json.loads(p.read_text())["fichier"]: p.unlink(); n += 1
    print(n, "verrou(s) supprimé(s)")
else: print(__doc__)
