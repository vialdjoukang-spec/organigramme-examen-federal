# Fermeture de l’infobulle · Codex, 18.10.2026 UTC

Le bouton Fermer cachait la fenêtre, puis le navigateur envoyait mouseover à la ligne qu’elle recouvrait. Une autre fenêtre apparaissait après 220 ms. La trace locale montre la fermeture de n|G1|c0 suivie de l’ouverture non épinglée de n|G1|c1.

Le patch 0029 annule la temporisation en attente et supprime le survol du nouvel élément sous le clic jusqu’à la sortie du pointeur, au moyen du mécanisme tipSup existant. Il ne change aucun texte médical.

Validation : quatre fermetures restaient ouvertes après 600 ms avant le correctif ; les quatre restent closes après. Suite Playwright 1.63 complète : 276/276. mono/prev/ck --check réussis. Aucune assertion ni référence visuelle modifiée.
