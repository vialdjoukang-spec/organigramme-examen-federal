# Relève Codex · 18.10.2026 UTC

Le projet n’est pas terminé. La porte 0 a été validée avant l’étape 1. Les passages suivants sont consignés dans ETAT.md et ETAT.json ; les travaux non achevés restent dans `en_attente`, sans fin de boucle inventée. L’étape 17 a été contrôlée puis refusée : couverture insuffisante, fusions/audits restants et accords Vial absents. Reprise courante : étape 8.

## Livraisons vérifiables

| Étape | Résultat concret | Reste dû |
|---|---|---|
| 0–2 | Catalogue/MCP/skills, porte, veille mode B, droits ; #71–#74 et sondes fusionnées ; #82 verrou des prédécesseurs fusionné, tests 5/5 + 5/5 | Maintenir les réessais |
| 3 | #43/#44/#45/#58/#47 fusionnées, critère historique satisfait | #85 G5 est un lot suivant séparé |
| 4 | #50/#53/#54 fusionnées dans cet ordre ; main à 207 monographies, shards résolus par script | #49 fusionnée ; #64 suspendue |
| 5 | #60 et #62 fusionnées, données réunies en 130 monographies dans main | Incident #62 avant #60 conservé ci-dessous |
| 6 | 98 lignes / 73 documents AIPS officiels relus ; quatre rapports `audit/AIPS-RELECTURE-PR*.json` ; comparateur sans écart et 3 tests réussis | #59 et #61 fusionnées ; #67/#70 suspendues ; références des monographies à compléter après fusion |
| 7 | #65 fusionnée : 414 entrées, baseline 3730 ; #68 : 543 entrées réunies, neuf exclusions cliniques remplacées, baseline 3567 | Sources « À vérifier » conservées ; fusion #68 après contrôles des cibles 24 px ; quatre tests du garde. Patches 0030/0031 : suite 278/278, référence conservée |
| 8 | #85 : 44 DD sur quatre SSP G5 conservés, fréquences inconnues explicites ; cohortes catalane et bâloise examinées | Chiffres adaptés, autres SSP et DD manquants ; aucun chiffre transposé ni gain de couverture revendiqué |
| 9–11 | Brouillons TIP.d et inventaires hors git ; DigiFab retrouvé dans AIPS, révision 02/2026, preuve en audit/ | Rédaction de masse, audits, doses des nouvelles fiches et baseline à zéro : non réalisés |
| 12 | #83 : 72 titres critiques restaurés, aucun mot changé ; captures bureau/mobile examinées, rouge/carte 6,77:1. #84 : fermeture corrigée, 4/4 reproductions et suite 276/276 | #84 fusionnée, suite main 42a432d 276/276 ; #83 et audit médical transversal restants ; inventaire explicite disponible |
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

Complément de relecture : la définition de cardioverter introduite dans #65 décrivait un appareil alors que la monographie emploie un verbe. Cette faute majeure est corrigée séparément par une définition relue au CHUV ; le journal des fautes identifie le commit et la source. La conduite de l’arythmie elle-même présente une ambiguïté potentiellement critique (bloc de haut degré inclus, consigne générale de cardioversion) : #88 porte une proposition distincte, attente-vial, avec ESC 2022 et protocole HUG 2024 relus. Aucun nouveau médicament ni dose, aucune fusion sans accord.

Après #65, le contrôle de #68 trouve deux cibles trop petites supplémentaires dans Notions. La correction à 24 px supprime les six défauts sur la reproduction bureau ; les autres thèmes/mobile et la référence restent à vérifier. Aucun compteur d’accessibilité ne doit être augmenté pour masquer ce défaut.

Inventaire : audit/RESTE_A_VERIFIER_20261018.json conserve SHA et pointeur pour chaque champ explicitement marqué. À main 33bb1d0 : 577 champs et 605 occurrences. Les branches non fusionnées, la validité médicale et les erreurs sans marque sont hors de ce décompte.

## Mise à jour après #68 et #85 · 18.10.2026 02:25 UTC

#68 est fusionnée (f2f9c04), après les contrôles requis verts et 278 tests réussis. Les six combinaisons thème/profil de Notions n’ont plus de défaut de taille de cible. Les défauts d’accessibilité hérités ne sont pas déclarés résolus. Référence CI adoptée après examen (source 39088253572, adoption 39088687562) ; le refus HTML intermédiaire a été corrigé sans relâcher sa référence.

#85 est fusionnée (27c9658) : 44 DD G5, inconnues explicites conservées. Prévalences 38/2587 (1 %), monographies 207/2287 (9 %), aucun gain quantitatif inventé. Pages : application et quatre JS contrôlés identiques à cet instantané à 02:23 UTC. Inventaire : 751 champs, 779 marques explicites, 24 fichiers ; les ajouts provisoires et inconnues expliquent l’augmentation, pas un nouvel audit exhaustif.

La relecture des propositions de skills confirme les procédures existantes ; inventaire ajouté à ssp-verite, adoption runner à ssp-qualite-visuelle. Étape 7 désormais validée par porte.py ; critères 8 et 9 refusés à juste titre. #83 et #41 continuent leur intégration ; état définitif à compléter ci-dessous après les contrôles.

#83 fusionnée (3e796d5) à 02:25:55 UTC après tous les contrôles verts. #41 : la reprise depuis ce main vérifie 17 remplacements sur 16 fiches, TIP.d et code hors TIP inchangés ; le refus non-fast-forward a été résolu par fetch et réunion de la branche distante, sans force. Nouvelle tête 35d25e0, CI relancée. Le nombre de remplacements ne correspond pas au nombre de fiches car l’une en reçoit deux.

Précision R8 : le modèle courant sert de secours dans la session interactive. Le refus 401 concerne la relance CLI autonome ; il ne rend pas impossible la rédaction interactive. Les tâches de contenu non faites restent explicitement dues. Lot G5 terminé par #85 ; reprise étape 8, lot 3, S7.6 puis S2.12, S8 après audit #37. Extraction du texte existant hors git préparée, sans ajout de fréquence ni monographie.

Actualisation 2026-10-18T02:30:26.096088+00:00 : #41 fusionnée (5de965f) après #83, contrôles requis verts et 278 tests. #81 reste en audit. Les corrections cliniques R13 #64/#67/#70/#88 restent en attente de Vial. La clôture reste refusée ; reprise à l’étape 8, lot 3.
