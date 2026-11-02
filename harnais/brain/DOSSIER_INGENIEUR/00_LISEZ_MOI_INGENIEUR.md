# Dossier de l'ingénieur BRAIN-HARNESS (Opus 5.5 élevé)

Ordre de lecture : 05 (doléances de Vial) → 01 (Harness actuel) → 02 (Bracelet) → 03 (Grille 14 points) → 06 (Prompt ULTIME V8) → 04 (cumul des corrections des auditeurs, long) → 07 à 16.
Plan 3D actuel : `harnais/brain/PLAN_BRAIN_HARNESS_3D.html` (généré par `dessinateur.py` depuis `brain_spec.json` v2). Scriptones existants : `harnais/brain/scriptones/`.

## Mémoire clonée (état au 27.10.2026)
- LOT_001 à 012 : fusionnés sur main (162 cours). LOT_013 à 016 : non commencés. Correction de masse : en attente de l'ordre de Vial après livraison du chantier de l'ingénieur.
- Circuit : rédacteurs Sonnet 5.5 (Phase A, Phase B), auditeurs B1 à B5 (Opus 5.5 moyen, correcteurs), contracteur, contrôle de LOT, PR, CI, relecture Codex, fusion par commit de fusion.
- Pièges : un fichier devient « prêt » seulement après le `fin` du rédacteur ; auditeur d'un DD = celui du roster ; fichier bloqué → effacer `bloque/` et l'entrée `essais_NNN.json` ; ne jamais copier dans une PR un script dépendant de fichiers absents de main ; un auditeur a réinitialisé l'inventaire du contracteur pour obtenir un visa (à interdire sans trace).
- Constat : Atkinson jamais chargé ; le circuit n'a vu aucune des 8 doléances de forme ; le cerveau v1 en relève 23 à 32 par cours et réduit de 92 à 97 % les jetons d'une boucle de correction.

## Décisions de Vial (cahier des charges du chantier théorique)
Architecture validée, avec ces valeurs : 160 scriptones équivalents suffisent (au lieu de 500) ; le reste du plan est validé. Voir `00_CAHIER_DES_CHARGES.md`.
