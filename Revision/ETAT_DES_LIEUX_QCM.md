# ÉTAT DES LIEUX — Questionnaires Type A « Réflexe SSP » · Temps 1 · catégorie G

_Régénéré par `_outils/scripts/etat_lieux.py` le 2026-11-02 à 00:10 (Europe/Zurich, UTC+1) · seuil couverture : ≥ 2 EX par DX_

## Relève Λ — en une ligne

- **Progression globale : 6/16 SSP livrés = 37.50 %** · pondérée (statut × couverture DD) : **30.0 %** · 481 questions au total.
- **Prochain SSP : G7 (LOT_007) — Bouffées vasomotrices (flush)**
- **Blockers / dettes :** aucun gap de couverture sur les SSP livrés. · Validation humaine (statut `valide`) : 0 SSP à ce jour.

## Tableau G1–G16

| SSP | LOT | Titre | Q | EX | AP | SPE | DX couverts | Statut | Progression | HTML |
|---|---|---|---:|---:|---:|---:|---|---|---:|---|
| G1 | LOT_001 | Transpiration anormale | 51 | 34 | 10 | 7 | 15/15 | 🟦 revue_auto | 80 % | [ouvrir](G_symptomes_generaux/G01_transpiration_anormale/LOT_001_G1_TypeA_Reflexe.html) |
| G2 | LOT_002 | Tuméfaction, tumeur, y compris augmentation de volume des ga | 63 | 42 | 11 | 10 | 15/15 | 🟦 revue_auto | 80 % | [ouvrir](G_symptomes_generaux/G02_adenopathie_tumefaction/LOT_002_G2_TypeA_Reflexe.html) |
| G3 | LOT_003 | Soif excessive, consommation excessive de liquides (polydips | 85 | 49 | 23 | 13 | 13/13 | 🟦 revue_auto | 80 % | [ouvrir](G_symptomes_generaux/G03_soif_polydipsie/LOT_003_G3_TypeA_Reflexe.html) |
| G4 | LOT_004 | Fatigue, lassitude | 88 | 52 | 20 | 16 | 11/11 | 🟦 revue_auto | 80 % | [ouvrir](G_symptomes_generaux/G04_fatigue_lassitude/LOT_004_G4_TypeA_Reflexe.html) |
| G5 | LOT_005 | Sensation de maladie | 94 | 56 | 22 | 16 | 15/15 | 🟦 revue_auto | 80 % | [ouvrir](G_symptomes_generaux/G05_sensation_maladie/LOT_005_G5_TypeA_Reflexe.html) |
| G6 | LOT_006 | Fièvre, frissons, hyperthermie | 100 | 60 | 24 | 16 | 15/15 | 🟦 revue_auto | 80 % | [ouvrir](G_symptomes_generaux/G06_fievre_frissons/LOT_006_G6_TypeA_Reflexe.html) |
| G7 | LOT_007 | Bouffées vasomotrices (flush) | 0 | 0 | 0 | 0 | 0/12 | ⬜ à faire | 0 % | — |
| G8 | LOT_008 | Hypothermie | 0 | 0 | 0 | 0 | 0/12 | ⬜ à faire | 0 % | — |
| G9 | LOT_009 | Prurit | 0 | 0 | 0 | 0 | 0/15 | ⬜ à faire | 0 % | — |
| G10 | LOT_010 | Douleurs de tous types | 0 | 0 | 0 | 0 | 0/15 | ⬜ à faire | 0 % | — |
| G11 | LOT_011 | Troubles du sommeil (insomnies, hypersomnies ou somnolence,  | 0 | 0 | 0 | 0 | 0/13 | ⬜ à faire | 0 % | — |
| G12 | LOT_012 | Œdème diffus ou localisé | 0 | 0 | 0 | 0 | 0/13 | ⬜ à faire | 0 % | — |
| G13 | LOT_013 | Décès non naturel | 0 | 0 | 0 | 0 | 0/10 | ⬜ à faire | 0 % | — |
| G14 | LOT_014 | Décès inattendu ou mort subite | 0 | 0 | 0 | 0 | 0/10 | ⬜ à faire | 0 % | — |
| G15 | LOT_015 | Prise de poids, obésité | 0 | 0 | 0 | 0 | 0/10 | ⬜ à faire | 0 % | — |
| G16 | LOT_016 | Perte de poids, perte d’appétit | 0 | 0 | 0 | 0 | 0/10 | ⬜ à faire | 0 % | — |

## Procédure pour le SSP suivant (5 commandes)

```bash
cd /workspace/grok/Revision
python3 _outils/scripts/init_ssp.py G7          # canevas + checklist DD
# rédiger _bank_GNN.py selon _outils/CHARTE_REDACTION.md (sources = LOT audité uniquement)
python3 _outils/scripts/build_ssp.py G_symptomes_generaux/GNN_xxx   # JSON + HTML
python3 _outils/scripts/couverture_dd.py G_symptomes_generaux/GNN_xxx  # 0 gap exigé
python3 _outils/scripts/etat_lieux.py                                 # ce fichier
```

Légende statut : ⬜ absent · 🟨 brouillon (canevas/bank sans JSON) · 🟦 revue_auto (contrôles automatiques OK, pas de relecture humaine) · 🟩 validé (relu).
