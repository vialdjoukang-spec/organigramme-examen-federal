# Conscience embarquée

Outil du rédacteur, pas un audit. Trois contrôles déterministes, en Python, sans appel de modèle. Il s'exécute pendant la rédaction, après un fichier (ou une section), avant `certitude_redaction.py` et avant `porte_zero_jeton.py avant redacteur`.

| Nom | Ce qu'elle regarde |
|---|---|
| conscience linguistique | formes fautives, sigles non développés, unités (espace, µg, mmol/l) |
| conscience médicale | cohérence des seuils, définitions de SOFA et qSOFA, plages de plausibilité, éléments centraux absents |
| conscience posologique | dose extraite du corps, comparée au cache AIPS local |

La terminologie est linguistique. La conscience médicale couvre la cohérence clinique, les définitions et les seuils.

Un fait central absent donne un ordre « SOURCER … plutôt que retirer ». On ne retire pas le fait pour faire taire l'ordre.

## Appel à coller dans le prompt du rédacteur

Après chaque fichier HTML, avant la certitude et avant la porte :

```
python3 grok-LOTS-html/outils/conscience/conscience.py fichier CHEMIN.html
```

Lire toute la sortie (30 lignes au plus). Code de sortie 1 : au moins un BLOQUANT, le corriger et relancer. Un SIGNAL « SOURCER » se traite en retrouvant la source, pas en supprimant l'élément. Puis seulement :

```
python3 grok-LOTS-html/outils/certitude_redaction.py CHEMIN.html --preuves DOSSIER --lot LOT_XXX
python3 grok-LOTS-html/outils/porte_zero_jeton.py avant redacteur CHEMIN.html --lot LOT_XXX
```

En fin de LOT (éléments attendus pour tout le SSP : Ottawa, Fleischner, seuils 0/1 h) :

```
python3 grok-LOTS-html/outils/conscience/conscience.py lot LOT_XXX
```

Section seule (linguistique et posologie limitées à l'ancre ; l'absence médicale reste jugée sur le fichier) :

```
python3 grok-LOTS-html/outils/conscience/conscience.py fichier CHEMIN.html --ancre p11
```

`--tout` enlève le plafond de 30 lignes (mesure, pas le prompt).

## Sortie

```
CONSCIENCE LOT_154_Phase_B_V0_DX.10.html — 1 ordre (0 BLOQUANT, 1 SIGNAL) — 0.02 s
SIGNAL conscience médicale : SOURCER S1Q3T3 et la fréquence lue — sourcer plutôt que retirer.
```

- `BLOQUANT` : dose au-dessus du plafond AIPS lu, unité incohérente (µg/mg), valeur physiologiquement impossible.
- `SIGNAL` : le reste, y compris « SOURCER ».
- Code 0 : aucun BLOQUANT. Code 1 : BLOQUANT. Code 2 : usage.
- Priorité d'affichage : BLOQUANT, puis conscience médicale, puis posologie, puis linguistique. Au-delà : une ligne « ordres masqués ».

## Juste milieu

Vérification ciblée, pas une relecture. Mesuré : Phase A de LOT_134 en 0,02 s ; un LOT de 11 fichiers en moins de 0,12 s. Les fenêtres de citation (popover) sont ignorées, pour ne pas juger le corpus source comme la leçon. L'insécable n'est pas exigé à chaque nombre (trop de bruit) : seule l'unité collée au chiffre l'est. Hunspell français n'est pas installé ici (bibliothèque anglaise seulement, pas de `fr_FR.dic`) : le volet orthographe externe reste inactif, le lexique local suffit. Un plafond AIPS n'est codé que si la phrase de posologie a été lue dans `ressources_ia/aips/fi_fr/` ; sinon SIGNAL « plage non extraite », jamais un BLOQUANT inventé.

## Données

`donnees/lexique_formes.json`, `sigles.json`, `bornes.json` (plausibilité, statut À vérifier comme seuil clinique), `elements_centraux.json` (indexé par le code SSP du catalogue, celui que reprend le brief de `contexte_lot.py`), `doses.json` (numéro AIPS et date du corpus 2026-10-08), `specialites.json` (noms du même index, pas des posologies).

`python3 grok-LOTS-html/outils/conscience/autotest.py` et `--backtest`. Le backtest n'écrit que `resultats_backtest.json` dans ce dossier.
