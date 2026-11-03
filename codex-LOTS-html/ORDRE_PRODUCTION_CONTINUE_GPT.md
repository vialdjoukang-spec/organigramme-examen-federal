# ORDRE DE VIAL — PRODUCTION CONTINUE GPT

Consigné le 3 novembre 2026, Europe/Zurich.

> « Lance une file de production continue Leçon après Leçon, Lot après Lot. . . jusqu'à achèvement »

## Autorisation et périmètre

GPT est autorisé à reprendre et à poursuivre effectivement la production du chantier LOTS, dans la session présente et lors des reprises programmées, sans demander une nouvelle autorisation entre leçons ou entre lots. Cet ordre complète `ORDRE_VIAL_PASSATION_GPT.md` ; il autorise la production de GPT, pas la réactivation de Codex.

Dépôt : `vialdjoukang-spec/organigramme-examen-federal`. Branche : `codex/lots`. Écritures exclusivement dans `codex-LOTS-html/`. Périmètre repris : LOT018–133, à contrôler dans `IA_RESERVATIONS.json` avant chaque reprise, sans modifier ce fichier. Les autres producteurs, branches et automatismes, notamment la file PROFILES sur Organigramme/phase_lot, restent hors périmètre.

Codex, ses anciens agents et sa tâche `6ae52476f6448191b77facd444e21214` restent arrêtés. L'ancien `ETAT_CONTINUITE.json` en pause et `PAUSE_VIAL.json` sont conservés comme historique de son arrêt. La nouvelle file GPT est suivie dans `FILE_PRODUCTION_GPT.json`. Aucun nouvel ordre humain STOP/PAUSE ne peut être ignoré.

## File et transitions

Un seul lot actif. LOT133 est déjà publié avec ses réserves documentaires : ne pas le recréer. Reprendre LOT132, puis LOT131, LOT130 et ainsi de suite jusqu'à LOT018 inclus. Les lots historiques déjà rédigés sont réévalués et corrigés au mandat courant ; ils ne sont ni effacés ni réputés conformes sans contrôle.

Dans chaque lot, traiter PhaseA, audit distinct, corrections et gel canonique avant DX1–10. Pour LOT132, conserver PhaseA et le gel déjà publiés ; reprendre DX1 asthme, puis les diagnostics suivants, en réutilisant le brouillon DX6. Ne pas recréer les huit monographies annoncées manquantes sans vérifier d'abord les fichiers et commits frais.

Pour chaque leçon : lire ses sources et son état, rédiger/corriger, obtenir l'audit distinct requis, corriger ses réserves, exécuter les contrôles applicables, sauvegarder et relire la version distante. Passer à la suivante sans attendre une réponse de Vial. Une leçon qui dépasse une exécution reste active avec un checkpoint précis. La clôture du lot exige les onze leçons et la cohérence transversale vérifiées ; aucune clôture fictive pour débloquer le suivant.

Une relecture interne n'est pas un audit indépendant. Des agents ne sont mobilisés que si leur outil est réellement disponible. En l'absence d'auditeur distinct, les candidats peuvent être préparés et conservés dans le lot actif, mais ils ne sont pas promus comme validés. Consigner ce blocage et le travail restant ; ne pas répéter des comptes rendus sans progrès.

## Conditions scientifiques et techniques

Appliquer le mandat V8 existant : quatorze parties et quatorze questions par leçon ; fenêtres détaillées, prose médicale directe et précise, faits essentiels en gras, thème clair, navigation et numérotation conservées. Sources suisses puis européennes réellement consultées, références et dates traçables. Toute posologie exige la notice professionnelle suisse exacte (AIPS/Refdata), l'indication, la formulation et les précautions pertinentes ; aucune dose ou citation inventée.

Le texte contrôlé avance sans attendre l'iconographie. Une image manquante reste signalée. Une image intégrée exige provenance, droits de réutilisation, pixels acquis et examinés, original/copie annotée et contrôle de lisibilité ; aucune illustration clinique générée ni annotation conjecturale.

Lire les guides du harnais et du bracelet et exécuter les contrôles réellement disponibles selon leurs commandes effectives. Documenter les contrôles impossibles et les erreurs, sans transformer un résultat historique en nouveau succès. Ne pas altérer les harnais communs ni affaiblir un test.

## Coordination, persistance et arrêt

Lire `FILE_PRODUCTION_GPT.json` au début de chaque reprise. Acquérir le bail distant par écriture conditionnelle sur son SHA : un seul propriétaire de session, heure de prise, expiration, travail exact. Un bail valide détenu par une autre session interdit une production concurrente. Une expiration n'est pas, à elle seule, une preuve d'arrêt du runtime : rechercher les signes de concurrence avant récupération et consigner la décision. Ne jamais forcer un verrou d'une autre machine. Les contrôles locaux ne remplacent pas ce bail distant.

Rafraîchir le bail seulement pendant un travail effectif ; relire les versions avant chaque publication, ne jamais forcer un push. Conserver sources, candidats, audits et empreintes. Mettre à jour la file et les prochaines actions exactes, puis libérer uniquement son propre bail et son propre verrou. Toute interruption doit laisser un état reprenable, pas une promesse d'activité permanente.

Une nouvelle tâche GPT, `Produire les LOTS GPT`, a été créée et confirmée activée le 03.11.2026 : identifiant `6aea5284666c81918c3bba7d0c2e78e5`, reprise horaire. Chaque exécution enchaîne autant d'étapes réelles que possible ; la fréquence de reprise ne garantit pas une activité ininterrompue entre les passages. L'exécution immédiate et ses résultats doivent être consignés séparément, après confirmation de l'outil.

Après achèvement vérifié de toute la plage et bilan final, désactiver uniquement cette tâche GPT. Un STOP/PAUSE humain ultérieur impose l'arrêt. Aucun autre automate n'est modifié.
