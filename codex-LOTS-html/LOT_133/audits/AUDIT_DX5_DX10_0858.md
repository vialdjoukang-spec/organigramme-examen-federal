# Audit indépendant DX5 / DX10 — 0858

02.11.2026 UTC. Auditeur distinct `audit_0858`. Écritures limitées à ce rapport et à la cohérence transversale attribuée. GUIDE, liste canonique et précédent audit lus ; aucune écriture auteur, Git ou registre global.

## État initial

Remises DX5/DX10 encore attendues. Aucun audit de fond ni verdict favorable n'est affirmé. Le contrôle `controler_brouillons.py` doit précéder la lecture scientifique des points 2,3,4,8,9,11,12 ; les sources effectivement lues, réserves AIPS et SHA exacts seront consignés après remise. La concordance HTML sera vérifiée après rendu. Aucun score ni validation médicale humaine.

## Verdict après remise et corrections

**DX5 et DX10 recevables pour intégration préparatoire aux empreintes ci-dessous.** Aucun score ni validation clinique ou médicale humaine. Ce verdict porte sur les passages précisés et leur traçabilité ; la concordance HTML reste à effectuer après rendu.

| Fichier | Octets | SHA-256 exact |
|---|---:|---|
| `_travail/DX5_REDACTION_0858.md` | 31449 | `6be11f09b1e7ac013d618635857607091286b77b3f6e03da2a3b15d1e045f1dd` |
| `evidence/DX5_0858.json` | 7287 | `311bdb76daf48af279ad8d8a5436e58163da26eb2a25b93d5f217c7a8ffb8889` |
| `_travail/DX10_REDACTION_0858.md` | 23378 | `8b3412fee0c59c4d681bed04021c8a8d6840d87b3cded14b3e626e4a1f7d6ce5` |
| `evidence/DX10_0858.json` | 7646 | `2de1d455bd8e5935ce3d245f2d0ba3a9cf18cd650ec505cf01ecc271081c44fc` |

Le script `controler_brouillons.py` a été exécuté avant lecture de chaque première remise, puis à nouveau sur les deux versions finales : code 0, parties 1–14 et questions 1–14. Ce résultat ne vaut pas validation scientifique. Les sept archives DX5 et dix références de cache DX10 (certaines dupliquées entre sources) ont été vérifiées par SHA : aucune discordance. Les preuves finales pointent vers les SHA Markdown contrôlés.

## Lecture indépendante réellement effectuée

Contrelecture des caches fournis, sans nouvelle acquisition réseau par cet auditeur. Les refus directs et lectures partielles des auteurs ne sont pas transformés en accès intégral. Les points 2,3,4,8,9,11,12 des deux Markdown ont été lus ; DX10 points 5,6,7 ont aussi été lus pour vérifier la continuité sémiologie–confirmation et la cohérence avec Phase A. Les questions ne sont contrôlées ici que par structure ; relecture linguistique et QCM de fond distincts.

DX5 : S1 HUG calculs, passages cliniques 81–95, définitions et appel 144 institutionnel ; S2 SNFGE facteurs, biologie, imagerie, traitement et signes d'alarme 37–75 ; S3 SNFGE cholangiocarcinome, imagerie/histologie/CA19-9 et chirurgie 55–68 ; S4 extraits ESGE2019 et recommandations principales sur extraction, bilan, drainage, prothèses, cholécystectomie et gravité ; S5 résumé officiel ESGE2018 sur drainage préopératoire/palliatif et choix de prothèses. Les détails de tableaux d'études inclus dans S4 ne sont pas assimilés à une lecture de toutes les études originales. Tokyo2018 original non lu.

DX10 : S1 Ligue suisse, lignes19–69 dont actualisation septembre2023 ; S2 La Tour texte clinique (facteurs/signes/examens/traitement/support), sans importer ses affirmations génétiques simplifiées ; S3 INCa2025 lignes250–865 sur facteurs, symptômes, diagnostic, histologie/biomarqueurs, TNM9, extension, bilan préthérapeutique et tableaux thérapeutiques ; recherche ciblée des passages neurologiques et toxicités ; S4 CEP2023 clinique/paranéoplasies, TEP, écho-endoscopie, cTNM/pTNM et opérabilité ; S5 CEP hémoptysie gravité, diagnostics différentiels, angioscanner et protection des voies aériennes, complétés par relecture ciblée des lignes240–263 ; S6 résumé Gounant2023 effectivement lu. La sortie combinée S1/S5/S6 ayant été tronquée, S1 et S6 ainsi que la fin du passage S5 ont été réextraits et lus séparément.

## Constats et corrections

| Cible | Résultat de contrelecture préparatoire |
|---|---|
| DX5 P2–3 | Migration lithiasique, facteurs et distinction stase/infection concordants ; pas de fréquence suisse inventée. Cytolyse possible en obstruction aiguë explicitement soutenue par S2. Cholestase non assimilée à infection ou localisation. |
| DX5 P4 | Triade incomplète, défaillances et contrôle de source priorisés. Demande précise : expliciter appel 144 hors hôpital devant défaillance ; correction relue, identifiée comme adaptation suisse. Délai de 12 h ESGE en choc cité comme repère ancien, pas comme attente autorisée. |
| DX5 P8–9 | Biologie et imagerie concordantes, écho initiale puis IRM/écho-endoscopie si suspicion persistante chez stable ; CPRE thérapeutique, pas examen automatique. CA19-9 non probant isolément ; prélèvement négatif ne clôt pas une suspicion tumorale. |
| DX5 P11 | Drainage/antibiothérapie distingués ; modalités grave/modéré/léger attribuées ESGE2019 et contextualisées. Alternative si CPRE impossible, extraction selon aptitude, cholécystectomie après CPRE et organisation HUG non universalisée. Drainage préopératoire malin non systématique ; prothèse non couverte évitée en étiologie extra-hépatique indéterminée. |
| DX5 P12 | Suivi de réponse et rendez-vous prothèse explicites. Retrait/échange 3–6 mois limité à prothèse plastique après extraction incomplète de calculs ; ne devient pas calendrier universel. |
| DX10 P2–3 | Risques tabac/expositions et non-fumeur ; symptômes/complications cohérents avec S1–S4. Aucun délai de toux transformé en attente devant hémoptysie. Dépistage français distinct du diagnostic et non transposé. |
| DX10 P4 | Hémoptysie : menace asphyxique, poumon saignant déclive si identifié, angioscanner et contrôle spécialisé sans attendre biopsie. Demande précise d'appel 144 : correction relue, numéro suisse séparé du CEP français. Syndrome cave/obstacle central et complications neurologiques orientés en urgence, sans protocole empirique uniforme. |
| DX10 P5–7 complément | Hippocratisme non spécifique, signes paranéoplasiques distincts de métastases ; scanner initial puis prélèvement du site pertinent, cytologie possible, matériel moléculaire préservé. Concordance avec la confirmation anatomopathologique annoncée en Phase A. |
| DX10 P8–9 | TEP et IRM cérébrale distinctes, ganglion hypermétabolique non preuve histologique ; cTNM/pTNM séparés. TNM9 INCa2025 explicitement distinguée du CEP2023 ; biomarqueurs exemples non panel exhaustif, opérabilité distincte de résécabilité. |
| DX10 P11–12 | Stratégies CBNPC par résécabilité/stade/terrain/biologie et CBPC rapide avec chirurgie exceptionnelle. Pas de protocole unique de stadeIII, ni irradiation prophylactique cérébrale universelle ; limites d'actualisation explicites. |

## Réserves maintenues

Aucune dose médicamenteuse proposée dans ces deux rédactions ; aucune notice AIPS exacte lue par cet auditeur pour ces deux nouveaux DX. Les classes thérapeutiques et réserves de prescription ne constituent pas une validation pharmaceutique. Les doses de tableaux étrangers présents dans les caches ne sont pas importées.

DX5 : ESGE2018/2019 anciens, lectures par extraits/résumé ; absence de remplacement récent non démontrée, Tokyo original non consulté, sources SNFGE grand public sans date éditoriale établie. Le rapport autorise une intégration préparatoire avec ces limites visibles, pas une procédure interventionnelle actuelle exhaustive.

DX10 : INCa2025 français et CEP2023 ne démontrent pas l'exhaustivité thérapeutique en novembre2026 ni les autorisations suisses. S6 est un résumé décrivant des thèmes et principes, insuffisant pour justifier un protocole détaillé de syndrome cave/obstruction centrale. Les orientations neurologiques et métaboliques restent des synthèses de triage sans schéma médicamenteux. Pas de revalidation de panel moléculaire complet ni de traitement de consolidation récent. Les statistiques et généralisations génétiques de La Tour ne sont pas reprises. Aucune lecture intégrale des longues bibliographies revendiquée.

## Concordance HTML finale ciblée

Extraction effective par `harness/cache_controles.py extraire` : DX5 P4,9,11,12 ; DX10 P4,7,8,9,11,12, fenêtres liées incluses. Lecture DOM ciblée des cinq/six notices sources et de leurs liens externes. Aucun HTML complet affiché, aucun test navigateur réalisé par cet auditeur. Root rapporte 19 contrôles statiques et quatre configurations Chromium par nouveau DX, puis 190 contrôles sur les dix monographies ; ces contrôles restent attribués à root.

| HTML final | Octets | SHA-256 exact |
|---|---:|---|
| `LOT_133_Phase_B_V0_DX.5.html` | 104650 | `b022f2e3e478f506c195011a6658144539f169951509ca1731e3ac32d5aced73` |
| `LOT_133_Phase_B_V0_DX.10.html` | 94776 | `b382697cad749cefba4094920879fbd4c0efbe97c5e2296c7ded669bb1ea755a` |

Le rendu conserve les deux corrections d'appel144, la chronologie sans attente de l'urgence, les délais ESGE contextualisés et le suivi ciblé des prothèses. DX10 conserve confirmation anatomopathologique, distinction TEP/IRM, TNM9, limites des biomarqueurs et traitements CBNPC/CBPC sans dose.

Défaut documentaire détecté puis corrigé centralement : le rendu initial DX5 ignorait `date_source`. Après correction, lecture DOM renouvelée : HUG26.02.2025, ESGE2019 et ESGE2018/actualisation2017 sont visibles avec date de consultation distincte. SNFGE S2/S3 n'ont pas de date éditoriale établie ; aucune date n'est fabriquée (ce manque est explicite dans le Markdown/evidence). Les limitations d'extraits, résumé et ancienneté demeurent visibles. DX10 conserve publication/consultation et les limites de ses six références, dont S6 résumé seulement.

**Verdict final de cette mission : concordance ciblée recevable pour intégration préparatoire aux SHA HTML précités ; aucun blocage supplémentaire identifié dans ce périmètre.** Les limites scientifiques, documentaires et d'actualisation ci-dessus persistent. Ni score, ni validation médicale humaine, ni vérification de publication, ni audit exhaustif des quatorze parties.
