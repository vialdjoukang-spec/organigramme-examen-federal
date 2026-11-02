#!/usr/bin/env python3
"""Bilan automatique depuis un instant donné (gratuit, lit git et le dossier de travail) :
  python3 harnais/bilan/bilan.py [--depuis 2026-10-27T00:41:27Z] [--md]
Tableau 1 : fusions sur main (PR, branche, heure UTC, fichiers du LOT).  Tableau 2 : état de chaque LOT (déposé, fusionné, en cours).
Les remarques de relecture et leurs corrections se lisent dans les PR ; ce script donne la trame chiffrée."""
import argparse, json, re, subprocess
from datetime import datetime, timezone
from pathlib import Path
R = Path(__file__).resolve().parents[2]
ap = argparse.ArgumentParser(); ap.add_argument("--depuis", default="2026-10-27T00:41:27Z"); ap.add_argument("--md", action="store_true"); ap.add_argument("--max", type=int, default=16); a = ap.parse_args()
sh = lambda *c, cwd=R: subprocess.run(c, cwd=cwd, capture_output=True, text=True).stdout
subprocess.run(["git", "fetch", "-q", "origin", "main"], cwd=R)
def grille(tete, lignes):
    if a.md: return "| " + " | ".join(tete) + " |\n|" + "---|" * len(tete) + "\n" + "\n".join("| " + " | ".join(map(str, l)) + " |" for l in lignes)
    w = [max(len(str(x)) for x in col) for col in zip(tete, *lignes)]
    sep = "+" + "+".join("-" * (n + 2) for n in w) + "+"; fmt = lambda l: "| " + " | ".join(str(x).ljust(n) for x, n in zip(l, w)) + " |"
    return "\n".join([sep, fmt(tete), sep] + [fmt(l) for l in lignes] + [sep])
rows = []
for l in sh("git", "log", "origin/main", "--merges", f"--since={a.depuis}", "--format=%cI|%s").splitlines():
    t, s = l.split("|", 1); m = re.match(r"Merge pull request #(\d+) from \S+/(\S+)", s)
    if not m: continue
    u = datetime.fromisoformat(t).astimezone(timezone.utc).strftime("%d %H:%M")
    rows.append((u, f"#{m.group(1)}", m.group(2)))
rows.sort()
print("1. FUSIONS SUR main (UTC)\n" + grille(["heure", "PR", "branche"], rows or [["—", "—", "—"]]))
etat = {l["lot"]: l for l in json.loads(sh("git", "show", "origin/main:LOT_Claude_Finaux/ETAT_FILE.json"))["lots"]}
L = []
for n in [k for k in sorted(etat) if int(k) <= a.max]:
    d = f"LOT_Claude_Finaux/LOT_{n}"; fich = [x for x in sh("git", "ls-tree", "--name-only", "origin/main", d + "/").splitlines() if x.endswith(".html")]
    W = R / ".cache/travail" / f"LOT_{n}"; ecrits = len(list(W.glob("*.html"))) if W.exists() else 0; prets = len(list((W / "pret").glob("*"))) if (W / "pret").exists() else 0
    blq = len(list((W / "bloque").glob("*"))) if (W / "bloque").exists() else 0
    e = etat[n]; etat_txt = "fusionné" if fich else ("en cours" if ecrits else ("préparé" if W.exists() else "à faire"))
    L.append((f"LOT_{n}", e.get("code", ""), len(fich) or "", etat_txt, f"{ecrits}/{prets}/{blq}" if ecrits else ""))
print("\n2. ÉTAT DES LOT (fichiers sur main ; en cours = écrits/prêts/bloqués)\n" + grille(["LOT", "G", "HTML sur main", "état", "écrits/prêts/bloqués"], L))
print(f"\nCommits de la branche de session depuis {a.depuis[:16]} : {len(sh('git','log','--since='+a.depuis,'--format=%h').split())}")
