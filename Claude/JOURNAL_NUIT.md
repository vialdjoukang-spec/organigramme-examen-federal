# JOURNAL_NUIT — Claude (mission LOT_043–071 + LOT_079, ordre de Vial du 10.11.2026)

- 01:40 · détection (327 branches) : LOT_043–071 et 079 absents partout ; consolidation de 218 leçons Claude → PR #514.
- 01:45 · correctif local : `outils/paquet.py` ne découpait pas les rubriques AIPS (espace en tête de ligne) → `Claude/_outils/lecon.py`.
- 02:30 · cause racine des doses « absentes » : liste HAM `zugelassene_packungen` sans les monopréparations courantes → liste élargie `erweiterte_ham_ind.xlsx` + préférence monopréparation.
- 02:45 · LOT_045 : P1–P3 franchies (11 ACCEPTE) → PR #524 ; revue Codex : Dafalgan 500 mg, clairance de la créatinine (corrigé).
- 02:57 · LOT_044 : P1–P3 franchies (11 ACCEPTE) → PR #525 ; revue Codex : fibrinolyse du STEMI (corrigé).
- 03:10 · BLOCAGE fusion : la protection de `main` exige 4 contrôles « expected » jamais publiés, et `auto-fusion.yml` n'agit que sur une autorisation technique (n° PR + SHA) inscrite dans `main` par Vial. PR #514, #524, #525 prêtes (CI verte, `audit-ok`), en attente de cette autorisation ou d'une fusion manuelle.
