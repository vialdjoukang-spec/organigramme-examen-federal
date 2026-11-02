#!/usr/bin/env python3
"""Suivi par leçon (Vial, 28.10.2026) : page HTML, une jauge par leçon avec des ÉTRANGLEMENTS aux points de contrôle nommés.
  python3 harnais/brain/suivi_html.py [--sortie suivi.html]
Gratuit, sans modèle : lit les journaux de lancer_parallele.py (essai_lot*/journal/*.jsonl) et les fragments."""
import html, json, sys, time
from pathlib import Path
R = Path(__file__).resolve().parents[2]
# (nom, poids %, ce qui s'y passe)
POINTS = [("Découpe", 5, "Le script prend l'instantané d'entrée, découpe la leçon en ses 14 points et pose le squelette Flash (îlots, fenêtres)."),
          ("Rédaction", 45, "Un agent Sonnet par fragment, en parallèle : condenser (Pareto), phrases complètes, fenêtres, mots interactifs."),
          ("Mise en forme", 10, "Réassemblage par script, puis un agent Sonnet assembleur harmonise la mise en forme (redites, jonctions, îlots, fenêtres) sans rien perdre du fond ; contrôle de chaque point."),
          ("Porte duo", 10, "Porte unique : volume 80–150 Ko, îlots, fenêtres, langue, médical (AIPS)."),
          ("Professeur", 20, "Opus (une tentative) corrige les points signalés ; un chiffre perdu ramène le point à sa version sans perte."),
          ("Porte finale", 5, "Contrôle final ; les fautes restantes partent en tableau .md pour Vial."),
          ("Terminé", 5, "Leçon enregistrée.")]
def etat(jr, fait, fragdir):
    ev = [json.loads(l) for l in jr.read_text(encoding="utf-8").splitlines() if l.strip()] if jr.exists() else []
    total = len(list((fragdir / "duo").glob("p*.html"))) if (fragdir / "duo").is_dir() else 0
    duo = [e for e in ev if e.get("role") == "duo"]; prof = [e for e in ev if e.get("role") == "professeur"]
    portes = [e for e in ev if str(e.get("porte", "")).startswith("fin")]
    pts = [e for e in ev if e.get("porte") == "point"]
    f = [0.0] * 7
    f[0] = 1.0 if ev else 0.0
    f[1] = 1.0 if (pts or portes) else (min(1.0, len(duo) / total) if total else (0.3 if duo else 0.0))
    f[2] = 1.0 if (portes or pts) else 0.0
    f[3] = 1.0 if any("duo" in str(e.get("porte")) for e in portes) else 0.0
    f[4] = 1.0 if any("professeur" in str(e.get("porte")) for e in portes) else (0.5 if prof else 0.0)
    f[5] = 1.0 if any("professeur" in str(e.get("porte")) for e in portes) else 0.0
    f[6] = 1.0 if fait.exists() or any("fin" in e and "temps" in e for e in ev) else 0.0
    refus = sum(1 for e in ev if "refus_agent" in e)
    dernier = portes[-1] if portes else None
    return f, dict(duo=len(duo), total=total, prof=len(prof), refus=refus, verdict=dernier.get("verdict") if dernier else None, ko=dernier.get("ko") if dernier else None)
def tube(f):
    """SVG : tube dont la hauteur se resserre (étranglement) à chaque frontière de point de contrôle ; remplissage = avancement."""
    W, H, n = 1000, 46, 0
    xs, acc = [], 0
    for _, w, _ in POINTS: acc += w; xs.append(acc * 10)
    pct = sum(fr * w for fr, (_, w, _) in zip(f, POINTS))
    top, bot = [], []
    for x in range(0, W + 1, 10):
        d = min(abs(x - b) for b in xs[:-1])
        r = 10 + 13 * min(1, d / 18)            # rayon : 10 à l'étranglement, 23 ailleurs
        top.append(f"{x},{23 - r:.1f}"); bot.append(f"{x},{23 + r:.1f}")
    poly = " ".join(top + bot[::-1])
    cid = f"c{abs(hash(tuple(f))) % 10**8}"
    col = "#16a34a" if pct >= 99.5 else "#2563eb"
    return (f'<svg viewBox="0 0 {W} {H}" preserveAspectRatio="none" role="img" aria-label="{pct:.0f} %"><defs><clipPath id="{cid}"><polygon points="{poly}"/></clipPath></defs>'
            f'<polygon points="{poly}" fill="var(--b)"/><rect x="0" y="0" width="{pct * 10:.0f}" height="{H}" fill="{col}" clip-path="url(#{cid})"/>'
            f'<polygon points="{poly}" fill="none" stroke="var(--m)" stroke-width="1.5"/></svg>'), pct
def main(a):
    sortie = Path(a[a.index("--sortie") + 1]) if "--sortie" in a else R / "harnais/etat/suivi_lecons.html"
    lignes, tot = [], []
    for d in sorted(R.glob("essai_lot*")):
        j = d / "journal"
        for f in sorted(d.glob("*.html")):
            fr, i = etat(j / (f.name + ".jsonl"), j / (f.stem + ".fait.json"), j / (f.stem + ".fragments"))
            svg, pct = tube(fr); tot.append(pct)
            etape = next((POINTS[k][0] for k in range(7) if fr[k] < 1), "Terminé")
            noms = "".join(f'<span style="flex:{POINTS[k][1]}" class="{"ok" if fr[k] >= 1 else "en" if fr[k] > 0 else ""}" title="{html.escape(POINTS[k][2])}">{POINTS[k][0]}</span>' for k in range(7))
            det = f"duo {i['duo']}/{i['total'] or '?'} · prof {i['prof']}" + (f" · porte {i['verdict']} {i['ko']} Ko" if i["verdict"] else "") + (f" · refus d'agent {i['refus']}" if i["refus"] else "")
            lignes.append(f'<div class="l"><div class="h"><b>{html.escape(f.stem.replace("_Phase_B_V0_", " · ").replace("_Phase_A_V0", " · Phase A"))}</b><span>{pct:.0f} % · {etape}</span></div>{svg}<div class="n">{noms}</div><small>{html.escape(det)}</small></div>')
    legende = "".join(f"<li><b>{n}</b> ({w} %) : {html.escape(t)}</li>" for n, w, t in POINTS)
    moy = sum(tot) / len(tot) if tot else 0
    page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="30"><title>Suivi des leçons</title>
<style>:root{{--bg:#f6f7fb;--c:#fff;--fg:#1b1f3b;--m:#5b6390;--b:#dfe3f2}}@media(prefers-color-scheme:dark){{:root{{--bg:#0f1226;--c:#1a1f3d;--fg:#e8eaf6;--m:#9aa3c7;--b:#2b3260}}}}
body{{margin:0;font:15px/1.45 system-ui,sans-serif;background:var(--bg);color:var(--fg)}}main{{max-width:1000px;margin:0 auto;padding:16px}}h1{{font-size:1.3rem;margin:0}}
.l{{background:var(--c);border:1px solid var(--b);border-radius:10px;padding:10px 12px;margin:10px 0}}.h{{display:flex;justify-content:space-between;gap:8px}}svg{{width:100%;height:42px;display:block}}
.n{{display:flex;justify-content:space-between;font-size:.72rem;color:var(--m);gap:2px}}.n span{{flex:1;text-align:center}}.n .ok{{color:#16a34a;font-weight:700}}.n .en{{color:#2563eb;font-weight:700}}small{{color:var(--m)}}details{{margin:8px 0}}ul{{padding-left:18px}}</style></head><body><main>
<h1>Suivi des leçons · {time.strftime("%d.%m.%Y %H:%M:%S")}</h1><small>Avancement moyen {moy:.0f} % sur {len(tot)} leçon(s) · l'étranglement marque un point de contrôle ; survoler le nom pour voir ce qui s'y passe.</small>
<details><summary>Points de contrôle</summary><ul>{legende}</ul></details>{"".join(lignes) or "<p>Aucune leçon en cours.</p>"}</main></body></html>"""
    sortie.write_text(page, encoding="utf-8"); print(f"{sortie} · {len(tot)} leçon(s) · moyenne {moy:.0f} %")
if __name__ == "__main__": main(sys.argv[1:])
