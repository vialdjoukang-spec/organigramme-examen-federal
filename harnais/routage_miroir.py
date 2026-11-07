#!/usr/bin/env python3
"""Miroir du routage des modèles — zéro jeton (Python standard), à relancer à chaque commit.

Lit  journal/routage.jsonl  (+ LOT_Claude_Finaux/LOT_*/audits/{corrections,scores}.jsonl)
Écrit LOT_Claude_Finaux/ROUTAGE_MIROIR.html : HTML autonome, SVG inline, thème clair/sombre, 390 px.

Usage : python3 harnais/routage_miroir.py [--sortie chemin.html]
"""
from __future__ import annotations
import argparse, html, json, re, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
ZURICH = 1  # CET après le 25.10.2026 ; affichage uniquement
AGENTS = ["redacteur-phase-a", "redacteur", "auditeur-medical", "auditeur-conformite", "mecanique", "general-purpose", "fable"]
COUL = {"redacteur-phase-a": "c1", "redacteur": "c2", "auditeur-medical": "c3", "auditeur-conformite": "c4",
        "mecanique": "c5", "general-purpose": "c6", "fable": "c7"}


def parse_t(s: str) -> datetime:
    d = datetime.fromisoformat(s)
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(timezone.utc)


def lire_jsonl(p: Path) -> list[dict]:
    out = []
    if p.is_file():
        for l in p.read_text(encoding="utf8").splitlines():
            l = l.strip()
            if l:
                try:
                    out.append(json.loads(l))
                except json.JSONDecodeError:
                    pass
    return out


def charger(racine: Path = RACINE) -> dict:
    ev = lire_jsonl(racine / "journal" / "routage.jsonl")
    for e in ev:
        e["t"] = parse_t(e["horodatage"])
        e["lot"] = e.get("lot") if e.get("lot") not in (None, "—") else "hors LOT"
        e["cle"] = f"{e.get('agent')} · {e.get('modele')} · {e.get('effort')}"
        e["fichier"] = e.get("fichier") or e.get("lecon") or ""
    ev.sort(key=lambda e: e["t"])
    corr, scores = {}, {}
    for d in sorted((racine / "LOT_Claude_Finaux").glob("LOT_0*")):
        corr[d.name] = lire_jsonl(d / "audits" / "corrections.jsonl")
        scores[d.name] = lire_jsonl(d / "audits" / "scores.jsonl")
    return {"ev": ev, "corr": corr, "scores": scores}


def agent_de(c: dict) -> str:
    a = c.get("auditeur")
    if isinstance(a, dict):
        a = a.get("agent")
    return (a or c.get("agent") or "?").split(" (")[0]


# ------------------------------------------------------------------ primitives SVG
def esc(s) -> str:
    return html.escape(str(s), quote=True)


def hhmm(t: datetime) -> str:
    return t.strftime("%H:%M")


def svg_lignes(series: dict[str, list[tuple[float, float]]], x0: float, x1: float, ylab: str, largeur=720, hauteur=300,
               ticks_x=None, couleurs=None) -> str:
    """Courbes en escalier (x en secondes UTC, y cumulé). ticks_x : [(x, étiquette)]."""
    ml, mr, mt, mb = 44, 12, 14, 34
    W, H = largeur, hauteur
    ymax = max([p[1] for s in series.values() for p in s] + [1])
    pas = 10 ** len(str(int(ymax))) / 10
    for m in (1, 2, 5, 10):
        if ymax / (pas * m) <= 5:
            pas *= m
            break
    ytop = ((int(ymax) // int(pas)) + 1) * pas if pas >= 1 else ymax
    sx = lambda x: ml + (x - x0) / max(x1 - x0, 1) * (W - ml - mr)
    sy = lambda y: H - mb - y / ytop * (H - mt - mb)
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(ylab)}" class="graph">']
    y = 0
    while y <= ytop + 1e-9:
        o.append(f'<line class="grille" x1="{ml}" x2="{W - mr}" y1="{sy(y):.1f}" y2="{sy(y):.1f}"/>'
                 f'<text class="ax" x="{ml - 6}" y="{sy(y) + 4:.1f}" text-anchor="end">{int(y)}</text>')
        y += pas
    for x, lab in (ticks_x or []):
        o.append(f'<line class="grille" x1="{sx(x):.1f}" x2="{sx(x):.1f}" y1="{mt}" y2="{H - mb}"/>'
                 f'<text class="ax" x="{sx(x):.1f}" y="{H - mb + 16}" text-anchor="middle">{esc(lab)}</text>')
    for nom, pts in series.items():
        if not pts:
            continue
        d, py = [], 0
        d.append(f"M{sx(pts[0][0]):.1f},{sy(0):.1f}")
        for x, yv in pts:
            d.append(f"L{sx(x):.1f},{sy(py):.1f}L{sx(x):.1f},{sy(yv):.1f}")
            py = yv
        d.append(f"L{sx(x1):.1f},{sy(py):.1f}")
        c = (couleurs or {}).get(nom, "c1")
        o.append(f'<path class="ligne {c}" d="{"".join(d)}"/>')
    o.append(f'<text class="ax" x="{ml}" y="10" >{esc(ylab)}</text></svg>')
    return "".join(o)


def svg_barres_h(items: list[tuple[str, float, str]], unite="", largeur=720, ligne=26, fmt="{:.0f}") -> str:
    """Barres horizontales : (libellé, valeur, classe couleur)."""
    ml = 190
    H = ligne * len(items) + 8
    vmax = max([v for _, v, _ in items] + [1])
    o = [f'<svg viewBox="0 0 {largeur} {H}" class="graph" role="img">']
    for i, (lab, v, c) in enumerate(items):
        y = 4 + i * ligne
        w = v / vmax * (largeur - ml - 70)
        o.append(f'<text class="ax" x="{ml - 8}" y="{y + 15}" text-anchor="end">{esc(lab)}</text>'
                 f'<rect class="barre {c}" x="{ml}" y="{y + 3}" width="{max(w, 1):.1f}" height="{ligne - 8}" rx="3"/>'
                 f'<text class="val" x="{ml + w + 6:.1f}" y="{y + 15}">{fmt.format(v)}{unite}</text>')
    o.append("</svg>")
    return "".join(o)


CSS = """
:root{--bg:#f6f8fa;--fg:#17232b;--mu:#566872;--ca:#fff;--li:#cfd9df;--c1:#7a4fb0;--c2:#1d6fa5;--c3:#c0392b;--c4:#2e8b57;--c5:#8a8a8a;--c6:#d99a00;--c7:#555}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#10181d;--fg:#e6edf1;--mu:#9fb0ba;--ca:#18242b;--li:#2c3d47;--c1:#b794e6;--c2:#58a6dc;--c3:#ff7b6b;--c4:#5fcf92;--c5:#a0a0a0;--c6:#f2c14e;--c7:#aaa}}
:root[data-theme="dark"]{--bg:#10181d;--fg:#e6edf1;--mu:#9fb0ba;--ca:#18242b;--li:#2c3d47;--c1:#b794e6;--c2:#58a6dc;--c3:#ff7b6b;--c4:#5fcf92;--c5:#a0a0a0;--c6:#f2c14e;--c7:#aaa}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
main{max-width:980px;margin:auto;padding:16px}h1{font-size:1.4rem;margin:.2rem 0}h2{font-size:1.1rem;margin:1.6rem 0 .5rem}
.carte{background:var(--ca);border:1px solid var(--li);border-radius:10px;padding:12px;margin:10px 0;overflow-x:auto}
.mu{color:var(--mu);font-size:.85rem}.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:8px}
.kpi{background:var(--ca);border:1px solid var(--li);border-radius:10px;padding:8px 10px}.kpi b{display:block;font-size:1.5rem}
svg.graph{width:100%;height:auto;display:block}.grille{stroke:var(--li);stroke-width:1}.ax{fill:var(--mu);font-size:11px}.val{fill:var(--fg);font-size:12px}
.ligne{fill:none;stroke-width:2.2}.c1{stroke:var(--c1);fill:var(--c1)}.c2{stroke:var(--c2);fill:var(--c2)}.c3{stroke:var(--c3);fill:var(--c3)}.c4{stroke:var(--c4);fill:var(--c4)}.c5{stroke:var(--c5);fill:var(--c5)}.c6{stroke:var(--c6);fill:var(--c6)}.c7{stroke:var(--c7);fill:var(--c7)}
.ligne.c1,.ligne.c2,.ligne.c3,.ligne.c4,.ligne.c5,.ligne.c6,.ligne.c7{fill:none}.barre{stroke:none}
.leg{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:.85rem;margin:6px 0}.leg i{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:5px;vertical-align:-1px}
.leg .c1{background:var(--c1)}.leg .c2{background:var(--c2)}.leg .c3{background:var(--c3)}.leg .c4{background:var(--c4)}.leg .c5{background:var(--c5)}.leg .c6{background:var(--c6)}.leg .c7{background:var(--c7)}
table{border-collapse:collapse;width:100%;font-size:.85rem}th,td{border-bottom:1px solid var(--li);padding:4px 6px;text-align:left;white-space:nowrap}th{color:var(--mu);font-weight:600}
td.n{text-align:right;font-variant-numeric:tabular-nums}.pt{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:1px}
.pt.c1{background:var(--c1)}.pt.c2{background:var(--c2)}.pt.c3{background:var(--c3)}.pt.c4{background:var(--c4)}.pt.c5{background:var(--c5)}.pt.c6{background:var(--c6)}.pt.c7{background:var(--c7)}
@media (max-width:480px){main{padding:16px}.kpi b{font-size:1.25rem}}
"""


def legende(noms) -> str:
    return '<div class="leg">' + "".join(f'<span><i class="{COUL.get(n, "c7")}"></i>{esc(n)}</span>' for n in noms) + "</div>"


def construire(data: dict) -> str:
    ev, corr, scores = data["ev"], data["corr"], data["scores"]
    if not ev:
        return "<p>Aucune décision.</p>"
    t0, t1 = ev[0]["t"], ev[-1]["t"]
    x0, x1 = t0.timestamp(), t1.timestamp()
    # axe temps : repères toutes les 2 h (heure locale ZURICH)
    h = 3600
    premier = int(x0 // h + 1) * h
    ticks = [(x, f"{(datetime.fromtimestamp(x, timezone.utc).hour + ZURICH) % 24:02d}h") for x in range(premier, int(x1), 2 * h)]

    # --- 1. courbe cumulée par agent
    ser = defaultdict(list)
    cpt = Counter()
    ser["total"] = []
    for e in ev:
        cpt[e["agent"]] += 1
        ser[e["agent"]].append((e["t"].timestamp(), cpt[e["agent"]]))
        ser["total"].append((e["t"].timestamp(), sum(cpt.values())))
    coul = dict(COUL, total="c5")
    noms_courbe = [a for a in AGENTS if a in ser] + ["total"]
    g1 = svg_lignes({n: ser[n] for n in noms_courbe}, x0, x1, "décisions cumulées", ticks_x=ticks, couleurs=coul)

    # --- 2. répartition (agent · modèle · effort)
    rep = Counter(e["cle"] for e in ev)
    items = [(k, v, COUL.get(k.split(" · ")[0], "c7")) for k, v in sorted(rep.items(), key=lambda x: -x[1])]
    g2 = svg_barres_h(items)

    # --- 3. enchaînement par LOT
    lots = sorted({e["lot"] for e in ev if e["lot"].startswith("LOT")})
    lignes = []
    dur = []
    for lot in lots:
        es = [e for e in ev if e["lot"] == lot]
        seq = "".join(f'<span class="pt {COUL.get(e["agent"], "c7")}"></span>' for e in es)
        a, b = es[0]["t"], es[-1]["t"]
        d = (b - a).total_seconds() / 3600
        dur.append((lot, d, "c2"))
        c = Counter(e["agent"] for e in es)
        nc = len(corr.get(lot, []))
        lignes.append(f"<tr><td>{lot}</td><td>{(a.hour + ZURICH) % 24:02d}:{a.minute:02d}</td>"
                      f"<td class='n'>{d:.1f} h</td><td class='n'>{len(es)}</td><td class='n'>{c['redacteur'] + c['redacteur-phase-a']}</td>"
                      f"<td class='n'>{c['auditeur-medical']}</td><td class='n'>{c['auditeur-conformite']}</td><td class='n'>{nc}</td>"
                      f"<td>{seq}</td></tr>")
    tab = ("<table><tr><th>LOT</th><th>début</th><th>durée</th><th>décisions</th><th>rédac.</th><th>méd.</th><th>conf.</th>"
           "<th>corrections</th><th>enchaînement (chaque point = 1 décision)</th></tr>" + "".join(lignes) + "</table>")
    g3 = svg_barres_h(dur, " h", fmt="{:.1f}")

    # --- 4. corrections par agent
    ca = Counter()
    for lot, cs in corr.items():
        for c in cs:
            ca[agent_de(c)] += 1
    g4 = svg_barres_h([(k, v, COUL.get(k, "c7")) for k, v in ca.most_common()])

    # --- scores moyens (avant → après) pour contexte
    sc_lignes = []
    for lot, ss in scores.items():
        for s in ss:
            if isinstance(s.get("apres"), dict) and "Phase_A" not in str(s.get("fichier", "")):
                sc_lignes.append((lot, s["apres"].get("score_medical"), s["apres"].get("score_langue")))
    moy_med = sum(x[1] for x in sc_lignes if isinstance(x[1], (int, float))) / max(1, sum(1 for x in sc_lignes if isinstance(x[1], (int, float))))

    maintenant = datetime.now(timezone.utc).astimezone().strftime("%d.%m.%Y %H:%M")
    n_ag = Counter(e["agent"] for e in ev)
    kp = [("décisions", len(ev)), ("rédactions", n_ag["redacteur"] + n_ag["redacteur-phase-a"]),
          ("audits médicaux", n_ag["auditeur-medical"]), ("audits conformité", n_ag["auditeur-conformite"]),
          ("corrections journalisées", sum(ca.values()))]
    kpis = "".join(f'<div class="kpi"><b>{v}</b><span class="mu">{k}</span></div>' for k, v in kp)
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Routage miroir</title><style>{CSS}</style></head><body><main>
<h1>Miroir du routage des modèles</h1>
<p class="mu">Source : journal/routage.jsonl ({len(ev)} décisions, du {t0.astimezone().strftime('%d.%m %H:%M')} UTC au {t1.astimezone().strftime('%d.%m %H:%M')} UTC) et audits/*.jsonl. Généré le {maintenant} par harnais/routage_miroir.py (zéro jeton). Heures locales de l'axe : Zurich (UTC+1).</p>
<div class="kpis">{kpis}</div>
<h2>Décisions cumulées depuis le début</h2><div class="carte">{legende(noms_courbe)}{g1}</div>
<h2>Répartition par agent, modèle et effort</h2><div class="carte">{g2}</div>
<h2>Enchaînement et durée par LOT</h2><div class="carte">{legende([a for a in AGENTS if a in n_ag])}{tab}</div>
<div class="carte"><b>Durée entre la première et la dernière décision de routage du LOT</b> (le LOT_016 est en cours){g3}</div>
<h2>Corrections journalisées par auditeur</h2><div class="carte">{g4}<p class="mu">Score médical moyen après audit, fichiers Phase B (n={len(sc_lignes)}) : {moy_med:.1f}/100.</p></div>
</main></body></html>"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", default=str(RACINE / "LOT_Claude_Finaux" / "ROUTAGE_MIROIR.html"))
    a = ap.parse_args()
    data = charger()
    out = Path(a.sortie)
    out.write_text(construire(data), encoding="utf8")
    print(f"{out} : {len(data['ev'])} décisions, {sum(len(v) for v in data['corr'].values())} corrections")
    return 0


if __name__ == "__main__":
    sys.exit(main())
