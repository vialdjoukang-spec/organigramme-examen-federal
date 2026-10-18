# Contre-audit indépendant · veille et contrat chronologique

Verdict : favorable sur les changements non committés examinés dans oef-g1-lot2. Pas de nouveau défaut technique bloquant constaté. Rapport technique uniquement : aucune validation clinique humaine, mutation de code/app/données/veille, capture, relance distante, adoption ou fusion par la sentinelle.

## Refus de clôture prématurée

complete exige la mission exclusive infobulles_prototype6 et un contrat explicite de version entière2, six rubriques entières et chronologie_obligatoire exactement true. Les huit compteurs de structure/relecture prototype et chronologie doivent chacun égaler les totaux correspondants, positifs et entiers stricts. Un flottant, booléen, champ absent, ancien contrat ou manque de preuve chronologique ne suffit pas. Doublons, SSP sans DD et anomalies empêchent également la fin. Aucun ancien nombre de monographies legacy ni arrondi ne termine la mission.

Les quatre compteurs chronologiques sont des alias explicites des compteurs de prototypes désormais exigeants : prototype_ready impose les champs du prototype, chronologie_ready et les drapeaux stricts. La revue requiert le marqueur chronologie_relue exactement true, validation_clinique exactement false, la date valide, les sources du registre, l’empreinte actuelle complète de la fiche et celle du rapport présent. Une mention libre ou une ancienne attestation sans ces éléments ne suffit pas.

Calcul local réellement exécuté sur les fichiers présents et le registre actuel :14/2287 diagnostics structurés et relus avec chronologie ;1/248 SSP structuré et relu avec chronologie. Égalité des alias vérifiée. complete retourne false : ni ces14fiches ni le SSPG1 ne sont assimilés à la fin de tous les SSP/DD.

## Boucle, baux et état

La boucle conserve les passages nominaux0/120/240s, les attentes fractionnées de25s, le verrou local et le groupe GitHub garde-progres. Les captures de main restent isolées du checkout interactif, puis supprimées en finally. report_for relit le runtime existant par chemin explicite ; il ne fabrique pas un runtime vide dans chaque instantané et ne recopie pas la branche d’état à chaque passage.

Le bail du worker est borné à180s et sa libération est tentée en finally, y compris après un timeout. Après les lectures coûteuses, l’état est relu pour préserver une déclaration d’activité d’agent arrivée entre-temps. Les écritures conservent le compare-and-swap local/distant : un conflit est refusé, pas écrasé. Les baux non finis ou booléens ne sont pas interprétés comme une activité valide. Un bail de demande est toujours distinct d’un agent effectivement déclaré et ne prouve pas son exécution.

Les erreurs réseau, états inconnus, CI active ou activité connue empêchent la nouvelle sollicitation. Le gating OEF_GARDE_RELANCE_PERMISE reste présent dans progres.py pour les relances et appels ; le cherry-pick des compteurs ne l’a pas retiré. Le nouveau texte de relance conserve la mission exclusive et demande maintenant bilan numéroté, phases de prise en charge et simultanéités explicites. Pas de dispatch de recherches transversales ajouté.

Une fenêtre terminée ou interrompue demeure un arrêt technique de cette fenêtre ; seul le contrat complet termine la tâche. Un arrêt demandé par configuration/STOP reste respecté. L’ordre des étapes n’est pas avancé automatiquement par les nouveaux compteurs.

## Vérifications exécutées

-11tests de permanence,8tests de coordination crise et6tests de jauges chronologiques :25réussis.
-37contre-tests indépendants de contrat/types/totaux/anomalies : tous les faux achèvements rejetés.
-Calcul réel de coordination en mémoire avec registre actuel ; compteurs et refus de clôture contrôlés sans écrire les jauges canoniques.
-git diff --check réussi.

## Exécution hébergée et limite de portée

L’intégrateur a fourni la preuve d’une fenêtre hébergée réussie sur run39174886621, job117815407544, avec passages23:03:50,23:05:46 et23:07:47UTC. Ce rapport ne réattribue pas cette exécution antérieure aux changements encore non committés contrôlés ici. Ces changements demandent leur propre CI et leur publication. Le bail manuel180s de root est une déclaration d’activité connue, pas une preuve d’IA permanente.

Le cron GitHub de déclenchement demeure5min ; les passages internes sont espacés nominalement de120s. La programmation, les passages effectivement constatés et une exécution d’agent sont trois faits distincts. La cadence peut subir des retards de runner, et aucun réveil automatique d’une session ChatGPT fermée n’est garanti.

## Empreintes de l’état examiné

- tools/garde/permanence.py : `7c3ada02c9ba6154dd6a9d9dfe95c5acd4564a7d3769028c2fe545dd9dfa37a8`
- tools/garde/progres.py : `808d7376e8cd4342cd6ba72a18efc2267d0e0790f990a084fce08bb0278096c3`
- tools/coordination/calculer.py : `b66d2a94ec0eab99a0a763fa45f2f42c9b9ce4c409b106b2a661a543412e6208`
- tools/garde/commun.py : `688046984f62d6713eceb12a3cde7291dc4513222126af1a39fbb2e2bdaa2703`
- tests/test_garde_permanence.py : `aea5164eaf830c5c399e5ee95c27e8a321f44b0638cd9aa03302e6b89ac8e747`


## Supplément de contre-audit · fenêtre de vingt minutes · tête734c326

Verdict favorable sur l’extension bornée : valeur par défaut CLI et configuration1200s, commande du workflow1200s et timeout runner30minutes. Le groupe garde-progres et cancel-in-progress=false restent inchangés : aucune nouvelle famille de workers ni lancement d’IA ajouté. Le bail indépendant du worker demeure180s et sa libération/nettoyage reste dans finally. Le seuil de30stalls avec fenêtre de2minutes conserve un délai nominal d’environ60minutes avant appel de Vial, sans promettre un horaire exact.

Vérifications exécutées :12tests de permanence réussis, dont onze passages simulés à0,120,…,1200s ; contre-test indépendant avec refresh-main simulé : onze instantanés temporaires tous supprimés, bail worker libéré et complet=false à la fin de la fenêtre ; git diff --check réussi. Aucun code ni autre fichier du dépôt modifié par la sentinelle.

Cette extension réduit les périodes dépendant d’un nouveau déclenchement cron entre des fenêtres de quatre minutes. Elle ne garantit pas qu’un runner restera disponible ni une transition immédiate entre fenêtres : le déclencheur demeure cinq minutes et peut être retardé. La preuve hébergée des trois passages antérieurs ne prouve pas encore une exécution des onze passages du nouveau code. Les déclarations d’agent doivent provenir de son responsable réellement actif ; le simple observateur n’en renouvelle pas artificiellement le bail.
