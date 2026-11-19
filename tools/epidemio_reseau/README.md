# Réseau épidémiologique – complétude bispatiale (Europe + Suisse)

Scripts locaux et gratuits. Pour chaque DX nommé des 2 480 DX, deux recherches lancées **en même temps** :
**Europe** (général, objectif : au moins une valeur vérifiée par DX) et **Suisse** (spécifique). Deux colonnes séparées,
chacune avec son contexte complet. Hors Europe, on s'arrête.

- `completude.sh` : chaîne complète, idempotente (SQLite WAL, checkpoints, cache disque). Lancée par `<IA>/completude_epidemio.sh`.
- `scripts/connecteurs.py`, `pipeline.py` : valeurs suisses (OFS, OFSP-IDD, ONEC, Obsan/MonAM).
- `scripts/applicabilite.py` : classes A/B/C/N.
- `scripts/eurostat_cod.py`, `eurostat_ehis.py` : Eurostat (causes de décès UE-27 et Suisse ; enquête EHIS 2019 UE-27), valeurs vérifiées automatiquement avec contexte complet.
- `scripts/recherche.py` : Europe + Suisse en parallèle (Orphanet/Orphadata CC BY 4.0, Europe PMC/PubMed, Wikidata pour le nom anglais) ; candidats + phrases chiffrées des résumés.
- `scripts/valider.py` : enregistre une valeur lue à la source ; refuse un contexte incomplet ou un territoire hors Europe.
- `scripts/plan.py` : `PLAN_COMPLETUDE_EPIDEMIO.{html,md}` (cases rouges, compteur t / n) + `taches.jsonl`.
- `etat/` : instantané partagé (plan, tâches) ; chaque IA écrit seulement dans `<IA>/<IA>__Completude_Epidemio/`.

**100 %** = chaque DX nommé a au moins une valeur européenne vérifiée (8 colonnes de contexte : population, âge/sexe, définition,
mesure et période, unité, année, territoire, type de source). Un candidat trouvé automatiquement n'est jamais une valeur vérifiée.
Référentiel Gemini non fiable. Aucune injection dans les cours sans PR conforme au prompt L1.
