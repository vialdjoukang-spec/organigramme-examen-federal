---
name: ssp-prevalences-automates
description: Rechercher les fréquences CH/Europe par catégorie SSP, afficher les jauges ou reprendre la file de l’agent statistique.
---
1. Pour « jauges prévalences » : `python3 tools/prevalences/jauges.py --distant` ; ajouter `--secteurs` pour les19 secteurs.
2. Pour lancer : `gh workflow run prevalences-recherche.yml --ref main -f limite=40`. Localement : `python3 tools/prevalences/g.py --limit 40` (option correcte avec espace : `--limit 40`), analogues s/f/o. Les catégories réelles sont G,S,F,O.
3. Lire `docs/prevalences/README.md`, l’état sur branche `automates/prevalences` et les erreurs. Un échec API ne vaut jamais absence de résultat. Les SSP sans DD restent comptés séparément.
4. Audit : contrôle mécanique `auditeur.py`, puis agent distinct selon `docs/prevalences/AUDITEUR_STATISTIQUE.md`. Source réelle, population, pays, diagnostic et dénominateurs relus ; corrections avant/après. Ne pas compter une relance comme une exécution.
5. Aucun candidat ne fait monter la couverture clinique. Admission des chiffres par PR de données avec sources datées, audit, builders et CI verts ; aucune écriture directe ni validation médicale inventée.
