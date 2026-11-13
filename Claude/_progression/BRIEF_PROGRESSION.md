# Brief PROGRESSION — rédacteur de fiches (examens, pharmacologie, psychiatrie, sciences fondamentales)

Spécification : `Claude/_progression/CAHIER_ARCHITECTURE_v2.md` (lire par extraits : `grep -n` puis `sed -n`).
Données : `Claude/_progression/donnees/<module>/<ID>.json`, une fiche par fichier ; page : `outils/receptacle.py`.

**Avant tout (≈ 4 Ko lus)**
1. `python3 Claude/_harnais/memoire_agent.py lire PROG <ID>` — ton carnet ; reprise sans relecture.
2. `python3 Claude/_harnais/sources_cache.py index <mot>` — une source déjà lue n'est jamais refetchée.
3. `sed -n '1,80p' Claude/_progression/donnees/<module>/<ID>.json` — la fiche vide : chaque case porte « — ».

**Règles 0 du cahier (non négociables)**
0.1 Charpente avant contenu : tu remplis une fiche existante ; tu ne crées ni ne renommes aucun identifiant
(`charpente.py` seul crée ; l'identifiant ne change jamais, le titre peut changer).
0.2 Un seul gabarit par type (`donnees/gabarits.json`) : aucun champ ajouté ni retiré ; « — » si rien de sûr.
0.3 S1 Neurologie et S11 Psychiatrie séparés : une molécule commune a deux fiches, chacune son « pourquoi elle » ;
lien entre elles par passerelle « Interface S1 ↔ S11 », jamais par fusion.
0.4 Psychiatrie : CIM-10 chapitre V seule (descriptions cliniques OMS) ; chiffre absent → critères pour la recherche,
signalé dans `complement_recherche`. Survol des critères : tous, une phrase courte chacun, jamais mot pour mot,
termes discriminants en gras. N'invente aucun code CIM-10.
0.5 Sources suisses d'abord : AIPS Swissmedic, puis sociétés et hôpitaux universitaires suisses, puis européennes
(signalées). « Selon X » seulement si la page de X a été lue ; sinon « (non vérifié CH) ».
0.6 Forme : Atkinson Hyperlegible, ≈ 15 px, colonne ≤ 760 px, une seule fenêtre ouverte, contraste ≥ 7:1,
**fond blanc, couleur vive partout ailleurs (aplats foncés vifs + texte blanc, contraste ≥ 7:1 ; un système = une couleur)** (`python3 Claude/_outils/restaurer_fond.py --verifier <html>`). Couleurs à sens fixe :
bleu normal · rouge pathologie · vert traitement du système · violet hors système · ocre non médicamenteux · orange danger.

**AIPS (posologie, grossesse, allaitement, contre-indications)**
`python3 Claude/_harnais/aips_fiche.py trouve <DCI|n°>` (corpus refdata hors ligne : n°, date, URL) puis
`aips_fiche.py fiche <url>`. Grossesse, allaitement, contre-indications et date « mise à jour » recopiés **mot pour mot** ;
hors AIPS écrit « hors AIPS », sans dose. Jamais le Compendium. Porte : `python3 Claude/_outils/verif_aips.py`.
Posologie : chaque terme (dose, intervalle, durée, seuil) porte un chiffre et une unité ; « à adapter » seul est refusé.

**Aucune donnée inventée.** Chiffre sans source lue → « — ». Déduction écrite comme telle. Passerelle ajoutée
seulement vers un identifiant existant, avec son « pourquoi » en une ligne.

**Écrire en peu de tours** : une fiche = un remplacement JSON groupé ; plusieurs fiches indépendantes dans le même tour.
Lecture par extraits seulement (`Read` avec `limit`, `grep -n`) ; une sortie d'outil > 20 000 caractères est une alerte.
Sorties de commande `| head -40`.

**Mémoire** : à chaque étape utile, `memoire_agent.py note PROG <ID> source|aips|decision|reste "<une ligne>"`.

**Portes avant de rendre (toutes vertes)**
`python3 Claude/_progression/controle.py` (identifiants, passerelles, cases « — », posologies chiffrées, S1/S11) ·
`python3 Claude/_progression/charpente.py` (doit écrire 0 fiche : la charpente est intacte) · `verif_aips.py` ·
`python3 outils/receptacle.py --audites "$(cat Claude/_reference/prets.txt)" --sortie /tmp/p.html`.

**Git** : tes fichiers seulement ; jamais --force, reset, stash, checkout d'autrui. Ne touche aucun `Claude/LOT_*`.
Commit terminé par « Prompt L1 lu et appliqué. ». Rapport final ≤ 5 lignes.
