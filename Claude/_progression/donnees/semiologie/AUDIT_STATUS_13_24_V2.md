# Audit médical V2 — fiches Status S-13 à S-24 (contre-vérification, 14.11.2026)

Ce document vérifie l'application de `CORRECTIONS_STATUS_13_24.md`.

**Méthode.**
- Les 12 JSON ont passé `json.load`, puis les champs patchés ont été relus un à un.
- Les noms des fichiers retirés ont été recherchés avec grep dans `img/`, `status/*.json` et `STATUS.html`.
- La licence d'`Elevated_JVP1.jpg` a été relue par l'API Commons : la requête a abouti cette fois.
- Les attributs `occ` et le voile ont été contrôlés dans `STATUS.html`.

## 1. Majeurs

| Point | Constat | Statut |
|---|---|---|
| S-17 Schober | **Nom** : « Test de Schober ». **Technique** : jonction lombo-sacrée et repère 10 cm au-dessus. **Positif si** : augmentation < 5 cm ; variante Macrae-Wright 5 cm sous et 10 cm au-dessus, normal ≥ 20 cm (À vérifier). **Normal du geste** : 10 → ≥ 15 cm. L'ensemble est cohérent et juste. | Corrigé |
| S-13 image | `img/S-13_hernie_inguinale_debout.jpg` est absent de `img/`, des JSON et de `STATUS.html` ; le champ est passé en `a_fournir`. | Corrigé |

## 2. Retraits et images

| Point | Constat | Statut |
|---|---|---|
| S-17 Adams | Fichier absent de `img/`, des JSON et du HTML ; le champ demande un figurant adulte. | Corrigé |
| S-24 `Elevated_JVP1.jpg` | L'API lue indique **CC BY-SA 3.0**, James Heilman, MD, avec la mention « Consent of person in picture obtained ». La légende signale la jugulaire probablement externe et précise que la mesure se fait sur l'interne. | Conforme |
| S-14, S-16 images intimes | `"occulter": true` est présent. `STATUS.html` contient 2 vignettes `occ`, chacune avec le voile « Image intime masquée ». | Conforme |

## 3. Mineurs : 24 sur 24 vérifiés

| Fiche | Points relus et justes |
|---|---|
| S-13 | Lampe retirée. |
| S-14 | Varicocèle droite, récente ou qui ne s'affaisse pas couché : rechercher une compression rénale ou cave. |
| S-16 | Renvoi corrigé en « voir S-12 ». |
| S-17 | Bragard en flexion dorsale ; technique du Spurling décrite. |
| S-18 | SY-59 cité ; nuque examinée en premier, sans contradiction ; Duale Reihe avant Hegedus. |
| S-19 | Hypoalgésie à la piqûre (RV 3,1 ; IC 2,0–5,1), conforme au résumé D'Arcy ; Finkelstein décrit ; syndrome des loges (SY-61) ajouté ; ordre des sources corrigé. |
| S-20 | Thomas : flessum controlatéral ; FABER ajouté ; mention « aucune source » déplacée dans `valeur`. |
| S-21 | Lachman « sans à-coup » ; critères d'Ottawa du genou détaillés. |
| S-22 | Installation reformulée ; SY-61 cité. |
| S-23 | IPS : normal 1,00–1,40 et zone limite 0,91–0,99 ; Lederle ajouté ; ESC citée par Eur Heart J 2024;45:3538-3700. |
| S-24 | Renvoi vers S-10 ; Wells 1997 (3 niveaux) et 2003 (2 niveaux) distingués ; CEAP étiquetée « source américaine ». |

**Aucune erreur médicale nouvelle** n'est apparue dans les champs modifiés.

## 4. Résidus (mineurs, non bloquants)

| Grav. | Champ | Ancien → Nouveau |
|---|---|---|
| Mineur | S-17 manoeuvres_speciales[1].image.a_fournir | « (L5 et 10 cm au-dessus) » → « (jonction lombo-sacrée et 10 cm au-dessus) » : alignement sur la technique corrigée |
| Mineur | S-24 sources | Placer « Füeßl/Middeke, Duale Reihe » avant « Wells PS… (source canadienne) », pour respecter l'ordre Europe → autre |
| Mineur | S-20 FABER .geste | Ajouter « en stabilisant l'épine iliaque antéro-supérieure opposée » après « légère pression sur le genou » |

## 5. Verdict
**audit-ok.** Les 2 majeurs et les 24 mineurs sont corrigés. Les images retirées ont disparu partout. La licence d'`Elevated_JVP1.jpg` est confirmée, et les 2 images intimes sont masquées. Les 3 résidus mineurs peuvent être corrigés au prochain passage. Les images `a_fournir` (S-13, S-17 Adams, gestes) restent à produire par une séance photo sous CC BY 4.0.
