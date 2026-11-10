# Claude — dossier de production

- Une leçon = une seule copie dans tout le dépôt : `Claude/LOT_XXX/LOT_XXX_Phase_A_V0.html` et `…Phase_B_V0_DX.i.html`.
- `_outils/` : copies de `detecteur_lots.py` (version la plus avancée de chaque leçon, main + toutes les branches), `consolider.py`, `progression.py`, `controle3.py`.
- `Progression_PR_Claude.html` : jauges, régénérées après chaque PR :

```bash
python3 Claude/_outils/detecteur_lots.py . --rafraichir --sortie /tmp/carte_lots.json
```
```bash
python3 Claude/_outils/progression.py --carte /tmp/carte_lots.json --ia Claude --sortie Claude/Progression_PR_Claude.html
```
