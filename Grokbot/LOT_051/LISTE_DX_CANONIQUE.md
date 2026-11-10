# LISTE_DX_CANONIQUE — LOT 051

SSP S2.12, douleur de la paroi thoracique. Ordre : fréquence décroissante dans une seule série suisse, la cohorte TOPIC de premier recours (Swiss Med Wkly 2008, 672 patients, 59 médecins de famille romands, suivi de 12 mois ; identifiants d’extraits de `evidence/topic2008.md`). Les fréquences sont celles du tableau 1 de cette cohorte, inscrites à l’identique dans la Phase A. Un diagnostic grave conserve son rang de fréquence et reçoit en plus un rang E. Un diagnostic sans aucun cas dans la cohorte reçoit un rang ordinal, sans pourcentage (« Ne rang »). À fréquence égale, le diagnostic le plus grave passe devant.

| Rang | Nom exact | Fréquence (TOPIC, n = 672) | Extrait | Grave | Rang E |
|---|---|---|---|---|---|
| DX.1 | Syndrome de la paroi thoracique | 42,7 % (287 patients) | topic2008.2 | non | — |
| DX.2 | Maladie coronarienne | 12,6 % | topic2008.10 | oui | E1 |
| DX.3 | Douleur thoracique psychogène | 11,5 % (77 patients) | topic2008.2 | non | — |
| DX.4 | Infection respiratoire aiguë | bronchite aiguë 5,5 % (37) + pleurésie ou pneumonie 2,5 % (17) | topic2008.2 | non | — |
| DX.5 | Œsophagite | 6,3 % (42 patients) | topic2008.2 | non | — |
| DX.6 | Embolie pulmonaire | 0,3 % (2 patients) | topic2008.2 | oui | E3 |
| DX.7 | Zona thoracique | 2 patients sur 672 | topic2008.2 | non | — |
| DX.8 | Dissection aortique | 8ᵉ rang, aucun cas | topic2008.9 | oui | E2 |
| DX.9 | Pneumothorax | 9ᵉ rang, aucun cas | topic2008.9 | oui (sous tension) | E4 sous tension |
| DX.10 | Péricardite aiguë | 10ᵉ rang, aucun cas | topic2008.9 | non | — |

Règles de classement appliquées.

1. DX.4 regroupe deux lignes du tableau 1 (bronchite aiguë, 37 patients ; pleurésie et pneumonie, 17 patients), soit 54 patients sur 672 (8,0 %, calcul de cette liste). La Phase A cite les deux composantes et non la somme.
2. DX.6 et DX.7 comptent chacun 2 patients ; l’embolie passe devant le zona parce qu’elle est grave.
3. DX.8, DX.9 et DX.10 n’ont aucun cas dans la cohorte (topic2008.9 : péricardite, dissection aortique et pneumothorax non rencontrés). Leur ordre suit la gravité : dissection, puis pneumothorax, puis péricardite.
4. Le syndrome de paroi occupe une seule place. Le traumatisme pariétal (26 patients, 3,9 %, topic2008.2) et le syndrome de Tietze (aucun vrai cas, verdon2007.6) en sont des variantes, sans rang propre.
5. L’hypertension artérielle aiguë (5 patients, 0,7 %, topic2008.2) est retirée : elle est un facteur de risque ou un signe d’accompagnement, non une cause de douleur de paroi à discuter en diagnostic différentiel.

Rangs E. Ils suivent la létalité et l’ordre d’exclusion de l’arbre décisionnel (Phase A, point 10) : E1 maladie coronarienne (ECG d’emblée, hugsca.0) ; E2 dissection aortique (20 % de décès préhospitaliers et survie de 80 % à 24 h sans traitement, blondon2009.4) ; E3 embolie pulmonaire (score, puis D-dimères, hugep.3) ; E4 pneumothorax sous tension (diagnostic clinique, décompression sans attendre l’image, hugthorax.1).

Comparaison externe, sans effet sur l’ordre. Cohorte hessoise de premier recours (n = 1212, bosner2013.0) : syndrome de paroi 46,6 %, maladie coronarienne 14,8 %, causes psychogènes 9,5 %, infection des voies respiratoires supérieures 8,1 %, reflux gastro-œsophagien 3,5 %, traumatisme 3,2 %, pleuropneumonie 2,1 %. L’ordre des cinq premiers DX est le même.

Phase B. Les fichiers DX.1 à DX.3 portent encore le bon intitulé. Les fichiers DX.4 à DX.10 ont été écrits sur l’ancienne liste ; leur titre ne correspond plus et ils sont notés « à refaire » dans `MANIFESTE.json`.

SHA-256 du texte de cette liste, ligne de signature exclue : e2a539b7b89d1b3af6473dd035c3d2397971ee357196fcf5d36cf87ac8bbed12 (détail dans `_travail/PA/gel_p1.json`).
