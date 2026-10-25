# BASE_LOTS_CUMUL_2026-10-25

Passation cumulative Drive × GitHub — 248 SSP (LOT_001–LOT_248).

## Résultat

- **73 / 248** achevés (Appel A + Appel B)
- Audités : **6** → [1, 2, 3, 4, 5, 6]
- Achevé mais non audité · non édité : **67**
- Nouveaux vs Drive-seul 43 : **30** → [41, 42, 73, 74, 75, 76, 77, 78, 104, 110, 111, 112, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 181, 182, 183, 208, 209, 210]

## Définition

- Appel A = 11 chapitres (10 DD + cours SSP)
- Appel B = 11 chapitres (DX.1–10)
- Fait = A et B à 11/11 (max Drive, GitHub)
- Label non audité : `achevé mais non audité · non édité`
- Jaune vif `#FFE600` si achevé

## Contenu

`data/lots_cumul.{json,csv}` · `data/summary.json` · `table/etat_cumul.{md,html,pdf}` · `spies/build_cumul.py` · `mirrors/titles_248.json`

## Continuer

1. Lire `data/summary.json`.
2. Lot en cours → `drive.csv_fichiers` + `github.branches`.
3. Ne pas fusionner les PR Flash sans audit.
4. Relancer `python3 spies/build_cumul.py`.
5. Drive LOTS_Finaux : `1DaFAd0uamsJQY2NH0ocuy2bhpfcVk9Vu`.

## Méthode

Drive: STATUT_LOTS_001_248.csv (fichiers A/P1–P4, V5/V7, AUDITÉ) + titres dossiers LOTS_Finaux. GitHub: flash-full-inventory.json (Appel_A + DX.1–10 sur branches flash A/B) + branches lot/LOT_* et audit/LOT_*. Max(Drive,GitHub) par lot. Pas de téléchargement binaire.

Généré : 2026-10-25T11:26:56+01:00 Europe/Zurich.
