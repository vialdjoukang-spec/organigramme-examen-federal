# Préparation mécanique du rendu DX.1 / DX.6 — 02.11.2026

Statut : **convertisseur préparé, aucun HTML produit**. Mission limitée à `_travail/rendre_dx.py` et ce rapport. Aucun audit clinique indépendant revendiqué. Aucun Git, catalogue, formatter partagé, source Phase A, journal global ou image modifié. Le root a déclaré le harnais vert et conserve son verrou d’intégration.

| Élément | Résultat / limite |
|---|---|
| Lectures | GUIDE.md, HARNAIS_FOURNI.md, BRACELET_FOURNI.md, formatter du LOT, deux rédactions et leurs sources ; AGENTS.md et docs/ARSENAL.md lus. |
| Conversion prévue | Instance isolée de `Lesson(title,n)` ; `S` et `T` remplacés uniquement en mémoire pour chaque DX. Titres spécifiques des auteurs conservés. |
| Conservation | Corps, préambule, réserves et annexes conservés dans les fenêtres ; gras, références, tableaux et listes convertis. Base réduite aux titres cliquables, sans résumé clinique automatique. |
| Sources | JSON DX propres ; identifiants S/A convertis en ancres numériques locales tout en gardant leurs labels visibles. Plages S6–S8 développées ; qualifications après point-virgule conservées. |
| Compléments | `--sources 1:chemin.json` ou `--sources 6:chemin.json`, répétable ; schéma `{sources: [{id, titre ou title, url, …}]}`. Une référence absente ou une redéfinition contradictoire bloque. Les autres formats de preuves AIPS doivent être normalisés explicitement par l’auteur : aucune découverte implicite ni attribution inventée. |
| Contrôle réellement exécuté | Mode sans option : DX.1 = 14 parties, 14 questions, 14 références résolues ; DX.6 = 14 parties, 14 questions, 8 références résolues, au moment de ce contrôle. Les auteurs peuvent encore modifier ces entrées. |
| Vérifications supplémentaires | Compilation en mémoire ; assertions ciblées références avec plages/qualifications, tableau, gras, HTML inline. Pas d’écriture `.pyc`, pas de rendu complet lancé. |
| Garde du futur rendu | Préparation en répertoire temporaire ; 14 sections, 14 questions, cibles de références présentes et fiche base ≤ 9000 octets avant écriture. SHA-256 des entrées vérifiés pour refuser une mutation concurrente. |
| Taille | Le contrôle ≤ 9000 octets porte sur le HTML de `<main>` à la première fenêtre, donc titre, réserves générales, sommaire et 14 parties ; les fenêtres et la bibliographie restent hors base. Taille réelle non mesurée sans rendu. Bande totale du harnais et fonctionnement visuel restent à contrôler après feu vert root. |
| Markdown | Convertisseur stdlib volontairement limité aux constructions présentes : paragraphes, titres, listes simples, tableaux rectangulaires, gras/italique, code inline, liens HTTP(S), HTML inline. Pas de promesse de conformité CommonMark complète ; blocs de code et tables non reconnues refusés. Listes imbriquées/HTML complexes nouveaux nécessitent une adaptation mécanique avant rendu. |
| Statut | Les réserves préparatoires des auteurs et du formatter restent visibles. Pas d’image ajoutée ni de validation pharmacologique ou médicale par le script. |

Commande de contrôle, sans produire de HTML :

```sh
python3 -B codex-LOTS-html/LOT_133/_travail/rendre_dx.py
```

Commande **à lancer seulement après signal root**, une fois les auteurs et preuves stabilisés :

```sh
python3 -B codex-LOTS-html/LOT_133/_travail/rendre_dx.py --render
```

Le formatter conserve ses noms canoniques `LOT_133_Phase_B_V0_DX.1.html` et `.6.html` ; « V8 » ne crée pas un suffixe de fichier nouveau. Après rendu, le root doit exécuter le harnais fourni, mesurer les tailles finales, vérifier les fenêtres/liens/tableaux et obtenir les contrelectures demandées. Le présent document prouve une préparation mécanique, pas un rendu validé.

## Compléments normalisés après instruction root

Deux fichiers propres ajoutés : `evidence/SOURCES_RENDU_DX1_0330.json` (S13–S17) et `evidence/SOURCES_RENDU_DX6_0330.json` (A1–A6). Identifiants cliniques inchangés. Les cinq URL DX1 sont reprises des références auteur et leur présence dans `lectures_web.json` est vérifiée. Les six URL DX6 proviennent des notices de `DX6_COMPLEMENT_0330.json` ; leurs caches texte existent, leur SHA-256 a été calculé et les trois URL anciennes AIPS correspondent à `DX6_AIPS_0240.json`. Les titres des médicaments proviennent de la première ligne de leurs caches réels. Limites de lecture et fraîcheur conservées ; aucune nouvelle consultation réseau revendiquée.

Contrôle à blanc réellement exécuté après normalisation : **DX1 = 14 parties, 14 questions, 19 références résolues ; DX6 = 14 parties, 14 questions, 14 références résolues.** Aucun rendu exécuté. Le mode par défaut sans `--sources` refuse volontairement les nouvelles références non résolues ; utiliser les compléments explicitement :

```sh
python3 -B codex-LOTS-html/LOT_133/_travail/rendre_dx.py \
  --sources 1:codex-LOTS-html/LOT_133/evidence/SOURCES_RENDU_DX1_0330.json \
  --sources 6:codex-LOTS-html/LOT_133/evidence/SOURCES_RENDU_DX6_0330.json
```

Ajouter `--render` uniquement après signal root et audit. Ces contrôles attestent la liaison des identifiants aux preuves auteur, pas la pertinence clinique des citations ni l’existence d’une version réglementaire plus récente.

## Corrections demandées par le root — périmètre du rendu

Cette section remplace les indications précédentes sur la conservation du préambule et des annexes dans les fenêtres. Seuls les paragraphes de périmètre clinique sont repris du préambule, sans auteur, version technique ni « Aucun HTML produit ». Un statut explicite de monographie préparatoire non exhaustive les introduit. Les 14 corps médicaux restent inchangés. Les références brutes, chemins de caches et journaux de corrections après les questions restent dans les Markdown de preuve ; la bibliographie HTML du formatter est conservée.

La coupure documentaire du DX6 inclut désormais « Sources et passages », avant son journal, pour éviter de rattacher les chemins de caches à la réponse 14. La bannière historique « liste non gelée » est remplacée uniquement dans le rendu local par « liste pédagogique figée ; monographie préparatoire ; illustrations absentes ». Si cette bannière du formatter change, le script refuse de poursuivre au lieu d’effectuer un remplacement aveugle.

Les fichiers temporaires futurs seront créés exclusivement sous `_travail/_cache/dx-render-*` ; aucun recours au répertoire temporaire système. Syntaxe, extraction du périmètre clinique et exclusion des métadonnées du quiz vérifiées sans rendre de leçon. Contrôle à blanc réexécuté : 14 parties et 14 questions chacun ; 19 références DX1 et 14 DX6. **Aucun `--render` exécuté ; signal root après audit toujours attendu.**

## Rendu effectivement exécuté après signal root

Le root a autorisé explicitement les deux HTML après le verdict final de `AUDIT_DX1_DX6_0330.md`. Les SHA-256 des Markdown ont été comparés aux versions exactes autorisées avant conversion : DX1 `00e1f35f981190d9deac8f309a4444c08d054289539a8f27892748e73f92c9d2`, DX6 `da40816347a27b584c2ecefd8aa395136084fcac8f3409056003701d691b32c0`.

La commande documentée ci-dessus a été exécutée avec `--render`. Fiche de base DX1 : **5827 octets** ; DX6 : **5510 octets**. Chacun contient 14 parties et 14 questions ; toutes les références ont une cible. Les chaînes de journal/auteur initial/chemins introductifs de sources et la bannière non gelée sont absentes des rendus.

| HTML produit | Octets totaux | SHA-256 |
|---|---:|---|
| DX.1 | 102569 | `64a42119fd36374257af40393afc21d865ee93e9f247b1eff58ea58ad12b77a8` |
| DX.6 | 94336 | `cd890c4f6946827a3911cf421795df3528866e5a32ffc0277695ef7a14d17c1e` |

Les mentions antérieures « aucun HTML produit » décrivent les étapes précédentes et sont désormais remplacées par ce résultat. Le root assure encore QA statique, harnais et navigateur. Aucune validation globale ou publication comme monographie thérapeutique complète revendiquée ; aucun Git effectué.

## Consolidation finale de l’orchestrateur

Titre DX1 aligné sur la liste canonique ; corps médical inchangé après dernier contrôle distinct. Métadonnées finales :

- DX1 : 102280 octets ; SHA256 `d1081c88077c79478eae3f8564296dd48ce617c23be5044482278e4fb6e95636`.
- DX6 : 94003 octets ; SHA256 `edf67b89f32979be7a7b7fc59049cf7b7b9117c87117d6e61ed1bb8a752b6aa2`.
