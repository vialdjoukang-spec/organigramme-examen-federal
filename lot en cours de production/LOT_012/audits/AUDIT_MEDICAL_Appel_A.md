# Audit médical correcteur — Appel A LOT_012

Auditeur : agent distinct du rédacteur. L’auto-audit du 25.10.2026 signé « même agent que le rédacteur » est **invalidé** et remplacé par ce rapport.

Date : 2026-10-25, 18:19 Europe/Zurich.

Fichier : `LOT_012_Appel_A_V7_Plan_et_Liste.html`.

`tools/cours/lots/G12.json` et `data/ck/prev.json` ne sont pas modifiés. Aucune dose médicamenteuse n’a été inventée.

## Score d’application du prompt (section 6.3)

Une seule monographie est notée : le chapitre 1 (quatorze parties du SSP). Le bloc 2 est une liste d’ancrages, pas dix monographies ; ses questions de monographie complète sont sans objet, avec renvoi à l’Appel B.

Cinquante questions, maximum 100. Points obtenus : 77.

| Point | Obtenu / max | Motif des 1 ou des 0 |
|---|---|---|
| 1 | 5/6 | Fenêtres encore pauvres sur la définition de la plainte. |
| 2 | 5/8 | Pas de distribution suisse de la plainte ; histoire naturelle et enjeux encore courts. Les chiffres de tête cardiaque et veineux sont maintenant datés. |
| 3 | 10/10 | Tableau lésion → exploration → conduite ajouté. |
| 4 | 4/4 | Graves nommées avant le fréquent. |
| 5 | 4/4 | Drapeaux actionnables. |
| 6 | 3/4 | La technique de chaque signe n’est pas partout écrite. |
| 7 | 6/10 | Syndromes non éclatés signe par signe dans ce chapitre. |
| 8 | 3/4 | Critères de certitude inégaux selon la cause. |
| 9 | 7/12 | Pas un tableau d’interprétation pour chaque examen. |
| 10 | 2/2 | Démarche en trois temps, complétée plus loin par l’algorithme. |
| 11 | 22/30 | Doses AIPS non ouvertes ; grossesse, enfant, foie, rein et sortie restent partiels. |
| 12 | 2/2 | Trois niveaux présents. |
| 13 | 2/2 | |
| 14 | 2/2 | |

**Score du fichier : 77 %.** Zéro erreur critique restante. Le seuil de dépôt de 90 % n’est pas atteint : l’Appel A reste un plan, pas une monographie V8 riche.

## Corrections

### Grave — corrigée

1. **Fichier** `LOT_012_Appel_A_V7_Plan_et_Liste.html`, chapitre 1 et DX.2.
   **Extrait** : « Le repère ambulatoire NT-proBNP<125ng/L vient d’ESC en2021. ESC en2026 distingue des seuils ambulatoires de probabilité ajustés à l’âge, dont les bornes exactes restent À vérifier ici » et « prévalence d’environ 1–2 % ».
   **Correction** : l’ESC 2026 (European Heart Journal, 28.08.2026, doi 10.1093/eurheartj/ehag100), lue le 25.10.2026, estime la prévalence entre 1 et 3 % des adultes, 12 à 58 pour 1 000 en Europe, incidence brute 2 à 13 pour 1 000 personnes-années. En ambulatoire, l’insuffisance cardiaque est probable dès 125 ng/L avant 50 ans, 250 ng/L entre 50 et 75 ans, 500 ng/L après 75 ans. En décompensation, l’exclusion non ajustée à l’âge reste inférieure à 300 ng/L. Le seuil unique de 125 ng/L de 2021 n’est plus le chiffre de tête.
   **Source** : [S8].

2. **Fichier** même HTML, DX.10 et repères biologiques.
   **Extrait** : « autour de 3–3,5 g/24 h » et « ≈300 mg/mmol, non 300 mg/g », sans le seuil KDIGO.
   **Correction** : KDIGO 2021, protéinurie supérieure à 3,5 g/24 h et albuminémie inférieure à 30 g/L. Le rang apparié publié avec ces définitions est d’au moins 300 mg/mmol, soit au moins 3 000 mg/g. Le seuil 300 mg/g n’est pas ce rang. La zone 3 à 3,5 g reste un héritage de lecture partielle.
   **Source** : [S9].

### Moyen — corrigée

3. Tableau de corrélation du point 3 absent. Ajouté (veine, cœur, néphrotique, lymphe), sans dose.
4. Phrase de sortie et de volet social absente au point 11. Ajoutée, avec le critère de congestion de l’ESC 2026 pour la décompensation et un « non trouvé » explicite pour le reste. [S8]
5. En-tête qui disait que les quatorze points des DX « attendent l’Appel B », alors que l’Appel B est rédigé. Phrase alignée.

### Léger — laissé, signalé

Espaces collés hérités du JSON canonique (`dihydropyridines5–15 %`, `après70ans` dans des puces non réécrites). Le JSON n’est pas modifié. Les phrases médicales corrigées ont retrouvé leurs espaces.

## Ce qui tenait déjà

C3 groupé 8 % et C2 européen 21 % : relus sur le texte ESVS 2022 le 25.10.2026. Dispersion de Bonn 1,1–14,9 % et godet 13,4 % : la revue secondaire était déjà qualifiée comme telle. Refus du mot « pathognomonique » pour le signe de Stemmer. Refus de 300 mg/g comme seuil suisse. Aucune dose en milligrammes de médicament. Rangs 3 à 10 marqués À vérifier. Wells ≥ 2 pour la branche TVP probable est celui du lot ; NICE NG158 n’a pas été rouvert (accès auparavant refusé).

## Critique restante

Aucune.

## HELP

1. LOT_012, Appel A, plainte, point 2. Aucune répartition suisse des causes d’œdème devant la plainte n’a été lue. Question : existe-t-il une série OFS, SSMIG ou hospitalière suisse ? Déjà cherché : ESVS 2022, ESC 2026, Revue du Praticien, Bonn via revue secondaire.
2. LOT_012, Appel A, point 11. Doses AIPS du furosémide, de la spironolactone et des bas. swissmedicinfo.ch n’a pas été ouvert dans cette session. Aucun numéro Swissmedic n’est déduit.
3. NICE NG158 : relecture impossible si l’accès reste en échec. Les délais de 4 h et de 24 h ne sont pas une règle suisse.

## Décision

Appel A corrigé sur les chiffres dangereux. Score 77 %, zéro critique. Pas un feu vert de dépôt Finaux au sens du seuil 90 %.
