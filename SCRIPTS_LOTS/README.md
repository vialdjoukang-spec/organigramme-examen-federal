# scripts_lots — scripts déterministes des agents de rédaction (v1.3)

Code Python 3 (bibliothèque standard), plus `curl` et `pdftotext`. **Aucune IA, aucune dépendance à installer.**

| Agent | Série | Script source | Script synchrone |
|---|---|---|---|
| 1 | LOT_227–237 | `agent_1/script_source.py` | `agent_1/script_synchrone.py` |
| 2 | LOT_238–248 | `agent_2/script_source.py` | `agent_2/script_synchrone.py` |

```sh
python3 agent_1/script_source.py crawl --domaines www.bag.admin.ch,www.sginf.ch --max-pages 40
python3 agent_1/script_source.py search "hyponatrémie traitement" --pec
python3 agent_1/script_source.py extrait https://www.bag.admin.ch/fr/… --requete "dose"
python3 agent_1/script_source.py pubmed "hyponatremia guideline" --max 5
python3 agent_1/script_source.py check LOTS/LOT_227/LOT_227_Appel_B_V7_Partie_1_DX.1_a_DX.2.html   # code 1 = DÉPÔT BLOQUÉ
python3 agent_1/script_synchrone.py review LOTS/LOT_227/LOT_227_Appel_A_V7_Plan_et_Liste.html
python3 agent_1/script_synchrone.py watch LOTS/LOT_227
python3 common/compteur_tokens.py log --config agent_1/config.json --lot LOT_227 --cas 1 --message "LOT_227 terminé ; suivi coché."
python3 common/compteur_tokens.py rapport --config agent_1/config.json --config agent_2/config.json
./lancer_tests.sh                 # 27 tests, sans réseau, sur LOT fictifs
python3 banc/banc_essai.py        # banc d'essai sur LOT fictif dans /tmp
```

Configuration : `agent_N/config.json` (série, cache, sorties propres ; seul `~/.scripts_lots/partage` est commun, pour les seaux de débit). Variables facultatives : `NCBI_API_KEY` (10 req/s au lieu de 3), `NCBI_ADMIN_EMAIL`.
Spécification complète : `CAHIER_DES_CHARGES_SCRIPTS_SKILLS/CAHIER_DES_CHARGES_SCRIPTS_SKILLS_GROK.md`.
