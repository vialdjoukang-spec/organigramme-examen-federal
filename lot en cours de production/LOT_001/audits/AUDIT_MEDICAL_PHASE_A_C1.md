# Audit médical C1 — LOT_001 Phase A V0 (G1 Transpiration anormale)

| Élément | Valeur |
|---|---|
| Fichier | `LOT_001_Phase_A_V0.html`, 171 635 octets, SHA-256 `b3ec1b93…57f597a2` |
| Date, rôle | 26.10.2026 ; auditeur médical (non rédacteur) ; points 2, 3, 4, 8, 9, 11, 12 + Bloc 2 (liste DX, tableau, algorithme) |
| Contrôle mécanique | `controle_lot.py verifier LOT_001` : fichier sans critique ; `a_verifier_aips = 1` ; critiques de lot = Phase B absente (attendu) |
| AIPS lues (`aips_texte.py`, 26.10.2026) | 69243, 52433, 55057, 70200, 31489, 32920, 69232, 53290, 55234, 57611, 60092 : 11 numéros présents dans l'index du corpus, aucun déduit |
| Autres sources ouvertes | HUG_000000812 (PDF), Inselspital Cobas PRO v21.0 (PDF), guide TB 2024 (PDF) ; WebSearch : OFSP TB 2025, Obsan diabète, VIH 2023, définition universelle 2026. Suva et Obsan : DNS refusé, donc non relus |
| Calculs refaits (Python) | 9,07 % ; 0,23 % ; normétanéphrine 0,80/1,60 ; 2,22× ; 20 g, 8, 10, 20 g ; 40 % ; 32 g ; 6,0 et 4,2/100 000 : **tous exacts** |

## Score §12.2 (2/1/0 ; aucune question sans objet)

| Point | Questions → note | Raison des notes < 2 | Total |
|---|---|---|---|
| 2 | Q2.1=2 ; Q2.2=2 ; Q2.3=1 ; Q2.4=1 | Coût non chiffré. Sources S105–S112 « texte intégral non ouvert » ; S112 = relais de presse ; VIH 2022 (2023 disponible) | 6/8 |
| 3 | Q3.1–Q3.5 = 2 | — | 10/10 |
| 4 | Q4.1=2 ; Q4.2=2 | — | 4/4 |
| 8 | Q8.1=1 ; Q8.2=2 | Critères tirés d'un formulaire local NHS (CG055), pas d'une société savante | 3/4 |
| 9 | Q9.1=2 ; Q9.2=2 ; Q9.3=2 ; Q9.4=1 ; Q9.5=2 ; Q9.6=2 | 99e percentile unique (14 ng/L) en 9.b, alors que le point 8 exige un seuil propre au sexe | 11/12 |
| 11 | Q11.1=2 ; Q11.2=2 ; **Q11.3=1** ; **Q11.5=1** ; Q11.4, Q11.6, Q11.7=2 ; **Q11.8=0** ; Q11.9–Q11.11=2 | Bolus IV de glucose absent malgré la source S14. CI BOTOX adoucie ; VEOZA sans dose ni CI. Axhidrox/grossesse contraire à l'AIPS ; grossesse et allaitement de l'oxybutynine absents | 18/22 |
| 12 | Q12.1=2 | — | 2/2 |
| **Total** | | | **54/62 = 87,1 %** |
| Grille /28 (7 points × 2) | Points 2=1 ; 3=2 ; 4=2 ; 8=1 ; 9=1 ; 11=0 (critique) ; 12=2 | Ma part : 9/14 = 64,3 % ; à fusionner avec l'audit linguistique pour obtenir le /28 | 9/14 |

## Corrections

| Classe | Emplacement | Extrait (≤ 200 car.) | Correction | Source |
|---|---|---|---|---|
| **Critique** | 11.B, Situations spéciales, ligne Grossesse | « Axhidrox® : le libellé AIPS exact de la rubrique Grossesse n'a pas été relu mot pour mot ; … À vérifier (AIPS). Aucun emploi d'Axhidrox® n'est proposé pendant la grossesse » | Supprimer « À vérifier » et l'interdiction. Écrire : « Données absentes ou limitées ; toxicité animale jugée non pertinente vu la faible exposition cutanée ; si nécessaire, l'application d'Axhidrox peut être envisagée pendant la grossesse. » La formulation V9 était fidèle ; l'audit V0 s'est trompé | AIPS 69243, Grossesse |
| **Critique** | 11.B, fenêtre « Toxines botuliques » | « Une infection au site fait revoir l'injection » | La présence d'une infection au(x) site(s) d'injection prévu(s) est une **contre-indication** de BOTOX. Écrire « contre-indique l'injection de BOTOX » | AIPS 52433, Contre-indications |
| Grave | 11.B, Urgence hypoglycémie, ligne « Pas de réponse à 10 min » | « L'IP demande du glucose IV sans chiffrer le bolus … ce manque reste bloquant (HELP Q3) » | Citer HUG (S14, déjà cité) : conscience altérée → 32 g de glucose (8 ampoules de G40 % à 4 g/10 mL) en IV lente sur 3–5 min ; glycémie à 10 min ; G10 % à 100 mL/h sur prescription. Fermer HELP Q3 | HUG_000000812 §3 ; AIPS 55234 (50 mL de G20–30 %) |
| Grave | Situations spéciales, lignes Grossesse et Allaitement | Oxybutynine absente des deux lignes | Ajouter : « ne doit pas être utilisé pendant la grossesse, sauf nécessité absolue » ; « ne doit pas être administré pendant l'allaitement » | AIPS 70200 |
| Grave | Bloc 2, critère d'ordre | « place d'abord les DD graves … puis classe les autres DD par fréquence décroissante » | La phrase contredit la liste : E4–E7 viennent après DX.4–6. Le §9.1 exige un ordre de fréquence où le grave rare garde son rang. Choisir un critère, l'écrire, puis aligner la liste canonique avant son gel | Prompt V0 §9.1 ; LISTE_DX_CANONIQUE |
| Grave | Point 2 et Bloc 2, badges S105–S112 | « Extrait de recherche … texte intégral non ouvert » ; S112 « relais La Télé » | Ouvrir et lire les sources primaires (OFS, OFSP, Obsan, ESC, NICER/ONRC) ; remplacer le relais de presse par l'OFS | Prompt V0 §13 |
| Grave | 11.B, ligne BOTOX/Dysport Grossesse | « emploi seulement en cas de nécessité absolue selon leurs IP » | BOTOX : ajouter « ni chez la femme en âge de procréer sans contraception, sauf nécessité absolue » ; sinon le texte est plus permissif que l'AIPS | AIPS 52433, Grossesse |
| Moyen | Point 3 (tableau) et 11.B | VEOZA® cité comme traitement, sans dose, sans CI | Ajouter 45 mg 1×/j ; CI : Child-Pugh B/C, DFGe < 30, inhibiteurs du CYP1A2 ; transaminases avant le début puis chaque mois pendant 3 mois | AIPS 69232 |
| Moyen | Fenêtre Axhidrox | Précautions absentes | Ajouter la prudence en cas de maladie coronarienne, d'insuffisance cardiaque, de trouble du rythme ou d'hypertension (DX.1) ; hyperplasie prostatique ; peau lésée | AIPS 69243, Mises en garde |
| Moyen | Fenêtre Oxybutynine | Mises en garde | Ajouter l'aggravation possible de l'hyperthyroïdie et de la tachycardie (DX.6), et l'épuisement par la chaleur | AIPS 70200 |
| Moyen | Fenêtre Glucagon | « Il peut échouer après jeûne prolongé, alcool ou certaines maladies hépatiques » | Écrire selon l'AIPS : jeûne prolongé, insuffisance surrénale, hypoglycémie chronique, hypoglycémie induite par l'alcool. Ajouter : sujet âgé, prudence et dose la plus faible | AIPS 31489 |
| Moyen | Point 2, VIH ; Bloc 2 DX.8 ; DX.9 | « 371 déclarations en 2022 … Chiffre national le plus récent » ; Hodgkin 2003–2006 | 2023 : 352 cas, 4,0/100 000 (à lire sur la source OFSP). Hodgkin : chercher le rapport suisse sur le cancer 2021 (ONRC/OFS) | OFSP ; OFS |
| Moyen | 9.b Troponine | « 99e percentile adulte indicatif 14 ng/L » | Signaler l'écart avec le seuil propre au sexe exigé par la définition universelle 2026 (point 8) | S22 ; S71 |
| Léger | 11.B, Axhidrox | « fréquence réduite jusqu'à 2 fois par semaine » | « peut être réduite à 2 fois par semaine » ; ajouter « de préférence le soir » | AIPS 69243 |
| Léger | 11.A | « une baisse d'au moins 2 points sert de critère de réponse » | Préciser que c'est un critère secondaire (p = 0,0542, non significatif) | AIPS 69243, Efficacité |
| Léger | Situations spéciales, Grossesse | « Glucagon : l'utilisation n'est pas interdite » | Reprendre le texte mot pour mot : « GlucaGen peut être utilisé pendant la grossesse » ; Glucosum : « être prudent » | AIPS 31489, 32920 |
| Léger | Point 2 et DX.2 | « 6,2 % de la population » | Écrire « des 15 ans et plus (autodéclaration) » | Obsan MonAM |

## Critique de `CORRECTIONS_AUDIT.md`

| N° | Constat | Action |
|---|---|---|
| 3 | Le n° 3 repose sur une prémisse fausse. L'AIPS 69243 contient bien « peut être envisagée » : le rédacteur a supprimé un texte exact | Réécrire : « reprendre la rubrique Grossesse mot pour mot (texte lu le 26.10.2026) » |
| 1 vs 2 | Le n° 2 (« graves, puis bénins ») contredit la liste canonique du n° 1 (DX.4–6 avant E4–E7) | Trancher selon le §9.1, puis mettre à jour les deux documents |
| 6 | Le score V7 est périmé | Remplacer par ce score C1 |

## Question finale

**Non.** Le patient n'est pas traité en sécurité, et le seuil de 90 % n'est pas atteint. Il manque :

- les deux corrections critiques : texte AIPS d'Axhidrox pendant la grossesse, contre-indication de BOTOX en cas d'infection ;
- le bolus de glucose IV, déjà sourcé ;
- la grossesse et l'allaitement sous oxybutynine ;
- un critère d'ordre des DD cohérent ;
- la lecture des sources S105–S112.

Rien n'est à reporter dans HELP : HELP Q1 et HELP Q3 sont résolus par l'AIPS 69243 et par HUG S14.
