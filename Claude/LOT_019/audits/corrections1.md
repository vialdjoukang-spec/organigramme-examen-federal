# LOT_019 — corrections de l'audit 1 (A et B), 11.11.2026

Base : 8a9bced9e. Chaque défaut a été vérifié sur le fichier ; les points médicaux sur l'AIPS refdata relue (Rectodelt 68119, document du 05.05.2026).
Contrôles finaux : `controle3 --script-ok` VERT sur les 11 fichiers ; `verif_aips` OK partout (seule alerte : DX.7 Xylocain 52097 « dose absente », faux positif confirmé par l'audit B) ;
tailles 83 907 à 139 666 o ; script de structure : aucune `section.fenetre` dans une autre, tout `href="#…"` et tout renvoi inter-fichiers a sa cible ; Playwright 1280 et 390 px : stridor, cisplatine, cétuximab, pembrolizumab et les 9 renvois DX.8 s'ouvrent (fenêtre visible, non nulle).

## Audit 1 A (Phase A, DX.1 à DX.5)

| Défaut | Décision | Motif / action |
|---|---|---|
| DX.1 Grave — f-dx1-p7-stridor imbriquée dans f-dx1-p7-tab | Appliqué | Paragraphe d'appel et fenêtre sortis après la fermeture de f-dx1-p7-tab ; texte inchangé ; ouverture vérifiée à Playwright. |
| DX.1 Moyen — croup : budésonide proposé sans écrire la divergence AIPS | Appliqué (reformulé) | AIPS 68119 relue : indication pseudocroup/croup, 100 mg, 2e suppositoire à 12–24 h. La dexaméthasone et le budésonide sont écrits hors AIPS ; en cas d'intolérance orale, Rectodelt 100 mg (S11). « Protocole des HUG » de la correction proposée non repris : aucune source HUG du croup dans la bibliographie. Décision ajoutée à HELP.md. |
| DX.1 Moyen — adrénaline nébulisée sans fiche | Appliqué | Lien vers la fiche Phase A f-ssp-m-adrenaline (AIPS 56551, aucune voie inhalée) et mention « hors AIPS pour la voie inhalée ». |
| DX.1 Moyen — terminologie au point 1 | Appliqué | Point 1 réduit à la définition AIPS du pseudocroup ; phrase Clinical Evidence et fenêtre déplacées à la fin du point 4 (id renommé f-dx1-p4-croup, aucun autre renvoi). |
| DX.1 Moyen — formule de lacune au point 2 | Appliqué | Phrase supprimée ; lacune déjà dans HELP.md. |
| DX.4 Moyen — délai ORL contraire à la Phase A | Appliqué (reformulé) | « 3 semaines, surtout chez un fumeur » (HUG, S1) ; seuil du Collège (8–15 j, S6) écrit comme divergence avec lien vers la fenêtre f-ssp-p8-delais de la Phase A. « Plus tôt chez le fumeur » non repris : les HUG écrivent « surtout ». |
| DX.2 Léger — ligne UEP (terminologie) au point 1 | Appliqué | Ligne UEP et critique « non organique / fonctionnel » déplacées dans la fenêtre « Classification étiologique » ; phrase sur le rangement régulatif retirée (redite de cette fenêtre). |
| Phase A Léger — enrouement, aphonie, cinq composantes au point 1 | Appliqué | Deux phrases déplacées au point 5 (caractérisation du symptôme), fenêtre f-ssp-p1-composantes inchangée. |
| DX.5 Léger — chiffres répétés (Rome 44/125, Glasgow 90 %) | Appliqué | Point 11 (Rome) et point 8 (Glasgow) renvoient au point 2 ; chiffres conservés aux points 2 et 14. |
| DX.1 Léger — dose Rectodelt répétée | Appliqué | Point 14 : explication remplacée par « la dose ne se calcule pas au poids », avec lien vers la fiche ; dose conservée dans la fiche, le tableau 11 et la réponse. |
| Tous Léger — images non insérées | Refusé | Non bloquant avant LOT_021 ; téléchargements Commons en file d'attente (HELP.md) ; hors périmètre de cette correction. |

## Audit 1 B (DX.6 à DX.10)

| Défaut | Décision | Motif / action |
|---|---|---|
| DX.8 Grave ×9 — renvois « ({id</td><td>libellé}) » | Appliqué | Les 9 convertis en `<a class="ouvre" href="#f-dx8-…">` ; cellules fantômes supprimées ; script : toutes les lignes de chaque tableau ont le même nombre de colonnes ; cibles présentes. |
| DX.10 Grave ×2 — fiches .mb imbriquées dans f-dx10-p11-med | Appliqué | Fermeture de f-dx10-p11-med avant la fiche cisplatine, fermeture en double retirée ; les trois fiches s'ouvrent depuis la fenêtre « Médicaments » (Playwright). |
| DX.10 Moyen — rang 🚩 E3 absent | Appliqué | Titre « Cancer du larynx 🚩 E3 », conforme à LISTE_DX_CANONIQUE.md. |
| DX.6 Moyen — redite logopédie (DX.2–DX.5) | Appliqué | Phrase supprimée (contenu tenu par DX.3 et les autres DX). Reformulation proposée refusée : aucune source lue pour elle. |
| DX.6 Moyen — redite profil vocal (DX.4) | Appliqué | Phrase supprimée ; définition tenue par DX.4 (et DX.2). |
| DX.9 Moyen — phrases nominales dans les tableaux | Appliqué en partie | Tableau des drapeaux rouges entièrement verbalisé (colonnes signification et action, sources inchangées). Autres cellules nominales (données d'études, schémas) laissées : controle3 VERT, reformulation massive hors priorité. |
| DX.8 Léger — dystonies focales au point 1 | Appliqué | Phrase RMS déplacée au point 3 (verbe reconnu par controle3). |
| DX.10 Léger — portée de la TNM au point 1 | Appliqué | Phrase déplacée dans la fenêtre f-dx10-p8-tnm (point 8). |
| DX.7 Léger — numérotation 9.b/9.d en double | Appliqué | Renumérotée 9.a à 9.g ; aucun renvoi textuel à ces numéros. |
| DX.7 Léger — redite sexe/tabac/cause maligne | Appliqué | Phrase du point 11 retirée ; fait conservé au point 2 (Valence, S9) et au point 5. |
| DX.10 Léger — redites réduction endoscopique / trachéostome | Appliqué en partie | Arbre décisionnel : renvoi à la fenêtre f-dx10-p11-urgence ; urgence, points clés et point 14 conservés (rôles distincts). |
| DX.6 Léger — h1 « SSP S1.3 » | Appliqué | « S1.3 ». |
| DX.6–DX.10 Léger — images, tableaux larges à 390 px | Refusé | Non bloquant avant LOT_021 ; images en file d'attente. |

## Retraits (aucun fait sourcé unique perdu)
- DX.1 point 2 : phrase de lacune (consignée dans HELP.md).
- DX.1 point 14 : rappel de la dose Rectodelt (reste dans la fiche f-dx1-m-prednisone, le tableau du point 11 et la réponse).
- DX.2 point 1 : « le guide allemand range la forme malrégulative parmi les dysphonies régulatives » (reste dans la fenêtre Classification étiologique).
- DX.5 points 8 et 11 : chiffres Glasgow 90 % et Rome 44/125 (restent aux points 2 et 14).
- DX.6 : phrase logopédie (DX.2, DX.3, DX.4, DX.5) et phrase profil vocal (DX.4, DX.2).
- DX.7 point 11 : sexe, tabac, cause maligne (point 2, S9).
- DX.10 arbre : réduction endoscopique avant laryngectomie (fenêtre urgence, points clés, point 14).
