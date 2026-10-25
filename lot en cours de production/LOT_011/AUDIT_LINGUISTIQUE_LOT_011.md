# Audit linguistique et de conformité — LOT_011 — G11 Troubles du sommeil

Auditeur linguistique et de conformité, rôle distinct du rédacteur d’origine et distinct de l’auditeur médical.
Date : 2026-10-25, 18:15 Europe/Zurich.
Prompt : V8 §5.2–5.3, §6.3, §7, §8, §10, §12.
Le score §6.3 ci-dessous est le même que celui de l’audit médical : il agrège les cinquante questions. Cet avis détaille la forme, le plan et la technique.

## Score §6.3

| Fichier | Plan 14 points | FIN_FICHIER | `title=` | Taille | Score §6.3 |
|---|---|---|---|---|---|
| Appel A | SSP et dix DX, 14 points chacun | oui | 0 | 151,7 Ko | **90 %** |
| Partie 1 | DX.1 et DX.2 | oui | 0 | 92,4 Ko | **93 %** |
| Partie 2 | DX.3 à DX.5 | oui | 0 | 89,3 Ko | **89 %** |
| Partie 3 | DX.6 et DX.7 | oui | 0 | 75,1 Ko | **90 %** |
| Partie 4 | DX.8 à DX.10 | oui | 0 | 86,2 Ko | **89 %** |

Zéro erreur critique de forme restante. Les parties 2 et 4 restent sous 90 % à cause des questions médicales de situations spéciales, pas à cause d’un point du plan manquant. Les parties 2, 3 et 4 sont sous 90 Ko après retrait du remplissage.

Hors du §6.3, la liste de contrôle V8 §16 exige aussi 90 à 200 Ko. Cette case n’est pas cochée pour les parties 2, 3 et 4. Le texte utile n’a pas été allongé pour franchir le seuil.

## Corrections

### Critique

Aucune.

### Grave

1. Fichiers : partie 1 (11 fois), partie 2 (4), partie 3 (41), partie 4 (12). Emplacement : après chaque mémo d’examen. Extrait mot pour mot : « Sur la copie, cette décision se rédige en phrase verbale. On nomme la source lue le 25.10.2026 lorsqu’elle existe, [S1] à [S5] selon le cas, et l’on n’habille pas un souvenir. Une prévalence suisse non ouverte reste À vérifier. Une posologie reste À vérifier (AIPS). Un droit de la conduite non lu reste À vérifier. Le badge du propriétaire ne se corrige pas pour faire plaisir à un seul article, et l’article ne se cache pas pour faire plaisir au badge. » Correction : paragraphe retiré partout. Les mémos cliniques uniques sont conservés. Source : V8 §7, interdiction du remplissage. La partie 3 passait de 92,5 Ko à 75,1 Ko : la marge au-dessus de 90 Ko était ce doublon.
2. Fichiers : tous les HTML, bandeau et pied. Extrait : « Il n’est pas déposé dans LOTS_Finaux. » et « Audit indépendant non réalisé. » Correction : le bandeau dit maintenant que l’audit correcteur du 25.10.2026 a eu lieu et renvoie aux rapports. Une copie Drive préexistait. Source : V8 §1, ne pas affirmer un état faux. Le dépôt de la version corrigée n’est pas annoncé comme fait.

### Moyen

1. Fichiers : les cinq HTML. Emplacement : `<div class="tablewrap">`. Extrait : la classe CSS portait `overflow-x:auto`, pas l’attribut exigé. Correction : `style="overflow-x:auto;"` ajouté sur chaque enveloppe. Les tableaux étaient déjà scrollables. Source : V8 §10.
2. Fichiers : Appel A (cinq occurrences). Extrait : « que je n’ai pas ouvert », « que je n’ai pas ouverte », « que je n’ai pas ouvertes ». Correction : tournure impersonnelle (« qui n’a pas été ouvert »). Source : V8 §7, pas de méta-commentaire à la première personne.
3. Fichiers : Appel A, point 11 ; partie 1, fenêtre « Limite ». Emplacement : la fenêtre d’audit avait été insérée à l’intérieur d’un `<p>` non fermé, et deux `</p>` se suivaient. Correction : paragraphes et fenêtres séparés. Balises `p`, `details`, `div`, `table`, `li`, `ol`, `section` rééquilibrées. Aucune ligne ne dépasse 3 000 caractères. Source : V8 §10.
4. Fichier : partie 1, question 2 de l’entraînement. Extrait : « aucune dose n’est écrite : À vérifier (AIPS) ». Correction : la phrase dit maintenant qu’on ne commence pas Quviviq® le jour même si une apnée est plausible, tout en reconnaissant que la dose d’insomnie est lue ailleurs. Source : cohérence interne après l’ajout AIPS ; V8 §1.

### Léger

1. Fichiers : parties B, tableaux « But / Moyen / Surveillance ». Extrait : « Confirmer », « Dès ce soir », « Médicament », « Zéro blessure ». Correction : non réécrites une à une. Ce sont des intitulés de cellules, pas des phrases. Elles restent un écart léger avec V8 §7, qui veut un verbe dans les tableaux. Les réécrire toutes aurait élargi le diff sans fait nouveau.
2. Fichiers : parties B. Les mémos numérotés sont nombreux et répétitifs dans l’intention, mais chaque paragraphe clinique diffère. Ils sont gardés. Seul le refrain identique a été jugé grave.

## Plan, fenêtres, pédagogie

Les quatorze points sont présents pour le SSP et pour chaque DX. Les sous-parties 11.A à 11.D existent sous forme de fenêtres ou de tableaux But / Moyens / Surveillance / pronostic. Les fenêtres `<details>` sont utilisées. Aucun `title=` ne sert d’infobulle. Aucun script, aucune image, aucune feuille externe. Le viewport et la règle 390 px sont dans la feuille interne. La mention de non-validation clinique est en place. La balise `FIN_FICHIER` est présente.

La question finale §6.2 n’est pas satisfaite à 100 % pour les DX dont la grossesse, le foie, le rein ou la dose suisse restent « À vérifier ». Elle est mieux satisfaite pour l’insomnie, où le premier choix européen et la seule spécialité suisse lue sont maintenant écrits. Un candidat ne peut pas encore traiter de mémoire sûre la narcolepsie, les jambes sans repos ou le trouble paradoxal sur le plan médicamenteux. C’est assumé dans le score, pas masqué.

Contenu d’audit produit par IA ; non validé cliniquement par un médecin.
