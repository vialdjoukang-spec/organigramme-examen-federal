# Format d’auteur v2 — une spécialité = un fichier

Chaque spécialité vit dans `data/specialites/<id>.js`. Le corps de `JEU.specialite( … )` est du **JSON strict** : les outils Node (validateur, couverture, audit, planche) le lisent sans exécuter de code. Crée le squelette vide et valide avec :

```
node tools/nouvelle-specialite.js <id>        # un fichier, id pris dans data/parcours.js
node tools/nouvelle-specialite.js --tous dir/ # toutes les spécialités du plan sans fichier (40 aujourd’hui)
```

Puis ajoute la ligne `<script src="data/specialites/<id>.js"></script>` dans `index.html`, après `js/engine/registry.js`.

**Règle des sources.** Tout contenu clinique vient de sociétés médicales suisses, d’universités, de facultés ou d’hôpitaux universitaires suisses. Un hôpital cantonal compte comme source **complémentaire** (la fiche l’affiche). Les sciences fondamentales et la pharmacologie peuvent citer des références internationales libres (catégorie `pharmaco`). On n’ouvre ni ne réutilise aucun cours ni lot existant du dépôt. Chaque source lue entre dans `data/sources.js` avec `titre`, `url`, `lu_le` (AAAA-MM-JJ), `type` (`suisse` ou `pharmaco`) et, pour une source suisse, sa `categorie`.

## 1. Affirmation

```json
{ "t": "Phrase complète, en propres termes.", "s": ["id-source"] }
```

- Sans source lue : `"s": []` et « À vérifier » dans `t`. Le validateur refuse toute autre affirmation sans source.
- Rubrique clinique (démarche à suivi) : au moins une source suisse, ou « À vérifier ».
- Dose : interdite sauf `"dose": { "verbatim": "extrait mot pour mot", "url": "https://www.swissmedicinfo.ch/…", "lu_le": "AAAA-MM-JJ" }`, relue par un médecin.
- `"quiz": false` exclut l’affirmation des questions automatiques (constat vrai pour plusieurs pathologies).
- `"echelon": 1` (fondamentaux seulement) place l’affirmation à l’échelon 1 « Fondamental » ; par défaut, les fondamentaux sont à l’échelon 2 « Mécanisme ».

## 2. Pathologie (catalogue)

```json
{ "id": "stemi", "nom": "…", "carte": "stemi", "ssp": ["S2.5", "F2.6"],
  "frequente": true | false | "à vérifier", "grave": true | false | "à vérifier",
  "justif": [ affirmation, … ] }
```

PROFILES ne publie pas de liste de maladies : chaque spécialité déclare son catalogue sourcé et le rattache aux codes SSP officiels (`data/profiles-ssp.js`, 248 SSP lues le 17.11.2026 sur smifk-cims.ch). `catalogue.complet` passe à `true` quand le catalogue est jugé exhaustif. Un drapeau fréquente/grave affirmé (`true`) demande une justification (avertissement sinon).

## 3. Carte et fiche en 8 rubriques

`{ id, specialite, type: "pathologie"|"examen"|"traitement"|"geste"|"fondamental", classe, nom, court, cle, rubriques, contre, pieges, noteFrequence, sources }`

| # | Rubrique | Échelon | Contenu |
|---|---|---|---|
| 1 | `fondamentaux` | 1–2 | structure, fonction, mécanisme |
| 2 | `demarche` | 3 | signe clé, drapeaux rouges |
| 3 | `differentiels` | 4 | `{ "dx": "…", "tue": true, "t": "…", "s": [] }`, ceux qui tuent d’abord |
| 4 | `exploration` | 5 | l’examen qui tranche, l’examen inutile |
| 5 | `diagnostic` | 6 | critères suisses |
| 6 | `priseEnCharge` | 7 | du général au spécifique, sans abus |
| 7 | `suivi` | 7 | hospitaliser, adresser, revoir |
| 8 | `explication` | — | complétée automatiquement par les messages des cas |

Une carte d’action peut mettre `{ "t": "Sans objet pour une carte d’action.", "s": [], "na": true }` dans une rubrique qui ne la concerne pas.

## 4. Cas

```json
{ "id": "…", "specialite": "…", "mode": "urgence"|"consultation"|"final", "chrono": 600,
  "pathologies": ["…"], "titre": "…", "intro": "…", "patient": { … }, "dossier": { … },
  "pvInitial": 100, "debrief": "…", "piege": "… (cas final)",
  "etapes": [ { "id": "e1", "titre": "…", "consigne": "…", "phase": "trier",
                "pathologie": "…", "adversaire": "<carte>", "main": ["…"], "objectifs": ["…"],
                "regles": { "<carte>": { "verdict": "bon"|"erreur"|"inutile"|"neutre"|"info",
                                         "gravite": "dangereuse"|"mineure", "msg": "1 à 3 phrases.",
                                         "fiche": "<carte>", "revele": "<examen>", "mortel": true,
                                         "avant": { "requiert": ["…"], "verdict": "neutre", "msg": "…" } } } } ] }
```

- 3 à 5 duels, phases dans l’ordre `trier → explorer → differencier → diagnostiquer → traiter` ; main ≤ 9 cartes ; objectifs dans la main.
- Chrono obligatoire en Urgence et en cas final ; la Consultation est sans chrono et pénalise l’examen inutile.
- Un cas final combine ≥ 2 pathologies et décrit son `piege`.
- `mortel: true` sur l’erreur qui oublie un différentiel qui tue (alimente les angles morts).

## 5. Questions rédigées (facultatif)

`"questions": [ { "id", "pathologie", "echelon": 1–7, "enonce", "choix": [ { "t", "juste": true } … ], "s": ["id-source"] } ]` — au moins 2 choix, un seul juste. Sans questions rédigées, le moteur en dérive de chaque affirmation sourcée et non ambiguë.

## 6. Règle de couverture exhaustive et rapport

`node tools/couverture.js` écrit `docs/couverture/` :

- `couverture.json` : `{ genere_le, profiles, regles, specialites: [ { id, nom, lot, statut, note, totaux: { pathologies, couvertes, partielles, manquantes, cas, cartes, affirmations, aVerifier, tauxAVerifier }, sspTouchees, pathologies: [ { id, nom, ssp, frequente, grave, exigeUrgenceEtConsultation, cas: { urgence, consultation, final }, echelonsSources, statut, besoins } ] } ], sspNonTouchees }` ; une spécialité sans fichier y figure avec `statut: "catalogue à produire"`.
- `INDEX.md` : tableau par spécialité ; `<id>.md` : détail par pathologie (statut, cas, échelons sourcés, ce qui manque).

Statuts : **couverte** = cas exigés présents (≥ 1 cas ; Urgence et Consultation si fréquente ou grave, « à vérifier » compte comme oui) et 7 échelons sourcés (source suisse hors fondamentaux) ; **partielle** = au moins un cas, exigences incomplètes ; **manquante** = aucun cas.

## 7. Contrôles avant push

```
node tests/valider.js          # 0 erreur exigée
node tests/test_moteur.js      # moteur
python3 tests/qa.py            # navigateur
node tools/couverture.js && python3 tools/planche.py <id>
```
