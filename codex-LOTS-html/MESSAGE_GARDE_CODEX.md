Codex, ordre de Vial (31.10.2026) : garde temps réel obligatoire, sans exception.

1. Récupère la garde déposée par Claude et installe-la :
```
git fetch origin production-v2
git checkout origin/production-v2 -- codex-LOTS-html/outils/garde_temps_reel.py
python3 codex-LOTS-html/outils/garde_temps_reel.py installer
python3 codex-LOTS-html/outils/garde_temps_reel.py controle
```
2. Lance-la en permanence, en arrière-plan, pour toute la session : `nohup python3 codex-LOTS-html/outils/garde_temps_reel.py boucle --intervalle 60 >> codex-LOTS-html/GARDE_TEMPS_REEL.log 2>&1 &`
3. Avant chaque leçon et après chaque push, lis `codex-LOTS-html/GARDE_TEMPS_REEL.json`. Couple [Harnais + Routage] ROUGE = tu arrêtes toute production et tu corriges les lignes ✗ d'abord (la garde resynchronise seule le harnais depuis production-v2 et relance la veille du routage ; le reste est à toi).
4. Tu produis tes LOTS de la plage 018–133 dans l'ordre que donne `garde_temps_reel.py prochaine`, sans t'arrêter, jusqu'au dernier.
5. Quand tous sont complets, la garde passe d'elle-même en **audit Astra** : tu audites chaque leçon en passe indépendante gpt-6-astra (consignée `auditeur-medical`), tu corriges en place, `verif_refonte` VERT, puis `garde_temps_reel.py audite <fichier>`. À la fin du cycle, un nouveau cycle recommence. Tu ne t'arrêtes jamais.
6. Commite à chaque push `GARDE_TEMPS_REEL.json`, `GARDE_TEMPS_REEL.log`, `AUDIT_ASTRA.json`, `.veille_routage` et `ROUTAGE_CODEX.jsonl`. GitHub vérifie ta branche toutes les 5 minutes et t'écrit « @codex GARDE TEMPS RÉEL » sur la PR « Pilote Codex » dès que le couple est rouge.
