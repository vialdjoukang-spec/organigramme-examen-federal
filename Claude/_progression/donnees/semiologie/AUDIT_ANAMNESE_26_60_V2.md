# Audit V2 (contre-vérification) : A-MOT-26 à A-MOT-60

Auditeur indépendant, 14.11.2026. Bases de la vérification : `CORRECTIONS_ANAMNESE_26_60.md` et les 35 JSON relus par script et à la main. Sources confrontées : HUG Céphalées 2022 (tableau 2, tableau 7, § 5.3, critères d'abus médicamenteux), HUG Alcool 2021 (§ 2.1, § 2.4), HUG Dépression 2022 (tableau 4b), HUG Personne âgée 2026 (§ 4.3), HUG Monoarthrite 2024. Tous ces PDF ont été lus lors de l'audit V1.

## 1. Vérification des corrections

| # | Fiche | Statut | Constat |
|---|---|---|---|
| G-1 | 26 | Corrigé | Les 11 drapeaux et le piège couvrent les 15 critères SNNOOP10 du tableau 2 HUG. Le seuil de 10 à 15 jours d'antalgiques est conforme à HUG 2022 (≥ 15 j pour paracétamol et AINS, ≥ 10 j pour triptans et opiacés) |
| G-2 | 27 | Corrigé | Drapeau « chute » et axe « Chutes (HUG) » conformes à HUG Personne âgée 2026 § 4.3 |
| G-3 | 31 | Corrigé | Drapeau AVC placé en tête, 144, filière AVC ; SY-12 et IMG-001 sont liés |
| M-1 | 26 | Corrigé | Règle angio-TDM < 6 h, puis PL, conforme au tableau 7 et au § 5.3 |
| M-2 | 28 | Corrigé | Drapeau « quel que soit le délai » ; glycémie chez tout patient ; délais marqués « À vérifier » |
| M-3 | 32 | Corrigé | AIT rétinien adressé le jour même par la filière AVC |
| M-4 | 33 | Corrigé | Drapeau et hypothèse « cellulite orbitaire » présents |
| M-5 | 36 | Corrigé | Hypothèse V (SCA) et syndrome de Lemierre ajoutés ; piège Centor réécrit en phrases verbales |
| M-6 | 55 | **Mal corrigé** | Le nouveau texte est juste, mais l'ancien reste collé derrière lui (voir N-1) |
| M-7 | 38 | Corrigé | Exception « sauf sepsis » présente |
| M-8 | 51 | Corrigé | Gradation RUD conforme au tableau 4b |
| M-9 | 52 | Corrigé | Axes R, U, D ; 144 ajouté |
| M-10 | 21 fiches | Corrigé | Il ne reste aucun triplet générique. Deux répétitions restent acceptables (« Avez-vous peur d'un cancer ? » ×2, « Qu'attendez-vous de cette consultation ? » ×3) |
| M-11 | Toutes | Corrigé | Les conduites sourcées gardent leur source (33, 34, 42, 56 : HUG ou RMS) ; les autres portent « déduction, non vérifié CH » |
| « lu » | 7 sources | Acceptable | La partie lue est précisée pour chacune (points à retenir, tableau B12, figure 1, algorithme). Je ne les ai pas relues moi-même |

## 2. Défauts restants et PATCH exacts

| # | Grav. | Fiche, champ | Extrait fautif (≤ 200 car.) | PATCH exact |
|---|---|---|---|---|
| N-1 | **Moyen** (erreur nouvelle) | 55 `pieges[1]` | « …cite encore l'ancien seuil de 4 et 2 verres. : plus de 4 verres standard par jour chez l'homme, plus de 2 chez la femme ; un verre standard contient 10 à 12 g d'alcool (ASSM § 3.6 ; HUG 2021 : 10 g). » | Supprimer tout ce qui suit « …l'ancien seuil de 4 et 2 verres. » Remplacer la fin par : « …l'ancien seuil de 4 et 2 verres, avec 10 à 12 g par verre. » |
| N-2 | Léger | 26 `sources[2]` | « (lu : points à retenir et tableau 2 des drapeaux rouges SNNOOP10) » | « (lu : points à retenir, tableau 2 SNNOOP10, tableau 7 imagerie, § 5.3 ponction lombaire, critères de céphalée par abus médicamenteux) » |
| N-3 | Léger | 26 `drapeaux_rouges[10].si_oui` | « …prévenir la chronicisation (HUG 2022, tableau 2). » | « …prévenir la chronicisation ; le seuil est de 15 jours par mois ou plus pour le paracétamol et les AINS, et de 10 jours ou plus pour les triptans et les opiacés (HUG 2022, tableau 2 et critères d'abus médicamenteux). » |
| N-4 | Léger | 31 `hypotheses[0].question_discriminante` | « La douleur au mollet apparaît-elle toujours après la même distance de marche ? » | « L'engourdissement est-il apparu d'un coup, d'un seul côté, visage compris ? » |

## 3. Verdict

| Question | Réponse |
|---|---|
| Les 3 défauts graves sont-ils corrigés ? | Oui |
| Les 11 défauts moyens sont-ils corrigés ? | 10 sur 11. M-6 a laissé l'ancien texte en place (N-1) |
| Les fiches peuvent-elles recevoir `audit-ok` ? | **Oui, sous condition** : appliquer N-1, qui est une correction mécanique, sans nouvel audit. N-2 à N-4 sont recommandés mais ne bloquent pas |

## Clôture
N-1 à N-4 appliqués mot pour mot : **audit-ok** pour A-MOT-26 à 60. Toute la Sémiologie (Status, Syndromes, Anamnèse, Management, Communication) est audit-ok.
