# Mémoire LOT_024 (résumeur, 11 fichiers)

## Liste gelée
DX.1 — Otite externe aiguë bactérienne
DX.2 — Otite moyenne aiguë perforée
DX.3 — Otite moyenne chronique suppurée sans cholestéatome
DX.4 — Otomycose
DX.5 — Dermatite eczémateuse du conduit auditif
DX.6 — Corps étranger du conduit auditif
DX.7 — Perforation tympanique traumatique
DX.8 — Cholestéatome de l’oreille moyenne 🚩 E3
DX.9 — Otite externe nécrosante 🚩 E2
DX.10 — Fuite otologique de liquide cérébrospinal 🚩 E1

## Fichiers
| Fichier | Titre | Octets | controle3 | Fenêtres | Fiches .mb (AIPS) | Sources | sha8 |
|---|---|---|---|---|---|---|---|
| Phase_A_V0.html | S1.8 — Écoulement auriculaire | discharge fr | 90191 | VERT | 40 | 0 (31957,44911,54807) | 20 | d1a5e7db |
| Phase_B_V0_DX.1.html | Otite externe aiguë bactérienne | 89073 | VERT | 41 | 4 (31957,45031,47503,54807) | 12 | 21a444b3 |
| Phase_B_V0_DX.2.html | Otite moyenne aiguë perforée | 91179 | VERT | 40 | 7 (31957,43838,44911,48306,49460,53982,53995,54807,56046,57192) | 22 | 3b9818c5 |
| Phase_B_V0_DX.3.html | Otite moyenne chronique suppurée sans choles | 84282 | VERT | 43 | 4 (31957,47795,51898,54807) | 19 | 463c4579 |
| Phase_B_V0_DX.4.html | Otomycose | 85086 | VERT | 42 | 4 (31957,37510,46100,54807) | 16 | b58f7abc |
| Phase_B_V0_DX.5.html | Dermatite eczémateuse du conduit auditif | 83942 | VERT | 43 | 4 (31957,36481,54807,55965) | 13 | e333f87a |
| Phase_B_V0_DX.6.html | Corps étranger du conduit auditif | 83494 | VERT | 38 | 6 (10714,43838,47503,54807,55766,56046) | 19 | e3be0be8 |
| Phase_B_V0_DX.7.html | Perforation tympanique traumatique | 87411 | VERT | 37 | 7 (10714,31957,43838,47503,54807,55766,56046) | 22 | 381f5ea7 |
| Phase_B_V0_DX.8.html | Cholestéatome de l’oreille moyenne 🚩 E3 | 83517 | VERT | 37 | 1 (44625) | 16 | 8b5b51be |
| Phase_B_V0_DX.9.html | Otite externe nécrosante 🚩 E2 | 88666 | VERT | 39 | 3 (46050,47795,57929,63001) | 23 | 995443a6 |
| Phase_B_V0_DX.10.html | Fuite otologique de liquide cérébrospinal 🚩  | 84714 | VERT | 38 | 3 (44625,69222,69781) | 16 | ea0ad731 |

## Audits
- LISTE_DX.audit.json : verdict CORRIGER, {}
- audit1_A.audit.json : verdict corrections, {'Critique': 1, 'Grave': 3, 'Moyen': 8, 'Léger': 14}
  - Critique · LOT_024_Phase_B_V0_DX.2.html · Fiche Co-Amoxi-Mepha : texte d'allaitement adouci. L'AIPS 53995 conclut « Il ne faudrait donc pas allaiter pendant le traitement par Co-Amox
  - Grave · LOT_024_Phase_B_V0_DX.4.html · Arbre décisionnel : la crème sur tympan perforé est enseignée sans dire qu'elle sort de l'AIPS (Canesten : « le tympan étant intact »). Le p
  - Grave · LOT_024_Phase_B_V0_DX.4.html · Même défaut dans le tableau des situations spéciales : la crème sur perforation y figure comme conduite, sans mention hors AIPS ni divergenc
  - Grave · LOT_024_Phase_B_V0_DX.5.html · Panotile (néomycine) enseigné dans l'eczéma aigu du conduit. Contredit DX.1 (« mauvais choix en cas d'eczéma du conduit »), la Phase A (poin
- audit1_B.audit.json : verdict corrections, {'Critique': 3, 'Grave': 4, 'Moyen': 7, 'Léger': 8}
  - Critique · LOT_024_Phase_B_V0_DX.7.html · Texte adouci : la phrase laisse croire que l'ibuprofène convient avant le troisième trimestre et pendant l'allaitement ; l'AIPS 55766 le lim
  - Critique · LOT_024_Phase_B_V0_DX.7.html · Fiche Algifor-L : la rubrique grossesse omet la restriction des 1er–2e trimestres et toute la rubrique allaitement.
  - Critique · LOT_024_Phase_B_V0_DX.6.html · Même omission dans la fiche Algifor-L du DX.6 ; la phrase suivante prescrit 1200 mg/j à l'adulte appareillé sans réserve de grossesse ni d'a
  - Grave · LOT_024_Phase_B_V0_DX.6.html · Fiche Algifor Junior : la rubrique « Grossesse et allaitement » ne porte que la CI du 3e trimestre ; l'AIPS 56046 exige aussi la nécessité a
  - Grave · LOT_024_Phase_B_V0_DX.10.html · Fiche Rocephin : rubrique intitulée « Grossesse et allaitement » sans la ligne allaitement de l'AIPS (interrompre l'allaitement si le traite
  - Grave · LOT_024_Phase_B_V0_DX.9.html · Les 4 dates de mise à jour AIPS sont fausses (relu refdata en direct le 12.11.2026) : la version citée n'a pas été lue.
  - Grave · LOT_024_Phase_B_V0_DX.10.html · Les 3 dates de mise à jour AIPS sont fausses (Rocephin daté juin 2025 dans le DX.8, juillet 2025 ici).
- phase_A.contre_audit.json : verdict ACCEPTE, {}, seconde passe ACCEPTE

## Lacunes (HELP.md, 8 dernières)
- DX.5 : Panotile (AIPS : dermatites eczémateuses) enseigné seulement sans antécédent de gouttes ; néomycine évitée si allergie suspectée (Sood 2002).
- DX.4 : kétoconazole en mèche (support HUG) écrit hors AIPS.

- DX.3 et DX.8 : aucune donnée épidémiologique suisse de population lue ; seules des séries hospitalières suisses (Zurich, Genève, Lucerne, Berne) et des données européennes.
- DX.3 : Ciloxan dans l'oreille (hors AIPS) sans posologie auriculaire suisse lue ; le cours ne donne aucun milligramme ni nombre de gouttes.
- DX.3 et DX.8 : audits A et B faits par le rédacteur (aucun sous-agent auditeur disponible) ; audit indépendant à faire.

- DX.3 : l'AIPS Ciproxine (47795) cite l'otite moyenne purulente chronique (2 × 500–750 mg, 7–14 j), mais Cochrane 2025 ne montre guère de bénéfice à l'ajouter aux gouttes ; le cours la réserve aux signes généraux (Bozorg Grayeli 2020) et écrit la divergence.

## Sources déjà lues dans ce LOT (121) — réutiliser avant toute recherche
- CIMS/SMIFK. PROFILES 2023 — Situations as Starting Points, SSP S1.8 «  — https://www.smifk-cims.ch/profiles-2023/ssps
- Hôpitaux universitaires de Genève (HUG), service d’ORL et de chirurgie — https://www.hug.ch/orl-chirurgie-cervico-faciale/otite-externe
- Société suisse d’infectiologie (SSI). Otite moyenne aiguë, version val — https://ssi.guidelines.ch/guideline/2406/fr
- Hôpitaux universitaires de Genève (HUG), service d’ORL. Otite moyenne  — https://www.hug.ch/orl-chirurgie-cervico-faciale/otite-moyenne-chronique-avec-sans-cholesteatome
- Hôpitaux universitaires de Genève (HUG), service d’ORL. Fracture de la — https://www.hug.ch/orl-chirurgie-cervico-faciale/fracture-base-crane
- Hôpitaux universitaires de Genève (HUG), service d’ORL. Perforation ty — https://www.hug.ch/orl-chirurgie-cervico-faciale/perforation-tympanique-traumatique
- Wiegand S, Berner R, Schneider A, Lundershausen E, Dietz A. Otitis ext — https://pmc.ncbi.nlm.nih.gov/articles/PMC6522672/
- ENT UK, Global ENT guidelines. Foreign bodies in the external auditory — https://www.entuk.org/_userfiles/pages/files/guidelines/global%20ent%20guidelines/foreign_bodies_external_auditory_canal.pdf
- Neher A, Nagl M, Scholtz AW (Innsbruck). Otitis externa: Ätiologie, Di — https://doi.org/10.1007/s00106-008-1830-y
- Linton S, Stapleton E. Necrotising otitis externa: a national increase — https://doi.org/10.1017/S0022215121004515
- Kong D, Linton S, Stapleton E. Necrotising otitis externa in England,  — https://doi.org/10.1017/S0022215125102910
- Stocker M, Hempel JM (LMU Munich). Malignant otitis externa: a single- — https://doi.org/10.1038/s41598-025-11742-z
- Kemps GJF, et al. (Pays-Bas). Beta-trace protein and beta-2 transferri — https://doi.org/10.1016/j.heliyon.2024.e28059
- Bajor B, et al. (Budapest). Otogén liquorcsorgás. Orv Hetil 2026;167(9 — https://doi.org/10.1556/650.2026.33498
- Alho OP, Jokinen K, Laitakari K, Palokangas J (Oulu). Chronic suppurat — https://doi.org/10.1046/j.1365-2273.1997.00027.x
- Li J, et al. (Australie). Incidence of cholesteatoma surgery. Laryngos — https://doi.org/10.1002/lio2.709
- Blausen Medical. Blausen 0328 Ear Anatomy, CC BY 3.0, Wikimedia Common — https://commons.wikimedia.org/wiki/File:Blausen_0328_EarAnatomy.png
- Swissmedic, information professionnelle : Panotile, gouttes auriculair — https://files.refdata.ch/simis-public-prod/MedicinalDocuments/2982497d75d8429f94238a7ee10de662-fr.html
- Swissmedic, information professionnelle : Ciproxin HC, suspension auri — https://files.refdata.ch/simis-public-prod/MedicinalDocuments/60c59a399aab401fadc6cd1179773b3f-fr.html
- Swissmedic, information professionnelle : Amoxi-Mepha, Mepha Pharma AG — https://files.refdata.ch/simis-public-prod/MedicinalDocuments/174c174fbc1a4bcb8daa6f13b5231a20-fr.html
- Hôpitaux universitaires de Genève (HUG), Département de médecine de pr — https://www.hug.ch/sites/interhug/files/2022-09/otite_exerne_aigue_14.07.2022.pdf
- Wiegand S, Berner R, Schneider A, Lundershausen E, Dietz A. Otitis ext — https://di.aerzteblatt.de/int/archive/article/206313
- Kaushik V, Malik T, Saeed SR. Interventions for acute otitis externa.  — https://doi.org/10.1002/14651858.CD004740.pub2
- van Balen FAM, Smit WM, Zuithoff NPA, Verheij TJM. Clinical efficacy o — https://doi.org/10.1136/bmj.327.7425.1201
- Swissmedic, AIPS Brufen® (ibuprofène), n° 45031, mise à jour décembre  — https://files.refdata.ch/simis-public-prod/MedicinalDocuments/b63870557e734d65a125b488d681c6a6-fr.html
- Swissmedic, AIPS DAFALGAN® (paracétamol), n° 47503, mise à jour juille — https://files.refdata.ch/simis-public-prod/MedicinalDocuments/783cc01c6fa7448399362d9df7d4be78-fr.html
- Peter KD (Wiehl, Allemagne). Otitis externa, photographie clinique, li — https://commons.wikimedia.org/wiki/File:Otitis_externa.jpg
- Heilman J. OtitisExterna10, photographie clinique d'une forme sévère,  — https://commons.wikimedia.org/wiki/File:OtitisExterna10.JPG
- HUG, Service de médecine de premier recours, Delhaye E, expert Schible — https://www.hug.ch/sites/interhug/files/2022-09/strategie-ivrs-2021_jezc-finalisee.pdf
- HUG, Service d'ORL et chirurgie cervico-faciale. Otite moyenne aiguë e — https://www.hug.ch/orl-chirurgie-cervico-faciale/otite-moyenne-aigue
- National Institute for Health and Care Excellence (NICE). Otitis media — https://www.nice.org.uk/guidance/ng91/chapter/Recommendations
- Rovers MM, Glasziou P, Appelman CL et al. Antibiotics for acute otitis — https://doi.org/10.1016/S0140-6736(06)69606-2
- Venekamp RP, Sanders SL, Glasziou PP, Rovers MM. Antibiotics for acute — https://doi.org/10.1002/14651858.CD000219.pub5
- Swissmedic, AIPS Co-Amoxi-Mepha® comprimés pelliculés (amoxicilline, a — https://files.refdata.ch/simis-public-prod/MedicinalDocuments/5fb4441216ee4ce993f9718820ba967c-fr.html
- Swissmedic, AIPS Co-Amoxi-Mepha® poudre pour suspension buvable (amoxi — https://files.refdata.ch/simis-public-prod/MedicinalDocuments/4dbfc7a2fc9444f9b676ec7602450513-fr.html
- Swissmedic, AIPS Zinat® (céfuroxime axétil), n° 49460, mise à jour avr — https://files.refdata.ch/simis-public-prod/MedicinalDocuments/951eb1bd630346c19086820afb483cc9-fr.html
- Swissmedic, AIPS Clarithromycin-Mepha® granulés pour suspension buvabl — https://files.refdata.ch/simis-public-prod/MedicinalDocuments/37a4d04b3caf4963b514cdf16c5e45e1-fr.html
- Swissmedic, AIPS Bactrim® forte, comprimés (triméthoprime, sulfaméthox — https://files.refdata.ch/simis-public-prod/MedicinalDocuments/48ee4e6cb19942b987ce445ab3c93d2a-fr.html
- Swissmedic, AIPS Algifor® Junior, suspension (ibuprofène), n° 56046, m — https://files.refdata.ch/simis-public-prod/MedicinalDocuments/7c1d565ae1414bc5801452751fffcc29-fr.html
- Swissmedic, AIPS DAFALGAN® enfant, sirop (paracétamol), n° 43838, mise — https://files.refdata.ch/simis-public-prod/MedicinalDocuments/7a077e38e06e42c69de49bde0648bb26-fr.html
- NHS (National Health Service, Royaume-Uni). Mastoiditis, page d'inform — https://www.nhs.uk/conditions/mastoiditis/
- Blausen.com staff (BruceBlaus). Blausen 0330 EarAnatomy MiddleEar, sch — https://commons.wikimedia.org/wiki/File:Blausen_0330_EarAnatomy_MiddleEar.png
- Welleschik B. Otitis media entdifferenziert2, photographie otoscopique — https://commons.wikimedia.org/wiki/File:Otitis_media_entdifferenziert2.jpg
- Hawke M. Subtotal perforation of the right tympanic membrane, photogra — https://commons.wikimedia.org/wiki/File:Subtotal_Perforation_of_the_right_tympanic_membrane.tif
- HUG, da Graça S. L’oreille aux urgences ambulatoires (UUA), support de — https://www.hug.ch/sites/interhug/files/atelier_mpr/24.07.19_presentation_sur_otites_5.pdf
- (+ 76 autres : grep -h '<li id="sb-' dans les cours)
