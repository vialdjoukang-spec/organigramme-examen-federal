# V7 scan agent 13 — résultats

Balayage en lecture seule du 2026-10-25. Agent Cursor 13. Moitié haute, ordre 248→001. Aucune écriture Drive, aucun HTML de production modifié.

Critère des 11 entités : 1 SSP (Appel A, 14 parties) + 10 DD (Appel B, 14 parties chacun) + package Drive 5/5 (A + B_P1 + B_P2 + B_P3 + B_P4).

## Résumé

- **n_complet : 12**
- **n_incomplet : 0**
- Incomplets : aucun

## Tableau

| lot | package_5_5 | ssp_parties/14 | dd_complets/10 | statut |
|-----|-------------|----------------|----------------|--------|
| LOT_239 | true | 14/14 | 10/10 | complet |
| LOT_238 | true | 14/14 | 10/10 | complet |
| LOT_228 | true | 14/14 | 10/10 | complet |
| LOT_227 | true | 14/14 | 10/10 | complet |
| LOT_218 | true | 14/14 | 10/10 | complet |
| LOT_217 | true | 14/14 | 10/10 | complet |
| LOT_216 | true | 14/14 | 10/10 | complet |
| LOT_215 | true | 14/14 | 10/10 | complet |
| LOT_214 | true | 14/14 | 10/10 | complet |
| LOT_213 | true | 14/14 | 10/10 | complet |
| LOT_212 | true | 14/14 | 10/10 | complet |
| LOT_211 | true | 14/14 | 10/10 | complet |

## Méthode

- Package : `PACKAGE_5_5_agent13.json`. Pour les 12 lots, A, P1, P2, P3 et P4 sont présents et `package_5_5` vaut true.
- Appel B : contrôle du 2026-10-25 (`V7_14PARTIES_CHECK`), verdict OK_14, 10 runs de longueur 14. Non recompté.
- Appel A : `analyze14.py` sur chaque HTML, puis contrôle des titres de partie (`h4` ou `p` + `strong`, suite 1..14). Le nombre retenu `ssp_parties` est cette suite structurelle.
- `analyze14.py` compte aussi les lignes « N. » des protocoles et des arbres. Quand une de ces listes redémarre à 1, le script coupe le plan SSP et peut ne plus rattacher les parties 11 à 14. Les titres de partie, eux, restent 1..14.

## Écarts analyze14 sur l’Appel A

| lot | analyze14 runs 14 | longueurs brutes | titres structurels 1..14 |
|-----|-------------------|------------------|---------------------------|
| LOT_239 | 1 | [14] | 14/14 (p>strong) |
| LOT_238 | 0 | [10, 5, 3, 4, 5, 3] | 14/14 (p>strong) |
| LOT_228 | 1 | [14, 9] | 14/14 (h4) |
| LOT_227 | 0 | [10, 6, 10] | 14/14 (h4) |
| LOT_218 | 1 | [14, 8] | 14/14 (h4) |
| LOT_217 | 1 | [14, 8] | 14/14 (h4) |
| LOT_216 | 1 | [14, 7] | 14/14 (h4) |
| LOT_215 | 1 | [14, 8] | 14/14 (h4) |
| LOT_214 | 1 | [14, 9] | 14/14 (h4) |
| LOT_213 | 1 | [14] | 14/14 (h4) |
| LOT_212 | 1 | [14] | 14/14 (h4) |
| LOT_211 | 1 | [14] | 14/14 (h4) |

Lots où analyze14 n’émet aucun run 14 alors que les titres 1..14 sont présents : **LOT_238**, **LOT_227**.

## Détail par lot

### LOT_239

- Package 5/5 : true. Dossier ASSIGN `1xRxN_xamk0g97DN_NGA-oFJfQX25QyV4`. Fichier A retenu : Agent_2 | LOT_239 Appel A — Plan et liste des différentiels.html.
- SSP : 14/14. Partie 1 « Définition et sémantique. ». Partie 14 « Pièges et questions fréquentes à l'examen fédéral. ».
- analyze14 Appel A : 1 run de 14, longueurs [14]. analyze14: au moins un run 1..14 (plan SSP). Les runs plus courts éventuels viennent de listes numérotées internes, pas d'un second plan SSP.
- DD : 10/10, verdict OK_14. LOT_239_B_P1_Agent2.html (2×14), LOT_239_B_P2.html (3×14), LOT_239_B_P3.html (2×14), LOT_239_B_P4.html (3×14).
- Entités DD :
  - DX.1 (B_P1, 14 parties) — DX.1. Certificat d'incapacité de travail (employeur, assureur d'indemnités journalières)
  - DX.2 (B_P1, 14 parties) — DX.2. Rapport médical à l'assurance-accidents (LAA) et question de causalité
  - DX.3 (B_P2, 14 parties) — DX.3. Demande de renseignements d'un assureur, de l'employeur ou d'une autorité et secret professionnel
  - DX.4 (B_P2, 14 parties) — DX.4. Constat et certificat de décès, décès extraordinaire (y compris l'assistance au suicide) — 4e rang
  - DX.5 (B_P2, 14 parties) — DX.5. Rapport et expertise pour l'assurance-invalidité (détection précoce, révision)
  - DX.6 (B_P3, 14 parties) — DX.6. Décision médicale de placement à des fins d'assistance (PAFA)
  - DX.7 (B_P3, 14 parties) — DX.7. Constat de lésions traumatiques et violence (certificat de coups et blessures)
  - DX.8 (B_P4, 14 parties) — DX.8. Aptitude à la conduite (communication à l'autorité, contrôle des conducteurs âgés)
  - DX.9 (B_P4, 14 parties) — DX.9. Attestation de capacité de discernement (directives anticipées, mandat pour cause d'inaptitude, assistance au suicide)
  - DX.10 (B_P4, 14 parties) — DX.10. Certificats d'aptitude et attestations diverses (sport, grossesse, annulation de voyage, enfant malade, demande de complaisance)
- Statut : **complet**.

### LOT_238

- Package 5/5 : true. Dossier ASSIGN `1VuvWcQXwQxvyTwGxdnZxcKW0rWgwqUup`. Fichier A retenu : LOT_238_Appel_A_V7_Plan_et_Liste.html.
- SSP : 14/14. Partie 1 « Définition et cadre de l'évaluation pré-interventionnelle. ». Partie 14 « Pièges et erreurs fréquentes. ».
- analyze14 Appel A : 0 run de 14, longueurs [10, 5, 3, 4, 5, 3]. analyze14 ne sort aucun run 14: des paragraphes « 1. » internes (protocole ou arbre) coupent la suite avant le titre 11, et les titres 11–14 ne sont plus rattachés. Les titres de partie 1..14 sont présents dans l'ordre.
- DD : 10/10, verdict OK_14. LOT_238_B_P1_V7.html (2×14), LOT_238_B_P2.html (3×14), LOT_238_B_P3.html (2×14), LOT_238_B_P4.html (3×14).
- Entités DD :
  - DX.1 (B_P1, 14 parties) — DX.1 — Risque cardiaque ischémique et lésion myocardique périopératoire
  - DX.2 (B_P1, 14 parties) — DX.2 — Anticoagulation orale (AOD et AVK)
  - DX.3 (B_P2, 14 parties) — DX.3 — Stent coronaire sous double antiagrégation plaquettaire
  - DX.4 (B_P2, 14 parties) — DX.4 — Anémie préopératoire et gestion du sang du patient
  - DX.5 (B_P2, 14 parties) — DX.5 — Sujet âgé fragile et risque de délire postopératoire
  - DX.6 (B_P3, 14 parties) — DX.6 — Antécédent d'allergie ou anaphylaxie périopératoire
  - DX.7 (B_P3, 14 parties) — DX.7 — BPCO et syndrome d'apnées obstructives du sommeil
  - DX.8 (B_P4, 14 parties) — DX.8 — Diabète sous SGLT2i, agoniste du GLP-1, metformine ou insuline
  - DX.9 (B_P4, 14 parties) — DX.9 — Corticothérapie prolongée et insuffisance surrénalienne
  - DX.10 (B_P4, 14 parties) — DX.10 — Maladie rénale chronique
- Statut : **complet**.

### LOT_228

- Package 5/5 : true. Dossier ASSIGN `1oHdO-R_gsSRDBFRd98-AQyaq-Z87AFGQ`. Fichier A retenu : LOT_228_Appel_A_V7_Plan_et_Liste.html.
- SSP : 14/14. Partie 1 « Définition et cadre nosologique ». Partie 14 « Pièges ».
- analyze14 Appel A : 1 run de 14, longueurs [14, 9]. analyze14: au moins un run 1..14 (plan SSP). Les runs plus courts éventuels viennent de listes numérotées internes, pas d'un second plan SSP.
- DD : 10/10, verdict OK_14. LOT_228_B_P1.html (2×14), LOT_228_B_P2.html (3×14), LOT_228_B_P3.html (2×14), LOT_228_B_P4.html (3×14).
- Entités DD :
  - DX.1 (B_P1, 14 parties) — DX.1 — Neutropénie fébrile après chimiothérapie
  - DX.2 (B_P1, 14 parties) — DX.2 — Infection par le VIH à un stade avancé et infections opportunistes
  - DX.3 (B_P2, 14 parties) — DX.3 — Pneumocystose chez le patient non infecté par le VIH
  - DX.4 (B_P2, 14 parties) — DX.4 — Infection à cytomégalovirus après greffe
  - DX.5 (B_P2, 14 parties) — DX.5 — Aspergillose invasive
  - DX.6 (B_P3, 14 parties) — DX.6 — Zona et infections à VZV de l’immunodéprimé
  - DX.7 (B_P3, 14 parties) — DX.7 — Réactivation tuberculeuse
  - DX.8 (B_P4, 14 parties) — DX.8 — Réactivation du VHB sous chimiothérapie ou rituximab
  - DX.9 (B_P4, 14 parties) — DX.9 — Syndrome septique post-splénectomie (OPSI)
  - DX.10 (B_P4, 14 parties) — DX.10 — Déficit immunitaire commun variable (DICV)
- Statut : **complet**.

### LOT_227

- Package 5/5 : true. Dossier ASSIGN `1FL3BSP7UlCsiD_ujY_gpghjhkTJ7ij2W`. Fichier A retenu : LOT_227_Appel_A_V7_Plan_et_Liste.html.
- SSP : 14/14. Partie 1 « Définition et sémantique ». Partie 14 « Pièges classiques d’examen ».
- analyze14 Appel A : 0 run de 14, longueurs [10, 6, 10]. analyze14 ne sort aucun run 14: des paragraphes « 1. » internes (protocole ou arbre) coupent la suite avant le titre 11, et les titres 11–14 ne sont plus rattachés. Les titres de partie 1..14 sont présents dans l'ordre.
- DD : 10/10, verdict OK_14. LOT_227_B_P1.html (2×14), LOT_227_B_P2.html (3×14), LOT_227_B_P3.html (2×14), LOT_227_B_P4.html (3×14).
- Entités DD :
  - DX.1 (B_P1, 14 parties) — DX.1 — Erreur de médication d’un collègue (prescription, transcription, préparation, administration)
  - DX.2 (B_P1, 14 parties) — DX.2 — Erreur ou retard diagnostique découvert en reprise de cas ou en second avis
  - DX.3 (B_P2, 14 parties) — DX.3 — Événement indésirable grave évitable (never event, décès inattendu) : information du patient et déclarations
  - DX.4 (B_P2, 14 parties) — DX.4 — Non-respect d’une procédure de sécurité (hygiène des mains, liste de contrôle chirurgicale)
  - DX.5 (B_P2, 14 parties) — DX.5 — Deuxième victime : détresse du collègue impliqué
  - DX.6 (B_P3, 14 parties) — DX.6 — Aptitude altérée (épuisement, fatigue, maladie psychique)
  - DX.7 (B_P3, 14 parties) — DX.7 — Alcool ou substances au travail
  - DX.8 (B_P4, 14 parties) — DX.8 — Harcèlement sexuel, discrimination, comportement irrespectueux
  - DX.9 (B_P4, 14 parties) — DX.9 — Fraude (faux certificat, falsification du dossier, facturation abusive)
  - DX.10 (B_P4, 14 parties) — DX.10 — Inconduite sexuelle ou abus de dépendance envers un patient
- Statut : **complet**.

### LOT_218

- Package 5/5 : true. Dossier ASSIGN `1kHPHThhhV_qDbxiBftCOuwQcfPp3mSxo`. Fichier A retenu : Agent_1 | LOT_218 Appel A — Plan et liste des différentiels.html.
- Note package : Agent_1 (no V7/Agent_2 name); also A_REDIGER stubs.
- SSP : 14/14. Partie 1 « Définition et sémantique ». Partie 14 « Pièges et questions fréquentes à l’examen fédéral suisse ».
- analyze14 Appel A : 1 run de 14, longueurs [14, 8]. analyze14: au moins un run 1..14 (plan SSP). Les runs plus courts éventuels viennent de listes numérotées internes, pas d'un second plan SSP.
- DD : 10/10, verdict OK_14. LOT_218_B_P1.html (2×14), LOT_218_B_P2.html (3×14), LOT_218_B_P3.html (2×14), LOT_218_B_P4.html (3×14).
- Entités DD :
  - DX.1 (B_P1, 14 parties) — DX.1 — Détresse psychique et suicidalité liées au stress minoritaire
  - DX.2 (B_P1, 14 parties) — DX.2 — Santé sexuelle des HSH et des femmes trans : VIH, IST, hépatites, HPV et mpox
  - DX.3 (B_P2, 14 parties) — DX.3 — Violences, discriminations, crimes de haine et pratiques de conversion
  - DX.4 (B_P2, 14 parties) — DX.4 — Chemsex et usage de substances psychoactives
  - DX.5 (B_P2, 14 parties) — DX.5 — Adolescent en questionnement : coming-out, confidentialité et capacité de discernement
  - DX.6 (B_P3, 14 parties) — DX.6 — Femmes lesbiennes et bisexuelles : prévention gynécologique et projet parental
  - DX.7 (B_P3, 14 parties) — DX.7 — Adulte trans ou non binaire demandant une transition (HA60)
  - DX.8 (B_P4, 14 parties) — DX.8 — Hormonothérapie féminisante : prescription, surveillance et complications
  - DX.9 (B_P4, 14 parties) — DX.9 — Hormonothérapie masculinisante : prescription, surveillance et complications
  - DX.10 (B_P4, 14 parties) — DX.10 — Adolescent avec incongruence ou dysphorie de genre
- Statut : **complet**.

### LOT_217

- Package 5/5 : true. Dossier ASSIGN `1bEeJLCZmQEHyqiEnSQvT-z62jmkio_Mi`. Fichier A retenu : Agent_1 | LOT_217 Appel A — Plan et liste des différentiels.html.
- Note package : Agent_1; also A_REDIGER stubs.
- SSP : 14/14. Partie 1 « Définitions, cadre et déontologie ». Partie 14 « Pièges et questions fréquentes à l’examen fédéral suisse ».
- analyze14 Appel A : 1 run de 14, longueurs [14, 8]. analyze14: au moins un run 1..14 (plan SSP). Les runs plus courts éventuels viennent de listes numérotées internes, pas d'un second plan SSP.
- DD : 10/10, verdict OK_14. LOT_217_B_P1.html (2×14), LOT_217_B_P2.html (3×14), LOT_217_B_P3.html (2×14), LOT_217_B_P4.html (3×14).
- Entités DD :
  - DX.1 (B_P1, 14 parties) — DX.1 — Mobbing (harcèlement psychologique) au travail chez l’adulte, avec trouble de l’adaptation (CIM-11 6B43)
  - DX.2 (B_P1, 14 parties) — DX.2 — Harcèlement scolaire (brimades) de l’enfant et de l’adolescent, avec plaintes psychosomatiques ou refus scolaire
  - DX.3 (B_P2, 14 parties) — DX.3 — Épisode dépressif avec idées suicidaires consécutif au harcèlement
  - DX.4 (B_P2, 14 parties) — DX.4 — Cyberharcèlement de l’adolescent, dont diffusion de contenus intimes et sextorsion
  - DX.5 (B_P2, 14 parties) — DX.5 — Harcèlement sexuel au travail, y compris en milieu médical
  - DX.6 (B_P3, 14 parties) — DX.6 — Conflit de travail ou burn-out sans mobbing
  - DX.7 (B_P3, 14 parties) — DX.7 — Violence et harcèlement envers les soignants par des patients ou des proches
  - DX.8 (B_P4, 14 parties) — DX.8 — Harcèlement obsessionnel (stalking)
  - DX.9 (B_P4, 14 parties) — DX.9 — Trouble de stress post-traumatique (TSPT) et TSPT complexe après un harcèlement grave
  - DX.10 (B_P4, 14 parties) — DX.10 — Allégation de harcèlement d’origine délirante ou paranoïaque
- Statut : **complet**.

### LOT_216

- Package 5/5 : true. Dossier ASSIGN `1cLlaj39EOMQw3zqDiigb9QNQdI90YTk-`. Fichier A retenu : Agent_1 | LOT_216 Appel A — Plan et liste des différentiels.html.
- Note package : Agent_1.
- SSP : 14/14. Partie 1 « Définitions, cadre et déontologie ». Partie 14 « Pièges et questions fréquentes à l’examen fédéral suisse ».
- analyze14 Appel A : 1 run de 14, longueurs [14, 7]. analyze14: au moins un run 1..14 (plan SSP). Les runs plus courts éventuels viennent de listes numérotées internes, pas d'un second plan SSP.
- DD : 10/10, verdict OK_14. LOT_216_B_P1.html (2×14), LOT_216_B_P2.html (3×14), LOT_216_B_P3.html (2×14), LOT_216_B_P4.html (3×14).
- Entités DD :
  - DX.1 (B_P1, 14 parties) — DX.1 — Violence physique et psychologique dans le couple chez l’adulte (violence conjugale)
  - DX.2 (B_P1, 14 parties) — DX.2 — Viol et contrainte sexuelle de l’adulte (agression sexuelle récente)
  - DX.3 (B_P2, 14 parties) — DX.3 — Violence dans le couple à haut risque létal : strangulation et menaces de mort
  - DX.4 (B_P2, 14 parties) — DX.4 — Maltraitance physique et psychologique de l’enfant, négligence comprise
  - DX.5 (B_P2, 14 parties) — DX.5 — Abus sexuels envers l’enfant et l’adolescent
  - DX.6 (B_P3, 14 parties) — DX.6 — Enfant exposé à la violence dans le couple
  - DX.7 (B_P3, 14 parties) — DX.7 — Maltraitance de la personne âgée
  - DX.8 (B_P4, 14 parties) — DX.8 — Traumatisme crânien infligé du nourrisson (syndrome du bébé secoué)
  - DX.9 (B_P4, 14 parties) — DX.9 — Agression sexuelle facilitée par des substances (soumission chimique)
  - DX.10 (B_P4, 14 parties) — DX.10 — Lésions accidentelles ou maladie organique mimant une maltraitance (diagnostic d’exclusion)
- Statut : **complet**.

### LOT_215

- Package 5/5 : true. Dossier ASSIGN `1ohcz2Puxd3exoAbk3jAwn5meYGwlJb9l`. Fichier A retenu : Agent_1 | LOT_215 Appel A — Plan et liste des différentiels.html.
- Note package : Agent_1.
- SSP : 14/14. Partie 1 « Définition et cadre nosologique ». Partie 14 « Pièges ».
- analyze14 Appel A : 1 run de 14, longueurs [14, 8]. analyze14: au moins un run 1..14 (plan SSP). Les runs plus courts éventuels viennent de listes numérotées internes, pas d'un second plan SSP.
- DD : 10/10, verdict OK_14. LOT_215_B_P1.html (2×14), LOT_215_B_P2.html (3×14), LOT_215_B_P3.html (2×14), LOT_215_B_P4.html (3×14).
- Entités DD :
  - DX.1 (B_P1, 14 parties) — DX.1 — Anorexie mentale
  - DX.2 (B_P1, 14 parties) — DX.2 — Boulimie (boulimie nerveuse)
  - DX.3 (B_P2, 14 parties) — DX.3 — Trouble dysmorphique corporel (dysmorphophobie)
  - DX.4 (B_P2, 14 parties) — DX.4 — Hyperphagie boulimique (souvent associée au surpoids ou à l’obésité)
  - DX.5 (B_P2, 14 parties) — DX.5 — Dysmorphie musculaire avec usage de stéroïdes anabolisants androgènes
  - DX.6 (B_P3, 14 parties) — DX.6 — Dermatose visible avec retentissement psychique (acné, alopécie, autres dermatoses affichantes)
  - DX.7 (B_P3, 14 parties) — DX.7 — Endocrinopathie modifiant l’apparence (SOPK et hirsutisme, syndrome de Cushing)
  - DX.8 (B_P4, 14 parties) — DX.8 — Altération de l’image corporelle secondaire à une maladie, un traitement ou une chirurgie (cancer, mastectomie, stomie)
  - DX.9 (B_P4, 14 parties) — DX.9 — Incongruence de genre (dysphorie de genre)
  - DX.10 (B_P4, 14 parties) — DX.10 — Insatisfaction corporelle normative (préoccupation non pathologique, diagnostic d’élimination)
- Statut : **complet**.

### LOT_214

- Package 5/5 : true. Dossier ASSIGN `1dQIdgiaVJnZRpqm_CjW8WxD0JkbF3zvW`. Fichier A retenu : Agent_1 | LOT_214 Appel A — Plan et liste des différentiels.html.
- Note package : Agent_1.
- SSP : 14/14. Partie 1 « Définition et cadre nosologique ». Partie 14 « Pièges ».
- analyze14 Appel A : 1 run de 14, longueurs [14, 9]. analyze14: au moins un run 1..14 (plan SSP). Les runs plus courts éventuels viennent de listes numérotées internes, pas d'un second plan SSP.
- DD : 10/10, verdict OK_14. LOT_214_B_P1.html (2×14), LOT_214_B_P2.html (3×14), LOT_214_B_P3.html (2×14), LOT_214_B_P4.html (3×14).
- Entités DD :
  - DX.1 (B_P1, 14 parties) — DX.1 — Trouble psychique lié au travail : épisode dépressif, trouble de l’adaptation ou burn-out (CIM-11 6A70, 6B43, QD85)
  - DX.2 (B_P1, 14 parties) — DX.2 — Lombalgie commune et autres troubles de l’appareil locomoteur
  - DX.3 (B_P2, 14 parties) — DX.3 — Maladie infectieuse aiguë de courte durée (grippe, infection respiratoire ou digestive)
  - DX.4 (B_P2, 14 parties) — DX.4 — Refus scolaire anxieux (anxiété de séparation, anxiété sociale) ou dépression de l’enfant et de l’adolescent (CIM-11 6B05, 6B04)
  - DX.5 (B_P2, 14 parties) — DX.5 — Absentéisme scolaire sans anxiété : école buissonnière, trouble des conduites (CIM-11 6C91) ou décrochage
  - DX.6 (B_P3, 14 parties) — DX.6 — Trouble lié à l’usage d’alcool ou d’autres substances (CIM-11 6C40, 6C41)
  - DX.7 (B_P3, 14 parties) — DX.7 — Accident professionnel ou non professionnel et maladie professionnelle (loi fédérale sur l’assurance-accidents, LAA)
  - DX.8 (B_P4, 14 parties) — DX.8 — Maladie somatique chronique ou trouble de détresse corporelle (anémie, hypothyroïdie, douleurs récurrentes ; CIM-11 6C20)
  - DX.9 (B_P4, 14 parties) — DX.9 — Violence subie : harcèlement scolaire, mobbing, violence domestique ou maltraitance
  - DX.10 (B_P4, 14 parties) — DX.10 — Absence sans incapacité médicale : motif personnel ou conflictuel, simulation (QC30), trouble factice (6D50) ou demande de certifica
- Statut : **complet**.

### LOT_213

- Package 5/5 : true. Dossier ASSIGN `1dOFE-MKyp_F8VU-bbh4CCCqgjLeXDM1Y`. Fichier A retenu : Agent_1 | LOT_213 Appel A — Plan et liste des différentiels.html.
- Note package : Agent_1.
- SSP : 14/14. Partie 1 « Définition et cadre conceptuel ». Partie 14 « Pièges ».
- analyze14 Appel A : 1 run de 14, longueurs [14]. analyze14: au moins un run 1..14 (plan SSP). Les runs plus courts éventuels viennent de listes numérotées internes, pas d'un second plan SSP.
- DD : 10/10, verdict OK_14. LOT_213_B_P1.html (2×14), LOT_213_B_P2.html (3×14), LOT_213_B_P3.html (2×14), LOT_213_B_P4.html (3×14).
- Entités DD :
  - DX.1 (B_P1, 14 parties) — DX.1 — Trouble dépressif ou anxieux avec risque suicidaire chez la personne gravement malade (crise suicidaire)
  - DX.2 (B_P1, 14 parties) — DX.2 — Détresse psychosociale d’adaptation à une maladie grave (trouble de l’adaptation, CIM-11 6B43)
  - DX.3 (B_P2, 14 parties) — DX.3 — Détresse spirituelle ou existentielle
  - DX.4 (B_P2, 14 parties) — DX.4 — Épuisement du proche aidant
  - DX.5 (B_P2, 14 parties) — DX.5 — Deuil anticipé, deuil compliqué ou trouble de deuil prolongé (CIM-11 6B42)
  - DX.6 (B_P3, 14 parties) — DX.6 — Isolement social et solitude
  - DX.7 (B_P3, 14 parties) — DX.7 — Précarité socio-économique et besoin d’aide sociale ou administrative
  - DX.8 (B_P4, 14 parties) — DX.8 — Violence domestique ou maltraitance d’une personne vulnérable
  - DX.9 (B_P4, 14 parties) — DX.9 — Personne migrante : barrière linguistique, exil et traumatisme
  - DX.10 (B_P4, 14 parties) — DX.10 — Désir de mourir et demande d’assistance au suicide
- Statut : **complet**.

### LOT_212

- Package 5/5 : true. Dossier ASSIGN `1GUuXmSG0DsP1bcP_FQ30sBURlnQeSEuT`. Fichier A retenu : Agent_1 | LOT_212 Appel A — Plan et liste des différentiels.html.
- Note package : Agent_1.
- SSP : 14/14. Partie 1 « Définition et cadre ». Partie 14 « Pièges et questions d’examen ».
- analyze14 Appel A : 1 run de 14, longueurs [14]. analyze14: au moins un run 1..14 (plan SSP). Les runs plus courts éventuels viennent de listes numérotées internes, pas d'un second plan SSP.
- DD : 10/10, verdict OK_14. LOT_212_B_P1.html (2×14), LOT_212_B_P2.html (3×14), LOT_212_B_P3.html (2×14), LOT_212_B_P4.html (3×14).
- Entités DD :
  - DX.1 (B_P1, 14 parties) — DX.1 — Douleur cancéreuse nociceptive insuffisamment contrôlée et exacerbations douloureuses
  - DX.2 (B_P1, 14 parties) — DX.2 — Nausées et vomissements chroniques d’origine médicamenteuse, toxique ou métabolique
  - DX.3 (B_P2, 14 parties) — DX.3 — Constipation induite par les opioïdes et fécalome
  - DX.4 (B_P2, 14 parties) — DX.4 — Délirium avec agitation de la phase avancée et terminale
  - DX.5 (B_P2, 14 parties) — DX.5 — Occlusion intestinale maligne
  - DX.6 (B_P3, 14 parties) — DX.6 — Douleur neuropathique ou mixte d’origine cancéreuse
  - DX.7 (B_P3, 14 parties) — DX.7 — Compression médullaire métastatique
  - DX.8 (B_P4, 14 parties) — DX.8 — Hypercalcémie tumorale
  - DX.9 (B_P4, 14 parties) — DX.9 — Neurotoxicité des opioïdes, surdosage et intoxication
  - DX.10 (B_P4, 14 parties) — DX.10 — Souffrance réfractaire globale (« douleur totale ») et indication de sédation palliative
- Statut : **complet**.

### LOT_211

- Package 5/5 : true. Dossier ASSIGN `1jbs4hOW-I_KgpxD7ZO0EAZ6sw9f6jxrt`. Fichier A retenu : Agent_1 | LOT_211 Appel A — Plan et liste des différentiels.html.
- Note package : Agent_1.
- SSP : 14/14. Partie 1 « Définition et cadre ». Partie 14 « Pièges et questions d’examen ».
- analyze14 Appel A : 1 run de 14, longueurs [14]. analyze14: au moins un run 1..14 (plan SSP). Les runs plus courts éventuels viennent de listes numérotées internes, pas d'un second plan SSP.
- DD : 10/10, verdict OK_14. LOT_211_B_P1.html (2×14), LOT_211_B_P2.html (3×14), LOT_211_B_P3.html (2×14), LOT_211_B_P4.html (3×14).
- Entités DD :
  - DX.1 (B_P1, 14 parties) — DX.1 — Douleur non contrôlée de la phase terminale
  - DX.2 (B_P1, 14 parties) — DX.2 — Affections buccales : xérostomie, stomatite, mycose buccale
  - DX.3 (B_P2, 14 parties) — DX.3 — Dyspnée terminale
  - DX.4 (B_P2, 14 parties) — DX.4 — Délirium terminal et agitation
  - DX.5 (B_P2, 14 parties) — DX.5 — Anxiété et détresse existentielle
  - DX.6 (B_P3, 14 parties) — DX.6 — Nausées et vomissements
  - DX.7 (B_P3, 14 parties) — DX.7 — Constipation, fécalome et rétention urinaire
  - DX.8 (B_P4, 14 parties) — DX.8 — Râle du mourant
  - DX.9 (B_P4, 14 parties) — DX.9 — Cause réversible mimant l’agonie : intoxication aux opioïdes, hypercalcémie
  - DX.10 (B_P4, 14 parties) — DX.10 — Urgence terminale : hémorragie massive, crise d’épilepsie
- Statut : **complet**.

## Incomplets

Aucun.
