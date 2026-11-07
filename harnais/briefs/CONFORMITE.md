# Brief type — audit de conformité d'un fichier Phase B (second audit)

Paramètres donnés dans l'appel : LOT, N (numéro du DX).
1. Lis `lot en cours de production/<LOT>/BRIEF_AUDIT_B.md` et applique-le pour N.
2. Lance `python3 harnais/audit_langue.py "lot en cours de production/<LOT>/<LOT>_Phase_B_V0_DX.<N>.html" --json` et pars de ses alertes.
3. L'audit médical est fait : ne touche à aucun chiffre, dose, seuil ou conduite, sauf contradiction interne évidente (à consigner).
4. Contrôles : phrases verbales courtes ; abréviations développées à la première occurrence ; 14 points présents et bien affectés ; points 1, 5, 6, 7, 10, 13, 14 ; `<h2>` mot pour mot selon `LISTE_DX_CANONIQUE.md` ; cohérence avec la Phase A ; fenêtres popover (bouton dans la phrase, div après le `</p>`, bouton Fermer avec `popovertargetaction="hide"` — ne jamais le retirer) ; aucun JavaScript ni `title=` ; aucune espace insécable ; balises `</td></tr></th>` conservées ; sources datées ; FIN_FICHIER intact ; 80 000–140 000 octets (compresse la forme si tu ajoutes).
5. Journaux : `LOT_Claude_Finaux/<LOT>/audits/corrections.jsonl` (type ∈ {dose, seuil, critère, conduite, source, omission, langue, format} ; gravite ∈ {critique, grave, moyen, léger}) et une ligne dans `scores.jsonl`.
6. Aucun téléchargement, aucun commit. Fin : `controle_lot.py verifier … --sans-nom --json`, puis `rapport_qualite.py`. Réponse ≤ 10 lignes.
