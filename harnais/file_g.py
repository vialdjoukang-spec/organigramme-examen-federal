#!/usr/bin/env python3
"""Prépare un LOT de la file G : dossier .cache/travail/LOT_XXX avec LISTE_DX_CANONIQUE.md, tableau de prévalences, plan R1/R2.
  python3 harnais/file_g.py prep 001"""
import glob, json, os, sys, zipfile
from pathlib import Path
R = Path(__file__).resolve().parent.parent
lot = sys.argv[2]; t = json.load(open(R / ".cache/g_in/g_tables.json"))[lot]
dd = [r for r in t["rows"] if r["dd"]]
D = R / ".cache/travail" / f"LOT_{lot}"; (D / "evidence").mkdir(parents=True, exist_ok=True)
N = len(dd); k = (N + 1) // 2
L = [f"# LISTE_DX_CANONIQUE — LOT_{lot} {t['code']} {t['nom']}", "", "**Statut :** liste fournie par les tableaux remplis (autre IA, 26.10.2026), ordre du tableau = prévalence décroissante ; lignes 11+ = à connaître absolument.", ""]
L += [f"DX.{i} — {r['dd']}" for i, r in enumerate(dd, 1)]
(D / "LISTE_DX_CANONIQUE.md").write_text("\n".join(L) + "\n", encoding="utf-8")
T = ["# Prévalences et sources fournies (non vérifiées par l'IA rédactrice : à relire dans la source avant usage)", ""] + [f"DX.{i} | {r['dd']} | {r['prev']} | {r['src']}" for i, r in enumerate(dd, 1)]
(D / "evidence" / "tableau_prevalences.md").write_text("\n".join(T) + "\n", encoding="utf-8")
(D / "PLAN.json").write_text(json.dumps({"lot": lot, "code": t["code"], "nom": t["nom"], "N": N, "R1": ["A"] + list(range(1, k + 1)), "R2": list(range(k + 1, N + 1))}, ensure_ascii=False))
S = R / ".cache/sources" / f"LOT_{lot}"
if not S.exists() or not any(S.iterdir()):
    S.mkdir(parents=True, exist_ok=True)
    z = zipfile.ZipFile(glob.glob(str(R / "LOTS*.zip"))[0])
    for i in z.infolist():
        if f"/LOT_{lot} " in i.filename and not i.is_dir():
            (S / i.filename.rsplit("/", 1)[1]).write_bytes(z.read(i))
print(json.dumps({"lot": lot, "sources": len(list(S.iterdir())), "code": t["code"], "nom": t["nom"], "N": N, "R1": ["A"] + list(range(1, k + 1)), "R2": list(range(k + 1, N + 1))}, ensure_ascii=False))
