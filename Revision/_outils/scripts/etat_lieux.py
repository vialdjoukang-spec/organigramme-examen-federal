#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""etat_lieux.py — Régénère ETAT_DES_LIEUX_QCM.md et _index/REGISTRE.csv pour G1–G16 (relève Λ).

Usage : python3 etat_lieux.py [--min 2]
Statut par SSP : absent (pas de JSON) | brouillon | revue_auto | valide (champ qualite.statut des questions).
Progression SSP = poids(statut) × couverture DD   avec poids absent 0 · brouillon 0,3 · revue_auto 0,8 · valide 1,0
  et couverture DD = part des DX ayant ≥ N EX cibles (couverture_dd.py).
Deux indicateurs globaux : % SSP livrés (revue_auto ou valide, 1/16 = 6,25 %) et % pondéré (moyenne des progressions).
"""
import sys, os, csv, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _commun import *
from couverture_dd import analyse

W = {'absent': 0, 'brouillon': .3, 'revue_auto': .8, 'valide': 1.0}

def main():
    a = sys.argv[1:]; nmin = int(a[a.index('--min') + 1]) if '--min' in a else 2
    M = load_map(); now = datetime.datetime.now()
    rows = []
    for s in M['ssp']:
        J, dx, cnt, gaps, trans = analyse(s, nmin)
        if J:
            st = J.get('statut') or 'revue_auto'; n = J['n']; rn = J['repartition_niveau']
            html = os.path.relpath(os.path.join(ssp_dir(s), f"{s['lot']}_{s['code']}_TypeA_Reflexe.html"), REV)
        else:
            st, n, rn, html = 'absent', 0, {}, ''
            if os.path.exists(os.path.join(ssp_dir(s), f"_bank_G{s['num']:02d}.py")): st = 'brouillon'
        cov = (len(dx) - len(gaps)) / len(dx) if (dx and J) else 0
        prog = W[st] * cov if J else 0
        rows.append(dict(ssp=s['code'], lot=s['lot'], titre=s['titre_fr'], n_q=n, ex=rn.get('examen', 0), ap=rn.get('approfondissement', 0),
                         spe=rn.get('specialiste', 0), dx_couverts=f"{len(dx)-len(gaps) if J else 0}/{len(dx)}", statut=st,
                         chemin_html=html, maj=now.strftime('%Y-%m-%d %H:%M'), _cov=cov, _prog=prog, _gaps=gaps if J else [k for k, _ in dx]))
    with open(os.path.join(REV, '_index', 'REGISTRE.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); keys = ['ssp', 'lot', 'titre', 'n_q', 'ex', 'ap', 'spe', 'dx_couverts', 'statut', 'chemin_html', 'maj']
        w.writerow(keys); [w.writerow([r[k] for k in keys]) for r in rows]
    livres = sum(1 for r in rows if r['statut'] in ('revue_auto', 'valide'))
    pond = sum(r['_prog'] for r in rows) / len(rows)
    nq = sum(r['n_q'] for r in rows)
    nxt = next((r for r in rows if r['statut'] in ('absent', 'brouillon')), None)
    incompl = [r for r in rows if r['statut'] in ('revue_auto', 'valide') and r['_gaps']]
    ic = {'absent': '⬜ à faire', 'brouillon': '🟨 brouillon', 'revue_auto': '🟦 revue_auto', 'valide': '🟩 validé'}
    L = ["# ÉTAT DES LIEUX — Questionnaires Type A « Réflexe SSP » · Temps 1 · catégorie G", "",
         f"_Régénéré par `_outils/scripts/etat_lieux.py` le {now:%Y-%m-%d à %H:%M} (Europe/Zurich, UTC+1) · seuil couverture : ≥ {nmin} EX par DX_", "",
         "## Relève Λ — en une ligne", "",
         f"- **Progression globale : {livres}/16 SSP livrés = {100*livres/16:.2f} %** · pondérée (statut × couverture DD) : **{100*pond:.1f} %** · {nq} questions au total.",
         f"- **Prochain SSP : {nxt['ssp']} ({nxt['lot']}) — {nxt['titre']}**" if nxt else "- Série G complète : passer à S (S_symptomes_systemes/).",
         "- **Blockers / dettes :** " + ("; ".join(f"{r['ssp']} : {len(r['_gaps'])} DX < {nmin} EX ({', '.join(r['_gaps'])})" for r in incompl) if incompl else "aucun gap de couverture sur les SSP livrés.")
         + " · Validation humaine (statut `valide`) : 0 SSP à ce jour.", "",
         "## Tableau G1–G16", "",
         "| SSP | LOT | Titre | Q | EX | AP | SPE | DX couverts | Statut | Progression | HTML |", "|---|---|---|---:|---:|---:|---:|---|---|---:|---|"]
    for r in rows:
        link = f"[ouvrir]({r['chemin_html']})" if r['chemin_html'] else "—"
        L.append(f"| {r['ssp']} | {r['lot']} | {r['titre'][:60]} | {r['n_q']} | {r['ex']} | {r['ap']} | {r['spe']} | {r['dx_couverts']} | {ic[r['statut']]} | {100*r['_prog']:.0f} % | {link} |")
    L += ["", "## Procédure pour le SSP suivant (5 commandes)", "", "```bash", "cd /workspace/grok/Revision",
          f"python3 _outils/scripts/init_ssp.py {nxt['ssp'] if nxt else 'G3'}          # canevas + checklist DD",
          "# rédiger _bank_GNN.py selon _outils/CHARTE_REDACTION.md (sources = LOT audité uniquement)",
          "python3 _outils/scripts/build_ssp.py G_symptomes_generaux/GNN_xxx   # JSON + HTML",
          "python3 _outils/scripts/couverture_dd.py G_symptomes_generaux/GNN_xxx  # 0 gap exigé",
          "python3 _outils/scripts/etat_lieux.py                                 # ce fichier", "```", "",
          "Légende statut : ⬜ absent · 🟨 brouillon (canevas/bank sans JSON) · 🟦 revue_auto (contrôles automatiques OK, pas de relecture humaine) · 🟩 validé (relu)."]
    open(os.path.join(REV, 'ETAT_DES_LIEUX_QCM.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(f"{livres}/16 livrés = {100*livres/16:.2f} % · pondéré {100*pond:.1f} % · {nq} Q · prochain {nxt['ssp'] if nxt else '—'}")

if __name__ == '__main__':
    main()
