# Audit médical — LOT_046_Phase_B_V0_DX.2.html
Version : 174830 octets, SHA-256 `3a7bec06640482b3`. Audit ciblé Θ3, points 4, 8, 9, 10, 11 ; extraits AIPS du paquet et liste HAM 30.09.2026 lus.

| Point | Note | Raison |
|---|---|---|
| 4 | 2/2 | CHAMPIT, graves avant fréquents, tableau tranche/piège |
| 8 | 1/2 | Classe FEVG 41-49 % supprimée par l'ESC 2026 ; seuil d'inclusion NT-proBNP < 50 ans omis |
| 9 | 1/2 | Néphropathie au contraste et prémédication « allergie à l'iode » selon définitions anciennes |
| 10 | 2/2 | Nœuds décisionnels ; NT-proBNP aigu < 300 correct |
| 11 | 0/2 | CI torasémide renvoyée alors que lue ; ESC 2021/2023 périmée (ESC 2026) et lue par revues |

**Score : 60.0 %. Question finale : non.** Des corrections Critique restent ouvertes ; le fichier ne passe pas la porte.

| Gravité | Pt | Extrait (≤ 200 car.) | Source |
|---|---|---|---|
| Critique | 11 | Voir l'information professionnelle aips-58181-5 | aips-58181-10 (CI lues dans le corpus, renvoyées) |
| Grave | 11 | Insuffisance rénale aiguë, hyperkaliémie, anurie aips-27257-8 | aips-27257-8 (ClCr < 30 omise) |
| Grave | 11 | Tachyarythmies réfractaires, tamponnade, sténose aortique aips-45687-8 | aips-45687-8 (asthme omis dans un cours de dyspnée) |
| Moyen | 11 | Les dérivés nitrés sont recommandés par l'ESC dès que la pression artérielle systolique dépasse 110 mmHg w67f662-14 . | w67f662-14 (ESC 2021 : classe IIb, « peut être envisagé », lu par revue secondaire) |
| Grave | 11 | La recommandation de l'ESC de 2021 le propose chez tous les patients en insuffisance cardiaque aiguë, avec la classe I et le niveau de preuve C, soit un consensus d'experts we1c591-9 . | we1c591-9 ; ESC 2021 remplacée par ESC 2026 (doi 10.1093/eurheartj/ehag100, 28.08.2026) : LV8 |

Corrections exactes (avant/après) : `LOT_046_Phase_B_V0_DX.2.html.audit.json`.

**Ce qui manque :**
- LV8 : la recommandation ESC 2026 de l'insuffisance cardiaque (publiée le 28.08.2026, doi 10.1093/eurheartj/ehag100) remplace ESC 2021 et 2023 : « décompensée » remplace « aiguë », HFmrEF supprimée. Relire tout le fichier sur ce texte primaire.
- Noradrénaline (Sintetica 60955), milrinone (59467), lévosimendan (Simdax 62463), morphine (51039), bisoprolol (Concor 47311) : monopréparations HAM ; HELP « sans AIPS » faux (Grave).
- Forxiga, Jardiance : contre-indication « Voir l'information professionnelle » alors que aips-65176-10 et aips-63227-10 sont lus (Léger : hypersensibilité seule).
