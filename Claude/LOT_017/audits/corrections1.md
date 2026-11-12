# LOT_017 — corrections de l'audit 1 (A et B), 11.11.2026

Contrôles finaux : `controle3 --script-ok` VERT sur les 11 fichiers ; `verif_aips.py` OK partout (aucun BLOQUANT ; 2 alertes « dose absente » préexistantes en DX.3 et DX.5) ; tailles hors images 105 530 à 149 865 o ; liens internes et inter-fichiers vérifiés.

## Défauts → décision

| Fichier | Grav. | Défaut | Décision |
|---|---|---|---|
| DX.10 | Grave | Nimodipine : plafond 1 mg/h omis (fiche) | **Appliqué.** AIPS 48153 relue sur refdata : « Par la suite, la dose ne devrait pas dépasser 1 mg/heure ». |
| DX.10 | Grave | Même plafond omis en question 14 | **Appliqué.** |
| Phase A | Grave | Fiches .mb recopiées (pyridostigmine, prednisone, méthylprednisolone, IgIV, téprotumumab) | **Appliqué.** Indication AIPS + lien vers la fiche DX (DX.4, DX.5, DX.7). Fait unique gardé : IgIV dans le Guillain-Barré (AIPS 0,4 g/kg × 5 j, EAN/PNS 2023). |
| Phase A | Moyen | Point 1 non limité à la définition | **Appliqué.** Restent les définitions (diplopie, ptosis gradué, mouvements anormaux). Déplacés : strabisme latent 70 % → point 2 ; classification de Finsterer → point 3 ; plainte du ptosis et amblyopie → point 5 ; piège du ptosis complet → fenêtre paupières du point 6. Retirés comme redites : test d'occlusion (déjà aux points 5 et 7), SSO/SSML (déjà aux points 6 et 12), tableau des mécanismes (déjà au point 3), définition EFNS de la myasthénie (point 8 et DX.4), Kremmyda (algorithme et DX.4). |
| DX.1 | Moyen | Point 1 : notions voisines | **Appliqué.** Lignes dermatochalasis et blépharochalasis, piège blépharoplastie et phrase des causes retirés du point 1. La blépharochalasis était unique : elle passe dans le tableau du point 4. |
| DX.2 | Moyen | Point 1 : liste de termes | **Appliqué.** |
| DX.5 | Moyen | Point 1 : terminologie | **Appliqué.** Phrases syndrome de Means et « ophtalmopathie » des AIPS retirées. La phrase de Jules-Gonin du paragraphe est gardée, car elle justifie le titre (« dysthyroïdienne »). |
| DX.6 | Moyen | Point 1 : fenêtre de termes | **Appliqué.** Déplacée au point 8 (`f-dx6-p8-termes`), avec un lien sur « critères de McDonald 2024 ». Phrase DIT retirée, car redite du point 8. |
| DX.1–DX.5, Phase A | Moyen | Formules « (déduction …) », « calcul dérivé », « recalculé par outil », « corpus AipsDownload », « fréquence non quantifiée » | **Appliqué.** 66 formules retirées, avec la citation conservée. Autres remplacements : altéplase « (0,9 mg/kg) » ; fiche aspirine « aucune recommandation suisse ne tranche ce cas ». |
| Phase A | Moyen | Ancres AIPS collées sur des doses de recommandation | **Appliqué.** Thiamine EFNS, Diamox, sélénite EUGOGO et hydrocortisone ESE/ES portent maintenant « hors AIPS » et leur seule source. La phrase de l'IIHTT (essai américain) est retirée. |
| DX.4 | Moyen | Atropine ×5, arrêt 24 h ×3 | **Appliqué.** Dose seulement dans la fiche atropine ; renvois depuis l'urgence, l'arbre et le point 14. Arrêt 24 h gardé dans la fiche prednisone et en points clés ; le point 14 renvoie. |
| Phase A + DX | Moyen | Redites inter-fichiers | **Appliqué en partie.** Thrombolyse 4,5 h : retirée de DX.2 (×3) et de Phase A (×2), avec un renvoi DX.3. Tours 88,3/75,7 % : retiré de DX.2. Botulisme « 2 heures » : retiré du texte de DX.1. Question « diabétique avec VI » de la Phase A remplacée par une question sur la diplopie monoculaire. Question prednisone retirée de la Phase A (6 questions). Phrases identiques Phase A↔DX.4 et DX.1↔DX.3 reformulées. **Non appliqué :** anatomie III/IV/VI et FLM (réécriture lourde de 4 fichiers à la limite de taille) ; OAC annexe 1, car chaque DX porte sa règle de conduite propre ; citations AIPS identiques dans les fiches DX d'une même molécule, car elles sont exigées par la règle « fiche par molécule ». |
| DX.3 et autres | Moyen | Images absentes (Phase A, DX.1–DX.5) | **Reporté.** Les clichés déjà présents (voie oculosympathique, angio-CT) sont guidés dans DX.9 et DX.10. Les recopier créerait une redite. Noté dans HELP.md. |
| DX.1 | Léger | Cellules télégraphiques | **Appliqué en partie.** Les parenthèses de déduction sont retirées. Les cellules `td` sont exemptées par controle3 ; aucune réécriture d'ensemble. |
| Phase A | Léger | Pédagogie (schéma réel) | Sans correction exigée. |
| DX.6 | Moyen | Seuils anti-JCV 0,9 / 1,5 | **Appliqué.** AIPS 57273 relue sur refdata, phrase exacte. Ligne de HELP supprimée. |
| DX.10 | Moyen | Imagerie de tout III : source américaine et chinoise seules | **Appliqué.** Ajout de S6, Lagrèze, Dtsch Arztebl 2026 (relu sur PMC) : « sparing of the pupil does not rule out such a lesion… any patient with an oculomotor nerve palsy should undergo an imaging study ». Ajout dans les points clés, l'arbre et la question 14. |
| DX.10 | Moyen | Arbre clip/endovasculaire | **Appliqué.** Ge 2025 relu : le critère « plus de 7 jours » est ajouté. La phrase dit que cette source unique ne vient pas d'Europe et que l'équipe neurovasculaire décide selon l'ESO 2022 (S3). |
| DX.7 | Moyen | Arbre « III → imagerie » sur S32 seul | **Appliqué.** Renvoi vers DX.10, qui porte ESO et Lagrèze. |
| DX.7 | Moyen | Prednisone 15–20 mg redite (11.A) | **Appliqué.** Le schéma reste dans l'arbre, l'urgence, la fiche et les points 13 et 14. |
| DX.6 | Léger | 46,2 % au point 13 | **Appliqué.** Valeurs par œil (46,2 %) et par patient (63,2 %). |
| DX.7 | Léger | Phrase Takayasu obscure | **Appliqué sur EULAR 2025 relu.** Le texte dit : « TAK tends to not involve the axillary arteries, and GCA tends not to involve the renal arteries ». Ligne de HELP supprimée. |
| DX.10 | Léger | Formule de lacune au point 11 | **Appliqué.** |
| DX.8 | Léger | « 25 cm » ×8 et point 1 | **Appliqué.** Le seuil reste au critère du point 8 et dans la fenêtre de la pression ; les autres endroits renvoient au point 8. Les deux premières phrases du point 1 sont fusionnées. « Pseudotumor cerebri » est gardé au point 1, car il délimite formes primaires et secondaires. |
| DX.6 | Léger | Syndrome un-et-demi | **Appliqué autrement.** Strupp (S9) relu : il ne nomme pas ce syndrome. Phrase de renvoi sans chiffre vers DX.3 (`f-dx3-p7-oin`), qui le porte sur S13. |
| DX.6–DX.10 | Léger | Images d'examen absentes | **Reporté.** Notées dans HELP.md. |
| DX.9 | Moyen | Fiches altéplase, aspirine et clopidogrel redites de DX.3 | **Appliqué.** Restent l'indication, la dose AIPS, l'âge et le délai, les contre-indications, la surveillance de l'altéplase et l'oubli du clopidogrel (faits uniques), plus un lien vers la fiche DX.3. Retirés : mécanisme, grossesse et allaitement. |
| DX.9 | Léger | Titres non uniformes | **Appliqué** aux 10 DX : « DX.n — nom canonique — S1.1 … ». |

## Retraits (où l'information reste)
- Phase A, 5 fiches .mb : posologie, contre-indications, grossesse et allaitement → fiches de DX.4 (pyridostigmine, prednisone, méthylprednisolone, IgIV), DX.5 (méthylprednisolone, téprotumumab) et DX.7 (prednisone, méthylprednisolone).
- Phase A, point 1 : test d'occlusion → points 5 et 7 ; SSO/SSML → points 6 et 12 ; tableau des mécanismes → point 3 ; Kremmyda → algorithme et DX.4 ; définition EFNS → point 8 et DX.4.
- Phase A : phrase de l'IIHTT retirée (essai américain seul) ; question prednisone → DX.4, point 14.
- DX.1 : dermatochalasis → points 2, 4, 6 et 7 ; blépharoplastie → points 10 et 11 ; phrase des causes et lentilles → points 2 et 3 ; botulisme 2 h → tableau du point 11 de DX.1 et Phase A.
- DX.2 : phrase des termes anglais retirée (terminologie seule) ; thrombolyse 4,5 h → fenêtre d'urgence de DX.2 et DX.3 ; Tours 88,3/75,7 % → Phase A, point 2.
- DX.4 : dose d'atropine → fiche atropine ; arrêt 24 h → fiche prednisone et point 13.
- DX.5 : Means/Saint-Yves et « ophtalmopathie » des AIPS retirés (terminologie seule).
- DX.6 : phrase DIT → point 8.
- DX.7 : 15–20 mg à 2–3 mois → arbre, urgence, fiche prednisone, points 13 et 14.
- DX.8 : « 25 cm » ×5 → critère du point 8 et fenêtre de la pression.
- DX.9 : mécanisme, grossesse et allaitement de l'altéplase, de l'aspirine et du clopidogrel → fiches de DX.3.
