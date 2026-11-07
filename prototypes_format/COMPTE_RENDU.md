# Compte rendu — quatre versions de DX.10 « Maladie d'Addison » (LOT_016)

Relevé du 30.10.2026. Mesure : **T = x Ko (+ y Ko)**, où x est le texte de la fiche lue d'un trait et y le texte de toutes les fenêtres et de tous les dépliants, qu'on n'ouvre que si l'on veut en savoir plus. Les Ko comptent le texte visible seulement (hors balises et style) ; la taille du fichier HTML est donnée à part. Lecture à 180 mots par minute. Notes : auditeur médical indépendant, même barème pour tous (`NOTATION.md`).

## 1. Mesures

| Version | Fichier | **T = x (+ y)** | Fenêtres | Dépliants | Lecture de la fiche | Examen /100 | PEC /100 | Lisibilité /100 | Erreurs créées |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Original (production) | 139 Ko | **21,8 (+ 91,9)** | 36 | 0 | 16 min | 97 | 99 | 58 | — |
| V1 sans redondance | 99 Ko | **25,8 (+ 54,8)** | 33 | 6 | 21 min | 97 | 97 | 86 | aucune |
| V2 cours court | 45 Ko | **13,4 (+ 18,2)** | 17 | 7 | 12 min | 85 | 93 | 79 | 2 (estrogènes ; définition) |
| V3 choix de l'expert | 96 Ko | **29,4 (+ 46,7)** | 26 | 18 | 24 min | 98 | 96 | 88 | 3 mineures (1 mot AIPS, 2 liens de cause inventés) |
| V4 la plus légère | 24 Ko | **9,4 (+ 7,0)** | 6 | 10 | 8 min | 77 | 82 | 80 | 4 (dont 1 dose contredisant l'AIPS) |

## 2. Chaque version jugée selon son propre contrat

**Original.** Contrat de production : tout dire, 80–150 Ko. Le fond est excellent (97/99), mais la lecture est pénible (58) : la fiche est faite de fragments nominaux et l'essentiel du savoir (92 Ko) est enfoui dans 36 fenêtres très lourdes, sans hiérarchie. *Contrat tenu sur le fond, échoué sur la lecture.*

**V1 — retirer la redondance avec la Phase A, < 100 Ko.** Contrat tenu : 99 Ko, aucune perte de note (97/97), aucune erreur créée, lisibilité +28 points. Mais la fiche est la plus longue à lire (21 min) : retirer la redondance ne suffit pas à rendre la fiche légère, car le texte principal garde trop de détails qui auraient leur place en fenêtre. *Contrat tenu ; ce n'est pas le compromis cherché.*

**V2 — taille minimale pour 90/90.** Contrat non tenu : 85 à l'examen. La fiche est légère (13,4 Ko, 12 min) et agréable, mais les fenêtres sont trop pauvres (18 Ko) : des notions d'examen ont disparu (tableau des différentiels, causes, détails du Synacthène), et le résumé a créé deux erreurs. *Bonne fiche, fenêtres insuffisantes.*

**V3 — choix de l'expert.** Meilleure version : 98/96, lisibilité 88. Elle utilise le plus de dépliants (18), notamment les 14 pièges en question/réponse, et un schéma de l'axe corticotrope. Sa fiche reste cependant lourde (29,4 Ko, 24 min) et trois petites fautes demandent correction. *Contrat tenu ; référence de qualité.*

**V4 — le plus petit possible avec le maximum de notions.** Contrat non tenu : 77/82. Le total (9,4 + 7,0 = 16 Ko de texte) est sous le seuil où les notions d'examen et les décisions cliniques tiennent ; la compression a produit quatre erreurs, dont une dose de chirurgie (40 mg) qui contredit l'AIPS de Solu-CORTEF®. *Démontre la limite basse.*

## 3. Ce que montrent les chiffres

1. **La note dépend du total x + y, pas de la fiche x.** Les versions à 95 et plus ont 76 à 114 Ko de texte au total ; V2 (32 Ko) et V4 (16 Ko) chutent. La couverture de 95 à 100 % des notions exige donc environ 70 à 80 Ko de texte au total pour ce chapitre.
2. **La lecture dépend de x, pas du total.** La fiche la plus agréable n'est pas la plus courte : V3 (29 Ko) lit mieux que V4 (9 Ko) parce qu'elle explique avec des phrases liées. Mais au-delà d'environ 20 Ko de fiche, le temps de lecture dépasse 15 minutes et décourage.
3. **Comprimer le fond crée des erreurs ; déplacer le fond en fenêtre n'en crée pas.** V2 et V4 ont résumé (erreurs) ; V1 et V3 ont déplacé (pas d'erreur de fond).
4. **Le bon compromis n'existe dans aucune des quatre versions** : il faut la fiche de V2 et les fenêtres de V3.

## 4. Conclusion et norme proposée

**Compromis optimal pour un diagnostic différentiel : T ≈ 15–20 Ko (+ 45–55 Ko).**
- **Fiche x ≤ 20 Ko de texte (≈ 12–15 minutes de lecture)** : les 14 parties en paragraphes courts, grammaticalement corrects, reliés par des connecteurs ; chaque partie dit ce qui est spécifique au diagnostic et ce qu'il faut faire, sans le détail.
- **Fenêtres et dépliants y ≈ 45–55 Ko** : principe et interprétation des examens avec tableaux, doses complètes et citations AIPS mot pour mot, critères, causes, rappels d'anatomie et de physiologie, pièges en question/réponse dépliable. Chaque notion approfondie a son mot cliquable dans la fiche.
- **Prise en charge** : dans la fiche, la conduite complète en phrases (quoi, quand, combien en résumé) ; dans la fenêtre, le détail opposable (doses par âge, voies, durées, contre-indications).
- **Aucun résumé de fond** : on déplace en fenêtre, on ne compresse pas. Toute version réduite passe un second audit médical.
- **Cible de note** : ≥ 95 à l'examen et ≥ 95 en prise en charge ; lisibilité ≥ 85.
- **Cours de Phase A** : 100 Ko au plus de fichier, même règle x (+ y).

Prochaine étape proposée : une **V5** construite exactement sur cette norme (fiche de V2 réécrite, fenêtres de V3 corrigées), notée avec le même barème, puis adoptée comme modèle de production pour Claude, Codex et Grok.
