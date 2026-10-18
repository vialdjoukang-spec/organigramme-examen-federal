# CONTINUATION · lecture obligatoire, en entier, avant toute action

> **Pour Codex (OpenAI) et tout agent IA sans mémoire longue.** Ce fichier est ta feuille de route complète, de l’installation jusqu’à la fin du projet.
> Tu ne commences **aucun** travail de contenu avant d’avoir lu ce fichier **en entier** et terminé l’**Étape 0** : `python3 tools/porte.py commencer 1` refuse tant que la porte n’est pas complète.
> Chaque session : lis `AGENTS.md` → `PROCHAINE_ACTION.md` → `ETAT.json` (`python3 tools/porte.py etat`) → la section de l’étape courante ci-dessous → travaille → `python3 tools/porte.py terminer`.
> État figé le **17.10.2026 à 23:30 (Europe/Zurich)**, revu le **18.10.2026 00:45**. Si un fait contredit `gh pr list` ou `origin/main`, **le dépôt fait foi** : corrige ce fichier dans ta PR.

## Ordre courant de Vial · 18.10.2026
Étape9 prioritaire ; étape8 en parallèle par les scripts catégoriels G/S/F/O. Lot2 G10 : compression médullaire et ischémie aiguë/dissection, deux fiches et cinq définitions, 253/2287 monographies sur branche ; CI/audit/fusion/publication exacts requis. G10 5/14 après intégration ; neuf autres restent dus. Recherche parallèle39155482602 réussie techniquement sur160 diagnostics ; résultats partiels, aucune nouvelle prévalence admise. Les étapes en boucle restent ouvertes ; le protocole Gardien reste annulé.

## Feuille de route (vue d’ensemble, dans l’ordre jusqu’à la fin)

| Étape | Objet | Fin quand… | Modèle | Suivante |
|---|---|---|---|---|
| **0** | Installation et porte (bloquante) : lecture, catalogue, proposition de skills, veille, droits | `porte.py verifier0` = 0 | défaut | 1 |
| **1** | État réel, sauvegardes, jauges | § 1 rempli, ETAT.md à jour | défaut | 2 |
| **2** | Réparer la fusion-publication automatique et le contrôle `visuel` | une PR test fusionne et publie seule | défaut | 3 |
| **3** | Files des prévalences #43 → #44 → #45 → #58 et du rapport #47 | toutes fusionnées | défaut | 4 |
| **4** | Files des monographies Hygie #50 → #53 → #54 → #64 et d’Hérophile #49 | toutes fusionnées | défaut | 5 |
| **5** | File des monographies Panacée #60 → #62 | toutes fusionnées | défaut | 6 |
| **6** | File des doses #59 → #61 → #67 → #70 et doutes de doses | toutes fusionnées, doutes tranchés ou « À vérifier » | défaut | 7 |
| **7** | File du glossaire #65 → #68 | toutes fusionnées | défaut | 8 |
| **8** | Prévalences en rouge des 248 SSP, 22 SSP sans différentiel (boucle par lot) | jauge Prévalences = 100 % | **GPT 6 Luna** | 9 |
| **9** | Monographies en 7 rubriques, deux chaînes opposées (boucle par lot) | jauge Monographies = 100 % | **GPT 6 Luna** | 10 |
| **10** | Doses AIPS, lot 5 et suivants (boucle) | chaque dose citée est dans `doses_ch.json` ou « À vérifier » | **GPT 6 Luna** | 11 |
| **11** | Glossaire automatique : définition très courte au clic (boucle) | baseline Lyncée = 0 terme non défini | **GPT 6 Luna** | 12 |
| **12** | Finitions P1 : « À ne pas manquer », balayage « À vérifier », audit final | rapport final d’audit fusionné | défaut | 13 |
| **13** | Nerfs crâniens (`feat/nc07-voie-motrice`, #39) | PR fusionnées | défaut | 14 |
| **14** | Stations CS (boucle) | stations des SSP prioritaires écrites, auditées | **GPT 6 Luna** | 15 |
| **15** | Lots d’urgences CK (#41, lot 3, boucle) | lots fusionnés | **GPT 6 Luna** | 16 |
| **16** | PR en pause : #32 fond pâle, #37 trauma S8, #16 présentation | fusionnées ou fermées avec motif | défaut | 17 |
| **17** | Clôture : vérification, publication, rapport final à Vial | site public = main, jauges 100 % | défaut | fin |

La même liste existe pour les machines dans `tools/etapes.json` (titres, critères, boucles, modèle, chaînes de PR). **Ne saute jamais une étape** ; si une étape est bloquée par un obstacle extérieur, consigne-le (§ R7) et passe à la suivante : la veille et la file de fusion reprendront l’étape bloquée.

---

## Partie A · Le projet, les règles, l’organisation

### A1. Projet en une ligne
« Organigramme Examen fédéral » : application d’étude en **un fichier HTML** pour l’examen fédéral suisse de médecine humaine (**CK** = connaissances cliniques, QCM ; **CS** = compétences cliniques, stations). **248 situations (SSP)** du catalogue PROFILES.
- Dépôt : `vialdjoukang-spec/organigramme-examen-federal` (public) · branche protégée `main` (PR + contrôles requis `garde`, `html`, `tests`, `visuel`, branche à jour « strict », règles appliquées aussi aux admins).
- Fichier de travail : `app_v2.html` (constantes `SSP`, `TIP`, `NOT`, `GES`, `PRV`… injectées par scripts, jamais à la main).
- En ligne : https://vialdjoukang-spec.github.io/organigramme-examen-federal/app_v2.html · progression : https://vialdjoukang-spec.github.io/organigramme-examen-federal/progres.html (recalcul toutes les 3 min).
- Titulaire : **Vial** (francophone, Europe/Zurich). Il valide les fautes critiques, les stations CS et les croquis. Il veut l’essentiel, sans bavardage.

### A2. Mission et priorités (ordre de Vial du 17.10.2026)
**P1 · CK, différentiels des 248 SSP** :
1. **Prévalence** : à côté de chaque diagnostic différentiel (DD), dans la fenêtre au survol, le **% de prévalence suisse ou européen en ROUGE**, avec cadre (population, lieu) et source. DD **triés par probabilité décroissante**. Sans chiffre lu : « % à vérifier ». **Ne jamais réécrire le texte DD existant** (226/248 SSP en ont déjà) : ajouter le chiffre, trier, et écrire les DD des **22 SSP qui n’en ont pas**.
2. **Monographie au survol de chaque DD**, 7 rubriques, dans cet ordre :
   1. **Définition** · 2. **Épidémiologie** (chiffres + sex-ratio) · 3. **Physiopathologie** · 4. **Syndrome clinique** (signes majeurs) · 5. **Syndrome aux explorations** (examen + trouvaille) · 6. **Diagnostic** (ce qui pose formellement le diagnostic) · 7. **Prise en charge** : **But** / **Mesures générales** / **Pharmacologie** / **Autre**.
   - **Gras = titres seulement.** Juste après les deux-points : l’absolument utile. **Phrases verbales concises.** « Sans objet » si une rubrique ne s’applique pas (situation non morbide, ex. conseil génétique).
   - Une monographie par diagnostic (clé normalisée), partagée par tous les SSP où il apparaît. Reprendre l’existant (TIP.d) dans la bonne rubrique (`tools/mono_build.py --draft <SSP>`), n’écrire que le manquant. Du 1er SSP au dernier, vite.
3. **Glossaire automatique** : tout terme médical, sémiologique ou spécialisé s’ouvre d’un clic sur une définition **très courte** (quelques mots), y compris dans une autre définition. Vial ne doit **jamais** avoir à chercher une définition sur internet. Un terme non défini fait échouer la CI (Lyncée, baseline qui ne peut que baisser).

**Après P1** (Étapes 13–16, dans cet ordre) : nerfs crâniens (NC), stations CS (5 pilotes à relire par Vial), lots d’urgences CK, fond pâle (#32), trauma S8 (#37), revues #39/#41, présentation premium (#16), 27 signes et ~85 termes de Galien.

### A3. Règles non négociables (R1–R15)
- **R1 · Sources** suisses ou européennes uniquement, **lues et datées** (« lu le JJ.MM.AAAA ») ; sinon « À vérifier ». **Ne jamais inventer** un chiffre, une dose, une référence, une image. Ligue pulmonaire suisse acceptée ; abcd.care / JBDS britannique refusé comme source principale ; GINA/GOLD jamais en source principale. Toute source citée doit exister dans `data/ck/src.json`.
- **R2 · Doses** : uniquement l’**AIPS suisse** (information professionnelle). Méthode approuvée par Vial le 17.10.2026 : extraction **par script, mot pour mot**, depuis le téléchargement officiel Swissmedic/Refdata, **chaque ligne relue** à la main + `tools/doses_check.py` (tout nombre absent de l’extrait officiel est refusé). **Piège des polices** : µ, ≥, ≤ en police symbole sur les pages officielles → noradrénaline lue « mg/min » au lieu de « µg/min » (facteur 1 000) ; vérifie **toujours l’unité**. **Le Compendium (compendium.ch) est exclu** (ni lecture automatisée, ni source). Pas dans l’AIPS → « À vérifier (AIPS) ». Skill `ssp-posologie-suisse`.
- **R3 · Justifier chaque examen et chaque traitement** (G8) : mécanisme → principe → moyen → pourquoi ce choix → limites.
- **R4 · Rouge = information critique seulement** (prévalence % et « À ne pas manquer »). **Fond très pâle, contraste élevé** (WCAG AA). Images réelles uniquement, licence vérifiée (skill `ssp-images-licence`).
- **R5 · Style** : fenêtres imbriquées, phrases complètes et verbales, concises, français soigné. Gras réservé aux titres de rubrique.
- **R6 · Audit agressif juste derrière chaque rédacteur** : chaque lot est relu (médical, sources, langue) **quelques minutes** après sa livraison, corrigé directement sur la branche de la PR, consigné dans `audit/RAPPORT_AUDIT_MEDICAL.md` (« les fautes corrigées », une section par lot), puis label `audit-ok`. Le rédacteur ne fusionne jamais son propre lot sans cet audit. Skill `ssp-audit-medical`.
- **R7 · Ne jamais s’arrêter devant un obstacle : c’est interdit.** Un échec (fusion, publication, CI, réseau, source illisible) se consigne (`journal/echecs_fusion.md`, ETAT.md, « À vérifier ») et le travail **continue** avec le lot ou l’étape suivante. La file de fusion (`tools/file_fusion.sh`) réessaie seule.
- **R8 · Tâches répétitives : ordre de Vial, elles utilisent le modèle « GPT 6 Luna »** (`gpt-6-luna`). Si ce modèle n’est pas disponible, utilise le modèle le moins cher disponible pour le travail en masse et **note-le dans ETAT.md** (section « Notes modèle »). Jugement non répétitif (réparations, conflits, décisions) : modèle par défaut.
- **R9 · Économie de jetons sans perte de qualité** : scripts déterministes pour le mécanique ; jugement clinique et audit par écrit, jamais automatisés à l’aveugle. Petits lots.
- **R10 · Communication concise** : jauges = barres seules, sans commentaire, envoyées à **chaque palier de +20 %** (`python3 tools/jauge/binomes.py`, copie de `/workspace/ssp/jauge/binomes.py`).
- **R11 · Aucune donnée personnelle dans ce dépôt public** : ni détail de décision d’autorité (MEBEKO), ni paiement, ni contenu de localStorage, ni courriel. Les PDF sources restent hors dépôt (`prive/`, `*.local.*` sont ignorés par git).
- **R12 · Ne jamais modifier `/workspace/ssp/app.html`** (référence, empreinte contrôlée par la CI `garde`).
- **R13 · Faute médicale critique** : la signaler en rouge en tête du rapport, poser le label `attente-vial` (la file de fusion la saute) ; sa correction attend l’accord de Vial avant fusion.
- **R14 · Fusion** : commit de fusion (`--merge`), jamais squash, jamais force-push d’une branche de PR, jamais `--admin` pour contourner, jamais affaiblir la protection de `main`. Permission permanente de Vial : fusionner soi-même **après audit et CI verte**.

- **R15 · Garde-fous (ordre de Vial, 18.10.2026)** : « Codex doit être libre, indépendant de tout PC ». La veille permanente est **GitHub Actions** (gratuit, dépôt public), plus aucun PC :
  - `garde-progres.yml` toutes les **5 min** (`tools/garde/progres.py`) mesure le contenu réel de `main` (prévalences, monographies, lignes de doses, glossaire). **STALL** = aucun compteur monté en **15 min**, ou seulement des PR de relevé : `@codex` sur la PR brouillon **« Pilote Codex »** (≤ 1 relance / 15 min) ; après **4 stalls consécutifs (environ 60 min)**, `@vialdjoukang-spec` (courriel, ≤ 1 / 60 min). Il recycle aussi chaque PR sans commit depuis **60 min** (`tools/garde/recyclage.py` : « reprends ou ferme avec motif », ne ferme rien).
  - `checkpoint.yml` (`tools/garde/checkpoint.py`) sur chaque PR : section **« Automates actifs »** obligatoire dans le corps (scripts/skills/MCP existants), interdit de déclarer finie une étape en boucle (8–11, 14, 15) sans données de contenu, aucune dose sans ligne `data/ck/doses_ch.json`. En cas d’échec, l’ordre de correction t’est posté avec `@codex`.
  - `appel-vial.yml` : étiquette `attente-vial` → une ligne à Vial sur « Pilote Codex » (courriel) **et** `@codex` : continue ailleurs, n’attends **jamais** Vial.
  - **Début de chaque session** : affiche `python tools/garde/checkpoint.py --inventaire` (tes automates actifs) ; recopie ceux que tu utilises dans « Automates actifs » de ta PR.
  - **Un relevé seul ne termine jamais une étape en boucle** ; seul le critère automatique (`porte.py`) la clôt.
  - Seuils en minutes, modifiables sans code : `tools/garde/config.json`. État anti-spam : branche `garde/etat`. `veille_relance.sh` devient **facultatif**.

### A4. Organisation : deux chaînes en sens opposé, chaque rédacteur suivi de son auditeur
Les noms sont des **rôles** ; seul, Codex les joue l’un après l’autre (rédiger un lot → l’auditer aussitôt en relecteur agressif → `audit-ok`). En parallèle (plusieurs sessions Codex), une session = un rôle, un worktree.

| Chaîne | Rédacteur | Sens | Auditeur suiveur |
|---|---|---|---|
| Monographies A | Hygie | du 1er SSP vers l’avant (G1 →) | Hérophile |
| Monographies B | Panacée | du dernier SSP vers l’arrière (O7.26 ←) | Érasistrate |
| Prévalences | Asclépios | groupes G1, G2… | Galien (médical + linguistique) |
| Doses | Pharmakon | AIPS verbatim → `data/ck/doses_ch.json` | Galien |
| Glossaire | Lyncée | termes non définis, balisage auto | contrôle CI |
| Affichage / CI | Iris | contrôle visuel, CLS, captures | — |

Les deux chaînes de monographies ne prennent jamais le même diagnostic (réservation du lot dans le titre et le corps de la PR) ; elles s’arrêtent quand elles se rejoignent.

### A5. Flux de travail (toutes étapes)
1. **Un worktree git par session**, créé depuis `origin/main` : `git -C /workspace/oef fetch && git -C /workspace/oef worktree add -b <branche> /workspace/oef-<role> origin/main` (hors box Grok : un clone suffit, une branche par lot). **Ne jamais changer de branche dans `/workspace/oef`.**
2. **Petits lots, une PR par lot.** Titre : « <Rôle> · <objet> lot N (<SSP/DD>) ». Corps : liste réservée, sources lues, « À vérifier », résultat des tests.
3. **Conflits de shards `data/ck/mono/*.json`** : jamais à la main. `git merge origin/main`, puis `python3 tools/merge_shards.py <fichiers en conflit>` (fusion 3 voies clé par clé ; voir § C3), puis `python3 tools/mono_build.py` (assets régénérés). Prévalence : `python3 tools/prev_build.py`. Conflit dans `app_v2.html` : reprendre la version de main et rejouer le patch (skill `ssp-fusion-patch`). `audit/RAPPORT_AUDIT_MEDICAL.md` en add/add : **garder toutes les sections**.
4. **Playwright** : sur la box Grok, seulement sous verrou `flock /tmp/oef-playwright.lock …`, venv `/workspace/venv_ck`, `CHROME_PATH=/home/box/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell`. ~15 Go de RAM sans swap : **pas de Blender** (OOM), pas de navigateurs parallèles.
5. **Commit + push après chaque lot** ; mettre à jour `HANDOFF.md` (section en tête, modèle : État / Prochaine / Sources / Pièges / À vérifier), ton `journal/*.md` et la ligne du journal des étapes d’ETAT.md. **Arrête la session avant que ton contexte devienne gros** : écris la relève, `porte.py terminer` si l’étape ou le lot est fini, puis termine ; la veille relance.
6. Tests en fin de lot : `python3 tests/run_tests.py` (suite complète, 241+), `python3 tools/mono_build.py --check`, `python3 tools/prev_build.py --check`, `python3 tools/ck_build.py --check`, `python3 tools/doses_check.py`, `python3 tools/lyncee.py`.
7. Fin de chaque étape : `python3 tools/propose_skills.py` puis lire `docs/skills/PROPOSITIONS.md` ; un candidat utile devient `docs/skills/<nom>/SKILL.md`.

### A6. Fusion-publication automatique (cible)
Label `audit-ok` → `.github/workflows/auto-fusion.yml` met la branche à jour (`update-branch`, sans force-push) et active l’auto-merge en commit de fusion ; GitHub fusionne quand `garde`, `html`, `tests`, `visuel` sont verts ; `pages-apres-fusion.yml` relance `pages.yml` (Pages). En plus, **filet gratuit** : `tools/file_fusion.sh` (lancé par la veille toutes les 3 min et par `.github/workflows/file-fusion.yml` toutes les 20 min) parcourt les chaînes de `tools/etapes.json` dans l’ordre, met à jour les branches en retard, approuve/relance les CI `action_required`, fusionne en commit de fusion ce qui est prêt, relance Pages, et **consigne chaque échec** dans `journal/echecs_fusion.md` sans jamais s’arrêter.

---

## Partie B · Les étapes

Format de chaque étape : **But** · **Actions** · **Fichiers** · **Commandes** · **Fin quand** · **Étape suivante**. Une étape « en boucle » se répète lot par lot : à chaque fin de lot, `porte.py terminer` ; la veille relance le lot suivant tant que le critère n’est pas atteint (`ETAT.json` champ `lot`). Pour une boucle sans critère automatique, écris `"fin_boucle": N` dans ETAT.json quand tout est fait, puis `porte.py terminer`.

### Étape 0 · Installation et porte (BLOQUANTE)
**But** : avoir lu tout ce fichier et monté tout le dispositif avant le moindre contenu. Tu vérifies toi-même : `ETAT.md` (cases de la porte), `ETAT.json` (`{"etape_courante":0,"statut":"en_cours"}`), `tools/porte.py` (refuse l’Étape 1 tant qu’une case est vide ou qu’un fichier manque).
**Actions** (cocher chaque case de la porte d’ETAT.md au fur et à mesure, `- [x]`) :
- **0.1 Lecture** : ce fichier en entier, `AGENTS.md`, `HANDOFF.md` (tête), `ETAT.md`, `PROCHAINE_ACTION.md`, `journal/coordination.md`, `journal/asclepios.md`, `journal/echecs_fusion.md`.
- **0.2 Skills** : `docs/skills/README.md`, puis `ssp-pilotage-codex`, `ssp-continuite`, `ssp-verite`, `ssp-posologie-suisse`, `ssp-audit-medical`, `ssp-fusion-patch` (les autres à l’étape qui les cite).
- **0.3 (a) Catalogue** : `python3 tools/catalogue.py` écrit `CATALOGUE.md` (scripts gratuits du dépôt, automates GitHub Actions, outils système, skills, droits). Remplace chaque « À COMPLÉTER PAR CODEX » par la liste réelle : **tes serveurs MCP** (`codex mcp list` ou `~/.codex/config.toml`), **tes skills et outils intégrés** (web, navigateur, exécution…), avec l’étape où chacun sert. **Présente ce catalogue** (copie-le dans ta réponse de session et dans `PROCHAINE_ACTION.md`) **avant de commencer**. Ajoute les automates gratuits manquants que tu jugerais utiles (ex. pre-commit, `act`, lychee) avec leur usage.
- **0.4 (b) Proposition de skills** : `python3 tools/propose_skills.py` (détecte les commandes et tâches répétitives dans `journal/*.md`, `HANDOFF.md`, `.etat_local/*.log` et `git log`, écrit `docs/skills/PROPOSITIONS.md`). Lis le résultat ; crée tout de suite les skills évidents. À relancer à la fin de chaque étape (A5.7).
- **0.5 (c) Veille de relance = GitHub Actions (R15)** : rien à lancer sur un PC. `garde-progres.yml` (toutes les 10 min) te relance par `@codex` sur la PR « Pilote Codex » dès 30 min sans contenu, `file-fusion.yml` fusionne et publie. Vérifie seulement qu’ils sont verts (`gh run list -w garde-progres.yml -L 3`). `tools/veille_relance.sh` reste **facultatif** (mode A `codex exec` si une machine est disponible ; mode B `PROCHAINE_ACTION.md`), jamais requis.
  - Note le mode et la commande dans ETAT.md (« Réglages notés »).
- **0.6 (d) Droits de fusion** : `bash tools/file_fusion.sh --droits` doit montrer `admin:true`, `merge_commit:true`, `auto_merge:true`. Moyens, dans l’ordre : ton jeton `gh` (déjà admin du dépôt sur la box Grok : `gh auth status`) ; sinon `gh auth login` avec le compte de Vial ; pour l’automate GitHub, un **secret `AUTO_FUSION_TOKEN`** (PAT fin limité à ce dépôt : Contents, Pull requests, Actions en écriture), lu par `auto-fusion.yml` et `file-fusion.yml` (`gh secret set AUTO_FUSION_TOKEN` : demande le jeton à Vial ; **n’écris jamais un jeton dans un fichier ni dans un message**). Les règles de protection restent intactes : « admin » sert à fusionner soi-même, pas à contourner la CI. Teste `bash tools/file_fusion.sh --dry-run`.
- **0.7 Modèle** : vérifie que `gpt-6-luna` est accessible (`codex exec -m gpt-6-luna "réponds OK"` ou le sélecteur de modèle). Sinon, `export MODELE_REPETITIF=<le moins cher>` pour la veille et note-le dans ETAT.md.
- **0.8 Worktree et tests** : worktree depuis `origin/main` (A5.1) ; `python3 tests/run_tests.py` (ou motif d’échec noté, puis on continue).
- **0.9 Jauges** : `python3 tools/jauge/binomes.py` ; note la valeur de départ.
**Fichiers** : `ETAT.md`, `ETAT.json`, `CATALOGUE.md`, `docs/skills/PROPOSITIONS.md`, `PROCHAINE_ACTION.md`, `journal/echecs_fusion.md`, `tools/{porte.py,veille_relance.sh,file_fusion.sh,propose_skills.py,catalogue.py,etapes.json}`.
**Commandes** : `python3 tools/porte.py verifier0` (liste ce qui manque) → `python3 tools/porte.py terminer` (refusé si incomplet).
**Fin quand** : `python3 tools/porte.py verifier0` répond « Étape 0 complète. » ; commit + PR « Codex · Étape 0 » (CATALOGUE.md, ETAT.md, PROPOSITIONS.md), fusionnée.
**Étape suivante : 1.**

### Étape 1 · État réel, sauvegardes, jauges
**But** : partir de la réalité du dépôt, pas de ce fichier.
**Actions** : `gh pr list --state open --limit 60` ; pour chaque PR de `tools/etapes.json` → `gh pr checks N` et `mergeStateStatus` ; comparer au § C1 et corriger ce fichier si besoin. Vérifier que les sauvegardes (§ C4) sont lisibles (`git bundle verify`). Vérifier que Pages publie la même empreinte que main (`curl -s <url>/app_v2.html | sha256sum` contre `git show origin/main:app_v2.html | sha256sum`). Lire `journal/echecs_fusion.md`. Envoyer les jauges si un palier de +20 % est franchi (`python3 tools/jauge/binomes.py --check`).
**Fichiers** : `CONTINUATION.md` § C1, `ETAT.md`.
**Fin quand** : § C1 conforme au dépôt, ETAT.md journalisé ; `porte.py terminer`.
**Étape suivante : 2.**

### Étape 2 · Réparer la fusion-publication automatique et le contrôle visuel
**But** : qu’une PR `audit-ok` fusionne et publie **seule**. Au minimum Codex fusionne lui-même ; idéalement fusion + publication automatiques.
**Blocages connus** :
1. `auto-fusion.yml` : `gh pr merge --auto` lancé sans dépôt local ni `GH_REPO` (« not a git repository »). Correctif déjà posé : `--repo` explicite (commit bf310fc) et `GH_REPO` dans l’environnement (PR de relève). À **prouver** sur une PR test.
2. Les commits de mise à jour faits par le bot (`GITHUB_TOKEN`) laissent la CI en **`action_required`** (contourné jusqu’ici par un commit vide). Remède : secret `AUTO_FUSION_TOKEN` (0.6), lu en priorité par les deux workflows ; `file_fusion.sh` approuve ou relance les exécutions `action_required`, sinon consigne « pousser un commit vide ».
3. Le contrôle **`visuel`** échoue sur les PR de monographies (CLS bureau 0,13–0,17 > plafond 0,144 ; cause : calendrier rendu après la première peinture, glo-index plus lourd). #66 (polices auto-hébergées, CLS stable) est **fusionnée** ; il faut rebâtir chaque PR sur main (fusion de main) et vérifier que `visuel` passe ; sinon corriger le CLS (réserver la hauteur de `#v-cal`, ou rendre le calendrier avant de charger glo-index) dans une PR d’Iris, **sans** changer la référence sans le label `visuel:nouvelle-reference` (`tools/visuel_reference.sh`).
4. #63 (auto-fusion via GraphQL) et #56 (sonde e2e) : fermer avec motif si le correctif ci-dessus suffit ; sinon reprendre #63.
**Actions** : ouvrir une PR triviale (ligne de journal), poser `audit-ok`, observer `auto-fusion` puis `pages` (`gh run list --workflow auto-fusion.yml`, `gh run view --log-failed`) ; corriger ; recommencer. Lancer `gh workflow run file-fusion.yml` une fois pour vérifier le filet.
**Fin quand** : une PR test est fusionnée et publiée sans intervention ; sinon, au plus tard après deux essais, `file_fusion.sh` (veille) fait le travail et l’échec est consigné — **on passe à l’Étape 3 dans tous les cas** (R7).
**Étape suivante : 3.**

### Étape 3 · Files des prévalences (#43 → #44 → #45 → #58) et rapport #47
**But** : fusionner les prévalences déjà écrites et auditées. #42 (infrastructure, patch 0020) est **déjà fusionnée** (17.10.2026 23:22).
**Actions** : pour chaque PR, dans l’ordre : worktree sur sa branche (`git worktree add /workspace/oef-prev-N <branche>`), `git merge origin/main`, `python3 tools/prev_build.py` (jamais retoucher `PRV` à la main), `python3 tests/run_tests.py`, push ; la file fusionne. **#58** (G4 fièvre G6 + syncope F1.19) n’est **pas auditée** : audit Galien d’abord (R6 : chiffres relus dans la source, cadre, date, langue), section au rapport, puis `audit-ok`. **#47** (rapport d’audit Galien) : fusionner main, garder toutes les sections du rapport, `audit-ok`.
**Fichiers** : `data/ck/prev.json`, `assets/ck/prev.js`, `app_v2.html` (PRV), `audit/RAPPORT_AUDIT_MEDICAL.md`.
**Fin quand** : critère automatique `porte.py critere 3` (toutes fusionnées).
**Étape suivante : 4.**

### Étape 4 · Files des monographies Hygie (#50 → #53 → #54 → #64) et corrections d’Hérophile (#49)
**But** : fusionner les monographies G2 à G8 et les 150 corrections d’Hérophile.
**Actions** : ordre imposé **#50 → #53 → #54 → #64** (lots qui se chevauchent). Pour chacune : fusion de main, `python3 tools/merge_shards.py` sur les shards en conflit, `python3 tools/mono_build.py`, tests, push. #50 porte `audit-ok` ; **#53 et #54 sont audités mais sans label** : poser `audit-ok` dès que la précédente est fusionnée ; **#64 (G7+G8, 25 DD)** : 22 corrections d’Hérophile poussées, audit final à faire, puis `audit-ok`. **#49** (audit Hygie lot 1 + Panacée lot 1, `audit-ok`) : même rebâtissage, indépendante de la chaîne.
**Fin quand** : `porte.py critere 4`.
**Étape suivante : 5.**

### Étape 5 · File des monographies Panacée (#60 → #62)
**But** : fusionner O7.20 → O7.15 (auditées par Érasistrate, `audit-ok`). #55 (O7.23–O7.21) est **déjà fusionnée**.
**Actions** : fusion de main, `merge_shards.py`, `mono_build.py`, tests ; `audit/RAPPORT_AUDIT_MEDICAL.md` en add/add : garder toutes les sections.
**Fin quand** : `porte.py critere 5`.
**Étape suivante : 6.**

### Étape 6 · File des doses (#59 → #61 → #67 → #70) et doutes de doses
**But** : fusionner la table suisse des doses (lots 1–4 : 98 lignes, 66 substances), **après l’audit de Galien, qui n’est pas fait** (les labels `audit-ok` de #59/#61 ont été posés avant la relecture complète : relis quand même).
**Actions** : pour chaque PR, dans l’ordre : relire **chaque ligne** contre l’extrait AIPS officiel (unité, voie, indication, population, µ/≥/≤), `python3 tools/doses_check.py`, corriger sur la branche, section au rapport, `audit-ok`. Trancher les doutes :
- **aciclovir** : AIPS 10 jours (encéphalite à HSV) contre 14/21 jours dans une monographie → la monographie suit l’AIPS, ou « À vérifier » avec la source européenne lue et datée si elle diffère ;
- **KCl** : unité « mmol/l heure » à relire dans l’AIPS (probablement mmol/heure) ;
- **lévothyroxine** et **pipéracilline-tazobactam** : unités présentes seulement dans l’en-tête d’un tableau → citer l’en-tête dans l’extrait ou « À vérifier » ;
- **absents de l’AIPS** → « À vérifier (AIPS) » : thiamazole, acarbose, phénoxybenzamine, charbon activé (seul texte suisse autorisé pour la diarrhée, aucune dose d’intoxication), glucose IV (aucune dose d’hypoglycémie), DigiFab (notice américaine seulement, tableau illisible), fomépizole, silibinine IV, physostigmine, artésunate IV, gluconate de calcium IV.
Puis remplacer dans les monographies les « À vérifier (AIPS) » par `dose_ref` vers `doses_ch.json` quand la dose existe.
**Fichiers** : `data/ck/doses_ch.json`, `tools/doses_check.py`, `data/ck/mono/*.json`.
**Fin quand** : `porte.py critere 6`, doutes tranchés ou « À vérifier ».
**Étape suivante : 7.**

### Étape 7 · File du glossaire (#65 → #68)
**But** : fusionner le glossaire automatique (#65 Lyncée 2, `audit-ok`) puis le lot 01 de 166 définitions courtes (#68, audit Galien à finir).
**Actions** : fusion de main, `python3 tools/ck_build.py`, `python3 tools/lyncee.py` (la baseline `qa/termes-baseline.json` ne peut que baisser), audit des définitions (très courtes, exactes, sans citer leur propre libellé ni alias, pas de paire circulaire), `audit-ok`.
**Fin quand** : `porte.py critere 7`.
**Étape suivante : 8.**

### Étape 8 · Prévalences en rouge des 248 SSP (boucle, GPT 6 Luna)
**But** : chaque DD de chaque SSP porte son % suisse ou européen (ou « % à vérifier »), en rouge, trié décroissant ; les **22 SSP sans DD** reçoivent leurs DD.
**Lot** : un groupe de plaintes (≈ 2–4 SSP). Ordre : G5 vertige, toux, lombalgie, malaise ; puis S7.6, S2.12, S8 (après #37) ; puis tous les autres SSP dans l’ordre du catalogue ; les 22 SSP sans DD dans le premier lot où ils tombent.
**Actions par lot** : (1) rédiger dans `data/ck/prev.json` (champs `prev_pct`, `src`, `date_lu`, `loc`, cadre ; règles P1–P7 de `tools/audit/prevalence.py`) ; décision d’Asclépios : le chiffre est la fréquence du diagnostic **parmi les patients consultant pour la plainte**, dans un cadre nommé (médecine de famille ou urgences, CH ou UE) ; une prévalence de population ne sert qu’à défaut (affichée « population ») ; (2) `python3 tools/prev_build.py` ; (3) tests ; (4) PR ; (5) **audit Galien aussitôt** (chiffre relu dans la source à l’emplacement exact, tableau/page, cadre, langue) ; (6) `audit-ok` ; (7) jauge.
**Pièges** : ne jamais éditer `PRV` à la main ; aucun « window.CK_ » littéral dans `app_v2.html` ; somme ≤ 100 % ; un chiffre exige l’emplacement exact.
**Fin quand** : jauge Prévalences = 100 % (`porte.py critere 8`).
**Étape suivante : 9.**

### Étape 9 · Monographies en 7 rubriques, deux chaînes opposées (boucle, GPT 6 Luna)
**But** : une monographie complète (A2.2) pour chaque DD, du premier au dernier SSP.
**Lot** : ≈ 25–30 DD. **Chaîne A (Hygie → Hérophile)** : prurit G9 + douleur G10 (≈ 30 DD), puis vers l’avant. **Chaîne B (Panacée → Érasistrate)** : O7.14 – O7.12, puis vers l’arrière. Réserver le lot dans la PR ; jamais le même DD dans les deux chaînes.
**Actions par lot** : `python3 tools/mono_build.py --draft <SSP>` (existant TIP.d à replacer) → compléter seulement le manquant dans `data/ck/mono/<lettre>.json` → `python3 tools/mono_build.py` puis `--check` (structure, gras, doses) → tests → PR → **audit aussitôt** (médical, sources lues et datées, langue : def/phy/dia/epi en phrases verbales ; cli/exp listes admises ; but/mes/pha à l’infinitif admis) → `audit-ok`. Doses : seulement `dose_ref` vers `doses_ch.json`, sinon « À vérifier (AIPS) ».
**Fin quand** : jauge Monographies = 100 % (`porte.py critere 9`).
**Étape suivante : 10.**

### Étape 10 · Doses AIPS, lot 5 et suivants (boucle, GPT 6 Luna)
**But** : toutes les substances citées dans les monographies ont leur ligne AIPS verbatim, ou « À vérifier ».
**Lot** : ≈ 20 substances, d’abord celles des nouvelles monographies ; revérifier les unités des lots précédents.
**Actions par lot** : télécharger l’AIPS officielle (Swissmedic/Refdata), extraire par script **mot pour mot**, relire chaque ligne, `doses_check.py`, PR « Pharmakon · doses lot N », audit Galien, `audit-ok`. Retenter DigiFab si une AIPS suisse lisible existe.
**Fin quand** : aucune dose citée hors `doses_ch.json` sans « À vérifier » ; écrire `"fin_boucle": 10` dans ETAT.json puis `porte.py terminer`.
**Étape suivante : 11.**

### Étape 11 · Glossaire automatique (boucle, GPT 6 Luna)
**But** : tout terme spécialisé se définit d’un clic, en quelques mots.
**Actions par lot** : `python3 tools/lyncee.py` (termes non définis, les plus fréquents d’abord) → lot de ≈ 150 définitions dans `data/ck/glo.json` (sources R1) → `ck_build.py` → baseline resserrée (`--update`) → audit → `audit-ok`. Inclure les ~85 termes de `journal/nerfs-ck.md` et les 27 signes « À vérifier » de Galien.
**Fin quand** : baseline Lyncée = 0 ; `"fin_boucle": 11` puis `porte.py terminer`.
**Étape suivante : 12.**

### Étape 12 · Finitions P1
**Actions** : script rejouable pour les **72 textes de DD** qui commencent par « À ne pas manquer.</b> » sans balise ouvrante (rouge perdu) ; balayage de tous les « À vérifier » (sourcer ce qui peut l’être) ; audit transversal (cohérence prévalence ↔ monographie ↔ dose) ; captures et `tests/visuel/` ; fond très pâle et contraste AA vérifiés.
**Fin quand** : rapport final fusionné ; `porte.py terminer`.
**Étape suivante : 13.**

### Étape 13 · Nerfs crâniens
**Actions** : reprendre `feat/nc07-voie-motrice` (SVG de la voie motrice du VII par Dédale) et #39 (revue Galien du VII, glossaire lot 02) : fusion de main, `nc_svg_js.py`, `ck_build.py`, correctif CLS si besoin, audit, fusion. Puis les autres paires crâniennes selon le même contrat (HANDOFF « Dédale », « Hermès »). Croquis validés par Vial.
**Étape suivante : 14.**

### Étape 14 · Stations CS (boucle)
**Actions** : faire relire les 5 stations pilotes par Vial (`valide_par_vial`) ; puis une station par SSP à haut rendement, format `data/cs/format.json`, `tools/cs_build.py`, aucune dose chiffrée (« À vérifier »), audit, fusion.
**Étape suivante : 15.**

### Étape 15 · Lots d’urgences CK (boucle)
**Actions** : #41 (audit Galien niveau 2, TIP champ 5) ; lot 3 (`feat/ck-urgences-lot3` : hémorragie variqueuse Baveno VII, épiglottite, asthme SGP-SSP) ; doses via `dose_ref`.
**Étape suivante : 16.**

### Étape 16 · PR en pause
**Actions** : #32 (fond pâle `#fbfbf8`, nouvelle référence visuelle), #37 (trauma S8.1–S8.12, conflits : la branche complète `feat/trauma-ddx` n’existe que dans les sauvegardes, § C4), #16 (présentation premium). Fusionner après audit ou fermer avec motif.
**Étape suivante : 17.**

### Étape 17 · Clôture
**Actions** : jauges à 100 % envoyées ; site public = main (empreinte) ; tests complets ; `HANDOFF.md`, `ETAT.md`, ce fichier à jour ; liste finale des « À vérifier » et des fautes critiques pour Vial ; désactiver `garde-progres.yml` (`gh workflow disable garde-progres.yml`) et, si utilisée, la veille facultative. **Fin du projet.**

---

## Partie C · État, outils, sauvegardes

### C1. État au 18.10.2026 00:45 (historique ; vérification Codex ci-dessous)
**Sur main** (9b5925c) : infrastructure monographies (patch 0026, `assets/mono/`), Hygie lot 1 (G1, 14 DD), Panacée lots 1–2 (O7.26–O7.21), **infrastructure prévalence #42** (aucun chiffre encore), **visuel CLS #66**, `progres.html`, auto-fusion v1 + `--repo` + correctif Pages.

| PR | Objet | État |
|---|---|---|
| #43 · #44 · #45 | Prévalence G1 thorax · G2 dyspnée · G3 abdomen (auditées Galien) | audit-ok ; #43/#44 BEHIND, #45 DIRTY |
| #58 | Prévalence G4 fièvre (G6) + syncope (F1.19) | DIRTY ; **audit Galien à faire** |
| #47 | Rapport d’audit Galien (prévalences) | DIRTY |
| #49 | Hérophile : audit Hygie lot 1 + Panacée lot 1 (150 corrections) | audit-ok ; DIRTY |
| #50 · #53 · #54 · #64 | Hygie lots 2 (G2) · 3 (G3+G4) · 4 (G5+G6) · 5 (G7+G8) | audités ; audit-ok sur #50 seulement ; ordre imposé ; #64 non audité en final |
| #60 · #62 | Panacée lots 3–4 (O7.20 → O7.15), audités Érasistrate | audit-ok ; DIRTY |
| #59 · #61 · #67 · #70 | Pharmakon : doses AIPS lots 1–4 | audit Galien **non fait** ; #70 CLEAN sans label |
| #65 · #68 | Lyncée : glossaire automatique · lot 01 (166 définitions) | #65 audit-ok DIRTY ; #68 audit à finir |
| #63 · #56 | auto-fusion GraphQL · sonde e2e | à fermer si l’Étape 2 réussit |
| #39 · #41 · #37 · #32 · #16 | NC/TIP Galien, trauma S8, fond pâle, premium | Étapes 13–16 |

**Jauges** (`tools/jauge/binomes.py`, origin/main, 18.10.2026 00:45) :
```
Prévalences   ░░░░░░░░░░    0 %  (0/2578 · audités 0)
Monographies  ░░░░░░░░░░    3 %  (70/2280 · audités 0)
```
(≈ 115 monographies et 34 prévalences écrites sur branches, non fusionnées.)

**Autres reliquats** : ~moitié des chiffres épidémiologiques des monographies encore « à vérifier » ; cartes d’approbation à chaque `git push` dans l’environnement Grok Bot (sans objet pour Codex).

### Vérification Codex · 18.10.2026 01:05 CEST

Main observé : `2228be7` (dépôt réel). Pages HTTP 200, SHA-256 identique à origin/main : `c750e1813c1c725508628d407ab7382c43ccb997923b3ee83e58bb5acf850f40`.

| PR | Branche | Fusion | Contrôles observés |
|---|---|---|---|
| #16 | feat/apollon-premium | UNKNOWN | garde: SUCCESS, visuel: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #32 | feat/fond-pale | UNKNOWN | visuel: FAILURE, garde: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #37 | feat/trauma-ddx | UNKNOWN | visuel: FAILURE, garde: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: FAILURE, tests: SUCCESS, schemas: SUCCESS |
| #39 | feat/galien-nc07-revue | UNKNOWN | visuel: FAILURE, garde: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #41 | fix/galien-tip-revue | UNKNOWN | visuel: FAILURE, garde: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #43 | feat/ddx-prev-g1-thorax | BLOCKED | garde: IN_PROGRESS, visuel: IN_PROGRESS, auto-fusion: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: IN_PROGRESS, tests: IN_PROGRESS, schemas: IN_PROGRESS |
| #44 | feat/ddx-prev-g2-dyspnee | UNKNOWN | visuel: FAILURE, visuel: FAILURE, garde: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #45 | feat/ddx-prev-g3-abdomen | UNKNOWN | visuel: FAILURE, visuel: FAILURE, garde: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #47 | audit/galien-prev | DIRTY | visuel: FAILURE, garde: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #49 | audit/herophile | DIRTY | auto-fusion: FAILURE, garde: IN_PROGRESS, visuel: IN_PROGRESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: IN_PROGRESS, schemas: IN_PROGRESS |
| #50 | feat/mono-g2 | DIRTY | auto-fusion: SUCCESS, garde: SUCCESS, visuel: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #53 | feat/mono-g3 | UNKNOWN | visuel: FAILURE, auto-fusion: SKIPPED, garde: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #54 | feat/mono-g5 | UNKNOWN | visuel: FAILURE, auto-fusion: SKIPPED, garde: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #56 | test/auto-fusion-e2e | UNKNOWN | aucun check publié |
| #58 | feat/ddx-prev-g4-fievre-syncope | UNKNOWN | aucun check publié |
| #59 | feat/doses-ch-1 | DIRTY | auto-fusion: FAILURE, garde: SUCCESS, visuel: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #60 | feat/mono-panacee-3 | DIRTY | garde: FAILURE, auto-fusion: SUCCESS, visuel: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #61 | feat/doses-ch-2 | UNKNOWN | aucun check publié |
| #62 | feat/mono-panacee-4 | UNKNOWN | aucun check publié |
| #63 | agent/auto-fusion-graphql | UNKNOWN | visuel: FAILURE, auto-fusion: SKIPPED, garde: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #64 | feat/mono-g7 | UNKNOWN | visuel: FAILURE, auto-fusion: SKIPPED, garde: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #65 | feat/lyncee-glossaire | DIRTY | auto-fusion: FAILURE, garde: SUCCESS, visuel: SUCCESS, visuel: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: SUCCESS, schemas: SUCCESS |
| #67 | feat/doses-ch-3 | DIRTY | aucun check publié |
| #68 | feat/glo-lyncee-01 | UNKNOWN | visuel: FAILURE, garde: SUCCESS, etiquette: SUCCESS, html: SUCCESS, liens: SUCCESS, tests: FAILURE, schemas: SUCCESS |
| #70 | feat/doses-ch-4 | CLEAN | aucun check publié |
| #71 | codex/etape-0 | BLOCKED | garde: IN_PROGRESS, visuel: IN_PROGRESS, etiquette: IN_PROGRESS, html: IN_PROGRESS, liens: IN_PROGRESS, tests: IN_PROGRESS, schemas: IN_PROGRESS |

UNKNOWN signifie que GitHub n’a pas encore calculé la fusion ; ce n’est pas une validation. Les sauvegardes bundle et patches Grok (§ C4) sont absentes des deux chemins dans cet environnement. Les branches distantes sont disponibles ; ne pas annoncer les travaux non commités comme récupérés.

Jauges inchangées : prévalences 0/2578 (0 %), monographies 70/2280 (3 %). `binomes.py --check` passe. La file locale a mis #43 à jour ; sa CI est en cours. La protection main n’est pas lisible via cette intégration (403), elle reste intacte.

### C2. Commandes et fichiers
| Chemin | Rôle |
|---|---|
| `tools/porte.py` | Porte des étapes : `etat`, `verifier0`, `commencer N`, `critere N`, `terminer`, `avancer`, `ordre`, `--dry-run`. |
| `tools/etapes.json` | Feuille de route machine : étapes, critères, boucles, modèle, chaînes de PR de la file de fusion. |
| `tools/garde/` + `garde-progres.yml`, `checkpoint.yml`, `appel-vial.yml` | **Veille permanente R15** (GitHub Actions, 5 min) : STALL → `@codex`, appel de Vial, recyclage, checkpoint de PR. |
| `tools/veille_relance.sh` | Veille facultative : file de fusion, fin d’étape, relance de Codex (mode A `codex exec`, mode B `PROCHAINE_ACTION.md`). |
| `tools/file_fusion.sh` | File de fusion-publication : `--dry-run`, `--chaine`, `--droits`, `--ci` ; échecs → `journal/echecs_fusion.md`. |
| `.github/workflows/file-fusion.yml` | Même file, planifiée toutes les 20 min sur GitHub (gratuit). |
| `tools/propose_skills.py` | Propositions automatiques de skills → `docs/skills/PROPOSITIONS.md`. |
| `tools/catalogue.py` | Écrit `CATALOGUE.md` (outils gratuits, automates, skills, MCP, droits). |
| `tools/jauge/binomes.py` | Deux jauges (prévalences, monographies) depuis `origin/main` ; `--json`, `--check`, `--init`. |
| `tools/merge_shards.py` | Fusion 3 voies clé par clé des shards `data/ck/mono/*.json` en conflit. |
| `tools/mono_build.py` | `data/ck/mono/<lettre>.json` → `assets/mono/mono-<lettre>.js`. `--check` (CI) ; `--draft <SSP>`. |
| `tools/prev_build.py` (+ `tools/audit/prevalence.py`) | `data/ck/prev.json` → `PRV` + `assets/ck/prev.js`. `--check` en CI. |
| `tools/doses_check.py` | Contrôle `data/ck/doses_ch.json` : extrait AIPS verbatim, url, versions, dates, chaque nombre présent dans l’extrait. *(branches #59…#70)* |
| `tools/ck_build.py` / `tools/ck_common.py` | Compile `data/ck/*.json` → `assets/ck/*.js` ; `--check` en CI. |
| `tools/lyncee.py` + `qa/termes-baseline.json` | Termes non définis ; la baseline ne peut que baisser. |
| `tools/json_inject.py`, `tools/_app.py`, `tools/patches/` | Injection des constantes dans `app_v2.html` ; patches à ancrage unique, rejouables (skill `ssp-patch`). |
| `tools/audit/rapport_fautes.py`, `tools/aletheia.py` | Audit niveau 1 (G1–G8), registre des fautes, blocage d’une faute critique. |
| `tools/cs_build.py`, `tools/build_mem.py`, `tools/build_exi.py` | Stations CS, Mémorisation, Exigences. |
| `tests/run_tests.py`, `tests/test_*.py`, `tests/visuel/` | Suite complète ; captures et comparaison visuelle (CLS). |
| `data/ck/` | `mono/`, `prev.json`, `doses_ch.json`, `src.json`, `glo.json`, `schema/`. |
| `audit/RAPPORT_AUDIT_MEDICAL.md` | Rapport public « les fautes corrigées » (une section par lot). |
| `skills/ssp-*/SKILL.md` = `docs/skills/ssp-*/SKILL.md` | Procédures (index : `docs/skills/README.md`). |
| Box Grok seulement : `/workspace/hippo_work/` | Outils d’audit d’origine : `newmono.py`, `autosrc.py`, `fix_*.py`, `poll_*.sh`, `HANDOFF_{GALIEN,HEROPHILE,ERASISTRATE}.md`, sources locales `src/`. |

### C3. Pièges déjà rencontrés
- G1 lit un seuil suivi de « mmol », « µg » ou « 30 mL » comme une dose : écrire « millimoles par litre », « 30 millilitres ». Une dose ajoutée dans TIP/NOT/GES échoue à G1 sans « À vérifier » dans le même texte.
- G6 ne connaît pas certains verbes (« rétrécissent », « entre », « resserre », « enlever », « convenir », « coaguler ») : reformuler ; la liste se régénère par `tools/audit/verbes_gen.py`, jamais à la main.
- Lyncée découpe au trait d’union (« Glasgow-Blatchford » → « score de Blatchford ») ; « IIa/IIb » lus comme termes : écrire le niveau en mots ; une définition ne cite ni son libellé ni ses alias.
- Après toute retouche de `data/ck` : `ck_build.py` ; de `data/cs` : `cs_build.py` ; d’un SVG : `nc_svg_js.py`. Sinon la CI échoue.
- Aucun « window.CK_ » ni « glo|<id> » littéral dans `app_v2.html` ; le rouge passe seulement par `.urg` ou `[data-bloquant]` (G7).
- `tools/merge_shards.py` garde HEAD en cas de « CONFLIT RÉEL » sur une même clé : relire ces clés à la main avant de pousser.
- Relèves détaillées des auditeurs (worktrees, scripts, ordre des labels) : `docs/releves/HANDOFF_{GALIEN,HEROPHILE,ERASISTRATE}.md`.

### C4. Sauvegardes de l’arrêt (17.10.2026 23:30) et comment les réappliquer
Emplacements : `/workspace/sauvegardes/20261017-2330-arret/` et `/cursor/stores/store-e5265852-6589-40c1-aa67-8de61d5486d9/sauvegardes/20261017-2330-arret/` (plus l’archive précédente `…/sauvegardes/20261017-2317/`). Hors de la box Grok, ces fichiers ne sont pas visibles : demander à Vial de les copier si besoin ; toutes les branches sont **aussi sur GitHub**.
- `toutes-branches.bundle` (167 références, toutes les branches) : `git bundle verify toutes-branches.bundle && git fetch toutes-branches.bundle 'refs/heads/*:refs/remotes/sauvegarde/*'`. Seule source complète de `feat/trauma-ddx`.
- Travail non commité, un patch par worktree (`git diff` contre la tête de la branche indiquée) :

| Patch | Branche (tête) | Contenu |
|---|---|---|
| `oef-asclepios.wip.patch` | feat/asclepios-examen (117bb94) | GES, NOT, PHT, SSP extraits |
| `oef-asclepios2.wip.patch` | feat/examen-tip (5c1f4bd) | GES, TIP extraits |
| `oef-asclepios3.wip.patch` | feat/trauma-ddx (c80e62f) | 32 fichiers (trauma S8, ci.yml, ETAT, HANDOFF, app_v2.html) |
| `oef-asclepios4.wip.patch` | feat/examen-fragments (c80e62f) | app_v2.html, TIP, tests |
| `oef-erasistrate.wip.patch` | era-pan4 (681a6e8) | TIP extrait |
| `oef-galien-g1/g3/g4.wip.patch` | galien-g1 (be15a0b) · galien-g3 (fddaa42) · galien-g4 (df0ce4e) | NOT, TIP extraits |
| `oef-galien-g2.wip.patch` | galien-g2 (7309a34) | 59 fichiers (workflows, données) |
| `oef-galien-prev.wip.patch` | audit/galien-prev (cb27d22) | TIP extrait |
| `oef-hippocrate.wip.patch` | feat/galien-nc07-revue (71a1d2d) | TIP extrait |
| `oef-lyncee-glo.wip.patch` | feat/glo-lyncee-01 (b0b7e38) | patch 0026 Lyncée (liste sans glossaire) |
| `oef-podalire5.wip.patch` | feat/ck-urgences-lot3 (0e138e4) | glossaire urgences lot 3 |
| `oef-prev.wip.patch` | feat/ddx-prevalence (91395aa) | NOT, TIP extraits |
| `wt_panacee.wip.patch` | feat/mono-panacee-4 (74dd946) | scripts `.pan/lot1–4.py` |

Réappliquer : `git worktree add /workspace/oef-reprise <branche>` (ou `git checkout -b reprise <sha>` depuis le bundle) → `git apply --3way --check <patch>` puis `git apply --3way <patch>`. Les fichiers `data/*.json` extraits (TIP, NOT, GES…) sont des **extractions de travail** de `json_inject.py` : ne pas les commiter tels quels, les régénérer. Ne réappliquer que ce qui sert l’étape en cours.

### C5. Modèle de relève (HANDOFF.md, section en tête)
```
## <Rôle> · <objet> · JJ.MM.AAAA, Europe/Zurich
État       : <branche, PR, ce qui est fait, tests>
Prochaine  : <lot suivant exact>
Sources    : <sources lues, datées>
Pièges     : <ce qui a cassé et comment l’éviter>
À vérifier : <liste>
```

### C6. Relève Codex du 18.10.2026 UTC
Le passage aux vérifications de clôture ne valide pas la fin du projet. État détaillé : `docs/releves/RELEVE_CODEX_20261018.md` ; étapes inachevées dans `ETAT.json.en_attente`, reprise de la boucle 8. #64/#67/#70 restent attente-vial. #80/#81 sont des brouillons, cinq stations restent non validées. Incident de fusion hors ordre #62, verrou proposé #82 ; défaut Fermer corrigé #84 avec suite 276/276. Le mode B de veille n’exécute pas de rédaction médicale autonome tant que la CLI est en 401. Aucun seuil, source, accord ou 100 % inventé.

### C7. Mise à jour factuelle · 18.10.2026 00:52 UTC

#45, #58, #60, #39, #84 et #82 sont fusionnées. Étape 3 complète ; les données Panacée sont réunies, avec incident d’ordre #62 avant #60 conservé. Main : prévalences 38/2587 (1 %), monographies 130/2287 (6 %). Suite main 42a432d : 276/276 ; Pages identique à main 8dd0d0a (HTTP 200, SHA-256 9e4720c6ce86056e4648eaa8744fe183479d9ddbf6419f1bb13ad60d8a800969). #65 et #68 restent en attente de fusion, références respectives 3735 et 3571 ; 527 entrées réunies sur #68. Les détails et réserves sont dans docs/releves/RELEVE_CODEX_20261018.md. Clôture toujours refusée, ETAT.json étape 8, lot 2, veille mode B conservée.

### C8. Mise à jour factuelle · 18.10.2026 01:15 UTC

#50→#53→#54 fusionnées ; #86 fusionnée. Main : 207/2287 monographies (9 %), 38/2587 prévalences (1 %). Pages et quatre fichiers JS cliniques contrôlés sont identiques à main 51cb2e5. #65 contient 406 entrées (référence 3734) et le patch 0030 du calendrier : suite 276/276 ; #68 contient 535 entrées (référence 3571), fusion après #65. #32 : référence CI adoptée explicitement par le script habituel sur runner, compteurs axe non augmentés et référence CLS resserrée, CI après adoption encore requise. DigiFab retrouvé dans l’AIPS officielle (révision 02/2026) ; extraction/audit de dose restant, aucune dose publiée. Réserves R13, stations/croquis non validés et limites du mode B inchangées. Voir relève détaillée, ETAT.json et preuve DigiFab.

Complément 01:16 UTC : #32 fusionnée (617878e), nouvelle référence et procédé d’adoption runner intégrés après contrôles requis verts. #37 reste en audit. #65 est réuni avec ce rendu ; les captures de la combinaison restent à examiner.

### C9. Complément de relecture · 18.10.2026 UTC

#49, #59, #61 et #65 sont fusionnées. #65 : 414 entrées, référence 3730 et suite 278/278, sans changer la référence visuelle pour masquer le déplacement de texte. #68 : 543 entrées, référence 3567 ; cibles des notions agrandies à 24 px, vérification/adoption de référence en cours. Nouvelle faute majeure terminologique : cardioverter employé comme verbe avait été défini comme appareil ; correction sourcée CHUV dans la relève en préparation. La conduite de la fiche arythmie-non-controlee fait l’objet de la proposition potentiellement critique #88, attente-vial. Les sources ESC 2022 et HUG 2024 ont été relues, la conduite proposée reste hors main. Inventaire des marques explicites par SHA/pointeur disponible ; il ne vaut pas audit ni clôture. Les autres attentes restent dans ETAT.json.

### C10. État après les fusions du glossaire et de G5 · 18.10.2026 UTC

#68 fusionnée (f2f9c04) après #65 : 543 entrées, référence 3567. Les cibles Notions de 24 px suppriment les défauts de taille observés sur les six profils ; adoption de la référence CI examinée, puis HTML, garde, visuel et suite 278/278 verts. L’erreur HTML ajoutée pendant la préparation a été corrigée sans changer sa référence. #85 fusionnée (27c9658) : 44 DD G5 explicitement inconnus ; couverture quantitative inchangée à 1 %. À 02:23 UTC, application et quatre JS contrôlés identiques à ce main sur Pages. Inventaire de cet instantané : 751 champs marqués, 779 occurrences, 24 fichiers ; ni audit complet ni preuve d’exhaustivité. Les états suivants des PR sont à lire dans ETAT.json et la relève datée, sans conclure la fin du projet.

Actualisation 2026-10-18T02:30:26.096088+00:00 : #41 fusionnée (5de965f) après #83, contrôles requis verts et 278 tests. #81 reste en audit. Les corrections cliniques R13 #64/#67/#70/#88 restent en attente de Vial. La clôture reste refusée ; reprise à l’étape 8, lot 3.

### Reprise après le lot 3 · 18.10.2026 UTC

#90 est fusionnée (6bbbde7). Main : 39/2587 fréquences, jauge arrondie 2 % ; 207/2287 monographies, 9 %. Une seule fréquence a été retenue après relecture (SCA, Zurich, 1/53) ; les dix-neuf autres du lot restent inconnues. Source de Berne non retenue sous la règle d’éditeur, miroir suisse inaccessible ; incohérences de l’autre tableau européen consignées. Aucun pays, chiffre ou critère inventé.

#91 contient six propositions G9 (xérose, prurits rénal, ferriprive, médicamenteux, neuropathiques, psychogène), EDF 2025 et HUG relus. Elles ne comptent pas dans main. Le verrou #64→#91 est dans main ; predecesseurs_fusion.py 91 constate #64 OPEN et ready=false. Ne pas activer directement l’auto-merge de #91.

Pages vérifié à 02:54:35 UTC : accueil, app et quatre JS HTTP 200, identiques à main 6bbbde7. Inventaire actualisé : 788 champs, 817 marques, 24 fichiers. La clôture reste refusée ; reprise étape 8 lot 4, G1–G4, S8 après #37. Les instantanés antérieurs restent historiques.

Complément 02:58 UTC : #91 passe la suite locale 278/278 sur 7af1a77, après les contrôles G1/G2/G3/G6 et Lyncée sans terme nouveau. PR prête et audit-ok ; aucun auto-merge directement activé. La preuve de chaîne constate #64 OPEN et ready=false. Les CI exactes restent requises ; six monographies hors main, pas de gain de couverture publié annoncé.

### Reprise réseau et chaîne · 18.10.2026 Europe/Zurich
#64→#91→#67→#70 fusionnées, ordre et SHA dans audit/FUSIONS-REPRISE-20261018.json. #64 était déjà fusionnée au début de la reprise ; #91, #67 et #70 ont été réunies avec main, recontrôlées puis fusionnées avec CI verte. Main après #70 : 39/2587 fréquences et 238/2287 monographies ; 98 lignes AIPS. #97 ajoute 60 fréquences inconnues G1–G4 sans aucun chiffre nouveau ; #98 propose deux G9. Boucles ouvertes, étape 8 lot 5. Sources EDF/HUG/AIPS accessibles ; Oxford, recherche Europe PMC, navigateur file:// et Pages ont les limites consignées dans les audits. Les paragraphes antérieurs sont historiques.

Complément après #97 : fusion observée 82bdd32, contrôles requis verts. #98 réunit deux propositions G9 (dysthyroïdies, cholestase obstructive) avec les réserves explicitement documentées ; sa branche compte 240/2287 monographies. Suite et visuel GitHub exacts requis avant sa fusion. Boucle 8 lot 5 : G7–G10 ; neuf autres G9, G10 et chaîne Panacée encore dus. Aucun nouveau chiffre de prévalence ni fin de boucle.

### Lot 5 et gales · 18.10.2026 Europe/Zurich
#99 fusionnée (8548085) : G7–G10, 56 libellés intacts, six fréquences G9 de Brest et cinquante inconnues. Main 45/2587 ; causes non exclusives et sélection hospitalière précisées. #100 réunit deux gales, cinq épidémiologies de prurit contextualisées et six définitions ; branche 242/2287 monographies, 563 entrées de glossaire et référence 3564. Les sept autres G9, G10 et Panacée restent dus. Reprise étape 8 lot 6, G11–G14 ; aucune clôture. Aucune dose étrangère transposée et aucune validation de médecin inventée.

### Lot 6 · 18.10.2026 Europe/Zurich
G11–G14 : 56 fréquences explicitement inconnues, libellés intacts, aucun chiffre nouveau. #100 est fusionnée (ed62ae5), main 242/2287 monographies. Prochain lot G15, G16, S1.1 et S1.2 ; sept G9 restent dus. Recontrôle : GitHub/EDF/HUG 200, Pages encore CONNECT 403 dans cette session ; configuration nouvelle non présumée appliquée. Aucune fin de boucle.

### Complément dermatose G9 · 18.10.2026 Europe/Zurich
#101 fusionnée (774de74), Pages réussi ; 45/2587 fréquences. PR #102 : psoriasis et urticaire chronique, six définitions, 244/2287 monographies et 569 entrées, référence 3563. Critères formels psoriasis et AIPS gardent leurs réserves ; CI exacte requise avant fusion. Cinq G9 restent dus (Hodgkin, pemphigoïde étendue, Vaquez, dermatite atopique, lichen plan), puis G10 et Panacée O7.14–O7.12. Boucle 8 lot 7 G15, G16, S1.1 et S1.2 ; aucune clôture.

### Reprise du découpage original · 18.10.2026 Europe/Zurich
Vial annule le protocole Gardien v1.0 ; fin.py reste facultatif. Sentinelle permanente rapprochée : passage toutes les 5 min, fenêtre et rappel Codex de 15 min, quatre stalls avant appel de Vial et délai d’appel de 60 min conservé. Un sous-agent sentinelle accompagne la tranche interactive sans pouvoir réveiller une session fermée. Étape officielle8 lot8, reprise de contenu à G10 ; S1.3–S1.6 et Panacée O7.14–O7.12 restent dus.
