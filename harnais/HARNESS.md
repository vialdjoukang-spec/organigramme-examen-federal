# HARNESS · version du 27.10.2026

Circuit unique de production des cours médicaux. Principe de Vial : **le texte est écrit par les agents, tout le reste est fait par des scripts gratuits**. Aucun audit externe ; un seul circuit de vérité.

Ordre de décision : qualité → exhaustivité du fond → économie → esthétique. L'économie ne coupe jamais le fond.

## 1. Le circuit, de gauche à droite

```
Mémoire → RÉDACTION → PORTE → AUDIT par territoire → CONTRACTEUR → COMMIT → PR → CI → FUSION
```

| Secteur | Qui | Ce qui s'y passe | Sortie |
|---|---|---|---|
| Mémoire | scripts `harnais/agents/<id>.py memoire` | l'agent reçoit sa part de la GRILLE À 14 POINTS, les règles du cours, ses leçons (5 au plus), la preuve du bracelet | un agent qui n'a rien à relire |
| Rédaction | A (Phase A), R1 à R8 (Phase B) : **Sonnet 5.5, effort moyen** | A écrit la Phase A ; chaque R écrit **2 DD au plus**. Boucle : écrire → `controle` → corriger → `fin` | fichier marqué « prêt » |
| Porte | scripts (`checkpoint.py`, `fin`) | véracité V2 (doses AIPS, PMID, chiffres retrouvés), langue, forme, grille | refus avec le détail, ou passage |
| Audit | B1 à B5 : **Opus 5.5, effort moyen** | audit du fond (V1) et de la conformité à la grille et au Prompt (V2), correction directe, strictement dans son territoire | V1 et V2 ≥ 90 %, zéro critique |
| Contracteur | KB1 à KB5 (clones, un par auditeur) | dernier secteur obligatoire : contraction du texte, conservation stricte des notions | visa lié à l'empreinte du fichier |
| Dépôt | chef de production, sans agent | commit sur `prod/lot-NNN-final`, manifeste, SHA-256, PR, CI, fusion | LOT fusionné |

Territoires d'audit : **B1** (orange pâle) audite d'abord la Phase A, puis DX.1–2 ; **B2 à B5** auditent 1 à 4 DD chacun. La répartition est calculée par `harnais/grille14/roster.py <LOT> <N>` (N de 10 à 16).

## 2. Définitions de Vial

- **V1** = exactitude du fond (doses AIPS, chiffres retrouvés dans leur source, références existantes, rien d'inventé).
- **V2** = conformité au Prompt ULTIME et à la GRILLE À 14 POINTS (`harnais/GRILLE_14_POINTS.md`, chaque question notée 2/1/0).
- Un fichier est validé à V1 ≥ 90 %, V2 ≥ 90 %, zéro critique.
- **Les phrases restent verbales ; les phrases nominales sont interdites.**
- Principe de chaque point : **CONCIS + DENSE + EXHAUSTIF**.
- Le texte est le cours, pour des médecins résidents : aucune mention de la conception (LOT, Phase, fichier, cycle, audit, « autre IA »), aucune date de rédaction, aucune genèse des sources.

## 3. Les scripts d'agents (lecture seule)

14 scripts « Grille des 14 points » : `A`, `R1`…`R8`, `B1`…`B5`, plus 5 clones du contracteur `KB1`…`KB5`. Moteur : `harnais/grille14/grille_agent.py`.

- Lecture seule (chmod 444), empreintes dans `harnais/agents/SHA256SUMS` ; une altération arrête l'agent (« ALTÉRATION DÉTECTÉE »).
- `memoire` : identité, périmètre, grille, règles, leçons ; écrit la preuve du bracelet dans `PREUVE_EMBOITEMENT.txt`.
- `controle <fichier>` : pose le verrou ; **réparations mécaniques gratuites** (balise `FIN_FICHIER`, lignes de plus de 3 000 caractères, `title=`, renvois `[Sn]` dupliqués) ; écarts à la grille point par point (critique, grave, moyen), avec les phrases à couper en premier.
- `fin <fichier>` : dernier contrôle + checkpoint ; lève le verrou. Rédacteur : sans commit (marqueur « prêt »). Auditeur : exige le visa du contracteur, les scores `--v1 --v2 --crit`, puis commit.
- `attendre <fichier>` (auditeur) : bloque jusqu'à 9 minutes tant que le rédacteur n'a pas fini.
- `lecon "<texte>"` : mémoire permanente de l'agent (5 leçons au plus).
- Garde-fous : refus **hors périmètre**, refus si le verrou est pris par un autre agent.

### Anti ping-pong (gratuit, dans les scripts)

1. Jamais de retour d'un Opus vers un Sonnet : l'auditeur corrige lui-même.
2. **3 essais de `fin` au plus** par agent et par fichier.
3. **Détecteur de stagnation** : mêmes écarts (scores compris) deux fois de suite ⇒ fichier **BLOQUÉ**, l'agent s'arrête.
4. `fin` répond « INCHANGÉ » (sans compter d'essai) si le fichier est identique à celui du dernier refus ; un second essai sans modification bloque le fichier.
5. Un refus du checkpoint affiche « À CORRIGER » : les lignes exactes des rapports (chiffres sans source, ® absents de l'AIPS, phrases sans verbe).
6. Un fichier BLOQUÉ revient au chef de production, qui ne relance pas d'agent en boucle dessus.
7. Panne d'outil (checkpoint qui plante) : incident écrit dans `incidents/`, aucun essai compté, code 6. Arguments faux : message clair, jamais de trace brute.

## 4. Le contracteur de texte · conservateur de notions

```
╔══ RÈGLE ABSOLUE DE VIAL ═════════════════════════════════════════════════════════════════════╗
║ LA CONTRACTION NE DOIT PAS DU TOUT TOUCHER LES NOTIONS, NI COMPROMETTRE LE SENS, NI           ║
║ L'EXPLICATION DE QUOI QUE CE SOIT. On n'a pas besoin de beaucoup de mots pour transmettre      ║
║ des notions expliquées.                                                                        ║
╚════════════════════════════════════════════════════════════════════════════════════════════════╝
```

La règle est une constante (`REGLE_ABSOLUE`) du moteur : imprimée en tête de **chaque** sortie de `contracter`, `verifier` et `etat`, écrite dans le docstring, injectée dans la `memoire` de chaque auditeur B1…B5. Contracter **peut reformuler plus concis** (pas seulement supprimer) ; jamais résumer.

`harnais/contracteur/contracteur.py` (lecture seule) ; clones `harnais/agents/KB1.py` … `KB5.py`, chacun limité au territoire de son auditeur (refus si le verrou est tenu par un autre agent).

- `contracter <fichier>` : inventaire **à l'entrée** (nombres, renvois `[Sn]`, sources de la liste, médicaments et DCI, termes cliquables, abréviations définies, couples comparateur + valeur + unité, tableaux, 14 points, lemmes, phrases avec explications et marqueurs), contraction mécanique sûre (formules creuses en début de phrase, doublons exacts ; jamais « Ainsi », « afin de », « dans la mesure où »), puis **cibles** : redites, phrases longues, phrases nominales, points lourds. Le gain est affiché, jamais exigé.
- `verifier <fichier> [--exceptions "mot,mot"]` (10 au plus) :
  - 100 % : nombres, médicaments (marques et DCI), sources de la liste, abréviations définies, couples comparateur + valeur + unité (aussi **dans leur phrase**) ; tableaux (lignes) et 14 points intacts ;
  - ≥ 95 % : termes cliquables, renvois `[Sn]`, notions (noms) ;
  - **explications** : chaque phrase portant car, parce que, donc, ainsi, provoque, entraîne, explique, permet, mécanisme, afin de, pour que, → est couverte à ≥ 85 % par les lemmes de la meilleure phrase du texte contracté (ou de deux phrases voisines : scinder est permis) ;
  - **autres phrases** : couvertes à ≥ 80 % ; sinon admises seulement si elles sont la redite d'une phrase conservée ;
  - **négations et conditions** (ne… pas, jamais, sans, aucun, contre-indiqué, interdit, éviter, seulement, uniquement, si, sauf) : présentes dans la phrase qui couvre, et jamais diminuées au total ;
  - **excès objectif** seulement : redites quasi identiques ≤ 3, phrases de plus de 30 mots ≤ 6 %, aucune phrase nominale en plus. **Aucun quota de volume** (l'ancien 15 % / 14 000 mots est supprimé ; `CIBLE.json` n'est plus lu pour décider).
  - Visa lié à l'empreinte du fichier : toute modification ultérieure l'annule.
- La contraction mécanique est appliquée aux deux côtés de la comparaison : elle est invisible au verdict.
- La commande `fin` d'un auditeur **refuse sans visa valide** (« aucun visa » ou « modifié après le visa »).

## 5. Forme des cours (convertisseur `harnais/forme_interactive.py`)

Le fichier brut reste lisible par les contrôles ; le dépôt reçoit la version convertie. Un fichier déjà converti est ré-habillé (idempotent).

- Point 1 : classification du général au particulier, **avec la classification d'origine** entre parenthèses (CIM-11, DSM-5, ATC…), en cartes descendantes ; 140 mots au plus de texte.
- **Abréviations : aucune nulle part sans être survolable avec sa définition.** La liste « Abréviations : A = …; B = … » du préambule est détruite à l'affichage (elle reste dans le brut). **Chaque occurrence** de chaque sigle (≥ 2 majuscules ou chiffres consécutifs : TSH, HbA1c, CIM-11, qSOFA), hors titres et bibliographie, y compris dans les fenêtres, devient `<abbr class="ab" data-k="TSH">` ; la définition est écrite **une seule fois** dans `<style id="sigles">` (survol et focus). Définitions : liste du préambule, fenêtres `.tm` dont le terme est un sigle, valeurs par défaut du harnais (DCI, ATC, AIPS, OMS, CIM-10/11, DSM-5, OFSP, OFS, DX).
- **Médicaments : aucun mentionné sans être cliquable avec sa classification.** Chaque fenêtre `.tm med` contient DCI, classe (ATC), groupe avec ses chefs de file, indications et posologies AIPS. **Chaque occurrence** (terme, DCI, marques de la ligne DCI, avec ou sans ®), hors titres et hors fenêtres, devient un lien vers une **bande** unique par médicament (comme les sources).
- **Contrôles d'échec (CRITIQUE, nommés à l'agent)** : sigle sans définition nulle part ; médicament mentionné sans fenêtre (marque ® ou ™, nom d'une colonne Molécule / Médicament / Spécialité d'un tableau, ou suffixe -pril, -sartan, -azole, -mab, -tinib, -statine, -olol, -oxacine, -cilline, -dipine, -parine, -mycine, -cycline, -vir…) ; fenêtre incomplète (élément manquant nommé). Faux positifs écartés : noms propres composés (Child-Pugh), mots capitalisés (PubMed), codes ATC/CIM, lettre + chiffres (T4, B12), chiffres romains, formules chimiques, classes au pluriel, cholestérol, somatostatine, cocaïne… (listes `EXC_SIGLES`, `SOFT`, `EXC_MEDS`).
- L'habillage automatique porte `data-auto` ou `<abbr>` : il ne compte ni comme terme cliquable de l'agent, ni comme fenêtre au point 13 ; les comptes de mots et de phrases se font sans lui.
- Sources : exposants discrets ; clic = source sur une petite bande bleu ciel ; liste unique en dernière page sous « Sources bibliographiques ».
- Aucun terme cliquable écrit par l'agent dans un titre. Tableaux colorés. Police **Atkinson Hyperlegible** embarquée.
- Aucune mention de conception, phrases de 8 à 20 mots (moyenne ≤ 20, pas plus de 6 % au-dessus de 30).

## 6. Taille

`harnais/BANDE.json` : **80–200 Ko**, **indicative : la taille ne bloque aucun fichier** (Vial, 27.10.2026). Grille : écart **MOYEN** (jamais CRITIQUE) ; `checkpoint.py` : « AVERTISSEMENT (non bloquant) » ; `controle_lot.py verifier` : avertissement de lot. L'habillage des sigles et des médicaments ajoute environ 25 à 50 Ko par fichier.

## 7. Outils du harnais d'origine, tous dans le circuit

| Outil | Où il est utilisé |
|---|---|
| Bracelet (`bracelet_suggest.py`) | à chaque `memoire`, avec preuve réelle dans `PREUVE_EMBOITEMENT.txt` |
| Lecture ciblée (`controle_lot.py extraire`, `aips_texte.py`, `pubmed.py`) | rédacteurs et auditeurs |
| Chonkie (`grille14/passage.py`) | passage utile d'une longue source |
| requests-cache + PyBreaker | `pubmed.py` (cache, disjoncteur sur l'erreur 429) |
| Verrous, tableau de tâches, territoires | non-collision |
| Arsenal (`tools/arsenal/lot.py`, `pr.sh`, `ci_attente.sh`, `audit_diff.py`) | dépôt et CI, côté chef de production |
| Veille, sentinelle, tableau de bord | observation (`harnais/dispositif/`) |
| Contrôles gratuits (`checkpoint.py` : médical, langue, forme) | porte |

Écartés (coût supérieur au gain) : LLMLingua, GPTCache, Mem0, Graphiti.

## 8. Santé et tests

- `python3 harnais/grille14/SANTE.py` : verrous orphelins, fichiers BLOQUÉS, fichiers prêts non audités, essais, commits en avance, empreintes.
- `python3 harnais/grille14/autotest.py` : 108 tests de bout en bout en moins d'une minute (mode `G14_TEST=1`, bac à sable, jamais de commit réel) ; il prouve aussi que les 16 fichiers réels de LOT_001 ne subissent aucune régression imprévue (lecture seule) et écrit les écarts nouveaux dans `.cache/test_g14/ecarts_LOT_001.json`.
- LOT par défaut des scripts : `harnais/grille14/LOT_ACTIF` (une ligne « 001 »), sinon la variable `G14_LOT`, sinon 001 ; `--lot NNN` prime.
- Notes d'ingénierie : `harnais/grille14/NOTES_INGENIERIE.md`.

## 9. Conduite d'un LOT (chef de production)

1. `python3 harnais/file_g.py prep NNN` ; `python3 harnais/grille14/roster.py NNN N` ; worktree `../wt-NNN` sur `prod/lot-NNN-final`.
2. Phase A (A puis B1), rédacteurs R1…R8 en parallèle, auditeurs B1…B5 (qui attendent), contracteur en dernier.
3. `controle_lot.py verifier` sur le dépôt : CONFORME.
4. PR, CI verte, **commit de fusion**, puis LOT suivant. Un seul LOT actif à la fois.
5. Reprise après redémarrage du conteneur : les fichiers sont conservés ; nettoyer les verrous (`verrou.py nettoyer-lot`), relancer les agents sur l'état réel des fichiers.
6. Défaut persistant des scripts ou échec élevé : recours autorisé à **un ingénieur Opus 5.5 effort moyen**, de façon économe (feu vert de Vial, 27.10.2026).

## 10. Coût (mesures du 27.10 pour LOT_001)

Les rédacteurs sont le gros poste : environ 400 000 à 570 000 jetons par paire de rédacteurs. Les relances après blocage coûtent de 20 000 à 60 000 jetons. Les scripts ne coûtent rien.

## 11. Décisions en attente de Vial

- Calibrage des seuils de conservation (85 % explications, 80 % autres phrases, redite à 80 %) : à confirmer à l'usage.
- LOT_001 : les sigles non définis et les médicaments sans fenêtre (mesurés dans `NOTES_INGENIERIE.md`) refusent désormais le checkpoint ; reprise à décider.
- Point 10 de la grille (arbre décisionnel) : texte de Vial à compléter.
- Bande 80–200 Ko indicative : appliquée (non bloquante).
