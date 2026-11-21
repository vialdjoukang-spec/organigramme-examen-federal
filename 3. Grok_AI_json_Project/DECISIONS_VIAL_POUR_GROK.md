# Décisions de Vial en réponse aux points soulevés par Grok

## 1. Emplacement de travail
- Grok n'écrit pas dans `Grokbot/`.
- Il écrit dans `3. Grok_AI_json_Project/SSP_nnn/source_json/` sur la branche `main`.
- Les brouillons déjà produits sur le PC de Vial sont maintenant dans le dépôt : SSP_246, SSP_236, SSP_247, SSP_240, SSP_034, SSP_035.
- SSP_248 et SSP_157 ne contiennent que leur `NOTIONS.json` : rien n'est rédigé.

## 2. Portée du rapport « 248/248 PASS »
- Grok a raison : ce rapport valide uniquement la préparation des plans, pas le contenu médical.
- La seule validation de contenu valable est `python _outils/verif_source_json.py <n>`.

## 3. État réel
- Voir `ETAT_AVANCEMENT.md`, généré par `verif_source_json.py`.
- SSP_236 (17/17) et SSP_240 (16/16) sont terminés.
- SSP_246, SSP_247, SSP_034 et SSP_035 sont partiels : fichiers manquants ou en échec listés dans ce fichier.
- Ne pas réécrire les fichiers déjà en PASS.

## 4. Ordre de reprise
1. Fichiers en échec puis manquants de SSP_246 (premier manquant : `DX.8`).
2. Même démarche pour SSP_247, SSP_034, SSP_035.
3. SSP_248 puis SSP_157.
4. Suite du classement `GEMINI_word_à_générer/00_CLASSEMENT_GRAVITE_248_LOTS.json`.

## 5. Mise en route des outils (une seule fois)
- `python _outils/preparer_outils.py` décompresse `cartographie_DATA.json.gz`.
- Puis `python _outils/verif_source_json.py 246`.
- Le dossier `3. Grok_AI_json_Project/` joue le rôle de `1_Claude AI/` : il contient `_outils/` et `SSP_nnn/`.

## 6. Rappel
- Grok fait d'abord un résumé complet du projet.
- Il attend la validation de Vial avant de rédiger.
