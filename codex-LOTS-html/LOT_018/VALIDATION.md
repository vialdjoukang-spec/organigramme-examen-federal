# Validation de production — LOT_018

État : onze leçons produites et relues en session unique, selon l’accord de Vial du 30.10.2026. Contrôles statiques V8 validés. Ce constat ne constitue pas une validation clinique, un audit indépendant ou une note de qualité médicale.

## Résultats contrôlés

- 11 fichiers HTML complets ; 14 parties et 14 questions par fichier, soit 154 questions.
- 275 contrôles statiques réussis ; liens locaux et entre leçons résolus.
- 161 fenêtres atteignables depuis la fiche, avec fermeture explicite ; fonctionnement réel au navigateur non testé.
- 183 paragraphes de citation AIPS retrouvés dans les fichiers originaux fournis ; seules les espaces sont normalisées pour la comparaison.
- Neuf empreintes du harnais inchangées ; polices locales embarquées et feuille de style officielle reprise.

| Fichier | Texte principal (Ko) | Fenêtres (Ko) | Contrôle statique |
|---|---:|---:|---|
| [Phase A](LOT_018_Phase_A_V0.html) | 13.1 | 41.3 | Réussi |
| [DX.1](LOT_018_Phase_B_V0_DX.1.html) | 5.2 | 11.4 | Réussi |
| [DX.2](LOT_018_Phase_B_V0_DX.2.html) | 5.1 | 10.4 | Réussi |
| [DX.3](LOT_018_Phase_B_V0_DX.3.html) | 5.1 | 16.5 | Réussi |
| [DX.4](LOT_018_Phase_B_V0_DX.4.html) | 4.9 | 13.9 | Réussi |
| [DX.5](LOT_018_Phase_B_V0_DX.5.html) | 5.0 | 16.8 | Réussi |
| [DX.6](LOT_018_Phase_B_V0_DX.6.html) | 5.2 | 15.6 | Réussi |
| [DX.7](LOT_018_Phase_B_V0_DX.7.html) | 5.2 | 10.3 | Réussi |
| [DX.8](LOT_018_Phase_B_V0_DX.8.html) | 5.5 | 16.4 | Réussi |
| [DX.9](LOT_018_Phase_B_V0_DX.9.html) | 5.0 | 10.0 | Réussi |
| [DX.10](LOT_018_Phase_B_V0_DX.10.html) | 5.6 | 22.1 | Réussi |

Limites appliquées par le script officiel `taille_xy.py` : 100 Ko de texte principal pour la Phase A ; 9 Ko pour chaque diagnostic. Les fenêtres ne sont pas plafonnées. Le manifeste contient les onze empreintes finales.

## Compatibilité des contrôleurs

Les scripts officiels ont réellement été exécutés et retournent le code 1. Leurs rapports bruts sont conservés : `audits/controle_officiel.json` et `audits/langue*.json`. Ils n’ont pas été modifiés.

| Règle historique qui échoue | Norme V8 appliquée (§12 du prompt maître) | Vérification complémentaire |
|---|---|---|
| Interdiction de tout `title` | `<abbr title>` explicitement demandé | `title` réservé aux abréviations non vides |
| Sources littérales `[S1]` | Exposants bleus, sans `[S1]` | Citations et entrées Sources reliées, URLs présentes |
| 14 titres `h3` | Parties en îlots avec `h2`, comme le modèle V8 | 14 identifiants ordonnés, titres DX canoniques exacts |
| Bande du fichier 80–150 Ko (DX.2 sous 80 Ko) | Taille du texte x, excluant fenêtres et balisage | Mesure officielle x conforme pour les onze fichiers |

Les avertissements linguistiques ont été examinés. Les sigles médicaux signalés sont définis dans `abbr`, que le contrôle historique ignore. Les répétitions relevées correspondent aux déclencheurs et titres de fenêtres. Les longues phrases AIPS et leur ponctuation sont conservées pour respecter le texte cité. La phrase explicative longue de DX.8 a été scindée. Les espaces insécables réclamées par le contrôle de langue restent exclues par le prompt. Les points-virgules restants sont un signal stylistique indicatif.

Le script complémentaire `../outils/verifier_lot_v8.py` contrôle la norme V8 sur les fichiers finaux. Il ne transforme pas le résultat du contrôleur historique en succès.

## Portée de la relecture

La relecture de la session principale a vérifié : cohérence des dix noms avec la Phase A ; distinction urgence artérielle/veineuse ; menace visuelle de l’ACG ; diagnostic de glaucome indépendant de la seule pression ; phénotypes de névrite ; gaz intraoculaire ; doses suisses par produit et par indication. Les corrections et choix sont consignés dans `CORRECTIONS_AUDIT.md`, `audits/corrections_internes.jsonl` et le journal de routage.

Aucun auditeur externe ni médecin n’a validé ces leçons. Aucun score 95/100 ou 90/100 n’est attribué. Le nombre de défauts médicaux graves n’est pas établi indépendamment. Le classement des dix diagnostics est pédagogique, pas un classement statistique démontré.

Le rendu navigateur et mobile reste non vérifié : téléchargement Playwright refusé HTTP 403 ; Chromium local refuse `file://` avec `net::ERR_BLOCKED_BY_ADMINISTRATOR`. Aucune restriction n’a été contournée. L’accord de poursuite autorise le dépôt avec ces limites connues.
