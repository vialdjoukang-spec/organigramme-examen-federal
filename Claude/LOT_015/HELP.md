# LOT_015 — G15 Prise de poids, obésité : ce qui reste ouvert (mis à jour le 11.11.2026)

« DX.n » désigne `LOT_015_Phase_B_V0_DX.n.html` ; « Phase A » désigne `LOT_015_Phase_A_V0.html`.

## Lacunes ouvertes
- Tout le LOT : aucune recommandation suisse propre n'a été trouvée pour DX.3, DX.4, DX.5, DX.7, DX.9 et DX.10 ; les règles propres d'arrêt de travail, d'assurance-invalidité et les critères de sortie manquent dans chaque leçon.
- Tout le LOT : aucune source lue ne chiffre la sensibilité ni la spécificité des signes physiques.
- Phase A et DX.3 : le terme français officiel du nouveau nom du SOPK (PMOS, 2026) n'a pas été trouvé ; le consensus de Teede 2026 n'a été lu qu'en résumé.
- Phase A : aucun seuil universel de prise de poids pathologique ; la limitation LS de Wegovy (« dès 12 ans et 60 kg ») n'a pas été relue.
- DX.1 : manquent la mortalité suisse attribuable à l'obésité, les règles d'incapacité après chirurgie et la part de DX.1 parmi les personnes obèses.
- DX.1 : l'acanthosis nigricans est téléchargé (`images/Acanthious_nigricans_new_photo_for_diagnosis_pigmentation_ap.webp`) mais n'est pas inséré au point 6.
- DX.2 : la Revue médicale suisse 2022 (S4) est illisible (page anti-robot) ; les chiffres qui reposaient sur elle seule sont absents (espérance de vie, excès de mortalité, risques d'obésité, pertes de poids par stratégie).
- DX.2 : manquent la prévalence suisse et le mécanisme des inhibiteurs de l'intégrase ; la fenêtre « cortico » garde le schéma chirurgical de Solu-Cortef, tenu ailleurs dans DX.9 seulement ; la fenêtre « second » recopie les seuils ESC 2026 de DX.6.
- DX.3 : manquent la mortalité et le coût suisses, le seuil de laboratoire de la testostérone, la dose d'acide folique renforcée, la dose de létrozole et le remboursement du laser ; le clomifène n'a aucune spécialité autorisée en Suisse.
- DX.3 : l'échographie d'ovaire polykystique est téléchargée (`images/PCO_polycystic_ovary.webp`) mais n'est pas insérée.
- DX.4 : manquent la répartition cantonale, les coûts suisses et la traduction française officielle de la CIM-11.
- DX.5 : manquent la mortalité suisse, le volume thyroïdien chiffré, la préparation avant la TSH et les critères de sortie après un coma myxœdémateux.
- DX.6 : le texte intégral de l'ESC 2026 (ehag100) et l'algorithme HFA-PEFF 2019 n'ont pas été lus ; le seuil FEVG ≥ 45 % avec IMC ≥ 30 kg/m² vient du diaporama officiel.
- DX.6 : la radiographie insérée porte des légendes anglaises ; un cliché brut reste à trouver.
- DX.7 : manquent l'incidence pédiatrique suisse, la mortalité et le coût suisses, la perte de poids quotidienne cible sous diurétique et l'antibiotique de la péritonite.
- DX.7 : le cliché d'œdème prenant le godet (`File:Pitting Edema2008.jpg`, CC BY-SA 3.0) reste à insérer au point 6.
- DX.8 : manquent la prévalence suisse, les prévalences d'Orphanet, les délais des panels génétiques et les seuils de leptine et de pro-insuline ; la métréleptine et le calcium IV n'ont aucune spécialité suisse ; aucune image.
- DX.9 : manquent l'incidence et le coût suisses et le seuil d'ACTH ; le kétoconazole et le lévokétoconazole n'ont aucune forme orale autorisée en Suisse ; le consensus SFE 2022 n'a pas été relu ; aucune image.
- DX.10 : manquent l'incidence suisse, la conduite d'urgence des troubles thermiques, la sédation de l'enfant, le schéma d'induction pubertaire et un texte suisse sur la chirurgie du craniopharyngiome.
- DX.10 : la légende d'origine de l'IRM insérée est tronquée ; le grade du repère C reste imprécis.
- Tout le LOT : `controle_lot.py verifier` refuse encore les ressources externes partagées (`forme.css`, `forme.js`) et les lignes de plus de 3 000 caractères ; le harnais doit les admettre.

## Décisions en vigueur
- Tout le LOT : chaque fichier pèse 149,6 à 150,0 Ko, au plafond ; toute image ou tout ajout exige un retrait équivalent.
- Tout le LOT : les fenêtres sont des `section.fenetre` ouvertes par `:target` ; les fiches de médicament portent la classe `mb` ; les appels AIPS pointent vers `sb-aips-<n° Swissmedic>` ; dans les cellules de tableau, les appels non AIPS restent textuels (« [S5] »).
- Tout le LOT : le point 1 ne porte que la définition ; les notions voisines figurent au point 4 sous « Situations frontières » ; l'examen physique tient en une fenêtre par région.
- Tout le LOT : un fait commun vit dans une seule leçon ; les autres y renvoient. Wegovy, Mounjaro, Saxenda, critères LS et chirurgie : DX.1. Schéma chirurgical de l'hydrocortisone et freinage à 1 mg : DX.9. Crise surrénale de l'adulte et de l'enfant : urgence A de DX.8. Lasix, Aldactone et Esidrex : DX.6. Clexane et Bactrim : DX.7.
- Tout le LOT : une dose de recommandation absente de l'AIPS le dit dans la phrase ; l'ancre AIPS ne sert qu'à cette mention.
- Tout le LOT : le freinage minute à 1 mg de dexaméthasone suit l'ESE 2020 et l'ESE-ENSAT ; l'AIPS n° 57974 n'est citée que pour la molécule et le comprimé de 1 mg.
- Phase A : la définition suit l'EASO (Busetto 2024) : IMC ≥ 30 kg/m², ou IMC ≥ 25 kg/m² avec rapport tour de taille/taille > 0,5 et atteinte ; l'entrée AIPS S8 reste groupée, une ligne par numéro d'autorisation.
- DX.1 : sous Mounjaro (AIPS n° 68726), la contraception est « recommandée » et la barrière « conseillée » ; Saxenda (n° 65899) est « non recommandé » si l'obésité est endocrinienne, alimentaire ou médicamenteuse ; sous Xenical (n° 54282), le polyvitaminé « peut être envisagé » chez l'adulte.
- DX.1 : le remboursement de Wegovy s'arrête à 16 semaines selon la liste des spécialités, contre 28 semaines dans l'AIPS n° 68798 ; le plafond « 1 stylo, 2,4 mg » relève de la LS ; les 7,2 mg ne sont pas remboursés.
- DX.2 : le seuil de Cushing de la prednisone vaut plus de 7,5 mg/j (AIPS n° 29349) ; les paliers de décroissance viennent de l'ESE 2024 ; avant une intervention mineure, Spiricort (n° 38840) écrit 100 mg et Solu-Cortef (n° 23533) 200 mg : la divergence reste écrite.
- DX.2 : la quétiapine ≤ 50 mg est hors indication ; « non recommandé en insuffisance rénale terminale » figure dans l'AIPS Wegovy, non dans celle d'Ozempic.
- DX.3 : Androcur-10 oppose la ligne directrice 2023 à l'AIPS n° 37482 ; la divergence est enseignée au point 14.
- DX.4 : aucune AIPS n'indique un médicament dans l'hyperphagie boulimique ; Elvanse est hors information professionnelle ; Fluctine 60 mg est réservée à la boulimie ; Wegovy ne porte pas la mise en garde suicidaire.
- DX.5 : la dose initiale de lévothyroxine (25–50 µg/j) est commune à la HAS et à l'AIPS Euthyrox n° 54949 ; la HAS adapte toutes les 6 à 8 semaines, l'AIPS toutes les 2 à 4 semaines : la divergence est écrite.
- DX.5 : les anti-TPO s'écrivent en kUI/L ; les apports en iode s'écrivent en toutes lettres.
- DX.6 : la finérénone « peut remplacer » l'antagoniste stéroïdien si FEVG ≥ 50 % (ESC 2026) ; l'AIPS Kerendia n° 68130 fait éviter l'association à un autre antagoniste ou à un épargneur de potassium.
- DX.6 : la HFA donne 400–600 mg de furosémide, l'AIPS Lasix n° 30630 1 500 mg/j au maximum ; la digoxine n'a aucune spécialité autorisée.
- DX.7 : les quantités non médicamenteuses (protéinurie, sodium, protéines) s'écrivent en g/24 h ou g/g ; les schémas KDIGO 2021 et 2025 de prednisolone sont « hors AIPS » de Spiricort ; l'hypovolémie impose l'arrêt des diurétiques et une perfusion d'albumine.
- DX.8 : les doses de crise surrénale suivent la BSPED 2023 et l'ESE/ES 2024 ; l'AIPS Solu-Cortef ne chiffre aucune dose de crise ni dose pédiatrique d'urgence.
- DX.8 et DX.10 : le setmélanotide (Imcivree n° 69694) n'a pas l'indication MC4R ni l'obésité hypothalamique ; les doses européennes sont « hors AIPS suisse ».
- DX.9 : Signifor LAR suit l'AIPS n° 65148 (10 à 40 mg ; Child-Pugh B : départ 10 mg, maximum 20 mg ; Child-Pugh C contre-indiqué) ; l'obésité sans signe spécifique ne se teste pas en routine (ESE R.3.1).
- DX.10 : le test au Synacthen suit l'AIPS n° 31723 (0,25 mg, cortisol à 30 minutes) ; le prélèvement à 60 minutes vient de l'ESE/ES 2024 ; la dose de crise ne se donne jamais sans l'âge.

## Doutes médicaux à trancher
Aucun.
