# scripts_lots — scripts déterministes des agents de rédaction (v1.4 — 8 agents, 2 équipes)

Code Python 3 (bibliothèque standard), plus `curl` et `pdftotext`. **Aucune IA, aucune dépendance à installer.**

| Agent | Équipe | Chapitre | Série | Scripts | État propre |
|---|---|---|---|---|---|
| 1 | 1 | Appel A + Partie 1 (LOT_227–228 entiers) | LOT_227–237 | `agent_1/` | `~/.scripts_lots/agent_1/` |
| 3 | 1 | Partie 2 | LOT_229–237 | `agent_3/` | `~/.scripts_lots/agent_3/` |
| 5 | 1 | Partie 3 | LOT_229–237 | `agent_5/` | `~/.scripts_lots/agent_5/` |
| 7 | 1 | Partie 4 | LOT_229–237 | `agent_7/` | `~/.scripts_lots/agent_7/` |
| 2 | 2 | Appel A + Partie 1 (LOT_238 et LOT_239 entiers) | LOT_238–248 | `agent_2/` | `~/.scripts_lots/agent_2/` |
| 4 | 2 | Partie 2 | LOT_240–248 | `agent_4/` | `~/.scripts_lots/agent_4/` |
| 6 | 2 | Partie 3 | LOT_240–248 | `agent_6/` | `~/.scripts_lots/agent_6/` |
| 8 | 2 | Partie 4 | LOT_240–248 | `agent_8/` | `~/.scripts_lots/agent_8/` |

Chaque `agent_N/` contient deux enveloppes minces (`script_source.py`, `script_synchrone.py`) et sa propre `config.json`, générées par `python3 generer_configs.py`.

```sh
python3 agent_1/script_source.py crawl --domaines www.bag.admin.ch,www.sginf.ch --max-pages 40
python3 agent_1/script_source.py search "hyponatrémie traitement" --pec
python3 agent_1/script_source.py extrait https://www.bag.admin.ch/fr/… --requete "dose"
python3 agent_1/script_source.py pubmed "hyponatremia guideline" --max 5
python3 agent_1/script_source.py check /workspace/agent1/LOT_229/LOT_229_Appel_B_V7_Partie_1_DX.1_a_DX.2.html   # code 1 = DÉPÔT BLOQUÉ
python3 agent_1/script_synchrone.py review /workspace/agent1/LOT_229/LOT_229_Appel_A_V7_Plan_et_Liste.html
python3 agent_1/script_synchrone.py watch /workspace/agent1/LOT_229
python3 common/compteur_tokens.py log --config agent_1/config.json --lot LOT_229 --cas 1 --message "LOT_229 Appel A + Partie 1 déposés."
python3 common/compteur_tokens.py rapport --config agent_1/config.json --config agent_2/config.json   # … jusqu'à agent_8
python3 agent_3/script_synchrone.py review /workspace/agent3/LOT_229/LOT_229_Appel_B_V7_Partie_2_DX.3_a_DX.5.html --appel-a /workspace/agent3/LOT_229/LOT_229_Appel_A_V7_Plan_et_Liste.html
./lancer_tests.sh                 # 39 tests, sans réseau, sur LOT fictifs
python3 banc/banc_essai.py        # banc d'essai sur LOT fictif dans /tmp
```

Configuration : `agent_N/config.json`. **Loi d'indépendance absolue (v1.4)** : aucun chemin inscriptible commun à deux agents — cache, retours, compteur et état des seaux (`shared_state_dir` = `~/.scripts_lots/agent_N/etat`) sont propres à chaque agent ; `~/.scripts_lots/partage` n'est plus utilisé (conservé tel quel, non supprimé). `pubmed.mcp_url` vide : aucun serveur MCP local partagé, E-utilities directement.

Champs facultatifs v1.4 (rétrocompatibles ; une configuration v1.3 sans eux fonctionne comme avant) : `equipe`, `chapitre`, `lots` (liste), `parties_autorisees` (liste de `A`, `P1`…`P4`, ou dictionnaire par LOT avec clé `*`), `dossier_travail` (chemin ou liste). `check` et `review` refusent (code 2, « REFUS (périmètre) ») un fichier hors LOT, hors Partie ou hors dossier de travail ; `review --appel-a` n'accepte que l'Appel A du même LOT ; `watch` ignore les fichiers d'autres chapitres. Avec `equipe`, `config.py` refuse tout chemin inscriptible hors d'un dossier `agent_N/` ou dans un dossier `partage`.

Budgets externes partagés en 8 (les huit agents ensemble restent sous les anciennes limites globales) :

| Ressource | Ancienne limite globale (2 agents) | Par agent (v1.4) | Total 8 agents |
|---|---|---|---|
| LanguageTool, requêtes | 10 req/min | 1 req/min (10 // 8, arrondi inférieur) ; 1 requête par passage | 8 req/min |
| LanguageTool, octets | 60 000 o/min ; 18 000 o/requête | 7 500 o/min ; 6 000 o/requête (rafale ≤ 7 200 o) | 60 000 o/min ; rafale ≤ 57 600 o |
| NCBI E-utilities sans clé | 3 req/s | 0,375 req/s (1 requête / 2,7 s ; capacité 1 jeton) | 3 req/s |
| NCBI E-utilities avec `NCBI_API_KEY` | 10 req/s | 1,25 req/s | 10 req/s |
| Par domaine (HTTP) | 1 req/s | 0,125 req/s (1 requête / 8 s par domaine ; capacité 1 jeton) | 1 req/s |

Conséquence : `crawl` est 8 fois plus lent par domaine (≈ 11 pages par domaine en 90 s) ; le recul après 429 est désormais propre à l'agent. Variables facultatives : `NCBI_API_KEY`, `NCBI_ADMIN_EMAIL`.
Spécification complète : `CAHIER_DES_CHARGES_SCRIPTS_SKILLS/CAHIER_DES_CHARGES_SCRIPTS_SKILLS_GROK.md`.
