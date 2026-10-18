# tools/ · Héphaïstos

Ces scripts permettent de travailler sur `app_v2.html` (5,4 Mo) sans jamais le lire en entier.
Ils utilisent `str.find`, car les expressions régulières expirent sur des lignes de plusieurs millions de caractères.

| Script | Rôle | Commande |
|---|---|---|
| `slim.py` | Il écrit une vue de code sans données (TIP, NOT, GES remplacés par un repère) dans `.cache/app_v2.slim.html`, soit environ 2,2 % du fichier. | `python3 tools/slim.py` |
| `json_inject.py` | Il extrait une constante JSON stricte dans `data/<NOM>.json`, puis la réinjecte compactée ; `check` vérifie l’aller-retour à l’octet. | `python3 tools/json_inject.py extract TIP` |
| `patches/` | Chaque modification de code s’écrit comme un patch à ancrage unique, rejouable. `0001` et `0002` reproduisent exactement `app_v2.html` à partir de `orig/app.html`. | `APP_FILE=/tmp/copie.html python3 tools/patches/0001-….py` |
| `check_hash.py` | Il vérifie que l’empreinte SHA-256 de `orig/app.html` reste `1e067c6ecb82190d…` (interdit I1). | `python3 tools/check_hash.py` |
| `budget.py` | Il refuse un `app_v2.html` de plus de 6 Mo et une image de plus de 200 Ko. | `python3 tools/budget.py` |
| `html_check.py` | Il compare la sortie du validateur Nu à `qa/html-baseline.json` et refuse toute erreur nouvelle. | voir `.github/workflows/ci.yml` |
| `links_changed.py` | Il liste les URL ajoutées ou modifiées depuis la branche de base, pour lychee. | `python3 tools/links_changed.py origin/main` |
| `ck_build.py` | Il valide data/ck (schémas, renvois, chaîne G5) et compile assets/ck/*.js ; `--check` échoue si la sortie n’est pas à jour. | `python3 tools/ck_build.py` |
| `lyncee.py` | Il détecte les termes médicaux non définis (G4) contre `qa/termes-baseline.json`, qui ne peut que baisser. | `python3 tools/lyncee.py --json .cache/lyncee.json` ; recensement main + branches ouvertes, par fréquence : `python3 tools/lyncee.py --branches 'feat/*' --top 150` |
| `audit/niveau1.py` | Il exécute les huit contrôles G1 à G8 de l’audit médical et écrit l’artefact des signalements. | `python3 tools/audit/niveau1.py --sortie qa/audit-flags.json` |
| `aletheia.py` | Il exécute G1, G2 et G3 (doses, sources, domaines). | `python3 tools/aletheia.py` |
| `audit/rapport_fautes.py` | Il régénère « Rapport d’audit médical : les fautes corrigées » depuis `qa/audit/fautes.jsonl`. | `python3 tools/audit/rapport_fautes.py` |
| `nc_svg_check.py` | Il contrôle les schémas des nerfs (couches, ressources, crédits, licence dérivée). | `python3 tools/nc_svg_check.py` |
| `templates/veille-squelette.yml` | Il sert de squelette de veille planifiée pour Argos. | à copier dans `.github/workflows/` |

## Commande de test (remise à Janus)

```bash
python3 tests/run_tests.py          # 43 contrôles Playwright ; n’affiche que le décompte et les échecs
python3 tests/test_gardes.py        # 5 tests des gardes (empreinte, budget, HTML)
```

Variables : `APP_FILE` (fichier testé, par défaut `app_v2.html`), `CHROME_PATH` (Chrome local ; sinon le Chromium de Playwright), `SHOTS_DIR` (captures, par défaut `qa/shots/`, ignoré par git).

## Règle

Aucun script n’ajoute de dépendance d’exécution à l’application, et aucun n’utilise de service payant.
