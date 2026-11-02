#!/usr/bin/env python3
"""Courbe de décroissance des jetons depuis un instant donné (gratuit : lit la transcription de la session).
  python3 harnais/bilan/courbe_jetons.py [--depuis 2026-10-27T00:41:27Z] [--pas 30] [--contexte 1000000] [--sortie DOSSIER]
Produit : courbe_jetons.csv, courbe_jetons.svg (sans dépendance), et un tableau texte.
 - « budget restant » = la valeur <total_tokens> annoncée à l'agent principal (décroît quand il écrit) ;
 - « agents » = jetons consommés par les sous-agents et workflows (champ subagent_tokens des notifications) ;
 - « contexte » = taille du contexte lue à chaque appel (entrée + cache) ; part de la fenêtre de 1 million."""
import argparse, glob, json, re, sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
ap = argparse.ArgumentParser()
ap.add_argument("--depuis", default="2026-10-27T00:41:27Z"); ap.add_argument("--pas", type=int, default=30)
ap.add_argument("--contexte", type=int, default=1_000_000); ap.add_argument("--sortie", default="harnais/bilan/sortie")
ap.add_argument("--transcription", default=None)
a = ap.parse_args()
P = lambda s: datetime.fromisoformat(s.replace("Z", "+00:00"))
t0 = P(a.depuis)
f = a.transcription or sorted(glob.glob(str(Path.home() / ".claude/projects/*/*.jsonl")), key=lambda p: Path(p).stat().st_size)[-1]
bud, sub, ctx = [], {}, []
for l in open(f, encoding="utf-8"):
    m = re.search(r'"timestamp":"([^"]+)"', l)
    if not m: continue
    try: t = P(m.group(1))
    except ValueError: continue
    if t < t0: continue
    for x in re.finditer(r"<total_tokens>([\d,]+) tokens left", l): bud.append((t, int(x.group(1).replace(",", ""))))
    for x in re.finditer(r"<subagent_tokens>(\d+)</subagent_tokens>", l): sub.setdefault(int(x.group(1)), t)   # dédoublonné par valeur
    if '"type":"assistant"' in l:
        try: u = json.loads(l).get("message", {}).get("usage") or {}
        except ValueError: u = {}
        c = u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0) + u.get("cache_read_input_tokens", 0)
        if c: ctx.append((t, c))
if not bud: sys.exit("aucune donnée de budget depuis cet instant")
fin = max(t for t, _ in bud); n = int((fin - t0).total_seconds() // (60 * a.pas)) + 1
rows = []
for i in range(n):
    b0, b1 = t0 + timedelta(minutes=i * a.pas), t0 + timedelta(minutes=(i + 1) * a.pas)
    bs = [v for t, v in bud if b0 <= t < b1]; cs = [v for t, v in ctx if b0 <= t < b1]
    ag = sum(v for v, ts in sub.items() if b0 <= ts < b1)
    rows.append(dict(debut=b0.strftime("%d %H:%M"), budget_restant=(min(bs) if bs else None), agents=ag, contexte_max=(max(cs) if cs else None)))
last = None
for r in rows:
    if r["budget_restant"] is None: r["budget_restant"] = last
    else: last = r["budget_restant"]
out = Path(a.sortie); out.mkdir(parents=True, exist_ok=True)
with open(out / "courbe_jetons.csv", "w", encoding="utf-8") as g:
    g.write("debut_UTC;budget_restant;jetons_agents;contexte_max;part_fenetre_pct\n")
    for r in rows: g.write(f"{r['debut']};{r['budget_restant']};{r['agents']};{r['contexte_max'] or ''};{round(100 * r['contexte_max'] / a.contexte, 1) if r['contexte_max'] else ''}\n")
W, H, M = 900, 380, 60; xs = lambda i: M + i * (W - 2 * M) / max(1, len(rows) - 1)
bv = [r["budget_restant"] for r in rows]; lo, hi = min(bv), max(bv); span = max(1, hi - lo)
yb = lambda v: M + (hi - v) * (H - 2 * M) / span
ma = max([r["agents"] for r in rows] + [1]); ya = lambda v: H - M - v * (H - 2 * M) / ma
pts = " ".join(f"{xs(i):.0f},{yb(v):.0f}" for i, v in enumerate(bv))
bars = "".join(f"<rect x='{xs(i)-6:.0f}' y='{ya(r['agents']):.0f}' width='12' height='{H-M-ya(r['agents']):.0f}' fill='#93c5fd' opacity='.7'/>" for i, r in enumerate(rows))
lab = "".join(f"<text x='{xs(i):.0f}' y='{H-M+16}' font-size='10' text-anchor='middle'>{r['debut'][-5:]}</text>" for i, r in enumerate(rows) if i % max(1, len(rows) // 12) == 0)
svg = f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' font-family='sans-serif'><rect width='{W}' height='{H}' fill='#fff'/>
<text x='{W/2}' y='24' text-anchor='middle' font-size='16' font-weight='bold'>Jetons depuis {a.depuis[:16].replace('T',' ')} UTC (pas {a.pas} min)</text>
{bars}<polyline points='{pts}' fill='none' stroke='#dc2626' stroke-width='3'/>
<line x1='{M}' y1='{H-M}' x2='{W-M}' y2='{H-M}' stroke='#444'/><line x1='{M}' y1='{M}' x2='{M}' y2='{H-M}' stroke='#444'/>{lab}
<text x='{M}' y='{M-8}' font-size='11' fill='#dc2626'>budget restant : {hi:,} → {lo:,}</text>
<text x='{W-M}' y='{M-8}' font-size='11' fill='#2563eb' text-anchor='end'>barres : jetons des agents par tranche (max {ma:,})</text></svg>""".replace(",", " ")
(out / "courbe_jetons.svg").write_text(svg, encoding="utf-8")
print(f"{'tranche UTC':<12}{'budget restant':>16}{'jetons agents':>16}{'contexte max':>14}{'% fenêtre':>10}")
for r in rows: print(f"{r['debut']:<12}{r['budget_restant']:>16,}{r['agents']:>16,}{(r['contexte_max'] or 0):>14,}{(100*r['contexte_max']/a.contexte if r['contexte_max'] else 0):>9.1f}%")
print(f"\nTOTAL agents : {sum(r['agents'] for r in rows):,} · budget principal consommé : {hi-lo:,} · fichiers : {out}/courbe_jetons.csv, courbe_jetons.svg")
