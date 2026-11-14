# Stratégie et état (2026-11-14 01:17 Europe/Zurich)

## État
- 32 manifests validés, 0 erreur : 24 complets et 8 partiels. Il en reste 312 en recherche.
- Le travail s'est arrêté faute de crédit d'usage. Il reprend en lisant `harnais/HARNESS.md` et `harnais/memory/journal_lot*.md`.
- Images, cache et manifests produits : sur la machine de travail, dans `/workspace/radio/`. Ils ne sont pas versionnés ici.

## Risques et réponses
1. **Flèche mal placée.** C'est le risque principal.
   - Réponse : une échelle de confiance, la preuve citée pour chaque flèche, et une relecture visuelle par l'auditeur.
   - Faille connue : `validate.py` ne contrôle pas la position anatomique des flèches.
2. **Appariement imparfait** (sujet, fenêtre, temps différents). L'écart est écrit dans `pair_match`, jamais masqué.
3. **Licences.** Seules les licences de la liste blanche sont acceptées. Radiopaedia est exclu, car sa licence est non commerciale.
4. **Poids de l'app.** Environ 50 Mo si toutes les images sont embarquées ; `build_app.py --external` évite cela.
5. **Open-i** sert des images de 512 px au maximum.

## Optimisations proposées
- Auditeur indépendant par lot, dès la reprise.
- Ajouter à `validate.py` la règle inverse : toute confiance `basse` doit apparaître dans `a_verifier`.
