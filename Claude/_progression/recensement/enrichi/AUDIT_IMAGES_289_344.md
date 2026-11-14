# Audit radiologique des images IMG-289 à IMG-344 (MI_TR.json), 14.11.2026

Méthode : les 48 copies `_verif` ont été regardées ; l'image brute de 304 a été agrandie. Légende et licence de chaque article relues dans le XML Europe PMC, y compris pour les figures choisies hors candidats.
Sans image (`manque`) : 301, 309, 312, 330, 331, 339, 342, 344.

**Verdict : corrections requises** (0 critique, 2 majeurs).

## 1. Majeurs

| id | Défaut constaté | PATCH exact |
|---|---|---|
| 340 Maltraitance | Le repère 3 « lésion métaphysaire du tibia » (60 ; 86) est posé sur le 3e cliché de la rangée inférieure. Ce cliché est un **avant-bras avec le coude** (main en haut, radius et ulna, palette humérale) : la pointe désigne la région du coude, pas un tibia. Les lésions métaphysaires tibiales de la légende (« metaphyses of tibias ») sont sur le cliché des membres inférieurs, en haut à droite. | Repère 3 : x = 82, y = 34 (métaphyse tibiale proximale gauche, à la pointe de la flèche blanche des auteurs). Contrôler sur `_verif`. |
| 326 RECIST | Le champ `normal` contient le scanner de référence **avant traitement**, qui montre la tumeur. Le texte le déclare, mais le rendu affiche l'étiquette « NORMAL » sur un cliché pathologique, ce qui enseigne une erreur de lecture. | Déplacer ce cliché du champ `normal` vers un champ `reference` affiché « RÉFÉRENCE (0 mois) ». Si le générateur ne gère pas ce champ : retirer `normal`, fusionner les deux temps (A : 0 mois, B : 6 mois) en un seul patho et déplacer le repère sur le panneau B. |

## 2. Points signalés, jugés un à un

| id | Jugement |
|---|---|
| 304 | Le diagnostic est bon. L'image agrandie montre un trait oblique de la fibula **à hauteur de l'interligne** : Weber B, compatible avec une fracture trimalléolaire. Un Weber C n'est pas nécessaire pour illustrer les règles d'Ottawa. La pointe du repère 1 (24 ; 48) est sur le bord latéral de la fibula, à côté du trait → mineur : x = 30, y = 47. |
| 337 | L'hémopéritoine survient après réanimation : il s'agit d'une lacération hépatique par le massage cardiaque, donc d'un traumatisme. Les fenêtres de Morison et pelvienne de l'eFAST sont démonstratives et les repères justes. Mineur : ajouter « lacération hépatique iatrogène ; même lecture chez le polytraumatisé » dans `technique`. |
| 299 | Le normal est repris de 300 (PMC9204292, « Normal A/P view X-ray of the knee »). Il est comparable (genou de face) : acceptable. |
| 321 | La date est masquée et aucune donnée nominative n'est visible. Salter-Harris II (légende fig. 18A) ; repères conformes. |

Licences des figures hors candidats, relues dans le XML : 299 PMC13547493 CC BY ; 305 PMC13212035 et PMC8197928 CC BY ; 324 PMC2579910 CC BY 2.0 et PMC3960191 CC BY ; 325 PMC2553402 CC BY 2.0 ; 337 PMC13552818 CC BY 4.0 ; 338 PMC13355908 CC BY 4.0 ; 341 PMC12057466 CC BY 4.0. Toutes sont libres et correspondent à la légende.

## 3. Mineurs

| id | Défaut constaté → PATCH |
|---|---|
| 325 | Le titre incrusté « Advantages of PET/CT in staging lung cancer » est visible → recadrer la bande supérieure (environ 12 %) et recalculer les y : y' = (y − 12)/0,88. |
| 323 | Le normal (gastrocnémien) et le patho (poplité) sont deux muscles différents → le déclarer dans `technique`. |
| 329 | Le normal vient d'un enfant (rachis thoraco-lombaire), le patho d'un adulte (thoracique) → déclarer l'âge. |
| 292 | Le signal visible (graisse claire, liquide sombre) évoque un T1, alors que la légende dit « T2 ». C'est déjà déclaré (« selon les auteurs ») : acceptable. |
| 338 | La pointe (71 ; 53) est sur le bord du secteur → la rapprocher de la paroi latérale du VG, x = 66, y = 50, puis contrôler. |
| 341 | L'entité « Radioprotection de l'enfant » est illustrée par une appendicite à l'échographie, ce qui est cohérent (examen sans rayons X en premier) → ajouter cette justification dans `technique`. |
| 327 | Le traceur (68Ga-PSMA-11) n'est pas nommé dans la légende de la fig. 4, seulement dans le texte de l'article → `technique` + « (selon le texte de l'article) ». |

## 4. Contrôles sans défaut

289, 290, 291, 293, 294, 295, 296, 297, 298, 300, 302, 303, 305, 306, 307, 308, 310, 311, 313, 314, 315, 316, 317, 318, 319, 320, 322, 324, 328, 332, 333, 334, 335, 336, 343.

Le crédit est présent partout. Aucune licence NC ni absente.
