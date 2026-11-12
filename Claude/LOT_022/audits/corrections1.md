# LOT_022 — corrections de l'audit 1 (A et B), 11.11.2026

Chaque défaut a été vérifié sur le fichier et, quand il touche un fait, sur la source réelle relue le 11.11.2026 :
RMS 2018 (PDF UNIGE unige:123502, p. 2 : « jusqu'à 60 % des cas » sous halopéridol, « 2 à 3 % » sous atypique),
EFNS 2011 (résumé PubMed 20482602), Valls-Solé et Defazio 2016 (PMC4814756), Defazio 2017 (PMC5941939, texte OAI),
Cochrane CD004900 (résumé français). Aucune dose n'a changé ; les AIPS citées restent celles de l'audit (refdata).

## Appliqué
| Fichier | Défaut | Correction |
|---|---|---|
| DX.8 | Grave : chiffre Dystonie-info.ch (Merz) 10/10 000 | Phrase, ligne de tableau et conclusion retirées ; le point 2 s'ouvre sur l'absence de série suisse, puis ESDE. |
| DX.8 | Appuis Dystonie-info (S1–S6) | Réancrés : cécité fonctionnelle et vie sociale (Valls-Solé), rareté et diagnostic manqué (Valls-Solé, Defazio 2017), « essentiel = idiopathique » et 25 % d'apparentés atteints (Defazio 2017), bilatéral et synchrone (Defazio 2017), stimulation cérébrale profonde après échec des médicaments et de la toxine (EFNS), objectif du traitement (Cochrane). Phrase « toxine meilleur choix » (S3) supprimée : l'EFNS et Cochrane le portent déjà. S2–S4 retirés de la bibliographie ; Dystonie-info ne garde que des faits descriptifs sans chiffre ni décision. |
| DX.8 | Point 1 : redite de l'apraxie (fenêtre f-dx8-p1-aeo) | Fenêtre supprimée ; renvoi au DX.10, qui porte définition et mécanisme. |
| DX.8 | Repère 3 hors de la portion orbitaire | Cercle et chiffre déplacés sur l'anneau rouge latéral (157,180), vérifiés sur rendu. L'emplacement de l'audit (150,127) tombait au bord supérieur, hors du muscle. |
| DX.8 | Numérotation S13 absente | Libellés visibles renumérotés S1–S12 dans l'ordre de la bibliographie (ancres inchangées). |
| DX.8, DX.6 | h1 hétérogène | « S1.6 — Blépharospasme ». |
| Phase A | « 2 à 3 % » pour tout neuroleptique | « Jusqu'à 60 % sous neuroleptique conventionnel, 2 à 3 % sous atypique » (deux tableaux), source S24 = RMS 2018 (HUG) ajoutée. |
| Phase A | Redite Claude Bernard-Horner dans f-p3-base | Puce des pièges retirée ; la phrase sourcée reste. |
| Phase A | Point 1 : phrase PROFILES | Déplacée en tête du point 4, avec S1. |
| Phase A | Légende qui recopie le titre | Texte de l'audit appliqué. |
| DX.6 | Badge 🚩 E1 absent | Ajouté au h2. |
| DX.6 | Redite cornéenne avec DX.5 | Couches, épaisseurs, Bowman, innervation et arc réflexe retirés ; renvoi au DX.5 ; restent l'épithélium barrière (7–10 jours), l'endothélium et une phrase sur le réflexe qui mime le blépharospasme. Œdème endothélial non ajouté (non vérifié dans S15). |
| DX.6 | « repères quatre et cinq » pour quatre repères | « repère quatre ». |
| DX.6 | Redite des 50 % de récidives | Seconde occurrence retirée ; le fait reste dans l'histoire naturelle (point 2). |
| DX.10 | Point 1 : commentaire du mot « apraxie » | Déplacé à la fin du premier paragraphe du point 3 (S21 conservé). |
| DX.5 | Point 1 : plaie perforante | Phrase retirée ; le fait reste dans la base anatomique, la démarche et les drapeaux rouges du même fichier. |
| DX.1, DX.2, DX.4, DX.5 | Méta-commentaire « Ce fichier traite… » | Phrase verbale centrée sur le diagnostic. |
| DX.7 | Repère 2 hors du pont | Cercle (495,355) et chiffre recentrés sur le pont, vérifiés sur rendu. |
| DX.9 | Repère 1 sur l'étiquette « SNc » | Cercle (497,592) et chiffre posés sur l'origine des fibres. |
| DX.1 | Point 9 sans image d'examen | Photographie libre (Kellogg, Univ. Michigan, CC BY 3.0, Wikimedia Commons) d'une érosion épithéliale d'œil sec colorée à la fluorescéine, insérée dans f-dx1-p9-fluo avec copie annotée, lecture guidée et piège. |

## Non appliqué
- Légendes « (titre) » de DX.2, DX.4, DX.5 : le titre entre parenthèses rend chaque légende unique ; sa suppression crée des phrases dupliquées que `controle3` refuse dans les fichiers à plusieurs figures.
- DX.3, fiche BOTOX : la fiche `.mb` doit porter la dose AIPS de sa molécule (règle L1) ; le renvoi à la Phase A est refusé.
- Photographies de myokymie et de tic (DX.3, DX.4), tableaux à 390 px, fiches BOTOX de DX.7–DX.10 : aucune action exigée ; lacune notée dans HELP.md.

## Contrôles
`controle3 --script-ok` VERT (local et `/home/user/wt/proto`) sur les 11 fichiers ; `verif_aips` OK, aucun bloquant.
Octets : Phase A 95 612 ; DX.1 87 219 ; DX.2 82 769 ; DX.3 83 260 ; DX.4 96 468 ; DX.5 99 694 ; DX.6 97 590 ;
DX.7 98 239 ; DX.8 93 253 ; DX.9 85 784 ; DX.10 91 561.
