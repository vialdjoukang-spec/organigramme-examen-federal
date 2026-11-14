# Audit radiologique V2 : vérification des corrections IMG-219 à IMG-237 (14.11.2026)

Méthode : j'ai lu `CORRECTIONS_IMAGES_219_237.md`, les champs `images` de `AB.json` et les copies `_verif` régénérées de 221 et 235. J'ai relu la légende et la licence de PMC7200970 dans le XML Europe PMC.

**Verdict : corrections requises.** Il reste un seul patch, sur une définition mal énoncée au 221 (§ 2). Les 3 majeurs et les mineurs de V1 sont corrigés.

## 1. Contrôles

| id | Contrôle | Statut |
|---|---|---|
| 221 | J'ai vérifié la nouvelle image : PMC7200970 fig. 16c, licence CC BY 4.0 dans le XML, légende « cystic renal mass with septae nodularity… considered to be a Bosniak IIIn cyst ». Le rendu montre une masse kystique traversée par une cloison épaisse et nodulaire ; la pointe du repère touche la nodularité, sous la flèche des auteurs. **Classe montrée** : « IIIn » appartient à la sous-classification proposée par les auteurs, et non au Bosniak 2019 officiel. Selon le Bosniak 2019, une protrusion rehaussée de 4 mm ou plus à angle obtus est un **nodule, donc une classe IV** ; une irrégularité de 3 mm ou moins relève de la classe III. Le texte « Bosniak III à IV » est donc juste et prudent. Le kyste simple (Bosniak I) est demandé comme normal dans `a_chercher`. | corrigé |
| 235 | `technique` porte « AAA rompu ». Le repère 3 (58 ; 50) tombe dans l'infiltration hématique para-aortique gauche, qui efface la graisse. Les textes des repères 1 et 2 sont conformes. Un normal est demandé dans `a_chercher`. | corrigé |
| 237 | La forme non athéromateuse est déclarée dans `technique`. La forme typique est demandée dans `a_chercher.patho`. | corrigé |
| 225 | Le repère (33 ; 54) est au centre de la masse. La photographie d'écran teintée est déclarée. | corrigé |
| 233 | La `semio` cite l'IR de 0,58 et l'onde tardus-parvus du pôle supérieur, comme la légende. | corrigé |
| 220, 224, 226, 228 | Contextes et limites ajoutés dans `technique` ou `semio`. | corrigé |

## 2. Patch restant (mineur)

| id | Défaut | PATCH exact |
|---|---|---|
| 221 `patho.technique` | La parenthèse « III si cloison ≥ 4 mm irrégulière rehaussée, IV si nodule rehaussé » fusionne deux critères distincts et ne définit pas le nodule. | Remplacer la parenthèse par : « Bosniak 2019 : III = paroi ou cloison rehaussée épaisse (≥ 4 mm) ou irrégulière (protrusion ≤ 3 mm à angle obtus) ; IV = nodule rehaussé (protrusion ≥ 4 mm à angle obtus, ou de toute taille à angle aigu) ». |

Une fois ce remplacement appliqué, le verdict passe à **audit-ok**.

## Clôture
Patch 221 (définitions Bosniak 2019) appliqué mot pour mot : **audit-ok** pour IMG-219 à 237.
