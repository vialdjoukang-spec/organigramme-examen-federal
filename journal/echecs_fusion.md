# Échecs de fusion-publication (tools/file_fusion.sh)

Une ligne par échec nouveau. Le travail continue toujours ; Codex traite ces lignes à l’étape 2 ou dans l’étape de la chaîne.

- 2026-10-17 23:04 UTC · #49 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-17 23:04 UTC · #50 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-17 23:04 UTC · #60 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-17 23:04 UTC · #59 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-17 23:04 UTC · #65 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)

- 18.10.2026 · Étape 0 · Lecture de protection main via l'intégration refusée (HTTP 403). Droits de dépôt admin/push/merge_commit/auto_merge confirmés. Protection conservée ; ne pas considérer le JSON d'erreur comme une liste de checks.
- 18.10.2026 · Étape 0 · Codex CLI installé mais test gpt-6-luna refusé pour authentification. Mode B retenu ; aucun renouvellement de connexion interactif demandé.

- 18.10.2026 01:07 CEST · Étape 2 · Lecture des secrets Actions refusée (403) ; gh opérationnel, auto-fusion #71 a réussi à activer MERGE. Aucune intervention interactive ni nouveau secret. Réparation du repli 403 et du réessai Pages livrée séparément.
- 2026-10-17 23:11 UTC · #44 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-17 23:12 UTC · #60 · contrôle requis garde en échec
- 2026-10-17 23:15 UTC · #44 · contrôle requis visuel en échec

- 18.10.2026 · Étape 3 · #44/#45/#58 : conflits dans app_v2 et prev.js ; app repris de main, correctifs audités rejoués, assets régénérés. Les fusions restent en attente des suites et de la CI, sans forçage. Poursuite Étape 4 selon R7, reprise par la file.
- 18.10.2026 · Tests locaux initiaux : Playwright 1.62 différent du 1.63 figé dans la CI ; échecs d'interaction de fermeture/panneau calendrier constatés. Venv 1.63 et Chromium 1243 installés, aucune assertion abaissée.

- 18.10.2026 · Étape 4 · Reprises des cinq PR effectuées ; fusions en attente de CI et d'ordre des labels. #64 suspendue par attente-vial (HOPE et constat de décès), pas d'audit-ok ; la file poursuit les autres chaînes.
- 2026-10-17 23:50 UTC · #75 · gh pr merge refusé (protection, tête changée ou droits)
- 2026-10-18 00:06 UTC · #45 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-18 00:07 UTC · #41 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)

- 18.10.2026 UTC · Incident #62 : fusion automatique à 23:55:43 UTC avant #60, causée par le workflow qui ignorait les prédécesseurs. Audit-ok de #61 retiré temporairement ; #82 ajoute le verrou de chaîne. #60 doit encore réunir ses données avec main ; aucune fusion annulée ni protection contournée.
- 2026-10-18 00:29 UTC · #32 · contrôle requis visuel en échec
- 2026-10-18 00:47 UTC · #83 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-18 00:57 UTC · #65 · contrôle requis tests en échec

- 18.10.2026 UTC · #83 : push non-fast-forward refusé car le bot avait avancé la branche ; fetch, réunion des commits distants, diff --check et push sans force réussis (0b86173).
- 18.10.2026 UTC · #32 : téléchargement local des deux artefacts refusé 403. Repli exécuté par le même script sur runner, SHA/branche/base vérifiés ; adoption et relance des contrôles sans contournement de protection.
- 2026-10-18 01:16 UTC · #32 · gh pr merge refusé (protection, tête changée ou droits)
- 2026-10-18 01:23 UTC · #65 · contrôle requis visuel en échec
- 2026-10-18 01:27 UTC · #61 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-18 01:27 UTC · #85 · conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)
- 2026-10-18 01:45 UTC · #68 · contrôle requis visuel en échec
- 2026-10-18 01:56 UTC · #68 · contrôle requis html en échec

- 18.10.2026 UTC · #68 : garde, tests 278 et visuel verts après adoption, contrôle HTML rouge pour deux règles nouvelles dans un style hérité du corps. Patch corrigé en portant les mêmes dimensions sur les éléments créés ; référence HTML inchangée, nouvelle CI demandée.

- 18.10.2026 02:19 UTC · #83 : liens en échec par quatre délais revmed.ch, sans erreur HTTP invalide. Reprise de main après #85, contrôle relancé vert ; aucune exclusion ni règle affaiblie.

- 18.10.2026 02:26 UTC · #41 : push non-fast-forward refusé, mises à jour automatiques de main déjà distantes. Fetch et réunion sans conflit, sans force ; builders/Lyncée repassés, push 35d25e0 réussi. CI relancée avant fusion.

- 18.10.2026 UTC · Étape 8 lot 3 : miroir PDF BORIS inaccessible (HTTP 503 et refus Anubis par le lecteur web). Texte primaire PLOS accessible et lu ; aucun accès au miroir prétendu, aucun contournement tenté.

- 18.10.2026, Europe/Zurich · chaîne #88→#64→#91→#67→#70 : accord de Vial lu sur les pages publiques. API api.github.com refusée par le proxy (HTTP 403 CONNECT), malgré GH_TOKEN présent et lecture Git fonctionnelle. Sources HUG/DOI également refusées. Domaines nécessaires ajoutés au brouillon des paramètres, sans prétendre leur application. Relecture et CI exactes non vérifiables ; aucune fusion hors ordre.

- 18.10.2026, Europe/Zurich · Reprise : GitHub/API et sources HUG/EDF/AIPS accessibles sur les URL testées. Oxford accueil 403, recherche Europe PMC expirée ; aucun résultat inventé. Chromium file:// bloqué et installation Playwright refusée 403 ; suites GitHub requises, aucun contournement. #70 ciblait encore feat/doses-ch-3 sans CI : base corrigée vers main, fusion toujours après #67. Conflits résolus par fusion des données et reconstruction, sans force-push.

- 18.10.2026 · #67 : tentative de fusion refusée par la politique de base alors que visuel était encore en cours. Aucun contournement ; attendre tous les contrôles requis. #70 : changement de base ne déclenche pas le workflow CI par défaut ; CI dispatchée sur la tête exacte, sans changement des règles.

- 18.10.2026 · lot 5 : Europe PMC répond par une coquille HTML et ses URL API testées 404/530 ; recherche directe du journal européen utilisée, sans prétendre avoir lu un texte Europe PMC. Source Brest enregistrée par son DOI canonique HTTP 200, sans changer la liste des domaines admis. Conflits de sources/rapport entre #99 et #100 réunis par id et sections, assets reconstruits. Contrôles non affaiblis.

- 18.10.2026 · Recontrôle après modification réseau par Vial : API GitHub, texte EDF et HUG HTTP 200 ; site public github.io toujours CONNECT 403 dans cette session, dont les observations ne contiennent pas ce domaine. Aucune application de la configuration présumée. DOI HypnoLaus renvoie vers Elsevier refusé : aucun chiffre repris. Poursuite du contenu.

- 18.10.2026 Europe/Zurich · lot 7 : Chromium Playwright absent localement, suite arrêtée avant exécution. CI navigateur requise sans modifier les assertions. Les quatre URL HUG initialement supposées ont répondu 404 ; navigation depuis l’index officiel vers les documents réels. Pages désormais HTTP 200 et app identique à bfa43f2 : ancien blocage levé sur cette URL.

- 18.10.2026 Europe/Zurich · dispositif catégoriel : endpoints officiels EBI Europe PMC et Crossref refusés CONNECT403 par ce runtime ; HUG accessible. Erreurs conservées, jamais traduites en absence de chiffre. Recherche sur runners GitHub à tester ; aucune règle réseau ni source contournée.

## G3 cours · 19.10.2026

Tests navigateur locaux : file:// refusé ERR_BLOCKED_BY_ADMINISTRATOR, aucun contournement. Les278contrôles et le parcoursG3 sont confiés à la CI exacte. Accès direct à plusieurs sources refusé ; seuls les passages effectivement lus viaweb sont attestés, limites dans le rapport sources. Un renouvellement de bail a échoué (état distant indisponible), puis lecture et renouvellement conditionnels ont réussi.

- 19.10.2026 · G4 cours : NICE NG206/202/106 et cadrage dg62 refusent l’ouverture complète403 ; seuls les extraits primaires ciblés lus sont attestés. Revue2021 refusée/captcha, extraits indexés recoupés indépendamment. Aucun contournement.
- 19.10.2026 · G4 : navigateur local file:// déjà refusé ERR_BLOCKED_BY_ADMINISTRATOR dans cet environnement ; parcours G4 confié à la CI exacte. Tests gardes exécutés directement (script sys.exit, incompatible unittest discover) ; comparateur correct tools/doses_check.py,98lignes0manquement.

- 19.10.2026 · G5 : accès complets SFE britannique/NICE refusés403, ESC redirection indisponible et SSC2026 sous abonnement ; seuls les extraits primaires ciblés réellement lus sont attestés. Aucun contournement. CO et Whipple complétés par deux primaires relues indépendamment.
- 19.10.2026 · G5 : navigateur file:// déjà refusé par politique ; suite d’interface confiée à GitHub. Cours auparavant sans métadonnées : compilateur étendu sans visa DD ; test détectant un partage mutable du lot corrigé par copie des listes. Aucun contrôle assoupli.
- 19.10.2026 · PR133, CI39277859737 liens : ancien PDFMSF404. Source9 remplacée par copie originale suisse FMS2023 p881, relue indépendamment ; aucune retouche des14parties. Métadonnées/audit/compilation et CI relancés ; aucun statut HTTP ignoré ajouté. Surveillance API temporairement502/401 ; lecture de contrôle reprise.

- 19.10.2026 Europe/Zurich · G5PR133 : tête30c2912, CI39281125489 journaux278/278 et parcoursG1–G5OK, visuel39281155143conforme ; fusionnormale refuséeHTTP405 «4of4requiredstatuschecksarequeued». Auto-fusionactive, aucune protectionmodifiée. Ordre utilisateur G6→G16traitésunàun ; G6préparé surG5conservé, fusion seulementdansl’ordre.

- 19.10.2026 Europe/Zurich · Incident G5 levé : PR133 fusionnée normalement à16:20:45UTC, main43a11f96. G6 CI39284307072 :278/278 contrôlesinteraction réussis, mais assertionUI premièrepartieG6 échoue (sous-parties horsliste). Correction des seulesbalises, mêmes motscliniques et contrôlesconservés ; testsdeportéeIUPS complétés. NouvelleCIrequise avantpublicationG6.

- 19.10.2026 Europe/Zurich,16:38UTC · G6PR134 : tête3e3e2ee, journauxCI39285718344 garde/278interactions/parcoursG1–G6 verts et visuel39285718471sanséchec ; fusion native avec SHA exact refusée par politique de base, métadonnées tests/visuel encorepending. Auto-fusionMERGEconservée, aucune protectioncontournée. G5PR133fusionnée ; Pages39284710145attenteenvironnement, règlebranchemainseule, aucunreviewer configuré etpasd’approbationpossible ; fichierspublicsencoreG4lorsducontrôle16:27UTC. Continuer cours unàun.
