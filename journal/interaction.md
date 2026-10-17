# Journal · Fenêtre, Calendrier et onglets · Hermès

Chaque entrée porte une date (Europe/Zurich), une décision et les sources lues. Aucune donnée personnelle n’entre dans ce journal public.

- Le chantier démarre à sa phase (plan v2, section 3) ; aucune entrée pour l’instant.

## 17.10.2026 · Calendrier interactif et sauvegarde automatique (patch 0004)

Décision. Le Calendrier garde le glisser-déposer existant et le placement en deux touchers, et ajoute :
- un clic ou un toucher sur une plage vide, qui ouvre une fenêtre de création rapide (jour, début, durée, activité, chapitre cherché) ;
- une sélection de plage à la souris, qui préremplit début et durée ;
- une barre de recherche floue (sans accents, par code, tolérante à une ou deux fautes) avec « Placer » et « Ouvrir » ; Entrée au clavier ouvre directement la fenêtre de création ;
- le déplacement et le redimensionnement des séances à la souris, au toucher (maintien de 300 ms, sinon la page défile) et au clavier (flèches, Maj + flèches, Entrée) ; tout s’aimante au quart d’heure ;
- l’attribut data-wd (1 à 7) sur les en-têtes et colonnes, pour les couleurs de jour d’Apollon.

Sauvegarde, en cinq points :
1. Chaque écriture locale (lsSet) programme, 600 ms plus tard, une copie « cur » de toutes les clés orga-* dans IndexedDB (base orga-sauvegarde), avec une somme FNV-1a.
2. Une version est ajoutée au plus une fois par heure si l’état a changé (« première version du jour », puis « horaire ») ; on garde les 20 plus récentes et une par jour jusqu’à 30 ; « Restaurer une version » liste date, type et résumé, et « Créer une version maintenant » en ajoute une.
3. La restauration vérifie la somme et le format (bakCheck), met d’abord l’état actuel de côté, puis recharge la page.
4. Au démarrage, si orga-ef manque ou si une clé est endommagée, les clés manquantes sont reprises de la copie « cur » validée, une seule fois par session.
5. navigator.storage.persist() est demandé et son résultat affiché ; sur Chromium de bureau, un fichier choisi par l’utilisateur reçoit le JSON au format d’export après chaque modification ; « Enregistré à hh:mm » s’affiche dans le statut.

Sources lues le 17.10.2026 : MDN StorageManager.persist(), IndexedDB API, File System Access API ; WebKit, plafond de sept jours du stockage écrit par script.

## 17.10.2026, 13:40 · Fusion de PR #15, contrôle du site public et patch 0009

Constat. PR #15 a été fusionnée à 13:26 par un commit de fusion (3c9b878) ; CI et Pages ont réussi sur main. Le site public sert un fichier identique à app_v2.html de main (même SHA-256), et tests/test_calendrier.py y réussit 32/32 sans erreur de console. Le Calendrier y porte data-wd 1 à 7 sur ses colonnes ; les teintes elles-mêmes attendent PR #16 (Apollon).

Défaut trouvé sur le site public. L’exemple affiché dans la barre, « insuffisance cardiaque », ne renvoyait aucun résultat, car la recherche ne lisait que le nom et le code des SSP.

Décision (patch 0009). Quand le nom et le code d’un SSP ne correspondent pas, la recherche lit les titres de ses diagnostics différentiels et de ses notions (NOT), normalisés une seule fois. Tous les mots doivent y figurer ; l’expression exacte et un diagnostic l’emportent sur une notion. Le titre trouvé s’affiche sous le nom (« Diagnostic : … ») ; sur mobile, il passe à la ligne. Le contenu complet des fiches (TIP, 4,9 millions de caractères) n’est pas fouillé : trop lourd et trop large. Test ajouté : recherche_notion, sur ordinateur et sur mobile.

Sources lues : aucune source externe ; données internes NOT et SSP.

## 17.10.2026, 14:20 · Bandes de séance coupées sur ordinateur (patch 0010)

Constat (capture de la titulaire). En vue Semaine sur ordinateur, une séance de 60 min (46 px) affichait l’en-tête puis trois lignes autorisées par -webkit-line-clamp:3 : la troisième ligne était coupée à mi-hauteur, sans « … ». Sur mobile (vue Jour, colonne large), le texte tenait.

Décision. La hauteur des bandes reste proportionnelle à la durée (elle porte l’information de temps, et une bande plus haute chevaucherait la suivante). blkFit() compte les lignes qui tiennent réellement et les impose par --cl : le texte finit alors par « … ». Sous une ligne (15 et 30 min), la bande passe sur une seule ligne compacte. La durée se masque quand elle cacherait l’horaire ou le code. Le texte complet (activité, chapitre, jour, horaire, durée) s’affiche en tête de la fenêtre de la séance, au survol, au clic, au clavier (i) et à l’appui long ; la clé devient s|code|séance.

Contrôle automatique. Iris (tests/visuel/capture.py, CLIP_JS) parcourt chaque vue, sur ordinateur et mobile et dans les trois thèmes, plus les états cal-bandes-semaine et cal-bandes-jour (séances de 15 à 120 min aux chapitres les plus longs) ; compare.py échoue sur tout élément à overflow hidden ou clip dont le contenu dépasse de plus de 1 px sans ellipse explicite et sans texte complet (title, data-t, aria-describedby). Sur main avant correctif : 30 éléments coupés détectés ; après : 0 sur 72 vues. Test ajouté : bandes_sans_coupure (ordinateur et mobile).

Sources lues : aucune source externe.

## 17.10.2026 · NC-0 · pile de fenêtres et lieur de termes (patch 0012)

Fait. gloLink(root) parcourt les nœuds texte avec un TreeWalker. Une seule expression régulière compare les formes repliées (sans accents ni casse), la plus longue d’abord ; une seconde, sensible à la casse, traite les abréviations. Le lieur ne lie que la première occurrence par bloc et exclut les termes déjà ouverts. Un MutationObserver sur .w lie les pages par petits lots en temps libre. Avec 3 200 termes, l’index se construit en 8 ms et aucune tâche longue ne s’ajoute à celles du démarrage. Les fenêtres s’empilent : un terme cliqué dans une fenêtre ouvre le niveau suivant (5 au plus), le fil d’Ariane et « ← Retour » y reviennent, et Échap ferme toute la pile. Au survol dans une fenêtre, la définition courte s’affiche en title. Sur mobile, la pile reste dans le panneau bas. showTip/hideTip gardent leur contrat (le 5e argument « keep » est facultatif).

Schémas. Les cases à cocher règlent les couches, les boutons choisissent la vue, et le tour en 8 vues se manie au glisser ou aux flèches. Le SVG est intégré en ligne depuis CK_SVG (assets/nc/ncXX.js, tools/nc_svg_js.py) et nettoyé par DOMParser (aucun script, aucun on*) ; il fonctionne donc en file://. Sans fichier JS, une <img> s’affiche et les couches sont désactivées.

Sources lues : aucune source clinique ; les données d’essai sont factices et marquées « À vérifier ».
