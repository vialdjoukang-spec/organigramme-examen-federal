#!/usr/bin/env python3
"""Détective de nouveaux fichiers (Vial, 28.10.2026) : veille des dossiers utiles, purge des brouillons.
  python3 harnais/brain/detective.py              un passage : nouveaux / modifiés / disparus depuis le dernier passage
  python3 harnais/brain/detective.py --veille [s] boucle (défaut 20 s) ; chaque nouveau HTML de LOT est mesuré en Ko (bande 100–298)
  python3 harnais/brain/detective.py --purger     détruit sans délai les brouillons NON SUIVIS par git (jamais un fichier versionné)
Dossiers utiles surveillés : DOSSIERS ci-dessous. Brouillons : __pycache__, *.pyc, *.tmp, *~, *.bak, *.orig, *.whl, .DS_Store, brouillon*/draft*.
Instantané : .cache/brain/detective.json."""
import hashlib, json, shutil, subprocess, sys, time
from pathlib import Path
R = Path(__file__).resolve().parents[2]
DOSSIERS = ["LOT_Claude_Finaux", "essai_flash", "harnais/etat", "harnais/brain", "audit", "journal", ".claude/agents"]
BROUILLON = ("*.pyc", "*.tmp", "*~", "*.bak", "*.orig", "*.whl", ".DS_Store", "brouillon*", "draft*")
SNAP = R / ".cache/brain/detective.json"
sys.path.insert(0, str(Path(__file__).parent)); import mesure_ko


def etat():
    e = {}
    for d in DOSSIERS:
        for f in sorted((R / d).rglob("*")) if (R / d).is_dir() else []:
            if f.is_file() and "__pycache__" not in f.parts and ".cache" not in f.parts:
                st = f.stat(); e[str(f.relative_to(R))] = [st.st_size, round(st.st_mtime)]
    return e


def passage(verbose=True):
    av = json.loads(SNAP.read_text()) if SNAP.exists() else None
    ap = etat(); SNAP.parent.mkdir(parents=True, exist_ok=True); SNAP.write_text(json.dumps(ap))
    if av is None: print(f"# premier passage : {len(ap)} fichiers en base"); return [], [], []
    nv, md, ds = [k for k in ap if k not in av], [k for k in ap if k in av and ap[k] != av[k]], [k for k in av if k not in ap]
    for t, l in (("NOUVEAU", nv), ("MODIFIÉ", md), ("DISPARU", ds)):
        for k in l:
            ko = f" · {mesure_ko.verdict(ap[k][0])} {ap[k][0] / 1000:.1f} Ko" if k.endswith(".html") and "LOT" in k and k in ap else ""
            print(f"{time.strftime('%H:%M:%S')} {t} {k}{ko}")
    if verbose and not (nv or md or ds): print(f"{time.strftime('%H:%M:%S')} rien de nouveau")
    return nv, md, ds


def purger():
    suivis = set(subprocess.run(["git", "ls-files"], capture_output=True, text=True, cwd=R).stdout.splitlines())
    n = 0
    for p in list(R.rglob("__pycache__")):
        if ".git" not in p.parts: shutil.rmtree(p, ignore_errors=True); n += 1
    for pat in BROUILLON:
        for f in R.rglob(pat):
            if f.is_file() and ".git" not in f.parts and str(f.relative_to(R)) not in suivis: f.unlink(); n += 1; print("détruit", f.relative_to(R))
    print(f"# purge : {n} brouillon(s) détruit(s) (fichiers versionnés intacts)")


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--purger" in a: purger()
    if "--veille" in a:
        s = int(a[a.index("--veille") + 1]) if a.index("--veille") + 1 < len(a) and a[a.index("--veille") + 1].isdigit() else 20
        while True: passage(verbose=False); time.sleep(s)
    elif "--purger" not in a: passage()
