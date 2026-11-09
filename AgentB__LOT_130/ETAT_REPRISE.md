# ETAT_REPRISE — LOT_130 — point 9, rév. 9.11.2026

Branche `agentB/lot-130`. Aucune pull request.

## Point 9 (rév. 9.11.2026)

- Sous-titre `9.a Gold standard` et `9.b Première intention` dans chaque monographie.
- Biologie : tableau Cas → Interprétation → Hypothèse (normal, positif, limite, discordant). Unités seulement si l'extrait les donne (mmHg, mmol/L). Aucun seuil inventé.
- Aucune image embarquée : aucune figure libre fiable pour le gold standard ou la première intention. Phrase explicite (Wikimedia Commons, Open-i, bibliothèque ouverte européenne, neuf novembre deux mille vingt-six). Pas de schéma généré.
- Point 11 : source suisse citée, sinon marque `exception-non-suisse`.
- Îlots `section.ilot` avec id `dxN-iK`. Harnais : 10 DX conformes, 0 critique. Avertissements : absence d'image (justifiée) ; « induite » (faux positif du suffixe) ; spaCy « sans verbe ».
- Phase A : le contrôleur cherche des ids `dx1-p*` parce que le nom de fichier n'est pas `Phase_B_V0_DX.n`. Les ids réels sont `ssp-p1`…`p14`.

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
