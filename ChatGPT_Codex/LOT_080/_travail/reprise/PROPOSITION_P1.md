# LOT_080 — proposition enrichie pour contre-audit P1

Aucun gel effectué. Auteur : /root/sources_lot080. Date :10novembre2026.

Synthèse qualitative contextualisée : présentations courantes de croissance, causes acquises usuelles de l’adulte, étiologies de terrain spécifique puis causes rares. Le tableau conserve pour chaque entité son âge et sa présentation. Les positions ne sont pas annoncées comme dix probabilités conditionnelles universelles.

| DX | Entité précise | Cadre | Justification |
|---|---|---|---|
| DX.1 | Scoliose idiopathique de l’adolescent | Croissance, surtout poussée pubertaire, courbure structurale avec rotation | Elle ouvre la synthèse parce que la source pédiatrique suisse la désigne comme la forme la plus fréquente de scoliose ; elle constitue le prototype structural de la croissance. |
| DX.2 | Cyphose posturale de l’adolescent | Adolescent avec dos rond réductible sans cunéiformisation structurale | Elle appartient aux premières causes courantes parce que le NHS la décrit comme la cyphose la plus commune, particulièrement chez les adolescents. |
| DX.3 | Attitude scoliotique fonctionnelle par inégalité de longueur des membres inférieurs | Déviation frontale avec bassin oblique et différence de longueur objectivée | Elle reste dans le groupe des causes réversibles de première ligne avant les malformations et atteintes neuro-axiales rares ; l’étude européenne et SOSORT établissent sa concurrence avec la scoliose structurale. |
| DX.4 | Maladie de Scheuermann thoracique | Adolescent avec cyphose thoracique rigide et cunéiformisation vertébrale | Après les présentations posturales réductibles, cette cause structurale de croissance est définie par les critères radiographiques ; sa forme thoracique typique est précisée pour éviter une catégorie indifférenciée. |
| DX.5 | Scoliose lombaire dégénérative de novo de l’adulte | Adulte vieillissant sans scoliose idiopathique préexistante connue | Elle ouvre la partie adulte de la synthèse : la source spécialisée suisse la place parmi les formes les plus fréquentes ; HUG distingue la forme de novo de la scoliose idiopathique vieillissante. |
| DX.6 | Fracture vertébrale ostéoporotique avec cyphose acquise | Âge avancé ou fragilité osseuse avec réduction de hauteur vertébrale | Elle suit la déformation dégénérative dans le groupe des causes acquises courantes ; la directive suisse la décrit comme fréquente et relie l’effondrement vertébral à la cyphose. |
| DX.7 | Spondylarthrite axiale radiographique avec ankylose rachidienne | Adulte avec histoire inflammatoire et limitation structurale progressive | Cette cause inflammatoire spécifique vient après les grandes causes posturales, dégénératives et de fragilité ; elle est distinguée d’une simple rachialgie inflammatoire sans déformation. |
| DX.8 | Camptocormie associée à la maladie de Parkinson | Patient Parkinson avec flexion thoracolombaire debout, réductible au décubitus | Elle représente une cause de terrain neurologique défini ; la revue européenne récente la qualifie de fréquente chez les patients Parkinson, sans l’étendre à la population entière. |
| DX.9 | Scoliose congénitale par hémivertèbre | Enfant avec anomalie de formation vertébrale, parfois révélée durant la croissance | Elle est placée dans le groupe rare : la source suisse décrit les malformations congénitales comme très rares ; l’hémivertèbre fixe une entité précise plutôt que toutes les malformations. |
| DX.10 | Scoliose révélatrice d’une syringomyélie foraminale associée à une malformation de Chiari I | Scoliose atypique ou signes neurologiques, parfois déformation comme seul mode de révélation | Elle clôt la fréquence proposée comme cause neuro-axiale rare mais décisive ; la série européenne établit sa révélation scoliotique et le PNDS2024 apporte l’évaluation actuelle. |

PROPOSITION_P1.json contient les extraits exacts, discriminants et limites de chaque position. INDEX_SOURCES.json référence les textes récupérés et leurs SHA256. Dix paquets propres aux entités sont prêts sous paquets/DX.i/ ; MATRICE_14_POINTS.json propose la sélection par point. Cette sélection lexicale doit être relue avant rédaction.

## Arbitrages demandés à l’audit

- Force de l’interclassement des causes courantes de croissance et de l’adulte.
- Place de la scoliose fonctionnelle : ne pas transformer la fréquence de l’inégalité en celle de la déformation.
- Ordre relatif axSpA et Parkinson dans leurs terrains.
- Ordre interne des causes rares et précision de la syringomyélie foraminale.
- PrioritésE proposées, à adapter aux signes cliniques effectifs.
