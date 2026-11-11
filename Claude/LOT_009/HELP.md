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
