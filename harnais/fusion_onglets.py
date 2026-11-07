#!/usr/bin/env python3
"""Réunit plusieurs versions HTML d'une leçon en un seul fichier à onglets majeurs (zéro jeton, sans JavaScript).

Chaque version est isolée dans un <iframe srcdoc> (ses fenêtres popover, ses ids et son style restent intacts).
Les onglets sont des boutons radio : un onglet = la page entière de la version choisie.
Usage : python3 harnais/fusion_onglets.py <sortie.html> <tableau.json> <libellé1>=<fichier1> <libellé2>=<fichier2> …
tableau.json : {"titre": "...", "colonnes": [...], "lignes": [[...], ...], "notes": ["...", ...]}
"""
import html, json, sys
from pathlib import Path

CSS = """
:root{--bg:#f4f6f8;--surface:#fff;--ink:#14212b;--ink2:#4a5865;--rule:#d6dee4;--accent:#0d6a8a;--accent-bg:#e2f0f5}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0f161c;--surface:#16202a;--ink:#e4ecf1;--ink2:#a8b6c1;--rule:#283541;--accent:#5eb4d4;--accent-bg:#17303b;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0f161c;--surface:#16202a;--ink:#e4ecf1;--ink2:#a8b6c1;--rule:#283541;--accent:#5eb4d4;--accent-bg:#17303b;color-scheme:dark}
*{box-sizing:border-box}html,body{height:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;display:flex;flex-direction:column}
header{padding:.6rem max(16px,env(safe-area-inset-left,0px)) .4rem;background:var(--surface);border-bottom:1px solid var(--rule)}
header h1{margin:0 0 .4rem;font-size:1.05rem}
.onglets{display:flex;flex-wrap:wrap;gap:.35rem}
.onglets input{position:absolute;opacity:0;pointer-events:none}
.onglets label{cursor:pointer;padding:.45rem .8rem;border:1px solid var(--rule);border-radius:8px 8px 0 0;background:var(--bg);color:var(--ink2);font-weight:600;font-size:.88rem}
.onglets label:hover{color:var(--ink)}
.onglets input:focus-visible+label{outline:2px solid var(--accent);outline-offset:2px}
main{flex:1;min-height:0;position:relative}
.page{display:none;position:absolute;inset:0}
.page iframe{width:100%;height:100%;border:0;background:#fff}
.tableau{overflow:auto;height:100%;padding:1rem max(16px,env(safe-area-inset-left,0px))}
.tableau table{border-collapse:collapse;background:var(--surface);font-size:.86rem;min-width:100%}
.tableau th,.tableau td{border:1px solid var(--rule);padding:.45rem .6rem;text-align:left;vertical-align:top;white-space:nowrap}
.tableau th{background:var(--accent-bg);font-weight:600}
.tableau td.n{text-align:right;font-variant-numeric:tabular-nums}
.tableau ul{max-width:70ch;padding-left:1.2rem}
"""


def main(a):
    sortie, tab = a[0], json.load(open(a[1], encoding="utf-8"))
    versions = [x.split("=", 1) for x in a[2:]]
    ids = ["t0"] + [f"t{i+1}" for i in range(len(versions))]
    regles = "".join(f"#{i}:checked~main .p-{i}{{display:block}} #{i}:checked+label{{background:var(--surface);color:var(--accent);border-bottom-color:var(--surface)}}" for i in ids)
    # les inputs doivent précéder main : on les met dans un même conteneur que main via une structure plate
    radios = [f'<input type="radio" name="o" id="t0" checked><label for="t0">Tableau final</label>']
    radios += [f'<input type="radio" name="o" id="{ids[i+1]}"><label for="{ids[i+1]}">{html.escape(lib)}</label>' for i, (lib, _) in enumerate(versions)]
    lignes = "".join("<tr>" + "".join(f'<td class="{"n" if isinstance(c,(int,float)) or str(c).replace(",","").replace(".","").replace(" ","").isdigit() else ""}">{html.escape(str(c))}</td>' for c in l) + "</tr>" for l in tab["lignes"])
    pages = [f'<div class="page p-t0"><div class="tableau"><h2>{html.escape(tab["titre"])}</h2><div style="overflow-x:auto"><table><thead><tr>'
             + "".join(f"<th>{html.escape(c)}</th>" for c in tab["colonnes"]) + f"</tr></thead><tbody>{lignes}</tbody></table></div>"
             + ("<ul>" + "".join(f"<li>{html.escape(n)}</li>" for n in tab.get("notes", [])) + "</ul>" if tab.get("notes") else "") + "</div></div>"]
    for i, (lib, f) in enumerate(versions):
        src = Path(f).read_text(encoding="utf-8")
        pages.append(f'<div class="page p-{ids[i+1]}"><iframe title="{html.escape(lib)}" srcdoc="{html.escape(src, quote=True)}"></iframe></div>')
    doc = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{html.escape(tab["titre"])}</title><style>{CSS}{regles}</style></head><body>'
           f'<header><h1>{html.escape(tab["titre"])}</h1></header>'
           f'<div style="display:contents"><div class="onglets" style="padding:0 max(16px,env(safe-area-inset-left,0px));background:var(--surface)">'
           + "".join(radios) + "</div></div></body></html>")
    # Structure CSS sans JS : les radios et main doivent être frères. On construit donc un conteneur plat.
    corps = ('<div class="cadre">'
             + "".join(radios).replace('<label', '<label style="display:inline-block"') + "<main>" + "".join(pages) + "</main></div>")
    doc = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{html.escape(tab["titre"])}</title><style>{CSS}{regles}.cadre>input{{position:absolute;opacity:0}}'
           f'.cadre{{padding-top:.3rem;display:flex;flex-wrap:wrap;align-items:flex-end;align-content:flex-start;flex:1;min-height:0}}.cadre>main{{flex:0 0 100%;height:calc(100vh - 6.2rem)}}.cadre>label{{margin-left:.35rem;cursor:pointer;padding:.45rem .8rem;border:1px solid var(--rule);border-radius:8px 8px 0 0;background:var(--bg);color:var(--ink2);font-weight:600;font-size:.88rem}}'
           f'.cadre>main{{border-top:1px solid var(--rule);margin-top:-1px}}</style></head><body>'
           f'<header><h1>{html.escape(tab["titre"])}</h1></header>{corps}</body></html>')
    Path(sortie).write_text(doc, encoding="utf-8")
    print(sortie, len(doc.encode()), "octets,", len(versions), "versions")


if __name__ == "__main__":
    main(sys.argv[1:])
