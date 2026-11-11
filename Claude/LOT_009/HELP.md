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
