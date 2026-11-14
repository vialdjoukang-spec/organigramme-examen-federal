# Contre-audit PHY-S5 à PHY-S8 (tour 2)

Auditeur indépendant, 14.11.2026. Objet : vérifier dans les fiches que `CORRECTIONS_PHY_S5_S8.md` a bien corrigé le défaut Grave et les défauts Moyens n° 2 à 9, et chercher toute erreur nouvelle. J'ai lu les champs JSON des fiches et non le seul relevé des corrections.

## 1. Vérification des corrections

| N° | Fiche | Constat dans le JSON | Verdict |
|---|---|---|---|
| 1 (Grave) | S7-3 | La `valeur` indique « hausse ≥ 60 % (doublement en moyenne) ». L'`usage` dit « fait suspecter… sans la prouver ; l'hCG ne localise pas… ; jamais un méthotrexate sur ce seul critère ». L'`exemple` et la cible méthotrexate concordent ; le calcul 25 % est juste. | **Corrigé** |
| 2 | S8-3 | 550 nmol/L est daté ; Elecsys Cortisol II donne 426 nmol/L à 30 min et 485 nmol/L à 60 min ; l'unité renvoie au seuil propre au laboratoire. | Corrigé ; le paragraphe 2 juge l'applicabilité |
| 3 | S8-4 | Les conditions aldostérone > 240 pmol/L et plancher de rénine sont présentes ; l'exemple (600 pmol/L) les respecte. | Corrigé |
| 4 | S6-6 | Le trou corrigé = trou + 0,25 × (40 − albumine) ; la norme dépend de l'automate ; GOLDMARK est en place. | Corrigé |
| 5 | S5-5 | Le mécanisme est juste : acide et pepsine, puis haptocorrine, protéases pancréatiques et facteur intrinsèque ; une source HUG 2013 est marquée « lu ». | Mécanisme corrigé, **mais l'ajout crée l'erreur nouvelle A** |
| 6 | S7-4 | Le texte remplaçant n'est plus une thrombose : « hémorragie du post-partum, pré-éclampsie : terrain hypercoagulable et vasculaire PP-S7-V ». | **Erreur nouvelle B** |
| 7 | S7-4 | La ligne « seuils propres à la grossesse : à vérifier (non vérifié CH) » est ajoutée. | Corrigé (honnête) |
| 8 | S5-4 | Le HPC Swissmedic sur Ocaliva du 20.08.2025 est cité et marqué « lu » ; les agonistes PPAR sont proposés en deuxième ligne. | Corrigé (je n'ai pas relu le HPC) |
| 9 | S8-9 | Le lactate est donné en « mmol/L… par déduction ». | Corrigé |
| 10 | toutes | Les sources lues ajoutées sont étiquetées ; le reste garde « déduction ». | Corrigé, sous la réserve C |
| Légers | échantillon de 14 | S5-1, S5-6 (1972 et facteur V), S5-7, S5-8, S6-1, S6-3, S6-5, S7-1, S7-2, S7-6 (ESHRE, présent dans EX-1-S7-fsh-lh), S7-7, S8-5, S8-6, S8-8 | Tous sont conformes au patch |

## 2. Synacthen 426/485 nmol/L : applicable au dosage de l'Insel ?

J'ai relu Okutan et al., Endocrine 2024 (PMC11246257) le 14.11.2026. Les seuils correspondent au 2,5e percentile ajusté de 100 volontaires sains de Copenhague. Le test utilisait 250 µg de Synacthen IV, entre 8 et 10 h, à jeun. Les femmes sous contraception œstrogénique étaient analysées à part et exclues des seuils.

**Jugement : le seuil s'applique au dosage Insel sous condition, mais il ne s'y transpose pas d'office.** La fiche EX indique que l'Insel travaille sur cobas pro, plateforme du dosage Elecsys Cortisol II ; la plateforme concorde donc. Il manque toutefois une preuve écrite que l'Insel emploie Cortisol II pour ce test, et aucune validation suisse n'existe. Il faut aussi préciser trois limites :

- le test standard utilise 250 µg ;
- la cohorte provient d'un seul centre ;
- les œstrogènes oraux élèvent la CBG et donc le cortisol total, ce qui peut rassurer à tort.

La formulation actuelle (« on demande celui du laboratoire Insel ») reste acceptable. Je propose de la préciser par le patch D.

## 3. Erreurs nouvelles et PATCH exact

| Réf. | Fiche, champ | Extrait | Gravité | PATCH exact |
|---|---|---|---|---|
| A | S5-5 `dereglements[4]` | « insuffisance pancréatique exocrine (malabsorption de la B12) PP-S5-T » | Moyen | PP-S5-T est la fiche « Tumoral » : l'insuffisance exocrine y est mal rangée, puisqu'elle vient surtout de la pancréatite chronique ou de la mucoviscidose. Remplacer l'affection par « cancer pancréatique (insuffisance pancréatique exocrine, malabsorption de la B12) » et garder `"pp": "PP-S5-T"`, `"semiologie": ["SY-39"]`. Signaler « pancréatite chronique » comme complément PP à venir. |
| B | S7-4 `dereglements[2]` | « hémorragie du post-partum, pré-éclampsie : terrain hypercoagulable et vasculaire » | Moyen | Le texte est faux sur le plan physiopathologique : l'hémorragie du post-partum ne découle pas de l'hypercoagulabilité, et la thrombose a disparu. Remplacer par `{"affection": "maladie thromboembolique veineuse de la grossesse (hypercoagulabilité ; fiche PP dédiée à venir)", "pp": "PP-S7-V", "semiologie": ["SY-23"]}`. La pré-éclampsie figure déjà en `dereglements[0]`. |
| C | S7-3 `sources` (NICE) | « lu par l'auditeur le 14.11.2026 » | Léger | J'ai lu le résumé du résultat de recherche de la page NG126, pas la page entière. Écrire : « seuil de 63 % vu par l'auditeur dans un résumé de recherche de la page NG126 (14.11.2026) ; page non lue en entier ». |
| D | S8-3 `valeurs_normales[1].unite` | « on demande celui du laboratoire Insel » | Léger | Ajouter : « seuils danois (100 volontaires sains, 250 µg IV, femmes sous œstrogènes oraux exclues) ; applicables si l'Insel dose par Elecsys Cortisol II (cobas), ce qui reste à confirmer ; les œstrogènes oraux élèvent faussement le cortisol total ». |
| E | toutes `honnetete` | même texte partout, qui cite « Swissmedic, HUG, RMS, Okutan 2024 » | Léger | Dans chaque fiche, ne citer que les sources marquées « lu » de cette fiche. |

## 4. Phrases verbales

`verbal.py` signale 324 phrases sur 876. J'en ai lu un échantillon aléatoire de 25 :

- 21 sont des étiquettes : unités, chaînes, classes, affections, `fonction`, mnémotechniques ;
- 4 sont des phrases rédigées dont le verbe manque au lexique (« sécrète », « réabsorbe », « forme », « ajuste »).

Je n'ai trouvé aucune phrase nominale réelle. Ces signalements ne bloquent pas.

## 5. Verdict

Le défaut Grave est corrigé. Huit défauts Moyens sur neuf sont corrigés, et 2 erreurs Moyennes nouvelles sont apparues (A, B). **Prêt pour `audit-ok` ? Non.** Il manque les patchs A et B ; C, D et E sont souhaités. Une fois A et B appliqués à l'identique, l'audit peut passer sans troisième tour. La fiche PP « MTEV de la grossesse » reste un complément à venir et ne bloque pas.
