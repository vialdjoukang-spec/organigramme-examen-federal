# STATUT · LOT 129 · DX pairs · agentB/lot-129-p2

Note d'arrêt, 9 novembre 2026. Rien n'a été supprimé. Le travail reprend plus tard sur cette branche.

Commit déjà poussé avant cette note : `2d12500b` (« LOT_129 : recopie les posologies AIPS des DX pairs, Gutron au n° 44977. »).

## DX finis sur cette branche

Les cinq HTML pairs sont présents, dans la bande 100–150 Ko, avec fenêtres et tableau de biologie au point 9. Contrôle de forme sans critique au moment de l'arrêt. Unicité interne d'environ 97 % ou plus. Les posologies citées ont été recopiées depuis `origin/grok/lots:ressources_ia/aips/fi_fr/`.

| DX | Fichier | Octets | Spécialités dont la Posologie est recopiée |
|---|---|---|---|
| DX.2 | `LOT_129_Phase_B_V0_DX.2.html` | 149 259 | Seresta 32497, Campral 53090, Naltrexin 56109, Antabus 15104, Benerva 10989 et 25636 |
| DX.4 | `LOT_129_Phase_B_V0_DX.4.html` | 149 143 | Seresta 32497 (pas d'indication cannabis ; contre-indication avant 12 ans) |
| DX.6 | `LOT_129_Phase_B_V0_DX.6.html` | 149 494 | Seresta 32497, Valium 28840 |
| DX.8 | `LOT_129_Phase_B_V0_DX.8.html` | 149 134 | Seresta 32497 (sommeil), Circadin 59311 |
| DX.10 | `LOT_129_Phase_B_V0_DX.10.html` | 149 106 | Seresta 32497, Campral 53090, Naltrexin 56109, Antabus 15104, Benerva 10989 et 25636, Valium 28840, Gutron 44977 |

## Corrections déjà faites

- Gutron n'est plus déclaré absent. Le n° lu est 44977, pas 44976. La mention « absent du corpus » a été retirée. MIDODRIN SUBSTIPHARM (69384) n'est cité dans aucun DX.
- Seresta : le sevrage alcoolique est dans la notice, « 15-30 mg, 3-4 fois par jour ».
- Naltrexin : le demi-comprimé du premier jour est le paragraphe opioïdes, pas la dose d'alcool de 50 mg.
- La « prescription spéciale » n'est pas dans la notice 32497.
- Aucune dose létale n'est écrite. Aucun médicament cité ne reste sans notice quand il est dans le corpus.

## Restant

La consigne d'usage reçue juste avant l'arrêt n'est pas faite : elle demandait des fichiers à 53–64 Ko à porter en 100–150 Ko, au moins 90 % de phrases uniques, et aucune phrase commune entre fichiers. Sur le disque, les cinq HTML sont déjà dans la bande 100–150 Ko. En revanche, des phrases identiques restent entre fichiers, surtout DX.2 et DX.10, parce que les mêmes citations AIPS y sont recopiées mot pour mot. Cette passe d'unicité croisée n'a pas été commencée.

Les DX impairs ne sont pas sur cette branche.

Les corps sources sont dans `AgentB__LOT_129/preuves/corps_dx{2,4,6,8,10}.html`.
