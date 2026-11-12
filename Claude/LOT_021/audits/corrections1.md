# LOT_021 — corrections de l'audit 1 (A et B), 11.11.2026

Chaque défaut a été relu sur le fichier ; les AIPS concernées (Xarelto 58728, Eliquis 61549, Nasivin 45138) figurent en bibliographie avec leur URL refdata. Contrôles finaux : `controle3 --script-ok` (proto et local) VERT pour les 11 fichiers ; `verif_aips` sans BLOQUANT (seule alerte : Phase A, Xylocain 20–60/600 mg, faux positif déjà levé par l'audit A) ; tailles 81,6 à 116,3 Ko ; Playwright (1280 px) : les 8 fiches `.mb` de DX.6 s'ouvrent depuis f-dx6-medic, et les images de base de DX.6 et DX.7 se chargent.

## Audit 1 A
| # | Fichier | Défaut | Décision | Motif ou mise en œuvre |
|---|---|---|---|---|
| A0–A1 | DX.2 | Point 1 : classification EHRA | Appliqué | Phrase et fenêtre f-dx2-p1-niv déplacées au point 8, sans perte. |
| A2 | DX.4 | Point 1 : épidémiologie vague | Appliqué | Fichier à 81 649 octets. |
| A3–A5 | DX.2 | Seuil en g/dL, redite | Appliqué | 70/100 g/L au point 9 et en 11.C ; 11.A renvoie au seuil SFORL. En plus : la redite du point 7 (f-dx2-p7-s3) renvoie au point 9. |
| A6 | DX.1 | Corticoïdes nasaux 8 → 20 % (redite) | Appliqué | Retrait au point 3 ; en plus, le point 12 renvoie au point 5 au lieu de répéter le chiffre. |
| A7 | DX.1 | « Deux faces de la cloison » (redite) | Appliqué | Règle gardée au point 13. |
| A8 | Phase A | Liste E1–E3 répétée | Appliqué | Le chapeau garde la liste. |
| A9 | Phase A | Durée du tamponnement (redite DX.1) | Appliqué | Renvoi vers DX.1 #dx1-p11. |
| A10 | Phase A | Ancre oxymétazoline | Appliqué | Ajout de l'ancre sb-aips-45138. |
| A11 | DX.2 | Mécanisme des AOD sur l'AIPS Ondexxya | Appliqué | Ancres Xarelto et Eliquis. |
| A12 | DX.2 | Méta-commentaire | Appliqué | — |
| A13 | DX.5 | Redite « évolution inhabituelle » | Appliqué | Texte de l'audit repris. |
| A14 | DX.5 | Point 1 : diamètre de la perforation | Appliqué (modifié) | Phrase déplacée au point 8, et non supprimée, pour ne perdre aucun fait. |
| A15 | DX.4 | Phrase agrammaticale | Appliqué (modifié) | « Tox Info Suisse conseille les parents au numéro 145 » (phrase reconnue verbale par controle3). |
| A16 | Tous les DX | « Ce fichier traite… » | Appliqué et étendu | Ouverture par le nom du diagnostic dans DX.1 à DX.8 et DX.10 (DX.9 n'en portait pas). |
| A17 | Phase A, DX.1–DX.5 | Volet social LAA/LAMal | Refusé ici | Aucun texte Fedlex n'a été lu pendant cette mission ; la lacune reste dans HELP.md. |
| A18–A21 | DX.3, DX.4, DX.1, Phase A | Images de signes ou de cas | Reporté | Images en file (Wikimedia) ; elles n'étaient pas dans les priorités de cette passe. |
| A22 | forme.css commun | Tableaux à 390 px | Reporté | Feuille commune : la décision revient au designer. |

## Audit 1 B
| # | Fichier | Défaut | Décision | Motif ou mise en œuvre |
|---|---|---|---|---|
| B0–B1 | DX.6 | 8 fiches `.mb` imbriquées dans f-dx6-medic | Appliqué | La fenêtre est fermée avant la première fiche et la balise orpheline est retirée. Avant : controle3 proto ROUGE (C_L1_fenetre_imbriquee, 8 cas). Après : VERT. Playwright : 8/8 fiches visibles. |
| B2 | DX.6 | Base sans image du clou plaquettaire | Appliqué | File:1909 Blood Clotting.jpg (OpenStax, CC BY 3.0, licence vérifiée par cliche.py) est insérée par `cliche.py figure` avec 4 repères, son piège (TP et TCA normaux) et sa décision. Le paragraphe est sourcé (S1, S17) et S17 ajoutée en bibliographie. |
| B3 | DX.6 | Point 1 : mécanisme redit au point 3 | Appliqué | — |
| B4 | DX.6 | Phrase de liaison méta | Appliqué | — |
| B5 | DX.7 | Base : cascade sans adhésion | Appliqué | La cascade Otocast est remplacée par la figure OpenStax (repères 1 à 4 : adhésion vWF, clou, VIIIa, fibrine). S18 ajoutée en bibliographie. La cascade reste dans DX.2. |
| B6 | DX.7 | « 0,30 et 50 UI/dL » | Appliqué | Corrigé en 30 à 50 UI/dL (ASH 2021 : 0,30–0,50 IU/mL). Même correction dans l'arbre décisionnel (« Facteur 30 à 50 UI/dL »). |
| B7 | DX.7 | Valeurs du point 9 redites | Appliqué | Renvoi vers f-dx7-p8-crit, avec la citation S4. |
| B8–B9 | DX.7 | Point 1 : classification en types | Appliqué | Phrase et fenêtre f-dx7-p1-types déplacées au point 8. |
| B10 | DX.7 | Phrase de liaison méta | Appliqué | — |
| B11–B12 | DX.8 | Nom anglais HHT au point 1 ; HUG | Appliqué | HUG est développé à sa première occurrence. |
| B13 | DX.8 | Erreur classique absente | Appliqué (modifié) | La fin de phrase est corrigée : on dépiste une MAV pulmonaire, qui commande l'antibioprophylaxie dentaire (S2). L'énoncé « avant tout geste dentaire » de l'audit était inexact. |
| B14 | DX.8 | Redite gastroscopie et coloscopie | Appliqué | — |
| B15 | DX.8 | Ligne sans source | Appliqué | — |
| B16 | DX.8 | Titre de page | Appliqué | Titres harmonisés aussi pour la Phase A, DX.2, DX.3, DX.9 et DX.10. |
| B17 | DX.9 | Erreur classique dite deux fois | Appliqué | La fenêtre « Raisonnement » garde l'erreur ; le repère du cornet moyen reste au point 6 et dans les tableaux. |
| B18–B19 | DX.9 | Coquille ; H1 | Appliqué | H1 harmonisé aussi dans DX.2 et DX.4. |
| B20 | DX.10 | Erreur classique absente | Appliqué (modifié) | Version plus courte : la règle des trois semaines, déjà dite cinq fois, n'est pas répétée en entier. Le bois est sourcé par S1 et S8. |
| B21 | DX.10 | Cliché TDM ou IRM au point 9 | Reporté | L'image est en file (Wikimedia 429, HELP.md) et le seul candidat est une métastase, non une tumeur primitive. |
| B22–B23 | DX.10 | H1 ; ligne sans source | Appliqué | — |

## Retraits (le fait reste ailleurs)
- DX.2, point 7 : seuil transfusionnel, qui reste au point 9.
- DX.2, 11.A : seuil, qui reste au point 9.
- DX.1, points 3 et 12 : 8 → 20 %, qui reste au point 5.
- DX.1, point 12 : « deux faces », qui reste au point 13.
- Phase A : liste E1–E3, qui reste dans le chapeau ; durée du tamponnement, qui reste dans DX.1, point 11.
- DX.4, point 1 : phrase sans chiffre (aucun fait sourcé perdu).
- DX.6, point 1 : mécanisme, qui reste au point 3. La mention du facteur Willebrand dans la Base de DX.6 est portée par DX.7.
- DX.7, point 9 : seuils, qui restent au point 8.
- DX.8 : nom anglais HHT (sémantique) ; « anémie → gastroscopie et coloscopie », qui reste au point 11.
- DX.9 : erreur classique, qui reste dans la fenêtre Raisonnement.
- DX.7, Base : image de la cascade Otocast, qui reste dans DX.2.
