#!/usr/bin/env python3
"""État des lieux : page HTML interactive (jauges de progression), régénérée à volonté, gratuite.
  etat_des_lieux.py [--sortie ETAT_DES_LIEUX.html] [--resume "texte"]   (--resume ajoute une entrée datée au journal des résumés)
Mesures automatiques sur origin/main (marqueurs du cerveau) + état des étapes (harnais/etat/etat.json, tenu par `etat.py`)."""
import argparse, datetime as dt, html, json, os, subprocess, sys
from pathlib import Path
H = Path(__file__).resolve().parent; R = H.parents[1]
ap = argparse.ArgumentParser(); ap.add_argument("--sortie", default=str(H / "ETAT_DES_LIEUX.html")); ap.add_argument("--resume"); ap.add_argument("--artefact", action="store_true", help="page sans squelette (publication Artifact)")
a = ap.parse_args()
def sh(c): return subprocess.run(c, shell=True, cwd=R, capture_output=True, text=True).stdout
now = dt.datetime.now(dt.timezone.utc)
RES = H / "resumes.jsonl"
if a.resume:
    open(RES, "a", encoding="utf-8").write(json.dumps({"t": now.strftime("%d.%m.%Y %H:%M UTC"), "texte": a.resume}, ensure_ascii=False) + "\n")
resumes = [json.loads(l) for l in open(RES, encoding="utf-8")] if RES.exists() else []
etat = json.load(open(H / "etat.json")) if (H / "etat.json").exists() else {}
sh("git fetch -q origin main")
def compte(lot, motif):
    d = f"LOT_Claude_Finaux/LOT_{lot:03d}"
    tot = len([l for l in sh(f"git ls-tree --name-only origin/main {d}/").splitlines() if l.endswith(".html")])
    ok = len(sh(f"git grep -l '{motif}' origin/main -- '{d}/*.html'").splitlines()) if tot else 0
    return ok, tot
lots = []
for n in range(1, 13):
    brain, tot = compte(n, 'id="brain-barre14"')
    e = etat.get(f"{n:03d}", {})
    lots.append({"n": n, "tot": tot, "brain": brain, "etape": e.get("etape", "à faire"), "pr": e.get("pr"), "captures": e.get("captures", 0), "note": e.get("note", "")})
T = sum(l["tot"] for l in lots) or 1; B = sum(l["brain"] for l in lots)
ETAPES = ["à faire", "scripts", "agents", "audit final", "PR", "fusionné"]
agents = len([l for l in sh("pgrep -fa 'agents/(B|R|A)|cerveau.py|grille_agent' | grep -v pgrep").splitlines()])
def jauge(p, c="#16a34a"): return f'<div class="j"><i style="width:{p:.0f}%;background:{c}"></i><b>{p:.0f} %</b></div>'
lignes = ""
for l in lots:
    p = 100 * l["brain"] / l["tot"] if l["tot"] else 0
    k = ETAPES.index(l["etape"]) if l["etape"] in ETAPES else 0
    pr = f'<a href="https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/{l["pr"]}">#{l["pr"]}</a>' if l["pr"] else "·"
    lignes += f'<tr><td data-l="LOT_{l["n"]:03d}">LOT_{l["n"]:03d}</td><td>{jauge(p)}</td><td>{l["brain"]}/{l["tot"]}</td><td>{jauge(100*k/5, "#2563eb")}<small>{html.escape(l["etape"])}</small></td><td>{pr}</td><td>{l["captures"]}/10</td><td>{html.escape(l["note"])}</td></tr>'
res = "".join(f'<li><time>{html.escape(r["t"])}</time> {html.escape(r["texte"])}</li>' for r in reversed(resumes)) or "<li>Premier résumé à venir (toutes les 60 min).</li>"
page = f"""<title>État des lieux</title><meta name="claude:viewport-fit-sides" content="cover">
<style>:root{{--bg:#f6f7fb;--c:#fff;--fg:#1b1f3b;--m:#5b6390;--b:#dfe3f2}}@media(prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0f1226;--c:#1a1f3d;--fg:#e8eaf6;--m:#9aa3c7;--b:#2b3260;color-scheme:dark}}}}:root[data-theme="dark"]{{--bg:#0f1226;--c:#1a1f3d;--fg:#e8eaf6;--m:#9aa3c7;--b:#2b3260;color-scheme:dark}}
body{{margin:0;font:16px/1.5 "Atkinson Hyperlegible",system-ui,sans-serif;background:var(--bg);color:var(--fg)}}main{{max-width:1100px;margin:0 auto;padding-block:16px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
h1{{font-size:1.4rem;margin:0}}h2{{font-size:1.05rem;margin:22px 0 8px}}.card{{background:var(--c);border:1px solid var(--b);border-radius:12px;padding:14px}}
.j{{position:relative;height:20px;background:var(--b);border-radius:10px;overflow:hidden;min-width:110px}}.j i{{position:absolute;inset:0 auto 0 0}}.j b{{position:absolute;inset:0;text-align:center;font-size:.8rem;line-height:20px}}
table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid var(--b);padding:6px 8px;text-align:left;vertical-align:middle}}th{{background:var(--c);position:sticky;top:0}}small{{color:var(--m)}}
.g{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}}.k{{font-size:1.7rem;font-weight:700}}ul{{padding-left:18px}}time{{color:var(--m);font-weight:600}}.sc{{overflow:auto}}</style><main>
<h1>État des lieux · mise à jour {now.strftime("%d.%m.%Y %H:%M UTC")}</h1><small>Page régénérée par script ; recharger pour la dernière version.</small>
<h2>Vue d'ensemble</h2><div class="g">
<div class="card"><small>Cours corrigés par le cerveau (sur main)</small><div class="k">{B}/{T}</div>{jauge(100*B/T)}</div>
<div class="card"><small>LOT fusionnés (production LOT_001 à 012)</small><div class="k">12/12</div>{jauge(100)}</div>
<div class="card"><small>Correction de masse : LOT terminés</small><div class="k">{sum(1 for l in lots if l["etape"]=="fusionné")}/12</div>{jauge(100*sum(1 for l in lots if l["etape"]=="fusionné")/12,"#2563eb")}</div>
<div class="card"><small>Processus agents actifs</small><div class="k">{agents}</div></div></div>
<h2>Par LOT</h2><div class="card sc"><table><tr><th>LOT</th><th>Cours au cerveau</th><th>Fichiers</th><th>Étape</th><th>PR</th><th>Captures</th><th>Note</th></tr>{lignes}</table></div>
<h2>Résumés datés (toutes les 60 min)</h2><div class="card"><ul>{res}</ul></div>
<h2>Règles en vigueur</h2><div class="card"><ul><li>Rang 1 : correcteur Sonnet 5.5, puis jugement médical Sonnet 5.5, puis audit final Opus 5.5 moyen.</li><li>Panne : réparation seule, puis ingénieur Opus après deux échecs.</li><li>Après le LOT_012 : remplacement complet des équipes et nouveau test par automates.</li></ul></div></main>"""
if not a.artefact:
    page = '<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">' + page.replace("</style><main>", "</style></head><body><main>") + "</body></html>"
Path(a.sortie).write_text(page, encoding="utf-8"); print(a.sortie, f"{B}/{T} au cerveau")
