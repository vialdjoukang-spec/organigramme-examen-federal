# Audit indépendant et couverture — disciplines alliées v5

## Conclusion
**Prêt comme référentiel documentaire, pas validé cliniquement ou juridiquement.** La v4 était fidèle quant au rattachement géométrique des disciplines ; sa « condensation » ne réduisait que très peu le contenu. Cette v5 reformule les phrases sans ajouter de recommandation, conserve les 137 couples et corrige la répétition « maintien du maintien ».

**Ce n'est pas une forte compression.** La conservation de tous les contextes, techniques, chiffres, conditions, exceptions et objectifs limite la réduction sûre. Aucune promesse d'une version « radicalement squeezée » n'est justifiée. Je n'ai pas identifié de réduction beaucoup plus forte sans risquer d'abandonner des détails ou de remplacer les phrases par des codes, options exclues ici. Ce n'est pas une preuve mathématique d'impossibilité.

## Périmètre et indépendance
PDF unique : 7 pages, 37 364 octets, SHA-256 `2b95b44c85a2a2b0bde82686e3145ab3eede243a93fdedb30362379d70b28d32`. Aucun document antérieur ou autre dossier traité. Aucune modification de v4, du PDF ou du premier référentiel v3. Aucun accès GitHub, HTTP ou modèle externe.

Extraction indépendante par centres des caractères et frontières horizontales réelles traversant la colonne N° : aucun remplissage automatique des noms à partir d'une ligne vide. Les centres des 137 cellules de discipline se rattachent à 45 groupes numérotés. Leurs libellés et textes normalisés coïncident avec l'extraction géométrique du producteur. Les pages 1 et 7 ont aussi été relues visuellement.

## Résultats
| Contrôle | Résultat |
|---|---|
| Spécialités | 45, mêmes numéros, noms et ordre |
| Couples discipline / moment-indication | 137 ; aucune fusion, suppression ou permutation |
| Libellés de discipline | Conservés à l'identique |
| Nombres et comparateurs | Séquences exactes dans chaque ligne |
| Grades romains et négations « sans/non » | Séquences exactes dans chaque ligne |
| Contextes / temporalités / conditions | Confrontation documentaire des 137 lignes, corrections avant livraison |
| Annotations de lien / URL explicite | 0 / 0 ; domaine textuel `siwf.ch` conservé |
| Instructions cliniques nouvelles | Aucune recherchée/ajoutée ; reformulation des seules indications source |
| Allégations de validation de la source | Attribuées à la source, pas reprises comme garantie |

Exemples de contraintes conservées : 30 minutes post-injection ; J-15 à J-1 et J0–J2 ; au moins 3 séances hebdomadaires pendant 3 à 6 mois ; 36 séances ; seuils NRS-2002, DFG et perte pondérale ; 56e jour et absence de franchise ; 24h **avant toute** reprise per os ; absence de débridement agressif sur lit artériel non restauré ; apparition du neutropénique fébrile ; grade IWGDF ; J14–J21 **dès** ablation de sonde. Les modalités ambulatoire/stationnaire, populations, alternatives et conditions locales restent attachées à leur ligne.

L'audit documentaire a rétabli pendant la réécriture les nuances « post-chirurgie », apprentissage pratique, muscles inspiratoires, courbe de poids, pose d'accès, calcul dosimétrique, contrôle des apports sodés, suivi de prise des psychotropes, etc. Elles ne sont pas considérées comme du superflu. Les divergences cliniques éventuelles du document source ne sont pas arbitrées.

## Mesures réelles (octets UTF-8, pas jetons)
| Mesure comparable | Source | v4 | v5 |
|---|---:|---:|---:|
| Somme libellés de discipline + moments/indications | 34268 | 33870 | 31903 |
| Markdown entier | sans objet | 39240 | 36724 |

- Corps utile : **−6.9 %** par rapport à la source ; **−5.81 %** par rapport à v4.
- Fichier Markdown entier : **−6.41 %** par rapport à v4.
- Le PDF binaire fait 37 364 octets : le comparer directement au Markdown ne mesure pas une économie d'inférence. Même si le Markdown reste volumineux, son contenu est accessible et sélectionnable sans analyse PDF.
- Aucun jeton, tarif, gain monétaire ou temps de lecture humain mesuré. Aucun pourcentage financier revendiqué.

## Preuves et reproduction
`COUVERTURE.json` contient les 137 textes source et condensé, leurs SHA-256, pages/rectangles/groupes, différences réversibles et contrôles numériques. Le vérificateur portable valide le paquet et ce mapping ; il **ne prouve pas le sens médical**.

- Intégrité et reconstruction : `python3 VERIFIER_PAQUET.py`.
- Audit indépendant contre le PDF (PyMuPDF requis) : `python3 audit_source.py /chemin/SOURCE_DISCIPLINES_ALLIEES.pdf`.
- Les en-têtes de tableau répétés ont été retirés ; l'introduction, les allégations d'audit, le cadre et les notes finales sont regroupés dans le Markdown. Les détails cliniques ne sont pas externalisés au JSON : le document principal se suffit à lui-même.

Limites : source scientifique/juridique non vérifiée ; aucune disponibilité de `siwf.ch` testée ; relecture documentaire non experte ; les tests lexicaux ne prouvent pas l'équivalence sémantique universelle. Les 137 reformulations ont été confrontées aux textes sources mais ne constituent pas une garantie d'absence de toute erreur. Aucun nouveau cours ni contenu médical autonome produit. Les copies identiques dans les deux dépôts restent à la charge du parent.

Markdown final SHA-256 : `8a03142b40df0974810f46531dc239d453b465a098f6956bd3403ee053194d3b`.
