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

## Reste

- Métriques de français **de ce dernier assemblage** : mesure interrompue par la pause. Ne pas les inventer.
- Mesure précédente (déduplication un peu moins stricte, mêmes textes de fond) : connecteurs dans la bande 1,5–4 pour les 10 DX, débuts identiques consécutifs à 0, 4-grammes encore au-dessus de 10/1000 pour plusieurs DX (notamment 2, 5, 6, 9 et 10), mots par phrase sous 14, détecteur de verbes spaCy `sm` encore bruité.
- Rapport final demandé (fenêtres par rubrique, avant/après, défauts) non clos.
- `audits/*.html` décrivent l’audit médical d’avant cette passe de forme. Ils n’ont pas été régénérés.
- Pas de pull request. Pas de fusion. Pas d’écriture dans `harnais/` ni `LOT_Claude_Finaux/`.
