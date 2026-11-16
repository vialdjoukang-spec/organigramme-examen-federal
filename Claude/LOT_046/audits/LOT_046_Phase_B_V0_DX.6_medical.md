# Audit médical — LOT_046_Phase_B_V0_DX.6.html

SHA-256 `2e0ee650c60a9287…`, 141224 octets. Points audités : 4, 8, 9, 10, 11 (Θ3). Score 60 % ; finale : **non**.

| Point | Note | 
|---|---|
| 4 | 2/2 |
| 8 | 1/2 |
| 9 | 2/2 |
| 10 | 1/2 |
| 11 | 0/2 |

Motif : Délai diagnostic-guide en centre d'angioplastie faux (90 au lieu de 60 minutes) ; aspirine sans son AIPS (Aspirine Cardio 51795 en cache du LOT) ; durées écrites en lettres ; dissection exclue après les antithrombotiques.

| Gravité | Point | Extrait (≤ 200 car.) | Correction | Source |
|---|---|---|---|---|
| Grave | 11 | En centre d'angioplastie, le fil doit franchir l'artère en moins de 90 minutes après le diagnosticw480b78-164. | En centre d'angioplastie, le fil doit franchir l'artère en moins de 60 minutes après le diagnostic, et en moins de 90 minutes après un transfertw480b78-164. | w480b78-164 |
| Grave | 11 | L'aspirine se débute par une dose de charge le plus tôt possible, puis se poursuit par une dose d'entretien quotidiennew480b78-198. | Dans l'infarctus aigu, Aspirine Cardio prévoit 200 à 300 mg par voie intraveineuse ou orale à résorption rapide, puis 100 mg par jour dès le deuxième jouraips-51795-4. | aips-51795-4 |
| Grave | 11 | La durée de la double antiagrégation plaquettaire vise douze mois, sauf contre-indicationw480b78-219. | La double antiagrégation plaquettaire est généralement recommandée pendant 12 mois, quel que soit le type de stent, sauf contre-indicationw480b78-219. | w480b78-219 |
| Grave | 11 | Elle prévoit ensuite 90 mg deux fois par jour pendant au moins douze moisaips-69596-4. | Elle prévoit ensuite 90 mg deux fois par jour pendant au moins 12 mois, sauf arrêt cliniquement indiquéaips-69596-4. | aips-69596-4 |
| Grave | 11 | Elle conseille un traitement de quinze mois, sauf arrêt cliniquement nécessaireaips-59136-2. | Elle conseille de poursuivre le traitement pendant 15 mois, sauf si l'arrêt est nécessaire du point de vue cliniqueaips-59136-2. | aips-59136-2 |
| Grave | 11 | Le prasugrel doit être arrêté au moins sept jours avant une opération programmée, si l'effet antiplaquettaire n'est pas souhaitéaips-59136-3. | Le prasugrel doit être interrompu au moins 7 jours avant une opération programmée, si l'effet antiagrégant plaquettaire n'est pas souhaitéaips-59136-3. | aips-59136-3 |
| Grave | 11 | Elle limite donc le traitement à trois jours au plus selon les données cliniquesaips-55459-4. | Selon les données cliniques, hémodynamiques et électrocardiographiques, elle limite la durée du traitement à 3 jours au plusaips-55459-4. | aips-55459-4 |
| Grave | 11 | La fibrinolyse préhospitalière réduit la mortalité précoce de 17 % si elle est administrée dans les deux premières heuresw480b78-185. | La fibrinolyse préhospitalière réduit la mortalité précoce de 17 %, surtout lorsqu'elle est administrée dans les 2 premières heures après le début des symptômesw480b78-185. | w480b78-185 |
| Grave | 8 | Un score supérieur à 140 définit donc un patient à haut risque, qui doit être considéré pour une coronarographie dans les vingt-quatre heuresw480b78-168. | Un score GRACE supérieur à 140 définit un patient à haut risque, chez qui une coronarographie dans les 24 heures doit être envisagéew480b78-179. | w480b78-179 |
| Grave | 9 | En effet, l'ESC distingue les stratégies selon le risque : immédiate pour le très haut risque, puis dans les vingt-quatre heures pour le haut risquew480b78-190. | L'ESC distingue les stratégies selon le risque : coronarographie immédiate pour le très haut risque, puis dans les 24 heures pour le haut risquew480b78-94. | w480b78-94 |
| Grave | 8 | Angiographie avant vingt-quatre heures | Angiographie avant 24 heuresw480b78-94 | w480b78-94 |
| Moyen | 8 | Une troponine négative ne suffit pas non plus à l'écarter si la douleur a débuté depuis moins de trois heures. | Supprimer | LV4 |
| Léger | 11 | Ainsi, une sortie dans les 72 heures ne provoque pas de surmortalité tardive chez les patients bien sélectionnésw480b78-296. | Une sortie dans les 72 heures ne provoque pas de surmortalité tardive chez les patients bien sélectionnésw480b78-296. | w480b78-296 |
| Léger | 11 | En effet, l'infarctus de type 2 n'a pas de traitement pharmacologique spécifique, et la prise en charge vise la cause déclenchantew480b78-361. | L'infarctus de type 2 n'a pas de traitement pharmacologique spécifique, et la prise en charge vise la cause déclenchantew480b78-361. | w480b78-361 |

Lacunes (HELP) :
- [Grave] Ajouter au paquet DX.6 les extraits aips-51795-0/-4/-5 (Aspirine Cardio, en cache _travail/PA, 2026-04-14), ajouter la ligne Aspirine Cardio (51795) au tableau 11.B.3 avec sa contre-indication ; le HELP DX.6 « aucune notice AIPS » est faux.
- [Grave] Monopréparations HAM disponibles et non lues : Beloc i.v. 56191 (métoprolol IV), Actilyse 48313, Metalyse 55418/69958, Morphin HCl Sintetica 51039 ; les lire avant tout chiffrage du point 11.
- [Moyen] Point 10 : placer la recherche de dissection (pouls et pressions aux deux bras) avant l'aspirine et l'héparine de la fenêtre Urgence, et non à l'étape 3.

Bilan : Grave 11, Léger 2, Moyen 1. Ce qui manque pour « oui » : appliquer les corrections Critique et Grave, puis relire les AIPS listées.
