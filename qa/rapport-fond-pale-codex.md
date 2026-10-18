# Revue ciblée #32 · Codex, 18.10.2026 UTC

Captures locales bureau (1366 × 860) et Pixel 7 examinées : fond #fbfbf8, surfaces blanches, titres et boutons lisibles, pas de sélecteur supplémentaire. Les polices locales et les contrôles actuels sont conservés.

Contrastes calculés depuis les couleurs résolues par Chromium : texte principal/fond 16,79:1, texte secondaire/fond 8,55:1, texte secondaire/carte 8,86:1, rouge critique/carte 7,31:1. Tous dépassent AA dans ces captures claires. Le workflow visuel reste obligatoire pour les autres états et thèmes ; aucune référence locale ni seuil remplacé par cette revue.

## Contrôle complet du 18.10.2026 UTC

60 captures locales avec Playwright 1.63.0 et axe-core 4.14.0 (empreinte identique à la CI). Trois thèmes, ordinateur et Pixel 7. Mesures : aucun débordement, aucun texte coupé, aucune erreur JavaScript ou police en échec ; CLS maximal 0,0358 ; aucune hausse de problème axe grave ou critique face à la référence. Les problèmes hérités restent présents : aucune conformité intégrale AA n’est revendiquée. Écarts examinés sur calendrier clair mobile et fenêtre dorée ordinateur, puis rendu clair ordinateur et sombre mobile : fond/carte et espace des contenus conformes à l’intention. La nouvelle référence reste nécessaire, sans modification de seuil.

Le téléchargement des deux artefacts GitHub échoue en HTTP 403 depuis cet environnement. Une entrée manuelle `adopter_pr` du workflow existant permet d’exécuter le même `tools/visuel_reference.sh` sur un runner GitHub après examen. Le job vérifie le numéro, la branche, la base main et l’identité exacte du SHA avant écriture ; il exige toujours le label, une exécution Visuel terminée et le script habituel. Il pousse uniquement la branche de PR. Les contrôles après adoption restent obligatoires ; aucun contournement de protection.
