# Audit médical — fiches Status S-13 à S-24 (14.11.2026)

L'auditeur est indépendant et n'a rédigé aucune fiche. Il applique les skills `medecin-expert` et `expert-web`.

**Méthode.** L'auditeur a fait les lectures suivantes :
- les 12 JSON en entier ;
- les 10 images `img/S-13…S-24_*.jpg` ;
- les **résumés PubMed** de 7 sources : Hegedus 2012 (PMID 22773322), van der Windt 2010 (20166095), Benjaminse 2006 (16715828), Bachmann 2003 (12595378), Wells 2006 (16403932), D'Arcy 2000 (10865306), HerniaSurge 2018 (29330835) ;
- les métadonnées Commons (API) de 9 fichiers sur 10.

`Elevated_JVP1.jpg` reste **non revérifié** (HTTP 429). Il a aussi contrôlé les codes EPA (2o–2bb, 2q, 2t, 2v) dans les notes PROFILES et les intitulés SY-xx dans `recensement_sf.json`.

## 1. Synthèse

| Gravité | Nombre | Fiches |
|---|---|---|
| Critique | 0 | — |
| Majeur | 2 | S-17 (Schober inversé), S-13 (image génitale sans signe lisible) |
| Mineur | 24 | toutes sauf S-15 |

**Verdict : corrections requises.** Les 2 majeurs bloquent l'`audit-ok`. Les mineurs peuvent suivre.

**Points vérifiés conformes :**
- **Valeurs chiffrées, conformes au résumé lu** :
  - Lasègue : Se 0,92 (0,87–0,95), Sp 0,28 (0,18–0,40) ; Lasègue croisé : Sp 0,90, Se 0,28 ;
  - Lachman : 85 % (83–87) / 94 % (92–95) ; pivot-shift : 24 / 98 % ; tiroir chronique : 92 / 91 % ;
  - Neer : 72 / 60 % ; Hawkins : 79 / 59 % ; arc douloureux : 53 / 76 % ; « lateral Jobe », « belly-off » et « belly-press » sont cités comme prometteurs ;
  - Ottawa : RV− 0,08 (0,03–0,18) et 0,08 (0,03–0,20), < 1,4 % de fractures à une prévalence de 15 %, 30–40 % de radiographies évitées ; Bachmann travaille bien au Horten-Zentrum de Zurich ;
  - Wells : prévalence de 5,0 / 17 / 53 % ;
  - D'Arcy : RV 3,1 et 1,8 ; Phalen et Tinel « little or no value » ;
  - HerniaSurge : diagnostic clinique, échographie rarement nécessaire.
- **Calcul refait** : IPS 110/140 = 0,786, donc 0,79.
- **Anatomie et technique justes** : collet inguinal au-dessus et en dedans du tubercule pubien, collet fémoral au-dessous et en dehors ; hernie fémorale en dedans des vaisseaux ; Tinel entre le long palmaire et le fléchisseur radial du carpe ; bornes de la tabatière ; Froment ; L5 (talons, extension de l'hallux) et S1 (pointes, achilléen) ; Léri = étirement fémoral (L3–L4) ; fracture du col (raccourcissement, rotation externe) et luxation postérieure (flexion, adduction, rotation interne) ; Trendelenburg (côté d'appui) ; rotation interne de hanche à 90° (pied vers l'extérieur) ; tiroir de genou hanche 45° / genou 90° ; McMurray (rotation externe et valgus pour le ménisque médial) ; Ottawa (6 cm, base du 5e métatarsien, naviculaire, 4 pas) ; Wells (10 cm sous la tubérosité tibiale, −2 points) ; CEAP (C2 ≥ 3 mm, C4, C6) ; Sims.
- **Gestes intimes** : ils sont nommés sans être faits (S-13 invagination, S-14, S-15, S-16 sur patiente). La station « écoulement génital sur modèle » est confirmée par l'Infotext 2026, d'après le rapport des sources.
- **Durées en CS** : 30 s à 4 min par fiche, compatibles avec une station de 11 min utiles.
- **Ordre** : l'ordre topographique tient (aines → pelvis → rachis → membres proximo-distaux → vaisseaux). Les EPA sont exacts.

## 2. Défauts et patchs

### S-13 Aines et orifices herniaires
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Majeur** | manoeuvres_speciales[0].image | **Problème.** La photo (CC0, auteur = uploadeur) montre un pénis et un scrotum nus de face. La voussure inguinale « discrète » n'est **pas identifiable** à la lecture : la nudité génitale n'a donc aucun gain pédagogique. **Patch.** Remplacer par `{"a_fournir":"Photo réelle d'une hernie inguinale franche, debout, cadrée sur l'aine, organes génitaux couverts (Commons CC BY/PD ou figurant consentant, CC BY 4.0)"}`. À défaut, conserver derrière une fenêtre occultante et corriger la légende : « voussure à peine visible ». |
| Mineur | materiel[1] | « lampe pour la transillumination » : aucun geste de S-13 ne l'emploie. **Patch :** retirer (elle figure en S-14). |

### S-14 Organes génitaux masculins
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | manoeuvres_speciales[1].image | **Problème.** L'uploadeur (UneAutreHistoire) diffère de l'auteur déclaré (EvguenieSokolov). Le consentement du sujet n'est pas documenté. **Patch :** afficher derrière une fenêtre occultante et ajouter à la légende « consentement du sujet non documenté sur Commons ». |
| Mineur | gestes « position ».anomalies[2].signifie | « …rechercher une compression veineuse » → « …ou varicocèle qui ne s'affaisse pas couché : rechercher une compression de la veine rénale ou cave (tumeur rénale) → échographie » |

### S-16 Examen gynécologique
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | installation[3] | « (voir S-11/S-12) » → « (voir S-12) » (S-11 traite des seins) |
| Mineur | sources | L'ordre est correct. Ajouter à la légende de l'image : « image intime : fenêtre occultante ». |

### S-17 Rachis
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Majeur** | manoeuvres_speciales[1] (nom, technique[1], positif_si) ; examen_complet[4].gestes[0].normal | **Problème.** Les variantes sont inversées. Deux repères (jonction lombo-sacrée + 10 cm) définissent le Schober **original**. Le Schober **modifié** (Macrae-Wright) ajoute un repère 5 cm **au-dessous** ; le normal est alors ≥ 20 cm. **Patch.** nom : « Test de Schober (modifié) » → « Test de Schober ». technique[1] : « (épineuse de L5) » → « (jonction lombo-sacrée) ». positif_si : « …(Schober original avec repère 5 cm sous L5) » → « La distance de 10 cm augmente de moins de 5 cm. Variante modifiée : repères 5 cm sous et 10 cm au-dessus de la jonction, normal ≥ 20 cm (À vérifier) ». normal : « le Schober modifié augmente » → « le Schober augmente ». |
| Mineur | manoeuvres_speciales[0].technique[4] | « fléchir le pied » → « mettre le pied en flexion dorsale » |
| Mineur | gestes[1] (rachis cervical) | « (Spurling, À vérifier) » : la fiche ne décrit pas la technique. **Patch :** « (Spurling : extension, inclinaison et rotation vers le côté atteint, puis compression axiale douce ; À vérifier) » |
| Mineur | manoeuvres_speciales[2].image | La photo montre probablement une **mineure**, de dos, non identifiable (article SOSORT, CC BY 2.0, vérifiée sur Commons). **Patch :** vérifier dans *Scoliosis* 2006;1:11 la mention du consentement, puis l'ajouter au crédit. |

### S-18 Épaule
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | gestes « mobilité ».anomalies[1].signifie | « capsulite rétractile ou omarthrose » → « capsulite rétractile ou omarthrose (SY-59) » (SY-59 est listé mais jamais cité) |
| Mineur | version_cs.a_dire[4] | « Puis j'examine la nuque » contredit installation[3] (rachis d'abord). **Patch :** déplacer « J'examine d'abord la nuque » en tête de a_dire[0]. |
| Mineur | sources | Placer Duale Reihe (Europe) **avant** Hegedus (américain). |

### S-19 Coude, poignet, main
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | manoeuvres_speciales[0].valeur ; gestes[3] | **Problème.** Le résumé dit « hypalgesia ». **Patch.** « l'hypoesthésie du territoire médian (RV 3,1) » → « l'hypoalgésie à la piqûre de la pulpe de l'index (RV 3,1 ; IC 2,0–5,1) ». Ajouter : « amyotrophie thénar, Phalen, Tinel, monofilament : peu ou pas de valeur ». |
| Mineur | gestes[1].anomalies[2] | Le Finkelstein n'est pas décrit. **Patch :** « (Finkelstein : pouce fléchi dans le poing, inclinaison ulnaire passive du poignet) » |
| Mineur | syndromes_lies | « SY-61 » n'est pas cité. **Patch :** ajouter `{"signe":"avant-bras tendu, douleur à l'extension passive des doigts après traumatisme","signifie":"syndrome des loges (SY-61) → aponévrotomie urgente"}`, ou retirer SY-61. |
| Mineur | sources | Placer Duale Reihe avant D'Arcy (américain). |

### S-20 Hanche
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | gestes[1].anomalies[0].signifie (Thomas) | « flessum de hanche » → « flessum de la hanche **controlatérale** (celle qui se soulève) » |
| Mineur | examen_complet[4] | Le FABER (Patrick) manque : il distingue une douleur sacro-iliaque d'une douleur coxo-fémorale. **Patch :** ajouter le geste « flexion-abduction-rotation externe, talon sur le genou opposé » ; normal « genou proche de la table, indolore » ; anomalie « douleur inguinale (hanche) ou fessière postérieure (sacro-iliaque, SY-58) ; valeur À vérifier ». |
| Mineur | sources[2] | « Aucune source suisse… » n'est pas une source. **Patch :** déplacer cette mention dans `valeur`. |

### S-21 Genou
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | manoeuvres_speciales[0].technique[2] | « Il tire brusquement le tibia vers l'avant » → « Il tire fermement le tibia vers l'avant, sans à-coup » (un geste brusque déclenche une contraction de défense, d'où un faux négatif) |
| Mineur | gestes[0].anomalies[3].signifie | « règle d'Ottawa du genou (À vérifier) » → « radiographie si âge ≥ 55 ans, douleur isolée de la rotule ou de la tête fibulaire, flexion < 90° ou 4 pas impossibles (source canadienne : Stiell, non lue, À vérifier) » |

### S-22 Cheville et pied
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | installation[2] | « si la règle d'Ottawa le permet » → « (le test des 4 pas fait partie de la règle d'Ottawa) » |
| Mineur | syndromes_lies | « SY-61 » n'est pas cité. **Patch :** retirer, ou ajouter « syndrome des loges de jambe après fracture (SY-61) » à anomalies[1].signifie. |

### S-23 Artères périphériques
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | gestes[0] IPS .normal | « IPS entre 0,91 et 1,40 » → « IPS 1,00–1,40 ; 0,91–0,99 = zone limite (À vérifier, ESC 2024) » |
| Mineur | manoeuvres_speciales[1].valeur | « À vérifier » → harmoniser avec le patch S-12 : « LR+ 12 pour une aorte élargie (source américaine : Lederle FA, JAMA 1999 — résumé lu par l'audit S-01–S-12) » |
| Mineur | sources[1] | Citer l'original : « Eur Heart J 2024;45:3538-3700 » plutôt que la traduction italienne. |

### S-24 Veines
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | manoeuvres_speciales[0].image.legende | **Problème.** La flèche vise une veine oblique sur le sterno-cléido-mastoïdien, probablement la **jugulaire externe**. La licence n'est pas revérifiée (429). **Patch :** ajouter « ; veine visible probablement externe : la mesure se fait sur la jugulaire interne. Licence à revérifier ». |
| Mineur | manoeuvres_speciales[1].technique[2] | **Problème.** La fiche mélange deux versions : le seuil à 3 niveaux vient de Wells 1997 (sans l'item « antécédent de TVP »), le seuil à 2 niveaux de Wells 2003. **Patch :** préciser « 3 niveaux : score original de 1997 ; 2 niveaux : score modifié de 2003 (avec antécédent de TVP) ». |
| Mineur | sources[3] et gestes varices | « source internationale, American Venous Forum » → « source américaine : American Venous Forum, CEAP 2020 » ; placer cette source après Duale Reihe. |
| Mineur | manoeuvres_speciales[0] | Doublon de S-10 (pression veineuse jugulaire). **Patch :** ajouter « (voir aussi S-10) ». |

## 3. Question finale
**Publiable en l'état ? Non.** Deux corrections manquent : (1) Schober original et modifié inversés (S-17) ; (2) photo génitale sans signe lisible (S-13). Après ces deux patchs, l'`audit-ok` devient possible, à deux réserves près : revérifier la licence de `Elevated_JVP1.jpg` et le consentement des sujets de S-14 et S-17. Les valeurs « À vérifier » restantes (Thompson, McMurray, Trendelenburg, tiroir de cheville, réflexe crémastérien) sont honnêtement étiquetées. Elles ne bloquent pas.
