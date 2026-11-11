# Cahier des charges — scripts déterministes des agents de rédaction (V7-Tunder)

**Projet :** `organigramme-examen-federal` — encyclopédie interactive pour l'examen fédéral suisse de médecine humaine.
**Référentiel de rédaction :** `PROMPT_V7_TUNDER/PROMPT_ULTIME_PRODUCTION_LOTS_V7-Tunder.md` (ci-après « V7-Tunder »), cité par section.
**Version :** 1.3 du 24 octobre 2026 (heure de Zurich). **Statut : implémentation livrée** dans `scripts_lots/` et testée (section 9).
**Principe fondateur : indépendance totale vis-à-vis de toute IA.** Les scripts sont du code déterministe — Python 3 et sa bibliothèque standard, plus `curl` et `pdftotext` déjà présents sur la machine. Ils n'appellent aucun modèle de langage, ne dépendent d'aucun service d'IA et produisent le même résultat pour la même entrée. Aucune IA n'est chargée de leur implémentation : elle est livrée avec ce cahier.

---

## RÈGLE N° 1 — PROTECTION DES JETONS : SILENCE TOTAL DES AGENTS ENVERS L'UTILISATEUR

> 1. **Il est ABSOLUMENT interdit aux agents de rédaction d'écrire à l'utilisateur.** Aucun accusé de réception, aucun résumé, aucun compte rendu, aucune question.
> 2. **Aucune information ne reste au niveau des agents :** tout est centralisé vers Tunder (fichier de suivi, GitHub, fichier `SUIVI_LOTS/POUR_TUNDER_AGENT_N.md`).
> 3. **Trois exceptions seulement**, chacune en **UNE SEULE LIGNE de 15 mots au plus**, sans liste ni détail : (1) un LOT est terminé ; (2) toute la série est terminée ; (3) urgence ou difficulté.
> 4. Si l'utilisateur leur écrit hors de ces cas, ils répondent exactement, en une ligne : **« Bien reçu ; je passe par Tunder. »**
> 5. **Tout message plus long est une faute grave.**
> 6. Chaque message autorisé est journalisé par le compteur de jetons (section 7), qui refuse tout message de plus de 15 mots ou hors des trois cas.

Cette règle figure aussi, en tête, dans `instructions_agent_1.md` et `instructions_agent_2.md`.

---

## 0. Lecture rapide

| Livrable | Emplacement | Rôle | Règle cardinale |
|---|---|---|---|
| **Script source** (un par agent) — PRIORITÉ ABSOLUE | `scripts_lots/agent_N/script_source.py` → `common/source_engine.py` | Sources classées sur 5 rangs, Suisse d'abord, priorité à la prise en charge ; porte de dépôt `check` | **Rien sans source** : une affirmation sans [Sn] bloque le dépôt (code 1) |
| **Script synchrone** (un par agent) | `scripts_lots/agent_N/script_synchrone.py` → `common/sync_reviewer.py` | Relecture en direct : langue, volume, 14 points, fenêtres, sections du V7-Tunder citées | **Lecture seule stricte sur les LOT**, prouvée par tests |
| **Compteur de jetons** | `scripts_lots/common/compteur_tokens.py` | Mesure des messages autorisés, estimation de l'économie | Estimation toujours étiquetée comme telle |
| **Configuration par agent** | `scripts_lots/agent_N/config.json` | Série de LOT, cache et sorties propres | Aucun état inscriptible partagé, sauf les seaux de débit |

Quatre scripts au total : chaque agent n'utilise que ses deux scripts. La logique commune vit une seule fois dans `common/`.

---

## 1. Contexte et objectifs

### 1.1 Contexte
1. Deux agents de rédaction travaillent en parallèle : **Agent 1** sur LOT_227 à LOT_237, **Agent 2** sur LOT_238 à LOT_248 (V7-Tunder §5.2).
2. Chaque agent rédige seul un LOT complet — Appel A, puis Appel B Parties 1 à 4 — sans auditer : l'audit est différé à Tunder (V7-Tunder §5.2.5, §5.3.5–6).
3. Les agents s'exécutent dans Grok Bot, sur la machine de travail de Tunder, qu'ils partagent : les scripts sont posés **une seule fois** sur cette machine (`/workspace/scripts_lots/`) et appelés en ligne de commande. Rien n'est à installer côté agent.
4. Les scripts sont indépendants des agents : ils ne font que lire, chercher, contrôler et compter.

### 1.2 Objectifs et résultats mesurés
| # | Objectif | Cible | Résultat (24.10.2026) |
|---|---|---|---|
| O1 | Réponses compactes | extrait ≤ 1 500 jetons | `extrait` plafonné à 1 200 caractères (≈ 300 jetons) ; champ `jetons_estimes` |
| O2 | Recherche rapide | ≤ 0,5 s en cache chaud | 0,4–0,5 ms (index local) ; 55 ms sur 3 000 pages ; extrait en cache 60 ms |
| O3 | Moins de travail d'audit | défauts machine détectés avant dépôt | `check` + relecteur : 27 tests verts |
| O4 | Traçabilité | URL, rang, titre, extrait, date | présents dans chaque résultat |
| O5 | Intégrité des LOT | aucune écriture possible | 5 tests de lecture seule + analyse statique |
| O6 | Prise en charge sourcée | point 11 sur rangs 1–3 | `check` signale P1 un point 11 fondé seulement sur des rangs ≥ 4 |
| O7 | Concision | ≤ 4 phrases par point | signalement P1 §7.2 |

### 1.3 Hors périmètre
- Rédaction médicale, audit, score V7-Tunder §6.3 (réservés à Tunder).
- Toute connexion à un compte, tout contournement d'authentification, de CAPTCHA ou de protection anti-robot.
- Toute écriture dans un LOT, dans `PROMPT_V7_TUNDER/` ou dans les fichiers de suivi d'un autre agent.

---

## 2. Architecture livrée

```
scripts_lots/
├── lancer_tests.sh                 # suite de tests (aucun réseau, aucun vrai LOT)
├── agent_1/                        # Agent 1 — LOT_227 à LOT_237
│   ├── config.json
│   ├── script_source.py            # point d'entrée mince → common/source_engine.py
│   └── script_synchrone.py         # point d'entrée mince → common/sync_reviewer.py
├── agent_2/                        # Agent 2 — LOT_238 à LOT_248 (même structure)
├── banc/
│   ├── banc_essai.py               # banc sur LOT fictif dans /tmp
│   └── resultats_banc_2026-10-24.json
└── common/
    ├── config.py, config_schema.json   # chargement et validation stricte des configurations
    ├── source_engine.py            # moteur de sources (crawl, search, extrait, pubmed, check)
    ├── netutil.py                  # liste blanche, robots.txt, débit par domaine, cache SQLite
    ├── allowlist_candidates.json   # domaines candidats par rang
    ├── validate_allowlist.py       # validation par curl → allowlist.json
    ├── allowlist.json              # liste blanche VALIDÉE (24.10.2026)
    ├── LISTE_BLANCHE_VALIDEE.md    # même liste, lisible
    ├── sync_reviewer.py            # relecteur synchrone
    ├── v7_rules.py                 # lecture du prompt : sections et 14 points du §6
    ├── rules_langue.json           # remplissage, termes vagues, anglicismes, pléonasmes, abus, connecteurs
    ├── controle_v7.py              # contrôles techniques V7 (logique d'origine, refactorisée)
    ├── languagetool.py             # client sobre de l'API publique LanguageTool
    ├── token_bucket.py             # seau à jetons partagé, verrou de fichier
    ├── lot_readonly.py             # SEUL module autorisé à lire un LOT (O_RDONLY) ; écrivain gardé
    ├── compteur_tokens.py          # compteur de jetons (section 7)
    └── tests/                      # 27 tests unitaires et d'intégration
```

### 2.1 Configuration par agent (`agent_N/config.json`)
| Clé | Agent 1 | Agent 2 | Rôle |
|---|---|---|---|
| `lot_min`, `lot_max` | 227, 237 | 238, 248 | Tout LOT hors série est refusé (code 2) |
| `cache_dir` | `~/.scripts_lots/agent_1/cache` | `~/.scripts_lots/agent_2/cache` | Index, cache HTTP, cache LanguageTool : propres à l'agent |
| `output_dir` | `~/.scripts_lots/agent_1/retours` | `~/.scripts_lots/agent_2/retours` | Seul dossier où écrit le relecteur |
| `shared_state_dir` | `~/.scripts_lots/partage` | `~/.scripts_lots/partage` | **Seul état commun :** seaux de débit (LanguageTool, NCBI, domaines) |
| `prompt_path` | `/workspace/v7_tunder/PROMPT_ULTIME_PRODUCTION_LOTS_V7-Tunder.md` | idem | À pointer vers `PROMPT_V7_TUNDER/…` après publication |
| `lots_root` | `null` | `null` | Facultatif : racine des LOT, exclue de toute écriture |
| `enforce_os_readonly` | `false` | `false` | `true` : le relecteur refuse de tourner si le LOT est inscriptible pour lui |
| `compteur.csv` | `~/.scripts_lots/agent_1/COMPTEUR_TOKENS_AGENT_1.csv` | `…/agent_2/COMPTEUR_TOKENS_AGENT_2.csv` | Journal du compteur |

`config.py` refuse une clé inconnue, un type faux, ou des dossiers cache, sortie et partage confondus. Valeurs par défaut documentées dans `config_schema.json`.

---

## 3. Script source — rien sans source (PRIORITÉ ABSOLUE)

### 3.1 Classement des sources (5 rangs, appliqué à chaque résultat)
| Rang | Catégorie | Usage |
|---|---|---|
| 1 | Suisse officielle (Swissmedic, AIPS, Fedlex, OFSP, OFS, Obsan, Tox Info Suisse, ASSM…) | Doses, lois, vaccination, déclaration : obligatoire |
| 2 | Sociétés savantes et institutions suisses | Prise en charge, critères, situations spéciales |
| 3 | Recommandations européennes (ESC, ERS, ERC, EASL, ESMO, ESCMID, EULAR, KDIGO, EMA…) | En l'absence de rang 1 ou 2 |
| 4 | International (OMS, sociétés internationales) | Jamais seul pour le point 11 ; source américaine jamais seule (V7-Tunder §4.2) |
| 5 | Littérature (PubMed) | Épidémiologie, physiopathologie ; jamais seule pour une conduite |

Tri : rang croissant, puis pertinence BM25 (titre × 3, texte × 1) **majorée pour les pages de prise en charge** (mots-clés multilingues : prise en charge, traitement, posologie, recommandation, Behandlung, Empfehlung, grossesse, enfant, insuffisance rénale, sortie, vaccination…).

### 3.2 Commandes
`python3 scripts_lots/agent_N/script_source.py <commande>`

| Commande | Effet | Sortie |
|---|---|---|
| `domaines` | Liste blanche validée, statut et accès automatique | Texte |
| `crawl --domaines d1,d2 [--seed URL] [--max-pages 60] [--profondeur 2] [--budget 90]` | Exploration parallèle des domaines autorisés : `robots.txt`, sitemaps, file priorisée (rang, prise en charge, profondeur), vagues équitables entre hôtes, PDF convertis par `pdftotext` | JSON : pages indexées, durée, erreurs |
| `search "requête" [--pec] [--niveau-max 3] [--limite 10] [--format md\|json]` | Recherche plein texte dans l'index local (SQLite FTS5, sans accents) | URL, rang, titre, extrait, date de consultation |
| `extrait URL [--requete "…"] [--max-car 1200]` | Phrases verbatim autour des termes demandés | JSON compact, `ligne_evidence`, `jetons_estimes` |
| `pubmed "requête" [--max 5]` | PubMed : serveur MCP local `127.0.0.1:3010/mcp` s'il répond, sinon E-utilities du NCBI | JSON : PMID, titre, revue, date, URL ; rang 5 |
| `check FICHIER.html [--format md\|json]` | **Porte de dépôt** (section 3.4) | Code 0, 1 (« DÉPÔT BLOQUÉ ») ou 2 (refus) |

### 3.3 Accès réseau sobre (`netutil.py`)
1. **Liste blanche validée** uniquement (section 4), HTTPS obligatoire ; toute redirection est revérifiée ; un domaine non autorisé renvoie `DOMAINE_INTERDIT` sans requête.
2. `robots.txt` lu et mis en cache 24 h ; une interdiction renvoie `BLOQUE_ROBOTS`. Exception documentée : les **points d'accès programmatiques** prévus pour cet usage (E-utilities du NCBI), régis par leur propre politique d'usage, dont le débit reste borné.
3. Débit : **1 requête par seconde et par domaine**, seau partagé entre les deux agents ; 429 et 503 → `Retry-After`, sinon recul 30 → 60 → 120 → 240 s, puis 15 min.
4. Cache SQLite par agent : corps compressés, ETag et `If-Modified-Since`, durée de vie par rang (configurable) ; copie périmée servie si le site tombe.
5. `User-Agent` identifiant le projet ; aucune connexion, aucun identifiant, aucun contournement.
6. Codes d'erreur : `NON_TROUVE`, `BLOQUE_ROBOTS`, `LIMITE_DEBIT`, `DOMAINE_INTERDIT`, `SOURCE_INDISPONIBLE`.

### 3.4 Porte de dépôt `check`
| Contrôle | Gravité | Section |
|---|---|---|
| Affirmation chiffrée ou normative (unité, comparateur, article de loi, « recommandé », « dose »…) sans [Sn] ; une ligne de tableau est couverte par le [Sn] de sa légende ou de son en-tête | P1 bloquant | §4.1 |
| Point 11 appuyé seulement sur des sources de rang ≥ 4 ou inconnues | P1 bloquant | §4.2 |
| [Sn] cité mais absent de la section Sources ; source sans URL ou sans date | P1 bloquant | §4.10 |
| Source hors liste blanche | P2 | §4 |
| Fichier hors de la série de l'agent | refus, code 2 | §5.2 |

Code 1 = « DÉPÔT BLOQUÉ » : l'agent corrige avant de déposer.

### 3.5 PubMed — décision NCBI
- **Par défaut, sans clé :** 3 requêtes par seconde (limite NCBI), seau `ncbi` partagé par les deux agents, cache de 7 jours.
- **Clé facultative** par la variable d'environnement `NCBI_API_KEY` : 10 requêtes par seconde. La clé n'est jamais écrite dans un fichier, un journal ni une clé de cache. `NCBI_ADMIN_EMAIL` est transmis s'il est défini.
- **Serveur MCP local** (cyanheads/pubmed-mcp-server, sur la machine de Tunder) : `MCP_TRANSPORT_TYPE=http`, `MCP_HTTP_HOST=127.0.0.1`, `MCP_HTTP_PORT=3010`, `MCP_SESSION_MODE=stateless`, `MCP_AUTH_MODE=none` (acceptable car l'écoute reste locale), `STORAGE_PROVIDER_TYPE=filesystem`. Le script l'utilise s'il répond ; sinon il passe seul par les E-utilities. Le 24.10.2026, aucun serveur n'écoutait sur le port 3010 : le repli a été utilisé et vérifié.

---

## 4. Liste blanche validée

### 4.1 Méthode
`common/validate_allowlist.py` interroge chaque domaine candidat par `curl -L` (racine, ou point d'accès précis pour les API), puis classe le résultat :
- **valide** : HTTP 200 sans page de défi anti-robot → accès automatique autorisé ;
- **joignable, protégé contre les robots** : 401, 403, 412, 415, 429, ou page « Just a moment… » → **consultation manuelle seulement** (aucun contournement) ;
- **injoignable** : aucune réponse lors du test ;
- **rejeté** : le domaine répond mais n'est pas l'organisme visé (par exemple `sgg-ssg.ch`, association de seniors et non la société de gastro-entérologie, qui est `sggssg.ch`).

Résultat écrit dans `common/allowlist.json` et `common/LISTE_BLANCHE_VALIDEE.md`. La validation se relance par `python3 scripts_lots/common/validate_allowlist.py` ; les statuts « protégé contre les robots » varient d'un passage à l'autre pour quelques sociétés suisses.

### 4.2 Synthèse du 24.10.2026
| Rang | Domaines | Valides | Protégés (manuel) | Injoignables | Rejetés |
|---|---|---|---|---|---|
| 1 | 15 | 14 | 1 (`www.fmh.ch`) | 0 | 0 |
| 2 | 42 | 36 | 2 | 1 | 3 |
| 3 | 20 | 20 | 0 | 0 | 0 |
| 4 | 11 | 8 | 3 | 0 | 0 |
| 5 | 4 | 3 | 1 (`europepmc.org`) | 0 | 0 |
| **Total** | **92** | **81** | **7** | **1** | **3** |

### 4.3 Tableau complet
| Rang | Domaine | Organisme | Statut au 2026-10-24 | Accès automatique |
|---|---|---|---|---|
| 1 | `compendium.ch` | Compendium suisse des médicaments (HCI Solutions) | valide (HTTP 200) | oui |
| 1 | `download.swissmedicinfo.ch` | Refdata — téléchargement officiel AIPS (XML, CGU à accepter) | valide (HTTP 200) | oui |
| 1 | `fedlex.data.admin.ch` | Fedlex — données ouvertes (SPARQL, ELI) | valide (HTTP 200) | oui |
| 1 | `sl.bag.admin.ch` | OFSP — liste des spécialités (LS) | valide (HTTP 200) | oui |
| 1 | `www.bag.admin.ch` | OFSP / BAG — santé publique, vaccination, déclaration | valide (HTTP 200) | oui |
| 1 | `www.bfs.admin.ch` | OFS / BFS — statistiques de santé | valide (HTTP 200) | oui |
| 1 | `www.bsv.admin.ch` | OFAS / BSV — assurances sociales (AI, AVS) | valide (HTTP 200) | oui |
| 1 | `www.fedlex.admin.ch` | Fedlex — recueil systématique du droit fédéral | valide (HTTP 200) | oui |
| 1 | `www.infovac.ch` | Infovac — information vaccinale (HUG, mandat OFSP) | valide (HTTP 200) | oui |
| 1 | `www.obsan.admin.ch` | Obsan — observatoire suisse de la santé | valide (HTTP 200) | oui |
| 1 | `www.samw.ch` | ASSM / SAMW — directives médico-éthiques | valide (HTTP 200) | oui |
| 1 | `www.swissmedic.ch` | Swissmedic — listes officielles, autorisations | valide (HTTP 200) | oui |
| 1 | `www.swissmedicinfo.ch` | Swissmedic / Refdata — AIPS (information professionnelle) | valide (HTTP 200) | oui |
| 1 | `www.toxinfo.ch` | Tox Info Suisse | valide (HTTP 200) | oui |
| 1 | `www.fmh.ch` | FMH — Fédération des médecins suisses | joignable, protégé contre les robots (403) | non — consultation manuelle |
| 2 | `pharmasuisse.org` | pharmaSuisse — pharmaciens | valide (HTTP 200) | oui |
| 2 | `sgc-ssc.ch` | SSC / SGC — chirurgie | valide (HTTP 200) | oui |
| 2 | `sggssg.ch` | SSG / SGG — gastro-entérologie et hépatologie | valide (HTTP 200) | oui |
| 2 | `sgnor.ch` | SSMUS / SGNOR — médecine d'urgence et de sauvetage | valide (HTTP 200) | oui |
| 2 | `sgr-ssr.ch` | SSR / SGR — radiologie | valide (HTTP 200) | oui |
| 2 | `sgtm.ch` | SSMT / SGTM — médecine tropicale et des voyages | valide (HTTP 200) | oui |
| 2 | `ssai.ch` | SSAI / SGAI — allergologie et immunologie (identité à confirmer) | valide (HTTP 200) | oui |
| 2 | `ssi.guidelines.ch` | SSI — recommandations thérapeutiques en ligne | valide (HTTP 200) | oui |
| 2 | `swissurology.ch` | SSU / SGU — urologie | valide (HTTP 200) | oui |
| 2 | `www.chuv.ch` | CHUV — hôpital universitaire | valide (HTTP 200) | oui |
| 2 | `www.derma.swiss` | SSDV / SGDV — dermatologie et vénéréologie | valide (HTTP 200) | oui |
| 2 | `www.diabetesschweiz.ch` | diabètesuisse | valide (HTTP 200) | oui |
| 2 | `www.hug.ch` | HUG — hôpitaux universitaires de Genève | valide (HTTP 200) | oui |
| 2 | `www.insel.ch` | Inselspital — hôpital universitaire | valide (HTTP 200) | oui |
| 2 | `www.orl-hno.ch` | SSORL — ORL et chirurgie cervico-faciale | valide (HTTP 200) | oui |
| 2 | `www.psychiatrie.ch` | SSPP / SGPP — psychiatrie et psychothérapie | valide (HTTP 200) | oui |
| 2 | `www.sfgg.ch` | SFGG / SPSG — gériatrie | valide (HTTP 200) | oui |
| 2 | `www.sgaim.ch` | SSMIG / SGAIM — médecine interne générale | valide (HTTP 200) | oui |
| 2 | `www.sgedssed.ch` | SSED / SGED — endocrinologie et diabétologie | valide (HTTP 200) | oui |
| 2 | `www.sggg.ch` | SSGO / SGGG — gynécologie et obstétrique | valide (HTTP 200) | oui |
| 2 | `www.sgh-ssh.ch` | SSH / SGH — hématologie | valide (HTTP 200) | oui |
| 2 | `www.sginf.ch` | SSI / SGInf — infectiologie | valide (HTTP 200) | oui |
| 2 | `www.sgkjpp.ch` | SSPPEA / SGKJPP — pédopsychiatrie | valide (HTTP 200) | oui |
| 2 | `www.sgmo.ch` | SSOM / SGMO — oncologie médicale | valide (HTTP 200) | oui |
| 2 | `www.sog-sso.ch` | SSO / SOG — ophtalmologie | valide (HTTP 200) | oui |
| 2 | `www.ssapm.ch` | SSAPM — anesthésiologie et médecine périopératoire | valide (HTTP 200) | oui |
| 2 | `www.swisscardio.ch` | SSC / SGK — cardiologie | valide (HTTP 200) | oui |
| 2 | `www.swissnephrology.ch` | SSN / SGN — néphrologie | valide (HTTP 200) | oui |
| 2 | `www.swissneuro.ch` | SSN / SNG — neurologie | valide (HTTP 200) | oui |
| 2 | `www.swissnoso.ch` | Swissnoso — infections associées aux soins | valide (HTTP 200) | oui |
| 2 | `www.swissorthopaedics.ch` | swiss orthopaedics — orthopédie | valide (HTTP 200) | oui |
| 2 | `www.swisstph.ch` | Swiss TPH — institut tropical et de santé publique | valide (HTTP 200) | oui |
| 2 | `www.swisstransplant.org` | Swisstransplant | valide (HTTP 200) | oui |
| 2 | `www.unisante.ch` | Unisanté — médecine générale et santé publique | valide (HTTP 200) | oui |
| 2 | `www.unispital-basel.ch` | USB — hôpital universitaire | valide (HTTP 200) | oui |
| 2 | `www.usz.ch` | USZ — hôpital universitaire | valide (HTTP 200) | oui |
| 2 | `sgg-ssg.ch` | REJET attendu : association de seniors, hors champ | REJETÉ (domaine hors sujet) (200) | non — consultation manuelle |
| 2 | `www.paediatrieschweiz.ch` | SSP / Pädiatrie Schweiz — pédiatrie | injoignable lors du test (000) | non — consultation manuelle |
| 2 | `www.pneumo.ch` | SSP / SGP — pneumologie | joignable, protégé contre les robots (200) | non — consultation manuelle |
| 2 | `www.rheuma-net.ch` | SSR / SGR — rhumatologie | joignable, protégé contre les robots (200) | non — consultation manuelle |
| 2 | `www.sgsmp.ch` | REJET attendu : physique médicale, hors champ | REJETÉ (domaine hors sujet) (200) | non — consultation manuelle |
| 2 | `www.ssai-sgai.ch` | REJET attendu : domaine non médical | REJETÉ (domaine hors sujet) (200) | non — consultation manuelle |
| 3 | `eaaci.org` | EAACI — allergologie | valide (HTTP 200) | oui |
| 3 | `eacs.sanfordguide.com` | EACS — recommandations en ligne | valide (HTTP 200) | oui |
| 3 | `easl.eu` | EASL — hépatologie | valide (HTTP 200) | oui |
| 3 | `esgar.org` | ESGAR — radiologie digestive | valide (HTTP 200) | oui |
| 3 | `esvs.org` | ESVS — chirurgie vasculaire | valide (HTTP 200) | oui |
| 3 | `ueg.eu` | UEG — gastro-entérologie | valide (HTTP 200) | oui |
| 3 | `uroweb.org` | EAU — urologie | valide (HTTP 200) | oui |
| 3 | `www.eacsociety.org` | EACS — VIH | valide (HTTP 200) | oui |
| 3 | `www.ean.org` | EAN — neurologie | valide (HTTP 200) | oui |
| 3 | `www.easd.org` | EASD — diabète | valide (HTTP 200) | oui |
| 3 | `www.ecdc.europa.eu` | ECDC | valide (HTTP 200) | oui |
| 3 | `www.ema.europa.eu` | EMA | valide (HTTP 200) | oui |
| 3 | `www.erc.edu` | ERC — réanimation | valide (HTTP 200) | oui |
| 3 | `www.ersnet.org` | ERS — pneumologie | valide (HTTP 200) | oui |
| 3 | `www.escardio.org` | ESC — cardiologie | valide (HTTP 200) | oui |
| 3 | `www.escmid.org` | ESCMID — infectiologie | valide (HTTP 200) | oui |
| 3 | `www.ese-hormones.org` | ESE — endocrinologie | valide (HTTP 200) | oui |
| 3 | `www.eshonline.org` | ESH — hypertension | valide (HTTP 200) | oui |
| 3 | `www.esmo.org` | ESMO — oncologie | valide (HTTP 200) | oui |
| 3 | `www.eular.org` | EULAR — rhumatologie | valide (HTTP 200) | oui |
| 4 | `ginasthma.org` | GINA | valide (HTTP 200) | oui |
| 4 | `goldcopd.org` | GOLD | valide (HTTP 200) | oui |
| 4 | `kdigo.org` | KDIGO | valide (HTTP 200) | oui |
| 4 | `www.acc.org` | ACC (jamais seule, V7-Tunder §4.2) | valide (HTTP 200) | oui |
| 4 | `www.idsociety.org` | IDSA (jamais seule, V7-Tunder §4.2) | valide (HTTP 200) | oui |
| 4 | `www.ilcor.org` | ILCOR | valide (HTTP 200) | oui |
| 4 | `www.nice.org.uk` | NICE | valide (HTTP 200) | oui |
| 4 | `www.who.int` | OMS | valide (HTTP 200) | oui |
| 4 | `www.ahajournals.org` | AHA (jamais seule, V7-Tunder §4.2) | joignable, protégé contre les robots (403) | non — consultation manuelle |
| 4 | `www.cdc.gov` | CDC (jamais seule, V7-Tunder §4.2) | joignable, protégé contre les robots (403) | non — consultation manuelle |
| 4 | `www.cochranelibrary.com` | Cochrane | joignable, protégé contre les robots (412) | non — consultation manuelle |
| 5 | `eutils.ncbi.nlm.nih.gov` | NCBI E-utilities (API) | valide (HTTP 200) | oui |
| 5 | `pubmed.ncbi.nlm.nih.gov` | PubMed | valide (HTTP 200) | oui |
| 5 | `www.ebi.ac.uk` | Europe PMC (API REST) | valide (HTTP 200) | oui |
| 5 | `europepmc.org` | Europe PMC (site) | joignable, protégé contre les robots (403) | non — consultation manuelle |

---

## 5. Script synchrone — relecteur en direct, STRICTEMENT EN LECTURE SEULE

> **RÈGLE CARDINALE — LE SCRIPT SYNCHRONE NE PEUT JAMAIS CRÉER, MODIFIER, DÉPLACER, RENOMMER NI SUPPRIMER UN FICHIER DE LOT. CETTE GARANTIE EST TECHNIQUE ET PROUVÉE PAR DES TESTS.**

### 5.1 Commandes
`python3 scripts_lots/agent_N/script_synchrone.py <commande>`

| Commande | Effet |
|---|---|
| `review FICHIER.html [--appel-a FICHIER_A.html] [--sans-lt]` | Un passage complet ; retours `.json` et `.md` dans `output_dir/LOT_X/` |
| `watch DOSSIER_DU_LOT [--intervalle 5]` | Surveillance : nouveau passage après modification, anti-rebond de 60 s pour LanguageTool |
| `retours FICHIER.html` | Affiche le dernier retour |

Codes : 0 (aucun P1), 1 (P1 présent), 2 (refus : hors série ou isolation violée), 3 (alerte d'intégrité).

### 5.2 Garanties de lecture seule
1. **Un seul lecteur :** `lot_readonly.py` ouvre les fichiers de LOT par `os.open(O_RDONLY | O_NOFOLLOW)` ; tout descripteur est inapte à l'écriture (`EBADF`).
2. **Un seul écrivain gardé :** `lot_readonly.ecrire_sortie` refuse tout chemin hors du dossier de sortie ou situé dans un dossier de LOT ; le cache du relecteur passe par le même écrivain.
3. **Isolation vérifiée avant toute action :** le relecteur refuse de tourner (code 2) si `output_dir`, `cache_dir` ou `shared_state_dir` est dans le dossier du LOT ou dans `lots_root`, ou les contient. Aucun dossier n'est créé avant cette vérification.
4. **Empreintes SHA-256** de tous les fichiers du dossier du LOT avant et après chaque passage ; l'analyse porte sur un instantané. Une différence écarte le passage, écrit `ALERTE_*.md` dans le dossier de sortie et renvoie le code 3.
5. **Utilisateur système distinct ou montage en lecture seule (recommandé) :** sur la machine de Tunder, lancer le relecteur sous un utilisateur sans droit d'écriture sur les LOT (`sudo -u relecteur python3 …`, droits `r-x` par ACL), ou monter le dossier des LOT en lecture seule (`mount --bind -o ro`) ; avec `enforce_os_readonly: true`, le relecteur refuse de tourner si le LOT reste inscriptible pour lui.
6. **Aucun jeton, aucun commit, aucun envoi :** la seule sortie réseau est l'API LanguageTool, qui ne reçoit que du texte extrait.

### 5.3 Appliquer le prompt sans le réécrire
1. `v7_rules.py` lit le prompt V7-Tunder au démarrage : numéros de sections (§0 à §16 et leurs points numérotés) et **titres des 14 points du §6**.
2. Chaque retour cite une section qui **existe** dans le prompt chargé (vérifié à l'exécution et par test). Les règles de `rules_langue.json` portent chacune leur section.
3. Les seuils viennent du prompt : « 1 à 4 phrases » (§7.2), 90–200 Ko (§2), etc. Le script ne recopie ni ne reformule les règles.

### 5.4 Contrôles
| Famille | Détection | Section citée |
|---|---|---|
| Technique | DOCTYPE, FIN_FICHIER, taille, `title=`, scripts, tableaux enveloppés, lignes longues (logique `controle_v7.py`) | §2, §10, §11 |
| Sources | Porte `check` intégrée | §4.1, §4.2, §4.10 |
| 14 points | Présence, ordre, mot-clé du titre, par monographie (`<details open>`) | §6 |
| Volume | > 4 phrases dans le texte principal d'un point ou d'une sous-partie (9.a, 11.B…) → P1 ; phrase > 35 mots ; point sans fenêtre | §7.2, §8.1, §8.2 |
| Point 11 | 11.A–D, situations spéciales, critères de sortie, surveillance ; forme compliquée sans fenêtre « Urgence — conduite chronologique » | §14, §8.5, §16 |
| Points 3 et 9 | Tableau de corrélation ; sous-parties 9.a–9.d | §16, §6 |
| Langue | Remplissage (31 motifs), termes vagues hors phrase chiffrée (29), anglicismes avec équivalent (28), pléonasmes (28), abus de langage (18), connecteurs absents d'un raisonnement (28), phrase nominale probable, point décimal, `mg/dl`, guillemets droits | §7.3, §7.6, §0.5, §7.1, §7.8 |
| Abréviations | Non développées à la première occurrence | §7.4 |
| Cohérence DX | Liste de l'Appel A ↔ Parties | §9.5 |
| LanguageTool | Grammaire, accords, typographie (section 6) | §0.5 |

Chaque retour : gravité P1/P2/P3, section, lieu, message ≤ 25 mots, extrait. Le `.md` est plafonné pour économiser les jetons ; le détail complet reste dans le `.json`. Le relecteur ne propose aucun texte de remplacement et ne calcule aucun score.

### 5.5 Incrémentalité
Chaque monographie est hachée ; une monographie inchangée n'est pas réanalysée (cache `relecteur_segments.json`, dans `cache_dir`).

---

## 6. LanguageTool — API publique, usage sobre

**Constat.** L'API publique (`POST https://api.languagetool.org/v2/check`) admet 20 requêtes par minute et par adresse IP en pointe, 75 Ko par minute et 20 Ko par requête ; ses conditions déconseillent les requêtes automatisées. Ce risque est accepté par Vial ; l'usage reste ponctuel.

| Mesure | Mise en œuvre (`common/languagetool.py`) |
|---|---|
| Regroupement | Texte visible des monographies, découpé en blocs ≤ 18 000 octets aux frontières de phrase ; au plus 4 requêtes par passage |
| Cache par empreinte | SHA-256 du bloc ; un bloc inchangé n'est jamais renvoyé (cache par agent) |
| Budget partagé | **10 requêtes/min et 60 Ko/min pour les deux agents réunis** : seau à jetons dans `shared_state_dir/languagetool`, verrou `fcntl` |
| Anti-rebond | 60 s après la dernière modification en mode `watch` |
| Recul | 429 ou 503 : `Retry-After`, sinon 30 → 60 → 120 → 240 s, puis 15 min, partagé entre agents |
| Jamais bloquant | Indisponible, budget épuisé ou panne interne → « **NON VÉRIFIÉ** » avec la raison ; les contrôles locaux continuent |
| Repli facultatif | Instance auto-hébergée par simple changement de `languagetool.url` |

---

## 7. Compteur de jetons

### 7.1 Objet
Mesurer l'effet de la règle n° 1. **Les agents n'ont encore jamais tourné : aucun historique n'existe.** Le compteur distingue donc strictement :
1. **Messages de référence « sans la règle » — ESTIMATION**, tirée d'un scénario documenté et configurable ; jamais présentée comme une mesure.
2. **Messages autorisés réellement envoyés — MESURE**, journalisés par l'agent avant chaque envoi.
3. **Informations routées vers Tunder au lieu de l'utilisateur — MESURE.**
4. **Jetons économisés — ESTIMATION.**

### 7.2 Commandes (`scripts_lots/common/compteur_tokens.py`)
| Commande | Effet |
|---|---|
| `log --config agent_N/config.json --lot LOT_X --cas 1\|2\|3 --message "…"` | Journalise un message autorisé ; **refus (code 2)** au-delà de 15 mots, sur plusieurs lignes, ou pour un LOT hors série |
| `tunder --config … --lot LOT_X --resume "…"` | Journalise une information routée vers Tunder |
| `rapport --config agent_1/config.json --config agent_2/config.json [--format md\|json]` | Synthèse Markdown pour Tunder |

Journal CSV : `horodatage, agent, lot, cas, mots, caracteres, jetons_estimes, message` (cas `T` pour Tunder), dans `~/.scripts_lots/agent_N/COMPTEUR_TOKENS_AGENT_N.csv`, copié par l'agent dans `SUIVI_LOTS/COMPTEUR_TOKENS_AGENT_N.csv` à chaque coche.

### 7.3 Scénario de référence (ESTIMATION, modifiable dans `config.json`, clé `compteur`)
| Message qu'un agent aurait envoyé sans la règle | Par LOT |
|---|---|
| Annonce de début de LOT | 1 |
| Comptes rendus de recherche de sources | 6 |
| Appel A terminé | 1 |
| Parties 1 à 4 terminées | 4 |
| Corrections annoncées | 4 |
| Questions à l'utilisateur | 2 |
| Résumé de fin de LOT | 1 |
| **Total par LOT** | **19** |
| Fin de série | 2 |

Hypothèses : message type de 480 caractères ; jetons ≈ ⌈caractères / 4⌉ (approximation déterministe pour le français) = 120 jetons ; coût de relecture du contexte : 120 jetons par message.

**Formule :** jetons économisés (ESTIMATION) = (messages sans règle − messages envoyés) × (⌈480 / 4⌉ + 120). Exemple : 11 LOT terminés, 11 messages de cas 1 et 1 de cas 2 → (11 × 19 + 2 − 12) × 240 = 47 760 jetons estimés par agent.

---

## 8. Plans de secours

| Incident | Conduite | Trace |
|---|---|---|
| **GitHub indisponible** | Dépôt dans le dossier Drive « LOTS_Finaux avec statut » (identifiant `1DaFAd0uamsJQY2NH0ocuy2bhpfcVk9Vu`), en `text/html`, sans conversion ; resynchronisation vers `lot/LOT_X` dès le retour de GitHub | Fichier de suivi de l'agent |
| **LanguageTool indisponible** | « NON VÉRIFIÉ » pour la langue ; les autres contrôles continuent | Retour du relecteur |
| **Serveur PubMed local arrêté** | Repli automatique sur les E-utilities du NCBI | Champ `voie` et `note` de la réponse |
| **Site suisse indisponible ou protégé** | Source suivante du même rang, puis rang suivant, signalée ; copie en cache servie si elle existe | `POUR_TUNDER_AGENT_N.md` |
| **Script en panne** | L'agent continue de rédiger et note la panne ; Tunder audite à la main | `POUR_TUNDER_AGENT_N.md` |
| **Limite de débit atteinte** | Recul exponentiel automatique et partagé ; aucune relance en boucle | Code `LIMITE_DEBIT` |
| **Conflit sur un fichier de suivi** | Chaque agent ne touche qu'à ses propres fichiers ; nouvel essai après mise à jour de la branche, jamais `--force` | Historique Git |
| **Alerte d'intégrité (code 3)** | Passage écarté ; l'agent poursuit ; Tunder examine `ALERTE_*.md` | Dossier de sortie |

---

## 9. Tests, banc d'essai et essais réels

### 9.1 Suite de tests — `scripts_lots/lancer_tests.sh` : **27 tests, tous verts (24.10.2026, 5,3 s)**
| Fichier | Tests |
|---|---|
| `test_lecture_seule.py` | **(1) empreintes inchangées après 100 passages** et aucun fichier ajouté au LOT ; **(2) tentative d'écriture refusée** : descripteur `O_RDONLY` (`EBADF`), écrivain gardé, système (`PermissionError` sur LOT en lecture seule), mode strict `enforce_os_readonly` ; **(3) isolation du dossier de sortie** : sortie ou cache dans le LOT, ou LOT dans la sortie → refus, aucun dossier créé ; (4) LOT hors série refusé ; (5) LOT modifié pendant un passage → alerte, code 3 |
| `test_analyse_statique.py` | Aucune écriture directe dans le relecteur (analyse AST) ; aucune dépendance à une IA dans le code |
| `test_source.py` | `check` bloque une affirmation sans [Sn] (code 1) ; fichier sourcé accepté (code 0) ; [Sn] absent, source sans date ; point 11 sur rang 4 seulement ; LOT d'un autre agent refusé (code 2) ; liste blanche (rangs, HTTP refusé, domaine rejeté, domaine protégé) ; classement rang puis prise en charge ; extraction HTML |
| `test_relecteur.py` | 14 points lus dans le prompt ; chaque règle référencée ; fichier conforme sans P1 ; défauts détectés (point manquant, volume, terme vague, remplissage, anglicisme, affirmation non sourcée) ; LanguageTool injoignable → « NON VÉRIFIÉ » en < 10 s ; incrémentalité ; cohérence DX |
| `test_partage_et_config.py` | Seau partagé entre deux processus (capacité commune) ; recul partagé ; configurations disjointes (séries, caches, sorties) ; configuration invalide refusée ; compteur (refus > 15 mots, refus hors série, calculs) |

Les tests n'utilisent que des LOT fictifs créés par `tests/fabrique_lot.py` dans des dossiers temporaires, jamais un LOT réel, et aucun accès réseau.

### 9.2 Banc d'essai — `scripts_lots/banc/banc_essai.py` (LOT fictif LOT_230 dans `/tmp`, 5 fichiers de 111 Ko)
| Mesure | Résultat (médiane / max) | Cible |
|---|---|---|
| Relecture complète, cache froid | 243 ms | ≤ 10 s |
| Relecture incrémentale (aucune monographie modifiée) | 34 / 35 ms | ≤ 2 s |
| Relecture du LOT complet (5 fichiers) | 168 / 174 ms | — |
| Porte `check` | 14 / 15 ms | — |
| Empreintes SHA-256 du LOT | 0,5 / 0,7 ms | — |
| Indexation de 3 000 pages | 709 ms | — |
| Recherche sur 3 000 pages | 55 / 73 ms | ≤ 300 ms |
| Intégrité du LOT fictif après tous les passages | inchangé | inchangé |

### 9.3 Essais réels (24.10.2026, volumes minimaux)
| Essai | Résultat |
|---|---|
| `crawl` sur `www.bag.admin.ch`, `www.swissmedic.ch`, `www.sginf.ch` (12 pages, profondeur 1) | 12 pages indexées en 16,4 s, réparties sur les trois domaines, 0 erreur ; pages de recommandations favorisées |
| `search "vaccination adultes" --pec` | 2 résultats de rang 1 (OFSP), 0,5 ms |
| `extrait` OFSP « Vaccination des adultes » | Extrait verbatim avec date de consultation et `ligne_evidence` |
| `pubmed "hyponatremia management guideline"` | Serveur local absent → E-utilities : 3 résultats en 1,2 s (2 requêtes NCBI) ; second appel servi par le cache en 0,07 s |
| LanguageTool (1 requête) | 3 corrections pertinentes (faute de frappe, accord, ponctuation) ; second appel servi par le cache |
| Validation de la liste blanche | 92 domaines testés (section 4) |

---

## 10. Sécurité

1. **Aucun secret** dans les fichiers ; clé NCBI par variable d'environnement seulement, jamais en cache ni en journal.
2. **Moindre privilège :** les scripts ne détiennent aucun jeton GitHub, Drive ou autre ; ils ne font ni commit, ni envoi.
3. **Liste blanche** pour toute requête sortante ; HTTPS obligatoire ; redirections revérifiées ; adresses locales refusées, sauf le serveur PubMed `127.0.0.1:3010`.
4. **Contenus externes traités comme des données :** aucune instruction d'une page ou d'un PDF n'est exécutée ; les extraits sont renvoyés tels quels.
5. **Aucune écriture** dans les LOT, dans `PROMPT_V7_TUNDER/` ni dans les fichiers de suivi.
6. **Aucune dépendance** hors bibliothèque standard Python, `curl` et `pdftotext` ; **aucune IA**.

---

## 11. Décisions — points ouverts de la v1.2 résolus

| # | Point ouvert (v1.2) | Décision (v1.3) |
|---|---|---|
| 1 | Liste blanche suisse | Validée par `curl` le 24.10.2026 ; fichier `allowlist.json` et tableau section 4 |
| 2 | Conditions de Refdata (XML de l'AIPS) | Non acceptées à ce jour : aucun téléchargement massif ; l'AIPS est consultée page par page sur les domaines autorisés |
| 3 | Clé NCBI | **Sans clé par défaut** (3 req/s) avec cache ; clé facultative par `NCBI_API_KEY` (10 req/s) |
| 4 | Emplacement de dépôt | **Branche `lot/LOT_X`, dossier `LOTS/LOT_X/`** ; brouillons non audités autorisés ; Drive en plan B ; dépôt final après audit Tunder dans `LOT_Finaux_Audités` |
| 5 | LanguageTool | API publique, 10 req/min partagées, cache, recul, « NON VÉRIFIÉ » sans blocage (section 6) |

---

## 12. Modifications du V7-Tunder (minimales)

Fichier : `PROMPT_V7_TUNDER/PROMPT_ULTIME_PRODUCTION_LOTS_V7-Tunder.md`, comparé au V7 d'origine dans `diff.txt`.

| Section | Modification |
|---|---|
| En-tête | Mention des sections ajustées en conséquence |
| §2.4 | Dépôt GitHub `lot/LOT_X`, `LOTS/LOT_X/`, sans conversion ; Drive en plan B seulement |
| §5.3.5 | Audit des Parties pendant la phase différée Tunder ; dépôt des brouillons autorisé sans audit |
| §5.3.6 | Seuil de 90 % appliqué lors de l'audit Tunder, avant le dépôt final dans `LOT_Finaux_Audités` ; non applicable aux brouillons |
| §11.3 | Taille vérifiée sur le dépôt GitHub (ou Drive en plan B) |
| §13 | Dépôt GitHub principal, Drive plan B ; remplacement par nouveau commit ; jamais de suppression ni de `--force` |
| §14 | L'interdit vise le dépôt dans `LOT_Finaux_Audités` d'un fichier non audité ou sous 90 % |
| §15.1 | HELP dans `LOTS/HELP_QUESTIONNAIRE/` (Drive en plan B) |
| §16 | Audit et score ≥ 90 % exigés avant le dépôt final ; dépôt `.html` sur GitHub |

**Inchangés :** les 14 points, les §6.1 à §6.3 (section 6 identique octet pour octet au V7) et le texte du seuil de 90 %.
**Empreinte SHA-256 du V7-Tunder modifié :** `148fcf09f66ecae7129ba91ace68c8754ecbb3a2fb7edfa86621f4e5fb2a6abd`.

---

## 13. Utilisation et publication

1. Sur la machine de Tunder : `python3 /workspace/scripts_lots/agent_N/script_source.py …` et `…/script_synchrone.py …`.
2. Pour la publication dans le dépôt, le dossier `scripts_lots/` est copié tel quel ; seul `prompt_path` est à ajuster vers `PROMPT_V7_TUNDER/…`.
3. Serveur PubMed facultatif, sur la machine de Tunder : `MCP_TRANSPORT_TYPE=http MCP_HTTP_HOST=127.0.0.1 MCP_HTTP_PORT=3010 MCP_SESSION_MODE=stateless npx @cyanheads/pubmed-mcp-server` (version 2.10.23 relevée).
4. Recette : `scripts_lots/lancer_tests.sh`, puis `python3 scripts_lots/banc/banc_essai.py`.

---

## 14. Limites connues (honnêteté)

1. Les fonctions spécialisées envisagées en v1.2 (`aips_section`, `swissmedic_verifier`, `fedlex_article` par SPARQL, `pec_dossier`) **ne sont pas livrées** : l'AIPS, Fedlex et l'OFSP sont traités par l'exploration générique, la recherche et `extrait`.
2. `swissmedicinfo.ch` est une application dynamique : son contenu se lit mal par exploration ; l'AIPS se vérifie alors à la main, et la dose reste exigée depuis l'AIPS.
3. Sept domaines protégés contre les robots (dont `www.fmh.ch`, `www.cdc.gov`, `www.cochranelibrary.com`, `europepmc.org`) sont en consultation manuelle seulement ; `www.paediatrieschweiz.ch` était injoignable lors du test.
4. Les détections linguistiques sont heuristiques : elles signalent, elles ne jugent pas ; l'audit reste à Tunder.
5. Le serveur PubMed local n'a pas été démarré ; seul le repli E-utilities a été essayé.
6. L'exécution sous un utilisateur système distinct est documentée (section 5.2) mais non configurée sur la machine.
