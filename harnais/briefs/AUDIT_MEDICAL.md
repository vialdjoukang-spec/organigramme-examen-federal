# Brief type — audit médical d'un fichier Phase B (premier audit)

Paramètres donnés dans l'appel : LOT, N, et les points d'attention signalés par le rédacteur.
1. Lis `lot en cours de production/<LOT>/BRIEF_AUDIT_B.md` et applique-le pour N ; hérite de `CORRECTIONS_AUDIT.md`.
2. Lance `python3 harnais/audit_langue.py "<fichier>" --json` pour la forme ; concentre ton effort sur le fond.
3. Vérifie chaque dose, contre-indication, grossesse et allaitement mot pour mot dans l'AIPS (corpus `.cache/aips/AipsDownload_20261008.xml`, extraits `.cache/aips/<n°>.txt`) ; usage hors information professionnelle écrit en clair ; conduite d'urgence sûre et sourcée.
4. Ne retire jamais `popovertargetaction="hide"` ; aucune espace insécable ; ≤ 140 000 octets.
5. Journaux : `LOT_Claude_Finaux/<LOT>/audits/corrections.jsonl` (type ∈ {dose, seuil, critère, conduite, source, omission, langue, format} ; gravite ∈ {critique, grave, moyen, léger}) et une ligne dans `scores.jsonl`.
6. Extraits de nouvelles sources : dans ton sous-dossier du scratchpad ; signale-les dans ta réponse pour la passe transversale. Pas de commit. Réponse ≤ 10 lignes.
