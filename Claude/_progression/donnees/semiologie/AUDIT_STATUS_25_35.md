# Audit médical — fiches Status S-25 à S-35 (14.11.2026)

Auditeur indépendant : je n'ai rédigé aucune de ces fiches. J'ai appliqué les skills `medecin-expert` et `expert-web`.

**Méthode.**
- J'ai lu en entier les 11 JSON et regardé les 29 images `img/S-25…S-35_*`.
- J'ai lu les pages Commons de 19 fichiers (wikitext et extmetadata). Les 10 autres licences n'ont pas été revérifiées : HTTP 429.
- J'ai lu les textes suivants :
  - PROFILES 2017, EPA 2a–2mm ;
  - Infotext MED 2026 (fr, § 5) ;
  - résumés PubMed : Thomas 2002, Kattah 2009, Uchihara 1991 ;
  - ASSM 2019 « La capacité de discernement dans la pratique médicale » (PDF, § 2.4–2.5) ;
  - art. 253 CPP (reproduction juriup) et art. 379 CC ;
  - Kuelling, SMW 2009;139:699 (protocole suisse d'oxymétrie de 2005) ;
  - communiqué de pédiatrie suisse du 16.06.2026 (nouvelles courbes) ;
  - HUG/SMPR « Vertiges » 2024 et « Personnes âgées » 2026.
- J'ai refait les calculs avec un outil : Sp = 1 − Se/LR+ ; somme Apgar ; somme GCS.
- `controle.py` ne couvre pas `semiologie/status` : aucun contrôle mécanique ne s'applique.

## 1. Synthèse

| Gravité | Nombre | Fiches |
|---|---|---|
| Critique | 1 | S-30 (image sous droit d'auteur Elsevier déclarée « PD-self ») |
| Majeur | 10 | S-28 (×2), S-32 (×3), S-33, S-30, S-25, S-34, S-35 |
| Mineur | 24 | toutes |

**Verdict : corrections requises.**

**Points conformes, vérifiés :**
- L'Infotext MED 2026 § 5 exclut bien la sphère intime, le réflexe cornéen et le réflexe nauséeux, et prévoit les cartes, photos et vidéos. S-25, S-29 et S-35 sont donc exacts.
- Les codes EPA 2dd, 2ee, 2ff, 2gg–2ii, 2jj, 2u, 2c et 2d sont exacts (S-35 fait exception, voir plus bas).
- GCS « Y2 V2 M4 = 8 » : la somme est juste.
- Les valeurs de Kattah 2009 (Se 100 %, Sp 96 %) figurent dans le résumé.
- Les Sp de Thomas 2002 (95 % et 68 %) se recalculent à partir des LR+ du résumé : 0,948 et 0,681.
- L'art. 253 CPP existe ; son al. 4 confie aux cantons le devoir d'annonce.
- L'ASSM 2019 existe (Sénat du 29.11.2018).
- La neuro-anatomie est juste dans les quatre fiches neurologiques : III, IV et VI, Weber/Rinne, XI–XII, confrontation, Brown-Séquard, Romberg, réflexes et racines, MRC, décortication et décérébration.

## 2. Défauts et patchs

### S-25 Nerfs crâniens
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Majeur** | manoeuvres_speciales[9] (HINTS) | Valeur « non relu… À vérifier » → « Se 100 %, Sp 96 % chez 101 patients avec syndrome vestibulaire aigu et ≥ 1 facteur de risque vasculaire (source américaine : Kattah JC et al., Stroke 2009;40:3504-10 — résumé lu) ». Ajouter en technique[4] : « HINTS+ : il teste l'audition (frottement des doigts) ; une hypoacousie aiguë impose de penser à un AVC de l'artère cérébelleuse antéro-inférieure, même si le HINTS paraît périphérique (HUG/SMPR, Vertiges 2024 — Suisse, lu) ». Retirer « par des neuro-otologistes » : la mention ne figure pas dans le résumé. |
| Mineur | sources[6] | « résumé seulement, À vérifier » → « résumé lu » ; ajouter « HUG/SMPR, Stratégie Vertiges 2024, DOI 10.53738/REVMED.2024.20.888.1702 — Suisse, lu » en tête des sources de technique. |
| Mineur | manoeuvres_speciales[1].image.credit | ajouter « ; montre l'effet de la lumière sur la pupille, pas le geste de la lampe oscillante ». |
| Mineur | manoeuvres_speciales[4].image | Visage entier d'une « volontaire » sans modèle de consentement sur Commons → recadrer sous les yeux, ou garder en indiquant « volontaire (page Commons) ». |

### S-26 Motricité, tonus, réflexes
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | manoeuvres_speciales[5].positif_si | « Secousses rythmiques inépuisables (plus de 3 à 5 battements) » → « Secousses rythmiques inépuisables, qui persistent tant que la dorsiflexion est maintenue (au-delà de 5 battements) ». |
| Mineur | examen_complet[Manœuvres].gestes[0] et manoeuvres_speciales[7].nom | « épreuve de Barré » appliquée aux bras → « épreuve des bras tendus » (la manœuvre de Barré classique se fait aux membres inférieurs, en procubitus). |
| Mineur | syndromes_lies | ajouter SY-31, SY-37, SY-42, SY-50, SY-55, SY-72 (cités dans le texte). |
| Mineur | manoeuvres_speciales[0].technique[4] | la cotation 0–4+ suit l'échelle NINDS (source américaine) → ajouter « (échelle NINDS, source américaine, non relue) ». |

### S-27 Sensibilité, coordination, marche
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | manoeuvres_speciales[3].positif_si | « Au moins un point non perçu » → « Sensibilité protectrice absente à un site si au moins 2 réponses fausses sur 3 (deux applications réelles, une fictive) ; 3 sites : pulpe du gros orteil, têtes des 1er et 5e métatarsiens (source internationale : IWGDF 2023, non lu, À vérifier) ». |
| Mineur | examen_complet[Manœuvres].gestes[4].geste | « test de poussée (pull test) » → « test de rétropulsion (pull test) ». |
| Mineur | manoeuvres_speciales[0].image.credit | ajouter « ; ataxie statique et marche ataxique, pas un Romberg pieds joints yeux fermés ». |

### S-28 Méningisme
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Majeur** | manoeuvres_speciales[1].interpretation et [2].interpretation | « Très spécifique… positif, il renforce fortement l'hypothèse » et « spécifique, peu sensible » → « Chez l'adulte suspect de méningite, le signe n'a aucune valeur discriminante : un signe positif ne change pas la probabilité (LR+ 0,97). Il ne retarde jamais la PL ni l'antibiothérapie. » Le résumé de Thomas 2002 conclut que les « 3 classic meningeal signs did not have diagnostic value ». |
| **Majeur** | manoeuvres_speciales[1].positif_si | « au-delà de 135° de flexion résiduelle » est faux : 135° est l'angle cuisse-jambe, pas la flexion résiduelle → « extension du genou impossible au-delà d'un angle cuisse-jambe d'environ 135° (À vérifier) ». |
| Mineur | manoeuvres_speciales[0], [1], [2].valeur et sources[3] | « non relu en texte intégral » → « résumé lu : Se 5 %, LR+ 0,97 (Kernig, Brudzinski) ; Se 30 %, LR+ 0,94 (raideur de nuque) ; Sp déduites de 95 % et 68 % ; méningite = ≥ 6 GB/µL (source américaine : Thomas KE et al., CID 2002;35:46-52) ». |
| Mineur | manoeuvres_speciales[3].valeur | → « Se 97 % (33/34), Sp 60 % (12/20) pour une pléiocytose, chez 54 patients fébriles avec céphalée récente (source japonaise : Uchihara T, Tsukagoshi H, Headache 1991;31:167-71 — résumé lu) ». |
| Mineur | examen_complet[Manœuvres].gestes[3] | ajouter la source des indications de l'imagerie avant la PL : « (source européenne : ESCMID 2016, van de Beek et al., non lu, À vérifier) ». |
| **Majeur** | manoeuvres_speciales[1].image | Photo de 1909 (Sahli, planche 12) : enfant nu, émacié, « expression of suffering » (page Commons lue). La licence est libre, mais l'image heurte la dignité du patient, sans consentement possible. → l'afficher derrière une fenêtre occultante, avec la légende « enfant, 1909 », ou la remplacer par `a_fournir` (adulte figurant, vue latérale). Décision à Vial. |

### S-29 Coma
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | manoeuvres_speciales[1].image | La page Commons décrit une « anisocoria… unknown causes » chez un adulte vigilant : discrète, elle n'illustre pas une mydriase aréactive de coma → légende : « anisocorie discrète chez un sujet vigilant, sans valeur d'engagement » ; sinon `a_fournir`. |
| Mineur | manoeuvres_speciales[0].valeur | ajouter « mise à jour : Teasdale G et al., Lancet Neurol 2014;13:844-54 (source britannique, non lue) ». |

### S-30 Status mental et cognition
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Critique** | manoeuvres_speciales[0].image | La page Commons de `AllochiriaClock.png` (lue) indique : « taken from… Smith AD et al., Brain & Cognition 2007… The copyright for this image is owned by Elsevier ». La licence « PD-self » est donc fausse. → retirer le fichier ; `{"a_fournir":"Horloge dessinée par un figurant (chiffres groupés à droite, aiguilles sur 11 h 10), scan CC BY 4.0"}`. |
| **Majeur** | examen_complet[Manœuvres].gestes[9].anomalies[0] et manoeuvres_speciales[3].technique, positif_si | Le modèle Appelbaum (comprendre, apprécier, raisonner, exprimer) doit laisser la place aux catégories de l'ASSM 2019 (§ 2.4) : capacité de compréhension, d'évaluation, de se forger une volonté, de concrétiser sa volonté. positif_si → « Une ou plusieurs de ces capacités sont **fortement limitées** pour la décision en jeu (ASSM 2019 § 2.5) ». |
| Mineur | sources[3] | « non relu… À vérifier » → « ASSM 2019 (Sénat 29.11.2018), lu § 2.1–2.5 ». |
| Mineur | manoeuvres_speciales[3].interpretation | « directives anticipées puis représentant thérapeutique (art. 377 ss CC) » → « directives anticipées (art. 370 ss CC), puis représentant (art. 378 CC) ; en urgence, il agit selon la volonté présumée et les intérêts du patient (art. 379 CC, lu) ». |

### S-31 Échographie ciblée
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | examen_complet[Manœuvres].gestes[5].anomalies[0].signe | « collapsus diastolique de l'oreillette ou du ventricule droit » → « collapsus de l'oreillette droite en télédiastole-systole, ou du ventricule droit en diastole ». |
| Mineur | gestes[1].anomalies[1].signifie | ajouter « ; aussi SDRA, pneumopathie interstitielle ». |
| Mineur | epa | PROFILES 2u ne vise que « pleural effusion, abdominal mass, ascites » (texte lu) → préciser « pneumothorax, péricarde, hémopéritoine : au-delà de 2u ». |
| Mineur | syndromes_lies | retirer SY-32 (jamais cité). |

### S-32 Nouveau-né
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Majeur** | version_cs.a_dire[1] | « …grimace, extrémités bleutées : Apgar 9 » → « Apgar 8 » (calcul : 2+2+2+1+1 = 8). |
| **Majeur** | examen_complet[Manœuvres].gestes[3] (oxymétrie) | Le protocole décrit (main droite + pied, écart ≤ 3 %) est le protocole américain. → « Il mesure la SpO2 **au pied** le 1er jour, chez un nouveau-né calme : ≥ 95 % normal ; 90–94 % : examen clinique et contrôle quelques heures plus tard ; < 90 %, ou contrôle < 95 % : échocardiographie (Société suisse de néonatologie et Société suisse de cardiologie pédiatrique 2005, selon Kuelling B, Swiss Med Wkly 2009;139:699-704 — Suisse, lu) ». |
| **Majeur** | manoeuvres_speciales[4].image | `Newborn_Examination_1967.jpg` montre le visage d'un nouveau-né identifiable (Turquie, 2000) sans consentement indiqué (page lue) → recadrer sous le menton, ou `a_fournir`. |
| Mineur | examen_complet | ajouter le dépistage auditif néonatal (OEA) et le test sur buvard dans « à nommer ». |
| Mineur | syndromes_lies | retirer SY-21 (jamais cité). |
| Mineur | manoeuvres_speciales[2].image | nourrisson, visage visible, photo très filtrée → légende « image retouchée ». |

### S-33 Enfant et adolescent
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Majeur** | sources[1], materiel[3], manoeuvres_speciales[0].technique[1] | « courbes de croissance suisses (2011, adaptées des données OMS) » sont caduques. → « Nouvelles courbes nationales recommandées par pédiatrie suisse depuis le 15.06.2026 (PEZZ Zurich, > 43 000 enfants ; OMS pour l'IMC de 0 à 2 ans ; Zurich et KiGGS pour le périmètre crânien) — communiqué du 16.06.2026, lu ». |
| Mineur | examen_complet[Manœuvres].gestes[0] | ajouter la source : « (source européenne : ESH 2016, Lurbe E et al., J Hypertens 2016, non lu, À vérifier) ». |
| Mineur | gestes[4].anomalies[0].signe | « Ecchymoses d'âges différents » → « Ecchymoses multiples (la datation par la couleur n'est pas fiable, voir S-35) ». |
| Mineur | syndromes_lies | retirer SY-81 (jamais cité). |

### S-34 Autonomie du sujet âgé
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Majeur** | examen_complet[Manœuvres].gestes[0] ; manoeuvres_speciales[0].positif_si, valeur | Le seuil de 12 s ne repose que sur une source américaine (STEADI). → « Seuil variable : la stratification mondiale retient un TUG > 15 s ou une vitesse de marche < 0,8 m/s (source internationale : World Falls Guidelines, Montero-Odasso, Age Ageing 2022, non lu, À vérifier) ; STEADI retient ≥ 12 s (source américaine). Outils recommandés en Suisse : TUG, lever de chaise, SPPB (HUG/SMPR, Personnes âgées 2026 — lu) ». |
| Mineur | gestes[2].normal (lever de chaise) | « < 15 s environ (seuil à vérifier) » → « ≤ 15 s pour 5 levers (source européenne : EWGSOP2, Cruz-Jentoft 2019) ». |

### S-35 Examens médico-légaux
| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| **Majeur** | epa, sources[0] | Les intitulés sont inversés. PROFILES 2017 (lu) : 2kk = personne sous l'influence, 2ll = violences physiques et sexuelles, 2mm = « clinical diagnosis of death, **estimation of time of death** ». Corriger, et ajouter à MS[2].interpretation : « PROFILES 2mm attend une estimation grossière du délai (lividités, rigidité, température), que le légiste affine ». |
| Mineur | manoeuvres_speciales[0].valeur ; sources[6] | « source australienne » → « source britannique (Cambridge, 1991) ». |
| Mineur | gestes[3].anomalies[0].signifie ; MS[3].valeur | « (art. 253 CPP) » → « annonce selon le droit cantonal (art. 253 al. 4 CPP, lu : les cantons désignent les soignants tenus d'annoncer) ». |
| Mineur | gestes[0].anomalies[3].signe | règle TEN-4 non sourcée → « (source américaine : Pierce MC et al., Pediatrics 2010, non lu, À vérifier) ». |
| Mineur | manoeuvres_speciales[1].image | photo de cadavre en salle d'autopsie (tête couverte, origine ru.wikipedia 2008) → fenêtre occultante avec la mention « image de défunt ». |
| Mineur | syndromes_lies | retirer SY-71 ou le citer. |

### Transversal
| Grav. | Défaut | Patch |
|---|---|---|
| Mineur | S-28 refuse les dessins de Commons (« Brud I/II »), alors que S-25, S-26 et S-27 emploient des gravures historiques (Greene, Gowers, Dana, Church). | Fixer une règle : gravure historique acceptée si elle est légendée « gravure, année » ; sinon tout retirer. Décision à Vial. |
| Mineur | 10 licences Commons non relues (HTTP 429) : papillœdème, monofilament, ecchymose, LungandEffusion, Morison, Greene, Gowers, Dana, Church, Hamilton. | Les relire avant publication. |

## 3. Question finale
**Publiable en l'état ? Non.** Il faut d'abord :
1. retirer l'horloge sous droit d'auteur Elsevier ;
2. corriger l'interprétation de Kernig et Brudzinski (LR+ ≈ 1) et la définition du Kernig ;
3. corriger l'Apgar (8) et le protocole suisse d'oxymétrie ;
4. passer aux courbes suisses de 2026 ;
5. reprendre les critères ASSM 2019 ;
6. ajouter le HINTS+ ;
7. remplacer le seuil TUG de source américaine exclusive ;
8. corriger les codes EPA de S-35 ;
9. traiter les images de l'enfant de 1909 et du nouveau-né identifiable.

Après ces patchs, audit-ok possible, sous réserve des 10 licences non relues.
