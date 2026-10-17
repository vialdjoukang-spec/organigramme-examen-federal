# CONTINUATION · lecture obligatoire avant toute action

> Prompt de transition pour tout agent IA (Cursor, Claude, GPT, Grok…) sans contexte préalable.
> État figé le **17.10.2026 vers 23:25 (Europe/Zurich)**. Lis ensuite `HANDOFF.md` (sections les plus récentes en tête), `ETAT.md`, `journal/*.md`, les PR ouvertes (`gh pr list`) et `skills/ssp-*/SKILL.md` (miroir : `docs/skills/`).
> Si un fait ci-dessous contredit `gh pr list` ou `origin/main`, **le dépôt fait foi** : mets ce fichier à jour.

## 0. Projet en une ligne
« Organigramme Examen fédéral » : application d’étude en un fichier HTML pour l’examen fédéral suisse de médecine humaine (**CK** = connaissances cliniques, QCM ; **CS** = compétences cliniques, stations). 248 situations (SSP) du catalogue PROFILES.
- Dépôt : `vialdjoukang-spec/organigramme-examen-federal` · branche protégée `main` (PR + CI verte obligatoires).
- Fichier de travail : `app_v2.html` (constantes `SSP`, `TIP`, `NOT`, `GES`, `PRV`… injectées par scripts).
- En ligne : https://vialdjoukang-spec.github.io/organigramme-examen-federal/app_v2.html · progression : …/progres.html (recalcul toutes les 3 min).
- Titulaire : Vial (francophone, Europe/Zurich). Il valide les fautes critiques, les stations CS et les croquis.

## 1. Mission et priorités (17.10.2026)
**P1 · CK, différentiels des 248 SSP** (tout le reste est en PAUSE) :
1. **Prévalence** : à côté de chaque diagnostic différentiel (DD), au survol, le **% de prévalence suisse ou européen en rouge**, avec cadre (population, lieu) et source. DD **triés par probabilité décroissante**. Sans chiffre lu : « % à vérifier ». Ne jamais réécrire le texte DD existant (226/248 SSP en ont déjà) : ajouter le chiffre, trier, compléter les 22 SSP sans DD.
2. **Monographie au survol de chaque DD**, 7 rubriques, dans cet ordre :
   1. **Définition** · 2. **Épidémiologie** (chiffres + sex-ratio) · 3. **Physiopathologie** · 4. **Syndrome clinique** (signes majeurs) · 5. **Syndrome aux explorations** (examen + trouvaille) · 6. **Diagnostic** (ce qui pose formellement le diagnostic) · 7. **Prise en charge** : **But** / **Mesures générales** / **Pharmacologie** / **Autre**.
   - **Gras = titres seulement.** Juste après les deux-points : l’absolument utile. Phrases verbales concises. « Sans objet » si une rubrique ne s’applique pas (ex. conseil génétique).
   - Une monographie par diagnostic (clé normalisée), partagée par tous les SSP où il apparaît. Reprendre l’existant (TIP.d) dans la bonne rubrique, n’écrire que le manquant.
3. **Glossaire automatique** : tout terme médical, sémiologique ou spécialisé s’ouvre d’un clic sur une définition **très courte** (quelques mots), y compris dans une autre définition. Un terme non défini fait échouer la CI (Lyncée, baseline qui ne peut que baisser).

**En pause** (ne pas reprendre sans ordre de Vial) : nerfs crâniens (NC), stations CS (5 pilotes à relire par Vial), lots d’urgences CK, fond pâle (#32), présentation premium (#16), trauma S8 (#37), revues #39/#41, 27 signes et ~85 termes de Galien.

## 2. Règles non négociables
- **Sources** suisses ou européennes uniquement, **lues et datées** (« lu le JJ.MM.AAAA ») ; sinon « À vérifier ». **Ne jamais inventer** un chiffre, une dose, une référence, une image. Ligue pulmonaire suisse acceptée ; abcd.care / JBDS britannique refusé comme source principale ; GINA/GOLD jamais en source principale.
- **Doses** : uniquement l’AIPS suisse (information professionnelle). Méthode approuvée par Vial le 17.10.2026 : extraction **par script, mot pour mot**, depuis le téléchargement officiel Swissmedic/Refdata (conditions d’utilisation compatibles), **chaque ligne relue** à la main + `tools/doses_check.py` (tout nombre absent de l’extrait officiel est refusé). **Piège** : µ, ≥, ≤ en police symbole sur les pages officielles → noradrénaline lue « mg/min » au lieu de « µg/min » (facteur 1 000) ; le script corrige, vérifie toujours l’unité. **Scraping du Compendium exclu.** Pas dans l’AIPS (ex. fomépizole, silibinine IV) → « À vérifier ».
- **Justifier chaque examen et chaque traitement** (G8) : mécanisme → principe → moyen → pourquoi ce choix → limites.
- **Rouge = information critique seulement** (prévalence et « À ne pas manquer »). Fond très pâle, contraste élevé (AA). Images réelles uniquement, licence vérifiée.
- Fenêtres imbriquées, phrases complètes, français soigné.
- **Économie de jetons sans perte de qualité** : scripts déterministes pour le mécanique ; jugement clinique et audit par écrit, jamais automatisés à l’aveugle.
- **Communication concise** (Vial veut l’essentiel ; jauges = barres seules, sans commentaire).
- **Aucune donnée personnelle dans ce dépôt public** : ni détail de décision d’autorité, ni paiement, ni contenu de localStorage, ni courriel. Les PDF sources restent hors dépôt.
- **Ne jamais modifier `/workspace/ssp/app.html`** (référence, empreinte contrôlée par la CI).
- Faute médicale **critique** : la signaler en rouge en tête du rapport ; sa correction attend l’accord de Vial avant fusion.
- Fusion : commit de fusion (`--merge`), jamais squash, jamais force-push d’une branche de PR labellisée, jamais affaiblir la protection de `main`.

## 3. Organisation : deux chaînes en sens opposé, chaque rédacteur suivi de son auditeur
| Chaîne | Rédacteur | Sens | Auditeur suiveur |
|---|---|---|---|
| Monographies A | Hygie | du 1er SSP vers l’avant (G1 →) | Hérophile |
| Monographies B | Panacée | du dernier SSP vers l’arrière (O7.26 ←) | Érasistrate |
| Prévalences | Asclépios | groupes G1… | Galien (médical + linguistique) |
| Doses | Pharmakon | AIPS verbatim → `data/ck/doses_ch.json` | Galien |
| Glossaire | Lyncée | termes non définis, balisage auto | contrôle CI |
| Affichage / CI | Iris | contrôle visuel, CLS, captures | — |

Les deux rédacteurs de monographies ne prennent jamais le même diagnostic (réservation par lot dans la PR). L’auditeur audite chaque lot **quelques minutes** après la livraison, corrige directement sur la branche de la PR, consigne dans `audit/RAPPORT_AUDIT_MEDICAL.md` (« les fautes corrigées »), puis pose `audit-ok`.

**Fusion-publication automatique** : label `audit-ok` → `.github/workflows/auto-fusion.yml` met la branche à jour (`update-branch`, sans force-push) et active l’auto-merge en commit de fusion ; GitHub fusionne quand `garde`, `html`, `tests`, `visuel` sont verts ; `pages-apres-fusion.yml` relance `pages.yml` (Pages). **État : cassé** (voir § 5).

**Jauges** : `/workspace/ssp/jauge/binomes.py` (hors dépôt, zéro jeton) lit `origin/main` et imprime deux barres (prévalences, monographies, + audités). Envoyer à Vial **à chaque palier de +20 %**, barres seules. `progres.html` en est le portage JS public.

## 4. Flux de travail
1. **Un worktree git par agent**, créé depuis `origin/main` : `git -C /workspace/oef fetch && git -C /workspace/oef worktree add -b <branche> /workspace/oef-<agent> origin/main`. **Ne jamais changer de branche dans `/workspace/oef`.**
2. **Petits lots, une PR par lot.** Le rédacteur **ne fusionne jamais** ; l’auditeur corrige sur la branche et pose `audit-ok`. Ordre imposé quand les lots se chevauchent (ex. #50 → #53 → #54 → #64).
3. **Conflits de shards `data/ck/mono/*.json`** : jamais à la main. `git merge origin/main`, puis `python3 /workspace/hippo_work/merge_shards.py <fichiers en conflit>` (fusion 3 voies clé par clé), puis `python3 tools/mono_build.py` (assets régénérés). Idem prévalence : `python3 tools/prev_build.py`. Conflit dans `app_v2.html` : reprendre la version de main et rejouer le patch (skill `ssp-fusion-patch`). `audit/RAPPORT_AUDIT_MEDICAL.md` en add/add : **garder toutes les sections**.
4. **Playwright seulement sous verrou** : `flock /tmp/oef-playwright.lock …`, venv `/workspace/venv_ck`, `CHROME_PATH=/home/box/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell`. ~15 Go de RAM sans swap : **pas de Blender** (OOM), pas de navigateurs parallèles.
5. **Commit + push après chaque étape** ; mettre à jour ta section de `HANDOFF.md` (modèle : État / Prochaine / Sources / Pièges / À vérifier) et ton `journal/*.md`. **Arrête-toi avant que ton contexte devienne gros** : écris la relève, puis termine.
6. Captures et tests d’affichage en fin de tâche (`python3 tests/run_tests.py`, `tests/visuel/`).
7. Fusion manuelle autorisée (permission permanente de Vial) quand la CI est verte et l’audit fait : `gh pr merge N --merge --match-head-commit <sha>`.

## 5. État courant (17.10.2026 ~23:25, à revérifier par `gh pr list`)
**Sur main** (1ead0fd) : infrastructure monographies (patch 0026, `assets/mono/`), Hygie lot 1 (G1, 14 DD), Panacée lot 1 (O7.26–O7.24, 27 DD), `progres.html`, auto-fusion v1 + correctif Pages. **Aucune prévalence sur main.**

**PR ouvertes**
| PR | Objet | État |
|---|---|---|
| #42 | Prévalence : infrastructure (prev.json, contrôle P1–P7, % rouge, tri, patch 0020) | audit-ok ; visuel en attente ; **à fusionner en premier** |
| #43 · #44 · #45 | Prévalence G1 thorax · G2 dyspnée · G3 abdomen (audités par Galien) | audit-ok ; DIRTY (rebâtir sur main après #42) |
| #58 | Prévalence G4 fièvre (G6) + syncope (F1.19) | DIRTY ; audit Galien à faire |
| #47 | Rapport d’audit Galien (prévalences) | BEHIND |
| #49 | Hérophile : audit Hygie lot 1 + Panacée lot 1 (150 corrections) | audit-ok |
| #50 · #53 · #54 · #64 | Hygie lots 2 (G2) · 3 (G3+G4) · 4 (G5+G6) · 5 (G7+G8) | audités ; audit-ok sur #50 seulement ; ordre #50→#53→#54→#64 ; visuel rouge |
| #55 · #60 · #62 | Panacée lots 2–4 (O7.23 → O7.15), audités par Érasistrate (182 corrections) | audit-ok ; BEHIND/BLOCKED |
| #59 · #61 · #67 | Pharmakon : doses AIPS lots 1–3 | #59 audit-ok ; #61, #67 audit Galien à finir |
| #63 | auto-fusion via GraphQL (sans git local) | CI en cours ; **réparation de l’auto-fusion** |
| #66 | visuel : polices auto-hébergées, CLS stable (cause du visuel rouge des monographies) | CI en cours ; **débloque les PR monographies** |
| #65 | Lyncée 2 : glossaire automatique (monographies dans G4) | CI verte, BLOCKED (à jour/revue) |
| #56 | sonde e2e de l’auto-fusion | test ; fermer après preuve |
| #39 · #41 · #37 · #32 · #16 | NC/TIP Galien, trauma S8, fond pâle, premium | **en pause** |

**Ordre de fusion recommandé** : #66 (visuel) → #63 (auto-fusion) → #42 → #43 → #44 → #45 → #47 → #58 · #49 → #50 → #53 → #54 → #64 · #55 → #60 → #62 · #59 → #61 → #67 · #65. Après chaque fusion, les suivantes fusionnent `origin/main` + rebuild (§ 4.3).

**Blocages connus**
1. `auto-fusion.yml` échoue (`gh pr merge --auto` sans checkout ni `GH_REPO` : « not a git repository ») → #63. Les commits de fusion du bot déclenchent des CI « action_required » (contourné par un commit vide).
2. Contrôle `visuel` rouge sur les PR de monographies (CLS bureau 0,13–0,17 > plafond 0,144) → #66 d’Iris.
3. Cartes d’approbation à chaque `git push` / création de PR (règle Auto-review de l’environnement Grok Bot). Vial peut ajouter une règle autorisant les push sur `feat/*` de ce dépôt.
4. Doses : la plupart des monographies portent « À vérifier (AIPS) » tant que #59/#61/#67 ne sont pas fusionnées ; ~moitié des chiffres épidémiologiques encore « à vérifier ».
5. Galien : 72 textes DD commencent par « À ne pas manquer.</b> » sans balise ouvrante (rouge perdu) → script rejouable après les groupes d’Asclépios.

**Lot suivant de chaque chaîne**
- Hygie : prurit + douleur (≈30 DD), après rattrapage d’Hérophile et fusion qui marche.
- Panacée : O7.14 et en arrière, après fusion de #55/#60/#62.
- Asclépios : vertige, toux, lombalgie, malaise (après fusion de #42).
- Pharmakon : tous les médicaments cités dans les monographies, revérification des unités.
- Lyncée : termes les plus fréquents d’abord.

**Jauges (`binomes.py`, origin/main, 17.10.2026 ~23:25)**
```
Prévalences   ░░░░░░░░░░    0 %  (0/2578 · audités 0)
Monographies  ░░░░░░░░░░    2 %  (41/2280 · audités 0)
```
(≈115 monographies et 34 prévalences écrites sur branches, non fusionnées.)

## 6. Commandes et fichiers
| Chemin | Rôle (2 lignes) |
|---|---|
| `tools/mono_build.py` | `data/ck/mono/<lettre>.json` → `assets/mono/mono-<lettre>.js`. `--check` (CI : structure, gras, doses, assets à jour) ; `--draft <SSP>` imprime l’existant TIP.d. |
| `tools/prev_build.py` (+ `tools/audit/prevalence.py`) | `data/ck/prev.json` → constante `PRV` + `assets/ck/prev.js`. `--check` en CI ; ne jamais retoucher `PRV` à la main. *(branche #42)* |
| `tools/doses_check.py` | Contrôle `data/ck/doses_ch.json` : extrait AIPS verbatim, url, versions, dates, chaque nombre présent dans l’extrait. *(branches #59/#61/#67)* |
| `tools/ck_build.py` / `tools/ck_common.py` | Compile `data/ck/*.json` (src, glo, sig, syn, hyp, loc, nc) → `assets/ck/*.js` ; `--check` en CI. |
| `tools/lyncee.py` + `qa/termes-baseline.json` | Recense les termes non définis ; la baseline ne peut que baisser. |
| `tools/json_inject.py`, `tools/_app.py`, `tools/patches/` | Injection des constantes dans `app_v2.html` ; patches à ancrage unique, rejouables (skill `ssp-patch`). |
| `tools/audit/rapport_fautes.py`, `tools/aletheia.py` | Audit niveau 1 (G1–G8), registre des fautes, blocage d’une faute critique. |
| `tools/cs_build.py`, `tools/build_mem.py`, `tools/build_exi.py` | Stations CS, Mémorisation, Exigences (en pause sauf maintenance). |
| `tests/run_tests.py`, `tests/test_*.py`, `tests/visuel/` | Suite complète (241+) ; captures et comparaison visuelle (CLS). |
| `/workspace/ssp/jauge/binomes.py` | Deux jauges (prévalences, monographies) depuis `origin/main`, déterministe. `--json`, `--check`. |
| `/workspace/ssp/jauge/contenu.py` | Compteur du contenu didactique CK/CS (seuils fixes). |
| `/workspace/hippo_work/` | Outils d’audit : `merge_shards.py`, `newmono.py`, `autosrc.py`, `fix_*.py`, `poll_*.sh`, `HANDOFF_{GALIEN,HEROPHILE,ERASISTRATE}.md`. |
| `data/ck/` | `mono/`, `prev.json`, `doses_ch.json`, `src.json` (toute source citée doit y être), `glo.json`, `schema/`. |
| `audit/RAPPORT_AUDIT_MEDICAL.md` | Rapport public « les fautes corrigées » (une section par lot). |
| `skills/ssp-*/SKILL.md` (= `docs/skills/`) | Procédures : `ssp-continuite` (relève), `ssp-verite` (sources), `ssp-posologie-suisse` (doses), `ssp-patch`/`ssp-fusion-patch`, `ssp-json-data`, `ssp-tests`, `ssp-audit-medical`, `ssp-signe-infobulle`, `ssp-revue-diff`, etc. |

## 7. Sauvegardes
- Toutes les branches poussées sur GitHub ; travaux en pause dans `wip/*` (urgences lot 3, fragments d’examen).
- Archive locale complète (branches, travaux non terminés, relèves, scripts des jauges et des doses) : `/cursor/stores/store-e5265852-6589-40c1-aa67-8de61d5486d9/sauvegardes/` (ex. `20261017-2317/`). La branche trauma S8 (`feat/trauma-ddx`, conflits non résolus) n’existe complète que là.
- Copie de ce fichier : `/workspace/CONTINUATION.md` et le store ci-dessus.

## 8. Cinq premières actions d’un agent neuf
1. Lire ce fichier, `HANDOFF.md` (tête), `ETAT.md`, ton `journal/*.md`, les `skills/ssp-*` de ton rôle ; `git -C /workspace/oef fetch`.
2. Faire l’état réel : `gh pr list --state open`, `gh pr checks <N>`, `python3 /workspace/ssp/jauge/binomes.py` ; corriger le § 5 si besoin.
3. Débloquer avant de produire : #66 (visuel) puis #63 (auto-fusion), puis fusionner dans l’ordre du § 5 (rebuild des shards, jamais à la main).
4. Créer ton worktree depuis `origin/main` et reprendre **le lot suivant de ta chaîne** (§ 5), petit lot, une PR, sans fusion par le rédacteur.
5. Commit + push à chaque étape, section `HANDOFF.md` à jour, jauges envoyées à chaque +20 % ; t’arrêter proprement avant un contexte trop gros.
