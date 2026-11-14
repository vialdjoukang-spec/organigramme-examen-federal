# Corrections des images IMG-105 à 165 (TH.json), d'après AUDIT_IMAGES_042_165.md (14.11.2026)

Méthode : patch appliqué, rendu `_verif/` régénéré et regardé pour chaque repère déplacé.

## Critiques
- 105 : image retirée (infarctus septique, bosse de Hampton, PMC8683236). Aucun autre candidat ne montre de condensation lobaire → `images.manque`.
- 119 : image retirée (pneumocystose sous abatacept, PMC4182847, coupe apicale). Aucun candidat valable → `images.manque`.
- 149 : technique « maladie de Fabry » ; lésion et sémiologie réécrites (phénocopie de CMH, segment basal inféro-latéral).

## Majeurs
- 112 : « (même cas que IMG-110) » ajouté ; sémiologie complétée par la volumétrie NELSON et la position EUPS 2017, à côté de Lung-RADS (ACR).
- 116 : repère 2 renommé « plaque pleurale calcifiée » ; sémiologie corrigée.
- 122 : repère 2 (cardiomégalie) déplacé de l'électrode ECG vers la silhouette cardiaque gauche (70 ; 74).
- 140 : repère 1 déplacé sur la fuite de contraste (55 ; 50).
- 153 : normal remplacé par la RX AP normale d'adulte de soins intensifs (PMC2700481), à la place du nourrisson.
- 154 : option 2 retenue : lésion « dilatation de l'aorte ascendante disséquée » ; la sémiologie ne prétend plus montrer le voile.
- 158 : repère 1 déplacé sur la pointe de la flèche, crosse fixante (48 ; 31).
- 164 : PMC4175749 absent des candidats ; la sémiologie précise que la fracture est isolée et que le volet exige ≥ 3 côtes consécutives fracturées en 2 points.

## Mineurs
- 106 : repère 1 placé sur l'arbre en bourgeons (25 ; 55).
- 108 : lésion « cavité à paroi épaisse » (niveau hydro-aérique non démontré).
- 135 : repère posé dans l'épanchement déclive (27 ; 74), et non à l'interface ni sur la côte.
- 136 : « épaississement pleural résiduel après traitement » ajouté.
- 130 (nouveau-né infecté par la COVID-19), 133 (enfant de 9 ans), 155 (anévrisme sur Takayasu), 156 (enfant de 9 ans), 163 (abcès sur mastite granulomateuse) : contexte précisé dans `technique`.
- Série TH, pathos basales (107, 109, 115, 117, 120, 128, 129, 164) : aucune TDM basale normale libre parmi les candidats. La technique du normal signale le niveau de coupe différent.

## Fichiers
`img/IMG-105_*` et `img/IMG-119_*` et leurs `_verif` supprimés. JSON validé, `generer.py` relancé.
