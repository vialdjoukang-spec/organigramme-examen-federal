# Déploiement du harnais par agent — 9 novembre 2026

Un cœur commun, une instance par agent (config, mémoire, cache, index, logs, santé). **Gratuit** : outils libres et runners GitHub gratuits (dépôt public).
Le harnais **ne rédige rien et ne juge rien cliniquement** ; contenu toujours « non validé cliniquement ».
Interdits rappelés : jamais `main`, jamais de PR ni de fusion, jamais `LOT_Claude_Finaux/` ni `harnais/`, jamais `psychotherapie-personnelle-de-Vial/`.

## 1. Box (Leona__Harnais_LOT132) — déjà installé et actif
```bash
H=/workspace/outils-puissants/Leona__Harnais_Agents_20261109
export HARNAIS_INSTANCE=$H/instances/Leona__Harnais_LOT132; alias harnais=$H/coeur/bin/harnais
$H/surveillance/demarrer_box.sh          # idempotent : (re)lance la boucle 5 min si absente (après redémarrage de la box)
cat $HARNAIS_INSTANCE/sante/statut.json  # dernier passage ; ALERTE.json n'existe qu'en cas d'échec
```
La boucle box surveille aussi, en lecture seule, les runs Actions des branches `agentA/lot-131` et `agentB/lot-130`
(`instances/Agent*/sante/cloud_runs.json`, API publique GitHub, 2 appels / 5 min, sous la limite anonyme de 60/h).

## 2. Agents cloud A et B
### 2.1 Dépôt du paquet sur la branche (fait par l'agent, sur SA branche uniquement)
Sur la box : `$H/surveillance/preparer_paquet.sh AgentA` (resp. `AgentB`) → `dist/paquet_AgentA.tar.gz` (+ `.sha256`).
Contenu : `Leona__Harnais_Agents/` (coeur sans binaires, registre, tests, surveillance, `instances/AgentA__Harnais_LOT131/`) + `.github/workflows/harnais-sante-agentA.yml`.
Dans la VM de l'agent, à la racine du dépôt :
```bash
git fetch origin agentA/lot-131 && git switch agentA/lot-131         # agentB/lot-130 pour B
tar xzf paquet_AgentA.tar.gz                                          # crée Leona__Harnais_Agents/ et .github/workflows/
git add Leona__Harnais_Agents .github/workflows/harnais-sante-agentA.yml
git commit -m "Harnais AgentA__Harnais_LOT131 : outils mécaniques + santé (sans PR)"
git push origin agentA/lot-131                                        # jamais main ; aucune PR
```
### 2.2 Installation et usage dans la VM de l'agent (chaque session)
```bash
H=$PWD/Leona__Harnais_Agents; bash $H/coeur/installer.sh             # HARNAIS_DEPS_SYSTEME=1 si chromium manque de bibliothèques
export HARNAIS_INSTANCE=$H/instances/AgentA__Harnais_LOT131; alias harnais=$H/coeur/bin/harnais
harnais init && harnais sante                                         # index NEO + CP initial, puis santé
(cd $H && coeur/.venv/bin/python -m pytest -q tests)                  # tests verts attendus
nohup $H/surveillance/boucle_sante.sh $HARNAIS_INSTANCE >/dev/null 2>&1 &   # boucle 5 min pendant la session
```
Ensuite : suivre `instances/<Agent>/SKILL.md` (collecter → chercher/pec → squelette → controler → captures → cp sauver).
Mémoire versionnable : `harnais memoire exporter` → `memoire_export.jsonl` (les bases SQLite, caches et index sont ignorés par `.gitignore`).

## 3. Toutes les 5 minutes : ce qui fonctionne vraiment (honnêteté)
| Mécanisme | Fréquence réelle | Statut |
|---|---|---|
| Boucle box `boucle_sante.sh` (setsid + nohup + flock) | 5 min | **active** ; survit à la fin de session ; **pas** au redémarrage de la box → relancer `demarrer_box.sh` |
| Boucle dans la VM de l'agent cloud | 5 min tant que la VM vit | à lancer par l'agent (§2.2) |
| Workflow `harnais-sante-agentX.yml` — `push` | à chaque push sur la branche | **effectif** sur une branche non par défaut |
| Workflow — `schedule: '*/5 * * * *'` et `workflow_dispatch` | — | **inertes** sur `agentA/lot-131` / `agentB/lot-130` : GitHub ne les déclenche que si le fichier existe sur la branche par défaut (`main`, interdite). Laissés pour le jour où Vial déciderait autrement. |
| Box → API publique des runs (`harnais cloud-etat`) | 5 min | **active** : alerte si le dernier run « Harnais sante » d'une branche échoue |

Source : docs.github.com, « Events that trigger workflows » — `schedule` : « will only trigger a workflow run if the workflow file exists on the default branch » ; même note pour `workflow_dispatch` ; `push` : « This includes workflows that are not merged into the default branch ».

## 4. Règle de réaction
L'agent **ne réagit qu'à `instances/<Agent>/sante/ALERTE.json`** (outil, CP ou skill en panne). Un passage vert ultérieur archive l'alerte dans `sante/alertes_resolues/`.
