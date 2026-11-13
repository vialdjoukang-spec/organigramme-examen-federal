#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Planche HTML de contrôle des candidats (fond blanc) : une ligne par diagnostic, description voulue,
puis vignettes normal / patho avec licence, score et légende. Le choix final revient à Vial et au radiologue.
Usage : python3 planche.py [--de IMG-042] [--a IMG-344] [--sortie planche.html]"""
import argparse, glob, html, json, os

ICI = os.path.dirname(os.path.abspath(__file__))
E = html.escape

CSS = """
:root{--fond:#fff;--texte:#1d1d1f;--doux:#5f6368;--trait:#d9d9de;--normal:#0b6e4f;--patho:#a3271f;--carte:#fafafa}
body{background:var(--fond);color:var(--texte);font:14px/1.4 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;margin:0;padding:16px}
h1{font-size:20px;margin:0 0 4px} .resume{color:var(--doux);margin:0 0 16px}
.dx{border-top:2px solid var(--trait);padding:14px 0}
.dx h2{font-size:16px;margin:0 0 4px} .dx h2 small{color:var(--doux);font-weight:400}
.gold{color:var(--doux);margin:0 0 8px}
.role{margin:8px 0} .role h3{font-size:13px;margin:0 0 2px;text-transform:uppercase;letter-spacing:.04em}
.role.normal h3{color:var(--normal)} .role.patho h3{color:var(--patho)}
.voulu{margin:0 0 6px;font-style:italic}
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px}
.c{background:var(--carte);border:1px solid var(--trait);border-radius:6px;padding:6px;font-size:12px}
.c img{width:100%;height:190px;object-fit:contain;background:#000;border-radius:4px;display:block}
.c .m{display:flex;justify-content:space-between;gap:4px;margin:4px 0 2px;font-weight:600}
.c .lic{color:var(--normal)} .c .leg{color:var(--texte);max-height:7.5em;overflow:auto}
.c .src{color:var(--doux);word-break:break-word} .vide{color:var(--patho)}
nav{position:sticky;top:0;background:var(--fond);padding:6px 0;border-bottom:1px solid var(--trait);margin-bottom:8px;font-size:12px}
nav input{font:inherit;padding:4px 8px;width:min(320px,100%)}
"""

JS = """
const q=document.getElementById('q');q.addEventListener('input',()=>{const v=q.value.toLowerCase();
document.querySelectorAll('.dx').forEach(d=>{d.style.display=d.textContent.toLowerCase().includes(v)?'':'none'})});
"""


def carte(c, n):
    lien = c.get("url_source") or ""
    cit = c.get("auteur") or ""
    pan = f" · panneau {E(c['panneau'])}" if c.get("panneau") else ""
    return (f'<div class="c"><a href="{E(c.get("fichier_local", ""))}" target="_blank"><img loading="lazy" src="{E(c.get("fichier_local", ""))}" alt="candidat {n}"></a>'
            f'<div class="m"><span>#{n} · {E(c["source"])}{pan}</span><span>score {c["score"]}</span></div>'
            f'<div class="lic">{E(c.get("licence", "?"))} · {E(c.get("dimensions", ""))}</div>'
            f'<div class="leg">{E(c["legende"][:600])}</div>'
            f'<div class="src">{E(cit[:180])}<br><a href="{E(lien)}" target="_blank">source</a> · {E(", ".join(c.get("motifs", [])))}</div></div>')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--de", default="IMG-042")
    ap.add_argument("--a", default="IMG-344")
    ap.add_argument("--sortie", default=os.path.join(ICI, "planche.html"))
    a = ap.parse_args()
    fichiers = sorted(glob.glob(os.path.join(ICI, "candidats", "IMG-*", "candidats.json")))
    res = [json.load(open(f, encoding="utf-8")) for f in fichiers]
    res = [r for r in res if a.de <= r["id"] <= a.a]
    n = len(res) or 1
    p1 = sum(1 for r in res if r["patho"]["candidats"]); n1 = sum(1 for r in res if r["normal"]["candidats"])
    blocs = []
    for r in res:
        roles = []
        for role, nom in (("normal", "Normal"), ("patho", "Pathologique")):
            d = r[role]
            cartes = "".join(carte(c, i + 1) for i, c in enumerate(d["candidats"])) or '<p class="vide">Aucun candidat libre fiable.</p>'
            roles.append(f'<div class="role {role}"><h3>{nom} · {E(d["modalite"])} {E(" ".join(d["details"]))}</h3>'
                         f'<p class="voulu">Voulu : {E(d["a_chercher"])}</p><div class="grille">{cartes}</div></div>')
        reporte = " · Commons à compléter" if r.get("commons_a_completer") else ""
        blocs.append(f'<section class="dx" id="{E(r["id"])}"><h2>{E(r["id"])} — {E(r["diagnostic"])} <small>{reporte}</small></h2>'
                     f'<p class="gold">Examen de référence : {E(r.get("gold", ""))}</p>{"".join(roles)}</section>')
    page = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>Planche des candidats</title><style>{CSS}</style></head><body>'
            f'<h1>Planche de contrôle des clichés candidats</h1>'
            f'<p class="resume">{len(res)} diagnostics · ≥1 normal : {n1} ({100*n1//n} %) · ≥1 pathologique : {p1} ({100*p1//n} %). '
            f'Licences libres seulement (CC0, domaine public, CC BY, CC BY-SA). Choix final et repères : étape suivante, après vérification visuelle.</p>'
            f'<nav><input id="q" placeholder="Filtrer (id, diagnostic, mot de légende)"></nav>'
            f'{"".join(blocs)}<script>{JS}</script></body></html>')
    open(a.sortie, "w", encoding="utf-8").write(page)
    print(f"Planche : {a.sortie} ({len(res)} diagnostics)")


if __name__ == "__main__":
    main()
