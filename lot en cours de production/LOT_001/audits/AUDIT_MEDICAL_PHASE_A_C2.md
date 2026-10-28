# Audit médical C2 — LOT_001 Phase A V0 (G1 Transpiration anormale)

| Élément | Valeur |
|---|---|
| Fichier | `LOT_001_Phase_A_V0.html`, 186 209 octets, SHA-256 `3180b291…0b2274c5c054` |
| Date, rôle | 26.10.2026 ; auditeur médical C2 (non rédacteur) ; points 2, 3, 4, 8, 9, 11, 12 + Bloc 2 (liste DX, tableau comparatif, algorithme) |
| Lecture | `controle_lot.py extraire --points 2,3,4,8,9,11,12` + Bloc 2 extrait du HTML (la commande ne sort pas le Bloc 2) |
| AIPS relues (`aips_texte.py`) | 69243, 52433, 55057, 70200, 31489, 69232, 32920, 55234, 53290, 57611, 60092 : 11 numéros identiques au corpus (`evidence/aips_corpus_LOT_001.tsv`) |
| Calculs refaits | 9,07 % ; 0,23 % ; 19 851 ; 9,5/91,5 = 10,4 % ; normétanéphrine 0,80 et 1,60 ; 1,00/0,45 = 2,22 ; 8 × 10 mL × 0,4 g/mL = 32 g ; 20 g ; 8, 10, 20 g : **exacts**. Un exemple faux (point 8, voir corrections) |
| Non relu | Sources non AIPS (OFS, OFSP, Obsan, HUG, LUKS, ESC) : confiance aux lectures C1 ; non rouvertes en C2 |
| Corrections C1 | Toutes reprises dans le texte (Axhidrox grossesse mot pour mot, CI BOTOX, bolus 32 g, oxybutynine grossesse/allaitement, VEOZA, critère d'ordre, S105–S112, troponine par sexe) |

## Dose par dose contre l'AIPS

| Médicament | Texte Phase A | AIPS lu | Verdict |
|---|---|---|---|
| Axhidrox 69243 | 2 pressions/aisselle, 4,4 mg, 1×/j le soir, 4 sem., puis 2×/sem. dès la 5e ; grossesse ; CI ; prudence coronaire, prostate, peau lésée ; rénal | identique ; « Si nécessaire, l'application d'Axhidrox peut être envisagée pendant la grossesse » | Conforme (« 4,4 mg » = par aisselle : à préciser) |
| BOTOX 52433 | 50 U/aisselle, 100 U/4,0 mL, 1–2 cm, ≥ 16 sem., 4–7 mois ; CI infection au site ; grossesse | identique ; CI « infection au(x) site(s) d'injection prévu(s) » ; « sauf nécessité absolue » | Conforme ; « 200 U réservé à l'export » introuvable dans l'IP |
| Dysport 55057 | 100 U/aisselle, 10 × 10 U, ≥ 12 sem., prurit et hypersudation compensatoire fréquents ; grossesse « ne devrait pas » | identique | Conforme ; CI (hypersensibilité) non écrite |
| Oxybutynin Macure 70200 | indications vésicales, aucune dose sudorale ; grossesse, allaitement, hyperthyroïdie, chaleur | identique | Conforme |
| GlucaGen 31489 | 1 mg SC/IM ; enfant 1 mg > 25 kg ou > 6–8 ans, sinon 0,5 mg ; glucose IV sans réponse à 10 min ; CI phéochromocytome ; jeûne, surrénale, alcool ; âgé ; grossesse et allaitement ; indométacine, warfarine | identique | Conforme |
| VEOZA 69232 | 45 mg 1×/j ; bilan avant puis mensuel × 3 ; pas de départ > 2× ; arrêt > 5× ou 3× + bilirubine 2× ; CI Child B/C, DFGe < 30, CYP1A2 ; fluvoxamine × 9,4 ; 12 mois | identique | Conforme |
| Glucosum 32920 | 0,5 g/kg/h ; 20–50 % par voie centrale ; CI ; « être prudent » | identique | Conforme |
| Diamicron MR 55234 | 50 mL G20–30 % IV rapide, puis G10 % ; ≥ 48 h | identique | Conforme |
| Humalog 53290 | 20 g IV (40 mL à 50 %) | identique | Conforme |
| Glimeryl 57611 | symptômes jusqu'à 24 h ; 12–72 h | identique ; l'IP demande aussi une glycémie surveillée ≥ 24 h | Conforme |
| Flucloxacilline 60092 | aminoside dans l'endocardite staphylococcique | « 12 g par jour plus un aminoglycoside » | Conforme |
| HUG 32 g (8 amp. G40 %) | 8 × 4 g = 32 g | non AIPS ; calcul exact | Conforme (source C1) |

**Aucune dose fausse, aucun texte AIPS adouci, aucun « À vérifier (AIPS) » résiduel.**

## Score §12.2 (2/1/0, note à neuf)

| Point | Questions → note | Raison des notes < 2 | Total |
|---|---|---|---|
| 2 | Q2.1=1 ; Q2.2=2 ; Q2.3=2 ; Q2.4=2 | Distribution suisse absente pour DX.3, DX.5, DX.6 (données européennes ou mondiales sans mention « donnée suisse non trouvée ») | 7/8 |
| 3 | Q3.1=2 ; Q3.2=2 ; **Q3.3=1** ; Q3.4=2 ; Q3.5=2 | Lignes VIH, TB, Hodgkin, PPGL du tableau : traitement nommé sans classe ni mécanisme | 9/10 |
| 4 | Q4.1=2 ; Q4.2=2 | — | 4/4 |
| 8 | Q8.1=1 ; Q8.2=2 | Critères de l'hyperhidrose tirés d'une revue, société et année d'origine non nommées ; exemple faux | 3/4 |
| 9 | Q9.1=2 ; Q9.2=2 ; Q9.3=2 ; Q9.4=1 ; Q9.5=2 ; Q9.6=2 | Seuil de troponine propre au sexe encore absent (HELP Q5) | 11/12 |
| 11 | Q11.1=2 ; Q11.2=2 ; **Q11.3=1** ; Q11.4=2 ; **Q11.5=1** ; Q11.6–Q11.11=2 | Q11.3 : urgence coronarienne et crise du PPGL sans médicament ni dose. Q11.5 : CI de Dysport et hypersensibilité de BOTOX absentes | 20/22 |
| 12 | Q12.1=1 | Aucune prévention cardiovasculaire (DX.1, 26,7–28,9 % des décès) ni plan de vaccination suisse cité | 1/2 |
| **Total** | | | **55/62 = 88,7 %** |
| Grille (7 points × 2) | 2=1 ; 3=1 ; 4=2 ; 8=1 ; 9=1 ; 11=1 ; 12=1 | Barème : 2 si toutes les questions à 2 ; 1 si une note à 1 ; 0 si une note à 0 ou une critique | **8/14 = 57,1 %** (les 14 autres points du /28 relèvent d'autres auditeurs) |

## Corrections

| Classe | Emplacement | Extrait (≤ 200 car.) | Correction | Source |
|---|---|---|---|---|
| Critique | — | aucune | — | — |
| Grave | — | aucune | — | — |
| Moyen | Point 8, critères cliniques suisses, « Exemple » | « deux aisselles atteintes chaque semaine depuis 7 mois, un début à 16 ans, aucune sueur nocturne et une gêne au travail réunissent 5 critères » | L'exemple réunit 6 critères (axillaire, bilatéral, hebdomadaire, pas de sueur nocturne, début < 25 ans, gêne). Écrire 6, ou retirer un élément | Revue médicale suisse 2017 (S114) |
| Moyen | Bloc 2, DX.4 et ligne DX.4 du tableau de fréquence | « une proportion qu'aucun autre DD n'atteint dans la population générale » ; « cause la plus fréquente en population » | Faux avec les chiffres du fichier : 31–52 % de 40–65 ans (≈ 16 % de la population féminine) donne environ 5–8 % de la population. Écrire que le dénominateur diffère et que le rang DX.4 < DX.5 reste à décider (HELP Q6) | S45, S111 |
| Moyen | Point 11, « Urgence — présentation coronarienne » et ligne E7 du point 4 | « stratégie pharmacologique et transfert » ; « Le médecin sécurise le patient » | Nommer les médicaments et doses AIPS (antiagrégant, anticoagulant ; blocage alpha du PPGL) ou écrire « dose AIPS en Phase B DX.1 / DX.10 » et l'inscrire dans CORRECTIONS_AUDIT | AIPS à lire |
| Moyen | Bloc 2, tableau, ligne DX.2 | « il injecte GlucaGen® 1 mg SC ou IM ou 32 g de glucose IV si la conscience est altérée » | Ajouter « diabétique sous insuline » et les limites du glucagon (jeûne, surrénale, alcool) ; glucose IV si voie veineuse | AIPS 31489 |
| Moyen | Bloc 2, algorithme | étapes 1–11 | Aucune branche pour des sueurs généralisées ou nocturnes sans orientation, ni pour une cause médicamenteuse. Ajouter l'étape 12 : revue des médicaments, hémogramme, CRP, TSH, suivi (voir 9.d) | Point 4, 9.d |
| Moyen | Point 8, critères des DD graves | « L'hypoglycémie se traite sous 4,0 mmol/L chez l'adulte diabétique » | C'est un seuil d'action, pas un critère diagnostique. Ajouter la triade de Whipple et le seuil hors diabète | HUG ; à lire |
| Moyen | Point 3, tableau, lignes VIH, TB, Hodgkin, PPGL | « Traitement antirétroviral spécialisé » ; « Traitement antituberculeux combiné » | Ajouter classe et mécanisme (inhibition de la réplication ; association de bactéricides ; chimiothérapie ; blocage alpha) | Q3.3 |
| Moyen | Point 12 | tableau des 3 niveaux | Ajouter la prévention cardiovasculaire (tabac, lipides, tension) et le plan de vaccination suisse | OFSP ; Infovac |
| Léger | 11.B, Axhidrox | « 2 pressions par aisselle (2,2 mg/pression, soit 4,4 mg) » | « soit 4,4 mg par aisselle » | AIPS 69243 |
| Léger | 11.B, BOTOX | « le dosage de 200 unités est réservé à l'export dans le registre consulté » | Introuvable dans l'IP : supprimer ou citer le registre | AIPS 52433 |
| Léger | Fenêtre toxines | CI de Dysport absente | Ajouter « hypersensibilité à un constituant » (Dysport) et celle de BOTOX | AIPS 55057, 52433 |
| Léger | Situations spéciales, insuffisance hépatique et rénale | glucagon absent | Ajouter « GlucaGen peut être utilisé avec précaution » | AIPS 31489 |
| Léger | Bloc 2, intitulé de liste | « Liste DX.4 → DX.10 » | La liste va de DX.1 à DX.10 | Liste canonique |
| Léger | Point 8, tableau « Score HDSS » | « une autorisation de médicament pour un enfant ou une région non autorisée » | Reformuler : le HDSS ne fonde aucune autorisation hors indication | S3, S8 |
| Léger | Point 2 | DX.3, DX.5, DX.6 sans chiffre suisse | Écrire « donnée suisse non trouvée » | Q4 HELP |

## Questions ouvertes (HELP)

| N° | Constat C2 |
|---|---|
| Q4 | Reste ouverte (aucune étude de répartition étiologique) ; formulation honnête dans Bloc 2 |
| Q5 | Seuil de troponine T hs par sexe : ouvrir ESC 2023 (escardio.org) ; à vérifier, non affirmé ici |
| Q6 | Décision de Vial toujours requise : critère d'ordre actuel écrit et aligné ; le §9.1 strict changerait DX.1–DX.6 et les fichiers Phase B |

## Question finale

**Non.** Le patient est traité en sécurité sur tout ce qui est dosé (aucune erreur AIPS, zéro critique), mais le score de 88,7 % reste sous le seuil de 90 %. Il manque :

- la classe et le mécanisme des traitements du tableau de corrélation (Q3.3) ;
- les médicaments d'urgence du SCA et du PPGL, ou leur renvoi explicite en Phase B (Q11.3) ;
- les contre-indications de Dysport et de BOTOX (hypersensibilité) (Q11.5) ;
- la société et l'année des critères de l'hyperhidrose, avec l'exemple corrigé (Q8.1) ;
- le seuil de troponine par sexe (Q9.4, HELP Q5) ;
- une ligne de prévention cardiovasculaire (Q12.1) et les chiffres suisses ou leur absence déclarée (Q2.1).
