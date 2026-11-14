# Audit médical — fiches Status S-01 à S-12 (14.11.2026)

Auditeur indépendant (aucune rédaction des fiches). Posture : skill `medecin-expert`, recherche : skill `expert-web`.
Méthode : lecture intégrale des 12 JSON ; lecture des 23 images (`img/S-01…S-12_*.jpg`) ; lecture du texte allemand de l'Infotext MED 2026 (pdftotext, § 5) ; lecture des **résumés PubMed** de 11 articles JAMA « Rational Clinical Examination » (source américaine) et du résumé ESCMID 2012 ; lecture des pages Commons de 2 fichiers. L'API Commons a refusé les autres requêtes (HTTP 429) : les licences des 21 autres fichiers restent **non revérifiées**. La recommandation SSI « Pharyngitis 2023 » (ssi.guidelines.ch/guideline/2408) ne s'est pas affichée : elle reste non lue.

## 1. Synthèse

| Gravité | Nombre | Fiches |
|---|---|---|
| Critique | 2 | S-05 (image d'un détenu de Guantánamo), S-12 (image sous droit d'auteur NEJM) |
| Majeur | 6 | S-04, S-08 (×2), S-11 (×2), S-01 |
| Mineur | 52 | toutes |

**Verdict : corrections requises.** Après application des patchs critiques et majeurs, les fiches seront publiables. Les mineurs pourront suivre.

Points conformes, vérifiés : séquence I-P-P-A et foyers USZ (S-09, S-10) ; Weber/Rinne (S-06) ; DPAR, anisocorie, confrontation (S-05) ; Centor/McIsaac (critères, +1 entre 3 et 14 ans, −1 dès 45 ans) ; NRS-2002 ; EWGSOP2 27/16 kg ; matité déclive mobile et sens du flux sous l'ombilic (S-12) ; IMC 70/1,75² = 22,86, arrondi juste à 22,9 (calcul refait) ; les valeurs d'Ebell 2016 (LR+ 3,1 ; 3,0–3,1 ; 5,3 ; LR 0,23–0,44) sont exactes selon le résumé lu. L'ordre des fiches suit la topographie ; S-11 (seins, 2cc) précède l'abdomen (2w) contre l'ordre PROFILES, ce qui reste justifié par la région Thorax. Les gestes sont rédigés en phrases verbales. Les sources sont classées Suisse → Allemagne → États-Unis → OMS. Les durées CS (1 à 4 min par fiche) restent compatibles avec une station de 13 min à signal de 11 min, qui comprend aussi l'anamnèse et le management.

## 2. Défauts et patchs par fiche

### S-01 Impression générale et signes vitaux
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Majeur | examen_complet[Manœuvres].gestes[0].normal | « PA < 140/90 mmHg au cabinet » → « Pas d'HTA si PA < 140/90 mmHg au cabinet ; l'ESC 2024 classe 120–139/70–89 en « PA élevée » (source européenne : ESC 2024, À vérifier ; position de la Société suisse d'hypertension non lue) » |
| Mineur | idem gestes[2].anomalies[0].signe | « (< 3,0 : sévère) » → « (< 3,0 : hypoglycémie de niveau 2 ; « sévère » = besoin d'aide d'un tiers) » |
| Mineur | idem gestes[1].anomalies[1].signifie | « sepsis grave (SY-79) » → « sepsis à haut risque (SY-79) » (Sepsis-3 a supprimé « sepsis grave ») |
| Mineur | manoeuvres_speciales[0].technique[3] | « répète et retient la moyenne » → « répète 3 fois à 1–2 min d'intervalle et retient la moyenne des 2 dernières (source européenne : ESC 2024, À vérifier) » |
| Mineur | manoeuvres_speciales[0].image.legende | « membrane sur l'artère humérale, lecture du manomètre » → « brassard au bras gauche, stéthoscope en place ; la membrane n'est pas visible. Photo de dépistage public, filigrane mmsapublichealth » |
| Mineur | syndromes_lies | ajouter « SY-35 », « SY-67 » (cités dans le texte) |

### S-02 État nutritionnel
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | gestes « perte de poids ».anomalies[0].signe | « perte > 5 % en 3 mois ou > 10 % en 6 mois » → « perte > 5 % en 6 mois ou > 10 % au-delà de 6 mois (source internationale : critères GLIM 2019, non lus, À vérifier) » |
| Mineur | gestes « signes de carence ».anomalies | ajouter `{"signe":"hémorragies périfolliculaires, poils en tire-bouchon, gingivite","signifie":"scorbut (carence en vitamine C)"}` |
| Mineur | syndromes_lies | retirer « SY-51 » (jamais cité) ou le citer explicitement |
| Mineur | sources | ajouter « Société suisse de nutrition clinique (GESKES) — recommandations non lues, À vérifier » avant la ligne ESPEN (ordre Suisse d'abord) |

### S-03 Peau, phanères, muqueuses
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | manoeuvres_speciales[2].image | La photo `S-03_schamroth.jpg` montre deux doigts fléchis sans fenêtre lisible ; la légende de l'auteur (« negative window test ») est ambiguë. → remplacer par une photo montrant clairement la fenêtre losangique, sinon `{"a_fournir":"Photo réelle des deux index accolés dos à dos : fenêtre losangique visible (normal) puis absente (hippocratisme)"}` |
| Mineur | examen_complet[Palpation].gestes[1] et [2] | Doublons de S-02 (godet, pli cutané). → garder dans S-03 et renvoyer dans S-02 : « (détail en S-03) » |
| Mineur | gestes[1].anomalies[4].signifie | « prurit de cholestase (SY-35) ou d'urémie (SY-42) » → « gale, dermatose prurigineuse, ou prurit de cholestase (SY-35) ou d'urémie (SY-42) » |
| Mineur | manoeuvres_speciales[0].image.legende | « thrombopénie d'un PTI » : la cause n'est pas vérifiée sur Commons (API refusée). → « Purpura pétéchial de jambe : montre le signe positif, pas le geste de vitropression. » |

### S-04 Aires ganglionnaires
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Majeur** | examen_complet[Palpation].gestes[3].geste | « en arrière de l'épicondyle médial » → « 3 cm au-dessus de l'épicondyle médial, dans le sillon entre biceps et triceps » (en arrière de l'épicondyle se trouve le nerf ulnaire, pas le ganglion) |
| Mineur | idem gestes[3].normal | « Non palpable. » → « Non palpable ; un ganglion épitrochléen > 0,5 cm est anormal (À vérifier) » |
| Mineur | syndromes_lies | retirer « SY-63 », « SY-79 » (non cités) |

### S-05 Yeux
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Critique** | manoeuvres_speciales[2].image | `Detainee_Medical_Care_DVIDS300716.jpg` montre un **détenu de Guantánamo** (page Commons lue : « A detainee receiving a routine checkup… Joint Task Force Guantanamo »). Le consentement libre est impossible à établir dans ce contexte. La légende masque ce fait. → retirer le fichier ; `{"a_fournir":"Photo réelle d'un fond d'œil à l'ophtalmoscope direct : main droite et œil droit de l'examinateur pour l'œil droit du figurant, pouce sur le sourcil"}` |
| Mineur | gestes « oculomotricité ».anomalies[1].signe | « unidirectionnel, épuisable » → « unidirectionnel, horizonto-rotatoire, inhibé par la fixation » (« épuisable » décrit le nystagmus positionnel du VPPB) |
| Mineur | idem anomalies[0].signifie | « paralysie du VI : hypertension intracrânienne (SY-6) » → « paralysie du VI : hypertension intracrânienne (SY-6) ou atteinte microvasculaire (diabète, HTA) » |
| Mineur | gestes « pupilles ».anomalies[3].signifie | ajouter « ou sympathomimétique (cocaïne, amphétamines) » |
| Mineur | materiel[0] | « chiffres de Monoyer » → « échelle de Monoyer » |
| Mineur | manoeuvres_speciales[1].technique[1] | « fixe le nez de l'examinateur » → « fixe l'œil ouvert de l'examinateur » |
| Mineur | examen_complet | ajouter un geste « vision des couleurs (Ishihara) et désaturation du rouge » : l'EPA 2g–2j et le matériel le prévoient, aucun geste ne le décrit |
| Mineur | manoeuvres_speciales[4].image | `Anisocoria.jpg` : différence à peine visible. → remplacer par une anisocorie franche, ou légender « différence discrète ; mieux visible dans la pénombre » |
| Mineur | sources[3] | « (source européenne : Société européenne d'ophtalmologie — aucune recommandation suisse publique lue…) » → supprimer (aucune source réelle citée) |

### S-06 Oreilles
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | manoeuvres_speciales[0].valeur (Weber) | « À vérifier » → « Weber anormal LR+ 1,6 ; normal LR 0,70 (source américaine : Bagai A et al., JAMA 2006;295:416-28 — résumé lu) » |
| Mineur | manoeuvres_speciales[1].valeur (Rinne) | « À vérifier » → « Rinne anormal LR+ 2,7–62 ; normal LR 0,01–0,85 (source américaine : Bagai 2006 — résumé lu) » |
| Mineur | gestes « voix chuchotée ».anomalies[0].signifie | ajouter « (non-perception LR+ 6,1 ; perception normale LR 0,03 — source américaine : Bagai 2006, résumé lu) » |
| Mineur | gestes « otoscopie ».anomalies | ajouter `{"signe":"perforation marginale ou attique avec squames blanchâtres, otorrhée fétide","signifie":"cholestéatome : avis ORL"}` |
| Mineur | sources[2] | « (source européenne : aucune recommandation suisse…) » → « (source américaine : Bagai A et al., Does this adult patient have hearing impairment? JAMA 2006;295:416-28 — résumé lu) » |
| Mineur | syndromes_lies | « SY-4 » non cité : ajouter dans version_cs.cible « vertige (SY-4) » ou le retirer |
| Mineur | manoeuvres_speciales[2].image.legende | ajouter « ; prise en poing, sans appui de la main sur la joue : technique imparfaite » |

### S-07 Nez, bouche, pharynx
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | manoeuvres_speciales[0].valeur | → « Recommandation SSI « Pharyngitis 2023 » non lue, À vérifier ; (source européenne : ESCMID Sore Throat Guideline 2012, résumé lu : test rapide à envisager pour 3–4 critères de Centor ; pas d'antibiotique pour 0–2) » |
| Mineur | gestes « ganglions cervicaux ».anomalies[1].signifie | « mononucléose (LR+ 3,1) » → « mononucléose (LR+ 3,1) (source américaine : Ebell 2016) » |
| Mineur | version_cs.a_dire[2] | « soit 4 points » → « soit 4 points ; j'ajuste selon l'âge (McIsaac) » |

### S-08 Cou, thyroïde, carotides
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Majeur** | gestes « carotide ».geste | « sous l'angle de la mandibule » → « au tiers inférieur du cou, à hauteur du cartilage cricoïde, en dedans du SCM, loin du sinus carotidien (bifurcation au bord supérieur du cartilage thyroïde) » |
| **Majeur** | manoeuvres_speciales[0].technique[2] | « en arrière du sterno-cléido-mastoïdien » → « entre la trachée et le bord antérieur du sterno-cléido-mastoïdien, en refoulant légèrement ce muscle » (le lobe thyroïdien est en avant et en dedans du SCM) |
| Mineur | gestes « auscultation carotide ».geste | « à l'angle de la mandibule » → « du creux sus-claviculaire à l'angle de la mandibule » (un souffle aortique irradié se reconnaît à la base) |
| Mineur | syndromes_lies | retirer « SY-15 » (non cité) |

### S-09 Thorax et poumons
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | gestes « excursion diaphragmatique ».normal | « 4–6 cm » → « ≈ 3–5 cm (À vérifier) » |
| Mineur | manoeuvres_speciales[2].valeur | « À vérifier » → « Aucun signe isolé ne confirme une pneumonie ; des signes vitaux et une auscultation normaux la rendent peu probable (source américaine : Metlay JP et al., JAMA 1997;278:1440-5 — résumé lu) » |
| Mineur | manoeuvres_speciales[2].image.legende | ajouter « ; stéthoscope sur l'omoplate : le placer dans l'espace paravertébral » |
| Mineur | syndromes_lies | ajouter « SY-24 » (cité), retirer « SY-31 » ou le citer (hypercapnie) |

### S-10 Cœur
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | manoeuvres_speciales[2].valeur (pouls paradoxal) | « À vérifier » → « Chez un patient avec épanchement péricardique : > 10 mmHg LR+ 3,3 ; ≤ 10 mmHg LR 0,03 (source américaine : Roy CL et al., JAMA 2007;297:1810-8 — résumé lu) » |
| Mineur | manoeuvres_speciales[3].image.legende | ajouter « ; la photo montre la jugulaire **externe**, la mesure se fait sur la jugulaire interne » |
| Mineur | sources[4] | « ESC 2021 Guidelines for heart failure » → « ESC 2021 Guidelines for heart failure et mise à jour ciblée 2023 » |

### S-11 Seins
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Majeur** | duree.cs ; version_cs.a_nommer_sans_faire[0] | « (consigne MEBEKO 2026) » → « (déduction : l'Infotext 2026 exclut les « Untersuchungen im Intimbereich » sans nommer les seins ; texte lu) » |
| **Majeur** | manoeuvres_speciales[0].image.legende | « visage hors champ » est inexact : le menton et la bouche sont visibles. → « …photo de modèle, bas du visage visible » ; voir l'avis § 3 |
| Mineur | gestes « inspection ».anomalies[4].signifie | ajouter « , tumeur testiculaire » |
| Mineur | gestes « écoulement ».anomalies[1].signifie | ajouter « , hypothyroïdie » |
| Mineur | syndromes_lies | retirer « SY-65 » ou le citer |

### S-12 Abdomen
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Critique** | manoeuvres_speciales[0].image | `Caput_medusae.jpg` provient du **NEJM 2005;353:e19** (page Commons lue). La licence porte la mention « Attribution » sans preuve d'autorisation de la Massachusetts Medical Society. Ce n'est donc pas une licence libre vérifiée. → retirer ; `{"a_fournir":"Photo réelle libre d'une circulation collatérale péri-ombilicale (Commons CC BY/PD ou Europe PMC CC BY relue)"}` |
| Mineur | manoeuvres_speciales[2].valeur (Murphy) | → « LR+ 2,8 (IC 95 % 0,8–8,6) ; aucun signe isolé ne confirme ni n'exclut la cholécystite (source américaine : Trowbridge RL et al., JAMA 2003;289:80-6 — résumé lu) » ; même correction dans sources[7] (« non lus » → « résumé lu » pour Trowbridge) |
| Mineur | manoeuvres_speciales[6].valeur (psoas) | « À vérifier (Wagner 1996, non lu) » → « Le psoas positif augmente la probabilité d'appendicite ; LR non chiffré dans le résumé (source américaine : Wagner 1996, résumé lu) » |
| Mineur | manoeuvres_speciales[4].technique[0] (Blumberg) | « sur une zone à distance ou sur la zone suspecte » → « sur la zone suspecte » |
| Mineur | gestes « palpation profonde » | ajouter `{"geste":"Il mesure la largeur de l'aorte des deux mains, de part et d'autre de la pulsation, au-dessus de l'ombilic.","normal":"< 3 cm","anomalies":[{"signe":"aorte élargie ≥ 3 cm","signifie":"anévrisme (LR+ 12 ; sensibilité 76 % si ≥ 5 cm — source américaine : Lederle FA, JAMA 1999;281:77-82, résumé lu)"}]}` |
| Mineur | gestes « Manœuvres ».geste | « …matité déclive mobile, flot. » : le flot n'est décrit nulle part. → ajouter la technique, ou retirer « flot » |
| Mineur | version_cs.a_nommer_sans_faire[1] | « Examen des orifices herniaires… (examen intime) » → « Examen des organes génitaux externes (examen intime, Infotext 2026) ; orifices herniaires : à nommer si l'examen exige d'invaginer le scrotum (déduction) » |
| Mineur | syndromes_lies | retirer « SY-39 » (non cité) |

## 3. Avis sur l'image S-11 (décision finale à Vial)
- **Licence** : NCI, domaine public selon la fiche. La licence n'a pas été revérifiée (API Commons refusée).
- **Pertinence pédagogique** : réelle mais faible. La photo montre bien la position « mains sur les hanches », mais elle ne montre aucun signe. La posture peut s'enseigner sans nudité.
- **Risques** : photo artistique en noir et blanc d'une modèle torse nu, bas du visage visible, dans un dépôt public. Elle n'apporte rien qu'une figurante en brassière ne montrerait pas.
- **Recommandation** : (1) préférer une photo de la posture sur figurante habillée, sous CC BY 4.0 ; (2) à défaut, recadrer sous le menton (le domaine public le permet) et afficher l'image derrière une fenêtre occultante, avec la mention « image médicale ».

## 4. Question finale
**Publiable en l'état ? Non.** Il manque : le retrait des 2 images critiques (S-05, S-12), la correction des 3 gestes faux (épitrochléen, niveau de palpation carotidienne, lobe thyroïdien), la requalification « déduction » de la consigne MEBEKO pour les seins, et l'ajustement du seuil de PA. Après ces patchs : audit-ok possible, sous réserve de revérifier les 21 licences Commons non relues (HTTP 429).
