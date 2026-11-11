# LOT_009 — lacunes et réserves (hors cours)

## Outil
- `renfort_citations.py` (passe mécanique) ne lit que la première source d'une citation groupée (`<sup><a sb-2>,<a sb-3></sup>` → seulement sb-2) et reporte la citation d'une cellule ou d'un item de liste au suivant. Les leçons du LOT_009 ont été reconstruites depuis `origin/main` avec une copie corrigée (toutes les sources du bloc ; pas de report entre cellules ni entre items). L'outil partagé n'a pas été modifié (hors périmètre LOT_009) : correctif à reporter dans `Claude/_outils/renfort_citations.py`.

## Phase A (G9 Prurit)
- Données manquantes (ancien bloc « Lacunes des données ») : prévalence suisse du prurit en population générale, coût suisse, fréquence suisse des DX.14 et DX.15, valeurs de référence suisses du bilan, critères de durée de l'urticaire, produits de contraste et IRM selon le dispositif, texte de la situation de départ G9, plan de vaccination suisse complet et dispositions LAI.
- Aucune source ne mesure la fréquence de chaque DD parmi les patients suisses qui démangent.
- Doses : référence AIPS groupée [19] (S19, une spécialité et son n° Swissmedic par molécule) ; chaque nombre de dose a été retrouvé dans le texte AIPS lu (index Refdata du 08.10.2026, lu le 10.11.2026).
- Images : aucune image insérée (la Phase A ne porte pas de signe visuel propre).

## Images (toutes les leçons DX)
- Wikimedia Commons ne répond pas (limitation 429 : `cliche.py chercher` reste bloqué au-delà de 90 s le 11.11.2026). Aucune image insérée, aucun titre de fichier à mettre en file. À faire dès que l'API répond : point 6 (signe visible) et point 9 (modalité décisive) de chaque DX — eczéma (DX.1), xérose et eczéma craquelé (DX.3), urticaire et dermographisme (DX.7), ictère/lésions de grattage (DX.10).

## DX.1 (Eczéma)
- Point 1 : la phrase AIPS d'Advantan® (formes d'eczéma) et le code CIM-10 L20–L30 sont déplacés au point 8 ; les notions proches vont au point 4.
- ORANGE résiduel : phrases longues portées par les définitions en infobulle (span.df) et quelques intitulés de situations spéciales ; le contenu est conservé tel quel.

## DX.2 (Prurit d'origine mixte)
- Ajouts sourcés (guide européen S2k 2025, PMC12529596, lu le 11.11.2026 ; série bernoise Lehmann 2020, PMC9128882) : fenêtre « Caractérisation du prurit mixte » (section 5.1, six questions, NRS/EVA, qualité), fenêtre « Sujet âgé » (section 6.6.1), association du groupe III aux catégories mixte et « autre » (Lehmann, tableau I et carte sémantique).
- Citations : les mesures générales reçoivent [2] (tableau 5 du guide) ; les citations AIPS reportées par l'outil sur des phrases sans médicament ont été retirées.

## Correction médicale (Phase A)
- Prégabaline : l'AIPS Lyrica® 57057 (version du 01.07.2026) exclut la prégabaline si Clcr < 30 mL/min ; les anciens paliers « Clcr 15–30 : 25 à 150 mg/j ; < 15 : 25 à 75 mg/j » (fiche, tableau pharmacologique, situations spéciales) ont été remplacés. La question d'examen qui en dépendait a été retirée.
- Vérification des doses : chaque nombre d'une phrase de dose est recherché dans la rubrique « Posologie/Mode d'emploi » de l'AIPS lue (jusqu'aux contre-indications) ; une phrase non vérifiée ne reçoit pas de citation AIPS et reste signalée.

## DX.3 (Xérose cutanée)
- Point 1 : groupe I de l'IFSI et place CIM-11 (ED54) déplacés au point 4 ; voisins exclus en fin de point 4.
- Lacune (retirée du cours) : aucune sensibilité ni spécificité chiffrée des signes d'examen dans les sources lues.
- Ajout sourcé : fenêtre « Caractérisation du prurit de la xérose » (guide européen S2k 2025, section 5.1 et 6.6.1).
- Citations AIPS vérifiées : Lyrica® 57057 (exclusion sous 30 mL/min), Neurontin® 52520 (titration, palier < 15 mL/min), Zyrtec® 48143 (5 mg/j de 30 à < 60 mL/min).

## DX.4 (Maladies systémiques)
- Point 1 : la liste des causes est déplacée en fin de point 4.
- Doses « hors AIPS » (colestyramine 4–16 g, rifampicine 300–600 mg, naltrexone 50 mg, sertraline 75–100 mg et 25 mg au départ, gabapentine 300 mg 3×/semaine après dialyse, prégabaline 50 mg un jour sur deux, paroxétine 20–40 mg, mirtazapine 15–30 mg) : chaque nombre retrouvé dans le guide européen S2k 2025 (tableaux des options thérapeutiques) ; la phrase cite le guide et l'AIPS de la molécule.
- Bézafibrate : l'AIPS Cedur® retard 45352 contre-indique le produit quand la clairance vaut 60 mL/min ou moins (le cours disait « sous 60 ») ; corrigé.
- Citations groupées scindées (une source par appel) pour que le contrôle lise chaque source.

## DX.5 (Composante psychique)
- Point 1 : distinctions F45.8, F54, F43.2 et délire d'infestation déplacées en fin de point 4.
- Ajout sourcé : fenêtre « Caractérisation du prurit à composante psychique » (Schneider et al. 2020, PMC9128937, lu le 11.11.2026 : début, type, vocabulaire, déclencheurs, horaire, réactions ; 77,7 % contre 48,8 % de variations liées au stress).
- Doxépine : 25 à 100 mg/j vérifiés dans le guide S2k ; AIPS Doxepin Rivopharm 69433 citée pour la molécule.
- Les consignes à l'impératif deviennent « Il faut … » (phrases verbales reconnues), sans changement de contenu.

## DX.6 (Éruption / prurit médicamenteux)
- Point 1 : diagnostics à ne pas confondre (DX.7, DX.9, DX.10) déplacés au point 4.
- Lacunes retirées du cours : « aucun critère officiel suisse n'a été lu » ; critères cliniques détaillés du DRESS et de la nécrolyse non relus.
- À vérifier hors cours : la décroissance des glucocorticoïdes (DRESS sévère 3 à 6 mois, DRESS léger 6 semaines à 3 mois) n'a pas pu être relue (texte intégral Brüggen 2024, PMC10652220, inaccessible le 11.11.2026) ; ces phrases restent sans citation.
- Ajout sourcé : fenêtre « Caractérisation du prurit médicamenteux » (guide S2k 2025 : 5 % des réactions, 12 mois, HES 12–42 %, deux tiers, 15 mois).

## DX.7 (Urticaire)
- Point 1 : les trois entités voisines vont en fin de point 4.
- Lacunes retirées du cours : examens du C4/C1-inhibiteur « non détaillés dans les sources lues » ; valeur chiffrée des signes d'examen et mesures de prévention non établies dans les sources lues.
- Ajouts sourcés (guide S2k 2025) : fenêtre « Caractérisation du prurit urticarien » ; fenêtre « Prurit de l'urticaire : données du guide européen » (antihistaminiques, cétirizine IV, 30 minutes sous glucocorticoïdes IV, omalizumab ISS7 −9,8/−8,1, antileucotriène, ciclosporine).
- Le guide EAACI 2022 (Zuberbier) n'est pas en accès libre : citations antérieures conservées.
- ORANGE résiduel : phrases de posologie répétées d'une fiche médicament à l'autre (antihistaminiques), conservées pour que chaque fiche reste complète.
