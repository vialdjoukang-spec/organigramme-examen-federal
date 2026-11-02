#!/usr/bin/env python3
"""Dessinateur : brain_spec.json -> plan HTML en 3D (CSS 3D, sans dépendance, hors ligne). Lit la v1 (scriptones en texte) et la v2 (objets).
Usage : dessinateur.py [spec.json] [sortie.html]   (par défaut : à côté de ce script)"""
import json, sys, html
from pathlib import Path
D = Path(__file__).resolve().parent
spec = json.load(open(sys.argv[1] if len(sys.argv) > 1 else D / "brain_spec.json", encoding="utf-8"))
sortie = sys.argv[2] if len(sys.argv) > 2 else D / "PLAN_BRAIN_HARNESS_3D.html"
e = html.escape
R = {r["id"]: r for r in spec["regions"]}
SC = lambda s: s if isinstance(s, dict) else {"nom": s, "etat": "prévu"}
L = [(l[0], l[1], l[2] if len(l) > 2 else "") for l in spec["liens"]]
dim = {i: sum(1 for a, b, _ in L if i in (a, b)) for i in R}
etat = lambda r: {k: sum(SC(s)["etat"] == k for s in r["scriptones"]) for k in ("implémenté", "existant", "prévu")}
cartes = "".join(
    f'<button class="slab" data-id="{r["id"]}" style="--c:{r["couleur"]};--z:{i}"><b>{e(r["nom"])}</b><i>{len(r["scriptones"])} scriptones · {etat(r)["implémenté"]} faits · {dim[r["id"]]} liens</i></button>'
    for i, r in enumerate(spec["regions"]))
detail = {r["id"]: {"nom": r["nom"], "role": r["role"], "c": r["couleur"],
          "sc": [[SC(s)["nom"], SC(s)["etat"], SC(s).get("fichier", ""), SC(s).get("codes", "")] for s in r["scriptones"]],
          "liens": sorted({f'{"→ " if a == r["id"] else "← "}{R[b if a == r["id"] else a]["nom"]}{" · " + t if t else ""}' for a, b, t in L if r["id"] in (a, b)}),
          "taches": [f'Tâche {t["n"]} · {t["sujet"]} : {t["scriptone"]}' for t in spec["taches_vial"] if t["region"] == r["id"]]} for r in spec["regions"]}
_F = json.loads((D.parent / "atkinson.b64.json").read_text())   # police embarquée, url citée à continuation CSS (hors ligne, jamais cassée)
_q = lambda b: "\\\n".join(b[i:i + 2000] for i in range(0, len(b), 2000))
FONTE = "".join(f'@font-face{{font-family:"Atkinson Hyperlegible";font-weight:{w};font-display:swap;src:url("data:font/woff2;base64,{_q(_F[w])}") format("woff2")}}' for w in ("400", "700"))
ul = lambda xs: "<ul>" + "".join(f"<li>{e(x)}</li>" for x in xs) + "</ul>"
met = "".join(f'<tr><td>{e(m["id"])}</td><td>{e(m["nom"])}</td><td>{e(m["seuil"])}</td><td>{e(m["mesure"])}</td></tr>' for m in spec.get("metriques", []))
bud = "".join(f'<tr><td>{e(b["etage"])}</td><td class="n">{b["plafond"]:,}</td><td>{e(b.get("mesure", b.get("note", "")))}</td></tr>'.replace(",", " ") for b in spec.get("budgets_jetons", []))
page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>BRAIN-HARNESS · plan 3D</title>
<style>{FONTE}
:root{{--bg:#f4f5fb;--fg:#1b1f3b;--mut:#5b6390;--card:#fff;--line:#d8dcef}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0f1226;--fg:#e8eaf6;--mut:#9aa3c7;--card:#1a1f3d;--line:#2c3360}}}}
:root[data-theme="dark"]{{--bg:#0f1226;--fg:#e8eaf6;--mut:#9aa3c7;--card:#1a1f3d;--line:#2c3360}}
*{{box-sizing:border-box}}body{{margin:0;font:16px/1.55 "Atkinson Hyperlegible",Verdana,system-ui,sans-serif;background:var(--bg);color:var(--fg)}}
header{{padding:16px}}h1{{margin:0 0 4px;font-size:1.3rem}}p.but{{margin:0;color:var(--mut);max-width:75ch}}
main{{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:16px;padding:0 16px 24px}}
@media(max-width:820px){{main{{grid-template-columns:1fr}}}}
.scene{{height:600px;perspective:1100px;display:flex;align-items:center;justify-content:center;cursor:grab;background:var(--card);border-radius:14px;overflow:hidden;touch-action:none}}
.rig{{position:relative;width:300px;height:44px;transform-style:preserve-3d;transform:rotateX(58deg) rotateZ(-28deg)}}
.slab{{all:unset;box-sizing:border-box;position:absolute;left:0;top:0;width:300px;height:44px;padding:6px 10px;border-radius:8px;background:var(--c);color:#fff;
 transform:translateZ(calc(var(--z)*30px - 160px));box-shadow:0 8px 22px #0006;display:flex;flex-direction:column;justify-content:center;font-size:13px;cursor:pointer}}
.slab i{{font-style:normal;opacity:.9;font-size:11px}}.slab:hover,.slab.on,.slab:focus-visible{{filter:brightness(1.25);outline:2px solid #fff}}
aside{{background:var(--card);border-radius:14px;padding:16px;min-width:0}}aside h2{{margin:0 0 6px;font-size:1.1rem}}
ul{{margin:6px 0 12px;padding-left:20px}}li{{margin:3px 0}}.chip{{display:inline-block;padding:1px 8px;border-radius:99px;background:#7c3aed22;margin:2px 4px 2px 0;font-size:.85rem}}
h3{{margin:14px 0 4px;font-size:.95rem;color:var(--mut)}}small{{color:var(--mut)}}code{{font-size:.82em;overflow-wrap:anywhere}}
.et{{display:inline-block;font-size:.72rem;border-radius:6px;padding:0 6px;margin-right:6px;color:#fff}}.et.implémenté{{background:#15803d}}.et.existant{{background:#2563eb}}.et.prévu{{background:#9ca3af}}
.tab{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;font-size:.85rem}}td,th{{border-top:1px solid var(--line);padding:4px 6px;text-align:left;vertical-align:top}}td.n{{text-align:right;white-space:nowrap}}
</style></head><body>
<header><h1>{e(spec["titre"])}</h1><p class="but">{e(spec["but"])}</p></header>
<main><div class="scene" id="scene" aria-label="Couches du cerveau, cliquables"><div class="rig" id="rig">{cartes}</div></div>
<aside id="d"><h2>Touchez une couche</h2><small>Glissez la scène pour la faire pivoter. Chaque couche est une région ; ses scriptones agissent sur l'information (corrigent, routent, bloquent) et parlent par le bus de doléances.</small>
<h3>Principes</h3>{ul(spec["principes"])}
<h3>Critique de la v1</h3>{ul(spec.get("critique_v1", []))}
<h3>Points de contrôle emboîtés</h3>{ul(spec.get("points_de_controle", []))}
<h3>Métriques</h3><div class="tab"><table><tr><th>id</th><th>mesure</th><th>seuil</th><th>état</th></tr>{met}</table></div>
<h3>Budgets de jetons par étage</h3><div class="tab"><table><tr><th>étage</th><th>plafond</th><th>note</th></tr>{bud}</table></div>
<h3>Phases</h3>{ul(spec["phases"])}</aside></main>
<script>
const D={json.dumps(detail, ensure_ascii=False)};
const rig=document.getElementById('rig'),sc=document.getElementById('scene'),d=document.getElementById('d'),acc=d.innerHTML;
const esc=s=>String(s).replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));
let rx=58,rz=-28,drag=null;const set=()=>rig.style.transform=`rotateX(${{rx}}deg) rotateZ(${{rz}}deg)`;
sc.addEventListener('pointerdown',ev=>{{if(ev.target.closest('.slab'))return;drag=[ev.clientX,ev.clientY,rx,rz]}});
addEventListener('pointerup',()=>drag=null);
addEventListener('pointermove',ev=>{{if(!drag)return;rz=drag[3]+(ev.clientX-drag[0])*.4;rx=Math.max(10,Math.min(85,drag[2]-(ev.clientY-drag[1])*.3));set()}});
document.querySelectorAll('.slab').forEach(s=>s.addEventListener('click',()=>{{
 const on=s.classList.contains('on');document.querySelectorAll('.slab').forEach(x=>x.classList.remove('on'));if(on){{d.innerHTML=acc;return}}
 s.classList.add('on');const r=D[s.dataset.id];
 d.innerHTML=`<h2 style="color:${{r.c}}">${{esc(r.nom)}}</h2><p>${{esc(r.role)}}</p><h3>Scriptones</h3><ul>${{r.sc.map(x=>`<li><span class="et ${{x[1]}}">${{x[1]}}</span>${{esc(x[0])}}${{x[3]?` <small>(${{esc(x[3])}})</small>`:''}}${{x[2]?`<br><code>${{esc(x[2])}}</code>`:''}}</li>`).join('')}}</ul><h3>Connexions</h3>${{r.liens.map(x=>`<span class=chip>${{esc(x)}}</span>`).join('')}}${{r.taches.length?`<h3>Répond à Vial</h3><ul>${{r.taches.map(x=>`<li>${{esc(x)}}</li>`).join('')}}</ul>`:''}}<p><small>Touchez à nouveau la couche pour revenir au plan.</small></p>`}}));
</script></body></html>"""
Path(sortie).write_text(page, encoding="utf-8")
print(sortie, len(page) // 1024, "Ko")
