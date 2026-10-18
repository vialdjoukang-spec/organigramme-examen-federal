# Hygie · journal des monographies (Europe/Zurich)

## Lot 4 · G5 + G6 · 17.10.2026
- 32 monographies (G5 : 17 ; G6 : 15) ; hypoglycémie, endocardite, syndrome sérotoninergique déjà faits (lot 1).
- Sources : cours SSP G5/G6 et sources vérifiées du G6 (OFSP Swiss Sepsis Report 2025, Sepsis-3, SSC 2021, NICE 2024, ESC 2019, EAU 2026…), lues le 17.10.2026.
- Épidémiologie chiffrée sourcée : 6 (sepsis et choc septique, paludisme, SMN, iatrogénie, maladies inflammatoires, néoplasies) ; les 26 autres « à vérifier (source CH/UE) » ; sex-ratio partout à vérifier.
- Doses : doses_ch.json (origin/main) ne contient que le valaciclovir → toutes « à vérifier (AIPS) ».
- Base origin/main : conflit d'ajout possible sur data/ck/mono/n.json et assets/ck/mono-n.js avec le lot 3 (#53), et en fin de fichiers JSON communs avec #50/#53 ; résoudre en gardant les deux blocs.
- Prochain : lot 5 = G7 + G8.

## Lot 5 · G7 + G8 · 17.10.2026 (branche feat/mono-g7, base origin/main)
- 25 monographies (G7 flush : 13 ; G8 hypothermie : 12) ; aucun identifiant déjà fait (main, #50, #53, #54, Panacée #55/#60/#62, #49).
- Sources : uniquement les sources vérifiées de chaque DD (TIP.v), relues le 17.10.2026 : ENETS 2022, ESH 2020, Valent 2021, ETA 2012 (CMT), ETA 2018 (Basedow), NICE NG23 (2026), consensus dumping 2020, Brooks 2009, EADV 2022 (rosacée), ICAR 2021, ERC 2021, Inselspital Berne 2022, CHUV 2023, SLF, Tipton, revues gelures 2023/2025, cas Cureus 2024.
- Épidémiologie : 19 avec chiffre sourcé, 6 « à vérifier (source CH/UE) » (VIPome, rosacée, flush médicamenteux, émotionnel, neurogène, gelures) ; sex-ratio sourcé pour 5 (Basedow, HT I-III, avalanche).
- Doses : 5 dose_ref AIPS (adrenaline-im-adulte-anaphylaxie, carbimazole-po-adulte-hyperthyroidie, adrenaline-iv-adulte-arret-cardiaque, noradrenaline-iv-adulte-perfusion, naloxone-iv-adulte-surdosage-opioide ; lignes dans #59/#61, non encore sur main) ; 12 « dose : à vérifier (AIPS) ».
- Critères formels complets : mastocytose (1 majeur + 1 mineur ou 3 mineurs), dumping (HGPO), phéochromocytome (seuil × 2), ménopause (NICE 1.3.1), HOPE ≥ 10 %.
- Conflits attendus : shards a/c/h/m/p/r/s/v et journal (add/add avec #54) : garder les deux blocs (merge_shards.py).
- Prochain : lot 6 = G9 + G10.

- 18.10.2026, Europe/Zurich · #64 : accord Vial lu ; main réuni sans conflit réel de clé, sorties reconstruites ; réserve tryptase ajoutée, assertion de décès fondée sur HOPE retirée au profit d’une vérification explicite. Audit primaire bloqué par la politique réseau, aucun label audit-ok nouveau.
