# Démarrage de CODEX — 5 minutes

1. Lis `codex-LOTS-html/PROMPT_CODEX.md` en entier, puis `PROMPT_PRODUCTION_V2.md`.
2. Branche : `git fetch --all && git checkout -b codex/lots origin/production-v2` (ou `git checkout codex/lots` si elle existe).
3. Registre (bloquant) : `python3 codex-LOTS-html/registre_ia.py lire codex`, puis `signer codex <jeton>`, puis `installer codex`.
4. Premier LOT : le premier « LIBRE » de ta plage dans `codex-LOTS-html/REGISTRE.md` ; `python3 codex-LOTS-html/registre_ia.py verifier codex LOT_XXX` doit répondre AUTORISÉ.
5. Ressources hors ligne : `ressources_ia/README.md` (AIPS complète, listes Swissmedic, liste des spécialités). Exemple : `python3 ressources_ia/outils/aips.py chercher Mestinon` puis `lire 19943 grossesse`.
6. Modèle de qualité : `LOT_Claude_Finaux/LOT_016/` (structure seulement) ; leçons : `lot en cours de production/LOT_017/LECONS_LOT_016.md`.
7. Contrôle de chaque fichier : `python3 harnais/controle_lot.py verifier codex-LOTS-html/LOT_XXX --sans-nom` et `python3 harnais/audit_langue.py <fichier> --json`.
8. Fin de session : `python3 codex-LOTS-html/registre_ia.py etat`, commit, `git push -u origin codex/lots`.
