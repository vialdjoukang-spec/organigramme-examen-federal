# Préaudit indépendant DX.1 et DX.6 — reprise 0240

Auditeur : `astra_audit_reprise`, distinct des deux rédacteurs. Date : 02.11.2026. Statut final de cette passe : **gel préparatoire possible pour DX.1 et DX.6 corrigés ; aucune validation thérapeutique finale.** Les quatorze parties et les quatorze réponses de chaque texte ont été contre-lues ; les changements ciblés ont été revérifiés. Aucun risque clinique bloquant identifié pour ce statut de travail explicitement non prescriptif. Les tableaux initiaux ci-dessous sont conservés comme historique ; le complément final en précise la résolution.

## Périmètre et limites de départ

| Domaine | Contrôle prévu / limite actuelle |
|---|---|
| Documents | Lire les quatorze parties de `_travail/DX1_REDACTION_0240.md` et `_travail/DX6_REDACTION_0240.md`, puis les preuves `evidence/dx1_0240.json` et `evidence/dx6_0240.json`. Aucun HTML à générer ni à auditer à ce stade. |
| Population | Parcours adulte ; ne pas transposer un protocole pédiatrique à l'adulte. Grossesse et situations particulières identifiées selon le périmètre réellement annoncé. |
| DX.1 / urgence | Déficit brutal même régressif, appel 144 sans délai, horaire pertinent, stabilisation et imagerie ; distinguer orientation initiale, confirmation, recherche étiologique et décision spécialisée. |
| DX.1 / limite documentaire | La page HUG grand public lue pour Phase A soutient l'imagerie et l'orientation, pas à elle seule les critères détaillés de reperfusion. Le protocole AVC pédiatrique ne valide pas un protocole adulte. |
| DX.6 / urgence | Terrain hépatique et complication distingués ; rechercher simultanément infection, hémorragie, troubles de conscience et atteinte rénale ; ne pas attendre une confirmation exhaustive pour traiter une défaillance. |
| DX.6 / bilan | Ponction diagnostique, cultures et cytologie selon présentation, culture négative non excluante ; endoscopie urgente en contexte hémorragique. La source CeMIR apporte un bilan contextuel, pas une batterie obligatoire universelle. |
| Chronologie | Aucun examen ou prélèvement ne doit induire un retard injustifié d'une action urgente ; distinguer gestes initiaux et bilan ultérieur. |
| Pharmacologie | Pour chaque dose : molécule, indication, voie, formulation/concentration, population, unité, fréquence, durée, maximum et adaptations effectivement proposés. Vérifier que le passage AIPS correspond au produit et à l'indication, et exposer toute limite ou usage hors indication documenté. |
| Swissmedic | Vérifier les identifiants contre le document source exact ; ne pas confondre numéro d'autorisation, numéro de présentation ou identifiant de fichier. Aucun numéro ne sera déduit du seul nom de marque. |
| Absence de preuve AIPS | Le gel pédagogique de Phase A sans doses n'a validé aucune posologie. Un extrait de recommandation ou de cours ne remplace pas une lecture AIPS ciblée. Toute preuve manquante sera nommée précisément, sans inventer une concordance. |
| Verdict | Rapport factuel sans score, réserves actionnables par partie ; aucun verdict de validation médicale humaine et aucun gel automatique. |

## Résultats

En attente de livraison confirmée par le coordinateur. Les constats de cette section seront complétés uniquement après lecture des fichiers effectivement livrés et des passages probants associés.


## DX.6 — première contrelecture clinique

Les quatorze parties et les quatorze questions/réponses ont été lues intégralement, ainsi que `evidence/dx6_0240.json`. Contrôle ciblé des nouveaux caches `dx6_0240/lectures_ch_ue.json` et `diagnostic_consensus.json` ; les preuves CeMIR/HUG déjà auditées ont été réutilisées. Texte initial audité SHA-256 : `77a29764b5d2c9f15aba99102f63cb827a6b3ad8d498013f9c836a2724425af7`.

**Verdict provisoire DX.6 : base de préparation recevable ; non finalisable comme monographie thérapeutique.** Deux précisions cliniques sont recommandées ci-dessous. Une recherche AIPS complémentaire est annoncée ; elle n'a pas encore été reçue ni validée par cet auditeur.

| Partie / domaine | Constat | Action / statut |
|---|---|---|
| P1–3, population et mécanismes | Titre canonique large mais parcours cirrhose adulte explicitement délimité ; insuffisance hépatique aiguë et ACLF distinguées ; absence de prévalence suisse inventée. | Recevable. |
| P4, urgence | Défaillances recherchées avant bilan ; appel 144 décrit pour hématémèse avec malaise. | Clarifier qu'une hématémèse impose une évaluation urgente même sans malaise ; ce dernier ne doit pas devenir un critère indispensable. |
| P5–7, clinique | Terrain, médicaments, déclencheurs et diagnostics concurrents couverts ; astérixis non spécifique, pas d'attribution systématique de confusion ou d'IRA à la cirrhose. | Recevable. |
| P8, confirmation | Biopsie conditionnelle, limites d'élastographie, ascite et défaillances contextualisées. | Recevable ; critique explicite de la formulation bernoise trop générale bienvenue. |
| P8, infection ascite | FMC-HGE 2026 L80 étaye neutrophiles ≥250, culture éventuellement négative ; valeur 250/mm³ diagnostique, pas posologie. | Conserver le contexte clinique : rechercher une autre cause/une péritonite secondaire si présentation évocatrice ; ce chiffre ne remplace pas l'évaluation du malade. |
| P9–10, chronologie | Bilan utile en parallèle de stabilisation ; ponction, endoscopie et imagerie organisées selon syndrome. | Préciser ponction diagnostique précoce si ascite nouvelle/aggravée ou complication, sans retard du traitement d'une infection grave. « Ponction indiquée » reste peu opérationnel. |
| P11, objectifs thérapeutiques | Classes génériques et objectifs, aucune dose ni spécialité ; filière hospitalière claire. | Préparatoire seulement : hémorragie portale sans détail vasoactif/antibioprophylaxie, ascite/encéphalopathie/infection sans choix pharmaceutiques ni adaptations. Les critères et notices exactes doivent précéder toute version thérapeutique finale. |
| P12–13, suivi | Surveillance rénale/électrolytique, nutrition, entourage, continuité et distinction amélioration/recompensation. CHUV L142 documente la périodicité semestrielle, reformulée prudemment en détection précoce. | Recevable. Pas de promesse de prévention du CHC par son seul dépistage. |
| P14, 14 réponses | Toutes concordent avec les principes du texte ; aucune dose ajoutée ni urgence inversée. | Recevable au stade préparatoire, questions non assimilées à un examen validé. |
| AIPS / Swissmedic | JSON : `notice_lue:false`, `doses_affirmees:false`. Aucun numéro Swissmedic affirmé dans le texte ou les preuves initiales. | Aucun identifiant erroné observé ; aucune exactitude d'autorisation démontrée. Complément AIPS attendu. |

La source S8 est un consensus autrichien de 2023 hébergé sur PMC : origine UE, hébergement américain, aucune validation suisse de médicament déduite de cet hébergement. Les documents sources contiennent certaines doses non importées dans la rédaction. Une relecture préparatoire sans dose ne les valide pas.


## DX.1 — première contrelecture clinique et AIPS

Les quatorze parties et quatorze questions/réponses ont été lues intégralement, ainsi que `evidence/dx1_0240.json`. Lecture ciblée des caches web DX.1, des deux extraits AIPS et des rubriques nécessaires des notices locales compressées, sans ouverture intégrale affichée du corpus. Texte audité SHA-256 : `5d59a908abdcf64ba8348b258adb6b0141e2c53c6076ad369a6de807d0706332`.

**Verdict provisoire DX.1 : base préparatoire recevable, aucune prescription chiffrée validée ; monographie thérapeutique non finale.** Les deux précisions proposées ci-dessous renforcent la chronologie et la transparence documentaire.

| Partie / domaine | Constat | Action / statut |
|---|---|---|
| P1–3 | AVC artériel adulte, ischémie/hémorragie et AIT distingués ; populations/parcours particuliers explicitement exclus ; pas d'incidence actuelle suisse inventée. | Recevable. |
| P4–5 | 144 même régression ; dernier état certainement asymptomatique distinct de découverte ; collecte des risques en parallèle du circuit urgent. | Recevable. |
| P6–9 | Examen/NIHSS, imagerie et bilan causal correctement séparés ; scanner initial normal non excluant, déficit mineur potentiellement invalidant. | Ajouter explicitement que prélèvements et ECG ne retardent pas l'imagerie. CeMIR L87 le formule directement. P10 mentionne déjà les actions parallèles. |
| P7 | Imitateurs reconnus mais aucun catalogue précis acquis. | Limite déclarée, acceptable pour préparation ; manque à traiter pour version diagnostique complète. |
| P10 | Séparation des branches hémorragique et ischémique ; éligibilité non réduite au délai ; suivi même sans reperfusion. | Recevable comme orientation. |
| P11, fenêtres | Sources suisses 2021 et HAS 2025 distinguent délai usuel, sélection tardive et thrombectomie jusqu'à 24 h dans des populations sélectionnées. | Aucun délai d'attente ni éligibilité universelle introduit. |
| P11, autorisations | A1/A2 locales confirment 4,5 h après dernier état sans symptômes et exclusion de saignement. Actilyse et Metalyse ne sont pas présentés comme interchangeables. | Attributions exactes pour les versions locales ; ajouter dans le corps du texte que notices 2025 consultées en 2026, sans actualisation réseau. |
| P11, divergences | Les exclusions et schémas ne sont pas identiques entre AIPS et recommandations ; la rédaction évite de les fusionner. | Conserver cette distinction. En particulier la notion de déficit invalidant des recommandations n'annule pas silencieusement les contre-indications libellées dans la notice Actilyse locale. |
| P11, limites thérapeutiques | Traitement hémorragique/réversion, prévention antithrombotique et complications non détaillés ; notices partiellement lues. | Pas de validation pharmaceutique exhaustive ni de monographie finale. |
| P12–13 | Réadaptation persistante après six mois, suivi 2–6 mois identifié comme repère HAS à adapter en Suisse, prévention selon mécanisme. | Concordant avec sources relues ; aucune cible chiffrée thérapeutique introduite. |
| P14 | Quatorze réponses cohérentes, sans dose ajoutée ; horaire, NIHSS et recommandations/autorisation bien distingués. | Recevable au stade préparatoire. |

### Vérification des identifiants et de la fraîcheur

| Produit | Vérification dans notice locale | Limite |
|---|---|---|
| Actilyse, 48313 | Rubrique « Numéro d’autorisation », lignes locales 500–501 : 48313 (Swissmedic) ; mise à jour L509–510 : juin 2025. Indication AVC L22 et L60 relue. SHA-256 gz `59a29647483de7cebe44fd46411648ebc4ab30470bd1465fbbe794e719b63bee`, concordant au JSON. | Lecture ciblée, pas vérification en ligne du statut actuel au 02.11.2026 ; ni interactions, ni préparation, ni gestion des complications intégralement auditées. |
| Metalyse 5000 U, 69958 | Rubrique « Numéro d’autorisation », L304–305 : 69958 (Swissmedic) ; présentation L307 : 5000 U/25 mg ; mise à jour L311–312 : mai 2025. Indication adulte L17–20 relue. SHA-256 gz `fdd3e4ccfd10d012c45a6f0e139c5ffcabf4f98c529aee78a7e8fa82afeb4f95`, concordant au JSON. | Les 5000 U désignent la présentation, pas une dose universelle ; notice comporte un schéma pondéral par tranches. Ne pas substituer automatiquement une formule issue d'une recommandation. Pas d'actualisation réseau en 2026. |

Les numéros sont bien des autorisations dans les documents locaux, non des numéros de lot ni une déduction à partir des noms de fichiers. Le dossier ne démontre pas l'absence de mise à jour réglementaire ultérieure. Aucune posologie n'est prescrite dans le texte ; les doses présentes dans les caches ne constituent pas un tableau thérapeutique validé.


## Complément DX.6 — trois notices AIPS effectivement contre-vérifiées

`evidence/DX6_AIPS_0240.json` a été lu, puis ses assertions confrontées directement aux fichiers gzip locaux correspondants dans `ressources_ia/aips/fi_fr/`. Pour les trois notices, les empreintes gzip et texte décompressé concordent avec le JSON. Les numéros y sont imprimés sous « Numéro d’autorisation » ; ils ne sont pas déduits uniquement des en-têtes du cache. Les lignes citées dans ce JSON sont comptées à partir de 1, contrairement aux indices base zéro explicités dans les preuves DX.1.

| Produit / autorisation | Concordance vérifiée | Limite clinique et documentaire |
|---|---|---|
| Duphalac / 32894 | Notice février 2023 ; indication encéphalopathie hépatique ; schéma adulte et adaptation selon selles, baisse si diarrhée ; CI citées conformes. | Discordance interne réellement présente : intolérance au lactose listée comme contre-indication, puis utilisation « avec prudence ». Ne pas gommer la CI ni en déduire une permission ; clarification de l'information professionnelle nécessaire avant un schéma autonome. Électrolytes à surveiller dans les circonstances décrites ; apport hydrique générique des laxatifs non automatiquement applicable à l'ascite. |
| Xifaxan / 63216 | Notice avril 2023 ; 550 mg, réduction des rechutes d'encéphalopathie manifeste chez cirrhotique ≥18 ans ; schéma cité et CI hypersensibilité/rifamycines et occlusion conformes. | Ne valide pas à lui seul le traitement du premier épisode aigu ; étude pivot majoritairement avec lactulose, réévaluation au-delà de six mois. Prudence insuffisances hépatique/rénale et interactions P-gp/INR ; effets cutanés graves réellement mentionnés. |
| Aldactone / 27257 | Notice août 2025 ; cirrhose avec ascite, schéma lié au rapport urinaire Na/K, maintenance minimale, CI rénales/ioniques et surveillance conformes. | Cas Na/K égal à 1 non tranché par le passage. Pas de substitution silencieuse par une titration étrangère ; surveillance spécifique d'IC sévère non transposable automatiquement à cirrhose. |

Les schémas cités dans le JSON ont été confrontés au texte source, mais ne sont pas reproduits ici comme prescription. Vérifier les passages ne signifie pas recommander leur emploi chez un patient donné ni résoudre les discordances de la notice. L'index local porte le nom `AipsDownload_20261008.xml` ; la date de modification des caches et la lecture du 02.11.2026 ne démontrent pas l'actualité en ligne. Les notices restent de 2023 ou 2025. Albumine, vasoactifs et antibioprophylaxie de l'hémorragie portale restent sans vérification suisse spécifique dans cette monographie.

## Résolution des corrections et verdict sur versions exactes

| Document | Corrections contrôlées | Décision |
|---|---|---|
| DX.1 | P6/P9 : biologie et ECG ne retardent pas l'imagerie ; P11 : notices locales 2025, lecture 2026 sans actualisation réseau. | Gel préparatoire possible ; pas de blocage médical identifié pour ce niveau. Branche hémorragique, imitateurs, antithrombotiques, complications et pharmacologie complète restent à développer. |
| DX.6 | P4 : hématémèse urgente même sans malaise ; P10 : ponction précoce si ascite nouvelle/aggravée ou complication, sans retarder le traitement d'infection grave ; P11 : vasoactif précoce et antibioprophylaxie hospitalière ajoutés, conformes à S8 L501/506/508 relues ; trois lectures AIPS tracées, aucune dose importée. | Gel préparatoire possible ; traitement reste générique et non final. Duphalac/lactose à clarifier avant publication prescriptive ; autres médicaments et indications suisses encore à documenter. |

Versions de texte contrôlées après corrections :

- `_travail/DX1_REDACTION_0240.md` : 17571 octets, SHA-256 `5d59a908abdcf64ba8348b258adb6b0141e2c53c6076ad369a6de807d0706332`.

- `_travail/DX6_REDACTION_0240.md` : 14325 octets, SHA-256 `bd7d6090a5b4431398681a391d8706a02cc7b598568e9d4855d76402ae310b32`.

Ce verdict ne valide ni un HTML futur ni des posologies prêtes à prescrire. Les lectures AIPS ont amélioré la traçabilité et confirmé les identifiants locaux ; leur fraîcheur réglementaire en ligne reste non vérifiée. Aucun score, aucune modification des textes auteurs, aucun HTML généré, aucun fichier global ou Git modifié par cet auditeur.
