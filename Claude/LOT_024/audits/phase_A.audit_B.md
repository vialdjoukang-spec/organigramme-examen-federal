# Audit B (conformité L1) — LOT_024 Phase A

Fichier : LOT_024_Phase_A_V0.html (81 796 octets, bande 80–150 Ko respectée). Contrôles faits : harnais `verifier`, extraction par point, superposition PIL des 6 cercles sur l'image, recherche de fenêtres imbriquées, liens internes, longueur des phrases (583 phrases), redites, abréviations.

Constats conformes : 14 points présents et bien affectés ; point 1 réduit à la définition (2 phrases) ; point 6 avec 7 fenêtres « Région 1 à 7 » ; point 14 avec 9 questions, toutes renvoyées à un point ; 39 fenêtres, 0 imbriquée, 0 lien mort ; image Blausen en couleurs (webp réelle) ; les 6 repères du SVG tombent justement (1 conduit cartilagineux, 2 conduit osseux, 3 tympan, 4 osselets, 5 trompe, 6 cochlée) ; ordre fréquence et 🚩 E1 fuite de LCS, E2 otite externe nécrosante, E3 cholestéatome conformes à LISTE_DX_CANONIQUE.md ; aucune phrase dupliquée.

| N° | Gravité | Extrait | Correction |
|---|---|---|---|
| 1 | critique (harnais, reprise telle quelle) | « script, image ou feuille de style externe présent » | Le harnais signale `<img src="images/…webp">` et `<image href>` ; à arbitrer avec la consigne 8 bis (image exigée). Si le dépôt exige l'autonomie, intégrer l'image en data-URI dans la bande 80–150 Ko ; sinon obtenir la dérogation écrite avant dépôt. |
| 2 | mineure (harnais) | mention « non validé cliniquement » absente | Ajouter en tête la mention exacte attendue. |
| 3 | majeure | Point 14, dernière question : « Comment traiter un insecte vivant dans le conduit ? … (point 6) » | Le traitement relève du point 11. Renvoyer au point 11 et y placer la règle (huile, puis retrait) ; le point 6 ne la contient qu'en fenêtre. |
| 4 | majeure | « selon la SSI » (point 7, 8, 11, 13, 14) ; « TEP au FDG » (point 9) ; « AIPS 31957 » | Développer à la première occurrence : « Société suisse d'infectiologie (SSI) » dès le point 2 ; « tomographie par émission de positons au fluorodésoxyglucose » ; « information professionnelle suisse (AIPS) ». Seuls ORL, HUG et IRM le sont. |
| 5 | majeure | Point 4 : « Le médecin exclut d'abord les trois urgences 🚩 E1 à E3, puis les drapeaux rouges sans rang , car une méningite… » (31 mots) | Couper en deux phrases de 12 à 28 mots. |
| 6 | majeure | Phrases de 29 à 31 mots : point 3 (« Pourquoi le tragus fait mal… », « Pourquoi l'infection gagne la base du crâne… ») ; point 9 (« L'imagerie, complétée… ») ; point 4 (« Une oreille qui coule saigne ou suppure… ») | Scinder chacune en deux phrases verbales de 28 mots au plus. |
| 7 | mineure | Tableaux : un seul porte « Interprétation : » sur 7 tableaux | Ajouter une phrase d'interprétation verbale sous chaque tableau, comme dans LOT_022 (légende « Ce tableau interprète… »). |
| 8 | mineure | Repère 2 : cercle à (423,319) chevauche le bord du toit osseux du conduit | Décaler d'environ 10 px vers le bas (≈ 423,332) pour cadrer le conduit osseux. |
| 9 | mineure | Redites : « 48 à 72 heures » 6 fois ; « Santorini » 2 fois ; sommaire du point 1 (69 mots) listé en prose | Garder une mention dans le point 11, renvoyer ailleurs par « (point 11) ». |

Question finale : dépôt autorisé après correction des lignes 1, 3, 4, 5 et 6 ? **non** (non en l'état ; la cohérence A↔B n'a pas été auditée ici, hors mandat).
