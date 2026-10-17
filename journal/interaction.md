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
