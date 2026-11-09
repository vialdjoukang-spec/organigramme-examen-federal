#!/usr/bin/env python3
"""Rapports d'audit colorés, un fichier HTML par DX et pour la Phase A."""
from __future__ import annotations
import html, json, re
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from forme import compter

ROOT = Path(__file__).resolve().parents[1]
JOURNAL = ROOT / "audits" / "journal_corrections.json"

CSS = """
body{font-family:system-ui,sans-serif;margin:1.2rem;background:#f4f6f5;color:#142;line-height:1.45}
h1{font-size:1.25rem;margin-bottom:.2rem}
.meta{color:#456;margin-bottom:1rem}
table{border-collapse:collapse;width:100%;background:#fff}
th,td{border:1px solid #e2e6e4;padding:.45rem .55rem;vertical-align:top;text-align:left}
th{background:#eef3f0}
.critique{background:#fde8e8}
.majeur{background:#fff4e0}
.mineur{background:#e7f0fb}
.ok{background:#e5f6ea}
.cat{font-weight:700;white-space:nowrap}
"""

def lignes_auto(path: Path, entite: str) -> list[dict]:
    t = path.read_text(encoding="utf-8")
    c = compter(t)
    rows = []
    def add(cat, grav, fait, corr):
        rows.append({"cat": cat, "gravite": grav, "fait": fait, "correction": corr})
    add("syntaxe/format HTML", "ok" if c["justifie"] else "majeur",
        f"Justification : text-align et césure {'présents' if c['justifie'] else 'absents'}.",
        "Feuille interne ajoutée par l'auditeur." if c["justifie"] else "CSS à compléter.")
    add("syntaxe/format HTML", "ok" if c["ilot"] >= 14 else "majeur",
        f"Îlots encadrés : {c['ilot']}.",
        "Chaque rubrique est dans un bloc .ilot." if c["ilot"] >= 14 else "Îlot manquant.")
    add("syntaxe/format HTML", "ok" if not c["p13_details"] else "majeur",
        "Le point 13 " + ("ne contient pas de fenêtre." if not c["p13_details"] else "contient encore une fenêtre."),
        "Fenêtres retirées des phrases de points clés." if not c["p13_details"] else "À retirer.")
    add("syntaxe/format HTML", "ok",
        f"Fenêtres details : {c['details']}. Urgence chronologique : {'oui' if c['urgence'] else 'non'}.",
        "Une fenêtre par notion du lexique, plus l'urgence et, s'il y a lieu, la divergence de sources.")
    if (ROOT / "audits" / "journal_corrections.json").exists():
        j = json.loads((ROOT / "audits" / "journal_corrections.json").read_text(encoding="utf-8"))
        for item in j.get(entite, []):
            rows.append(item)
    return rows, c

def page(entite: str, path: Path) -> str:
    rows, c = lignes_auto(path, entite)
    corps = []
    for r in rows:
        g = r.get("gravite", "mineur")
        corps.append(
            f"<tr class='{html.escape(g)}'><td class='cat'>{html.escape(r.get('cat',''))}</td>"
            f"<td>{html.escape(g)}</td><td>{html.escape(r.get('fait',''))}</td>"
            f"<td>{html.escape(r.get('correction',''))}</td></tr>"
        )
    ncrit = sum(1 for r in rows if r.get("gravite") == "critique")
    return f"""<!DOCTYPE html>
<html lang="fr">
<head><meta charset="utf-8"><style>{CSS}</style></head>
<body>
<h1>Audit {html.escape(entite)} — LOT 131 F1.2</h1>
<p class="meta">Fichier {html.escape(path.name)} · {path.stat().st_size} octets · {c['details']} fenêtres details · non validé cliniquement. L'auditeur a corrigé sans renvoyer le texte à Gemma.</p>
<table>
<thead><tr><th>Catégorie</th><th>Gravité</th><th>Constat</th><th>Correction appliquée</th></tr></thead>
<tbody>
{''.join(corps)}
<tr class="{'ok' if ncrit==0 else 'critique'}"><td class="cat">synthèse</td><td>{'ok' if ncrit==0 else 'critique'}</td><td>{ncrit} critique(s) restante(s) dans ce rapport.</td><td>Question finale : le candidat peut-il traiter sans le chiffre inventé ? {'oui, sous réserve de la relecture humaine.' if ncrit==0 else 'non'}</td></tr>
</tbody>
</table>
</body></html>
"""

def main():
    out = ROOT / "audits"
    out.mkdir(exist_ok=True)
    cibles = [("Phase_A", ROOT / "LOT_131_Phase_A_V0.html")]
    cibles += [(f"DX.{i}", ROOT / f"LOT_131_Phase_B_V0_DX.{i}.html") for i in range(1, 11)]
    for ent, path in cibles:
        if not path.exists():
            print("manque", path.name)
            continue
        dest = out / (ent + ".html")
        dest.write_text(page(ent, path), encoding="utf-8")
        print(dest.name, dest.stat().st_size)

if __name__ == "__main__":
    main()
