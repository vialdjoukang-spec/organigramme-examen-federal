# Audit agressif V0 — LOT_012 — G12 Œdème diffus ou localisé

Date : 2026-10-25, 21:07 Europe/Zurich.
Auditeur : session distincte des rédacteurs de l’Appel A, de l’Appel B et de l’audit correcteur PR #444.
Périmètre : rapport seul. Aucune monographie réécrite. Aucune fusion. Aucun message à l’owner.
Brief appliqué : PROMPT ULTIME V0 (25.10.2026), grille §12.2. Les pourcentages 77 / 94 / 92 de la PR #444 sont une jauge structurelle V7/V8 (50 questions, maximum 100). Ils ne sont pas repris.

## Décision

**Prêt-dépôt : NON.**

Question finale, pour la monographie SSP et pour chacun des dix DX : **non**. Un candidat ne peut pas, sur ces fichiers, viser 90 à 100 % des points de l’examen fédéral ni conduire le patient avec une dose suisse lue.

Seuil V0 : ≥ 90 % de la grille 2/1/0, zéro critique, question finale « oui », chaque entité entre 150 et 200 Ko après densification puis rabotage. Aucune entité ne passe.

## Trois critiques

1. **Omission de volume.** Les onze entités sont sous 150 Ko. Le chapitre 1 du SSP pèse 18 852 octets. Les DX pèsent de 39,0 Ko (DX.9) à 66,7 Ko (DX.1). Aucun premier jet au-delà de 200 Ko n’est documenté. La phrase « Si le geste est un médicament, la dose reste À vérifier (AIPS). » est répétée 14 fois dans chaque DX : ce n’est pas de la densité clinique.

2. **AIPS Medina non lu.** Le lot écrit « À vérifier (AIPS) » 447 fois. Le corpus `AipsDownload_20261008.zip` (dépôt Medina, SHA-256 `9fd0c713e28cd0a9ff402d2f621b032e9086f2df150c63291ab721e6a06aaced`, ouvert le 25.10.2026) contient les informations professionnelles. Les SmPC français ont été ouverts. Le lot n’en cite ni la dose ni le numéro d’autorisation. Extraits lus ce jour, non recopiés dans le HTML :
   - Lasix®, autorisation 30630 : adulte, dose initiale 20 à 40 mg i.v. ou i.m. ; œdème pulmonaire aigu, 40 mg i.v., puis 20 à 40 mg si besoin après 20 minutes.
   - Aldactone®, autorisation 27257 : œdèmes de l’insuffisance cardiaque, 100 mg/jour, jusqu’à 200 mg/jour ; l’indication « cirrhose avec ascite » et le syndrome néphrotique y figurent.
   - Torasemid-Mepha, autorisation 58181 : œdème cardiaque, début 5 mg le matin, jusqu’à 20 mg ; cirrhose avec ascite, début 10 mg le matin.
   - Xarelto®, autorisation 58728, mise à jour mai 2025 : TVP et EP, 15 mg deux fois par jour du jour 1 au jour 21, puis 20 mg une fois par jour.
   - Amoxi-Mepha, autorisation 44911 : adulte > 40 kg, infections légères à moyennes, 1 500 à 3 000 mg/jour en 3 à 4 prises ; streptocoque β-hémolytique, au moins dix jours.
   - Euthyrox®, autorisation 54949 : hypothyroïdie, dose initiale 25 à 50 µg/jour, entretien 100 à 200 µg/jour.
   - Epipen®, autorisation 53836 : 0,3 mg d’adrénaline ; Epipen Junior 0,15 mg. L’angio-œdème bradykinique sous IEC n’est pas cette indication : le lot a raison de le distinguer, et tort de laisser la dose d’anaphylaxie en « À vérifier » alors que la fiche est dans le zip.
   - Norvasc®, autorisation 50044 : 5 mg puis 10 mg une fois par jour. C’est une cause d’œdème, pas un traitement de l’œdème.

3. **Grille V0 sous 90 % et critère faux dans l’arbre du DX.10.** Le meilleur score est 47,8 % (DX.1). Le point 8 du DX.10 retient le KDIGO 2021 : protéinurie supérieure à 3,5 g/24 h et albuminémie inférieure à 30 g/L. L’arbre du même fichier dit encore : « Si la zone des 3 à 3,5 g/24 h […] est atteinte […] nommer le syndrome ». Les points clés oraux redisent « environ 3 à 3,5 g par 24 heures ». Un candidat qui apprend les points clés apprend le seuil que le point 8 vient d’écarter. La Phase A n’a aucun rang d’exclusion E1, E2… ni de badge 🚩. Les rangs 3 à 10 sont des rangs de travail, marqués À vérifier.

## Source notée

Meilleur HTML disponible : branche `cursor/lot-012-audit-correcteur-2d46`, PR #444 ouverte, non fusionnée. Aucun HTML nommé V8 ou V0 n’existe. Les noms restent `Appel_A_V7` et `Appel_B_V7`.

`main` est plus court (Appel A 57 869 octets contre 63 447). Il n’est pas noté.

Dossier Drive `1WYj7HAc2zHezy8CurwGshSpNxOhNeG3B`, listé le 25.10.2026 : les cinq HTML ont les mêmes tailles que la PR #444 (63 447, 143 344, 157 110, 99 688, 138 114). Le SHA-256 des octets Drive n’a pas été recalculé. Le `STATUT.md` de la PR cite d’autres identifiants Drive : ces identifiants ne sont plus ceux du dossier listé. Le dépôt Drive a donc déjà reçu cette version, alors que le statut écrit refuse le feu vert. Ce rapport ne dépose rien et ne remplace rien.

HTML unique consolidé SSP + 10 DX : **absent**. Le critère « HTML unique interdit » est respecté. Le lot reste incomplet au sens V0 : pas de fichiers `Phase_A_V0` / `Phase_B_V0`, pas de `LISTE_DX_CANONIQUE.md`, pas de bande 150–200 Ko.

| Fichier PR #444 | Octets | SHA-256 |
|---|---:|---|
| `LOT_012_Appel_A_V7_Plan_et_Liste.html` | 63 447 | `d4da62085b89869dba0eb9322fe2daae95b3468f07597320108da715b6075d02` |
| `LOT_012_Appel_B_V7_Partie_1_DX.1_a_DX.2.html` | 143 344 | `0ba7763264aff7cd5641c8c3ebffb1b76f3d6143f903f6069a7db2df8d589c2c` |
| `LOT_012_Appel_B_V7_Partie_2_DX.3_a_DX.5.html` | 157 110 | `39d6c63207f61b9be602643912a0e806b3acf8b60484224020fd373766199eed` |
| `LOT_012_Appel_B_V7_Partie_3_DX.6_a_DX.7.html` | 99 688 | `82932d556938d70c459bff863c591fb2a14e8603d7cd80a7a4c0572cad12892f` |
| `LOT_012_Appel_B_V7_Partie_4_DX.8_a_DX.10.html` | 138 114 | `15be1ba79fa661de76c25f2e51b72ff5485f433a4b485ced33069b541f27d4e0` |

## Tailles par entité

L’entité notée pour les DX est le bloc `<h2>` de l’Appel B, pas l’ancre de 2 à 8 Ko de l’Appel A. L’entité SSP est le chapitre 1 seul.

| Entité | Octets | Ko | Bande 150–200 Ko |
|---|---:|---:|---|
| A — SSP, chapitre 1 | 18 852 | 18,4 | non — omission |
| DX.1 Insuffisance veineuse chronique | 68 334 | 66,7 | non — omission |
| DX.2 Insuffisance cardiaque décompensée / anasarque | 56 886 | 55,6 | non — omission |
| DX.3 Œdème médicamenteux | 50 267 | 49,1 | non — omission |
| DX.4 Lymphœdème | 46 562 | 45,5 | non — omission |
| DX.5 TVP / embolie pulmonaire | 45 467 | 44,4 | non — omission |
| DX.6 Érysipèle (dermohypodermite) | 42 515 | 41,5 | non — omission |
| DX.7 Insuffisance rénale avec surcharge | 42 393 | 41,4 | non — omission |
| DX.8 Cirrhose / hypertension portale | 41 124 | 40,2 | non — omission |
| DX.9 Myxœdème (hypothyroïdie) | 39 961 | 39,0 | non — omission |
| DX.10 Syndrome néphrotique | 42 205 | 41,2 | non — omission |

## Scores V0 — grille 2/1/0

46 questions, maximum 92. Score = somme / 92. Une question à 2 est pleinement tenue, à 1 partielle, à 0 absente ou fausse. Sans objet : aucun. Cible ≥ 95 %. Plancher de validation ≥ 90 % (soit au moins 83/92) et zéro critique. Tous les totaux sont sous ce plancher.

| Entité | /92 | % | Finale | Critique de taille | Q11.5 AIPS |
|---|---:|---:|---|---|---|
| A — SSP | 28 | 30,4 | non | oui | 0 |
| DX.1 | 44 | 47,8 | non | oui | 0 |
| DX.2 | 37 | 40,2 | non | oui | 0 |
| DX.3 | 31 | 33,7 | non | oui | 0 |
| DX.4 | 32 | 34,8 | non | oui | 0 |
| DX.5 | 33 | 35,9 | non | oui | 0 |
| DX.6 | 31 | 33,7 | non | oui | 0 |
| DX.7 | 33 | 35,9 | non | oui | 0 |
| DX.8 | 31 | 33,7 | non | oui | 0 |
| DX.9 | 32 | 34,8 | non | oui | 0 |
| DX.10 | 33 | 35,9 | non | oui | 0 |

Sous-totaux par point (obtenu / maximum du point). Maximums : 1=6, 2=8, 3=10, 4=4, 5=4, 6=4, 7=10, 8=4, 9=12, 10=2, 11=22, 12=2, 13=2, 14=2.

| Entité | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 3 | 2 | 4 | 2 | 2 | 1 | 0 | 3 | 3 | 1 | 4 | 0 | 1 | 2 |
| DX.1 | 5 | 5 | 5 | 3 | 3 | 3 | 1 | 4 | 5 | 1 | 5 | 1 | 1 | 2 |
| DX.2 | 4 | 5 | 4 | 3 | 2 | 3 | 0 | 2 | 4 | 1 | 5 | 1 | 1 | 2 |
| DX.3 | 2 | 3 | 4 | 3 | 2 | 2 | 0 | 2 | 4 | 1 | 5 | 1 | 1 | 1 |
| DX.4 | 3 | 3 | 4 | 3 | 2 | 2 | 0 | 2 | 4 | 1 | 5 | 1 | 1 | 1 |
| DX.5 | 3 | 3 | 4 | 3 | 2 | 2 | 0 | 2 | 4 | 1 | 5 | 1 | 1 | 2 |
| DX.6 | 2 | 3 | 4 | 3 | 2 | 2 | 0 | 2 | 4 | 1 | 5 | 1 | 1 | 1 |
| DX.7 | 3 | 3 | 4 | 3 | 2 | 2 | 0 | 2 | 5 | 1 | 5 | 1 | 1 | 1 |
| DX.8 | 2 | 3 | 4 | 3 | 2 | 2 | 0 | 2 | 4 | 1 | 5 | 1 | 1 | 1 |
| DX.9 | 3 | 3 | 4 | 3 | 2 | 2 | 0 | 2 | 4 | 1 | 5 | 1 | 1 | 1 |
| DX.10 | 4 | 3 | 4 | 3 | 2 | 2 | 0 | 4 | 4 | 0 | 5 | 1 | 0 | 1 |

Lecture de la grille. Le point 7 est à 0 ou 1 partout : aucun syndrome numéroté 7.1, 7.2, aucun éclatement signe fonctionnel / signe physique, geste et mécanisme. Le point 11 est à 5/22 partout dans les DX : les lettres A à D existent, les doses, la chronologie minute par minute, les paliers de DFGe, les critères de sortie un par un et le but chiffré n’y sont pas. Q11.5 est à 0 sur les onze entités. Le point 10 du DX.10 est à 0 parce que l’embranchement enseigne le mauvais seuil.

Ce qui tient, et qui ne rachète pas le lot. DX.1 ancre la définition sur l’ESVS 2022 lue le 25.10.2026 (C3–C6, reflux > 0,5 s, compression 20–40 mmHg citée comme recommandation européenne, pas comme classe suisse de bas). DX.2 reprend les seuils NT-proBNP de l’ESC 2026 (ambulatoire 125 / 250 / 500 ng/L selon l’âge ; exclusion en décompensation < 300 ng/L). DX.10, au point 8 seulement, refuse 300 mg/g et pose > 3,5 g/24 h. Les tableaux sont enveloppés. Aucun attribut `title=`. Balise FIN_FICHIER présente. Aucune ligne > 3 000 caractères repérée. La lisibilité à 390 px n’a pas été essayée dans un navigateur.

## Cohérence Phase A ↔ Phase B

Les dix diagnostics sont les mêmes, dans le même ordre : veineux, cardiaque, médicamenteux, lymphœdème, TVP/EP, érysipèle, surcharge rénale, cirrhose, myxœdème, néphrotique. Écart de libellé : l’Appel B ajoute « (dermohypodermite) » au DX.6. Sous la lettre V0, une divergence de nom bloque le dépôt. Les ancres de l’Appel A ne sont pas des monographies en 14 points : elles renvoient à l’Appel B. C’est cohérent comme architecture V7, et insuffisant comme LOT COMPLET V0.

Gravité. L’algorithme de l’Appel A commence par les menaces (voies aériennes, détresse, fasciite, embolie). Les rangs d’exclusion E1… et le badge 🚩 sont absents. TVP/EP reste au rang 5 de fréquence, ce qui est acceptable seulement s’il est marqué et placé en tête d’algorithme. Le marquage manque. L’angio-œdème laryngé, la dénutrition et le syndrome cave supérieur sont hors du top 10, nommés comme gravités : ils ne portent pas non plus de rang E.

## Autres écarts, classés

**Grave.** Le seul parcours minutés de la TVP est NICE NG158 (4 h, 24 h, contrôle 6–8 jours), lecture du 19.10.2026, non rouverte le 25.10.2026 (accès auparavant refusé). Le texte dit que ce n’est pas une règle suisse, puis c’est quand même l’arbre chiffré. Resuscitation Council UK 2021 est cité pour l’adrénaline à la place de l’AIPS Epipen. Le chapitre 1 de l’Appel A garde des débris de gabarit (`§coeur-vaisseaux`, `¶0`, `¶1`) dans l’examen physique, et des puces nominales. Les points 11.A–D, 9.a–d et 7.x ne sont pas les sous-titres exigés : l’Appel B utilise « A. Menace vitale » jusqu’à « D. Traitement symptomatique », ce qui couvre le plan mais pas les situations spéciales chiffrées. La sortie est une phrase unique : le motif d’hospitalisation est stabilisé et un suivi est nommé. Les critères un par un, LAMal, LAA, LAI et aptitude à la conduite sont déclarés non trouvés. L’aveu est honnête. La question Q11.7 et Q11.10 restent à 0.

**Moyen.** Définitions des DX.3, DX.4, DX.6, DX.8 et DX.9 appuyées sur « le cours » ou sur la Revue du Praticien du 15.03.2024, pas sur une société savante nommée et datée. Aucune distribution suisse de la plainte. International Society of Lymphology 2023 citée pour les diurétiques du lymphœdème, avec la réserve que ce n’est pas une règle suisse. Aucun numéro Swissmedic dans les HTML. Aucun « À vérifier (AIPS) » n’était légitime pour les molécules présentes dans le zip.

**Léger.** Espaces collés hérités dans l’Appel A (`dihydropyridines5–15 %`). Formulations orales qui répètent le point et y recollent la phrase AIPS vide.

## Harnais

`harnais/ARSENAL.md` et `harnais/HARNAIS_OBLIGATOIRE.md` lus. `app_v2.html` non lu. `tools/arsenal/pr.sh` non lancé. Bracelet exécuté, sortie réelle :

```text
python3 harnais/bracelet/bracelet_suggest.py "audit agressif LOT_012 G12 oedeme diffus V0 rapport scores 14 points AIPS Medina"
1. Chonkie score=0.2
2. Crawl4AI score=0.2
3. Firecrawl score=0.2

python3 harnais/bracelet/bracelet_suggest.py "audit agressif LOT_012 monographies HTML longues G12 oedeme decouper documents compresser cache reponses grille V0 AIPS"
1. LLMLingua score=1.6
2. Chonkie score=1.3
3. RTK score=1.3
```

Le trio attendu Chonkie · LLMLingua · GPTCache n’est pas sorti. Écart : le catalogue suit les mots de la requête ; GPTCache n’est pas apparu. Découpage fait par balises `h2`/`h3`, sans installer Chonkie. Pas de compression du texte clinique. Pas de cache de scores : les 77 / 94 / 92 ne sont pas réutilisés. Drive Finaux non modifié.

## Checklist §20 — dépôt

Non cochée. Sources partiellement lues et datées, doses AIPS non ouvertes par les rédacteurs, 14 numéros présents dans l’Appel B mais point 7 non conforme, question finale « non », bande 150–200 Ko non atteinte, audit médical et linguistique antérieurs invalides comme score V0, lot non validé. Les lacunes de dose ne vont pas dans un « À vérifier » : les fiches sont dans le zip.

Contenu établi à partir des HTML de la PR #444 et des SmPC Medina ouverts le 25.10.2026. Ce rapport n’est pas une validation clinique.
