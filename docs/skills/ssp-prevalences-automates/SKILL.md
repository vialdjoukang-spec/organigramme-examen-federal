---
name: ssp-prevalences-automates
description: Rechercher les fréquences CH/Europe par catégorie SSP, afficher les jauges ou reprendre la file de l’agent statistique.
---
1. Pour « jauges prévalences » : `python3 tools/prevalences/jauges.py --distant` ; ajouter `--secteurs` pour les 19 secteurs.
2. Pour lancer : `gh workflow run prevalences-recherche.yml --ref main -f limite=8`. Localement : `python3 tools/prevalences/g.py --limit 40` (option correcte avec espace : `--limit 40`), analogues s/f/o. Les catégories réelles sont G,S,F,O.
3. Lire `docs/prevalences/README.md`, l’état sur branche `automates/prevalences` et les erreurs. Un échec API ne vaut jamais absence de résultat. Les SSP sans DD restent comptés séparément.
4. Audit : contrôle mécanique `auditeur.py`, puis agent distinct selon `docs/prevalences/AUDITEUR_STATISTIQUE.md`. Source réelle, population, pays, diagnostic et dénominateurs relus ; corrections avant/après. Ne pas compter une relance comme une exécution.
5. Aucun candidat ne fait monter la couverture clinique. Admission des chiffres par PR de données avec sources datées, audit, builders et CI verts ; aucune écriture directe ni validation médicale inventée.

6. Sélection : lire `selection.py` et `sources_reconnues.json`. Identité éditoriale vérifiée, méthode/biais attestés, comparabilité explicite puis plus grand N analysé à qualité équivalente. Aucun mélange de populations ni validation clinique automatique.
7. Synthèse : `jauges.py --distant --output work/synthese` produit erreurs.json et erreurs.pdf. Préserver le journal antérieur ; absences archivées distinctes des corrections prouvées. PDF public : prevalences-erreurs.pdf.

8. Coordination8/9 : `python3 tools/coordination/calculer.py --output work/coordination` ; `relance.py --plan work/coordination/priorites.json` observe sans lancer. La veille GitHub contrôle toutes les10min, espace les recherches de4h et limite à2 diagnostics/catégorie si la file documentaire atteint200. La monographie est partagée par diagnostic ; la prévalence reste liée à SSP#index+empreinte. `--lancer` seul autorise un dispatch ; ni commentaire ni succès technique ne prouvent l’exécution d’un agent.
