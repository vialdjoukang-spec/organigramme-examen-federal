# Audit médical — LOT_046_Phase_B_V0_DX.1.html
Version : 168863 octets, SHA-256 `80032402db2e7147`. Audit ciblé Θ3, points 4, 8, 9, 10, 11 ; extraits AIPS du paquet et liste HAM 30.09.2026 lus.

| Point | Note | Raison |
|---|---|---|
| 4 | 2/2 | Graves avant fréquents ; élément qui tranche et piège par DX |
| 8 | 1/2 | Critères ERS datés ; critères de gravité ATS/IDSA au premier plan (LV5) |
| 9 | 1/2 | Valeurs de référence du tableau non sourcées (HELP) |
| 10 | 2/2 | Chaque nœud mène à une décision |
| 11 | 1/2 | AIPS Augmentin adoucie ; amoxicilline dosée par HUG sans AIPS alors que l'AIPS adulte existe |

**Score : 70.0 %. Question finale : non.** Corrections Critique ouvertes ; le fichier ne passe pas la porte.

| Gravité | Pt | Extrait (≤ 200 car.) | Source |
|---|---|---|---|
| Grave | 11 | Ainsi, elle se prescrit à la dose de 1 g trois fois par jour selon la stratégie genevoise w1147a0-33 . | w1147a0-33 ; AIPS adulte à rapatrier (Amoxi-Mepha 44911, Amoxicillin Sandoz 49924 : liste HAM) — « sans AIPS » faux |
| Grave | 11 | La dose genevoise est de 1 g trois fois par jour w1147a0-33 . | aips-45674-4 (la dose HUG 3 x 1 g est le maximum AIPS, pas la dose usuelle) |
| Critique | 11 | L'usage est contre-indiqué en cas d'hypersensibilité connue aux pénicillines et aux céphalosporines, ou d'ictère lié à un traitement antérieur par Augmentin® aips-45674-7 . | aips-45674-7 (« troubles de la fonction hépatique » omis = AIPS adouci) |
| Moyen | 4 | Les seuils de définition sont un BNP supérieur à 35 pg/ml ou un NT-proBNP supérieur à 125 ng/l w149687-13 . | w149687-13, w149687-30 |
| Moyen | 11 | En outre, les recommandations internationales placent une fluoroquinolone ou un macrolide, de préférence l'azithromycine, en première ligne dans la légionellose wac7cb5-5 . | wac7cb5-5 (revue, non recommandation ; l'AIPS lévofloxacine signale une expérience insuffisante dans la légionellose, aips-62207-4) |

Corrections exactes (avant/après) : `LOT_046_Phase_B_V0_DX.1.audit.json`.

**Ce qui manque :**
- Amoxicilline orale adulte, doxycycline (Doxyclin 44000, dose dans aips-44000-8 du paquet DX.3), lévofloxacine orale (Tavanic 54365) : monopréparations présentes dans la liste HAM ; HELP « sans AIPS » faux (Grave).
- Corticoïdes de la PAC sévère : vérifier la version ERS/ESICM/ESCMID/ALAT 2023 face aux données postérieures.
