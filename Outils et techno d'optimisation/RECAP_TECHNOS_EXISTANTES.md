# Technologies déjà en place avant le 6 novembre 2026

Récapitulatif en mots simples, établi à partir des fichiers réellement présents. Il décrit l’existant, pas les ajouts de cette mission.

## 1. Fabriquer les prompts et suivre les LOTs

**Le prompteur (`prompteur_grok.py`)** fabrique un prompt complet pour chaque LOT. Il choisit le code et le titre dans le catalogue, attribue le travail à l’agent A ou B, indique le LOT suivant et garde un journal. La commande `lancer <N>` prépare le lancement ; `agent` note l’agent ; `noter` ajoute une note. C’est un script local, sans appel IA, donc zéro token pour cette gestion.

**Deux rédacteurs cloud en parallèle** travaillaient avec une règle simple : A prend les LOTs impairs, B les pairs. Les documents `CAHIER_DES_CHARGES_VARIANTE_DRIVE.md` et `passation/PASSATION` distinguent trois voies : rédiger les LOTs vides en V8, compléter les LOTs partiels puis auditer, et auditer les LOTs déjà complets sans les réécrire.

**La passation et la relance** (`prompteur/PASSATION_GROK.md`, `prompteur/PROMPT_RELANCE_GROK.md`) servent de mémoire de reprise : état de la file, dernier LOT, commandes, interdits et gabarit de prompt. Elles évitent de faire redécouvrir tout le projet à chaque session.

## 2. Deux formats de cours, deux contrats

**V8 / SSP** produit une Phase A puis des fichiers par notion ou geste. La consigne demande une liste canonique, des sources, des incertitudes, des illustrations SVG contrôlées visuellement et des tailles de contenu. Les contrôles `conscience.py`, `certitude_redaction.py` et `porte_zero_jeton.py` sont explicitement présents dans le modèle de prompt.

**Medina / CHAPTER_SPEC** est un autre contrat : chapitre en quatre onglets, fenêtres cliquables, quiz, références, Pareto et fichiers séparés. `refs/CHAPTER_SPEC.md` impose notamment les classes et clés, la construction et les tests de prévisualisation. Les deux formats partagent des idées d’optimisation mais ne doivent pas être mélangés.

## 3. Le harnais : des règles et des portes, pas un modèle de plus

**Le mode « Harnais seul », sans Routage**, est la consigne de production consignée dans les passations. Il ne signifie pas « sans contrôle » : il fixe des étapes, permissions, preuves, critères d’arrêt et interdits.

**Le harnais existant** (`repo/harnais/HARNAIS_OBLIGATOIRE.md`) contient la lecture de l’arsenal, le Bracelet, une preuve d’exécution, la compilation Python, des contrôles avant l’IA, l’extraction ciblée des gros HTML, des caches par empreinte SHA-256, des rapports courts et des fichiers d’état. Son mode historique précise aussi un parallélisme et une escalade de modèle ; la variante Grok de passation désactive le Routage.

**La garde** (`garde_harnais_seul.py`) vérifie le harnais, compile ses scripts et regarde que le hook `pre-commit` est installé. `veille_box.sh` répète cette garde toutes les cinq minutes. Le modèle de prompt prévoit `porte_zero_jeton.py precommit` dans le hook : les défauts mécaniques sont arrêtés avant un commit, sans appel payant.

## 4. Certitude, sources et audits

**`certitude_redaction.py` existe** à `repo/grok-LOTS-html/outils/certitude_redaction.py`. D’après la boucle documentée, il rend VERT, ORANGE ou ROUGE à partir du fichier et des preuves. Les éléments centraux ne doivent pas être supprimés pour faire passer un contrôle ; les incertitudes sont consignées.

**Les audits** étaient organisés par rôle : contrôles mécaniques dans la boucle de rédaction ; pour les LOTs complets de la voie 3, audit médical puis conformité par un modèle différent du rédacteur. Ce n’est donc pas un audit externe uniforme sur chaque étape : le cahier de la variante prévoit d’abord une rédaction V8 sans audit général, puis un audit restauré pour les autres pistes.

## 5. Bracelet, Skills et dessin

**Le Bracelet** (`repo/harnais/bracelet/bracelet_suggest.py`) associe la description d’une tâche à un petit catalogue : nettoyage web, mémoire, cache, orchestration, protection et mesure. Il retourne au maximum trois suggestions. Le harnais demande d’en utiliser un à trois, jamais les dix-neuf.

**Les Skills SSP** sont présents sous `repo/skills/` et `repo/docs/skills/` : extraction ciblée, revue du diff, qualité visuelle, tests, sources, posologie suisse et audit médical, entre autres. Ils chargent un mode d’emploi spécialisé à la demande.

**Le dessinateur** et les SVG interactifs font partie du prompt V8 ; chaque illustration doit être capturée puis regardée. Les données techniques concernant les coûts sont consignées dans les journaux de consommation plutôt que déduites d’une promesse commerciale.

## 6. Éléments non trouvés ou non vérifiés

- Aucun fichier nommé `audit-lot-v7` n’a été trouvé dans les arbres consultés ; des fichiers V7 sont présents, mais cela ne prouve pas l’existence de cette Skill sous ce nom.
- Aucune preuve lue ici ne permet d’affirmer qu’un petit modèle local, OpenCode ou Promptfoo était déjà intégré à la production : ces outils sont des ajouts proposés dans la présente mission.
- Les documents historiques contiennent des chiffres de volumes et d’états de LOTs ; ils ne sont pas repris comme mesures de performance ni d’économie.

## Sources consultées

`/workspace/grok/CAHIER_DES_CHARGES_VARIANTE_DRIVE.md` ; `prompteur/PASSATION_GROK.md` ; `prompteur/PROMPT_RELANCE_GROK.md` ; `veille_box.sh` ; `garde_harnais_seul.py` ; `repo/harnais/HARNAIS_OBLIGATOIRE.md` ; `repo/harnais/bracelet/` ; `repo/grok-LOTS-html/outils/certitude_redaction.py` ; `/workspace/outils-puissants/refs/CHAPTER_SPEC.md`.
