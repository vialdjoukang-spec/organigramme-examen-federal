#!/usr/bin/env python3
"""Script qui maîtrise le Prompt ULTIME : extrait, du fichier PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md, les exigences opposables au rôle.
  python3 harnais/prompt_expert.py redacteur|phase-a [--complet]    (par défaut : liste d'obligations compacte, sourcée par § )
Les agents le lisent AVANT d'écrire ; les scripts de contrôle (médical, langue) appliquent les mêmes exigences à la sortie."""
import re, sys
from pathlib import Path
T = (Path(__file__).resolve().parent.parent / "PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md").read_text(encoding="utf-8")
role = sys.argv[1] if len(sys.argv) > 1 else "redacteur"
sec = {m.group(1): (m.start(), m) for m in re.finditer(r"^## (\d+)\. .*$", T, re.M)}
def S(n):
    ks = sorted(int(k) for k in sec); i = sec[str(n)][0]; j = [sec[str(k)][0] for k in ks if k > n][:1]; return T[i:(j[0] if j else len(T))]
W = {"redacteur": [11, 12, 13, 14, 16], "phase-a": [9, 11, 12, 13, 14, 16]}[role if role in ("redacteur", "phase-a") else "redacteur"]
print(f"# Exigences du Prompt ULTIME pour le rôle « {role} » (extraites du fichier, §{'/§'.join(map(str, W))})\n")
for n in W:
    s = S(n); print(f"## §{n} " + re.sub(r"^## \d+\. ", "", sec[str(n)][1].group(0)))
    if "--complet" in sys.argv: print(s); continue
    for l in s.splitlines():
        l = l.strip()
        if re.match(r"^\|\s*\d+\s*\|", l): print("- " + re.sub(r"\*\*|<[^>]+>", "", l)[:330])           # points 1–14
        elif re.search(r"Obsession|Interdit|jamais|obligatoire|bloquant|exig", l, re.I) and not l.startswith("|---"): print("- " + re.sub(r"\*\*|<[^>]+>|^[>\- ]+", "", l)[:300])
print("\n(Détail d'un § : --complet ; AIPS : harnais/aips_texte.py ; sources : harnais/SOURCES_AUTORISEES.md)")
