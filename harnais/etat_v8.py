#!/usr/bin/env python3
"""État des lieux de la refonte V8 (zéro jeton) : LOTS_V8 par LOT, contrôle verif_refonte, audits croisés et effort réel, agents en cours, K.
Sortie : LOT_Claude_Finaux/ETAT_V8.html"""
import datetime as dt, html, json, re, subprocess, sys
from pathlib import Path

R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R / "harnais"))
import modele_reel as mr, gouverneur as gv
H = html.escape
OUT = R / "LOT_Claude_Finaux" / "ETAT_V8.html"


def verif(lot, f):
    src = R / "LOT_Claude_Finaux" / lot / f.name
    a = ["python3", str(R / "harnais/verif_refonte.py"), str(src), str(f)]
    a += ["--phase-a"] if "Phase_A" in f.name else ["--ref", str(R / "LOTS_V8" / lot / f"{lot}_Phase_A_V0.html")]
    o = subprocess.run(a, capture_output=True, text=True).stdout.strip().splitlines()
    l = o[-1] if o else "?"
    m = re.search(r"T = ([\d.]+) Ko \(\+ ([\d.]+) Ko\)", l)
    return l.startswith("VERT"), (float(m.group(1)), float(m.group(2))) if m else (0, 0)


def attendus(lot):
    p = R / "LOT_Claude_Finaux" / lot
    return 1 + len(list(p.glob(f"{lot}_Phase_B_V0_DX.*.html")))


_, ags = mr.agents()
audits = {}
for a in ags:
    m = re.search(r"Audit croisé.*?(LOT_\d{3})", a["desc"])
    if m and a["etat"] == "terminé":
        audits.setdefault(m.group(1), []).append(a["servi"].split(" · ")[-1])
en_cours = [a for a in ags if a["etat"] == "en cours"]
lignes, tot_f, tot_att, tot_v = [], 0, 0, 0
for d in sorted((R / "LOTS_V8").glob("LOT_*"), reverse=True):
    lot = d.name; fs = sorted(d.glob("*.html")); att = attendus(lot)
    res = [(f, *verif(lot, f)) for f in fs]
    nv = sum(1 for _, ok, _ in res if ok); dx = [t for f, ok, t in res if "Phase_B" in f.name]
    pa = [t for f, ok, t in res if "Phase_A" in f.name]
    cours = [a["desc"] for a in en_cours if lot in a["desc"]]
    au = audits.get(lot, [])
    etat = ("audité xhigh" if "xhigh" in au and len(fs) == att else "refondu, audit à faire" if len(fs) == att and not any("Audit" in c for c in cours)
            else "audit en cours" if any("Audit" in c for c in cours) else "refonte en cours")
    lignes.append((lot, len(fs), att, nv, dx, pa, au, cours, etat)); tot_f += len(fs); tot_att += att; tot_v += nv
g = gv.calculer(); now = dt.datetime.now(dt.timezone(dt.timedelta(hours=1)))
ecarts = sum(1 for a in ags if a["ecart"])

rows = "".join(
    f'<tr><td class="m">{lot}</td><td class="n">{nf}/{att}</td><td class="n {"ok" if nv == nf else "ko"}">{nv}/{nf}</td>'
    f'<td class="n">{(f"{min(x for x,_ in dx):.1f}–{max(x for x,_ in dx):.1f}" if dx else "—")}</td><td class="n">{(f"{pa[0][0]:.1f}" if pa else "—")}</td>'
    f'<td>{", ".join(au) or "—"}</td><td><span class="b {"ok" if e.startswith("audité") else "run"}">{e}</span>{"<br><small>" + H("; ".join(c)) + "</small>" if c else ""}</td></tr>'
    for lot, nf, att, nv, dx, pa, au, c, e in lignes)
cours_html = "".join(f'<li><b>{H(a["desc"])}</b> — {H(a["servi"])} {"⚠ " + H(a["ecart"]) if a["ecart"] else "· conforme"}</li>' for a in en_cours) or "<li>Aucun</li>"
doc = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>État des lieux V8</title>
<style>:root{{--bg:#f3f7fa;--s:#fff;--i:#14212b;--i2:#4a5865;--r:#d6dee4;--ok:#1f7a4d;--run:#0d6a8a;--ko:#b3261e}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0f161c;--s:#16202a;--i:#e4ecf1;--i2:#a8b6c1;--r:#283541;--ok:#5cc28c;--run:#5eb4d4;--ko:#f2867e}}}}
:root[data-theme="dark"]{{--bg:#0f161c;--s:#16202a;--i:#e4ecf1;--i2:#a8b6c1;--r:#283541;--ok:#5cc28c;--run:#5eb4d4;--ko:#f2867e}}
body{{margin:0;background:var(--bg);color:var(--i);font:15px/1.45 system-ui,sans-serif;padding:16px;max-width:1000px;margin:auto}}
h1{{font-size:1.3rem;margin:.2rem 0}}h2{{font-size:1.05rem;margin:1.4rem 0 .5rem}}.meta{{color:var(--i2);font-size:.85rem}}
.tiles{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin-top:12px}}
.t{{background:var(--s);border:1px solid var(--r);border-radius:10px;padding:12px}}.t .big{{font-size:1.7rem;font-weight:700}}.t small{{color:var(--i2)}}
.w{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;background:var(--s);font-size:.88rem}}th,td{{border:1px solid var(--r);padding:6px 8px;text-align:left;vertical-align:top}}
th{{background:var(--bg)}}.n{{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}}.m{{font-family:ui-monospace,monospace}}
.ok{{color:var(--ok);font-weight:600}}.ko{{color:var(--ko);font-weight:600}}.b{{font-weight:600}}.b.run{{color:var(--run)}}.b.ok{{color:var(--ok)}}
ul{{background:var(--s);border:1px solid var(--r);border-radius:10px;padding:10px 10px 10px 28px}}li{{margin:.25rem 0}}</style></head><body>
<h1>État des lieux — refonte V8</h1><div class="meta">Relevé du {now:%d.%m.%Y à %H:%M} (Zurich) · branche production-v2 · généré par <span class="m">harnais/etat_v8.py</span>, zéro jeton</div>
<div class="tiles">
<div class="t"><small>Fichiers V8 produits</small><div class="big">{tot_f}<small> / {tot_att}</small></div><small>dans les LOTS entamés ({len(lignes)} LOTS)</small></div>
<div class="t"><small>Contrôle verif_refonte</small><div class="big {"ok" if tot_v == tot_f else "ko"}">{tot_v}/{tot_f}</div><small>VERT (nombres, fenêtres, fiche ≤ 9 Ko pour un DD)</small></div>
<div class="t"><small>LOTS audités en xhigh</small><div class="big">{sum(1 for l in lignes if l[8].startswith("audité"))}<small> / {len(lignes)}</small></div><small>audit croisé à effort réel xhigh (Article 4)</small></div>
<div class="t"><small>Parallélisme</small><div class="big">K = {g["K"]:.2f}</div><small>N* = {g["n_star"]:.1f} agents Opus xhigh · fenêtre 5 h : {g["conso_5h"]/g["B"]*100:.0f} % consommés</small></div>
</div>
<h2>Par LOT</h2><div class="w"><table><thead><tr><th>LOT</th><th>Fichiers</th><th>VERT</th><th>Fiches DX (Ko)</th><th>Phase A (Ko)</th><th>Audits croisés (effort réel)</th><th>État</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2>Agents en cours ({len(en_cours)})</h2><ul>{cours_html}</ul>
<h2>Article 4</h2><ul><li>{ecarts} agent(s) de la session ont tourné hors contrat (surtout les refontes LOT_013–016 en medium) ; détail dans <span class="m">journal/MODELE_REEL.md</span>.</li>
<li>LOT_013 à LOT_016 : refontes medium compensées par un audit croisé xhigh. Depuis 21:40, tout agent est lancé avec l'effort du contrat et vérifié en temps réel.</li></ul>
<h2>Reste à faire</h2><ul><li>LOT_011 : refonte en cours, puis audit croisé.</li><li>LOT_010 à LOT_001 : refonte V8 à faire (format ancien).</li><li>LOT_017 : production arrêtée (STOP), à reprendre directement en V8.</li><li>Décisions de Vial : listées par l'audit de LOT_012 à son retour.</li></ul>
</body></html>"""
OUT.write_text(doc, encoding="utf-8")
print(OUT, len(doc.encode()), "octets ·", f"{tot_f}/{tot_att} fichiers · {tot_v} VERT")
