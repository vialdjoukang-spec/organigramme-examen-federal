# Sources officielles suisses — index pour la production des LOTS PROFILES

État vérifié le 22.10.2026 : chaque lien ci-dessous a répondu (HTTP 200) ce jour-là.

## 1. Les listes Swissmedic dans ce dossier (état au 30.09.2026)

Ces listes répondent à une seule question : **ce médicament est-il autorisé en Suisse, sous quel nom et sous quel numéro ?** Elles ne donnent aucune dose.

| Fichier | Contenu | Lignes |
|---|---|---|
| `Swissmedic_Medicaments_autorises_HAM.xlsx` / `.csv` | Médicaments à usage humain autorisés, avec indication, n° d'autorisation, titulaire, catégorie de remise | 11 107 |
| `Swissmedic_Liste_etendue_HAM.xlsx` / `.csv` | Même liste, plus le type d'autorisation, dont « export uniquement » | 11 107 |
| `Swissmedic_Emballages_autorises_HAM.xlsx` / `.csv` | Emballages autorisés, avec code ATC et n° IT | 18 101 |

Mode d'emploi :
- Cherche la DCI ou le nom de marque dans le CSV.
- Recopie le n° d'autorisation, par exemple Benerva® 10989.
- Vérifie le type d'autorisation dans la liste étendue. Un produit « export uniquement » n'est **pas** disponible en Suisse : c'est le cas de deux n° de Zometa®.
- Un produit absent des trois listes n'est pas autorisé en Suisse. Écris-le, par exemple : pamidronate, Moduretic®.

Page source officielle : https://www.swissmedic.ch/swissmedic/fr/home/services/listen_neu.html

## 2. Médicament : dose, voie, adaptations

| Source | Usage | Lien |
|---|---|---|
| AIPS — information professionnelle Swissmedic | **Seule source des doses**, voies, adaptations rénale, hépatique, pédiatrique et grossesse | https://www.swissmedicinfo.ch/ — accès professionnel : https://www.swissmedicinfo-pro.ch/ |
| Swissmedic — HPC/DHPC | Alertes de sécurité, changements de dose ou de seuil (ex. EpiPen® 19.01.2026) | https://www.swissmedic.ch/swissmedic/fr/home/humanarzneimittel/marktueberwachung/health-professional-communication--hpc-.html |
| Liste des spécialités OFSP | Remboursement LAMal, limitations | https://www.spezialitaetenliste.ch/ |
| Tox Info Suisse | Intoxications, antidotes | https://www.toxinfo.ch/ |

Le Compendium est interdit pour les doses.

## 3. Autorités fédérales

| Source | Usage | Lien |
|---|---|---|
| OFSP — Plan de vaccination suisse | Vaccins, schémas, rattrapages | https://www.bag.admin.ch/fr/plan-de-vaccination-suisse |
| CFV/EKIF | Recommandations vaccinales détaillées | https://www.ekif.ch/ |
| OFSP — Liste des analyses | Analyses de laboratoire remboursées | https://www.bag.admin.ch/bag/fr/home/versicherungen/krankenversicherung/krankenversicherung-leistungen-tarife/Analysenliste.html |
| Fedlex | Lois : LEp, LPTh, LAMal, OAMal | https://www.fedlex.admin.ch/ |
| OFS — santé | Épidémiologie suisse | https://www.bfs.admin.ch/bfs/fr/home/statistiques/sante.html |
| Obsan | Observatoire suisse de la santé | https://www.obsan.admin.ch/fr |
| ANRESIS | Résistances bactériennes en Suisse | https://www.anresis.ch/fr/ |
| Swissnoso | Infections nosocomiales | https://www.swissnoso.ch/ |

## 4. Sociétés et institutions suisses

| Source | Domaine | Lien |
|---|---|---|
| SSI — guidelines | Infectiologie : antibiothérapie | https://ssi.guidelines.ch/ |
| SSMIG/SGAIM | Médecine interne générale | https://www.sgaim.ch/fr/ |
| smarter medicine | Listes « Choosing Wisely » suisses | https://www.smartermedicine.ch/fr |
| ASSM/SAMW | Éthique, directives médico-éthiques | https://www.samw.ch/fr |
| Swiss Resuscitation Council | Réanimation | https://www.resuscitation.ch/ |
| Société suisse de cardiologie | Cardiologie | https://www.swisscardio.ch/ |
| SSED/SGED | Endocrinologie, diabète | https://www.sgedssed.ch/ |
| Société suisse de néphrologie | Néphrologie | https://www.swissnephrology.ch/ |
| SSGO/SGGG | Gynécologie, obstétrique | https://www.sggg.ch/ |
| Pédiatrie suisse | Pédiatrie | https://www.paediatrieschweiz.ch/ |
| palliative ch | Soins palliatifs, sédation | https://www.palliative.ch/ |
| Swiss TPH / healthytravel | Paludisme, médecine des voyages | https://www.swisstph.ch/fr — https://www.healthytravel.ch/ |
| Swiss Medical Weekly | Articles suisses en libre accès | https://smw.ch/ |
| PROFILES (référentiel de l'examen) | Objectifs SSP | https://www.profilesmed.ch (redirige vers smifk-cims.ch) |

## 5. Hiérarchie

1. Autorité ou société suisse, dans sa version la plus récente.
2. Si aucune source suisse n'existe : la recommandation européenne la plus récente (ESC, ERC, ESCMID, EASL, ESE, EULAR, EAACI, KDIGO, EMA).
3. Jamais une recommandation exclusivement américaine.
4. Si rien n'est trouvé : écris « donnée non trouvée dans les sources consultées ».
