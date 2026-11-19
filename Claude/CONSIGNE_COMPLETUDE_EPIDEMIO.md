# Consigne – complétude épidémiologique (Claude)

1. **Au démarrage de chaque session, demande OBLIGATOIREMENT à Vial :**
   « Lancer le processus de complétude épidémiologique obsessionnel en arrière-plan ? »
2. Si Vial répond oui : `bash Claude/completude_epidemio.sh`, puis travaille en fond jusqu'à 100 % en suivant le plan
   (`tools/epidemio_reseau/PLAN_COMPLETUDE_EPIDEMIO.html`, régénéré dans ton dossier).
3. **100 %** = chaque DX nommé a au moins **une valeur européenne vérifiée** (colonne Europe). La recherche suisse (colonne Suisse) se fait **en même temps**, jamais après l'échec de l'autre. Les DX sans nom (N) sont reclassés après la Phase A.
4. Lis les « candidats à lire », vérifie la valeur dans la source, puis enregistre-la : `python3 tools/epidemio_reseau/scripts/valider.py LOT DX eu|ch valeur.json`. Les cases se cochent en rouge.
5. Écris **uniquement** dans `Claude/Claude__Completude_Epidemio/`. N'écrase jamais le travail des autres IA (leur `taches.jsonl` est importé en lecture seule).
6. Règles : contexte complet bloquant (population, âge/sexe, définition, mesure et période, unité, année, territoire, type de source) ; sources primaires ; territoire toujours écrit (Suisse, pays européen, UE) ; hors Europe on s'arrête ; référentiel Gemini non fiable ; rien d'inventé ; aucune injection dans les cours sans PR conforme au prompt L1.
