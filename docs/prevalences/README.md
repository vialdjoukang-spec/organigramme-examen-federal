# Automates de prévalences · G, S, F, O

Ordre de Vial du 18.10.2026 : suspendre les lots le temps de créer les recherches catégorielles, leurs jauges et un agent auditeur statistique, puis reprendre la suite. Le catalogue réel contient G, S, F et O ; aucune catégorie P. Les 19 secteurs sont calculés depuis SSP. Les dénominateurs sont recalculés depuis NOT à chaque exécution, sans recopier un total historique.

## Demande simple : « jauges prévalences »

```sh
python3 tools/prevalences/jauges.py --distant
python3 tools/prevalences/jauges.py --distant --secteurs
```

Jauges publiques : [prévalences par catégorie et secteur](https://vialdjoukang-spec.github.io/organigramme-examen-federal/prevalences.html), également liées depuis progres.html. Le JSON voisin est téléchargeable. Le calculateur lit les résultats persistants de la branche `automates/prevalences` ; `--distant` effectue un fetch sans changer de branche. Hors réseau, omettre `--distant` pour lire le dossier local `.etat_local/prevalences` (une absence d'état donne zéro recherche, jamais une exécution inventée).

## Quatre scripts, un moteur commun

```sh
python3 tools/prevalences/g.py --limit 40
python3 tools/prevalences/s.py --limit 40
python3 tools/prevalences/f.py --limit 40
python3 tools/prevalences/o.py --limit 40
```

Chaque script repart du premier diagnostic jamais recherché de sa catégorie, depuis G1 pour G, dans l'ordre officiel du catalogue. Il conserve l'état après chaque diagnostic. Les libellés et contextes SSP sont identifiés par empreinte ; un changement invalide le vieux résultat pour la jauge. Les doublons de diagnostics restent distincts par plainte pour ne pas confondre les dénominateurs ; le cache réseau évite de télécharger plusieurs fois le même résultat.

Pour chaque diagnostic : requêtes Suisse puis Europe, consultation puis population, libellé français et alias anglais configurés. Europe PMC fournit les références/résumés, Crossref élargit la découverte, l'index officiel HUG donne des PDF dont les pages sont conservées. Les extraits chiffrés exigent au moins un terme du diagnostic. Cette correspondance lexicale est une piste à relire, jamais la preuve que le diagnostic exact ou la population convient. Les sources découvertes ne sont pas automatiquement admises dans les sources cliniques.

`--plan` affiche les tâches sans réseau ; `--limit 0` parcourt toute la catégorie dans le budget ; `--budget-seconds`, `--timeout`, `--workers` (1–4), `--refresh-days` et `--retry-hours` bornent l'exécution. `--providers hug` permet un diagnostic d'accès ciblé, mais ne valide pas la jauge « recherche aboutie », qui exige le protocole complet. Les requêtes sont espacées, les documents plafonnés et les résultats mis en cache. Les exceptions sont des erreurs, pas des recherches sans résultat. Les candidats sont conservés avec diversité fournisseur/CH/Europe/cadre ; les omissions dues au plafond sont comptées. Aucune source brute intégrale n'est publiée.

## Activation sans PC

`.github/workflows/prevalences-recherche.yml` lance les quatre scripts sur quatre jobs indépendants toutes les quatre heures (`23 */4 * * *`) et sur demande. Chaque lot traite au plus 40 diagnostics par catégorie, dans un budget de 12 minutes ; les diagnostics non commencés restent dus. Une erreur d'un secteur ne bloque pas les autres. Le contrôle statistique déterministe est appliqué après chaque catégorie puis à la consolidation. L'état, les candidats, les erreurs et les audits sont conservés dans la branche de suivi séparée, sans écrire de chiffre dans main.

Relance manuelle :

```sh
gh workflow run prevalences-recherche.yml --ref main -f limite=40
```

La planification GitHub peut être retardée ; regarder les dates réelles. Les succès de requêtes signifient que les moteurs ont répondu au protocole, pas que toute la littérature a été trouvée. Une API bloquée garde la recherche partielle et la cause exacte ; elle sera réessayée. La session interactive du 18.10 refuse les API EBI/Crossref, alors que HUG est accessible ; les runners GitHub ont leur propre configuration réseau, contrôlée au premier lancement réel.

## Lecture des quatre mesures

- Tentés : diagnostics ayant au moins une tentative, échecs compris.
- Recherche aboutie : toutes les neuf requêtes attendues ont répondu, sans requête manquante ou dupliquée. Zéro article trouvé peut être une réponse valide ; ce n'est pas une absence de maladie.
- Candidats : extraits chiffrés à relire. Une hausse ne fait jamais monter la couverture clinique.
- Chiffres sourcés : données de main avec chiffre valide, diagnostic exact, source présente, date et emplacement. C'est un contrôle de structure, pas une approbation médicale. La règle clinique actuelle P2 exige un chiffre strictement positif ; un véritable zéro nécessite sa propre justification et une évolution explicite de cette règle.

Les SSP sans différentiel sont comptés séparément. À la création, le catalogue réel en contient 12 (S8.1–S8.12), et non les 22 des anciens relevés. Aucun diagnostic ni dénominateur n'est fabriqué pour les faire disparaître.

## Agent auditeur statistique

Voir [son mandat](AUDITEUR_STATISTIQUE.md). Un agent distinct a relu le dispositif dans cette session. Le script `auditeur.py` exécute les contrôles mécaniques et corrections arithmétiques documentées ; il ne se présente pas comme un jugement clinique autonome. Les nouveaux candidats forment `agent-file.json`. Une relance `@codex` demande à l'intégration du dépôt de reprendre cette file, au plus une fois toutes les 12 heures, tant que de nouveaux candidats ou une file non acquittée restent dus. Le lien de commentaire est conservé ; il ne prouve pas que le travail d'un agent est commencé ou achevé.

Les pourcentages n'entrent dans l'application qu'après source réellement relue, population et diagnostic contrôlés, référence datée, audit et CI verts. Suisse et Europe sont recherchées largement ; leur comparabilité n'est pas présumée pour chaque cohorte (âge, recrutement, pays, période et cadre restent explicites).
