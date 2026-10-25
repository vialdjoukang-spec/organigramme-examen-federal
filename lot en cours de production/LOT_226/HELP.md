# HELP — reprise V0 du LOT_226

Ce registre ne constitue ni un audit médical ni une validation. Les anciens rapports restent sur leurs branches historiques.

## H01 — Harnais individuel, étape zéro

Les versions épinglées du runtime ont été installées dans `/tmp/harnais-codex-v0`. Le probe canonique, exécuté sous l'identité `CODEX_V0_LOT226`, échoue sur le téléchargement de `https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken` : le proxy renvoie `403 Forbidden`.

La preuve réelle est `PREUVE_RUNTIME_HARNAIS_CODEX_V0.json`, avec `complete:false`. Aucun téléchargement alternatif, changement de proxy ou test modifié pour obtenir un faux vert n'est tenté. La configuration réseau doit être corrigée par le mécanisme autorisé de l'environnement, puis le probe doit être relancé sans altération. Aucun GO clinique n'est acquis entre-temps.

## H02 — Phase A, liste des dix scénarios et fréquences

Le registre historique `evidence/registre_sources.json` du commit `502f8ff2284dc0417ddb3c6245f73a901596c36d` déclare que les fréquences comparables des dix scénarios parmi les malades chroniques suisses n'ont pas été trouvées. Leur ordre pédagogique n'est pas un classement statistique démontré.

Il faut établir les arguments de fréquence sur des sources suisses réellement relues, puis européennes si nécessaire ; expliciter les inconnues et les priorités d'exclusion. Aucune liste canonique n'est encore gelée. Emplacement cible : Bloc 2 de Phase A, puis `LISTE_DX_CANONIQUE.md` après validation.

## H03 — Médicaments et AIPS

L'entrée historique AIPS est un portail ouvert, pas une monographie de produit lue. Les informations professionnelles des médicaments effectivement retenus, dont sertraline ou escitalopram si ces traitements sont développés, restent à ouvrir et à vérifier intégralement. Les doses, indications, adaptations, grossesse/allaitement et numéros Swissmedic ne sont pas certifiés par cette séance. Emplacement cible : les points 11 concernés. Toute donnée introuvable reste « À vérifier (AIPS) ».

Le corpus indiqué par Vial a été retrouvé : `Medina/AipsDownload_20261008.zip`, au commit `8a512893acbab9caa0dcfdd0e8682a44ea72fda6`. Le ZIP et ses empreintes ont été vérifiés. Il contient un XML et son XSD, générés le 8 octobre 2026. Le schéma décrit un index avec références URL, pas des textes de monographies embarqués. L'inventaire technique compte 10 221 notices et 30 279 documents rattachés. La lecture des fiches primaires et la vérification d'éventuelles mises à jour depuis cet export restent nécessaires. `AIPS_MEDINA_INVENTAIRE.json` conserve les métadonnées ; aucune posologie n'est présentée comme vérifiée par cet inventaire.

## H04 — QA390

Le refus explicite historique du navigateur demeure conservé. Aucun contournement par localhost, dataURL, CI de rendu ou navigateur alternatif n'est tenté. La preuve autorisée doit identifier le fichier, sa date, sa taille, son SHA-256, les mesures et les interactions contrôlées. Sans elle, aucune validation globale n'est prononcée.

## H05 — Auditeur indépendant

Aucun auditeur distinct n'est affecté à cette séance. Il faut deux grilles séparées, médicale et linguistique/conformité, sur chaque version figée. Le rédacteur ne s'auto-note pas ; une nouvelle session ou un nouveau nom ne remplace pas l'indépendance. Un score d'au moins 90 %, zéro critique et une réponse finale « oui » sont requis pour chaque monographie et chaque fichier.

## H06 — Poids et contenu utile

Les 139 627 octets du fichier historique A incluent l'ensemble du HTML ; ils ne prouvent pas 150–200 Ko de contenu propre pour la seule monographie SSP. Les quatre fichiers B historiques contiennent chacun plusieurs scénarios et restent également insuffisants pour démontrer ce poids par entité. La remise en conformité devra compléter les lacunes sur sources, sans répétition ni remplissage. Un renommage V0 ne suffit pas.

## H07 — Publication et automatismes

La PR447 publie le V0 corrigé sur une autre branche ; ne pas la dupliquer. Le prototype inverse V8 n'est ni contre-audité ni déployé. Le nouveau moteur V0 reste lui aussi sans déploiement et sans tâche GPT créée. L'intégration d'une cadence GitHub 5 min et GPT 1 h ne sera déclarée active qu'après vérification des capacités et de preuves réelles. Aucun automate ne doit attribuer un nouveau lot.
