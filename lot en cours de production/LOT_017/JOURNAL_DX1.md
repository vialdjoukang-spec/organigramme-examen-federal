# JOURNAL_DX1 — LOT_017 — DX.1 Ptosis aponévrotique (involutif) de l'adulte

Rédacteur Phase B, 30.10.2026 (Europe/Zurich). Fichier : `LOT_017_Phase_B_V0_DX.1.html`. Aucun score attribué.

## Hypothèses et choix consignés
1. Définition de société savante : DOG-SORC, prise de position du 23.09.2015 (dernière de la DOG sur ce thème dans la liste consultée). Aucune définition suisse trouvée (HELP_DX1 HDX1-01).
2. Critère d'indication fonctionnelle : celui de la DOG (champ < 20° vers le haut ou < 70° en temporal, Goldmann III/4) ; texte écrit pour la blépharoplastie, appliqué au ptosis par extension et signalé comme tel dans le HTML.
3. Jurisprudence LAMal : TFA K 92/05 (refus) lu sur servat.unibe.ch ; KG LU 5V 15 40 du 19.04.2016 (accord) lu sur une reproduction Omnilex (HDX1-08) ; K 1/05 seulement cité par l'arrêt lucernois.
4. Médicaments retenus : Neosynephrin-POS® 5 % (65568, test, hors information professionnelle), Iopidine® 0,5 % (52813, test du Horner, hors information professionnelle), Rapidocain® avec Epinéphrine (20272 ; sans épinéphrine 32381), Vitamin A «Blache» (22398, choix déduit de l'indication AIPS « érosions de la cornée »), VISTABEL® (55955, cause iatrogène). Numéros vérifiés par script dans la liste Swissmedic au 30.09.2026 (evidence/DX1_S44_…).
5. Oxymétazoline 0,1 % en collyre : aucune forme ophtalmique dans la liste Swissmedic ni dans le corpus AIPS ; écrite « non autorisée en Suisse », sans dose.
6. Revue de Bacharach 2021 (Eye) : auteurs américains, rédaction financée par RVL Pharmaceuticals ; utilisée pour des données primaires et l'anatomie, jamais comme recommandation ; divergence avec S18 sur la part bilatérale (57 % contre 39 %) écrite.
7. Calculs dérivés recalculés par script : 34/400 = 8,5 % ; 34/46 = 73,9 % ; 100 − 64 = 36 % ; 4,0 × 0,42 + 11,3 × 0,35 = 5,635.
8. Divergence sur l'étendue du bilan (Finsterer 2003 contre Bacharach 2021) présentée au point 9.a et au point 14.

## Fichiers écrits
- `LOT_017_Phase_B_V0_DX.1.html` (≈ 125,7 Ko).
- `evidence/DX1_*.txt` (17 extraits datés, dont DX1_S44 et DX1_S47 pour les sources S44 et S47 de la Phase A).
- `.cache/aips/` : 65568, 52813, 55955, 20272, 32381, 22398 (créés ; aucun fichier existant écrasé).
- `HELP_DX1.md`, `JOURNAL_DX1.md`.

## Contrôles
- `controle_lot.py verifier … --sans-nom --json` : 0 critique sur DX.1, titre conforme à la liste canonique.
- `audit_langue.py --json` : 0 critique ; avertissements restants surtout dans les tableaux et la section Sources (initiales d'auteurs, points-virgules) ; aucune espace insécable (leçon 11 de LOT_015).
