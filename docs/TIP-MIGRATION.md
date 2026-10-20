# TIP : source par SSP et asset publié

## Reprise sur la tête `2b7b9ee`

La migration est réancrée sur le littéral exact `2d9135a9340a942da3ebc24658cf0acd0aafb994426d56455c0b25c2bf1edc48`. La comparaison avec la base de l’audit initial trouve uniquement les deux URL de source S1.8 et S1.9 réparées par la PR149 ; les 3 472 parties restent identiques. La mesure et la reconstruction intégrales sont dans `audit/TIP-REPRISE-INTEGRATION-20261020.json`. Le contrôle d’empreinte reste strict. La contrelecture de cette reprise, la CI et la publication doivent être vérifiées sur le SHA final.

## Historique de l’audit initial

## Migration initiale (base `8aa1296`)

`tools/patches/0100-externaliser-tip.py` n'accepte que le littéral TIP initial d'empreinte SHA-256 `8e64b5443a5ae36b0a8a6a9f284e0803928020a0b60ba49d6e640f5d09613e0a`. Il contrôle les 248 codes dans l'ordre de SSP et les 3 472 parties, écrit un JSON lisible par SSP, puis crée un script classique synchrone. Le littéral placé dans `assets/config/tip.js` est identique octet pour octet au littéral original. En retirant le nouveau tag et en remettant ce littéral à sa position initiale, l'application reconstituée a l'empreinte SHA-256 `04571ffd9924b732a37d18b649794dcc18972b84222dcfa27e407a5ce0953490` de la base. Le nouvel HTML mesure 440 518 octets, contre 5 907 998 auparavant ; l'asset mesure 5 467 526 octets. Ces empreintes attestent uniquement la migration initiale et ne sont pas des valeurs à figer pour les futurs cours.

## Écriture et contrôle

La source canonique est `data/tip/<SSP>.json`. `assets/config/tip.js` est le produit déterministe chargé avant le script principal, également accessible en `file://` sans requête réseau. `python3 tools/cours/appliquer.py <SSP>` applique un lot documentaire audité à un seul JSON et régénère l'asset. Après une autre édition autorisée, exécuter `python3 -c "from tools.tip_data import build; build('.')"`. `python3 tools/tip_data.py` refuse fichier manquant ou supplémentaire, nombre de parties incorrect, chargement déplacé, asset divergent et asset de plus de 12 Mio. Le budget `app_v2.html` reste 6 000 000 octets.

Le flux historique `json_inject.py extract TIP` → édition de `data/TIP.json` → `inject TIP` reste possible : un instantané d'empreintes par SSP évite d'écraser une modification concurrente. Ces fichiers de travail sont ignorés par Git. Les branches anciennes avec TIP inline restent lisibles par les outils ; les nouvelles preuves de publication ALPHA exigent aussi l'asset TIP publié et sa correspondance avec le JSON du SSP. Les contrôles de doses, sources, glossaire, liens, relectures et 14 empreintes de parties continuent de lire tout TIP. Une modification des JSON sans régénération de l'asset fait échouer la CI.

## Contrôle indépendant et anciens lots

Le contre-audit technique est consigné dans `audit/TIP-EXTERNALISATION-CONTRE-AUDIT-20261020.json` et son rapport Markdown. Les preuves de publication vérifient aussi les vrais éléments `script` de l'HTML : chargement classique avant le script principal, sans doublon ni déclaration TIP inline. Une preuve HTTP et des empreintes exactes ne suffisent pas si l'HTML est inexécutable. Un cours doit contenir une liste de quatorze textes, pas seulement une valeur de longueur quatorze.

Pour reprendre un lot clinique d'une ancienne branche inline, conserver le fichier `tools/cours/lots/<SSP>.json` relu et ses quatorze empreintes `avant_sha256`, puis utiliser l'outil `appliquer.py` de la branche actuelle sur le shard correspondant. Ne pas reprendre l'ancien `app_v2.html` ni son TIP complet. L'outil refuse un cours modifié depuis les empreintes et préserve les DD/fondamentaux ; le même lot donne le même objet final en fixture inline et externalisée. L'intégration reste séquentielle dans chaque worktree ; le contrôle de brouillon par SSP ne constitue pas un verrou entre processus simultanés.

Le petit lecteur `tools/audit_examen/analyse.py` lit désormais les sources publiées via le lecteur canonique et écrit son résultat local dans `.cache/audit_examen/stats.json`.
