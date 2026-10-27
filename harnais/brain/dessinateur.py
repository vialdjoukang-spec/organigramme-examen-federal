#!/usr/bin/env python3
"""Dessinateur : brain_spec.json -> plan HTML en 3D (CSS 3D, sans dépendance, hors ligne).
Usage : dessinateur.py [spec.json] [sortie.html]"""
import json, sys, html
spec = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "brain_spec.json"))
sortie = sys.argv[2] if len(sys.argv) > 2 else "PLAN_BRAIN_HARNESS_3D.html"
e = html.escape
R = {r["id"]: r for r in spec["regions"]}
dim = {r["id"]: sum(1 for a, b in spec["liens"] if r["id"] in (a, b)) for r in spec["regions"]}
cartes = "".join(
 f'<div class="slab" data-id="{r["id"]}" style="--c:{r["couleur"]};--z:{i}"><b>{e(r["nom"])}</b><i>{len(r["scriptones"])} scriptones · {dim[r["id"]]} liens</i></div>'
 for i, r in enumerate(spec["regions"]))
detail = {r["id"]: {"nom": r["nom"], "role": r["role"], "sc": r["scriptones"], "c": r["couleur"],
          "liens": sorted({(R[b]["nom"] if a == r["id"] else R[a]["nom"]) for a, b in spec["liens"] if r["id"] in (a, b)}),
          "taches": [f'Tâche {t["n"]} · {t["sujet"]}' for t in spec["taches_vial"] if t["region"] == r["id"]]} for r in spec["regions"]}
page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>BRAIN-HARNESS · plan 3D</title>
<style>
:root{{--bg:#0f1226;--fg:#e8eaf6;--mut:#9aa3c7;--card:#1a1f3d}}
@media (prefers-color-scheme:light){{:root{{--bg:#f4f5fb;--fg:#1b1f3b;--mut:#5b6390;--card:#fff}}}}
*{{box-sizing:border-box}}body{{margin:0;font:16px/1.5 "Atkinson Hyperlegible",system-ui,sans-serif;background:var(--bg);color:var(--fg)}}
header{{padding:16px}}h1{{margin:0 0 4px;font-size:1.3rem}}p.but{{margin:0;color:var(--mut);max-width:70ch}}
main{{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:16px;padding:0 16px 24px}}
@media(max-width:820px){{main{{grid-template-columns:1fr}}}}
.scene{{height:560px;perspective:1100px;display:flex;align-items:center;justify-content:center;cursor:grab;background:var(--card);border-radius:14px;overflow:hidden;touch-action:none}}
.rig{{position:relative;width:300px;height:44px;transform-style:preserve-3d;transform:rotateX(58deg) rotateZ(-28deg)}}
.slab{{position:absolute;left:0;top:0;width:300px;height:44px;padding:6px 10px;border-radius:8px;background:var(--c);color:#fff;
 transform:translateZ(calc(var(--z)*34px - 150px));box-shadow:0 8px 22px #0006;transition:filter .2s;display:flex;flex-direction:column;justify-content:center;font-size:13px;cursor:pointer}}
.slab i{{font-style:normal;opacity:.85;font-size:11px}}.slab:hover,.slab.on{{filter:brightness(1.25)}}
aside{{background:var(--card);border-radius:14px;padding:16px;min-height:200px}}aside h2{{margin:0 0 6px;font-size:1.1rem}}
ul{{margin:6px 0 12px;padding-left:20px}}li{{margin:2px 0}}.chip{{display:inline-block;padding:1px 8px;border-radius:99px;background:#7c3aed33;margin:2px 4px 2px 0;font-size:.85rem}}
h3{{margin:12px 0 4px;font-size:.95rem;color:var(--mut)}}small{{color:var(--mut)}}
</style></head><body>
<header><h1>{e(spec["titre"])}</h1><p class="but">{e(spec["but"])}</p></header>
<main><div class="scene" id="scene"><div class="rig" id="rig">{cartes}</div></div>
<aside id="d"><h2>Touchez une couche</h2><small>Glissez la scène pour la faire pivoter. Chaque couche est une région du cerveau ; ses scriptones sont les neurones qui agissent sur l'information.</small>
<h3>Principes</h3><ul>{"".join(f"<li>{e(p)}</li>" for p in spec["principes"])}</ul>
<h3>Phases</h3><ul>{"".join(f"<li>{e(p)}</li>" for p in spec["phases"])}</ul></aside></main>
<script>
const D={json.dumps(detail, ensure_ascii=False)};
const rig=document.getElementById('rig'),sc=document.getElementById('scene'),d=document.getElementById('d');
let rx=58,rz=-28,drag=null;const set=()=>rig.style.transform=`rotateX(${{rx}}deg) rotateZ(${{rz}}deg)`;
sc.addEventListener('pointerdown',e=>{{drag=[e.clientX,e.clientY,rx,rz]}});
addEventListener('pointerup',()=>drag=null);
addEventListener('pointermove',e=>{{if(!drag)return;rz=drag[3]+(e.clientX-drag[0])*.4;rx=Math.max(10,Math.min(85,drag[2]-(e.clientY-drag[1])*.3));set()}});
const li=a=>a.map(x=>`<li>${{x}}</li>`).join('');
document.querySelectorAll('.slab').forEach(s=>s.addEventListener('click',()=>{{
 document.querySelectorAll('.slab').forEach(x=>x.classList.remove('on'));s.classList.add('on');const r=D[s.dataset.id];
 d.innerHTML=`<h2 style="color:${{r.c}}">${{r.nom}}</h2><p>${{r.role}}</p><h3>Scriptones</h3><ul>${{li(r.sc)}}</ul><h3>Connexions</h3>${{r.liens.map(x=>`<span class=chip>${{x}}</span>`).join('')}}${{r.taches.length?`<h3>Répond à</h3><ul>${{li(r.taches)}}</ul>`:''}}`}}));
</script></body></html>"""
open(sortie, "w", encoding="utf-8").write(page)
print(sortie, len(page) // 1024, "Ko")
