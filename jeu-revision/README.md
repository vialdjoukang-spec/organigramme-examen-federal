# Internat · Révision PROFILES — révision médicale par duels de cartes

Prototype jouable dans un navigateur, sans installation. Tu joues l’interne. Chaque cas clinique se gagne en **duels de cartes** : tu associes le bon geste ou le bon médicament à la bonne situation. Chaque erreur ouvre automatiquement la **fiche** en 8 rubriques ; chaque coup alimente le **tableau de bord** (carte de chaleur, calibration, angles morts, répétition espacée).

Public visé : préparation de l’examen fédéral suisse de médecine humaine (format PROFILES) et pratique clinique en Suisse.

> Prototype pédagogique. Le contenu sert à réviser ; ce n’est pas un protocole et il ne remplace ni un protocole local ni l’avis d’un médecin. Aucune dose n’est affichée. Tout contenu sans source suisse lue porte la mention « À vérifier ».
>
> **Relecture médicale** : la validation médicale du contenu relève de Dr Vial Djoukang, médecin, auteur et responsable du projet. Le prototype a été rédigé avec un assistant et attend cette relecture avant tout usage.

## Catalogue et veille

- **Catalogue des salles** : ouvre [`catalogue.html`](catalogue.html) (ou la [version publiée](https://vialdjoukang-spec.github.io/organigramme-examen-federal/jeu-revision/catalogue.html)). Il liste les 63 spécialités et disciplines du plan, indique celles qui sont déjà jouables, et propose un aperçu d'une minute avant d'entrer dans l'Arène. Ce catalogue se régénère par `python3 tools/progression.py render`.
- **Veille** : ouvre la [page publique](https://vialdjoukang-spec.github.io/organigramme-examen-federal/veille/) (une copie locale se trouve dans [`veille/index.html`](veille/index.html)). Tu y trouves les pages officielles de l'examen fédéral, les actualités de santé publique suisse des 7 derniers jours, et un extrait par société savante. La mise à jour est quotidienne, gratuite, hébergée sur GitHub.

## Lancer le jeu

- **Sans serveur** : ouvre `index.html` dans le navigateur (double-clic). Le jeu utilise des scripts classiques, donc il fonctionne en `file://`.
- **Avec un serveur local** (optionnel) : `python3 -m http.server 8000`, puis ouvre <http://localhost:8000>.

## Comment jouer

1. **Parcours** : une salle par spécialité (lots A à G du plan). Chaque salle suit le cycle Fondamentaux → Consultation → Urgence → cas final. Une salle s’ouvre quand la précédente atteint 2 étoiles de moyenne ; le mode **Entraînement** ouvre tout et coupe le chrono.
2. **Duel** : choisis une carte (clic ou touches **1 à 9**), puis déclare ta confiance : **Sûr (S)**, **Hésitant (H)** ou **Au hasard (A)**. Rien n’est présélectionné ; le coup part seulement après la confiance. Échap annule.
3. **Règles** : erreur dangereuse −30 PV, erreur mineure −10 PV, examen inutile −5 PV et +1 min. Urgence et cas final se jouent sous chrono. Étoiles : 3 au départ, −1 sous 80 % de PV, −1 sous 50 %, −1 pour un examen inutile, −1 si le chrono est dépassé ; minimum 1 en cas de victoire.
4. **Fiche** : toute erreur ouvre la fiche en 8 rubriques (fondamentaux, démarche, différentiels, exploration, diagnostic, prise en charge, suivi, explication des coups).
5. **Ronde** : chaque jour, 20 minutes sur les points faibles, angles morts en premier (Leitner, 5 boîtes).
6. **Tableau de bord** : grade, carte de chaleur spécialité × échelon, calibration et excès de confiance, angles morts, vitesse (objectif Urgence < 20 s), boîtes Leitner, préparation par domaine PROFILES, export/import JSON.
7. **Examen blanc** : structure prête (cas mêlés, chronométrés, notés) ; le seuil de réussite reste « À vérifier ».

Une pathologie est **maîtrisée** quand ses 7 échelons sont réussis avec « sûr » à J0, J+1 et J+7 ; elle revient à J+30. Grades : Externe, Interne (25 %), Chef de clinique (50 %), Médecin cadre (75 %), prêt pour l’examen blanc (90 %).

**Sauvegarde.** La progression reste dans le navigateur (`localStorage`, clé `revmed.progression.v2`). Exporte-la régulièrement ; l’import vérifie le schéma et la version, puis fusionne sans rien perdre ni dupliquer.

## Structure

```
index.html                       page unique, ordre de chargement des scripts
css/                             tokens, mise en page, cartes, fiche, composants v2 (mouvement réduit)
data/sources.js                  registre des sources (URL, date de lecture, type, catégorie)
data/parcours.js                 lots A–G et 41 spécialités
data/profiles-ssp.js             248 SSP PROFILES officielles (smifk-cims.ch, lues le 17.11.2026)
data/specialites/<id>.js         une spécialité : catalogue, cartes, cas, questions (JSON strict)
js/engine/schema.js              schéma 8 rubriques + validateur
js/engine/registry.js            index des données, rareté (poids PROFILES provisoire)
js/engine/duel.js                duel, règles, chrono, étoiles (sans DOM)
js/engine/progression.js         traqueur : coups, Leitner, maîtrise, grades, export/import
js/engine/quiz.js                questions à 7 échelons, Fondamentaux, Ronde
js/engine/son.js                 sons Web Audio synthétisés
js/ui/*.js                       parcours, plateau, confiance, fiche, Ronde, tableau, collection, règles
tools/nouvelle-specialite.js     gabarit d’une spécialité vide et valide
tools/couverture.js              rapport de couverture → docs/couverture/
tools/planche.py                 planche par spécialité → planches/<id>.html
tests/                           valider.js, test_moteur.js, qa.py, audit.js, check_links.sh, check_overlap.py
docs/FORMAT_AUTEUR.md            format d’auteur, règle de couverture, format du rapport
docs/CONTINUITE.md               état, suite (ordre du lot A), pièges
```

## Ajouter du contenu

Suis `docs/FORMAT_AUTEUR.md` : `node tools/nouvelle-specialite.js <id>`, remplis le fichier depuis des sources suisses, ajoute sa ligne `<script>` dans `index.html`, puis lance `node tests/valider.js` et `node tools/couverture.js`.

## Politique des sources

- **Clinique** (diagnostic, gestes, traitements, protocoles) : seules les sources suisses font foi : sociétés savantes suisses, facultés et hôpitaux (HUG, CHUV, Inselspital, USZ, USB…), Revue Médicale Suisse, Swiss Medical Forum, hôpitaux cantonaux. Une ligne directrice européenne compte seulement si une source suisse s’y réfère ; la fiche cite alors la page suisse.
- **Sciences fondamentales et pharmacologie** : références internationales en libre accès (ici OpenStax, StatPearls).
- **Doses** : aucune dose ne s’affiche sans extrait mot pour mot de l’information professionnelle suisse (swissmedicinfo.ch), daté et relu par un médecin. Le prototype n’en affiche aucune.
- Chaque fiche liste ses sources avec URL et date de lecture (17.11.2026). Toute affirmation sans source lue porte « À vérifier ».

## Contrôles

```
node tests/valider.js        # validateur du schéma et des sources : 0 erreur exigée
node tests/test_moteur.js    # moteur : progression, Leitner, maîtrise, import/export, duel, validateur
python3 tests/qa.py          # Playwright + Chrome : parcours, duel, fiche, Ronde, tableau, captures
node tests/audit.js > docs/AUDIT-donnees.md
node tools/couverture.js     # rapport de couverture → docs/couverture/
python3 tools/planche.py cardiologie   # planche → planches/cardiologie.html
./tests/check_links.sh       # chaque URL de source doit répondre 200
```

## Licence

Licence du code et des textes : à choisir par l’auteur.

**Textes originaux.** Toutes les phrases des fiches sont rédigées en propres termes, en français. Aucun passage n’est copié des sources : les passages inspirés d’OpenStax *Pharmacology for Nurses* (CC BY-NC-SA 4.0) et de StatPearls ont été réécrits, puis contrôlés par recherche de suites de mots communes (`tests/check_overlap.py`). Seules subsistent des expressions techniques courtes (ex. « point J dans 2 dérivations contiguës »). Chaque source reste citée dans la fiche, avec URL et date de lecture.

Sources suisses citées : HUG (hôpital universitaire), Kantonsspital St.Gallen (**hôpital cantonal**, manuel sous CC BY 4.0, source complémentaire), algorithmes préhospitaliers des services de sauvetage de Bâle, Bâle-Campagne, Winterthour et Einsiedeln (publiés par le canton de Bâle-Ville), Revue Médicale Suisse, Université de Genève.
