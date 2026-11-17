# Note de continuité — jeu-revision (Phase 0 terminée, 17.11.2026)

Lis d’abord `docs/PROMPT_PROJET.md`, `docs/PLAN_PRODUCTION.md` et `docs/PROGRESSION.md` (font foi), puis cette note, puis `docs/FORMAT_AUTEUR.md`.

## Interdits permanents
- N’ouvre, ne lis, ne convertis ni ne réutilise **aucun** cours ou lot du dépôt hors `jeu-revision/` (data/tip, data/ck, LOT_*, grok-LOTS-html, contenu SSP audité…). Le convertisseur data/tip est **annulé** (jamais écrit).
- Clinique : sources suisses seulement (sociétés, universités, facultés, hôpitaux universitaires ; hôpital cantonal = complémentaire). Fondamentaux et pharmacologie : références internationales libres permises.
- Aucune dose sans extrait swissmedicinfo mot pour mot daté. « À vérifier » sur tout ce qui n’a pas de source lue.
- Commit seulement dans `jeu-revision/`, identité `vialdjoukang-spec <vial.djoukang@gmail.com>`, fetch + pull --rebase avant chaque push, jamais de force-push.

## Fait (Phase 0)
- Moteur v2 : schéma 8 rubriques + validateur (`js/engine/schema.js`), registre, duel (modes Urgence, Consultation, Entraînement, cas final, examen blanc ; pénalités dangereuse −30, mineure −10, inutile −5 PV et +1 min ; chrono ; étoiles 0–3), confiance obligatoire Sûr/Hésitant/Au hasard (S/H/A).
- Traqueur event-sourcé (`js/engine/progression.js`, clé `revmed.progression.v2`) : coups (carte, échelon, réponse, confiance, temps, gravité), carte de chaleur, calibration et excès de confiance, angles morts, vitesse, Leitner 5 boîtes, Ronde 20 min, maîtrise J0/J+1/J+7 + rappel J+30, grades, préparation par domaine PROFILES, export/import JSON versionné avec fusion sans perte, migration du journal v1.
- Questions à 7 échelons (`js/engine/quiz.js`) ; Fondamentaux et Ronde (`js/ui/quiz-ui.js`).
- Parcours : 41 salles (lots A–G), cycle Fondamentaux → Consultation → Urgence → cas final, verrou à 2 étoiles de moyenne, mode Entraînement ; examen blanc (structure, seuil « À vérifier »).
- Son Web Audio synthétisé, muet mémorisé, coupé par défaut en mouvement réduit.
- Outils : `tools/nouvelle-specialite.js`, `tools/couverture.js`, `tools/planche.py`, `tests/valider.js`, `tests/test_moteur.js`, `tests/qa.py`, `tests/audit.js`.
- Cardiologie migrée au schéma v2 (6 pathologies, 18 cartes, 1 cas Urgence) ; planche `planches/cardiologie.html`.

## Prochaine étape : Lot A, dans cet ordre
1. cardiologie (compléter : catalogue exhaustif, cas Consultation, NSTEMI, EP, péricardite, cas final)
2. angiologie
3. pneumologie
4. gastro-entérologie et hépatologie
5. néphrologie
6. endocrinologie et diabétologie
7. hématologie
8. oncologie
9. infectiologie
10. rhumatologie
11. immunologie et allergologie
12. gériatrie

Au plus 3 spécialités en parallèle, un fichier chacune. Par spécialité : catalogue sourcé lié aux SSP → cartes 8 rubriques → cas (Urgence ET Consultation pour chaque pathologie fréquente ou grave) → cas final → `node tests/valider.js` → `node tools/couverture.js` → `python3 tools/planche.py <id>` → audit indépendant → push.

## Liste complète des spécialités (data/parcours.js)
- A : cardiologie, angiologie, pneumologie, gastro-hepatologie, nephrologie, endocrinologie-diabetologie, hematologie, oncologie, infectiologie, rhumatologie, immunologie-allergologie, geriatrie
- B : neurologie, psychiatrie, pedopsychiatrie, addictologie
- C : pediatrie, neonatologie, gynecologie, obstetrique
- D : chirurgie-viscerale, traumatologie-orthopedie, urologie, chirurgie-vasculaire, chirurgie-thoracique-cardiaque, neurochirurgie
- E : orl, ophtalmologie, dermatologie-venereologie
- F : medecine-urgence, anesthesiologie, medecine-intensive, toxicologie, medecine-palliative
- G : medecine-famille, medecine-voyages, medecine-travail, medecine-physique, prevention-sante-publique, medecine-legale, genetique-medicale

## À confirmer par Vial
- Lecture des grades : Externe < 25 %, Interne ≥ 25 %, Chef de clinique ≥ 50 %, Médecin cadre ≥ 75 %, « prêt pour l’examen blanc » ≥ 90 %.
- Poids PROFILES provisoire = nombre de SSP rattachées (≥ 4 élevé, 3 moyen, ≤ 2 ciblé). À vérifier.
- Seuil de réussite de l’examen blanc : À vérifier.
- Règle « pas d’antithrombotique avant exclusion d’une dissection » : aucune formulation suisse explicite trouvée, reste « À vérifier ».

## Pièges connus
- Les fichiers de spécialité sont du JSON strict : pas de virgule finale, pas de commentaire dans le corps.
- `h()` aplatit les tableaux imbriqués (`flat(Infinity)`) ; garder cette propriété.
- Tests Node : les tableaux du contexte vm ne passent pas `deepStrictEqual` ; comparer en JSON.
- Pas de rsync sur la machine de travail : utiliser tar.
