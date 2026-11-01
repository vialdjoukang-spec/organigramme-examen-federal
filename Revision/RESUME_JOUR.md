# Résumé du jour — Revision QCM

*Généré dynamiquement le 2026-11-01 22:34 Europe/Zurich par `Revision/_outils/scripts/resume_jour.py`.*

## Progression G1–G16

**2/16 SSP prêts (12.5 %)** · branche locale repo `grok/revision` @ `2598db63`

| SSP | LOT | Titre | Statut | Q | EX | AP | SPE | HTML |
|-----|-----|-------|--------|---|----|----|-----|------|
| G01 | LOT_001 | Transpiration anormale | revue_auto | 51 | 34 | 10 | 7 | `G_symptomes_generaux/G01_transpiration_anormale/LOT_001_G1_TypeA_Reflexe.html` |
| G02 | LOT_002 | Tuméfaction / adénopathie | revue_auto | 63 | 42 | 11 | 10 | `G_symptomes_generaux/G02_adenopathie_tumefaction/LOT_002_G2_TypeA_Reflexe.html` |
| G03 | LOT_003 | Soif excessive / polydipsie | absent | 0 | 0 | 0 | 0 | `—` |
| G04 | LOT_004 | Fatigue, lassitude | absent | 0 | 0 | 0 | 0 | `—` |
| G05 | LOT_005 | Sensation de maladie | absent | 0 | 0 | 0 | 0 | `—` |
| G06 | LOT_006 | Fièvre, frissons, hyperthermie | absent | 0 | 0 | 0 | 0 | `—` |
| G07 | LOT_007 | Bouffées vasomotrices (flush) | absent | 0 | 0 | 0 | 0 | `—` |
| G08 | LOT_008 | Hypothermie | absent | 0 | 0 | 0 | 0 | `—` |
| G09 | LOT_009 | Prurit | absent | 0 | 0 | 0 | 0 | `—` |
| G10 | LOT_010 | Douleurs de tous types | absent | 0 | 0 | 0 | 0 | `—` |
| G11 | LOT_011 | Troubles du sommeil | absent | 0 | 0 | 0 | 0 | `—` |
| G12 | LOT_012 | Œdème diffus ou localisé | absent | 0 | 0 | 0 | 0 | `—` |
| G13 | LOT_013 | Décès non naturel | absent | 0 | 0 | 0 | 0 | `—` |
| G14 | LOT_014 | Décès inattendu / mort subite | absent | 0 | 0 | 0 | 0 | `—` |
| G15 | LOT_015 | Prise de poids, obésité | absent | 0 | 0 | 0 | 0 | `—` |
| G16 | LOT_016 | Perte de poids / appétit | absent | 0 | 0 | 0 | 0 | `—` |

## Livrables détectés (jour / Revision)

- `STRATEGIE_QCM_EXAMEN_CH.md` — Stratégie QCM examen CH
- `EVALUATION_MEDICAL_LANGUE_LOT_001_248.html` — Évaluation médicale/langue 001–248
- `Revision/ETAT_DES_LIEUX_QCM.md` — État des lieux QCM
- `Revision/README.md` — README Revision
- `Revision/_outils/PEDAGOGIE_PREPARATION_SANS_COMPARAISON.md` — Architecture « Préparation sans comparaison »
- `Revision/_outils/CHARTE_REDACTION.md` — Charte de rédaction QCM Type A
- `Revision/_outils/PROFIL_GRAND_MAITRE_BITUNDER.md` — Profil Grand Maître Professeur Bitunder
- `Revision/G_symptomes_generaux/G01_transpiration_anormale/LOT_001_G1_TypeA_Reflexe.html` — G01 Type A Réflexe (+ JSON, COUVERTURE_DD.md, CHANGELOG.md)
- `Revision/G_symptomes_generaux/G02_adenopathie_tumefaction/LOT_002_G2_TypeA_Reflexe.html` — G02 Type A Réflexe (+ JSON, COUVERTURE_DD.md, CHANGELOG.md)
- `STRATEGIE_QCM_EXAMEN_CH.html` — Stratégie QCM (HTML)
- `STRATEGIE_QCM_EXAMEN_CH.pdf` — Stratégie QCM (PDF)
- `EVALUATION_MEDICAL_LANGUE_LOT_001_248.json` — Évaluation (JSON)
- `EVALUATION_MEDICAL_LANGUE_LOT_001_248.pdf` — Évaluation (PDF)
- `QCM-banque/LOT_001/README_POINTEUR.md` — Pointeur QCM-banque → Revision/G01
- `Revision/_index/MAP_G1_G16.json` — Carte G1–G16 (DX par SSP)
- `Revision/_outils/scripts/build_ssp.py` — Build générique SSP
- `Revision/_outils/scripts/etat_lieux.py` — État des lieux + REGISTRE

## Relève Λ

- Progression globale G : **12.5 %** (2/16).
- Prochain SSP absent : **G03** · détail couverture DD et blockers : `ETAT_DES_LIEUX_QCM.md`.
- Contraintes : GitHub only (jamais Drive) ; pas de PR/merge/main/force-push sans ordre Vial.

## Prêt à pousser (CloudAgent)

- Cible : `vialdjoukang-spec/organigramme-examen-federal`, branche **`grok/revision`** — jamais Drive, jamais force-push, jamais `main`, pas de PR.
- À synchroniser dans le dépôt : `Revision/` entier (sans `__pycache__/`, sans `_print.html`) ; `QCM-banque/LOT_001/README_POINTEUR.md` ; `STRATEGIE_QCM_EXAMEN_CH.{md,html,pdf}` ; `EVALUATION_MEDICAL_LANGUE_LOT_001_248.{html,json,pdf}` ; script résumé dynamique `Revision/_outils/scripts/resume_jour.py`.
- Source de vérité : `/workspace/grok/Revision` (la copie `repo/Revision` @ HEAD local est plus ancienne : G1 v2, pas de G2).

## Commandes

```bash
python3 /workspace/grok/Revision/_outils/scripts/resume_jour.py --write
python3 /workspace/grok/Revision/_outils/scripts/etat_lieux.py  # si présent
```
