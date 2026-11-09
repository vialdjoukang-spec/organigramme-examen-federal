# Liste déduite — LOT_132 F1.3 — Agent B — 2026-11-09T17:10 Europe/Zurich

La branche `agentA/lot-132-p1` était absente du dépôt distant au moment de cette déduction (`git fetch` : ref introuvable). Aucun fichier n'a été écrit sur cette branche. La Phase A n'était pas lisible. L'ordre ci-dessous reprend les entités du programme `data/tip/F1.3.json` (champ `d` et algorithme du cours) et les classe par la prévalence réellement lue, Suisse d'abord.

Critère annoncé : fréquence décroissante du diagnostic qui produit l'anomalie auscultatoire. Un pourcentage n'est écrit que s'il a été lu. Les rangs sans chiffre restent des rangs argumentés, pas des prévalences inventées.

| DX | Nom exact utilisé dans les h2 | Argument lu le 9.11.2026 | Gravité |
|---|---|---|---|
| DX.1 | Asthme | HUG, stratégie Asthme, PDF lu : prévalence environ 5–7 % en Suisse. Plus élevé que le 2 % d'adultes porteurs d'une valvulopathie (CHUV). | Le thorax silencieux est le drapeau rouge. Fichier Agent A. |
| DX.2 | Rétrécissement aortique calcifié | CHUV, page Valves aortiques, lue : « La sténose aortique est la maladie valvulaire la plus fréquente. » Valvulopathie chez près de 2 % des adultes et 10 à 15 % après 75 ans (tous types confondus, pas la sténose seule). | Symptomatique : intervention. |
| DX.3 | Insuffisance mitrale dégénérative | RMS, Approche des valvulopathies : SA et IM sont les deux plus fréquentes en Suisse. RMS 2013;395 : l'IM est la deuxième valvulopathie en Europe. Méta-analyse 2025 : IM modérée à sévère 0,60 % en Europe. | Fichier Agent A. |
| DX.4 | Souffle systolique fonctionnel | RMS, Approche des valvulopathies : le premier geste est de séparer le souffle fonctionnel de l'organique ; le fonctionnel ne requiert pas d'échocardiographie. Fréquence suisse chiffrée non trouvée dans les pages lues. | Fichier Agent B. |
| DX.5 | Prolapsus valvulaire mitral | Carte du programme F1.3. Prévalence chiffrée suisse non lue ce jour : rang placé après les entités quantifiées, sans pourcentage. | Fichier Agent A. |
| DX.6 | Insuffisance aortique | CHUV : fuite par dégénérescence, Marfan, ou forme aiguë (endocardite ou dissection). Moins présentée comme la valvulopathie la plus fréquente. | Forme aiguë 🚩 à exclure en tête d'algorithme. |
| DX.7 | Cardiomyopathie hypertrophique obstructive | Carte du programme (Valsalva). Prévalence chiffrée non lue ce jour. | Fichier Agent A. |
| DX.8 | Péricardite aiguë | RMS 2025;908 (résumé lu, texte intégral non accessible) et RMS 2016;529 (texte lu). Moins fréquente que l'asthme et les valvulopathies dégénératives dans les sources lues. | Tamponnade 🚩. |
| DX.9 | Pneumothorax | Carte du programme (silence unilatéral, tympanisme). Incidence suisse non lue ce jour. | Sous tension 🚩. Fichier Agent A. |
| DX.10 | Endocardite infectieuse | ESC 2023, EHJ : incidence estimée 13,8 pour 100 000 par an dans le monde en 2019. Rare. Reste dans la liste parce que le programme F1.3 en fait le souffle fébrile à ne pas manquer. | 🚩 E1. |

Agent B n'écrit que DX.2, DX.4, DX.6, DX.8 et DX.10. Si `LISTE_DX_CANONIQUE.md` apparaît sur `agentA/lot-132-p1`, les titres seront realignés mot pour mot sans toucher à cette branche.
