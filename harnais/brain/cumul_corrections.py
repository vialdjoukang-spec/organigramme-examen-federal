#!/usr/bin/env python3
"""Cumul des corrections : agrège les rapports des agents (journaux de workflows) et les doléances de Vial.
Usage : cumul_corrections.py [dossier_workflows] [sortie.md]  — gratuit, zéro jeton."""
import glob, json, os, re, sys, collections
base = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/.claude/projects/-home-user-organigramme-examen-federal/939dd4bc-a7c0-53f6-b753-cf529d7def3a/subagents/workflows")
sortie = sys.argv[2] if len(sys.argv) > 2 else "CUMUL_CORRECTIONS.md"
par = collections.defaultdict(list); vus = set()
for j in sorted(glob.glob(os.path.join(base, "*", "journal.jsonl"))):
    for ligne in open(j, encoding="utf-8", errors="ignore"):
        try: o = json.loads(ligne)
        except Exception: continue
        r = o.get("result")
        if o.get("type") != "result" or not isinstance(r, str) or not re.search(r"corrig|retir|remplac|ajout|chang|réécri|supprim", r, re.I): continue
        r = re.sub(r"^SECURITY WARNING:.*?\n\n", "", r, flags=re.S).strip()
        if r[:80] in vus: continue
        vus.add(r[:80]); m = re.search(r"LOT_(\d{3})", r); par[m.group(1) if m else "—"].append(re.sub(r"\s+", " ", r))
n = sum(len(v) for v in par.values())
out = ["# Cumul des corrections depuis le début de la production", "",
 f"Source : rapports des agents auditeurs ({n} rapports), remarques de relecture externe, doléances de Vial. Généré par `harnais/brain/cumul_corrections.py` (gratuit).", ""]
for lot in sorted(par):
    out += [f"## LOT_{lot}" if lot != "—" else "## Non rattaché à un LOT", ""] + [f"- {t}" for t in par[lot]] + [""]
open(sortie, "w", encoding="utf-8").write("\n".join(out)); print(sortie, n, "rapports", os.path.getsize(sortie)//1024, "Ko")
