# Audit radiologique V2 : vérification des corrections IMG-289 à IMG-344 (14.11.2026)

Méthode : j'ai lu `CORRECTIONS_IMAGES_289_344.md` et les champs `images` de `MI_TR.json`, puis regardé les copies `_verif` régénérées de 304, 326, 337, 338 et 340.

**Verdict : audit-ok.**

| id | Contrôle sur le rendu | Statut |
|---|---|---|
| 340 | Le repère 3 (82 ; 34) est désormais sur le cliché des membres inférieurs, à la métaphyse tibiale proximale, contre la flèche des auteurs. Il ne pointe plus le coude. | corrigé |
| 326 | L'étiquette « NORMAL » a disparu. Les panneaux A (référence à 0 mois) et B (6 mois) sont réunis dans le cliché patho, et la `technique` les déclare. Le repère (63 ; 81) est au centre de la lésion cible, sur le panneau B, entre les flèches. `manque_normal` est présent. | corrigé |
| 304 | Le repère 1 (30 ; 47) touche le trait oblique de la fibula à hauteur de l'interligne (Weber B). | corrigé |
| 337 | La `technique` déclare la lacération hépatique iatrogène et rappelle que la lecture eFAST est la même chez le polytraumatisé. | corrigé |
| 338 | Le correcteur a remplacé mon patch (66 ; 50) par (69 ; 55). **J'accepte cet écart** : sur le rendu, (69 ; 55) tombe dans la bande anéchogène entre la paroi latérale du VG et le péricarde, donc dans l'épanchement, alors que mon point touchait la paroi. | corrigé |

J'ai relu les autres mineurs (325, 323, 329, 341, 327) dans le JSON : ils sont appliqués. Plus aucun défaut ouvert sur ce lot.
