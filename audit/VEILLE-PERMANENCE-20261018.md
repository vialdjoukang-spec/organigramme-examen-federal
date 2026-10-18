# Contre-audit indépendant de la veille de permanence

Verdict final : **favorable pour le périmètre technique actuel**, après les correctifs relus ci-dessous. Aucun défaut bloquant restant identifié. Cette conclusion concerne la mesure et les demandes de reprise ; elle ne certifie ni l’exécution d’un agent IA, ni une cadence distante garantie, ni une validation médicale humaine.

## Corrections confirmées

1. La clôture exige des compteurs entiers exacts pour tous les SSP et tous les diagnostics, sans SSP dépourvu de différentiel, doublons ou anomalies. Une régression révoque l’ancien verdict ; une ancienne monographie structurée ne vaut pas une relecture actuelle.
2. Le calculateur de l’instantané reçoit désormais explicitement le chemin runtime de la racine via `--state-dir`. Il ne fabrique plus quatre états absents du seul fait de l’archive neuve. Le test ciblé contrôle ce chemin.
3. Le bail de demande dure 120 secondes. Il est distinct du bail d’un agent dont une activité réelle a été déclarée ; sa présence ne compte pas comme preuve d’exécution.
4. Le bail du worker dure 180 secondes et est renouvelé à chaque passage. Sa libération est tentée dans un `finally`, y compris après un timeout du calculateur ; le test confirme l’absence de bail résiduel. Un arrêt brutal empêchant ce traitement laisse le bail expirer ; le prochain lancement peut reprendre ensuite.
5. L’état est relu après les lectures potentiellement longues. Un acquittement d’agent arrivé entretemps est ainsi conservé. Le propriétaire worker est vérifié, puis l’écriture CAS protège la réservation avant toute notification.
6. Les baux refusent booléens, NaN et infini comme dates d’expiration. Les instantanés retournés par `snapshot()` sont supprimés dans un `finally`, y compris si le calcul échoue.
7. Sans notification, le journal de la nouvelle version porte `observation_sans_notification`. Le libellé antérieur « occupe » ne prouvait pas une activité d’agent et n’est pas interprété ainsi.

## Protections et limites de portée

- Le cron GitHub reste `*/5 * * * *`, avec échéances internes à 0, 120 et 240 secondes. Le groupe de concurrence sérialise les fenêtres, les attentes sont fractionnées à 25 secondes. Les retards GitHub, réseau ou de commande peuvent espacer les passages ; aucune garantie globale de deux minutes n’est déduite du YAML.
- Chaque passage actualisé relit main, la configuration et la mission ; le checkout interactif n’est pas réinitialisé. STOP local est contrôlé pendant les attentes, et `permanence_enabled:false` est respecté au passage suivant. Une fenêtre terminée ne vaut pas mission terminée.
- CAS local par empreinte et remplacement atomique ; CAS distant par SHA Contents. Une activité distante inconnue bloque la demande. Le garde ne notifie qu’avec une autorisation d’exécution explicite transmise par le contrôleur.
- Aucun lancement direct d’IA ou de recherche transversale dans ce worker. Une CI, un processus détecté ou un bail déclaré sont des protections contre les doublons, sans preuve automatique de travail utile.
- Les tests amont vérifient que modifier une fiche ou son rapport révoque l’attestation liée aux empreintes. Une structure mécanique sans relecture demeure dans la file. La couverture documentaire mesurée ne certifie pas le rendu, les termes cliquables, un classement inconnu ou la qualité clinique.

## Tests réellement exécutés

Commande : `python3 -B -m unittest tests.test_garde_permanence tests.test_prevalences_coordination tests.test_coordination_crise tests.test_mono_prototype -v`.

**37 tests réussis** : permanence 10, coordination 11, crise/prototype 16. Les contrôles couvrent complétude exacte, régression, SSP sans DD, refus des faux baux non finis, CAS local et propriétaires concurrents, STOP, échéances simulées, chemin runtime, timeout libérant le bail et invalidation des preuves actuelles.

Aucun test de mutation CAS sur GitHub, aucune mention externe et aucun démarrage d’agent effectués par cet audit. Aucun script partagé, fichier canonique ou application modifié par l’auditeur.

## Observation locale réellement lue

Journal `.etat_local/permanence/worker.log`, ancienne version : passages à **22:45:31, 22:47:31 et 22:49:31 UTC** le 18.10.2026, soit deux intervalles observés de 120 secondes. Événement `stop_demande` à **22:50:21 UTC**. Le libellé « occupe » de ces passages était produit par l’observation sans notification ; il ne démontre pas un agent actif. Ces observations ne prouvent pas le fonctionnement distant de la nouvelle version.

## Réserves non bloquantes et suivi requis

- `busy_now()` lit au maximum 100 PR et 100 runs. Une pagination ou une interrogation ciblée des statuts actifs devra précéder toute affirmation de couverture exhaustive dans un dépôt dépassant ce volume.
- Si `snapshot()` échoue avant de retourner son répertoire, son nettoyage interne reste à durcir ; le `finally` du worker ne connaît pas encore ce chemin. Le nettoyage du chemin retourné est corrigé.
- Les futurs compteurs chronologiques ne sont pas encore présents dans ce périmètre. Dès leur intégration, **le critère de clôture et les tests doivent les inclure** ; cet avis ne vaut pas validation d’une clôture qui les ignorerait.
- Les accords Vial déjà enregistrés ne sont pas soumis à une nouvelle confirmation par cet audit. Ce rapport n’autorise aucune fusion sans les contrôles requis du dépôt.

## Empreintes finales relues

Date de cette passe : 2026-10-18T22:51:28+00:00.

- `tools/garde/permanence.py` : `14d6815688b046905c0bed75acd16ec5d7103e6fb57b53957c7ca5695e5f6b79`
- `.github/workflows/garde-progres.yml` : `61862bbdb26ca51b178ab8eca2a605df2b157c9e5c876f6bd7ce68d1515bba18`
- `tools/garde/config.json` : `682dc8d4d47fcb1d6de24d500012e8113410c7e9f1397a4ad0379bed7fecfd06`
- `tools/coordination/config.json` : `5e8db4652a760cce23c771c05622878a4969ccff92817c64ebc987f1388c153b`
- `tools/garde/progres.py` : `120cdb5ee704944fb2bf1ce01a28345fca539fde6912ac3cc6532e2dc9f0eaa4`
- `tests/test_garde_permanence.py` : `d98b34b1ede3ffefc7f8bb577355f301391bb30cd4be898c94cbce23564a19fc`
- `docs/VEILLE_PERMANENCE.md` : `cb93f9d94398c565c4a4bff4715bf9b7e556b3056ef524e4ecfd4d30922894ed`
