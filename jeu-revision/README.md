# Internat · Urgences cardio — révision médicale par duels de cartes

Prototype jouable dans un navigateur, sans installation. Tu joues l’interne. Chaque cas clinique se gagne en **duels de cartes** : tu associes le bon geste ou le bon médicament à la bonne situation. Chaque erreur ouvre automatiquement la **fiche** correspondante et met à jour le **journal**.

Public visé : préparation de l’examen fédéral suisse de médecine humaine (format PROFILES) et pratique clinique en Suisse.

> Prototype pédagogique. Le contenu sert à réviser ; ce n’est pas un protocole et il ne remplace ni un protocole local ni l’avis d’un médecin. Aucune dose n’est affichée. Tout contenu sans source suisse lue porte la mention « À vérifier ».
>
> **Relecture médicale** : la validation médicale du contenu relève de Dr Vial Djoukang, médecin, auteur et responsable du projet. Le prototype a été rédigé avec un assistant et attend cette relecture avant tout usage.

## Lancer le jeu

- **Sans serveur** : ouvre `index.html` dans le navigateur (double-clic). Le jeu utilise des scripts classiques, donc il fonctionne en `file://`.
- **Avec un serveur local** (optionnel) : `python3 -m http.server 8000`, puis ouvre <http://localhost:8000>.

## Comment jouer

1. Clique « Prendre la garde ».
2. Lis le **dossier** à gauche : les valeurs en rouge signalent une alerte vitale.
3. Joue une carte de ta main (clic, Entrée, ou touches **1 à 9**).
4. Le retour s’affiche tout de suite : **vert** = bon réflexe, **rouge** = erreur (perte de PV), **bleu** = information.
5. Une erreur ouvre la fiche. Lis-la, ferme-la (Échap), puis continue.
6. Joue tous les objectifs du duel pour passer au suivant.

Le cas « Douleur thoracique, 74 ans » compte quatre duels :

| Duel | Situation | Objectifs | Pièges |
|---|---|---|---|
| 1 | Exclure la dissection | ECG 12 D, angio-CT | aspirine, héparine, P2Y12 avant exclusion ; O₂ ; nitrés |
| 2 | Nommer la menace | STEMI | péricardite, NSTEMI, EP, dissection |
| 3 | Chercher le ventricule droit | V3R–V4R | nitrés, bêtabloquant, O₂ |
| 4 | Reperfuser | aspirine, HNF, alarme STEMI → ICP | nitrés, O₂, bêtabloquant |

Trois écrans : **Plateau** (duel), **Fiche** (fenêtre au clic sur « Fiche » ou sur toute carte hors de la main), **Journal** (précision par système, erreurs, fiches à revoir, remise à zéro). Un onglet **Collection** montre toutes les cartes et la légende des raretés.

## Structure

```
index.html                    page unique, ordre de chargement des scripts
css/tokens.css                couleurs fonctionnelles, typographie, espacements
css/layout.css                en-tête, plateau, journal, responsive, mouvement réduit
css/cards.css                 cartes et animations (distribution, survol, secousse, halo)
css/fiche.css                 fiche détaillée (dialog)
data/sources.js               registre des sources (URL, éditeur, date de lecture, portée)
data/systems.js               systèmes du journal (cardio actif ; neuro, infectio, pneumo à venir)
data/cards/cardio.js          18 cartes (6 pathologies, 12 actions/médicaments)
data/services/urgences-cardio.js  le cas, ses 4 duels et leurs règles
js/engine/registry.js         index des données + validation de cohérence
js/engine/duel.js             moteur de duel (sans DOM)
js/engine/journal.js          journal persistant (localStorage, clé revmed.journal.v1)
js/ui/*.js                    rendu : carte, plateau, fiche, collection, journal
js/main.js                    démarrage et navigation
tests/qa.py                   QA Playwright (28 contrôles) + captures d’écran
tests/audit.js                auto-audit des données → docs/AUDIT-donnees.md
tests/check_links.sh          vérifie que chaque URL de source répond
docs/screenshots/             captures produites par la QA
docs/AUDIT.md                 auto-audit commenté (sources, « À vérifier », limites)
tests/check_overlap.py        contrôle de reprise textuelle face aux sources téléchargées
tests/dump_text.js            extrait le texte du jeu pour ce contrôle
```

## Ajouter du contenu

**Une carte** : ajoute un objet dans `data/cards/<systeme>.js`. Chaque affirmation s’écrit `c("Phrase complète.", "id-source")`. Sans source, écris `c("Phrase. À vérifier.")` : l’interface affiche le badge. Ajoute la source dans `data/sources.js` avec sa date de lecture.

**Un système** : ajoute `{ id, nom, actif: true }` dans `data/systems.js`, puis un fichier `data/cards/<id>.js` chargé dans `index.html`.

**Un service** : copie `data/services/urgences-cardio.js`, change `id`, `nom`, `systeme`, puis écris le cas : `patient`, `dossier` (examens à révéler), `etapes` (adversaire, main, objectifs, règles). Ajoute la ligne `<script>` dans `index.html` et l’entrée sur la carte des services (`js/ui/board.js`). Au démarrage, `JEU.registry.validate()` signale en console toute carte ou source inconnue.

## Politique des sources

- **Clinique** (diagnostic, gestes, traitements, protocoles) : seules les sources suisses font foi : sociétés savantes suisses, facultés et hôpitaux (HUG, CHUV, Inselspital, USZ, USB…), Revue Médicale Suisse, Swiss Medical Forum, hôpitaux cantonaux. Une ligne directrice européenne compte seulement si une source suisse s’y réfère ; la fiche cite alors la page suisse.
- **Sciences fondamentales et pharmacologie** : références internationales en libre accès (ici OpenStax, StatPearls).
- **Doses** : aucune dose ne s’affiche sans extrait mot pour mot de l’information professionnelle suisse (swissmedicinfo.ch), daté et relu par un médecin. Le prototype n’en affiche aucune.
- Chaque fiche liste ses sources avec URL et date de lecture (17.11.2026). Toute affirmation sans source lue porte « À vérifier ».

## Contrôles

```
python3 tests/qa.py          # Playwright + Chromium : partie complète, fiche, journal, captures
node tests/audit.js > docs/AUDIT-donnees.md
./tests/check_links.sh       # chaque URL de source doit répondre 200
```

## Licence

Licence du code et des textes : à choisir par l’auteur.

**Textes originaux.** Toutes les phrases des fiches sont rédigées en propres termes, en français. Aucun passage n’est copié des sources : les passages inspirés d’OpenStax *Pharmacology for Nurses* (CC BY-NC-SA 4.0) et de StatPearls ont été réécrits, puis contrôlés par recherche de suites de mots communes (`tests/check_overlap.py`). Seules subsistent des expressions techniques courtes (ex. « point J dans 2 dérivations contiguës »). Chaque source reste citée dans la fiche, avec URL et date de lecture.

Sources suisses citées : HUG (hôpital universitaire), Kantonsspital St.Gallen (**hôpital cantonal**, manuel sous CC BY 4.0, source complémentaire), algorithmes préhospitaliers des services de sauvetage de Bâle, Bâle-Campagne, Winterthour et Einsiedeln (publiés par le canton de Bâle-Ville), Revue Médicale Suisse, Université de Genève.
