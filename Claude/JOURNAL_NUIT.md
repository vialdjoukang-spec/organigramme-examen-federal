# JOURNAL_NUIT — Claude (mission LOT_043–071 + LOT_079, ordre de Vial du 10.11.2026)

- 01:40 · détection (327 branches) : LOT_043–071 et 079 absents partout ; consolidation de 218 leçons Claude → PR #514.
- 01:45 · correctif local : `outils/paquet.py` ne découpait pas les rubriques AIPS (espace en tête de ligne) → `Claude/_outils/lecon.py`.
- 02:30 · cause racine des doses « absentes » : liste HAM `zugelassene_packungen` sans les monopréparations courantes → liste élargie `erweiterte_ham_ind.xlsx` + préférence monopréparation.
- 02:45 · LOT_045 : P1–P3 franchies (11 ACCEPTE) → PR #524 ; revue Codex : Dafalgan 500 mg, clairance de la créatinine (corrigé).
- 02:57 · LOT_044 : P1–P3 franchies (11 ACCEPTE) → PR #525 ; revue Codex : fibrinolyse du STEMI (corrigé).
- 03:10 · BLOCAGE fusion : la protection de `main` exige 4 contrôles « expected » jamais publiés, et `auto-fusion.yml` n'agit que sur une autorisation technique (n° PR + SHA) inscrite dans `main` par Vial. PR #514, #524, #525 prêtes (CI verte, `audit-ok`), en attente de cette autorisation ou d'une fusion manuelle.
- 07:20 UTC · LOT_046 livré : PR #532 (11 leçons, 9 VERT/2 ORANGE, P3 + audit3), étiquette audit-ok ; fusion bloquée comme #514/#524/#525/#527 (autorisation technique absente). Limite d'usage 03:25–05:50 UTC : 15 agents interrompus puis relancés. LOT_048 en audit P3 ; LOT_050 liste en audit P1.
- 07:53 UTC · LOT_048 livré : PR #533 ; LOT_049 livré : PR #535 (11 leçons VERT, P3 + audit3, arbitrage salbutamol « AIPS prime » soumis à Vial). LOT_047 : second audit, corrections DX.5–DX.7 en cours. LOT_050 : 11 leçons VERT, audit P3 en cours. LOT_051 (S2.12) : liste DX en cours. Fusions toujours bloquées (autorisation technique).
- 07:58 UTC · LOT_047 livré : PR #537 (11 leçons VERT, P3 + audit3). LOT_050 : 11 leçons en correction P3 (nombreux AIPS déclarés à tort absents ; brief renforcé). LOT_051 : liste gelée (audit P1 : néoplasie pariétale ajoutée, péricardite retirée), rédaction des 11 leçons lancée.
