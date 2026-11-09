# ETAT_REPRISE — LOT_130 — pause du 9 novembre 2026

Branche `agentB/lot-130`. Aucune pull request. Reprise seulement sur ordre explicite.

## Fait

- Lot F1.1 complet : Phase A + 10 DX, liste gelée, preuves dans `preuves/`, contenu marqué non validé cliniquement.
- Passe de forme engagée, sans Gemma :
  - fenêtres `<details style='display:inline;'>` (mécanisme, exemple chiffré, piège, source `[Sn]`) ;
  - fenêtre « Urgence — conduite chronologique » au point 11 ;
  - fenêtre « cibles tensionnelles » (fiche suisse vs texte européen) ;
  - point 13 sans fenêtre ;
  - `text-align: justify` et `hyphens: auto` avec `lang="fr"` ;
  - chaque rubrique dans un `<article class="ilot">`, ids `ssp-p1`…`p14` et `dxN-p1`…`p14` intacts.
- Dernier assemblage : chiffres hors extrait = 0 ; `controle_lot_80_150.py` = CONFORME, 0 critique ; `controle_fenetres.py` = OK (381 fenêtres dans les îlots). Tailles entre 112 557 et 118 754 octets. SHA-256 dans `MANIFESTE.json`.
- Répétitions : les phrases qui répètent un 4-gramme déjà vu sont déplacées dans une fenêtre, pas supprimées.

## Clos à la reprise du 9 novembre 2026

- Métriques du dernier assemblage mesurées avec `Leona__Harnais_Agents/coeur/metriques_francais.py`.
- Seuls DX.6 (10,2) et DX.10 (11,1) dépassaient 10 répétitions de 4-grammes pour 1000 mots. Phrases reformulées, faits conservés. Après correction : les 11 fichiers sont dans la bande (répétitions ≤ 10, connecteurs entre 1,5 et 4).
- Les îlots sont des `<section class="ilot">`. Les citations portent aussi `[Sn]`.
- `audits/*.html` restent l’audit médical d’avant la passe de forme.
- Défauts encore ouverts : le contrôleur du harnais signale, au point 11, des blocs dont la seule source citée n’est pas de rang suisse 1 à 5 (ESC ou campagne sepsis) ; l’heuristique des termes sans fenêtre (par exemple endoscopie, nycturie) ; le détecteur spaCy `sm` et la longueur moyenne des phrases, hors cible de cette reprise.
- Pas de pull request.
