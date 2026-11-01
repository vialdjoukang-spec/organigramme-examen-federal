#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""init_ssp.py — Prépare un SSP vide prêt à rédiger (canevas + checklist DD), sans rien écraser.

Usage : python3 init_ssp.py G3            (ou G03)
Crée dans Revision/<dossier MAP> :
  _bank_GNN.py        canevas d'auteur : META pré-rempli + 1 bloc commenté par DX (cibles EX/AP/SPE) + liens sources
  COUVERTURE_DD.md    checklist DD vide (régénérée ensuite par couverture_dd.py)
  CHANGELOG.md        journal
Puis :  rédiger → build_ssp.py <dossier> → couverture_dd.py <dossier> → etat_lieux.py
"""
import sys, os, re, datetime, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _commun import *

def titres_phase_a(s):
    p = os.path.join(lot_dir(s), f"{s['lot']}_Phase_A_V0.html")
    if not os.path.exists(p): return []
    t = open(p, encoding='utf-8').read()
    return [re.sub('<[^>]+>', '', m) for m in re.findall(r'<h3[^>]*>(.*?)</h3>', t, re.S)][:16]

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    s = ssp_entry(sys.argv[1]); d = ssp_dir(s); os.makedirs(d, exist_ok=True)
    nn = f"{s['num']:02d}"; bank = os.path.join(d, f"_bank_G{nn}.py")
    dx = liste_dx(s); today = datetime.date.today().isoformat()
    lotfiles = sorted(os.listdir(lot_dir(s)))
    if os.path.exists(bank):
        print(f"⚠ {bank} existe déjà : rien n'est écrasé."); return
    L = [f"# -*- coding: utf-8 -*-",
         f"# Banque {s['code']} — {s['titre_fr']} ({s['lot']}). Canevas généré par init_ssp.py le {today}.",
         "# RÈGLES : lire _outils/CHARTE_REDACTION.md AVANT d'écrire. Sources = UNIQUEMENT le LOT audité ci-dessous.",
         "# opts[0] = bonne réponse (son « pourquoi pas » est ignoré). dx : 1er DX.n = DX cible ; suivants = discrimination croisée.",
         "# Cible minimale : ≥ 2 EX par DX + discrimination croisée entre DX proches + red flags (bloc P) ; AP (mécanismes) et SPE (spécialité) en bonus.",
         f'R = "../../../{s["source"]}"',
         f'def PA(sec, label): return (f"{{R}}{s["lot"]}_Phase_A_V0.html#{{sec}}", f"Phase A {{label}}")',
         f'def B(n, p): return (f"{{R}}{s["lot"]}_Phase_B_V0_DX.{{n}}.html#dx{{n}}-p{{p}}", f"Phase B DX.{{n}} §{{p}}")',
         "# Ancres utiles : Phase A ssp-p1…ssp-p14, tableau, algo ; Phase B dx<n>-p1…p14 (§8 critères, §13 points clés, §14 pièges examen).",
         "", "# Sections Phase A détectées : " + " | ".join(titres_phase_a(s)[:14]), "",
         "# Modèle d'item :",
         '# q("D","DX.1 vs DX.2","assessment_diagnosis","cabinet",',
         '#  "Vignette : âge, sexe, contexte, signes, constantes, examens (sans indice de la réponse).",',
         '#  "Quelle est la prochaine étape la plus appropriée ?",',
         '#  [("Bonne réponse",""), ("Distracteur 1","pourquoi pas"), ("Distracteur 2","pourquoi pas"), ("Distracteur 3","pourquoi pas"), ("Distracteur 4","pourquoi pas")],',
         '#  "① Pourquoi c\'est juste (2–3 phrases, chiffres du cours).", "③ Perle clinique (1–2 phrases).", B(1,13),',
         '#  pol="positive", niv="examen", spe=None)',
         ""]
    for k, nom in dx:
        n = k.split('.')[1]
        L += [f"# ───── {k} — {nom}", f"#  sources : B({n},8) critères · B({n},13) points clés · B({n},14) pièges",
              "#  ☐ EX 1 (diagnostic / discrimination)   ☐ EX 2 (prise en charge / examen qui tranche)   ☐ AP (mécanisme)   ☐ SPE (spécialité ?)", ""]
    L += ["META = dict(",
          f' code="{s["code"]}", lot="{s["lot"]}", version="2.0.0", seed={s["num"]*3+1}, date="{today}",',
          f' titre={s["titre_fr"]!r}, titre_court={s["titre_fr"][:48]!r}, n_dx={len(dx)},',
          ' note_version="v2 : gabarit Revision (EX/AP/SPE, 💡 fermé)",',
          f' note_media="Vérifier la présence d\'images dans les HTML {s["lot"]} ; sinon media = null (ne jamais inventer de cliché).",',
          ' intro_R="Triage, prochain pas, red flag, mécanisme.",',
          ' intro_D="Les DX du LOT face à face : un signe, un examen qui tranche.",',
          ' intro_P="Pièges d\'examen et alarmes à ne jamais rater.",',
          f' verdict_label="Réflexe {s["code"]}",',
          f' footer="{s["lot"]} · {s["code"]} · Banque « Temps 1 » v2 · Faits issus exclusivement des leçons auditées {s["lot"]} · Type A (règles IML).",',
          ' carte_html="""<div class="reflex"><b>Les 3 questions réflexes</b><ol><li>…</li><li>…</li><li>…</li></ol></div><div class="map" style="margin-top:10px"><div class="ax rf"><h3>🚩 Ordre d\'exclusion</h3><ol><li>…</li></ol></div></div>""",',
          ' algo_html="""<table class="algo"><tr><th>Si…</th><th>Alors…</th></tr><tr class="e"><td>…</td><td>…</td></tr></table>""",',
          ")"]
    open(bank, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    cov = [f"# COUVERTURE_DD — {s['code']} {s['titre_fr']} ({s['lot']})", "", "_Checklist initiale (init_ssp.py) — à régénérer par couverture_dd.py après build_ssp.py._", "",
           "| DX | Diagnostic | EX ≥ 2 | AP | SPE |", "|---|---|---|---|---|"] + [f"| {k} | {nom} | ☐ ☐ | ☐ | ☐ |" for k, nom in dx]
    open(os.path.join(d, 'COUVERTURE_DD.md'), 'w', encoding='utf-8').write('\n'.join(cov) + '\n')
    ch = os.path.join(d, 'CHANGELOG.md')
    if not os.path.exists(ch):
        open(ch, 'w', encoding='utf-8').write(f"# {s['code']} — CHANGELOG\n\n- {today} : dossier initialisé par init_ssp.py ({len(dx)} DX, sources {s['source']}, {len(lotfiles)} fichiers).\n")
    print(f"✔ {s['code']} initialisé → {d}\n  {len(dx)} DX · canevas {os.path.basename(bank)} · prochain : rédiger puis build_ssp.py {s['dossier']}")

if __name__ == '__main__':
    main()
