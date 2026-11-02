# Contrelecture rédactionnelle ciblée — LOT 133 Phase A

Date : 02.11.2026. Lecteur : `astra_sources_a`. Fichier : `LOT_133_Phase_A_V0.html`. SHA-256 effectivement mesuré : `60d1fdf9b889cf36a6e46af3255bd1fe58ae73a397e4b87ecbd75fe6f3dfd5e1`.

**Verdict : rédaction recevable avec deux améliorations mineures actionnables ; aucun blocage rédactionnel identifié dans les points examinés.** Ce rapport ne vaut ni audit médical indépendant, ni validation du LOT, ni gel de la liste. Le lecteur a fourni des notes documentaires utilisées pour la rédaction, mais n’a pas écrit le cours HTML.

## Périmètre et méthode

Lecture ciblée des points 1, 5, 6, 7, 10, 13 et 14 : résumés visibles et infobulles correspondantes, tableau inclus au point 7. L’extracteur `cache_controles.py extraire --points 1,5,6,7,10,13,14` a retourné « Aucun point demandé retrouvé ; extraction impossible. » Une extraction locale en lecture seule, fondée sur les identifiants réels `a-pN` et `a-detailN`, a permis la contrelecture sans afficher le HTML entier. Une tentative avec BeautifulSoup a échoué faute de module ; extraction réalisée avec la bibliothèque standard. Aucun outil partagé ni HTML modifié. Les 20 conditions statiques vertes sont rapportées par root ; elles ne sont pas réexécutées ni transformées en constat médical ici.

## Constats

| Point | Résultat | Constat ou action précise |
|---|---|---|
| 1 | Conforme rédactionnellement | La population adulte est nommée dès l’entrée. La distinction entre constat et interprétation est directe ; le fait structurant est en gras dans l’infobulle. |
| 5 | Conforme rédactionnellement | Enchaînement clair : début, contexte, symptômes, retentissement, urgence. L’appel au 144 est visible en gras ; l’interrogatoire ne doit pas retarder les secours. |
| 6 | Amélioration mineure | « rechercher l’évolution du souffle » est ambigu dans un cours médical : le lecteur peut comprendre un souffle auscultatoire. Préférer « rechercher l’évolution de l’essoufflement » si tel est bien le sens voulu par l’auteur. |
| 7 | Conforme rédactionnellement | Le tableau sépare indice, bilan, confirmation et priorité. La population adulte, la sélection pédagogique et l’absence de classement de fréquence sont explicites. Les limites figurent auprès des hypothèses. |
| 7 | Amélioration mineure | « Ils illustrent trois problèmes de couleur, volume ou mouvement » peut laisser croire à trois problèmes précis. Préférer « Ils illustrent des anomalies de couleur, de volume ou de mouvement ». |
| 10 | Conforme, avec même ambiguïté lexicale | Les branches commencent par une condition et débouchent sur une action. Remplacer éventuellement « une aggravation du souffle » par « une aggravation de l’essoufflement », en cohérence avec le point 6. |
| 13 | Conforme rédactionnellement | La restitution clinique donne un constat, une hypothèse et une action ; la phrase en gras rappelle correctement la portée limitée d’un examen partiel sur le plan rédactionnel. |
| 14 | Conforme structurellement | Quatorze éléments `details.quiz` et quatorze `summary` effectivement comptés ; chaque question comporte une réponse. Les questions sont explicitement pédagogiques et non officielles. |
| Gras | Conforme sur le périmètre | Le gras souligne des décisions ou limites structurantes, particulièrement l’urgence neurologique, les limites de l’inspection et les étapes conditionnelles. Les résumés visibles restent brefs et les infobulles portent les développements. |

Les deux améliorations proposées sont lexicales : elles n’autorisent aucune modification du fond médical sans l’auteur. Les formulations elliptiques du tableau restent compréhensibles ; aucune faute de langue bloquante relevée sur le périmètre. Aucune correction appliquée au HTML. Toute modification ultérieure change l’empreinte de la version examinée.
