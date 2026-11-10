# Arrêt Codex et passation ouverte à toute IA

## Autorisation de Vial

Le 10 novembre 2026, Vial demande : « STOP TOUT », puis autorise n’importe quelle IA à reprendre le travail, le terminer et l’auditer.

La production Codex est arrêtée. Tous les contenus de `ChatGPT_Codex/`, y compris sources, brouillons, scripts, audits et leçons, sont ouverts à la reprise par toute IA. Toute réservation ou exclusivité Codex est levée. Toute IA peut les lire, copier, corriger, compléter, réorganiser et auditer sans demander l’accord de Codex. Cette autorisation porte sur le travail confié par Vial ; elle ne change pas les licences des sources tierces ni les droits techniques du dépôt.

## Références et exigences conservées

La référence rédactionnelle est `PROMPT_Casern/PROMPT_LOTS_Lo_9.11.26.claude.md`, avec `outils/` sur main, ou la branche `reference/prompts-9.11.26` si nécessaire. Intervalle confié : LOT080 à LOT102, onze leçons par LOT. Images et perfectionnement étaient différés.

Les leçons exigent des sources effectivement lues, des doses vérifiées dans l’AIPS et une contrelecture indépendante du rédacteur. Respecter la chaîne M5 et ses portes ; ne pas compter la présence d’un HTML comme une validation clinique. Conserver les refus historiques. Aucun force-push ni suppression de branche.

## État vérifié lors de la passation

- Consolidation de 858 leçons existantes effectuée précédemment, PR516 fusionnée ; ce nombre est distinct de la production nouvelle.
- LOT080 : onze leçons poussées historiquement ; DX5 et DX6 refusées après deux P3. LOT non livré. Branche historique `codex/lot-080` ; ne pas effacer ces verdicts ni présumer leur résolution.
- LOT081 : onze leçons livrées, PR567 fusionnée.
- LOT082 : onze leçons livrées, PR599 fusionnée.
- LOT083 : onze leçons livrées, PR602 fusionnée le 10 novembre 2026 à 14:37:18 UTC, commit de fusion `5348ddbc313780ff343cdeed86c7986c5a7b444a`. Les onze fichiers ont été confrontés au manifeste dans le checkout de main lors de cette passation.
- Bilan : trois LOTs livrés sur vingt-trois ; quarante-quatre nouvelles leçons poussées historiquement, dont onze du LOT080 refusé. Aucun achèvement global n’est déclaré.
- Progression d’équipe à midi : PR600 créée précédemment. Son état actuel n’est pas vérifié dans cette passation.
- LOT084 : préparation et P1 indépendamment franchie dans l’ancien environnement ; aucun HTML contrôlé ou poussé attesté. Le checkout actuel de main ne contient pas son dossier. La branche distante `codex/lot-084` existe mais ne prouve pas la sauvegarde des préparations récentes.
- LOT085–102 : aucune production livrée par cette session attestée.

## LOT084 : récupération nécessaire avant reprise

L’ancien environnement s’est déconnecté pendant la rédaction. Les écritures non confirmées et les manuscrits conservés seulement en mémoire d’agent ne doivent pas être considérés comme présents dans Git. Examiner les caches disponibles et les branches avant de refaire ou remplacer un fichier. Ne pas annoncer de récupération sans vérifier les octets.

Liste gelée dans l’ancien environnement : 1 Crampes nocturnes idiopathiques ; 2 Syndrome du canal carpien ; 3 Polyneuropathie diabétique distale symétrique ; 4 Radiculopathie lombo-sacrée L5 ou S1 sur hernie discale lombaire ; 5 Syndrome des jambes sans repos ; 6 Sténose canalaire lombaire dégénérative symptomatique ; 7 Artériopathie oblitérante des membres inférieurs avec claudication intermittente ; 8 Phénomène de Raynaud primaire ; 9 Thrombose veineuse profonde aiguë du membre inférieur ; 10 Ischémie artérielle aiguë de membre.

Cette liste décrit un ordre contextuel de présentation, pas dix prévalences comparables. Son JSON avait pour SHA256 `48f416b8b0bbdfa904a1c2a14c389ab4f28234b6c29f4da7737fba3d1f22d7bc`. L’attestation P1 finale avait pour SHA256 `2ed009012e1942f3b76a51ae9d03b807b9f361980817388ad6dc7efa54baaccc`. Vérifier les fichiers originaux ; ces indications de passation ne remplacent pas leurs preuves.

Phase A : points1–8 enregistrés dans l’ancien espace ; tentative des points10/13/14 sans confirmation. DX : paquets et contrats préparés, rédactions à divers stades ; aucun assemblage ou P3 final attesté. Les manuscrits DX3 et DX8 étaient conservés dans la mémoire privée de l’agent `sources_lot080`, sous `lot084_fichiers_a_materialiser` ; cette mémoire n’est pas une sauvegarde partagée garantie.

## Première intervention de l’IA repreneuse

Lire cette passation, inventorier ce qui existe réellement sur main, les branches et les éventuels caches restaurés, puis distinguer livré, refusé, brouillon et manquant. Reprendre ensuite la finalisation et l’audit demandés par Vial sur cette base, sans exclusivité Codex et sans transformer un ancien statut en validation nouvelle.

Le script de lecture et `AGENTS.md` rendent l’instruction explicite aux repreneurs. Ils ne prétendent pas imposer un verrou technique à toutes les IA ni modifier les protections GitHub.
