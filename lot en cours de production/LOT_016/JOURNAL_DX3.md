# JOURNAL_DX3 — LOT_016, Phase B, DX.3 (rédacteur, 30.10.2026)

Fichier : `LOT_016_Phase_B_V0_DX.3.html`, 134 974 octets, SHA-256 `6109426dc749fb8d2c2bf4a18274ea46a7e82a353b9b926876f019a20def0af5`. `controle_lot.py verifier --sans-nom` : 0 critique, 0 avertissement pour ce fichier ; 55 fenêtres `popover` ; 0 « À vérifier (AIPS) ».

## Hypothèses et décisions (une ligne chacune)

- Titre `<h2>` repris mot pour mot de `LISTE_DX_CANONIQUE.md` ; le fichier traite la cause (anorexie du vieillissement, bouche, déglutition, isolement), pas la dénutrition en général (correction 1, T7).
- Numérotation [S1]–[S44] propre au fichier ; les sources S01–S33 de `evidence/` sont réutilisées sous un autre numéro (correspondance dans la section Sources du HTML).
- Taille : premier jet à 142,5 Ko ; forme comprimée (doublons entre points supprimés, colonnes « Source » fusionnées, légendes raccourcies) jusqu'à 134 974 octets, sans retirer de dose ni de citation AIPS.
- Méta-termes retirés de l'en-tête visible et du `<title>` (correction 17) ; seul le marqueur FIN_FICHIER garde « LOT_016_Phase_B ».
- Thiamine de renutrition (200–300 mg, Friedli 2018 via Reber 2019) écrite hors information professionnelle ; plafond parentéral AIPS 200 mg/j ; numéros par forme 25636/10989 (corrections 5, 6, 8, 13 ; T3).
- Mégestrol écrit « non autorisé en Suisse » après relecture de la liste Swissmedic au 30.09.2026 (0 occurrence hors nomégestrol) et du XML AIPS (0) (correction 7, T5).
- SNO : deux régimes datés écrits (annexe 1 OPAS jusqu'au 31.12.2026 ; LiMA chap. 36 dès le 1.1.2027) après relecture de S39 et S40 (correction 9, T6).
- Crise surrénalienne citée sans dose (renvoi DX.10), dans l'ordre « prélever cortisol et ACTH si cela ne retarde rien, puis hydrocortisone » (correction 2).
- Salagen : indications AIPS limitées (radiothérapie ORL, Sjögren) ; xérostomie médicamenteuse dite hors information professionnelle. Mirtazapine et Farlutal® : indication AIPS citée, usage orexigène dit hors information professionnelle, sans dose.
- Noms de spécialité : « Mycostatine® » (titre AIPS) et « Dentohexine 0.2% » (titre AIPS, sans ®) ; la LS les liste sous « Mycostatin » et ne contient pas Dentohexine.
- COFA 2018 : divergence interne sur la sonde dans la démence (management summary A vs recommandations B) ; la version B (recommandations) est retenue.
- Seuils du Mini-Cog et de la GDS non donnés : aucune source lue ne les chiffre (voir HELP_DX3.md).
- EWGSOP2 lu par l'API NCBI E-utilities (Europe PMC : HTTP 500, erreur serveur, pas un filtre). Page UNIGE (leçon d'honneur F. Müller) bloquée par un système de sécurité : non contournée, non citée.
- Collision constatée dans le scratchpad partagé (un fichier `ewgsop2.*` réécrit par un autre agent) : toutes les sources ont été retéléchargées dans un sous-dossier privé (`scratchpad/dx3_dl/`) et les extraits `evidence/DX3_*` régénérés depuis ces copies.

## Fichiers écrits

- `LOT_016_Phase_B_V0_DX.3.html`
- `evidence/DX3_*.txt` (19 fichiers : COFA 2018, RMS 2020 HUG, RMS 2015 CHUV, Landi 2016, Cox 2019, ESSD-EUGMS 2016, EWGSOP2 2019, MNA-SF, NICE NG12 1.2.1/1.8.2, compléments ESPEN 2022, Reber/Friedli, Bosch tableau 3, Fedlex OPAS 10–11/17–19, Fedlex LPC 14/CC 377-378-443/LAVS 43bis, S36 Swissmedic, S37 LS, S39 LiMA, S40 SSNC, Berne santé bucco-dentaire)
- `.cache/aips/` : 55901 (Salagen), 43494 (Daktarin® Gel oral), 33043 (Mycostatine®), 50174 (Dentohexine 0.2%)
- `JOURNAL_DX3.md`, `HELP_DX3.md`
