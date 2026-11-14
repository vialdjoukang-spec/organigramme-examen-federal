# Corrections des images IMG-219 à IMG-237 après l'audit du 14.11.2026

Toutes les corrections ont été appliquées. Chaque copie `_verif` touchée a été régénérée, puis regardée.

## Majeurs
- **221** : un kyste complexe a été trouvé dans le pool des candidats. Il remplace le kyste d'aspect simple : PMC7200970 fig. 16c, TDM injectée d'une masse kystique à cloison épaisse nodulaire, classée Bosniak IIIn par les auteurs, CC BY 4.0, licence relue dans le XML. Le repère 1 est posé sur la cloison nodulaire.
  - `technique` rappelle les critères de Bosniak 2019 (III / IV).
  - Le normal reste en `manque_normal`.
- **237** : l'image est gardée. `technique` précise qu'il s'agit d'une forme non athéromateuse, alors que la forme typique associe des sténoses athéromateuses ostiales d'au moins 2 troncs. `images.a_chercher.patho` demande des sténoses athéromateuses calcifiées du tronc cœliaque et de l'AMS.
- **235** : `technique` précise « AAA rompu ».
  - Repère 1 : la lumière opacifiée mesure 51 mm, et le diamètre se mesure paroi externe à paroi externe.
  - Repère 2 : le croissant hyperdense signe la fissuration.
  - Repère 3 ajouté : hématome rétropéritonéal en (58 ; 50), contrôlé sur `_verif`.

## Mineurs
- **225** : repère en (33 ; 54) ; `technique` précise « photographie d'écran teintée ».
- **233** : `semio` reprend l'IR à 0,58 et l'onde tardus-parvus du pôle supérieur, selon la légende.
- **224** : `technique` précise qu'il s'agit d'un adénome cortisolique dans un contexte de Cushing, que la densité n'est pas précisée, et rappelle la définition de l'incidentalome (≤ 10 UH).
- **226** : `semio` signale la cause inflammatoire (Takayasu) et la rapproche de la sténose athéromateuse ostiale, plus fréquente.
- **228** : `technique` précise qu'il s'agit d'un enfant (hydronéphrose associée à un abcès rétropéritonéal) et que le normal est adulte.
- **220** : `technique` précise que la phase est unique et rappelle le critère de rehaussement > 20 UH.

## Contrôle final
`enrichi/AB.json` est un JSON valide et `python3 generer.py` passe. Toutes les licences retenues sont des CC BY.
