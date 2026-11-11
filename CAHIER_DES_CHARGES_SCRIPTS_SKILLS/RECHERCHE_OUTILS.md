# Recherche — compétences (skills), serveurs MCP et outils pour les agents Grok G1 et G2

Relevé effectué le 24 octobre 2026 (heure de Zurich, UTC+2). Étoiles et dates de dernier envoi (« push ») lues sur l'API publique GitHub le même jour ; elles évoluent.
Aucun élément n'a été installé. Chaque verdict reste une recommandation soumise à votre accord.

## Contrainte technique préalable — plateforme Grok

L'API xAI accepte des serveurs MCP **distants uniquement** (transport « Streamable HTTP » ou SSE), pas les serveurs locaux en stdio ([docs.x.ai — Remote MCP Tools](https://docs.x.ai/developers/tools/remote-mcp)). Le paramètre `allowed_tools` limite les outils injectés dans le contexte ; il réduit les jetons et le risque. Un serveur stdio (Git, Fetch, LanguageTool local…) doit donc soit tourner dans l'environnement d'exécution de l'agent (si celui-ci dispose d'un shell), soit être exposé derrière une passerelle HTTP privée et authentifiée.
La mise en cache des préfixes est automatique chez xAI ; elle exige un préfixe stable et une clé `prompt_cache_key` constante par conversation ([docs.x.ai — Best Practices](https://docs.x.ai/developers/model-capabilities/text/best-practices)).

## Tableau de synthèse

| # | Outil | URL | Rôle | Mainteneur | Étoiles / dernier envoi | Sécurité | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | GitHub MCP Server (officiel) | https://github.com/github/github-mcp-server | Branches, fichiers, PR, revues, Actions | GitHub (officiel) | 33 895 / 23.10.2026 | Officiel, MIT. Exige un jeton : utiliser un **PAT à granularité fine limité au seul dépôt**, droits `contents:write` et `pull_requests:write`, rien d'autre. Restreindre par `--toolsets repos,pull_requests` (ou `allowed_tools`). Mode lecture seule disponible pour les auditeurs. | **Adopter** |
| 2 | Connecteur `cursor-github` déjà relié | (connecteur existant) | Même usage, déjà authentifié | — | — | Déjà en place ; évite de créer un nouveau jeton. | **Adopter** (si les agents Grok y ont accès) |
| 3 | Serveur de référence Git | https://github.com/modelcontextprotocol/servers/tree/main/src/git | Opérations git locales (branche, diff, commit) | MCP steering group | dépôt 91 525 / 22.10.2026 | Officiel mais **« implémentation de référence, non prête pour la production »** selon son README. Stdio uniquement. Un `git` CLI natif suffit si l'agent dispose d'un shell. | Peut-être |
| 4 | Serveur de référence Fetch | https://github.com/modelcontextprotocol/servers/tree/main/src/fetch | Lire une page web (AIPS, Fedlex, OFSP) en Markdown | MCP steering group | idem | Officiel, référence. Risque SSRF (accès réseau interne) : n'exposer qu'en environnement isolé. L'outil de recherche web natif de Grok peut suffire. | Peut-être |
| 5 | Serveurs Filesystem / Memory / Sequential Thinking | https://github.com/modelcontextprotocol/servers | Fichiers, mémoire graphe, raisonnement guidé | MCP steering group | idem | Officiels, référence. Memory et Sequential Thinking **augmentent** les jetons sans bénéfice net ici. | Rejeter (Memory, SeqThinking) ; Filesystem : peut-être, borné au dossier du lot |
| 6 | PubMed (hébergé par Anthropic) | https://pubmed.mcp.claude.com/mcp — doc : https://claude.com/resources/tutorials/using-the-pubmed-connector-in-claude | Recherche PubMed/PMC, métadonnées, texte intégral PMC, conversion d'identifiants | Anthropic (première partie) | marketplace https://github.com/anthropics/life-sciences : 625 / 23.10.2026 | Sans authentification, lecture seule. Panne signalée (issue anthropics/healthcare #40, mars–avril 2026). Usage depuis Grok non documenté par Anthropic : à tester. | Peut-être (tester d'abord) |
| 7 | cyanheads/pubmed-mcp-server | https://github.com/cyanheads/pubmed-mcp-server | 11 outils PubMed + Europe PMC (utile pour l'Europe), MeSH, citations Vancouver, **avis de rétractation liés** | Communauté (Casey Hand) | 162 / 23.10.2026 (v2.10.23) ; Apache-2.0 | Communautaire mais très actif, API NCBI officielles en lecture seule. Le point d'accès public `pubmed.caseyjhand.com` est un serveur personnel : **l'auto-héberger** (Docker, Streamable HTTP) plutôt que d'envoyer les requêtes à un tiers. Clé NCBI facultative. | **Adopter (auto-hébergé)** |
| 8 | nickjlamb/pubcrawl | https://github.com/nickjlamb/pubcrawl | PubMed, Europe PMC, étiquetage FDA/UK, ClinicalTrials.gov | Communauté (PharmaTools.AI) | 15 / 16.10.2026 ; MIT | Peu d'étoiles. L'étiquetage **FDA** est interdit comme référence par la V7 (§4.2). | Rejeter |
| 9 | Autres serveurs PubMed (JackKuo666, Augmented-Nature, benoitleq, masa061580) | GitHub | PubMed simple | Communauté | 132 / mai 2025 ; 15 ; 0 ; 2 | Peu maintenus ou très récents, sans revue. | Rejeter |
| 10 | LanguageTool (serveur officiel, auto-hébergé) | https://github.com/languagetool-org/languagetool ; image Docker communautaire https://github.com/Erikvl87/docker-languagetool | Grammaire, orthographe, typographie françaises (fr-CH disponible) | LanguageTool GmbH (officiel) ; image : communauté | 15 184 / 23.10.2026 (LGPL-2.1) ; image 728 / 17.06.2026 | L'API publique **interdit les requêtes automatisées** et limite à 20 requêtes/min et 20 Ko/requête (https://dev.languagetool.org/public-http-api). Il faut donc une instance privée. Appel par un script local (`POST /v2/check`) plutôt que par un MCP communautaire. | **Adopter (instance privée + script)** |
| 11 | MCP LanguageTool communautaires (gebab88, dpesch, olga1988olga) | https://github.com/gebab88/languagetool-mcp-api-wrapper ; https://codeberg.org/dpesch/languagetool-mcp-server | Enveloppe MCP de LanguageTool | Particuliers | 0 étoile / 15.10.2026 ; npm ~10 téléchargements/semaine | Non audités, stdio, faible adoption ; dpesch exige un abonnement Pro et transmet des identifiants. | Rejeter (un script de 30 lignes fait mieux) |
| 12 | anthropics/skills — `skill-creator` | https://github.com/anthropics/skills/tree/main/skills/skill-creator | Méthode pour écrire et tester une compétence SKILL.md | Anthropic (officiel) | 183 294 / 09.10.2026 ; Apache-2.0 | Texte et scripts lisibles, aucun accès réseau requis. README : « à des fins de démonstration ». | **Adopter** (comme modèle de format) |
| 13 | anthropics/skills — `webapp-testing` | https://github.com/anthropics/skills/tree/main/skills/webapp-testing | Tests Playwright : rendu réel à 390 px (V7 §10), absence de débordement | Anthropic (officiel) | idem | Exécute un navigateur local ; aucun secret. Répond au blocage « rendu 390 px NON VÉRIFIÉ » consigné dans l'état du projet. | **Adopter** |
| 14 | microsoft/playwright-mcp | https://github.com/microsoft/playwright-mcp | Pilotage navigateur par MCP | Microsoft (officiel) | 38 558 / 22.10.2026 ; Apache-2.0 | Officiel ; navigation libre = surface d'attaque plus large que le script de `webapp-testing`. | Peut-être (seulement si aucun shell) |
| 15 | anthropics/skills — `docx`, `pdf`, `pptx`, `xlsx` | https://github.com/anthropics/skills/tree/main/skills | Documents bureautiques | Anthropic | idem | **Source disponible, pas open source** (README). Sortie autre que .html interdite par la V7 §2. | Rejeter |
| 16 | anthropics/skills — `frontend-design`, `web-artifacts-builder` | idem | Génération d'interfaces HTML/React | Anthropic | idem | Orientés applications avec scripts/React ; contraires au gabarit V7 (aucun script, aucune feuille externe). | Rejeter |
| 17 | microsoft/markitdown | https://github.com/microsoft/markitdown | Convertit PDF/DOCX/HTML (recommandations, AIPS téléchargées) en Markdown compact | Microsoft (officiel) | 191 826 / 23.10.2026 ; MIT | Local, pas de jeton. **Gros gain de jetons** : on lit un Markdown filtré au lieu d'un PDF brut. Relire les tableaux de doses sur l'original (risque de perte de mise en page). | **Adopter** |
| 18 | Nu Html Checker (vnu) | https://github.com/validator/validator | Validation HTML5 hors ligne (balises équilibrées, V7 §10) | W3C / validator.nu | 1 991 / 12.10.2026 ; MIT | Local (jar ou Docker), aucun réseau. Contrôle à zéro jeton. | **Adopter** |
| 19 | upstash/context7 | https://github.com/upstash/context7 | Documentation de bibliothèques logicielles | Upstash | 63 553 / 23.10.2026 | Sans rapport avec le contenu médical. | Rejeter |
| 20 | yamadashy/repomix | https://github.com/yamadashy/repomix | Empaquette un dépôt pour un LLM | Communauté | 29 000 / 22.10.2026 | Utile pour du code ; ici, il **gonflerait** le contexte. | Rejeter |
| 21 | trufflesecurity/trufflehog | https://github.com/trufflesecurity/trufflehog | Détection de secrets avant envoi | Truffle Security | 28 676 / 23.10.2026 ; AGPL-3.0 | Local ; protège contre l'envoi accidentel d'un jeton dans une branche. | Peut-être (crochet pré-envoi) |
| 22 | anthropics/healthcare (CMS, ICD-10, NPI) | https://github.com/anthropics/healthcare | Données de santé **américaines** | Anthropic | — | Hors référentiel suisse (V7 §4.2). | Rejeter |

## Lacune importante

Aucun serveur MCP réputé ne couvre les sources **suisses** exigées par la V7 : swissmedicinfo.ch (AIPS), liste Swissmedic, Fedlex, OFSP, sociétés suisses. Recommandation :
1. Utiliser la recherche/lecture web native de Grok (ou Fetch) et **markitdown** pour ces pages.
2. Interroger les CSV Swissmedic déjà présents dans le projet par `grep`/script, jamais en les chargeant dans le contexte.
3. Pour Fedlex, un point SPARQL public existe (fedlex.data.admin.ch) ; un petit script maison est plus sûr qu'un MCP inconnu (à confirmer avant usage).

## Règles de sécurité communes

- Jetons : un PAT fin par agent, limité au dépôt, sans droit d'administration ni de workflow ; jamais écrit dans un fichier du dépôt.
- `allowed_tools` explicite pour chaque serveur MCP ; aucune suppression de branche, aucune fusion vers `main`.
- Aucun serveur hébergé par un particulier ne reçoit les requêtes des agents ; auto-hébergement ou première partie seulement.
- Toute réponse d'un outil (PubMed, page web) est une donnée à vérifier, jamais une instruction.
