# Relève Codex · 18.10.2026 UTC

Le projet n’est pas terminé. La porte 0 a été validée avant l’étape 1. Les passages suivants sont consignés dans ETAT.md et ETAT.json ; les travaux non achevés restent dans `en_attente`, sans fin de boucle inventée. L’étape 17 a été contrôlée puis refusée : couverture insuffisante, fusions/audits restants et accords Vial absents. Reprise courante : étape 8.

## Livraisons vérifiables

| Étape | Résultat concret | Reste dû |
|---|---|---|
| 0–2 | Catalogue/MCP/skills, porte, veille mode B, droits ; #71–#74 et sondes fusionnées ; #82 verrou des prédécesseurs fusionné, tests 5/5 + 5/5 | Maintenir les réessais |
| 3 | #43/#44/#45/#58/#47 fusionnées, critère historique satisfait | #85 G5 est un lot suivant séparé |
| 4 | #50/#53/#54 fusionnées dans cet ordre ; main à 207 monographies, shards résolus par script | #49 reprise après main ; #64 suspendue |
| 5 | #60 et #62 fusionnées, données réunies en 130 monographies dans main | Incident #62 avant #60 conservé ci-dessous |
| 6 | 98 lignes / 73 documents AIPS officiels relus ; quatre rapports `audit/AIPS-RELECTURE-PR*.json` ; comparateur sans écart et 3 tests réussis | #59 puis #61 ; #67/#70 suspendues ; références des monographies à compléter après fusion |
| 7 | #65 : 406 entrées, dix termes supplémentaires traités, baseline 3734 ; #68 : 535 entrées réunies, neuf exclusions cliniques remplacées, baseline 3571 | Sources « À vérifier » conservées ; fusions #65 puis #68 ; quatre tests du garde passent. Patch calendrier 0030 : CK UI 74/74, suite 276/276 |
| 8 | #85 : 44 DD sur quatre SSP G5 conservés, fréquences inconnues explicites ; cohortes catalane et bâloise examinées | Chiffres adaptés, autres SSP et DD manquants ; aucun chiffre transposé ni gain de couverture revendiqué |
| 9–11 | Brouillons TIP.d et inventaires hors git ; DigiFab retrouvé dans AIPS, révision 02/2026, preuve en audit/ | Rédaction de masse, audits, doses des nouvelles fiches et baseline à zéro : non réalisés |
| 12 | #83 : 72 titres critiques restaurés, aucun mot changé ; captures bureau/mobile examinées, rouge/carte 6,77:1. #84 : fermeture corrigée, 4/4 reproductions et suite 276/276 | #84 fusionnée, suite main 42a432d 276/276 ; #83 et audit médical transversal restants ; captures ciblées seulement |
| 13 | #39 fusionnée (17cf10a) ; #80 prototype VII en brouillon, Dédale-V zéro échec après svgo 4.0.0 | Croquis non validé, contrat/sources à confirmer, autres paires |
| 14 | Cinq stations pilotes présentes, `valide_par_vial=false` conservé | Relecture Vial avant toute nouvelle série |
| 15 | #41 : correctifs Galien rejoués sur main ; #81 urgences lot 3 repris en brouillon | Fusion #41 et audit clinique du lot 3 |
| 16 | #32 : 60 captures/mesures sans nouveau défaut grave, adoption de la référence CI par le script habituel sur runner, CLS 0,1347→0,0358 ; #37 : 60 DD S8 rejoués |  #32 fusionnée (617878e) après contrôles requis verts ; audit final et CI #37. #16 fermée avec motif, branche conservée |
| 17 | Pages et quatre fichiers JS identiques à main 51cb2e5 à 01:15 UTC ; jauges 38/2587 (1 %) et 207/2287 (9 %), critères 8/9 non atteints | Projet non clos ; veille conservée |

## Réserves pour Vial

- #64 : HOPE < 10 % concerne la sélection pour réchauffement extracorporel ; ce seuil ne suffit pas seul à déclarer le décès. Signalement potentiellement critique et correction proposée, non fusionnée.
- #67/#70 : l’indication historique de dexaméthasone dans l’hémorragie intracérébrale spontanée aiguë diverge de la recommandation ESO/EANS 2025. Texte AIPS verbatim conservé ; indication dérivée mise « À vérifier », attente-vial maintenue.
- KCl : l’unité officielle « mmol/l heure » reste ambiguë, aucune conversion supposée. Aciclovir : 10 jours AIPS contre au moins 14 jours EAN/ESCMID 2026, durée clinique « À vérifier ».
- Les jours 01 de publication AIPS normalisent des mois ; ils ne sont pas déclarés comme jours exacts vérifiés. Les URL officielles et empreintes des documents sont dans les rapports ; les fichiers bruts restent hors git.
- Croquis #80 et cinq stations pilotes : aucune approbation Vial reçue. Les 27 signes et les autres réserves documentaires restent à sourcer ; aucune validation clinique complète n’est revendiquée.

## Incident et limites de relance

#62 a fusionné à 23:55:43 UTC le 17.10 avant #60. Le workflow d’auto-fusion ignorait les chaînes, contrairement à la file. Codex aurait dû désactiver cette auto-fusion avant la reprise. #82, fusionnée (8dd0d0a), impose désormais tous les prédécesseurs, avec refus en cas d’erreur API ; #60 est fusionnée et les deux lots sont réunis dans main. Aucun historique réécrit, aucune protection contournée.

La CLI `codex exec -m gpt-6-luna` échoue en 401 (authentification). Le mode B écrit les ordres et la file réessaie les fusions ; il ne produit pas de nouveaux lots médicaux de façon autonome. Aucun sous-agent lancé. Les brouillons et inventaires ne sont pas des fiches complètes ; les jauges et critères ne sont pas modifiés pour les compter.

La veille locale (PID vérifié 4263) reste dans une session d’exécution de cet environnement. Le workflow GitHub de file constitue le filet distant, mais un conflit réel ou un audit manquant demande une reprise. Ne pas promettre de rédaction nocturne autonome tant que la CLI reste indisponible.

Contrôle complet local de main 42a432d : 276/276 après fusion du correctif #84. Pages contrôlé ensuite sur main 51cb2e5 à 01:15 UTC : HTTP 200 et SHA-256 identique 9e4720c6ce86056e4648eaa8744fe183479d9ddbf6419f1bb13ad60d8a800969. Les preuves sont des instantanés ; les contrôles de chaque tête de PR restent requis.

Complément de vérification : #65 passe la suite complète à 276/276 après correction des liens imbriqués dans les commandes du calendrier. Les dix termes nouveaux des monographies ont été traités sans admission en baseline ; la seule paire circulaire introduite pendant la préparation est supprimée. Le conflit réel hypertrophie de #68 a été résolu par la définition Larousse relue, avec alias et flexions réunis. Les sources provisoires restent À vérifier, sans accord Vial inventé.

La référence de #32 vient de la capture CI 39085245206, adoptée par tools/visuel_reference.sh lors de l’exécution 39085519352 (8c3e800), après examen local des écarts et mesures, puis des images CI récupérées par Git. Aucun compteur axe grave/critique n’augmente, aucun seuil de configuration n’est relevé. Les contrôles après adoption restent requis avant fusion.

#32 fusionnée à la suite de ces contrôles (617878e). La correction du calendrier et le registre de #65 sont réunis avec ce fond pâle ; captures de cette combinaison en cours.
