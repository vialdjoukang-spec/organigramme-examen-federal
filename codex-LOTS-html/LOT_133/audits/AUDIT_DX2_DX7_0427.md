# Audit indépendant documentaire — DX.2 et DX.7 — reprise 0427

Date : 02.11.2026 UTC. Auditeur : `audit_0427`, distinct des auteurs `dx2_0427` et `dx7_0427`. Aucun texte auteur modifié par cet auditeur ; seul le présent rapport est écrit. Aucun Git, registre global ou sous-agent. Aucun score.

**Verdict : deux brouillons recevables pour une intégration préparatoire, hors validation clinique.** Les corrections ciblées demandées ont été intégrées et relues. Ce verdict porte sur les empreintes ci-dessous, pas sur un HTML futur, ni sur un protocole prescriptif complet ou une validation médicale humaine.

## Versions auditées

| Fichier relatif au LOT133 | SHA-256 exact |
|---|---|
| `_travail/DX2_REDACTION_0427.md` | `4d7c1049d7dd1a82beaff7aae1257afee7da9d514cb24beeb8ec1ec9bd484acd` |
| `_travail/DX7_REDACTION_0427.md` | `94018d1f5e241957c53996203ae866622768233c0557b1052758fcba8f8256e1` |
| `evidence/DX2_0427.json` | `e68342b26a9461db78e69de01afd2289685bf1c05ec5db25e40ffe941ba8b6d5` |
| `evidence/DX7_0427.json` | `33d6cdd2d69ab26ce3dcfc0a2b733247663f72836cb4eeec947ae922d082dcd5` |
| `LISTE_DX_CANONIQUE.md` | `4902f35db88823c5307089e7b955ec7fdb2ab8e0917d81e3c0ca1369f5d3c7eb` |

Le contrôle `python3 -B codex-LOTS-html/LOT_133/_travail/controler_brouillons.py <DX2.md> <DX7.md>` a été exécuté avant puis après corrections : chaque fichier possède les parties 1–14 et questions 1–14, sans manque ni doublon. Tailles finales : DX2 26 777 octets ; DX7 20 564 octets. Ce contrôle mécanique ne valide pas le fond, les sources ni le rendu.

## Méthode et lectures effectives

Instructions locales, `docs/ARSENAL.md`, `harness/GUIDE.md`, liste canonique et `audits/AUDIT_DOCUMENTAIRE_0240.md` lus. Les preuves Phase A sont une préparation de périmètre ; leur ancien verdict n’est pas automatiquement transféré aux nouveaux chapitres. Les deux Markdown et leurs preuves ont été lus, avec examen renforcé des parties 2,3,4,8,9,11,12. Les SHA de tous les caches déclarés dans les deux preuves concordent avec les fichiers présents ; cela atteste l’identité des données, pas leur vérité scientifique.

Contrelecture directe de caches acquis par les auteurs, sans nouvelle acquisition réseau par cet auditeur :

- Phase A : CeMIR sepsis, `recherche_a/web_lecture_3.json`, lignes105–260 ; HUG IC, `recherche_b/tvp_cancer_ic.json`, lignes39–102 ; HUG examens, `examens_ic.json`, lignes44–46,124–126,140–142. Ils confirment les limites de l’orientation adulte initiale.
- DX2 : OFSP S2, contacts/portage, classification, déclaration, isolement et prophylaxie ; Pilly S5, sémiologie et démarche adulte ; SRLF S6, physiopathologie, présentation, microbiologie, prise en charge et pronostic. HAS S4 : passages ambulatoires/biomarqueurs, section adulte3.1.1 (notamment recommandation23), suivi/consultation avant3mois et annexe adulte déconseillant le score unique comme seul dépistage. Les passages HAS naguère absents de Phase A sont désormais présents et effectivement relus. S1 est identifié comme information publique ; sa présence n’est pas utilisée pour justifier un protocole de réanimation.
- DX7 : HUG S3, pages4–13 ; brochure S4, deux pages ; ACVC/ESC S6, lignes243–280 et412–438 ; ESC2023 S7, tableau3 et passages sur SGLT2, stabilisation, acidocétose et suivi précoce. Les extraits indexés S5 sur bilan aigu, oxygène et monitorage ont été personnellement lus dans `escsearch.json` ; ce ne sont pas une ouverture intégrale de la recommandation.

Les géographies sont conservées : OFSP/HUG Suisse, CeMIR/HAS/Pilly/SRLF France, ESC organisme européen avec auteurs internationaux ; PMC est un hébergeur américain, pas la nationalité du statement. Les références seulement présentes dans les bibliographies ne deviennent pas des sources personnellement consultées.

## Fond ciblé : DX.2

| Parties | Constat |
|---|---|
| 2–3 | Sépare maladie invasive à méningocoque, sepsis avec purpura et purpura fulminans. Fréquence OFSP contextuelle, sans classement suisse fictif. Mécanismes endothéliaux et absence possible de CIVD concordent avec SRLF ; aucune extrapolation de l’algorithme HUG pédiatrique. |
| 4 | Urgence sur suspicion, prise en charge et transfert sans attendre hypotension, score ou prélèvement. Précautions respiratoires et transfert suisse distingués des procédures françaises. |
| 8–9 | Diagnostic clinique initial distingué de la documentation microbiologique. Culture négative non excluante ; PCR/biopsie adaptées au laboratoire ; portage pharyngé non assimilé à maladie invasive. PL discutée selon stabilité/hémostase, jamais préalable obligatoire. qSOFA non exclusif et biomarqueurs ambulatoires distingués de l’usage hospitalier du lactate. |
| 11 | Antibiothérapie et soutien en parallèle ; remplissage individualisé étayé par HAS adulte2025. Pas de dose, volume standard, durée arbitraire, corticothérapie systématique ni régime français ARS importé. Réserve AIPS explicite. |
| 12 | Contacts étroits distingués de proximité ; dates OFSP2022 reconnues anciennes. Ajout demandé sur l’éradication du portage du cas index avant sortie intégré et concordant avec S2. Suivi post-sepsis, séquelles et réadaptation explicités. |

Correction demandée puis résolue : ajouter en P12 la vérification que le traitement du cas index éradique aussi le portage, avec prophylaxie complémentaire si nécessaire, décision infectiologique/AIPS. La formulation finale n’impose pas une culture pharyngée de contrôle systématique et n’ajoute aucune dose.

## Fond ciblé : DX.7

| Parties | Constat |
|---|---|
| 2–3 | Phénotypes de FEVG cohérents HUG/ESC ; HFpEF non déduite d’une FEVG préservée seule. NYHA distincte du phénotype, causes et mécanismes contextualisés. |
| 4 | Détresse/hypoperfusion identifiées ; pression conservée non rassurante à elle seule. Stabilisation urgente sans attendre peptides. Monitorage attribué honnêtement à un extrait indexé. |
| 8 | BNP35/NT-proBNP125 ng/L explicitement réservés au contexte non aigu ; conversion ng/L=pg/mL correcte. Erreur d’unités du schéma HUG écartée au profit du texte p8. Âge, rein, FA et obésité modulent l’interprétation. Bilan aigu dépend partiellement d’extraits indexés, ce qui reste signalé. |
| 9 | ETT centrale ; structure, fonctions et valves au-delà de la seule FEVG. Examens spécialisés contextualisés, pas liste obligatoire universelle. |
| 11 | Congestion et traitement de fond distingués ; quatre classes HFrEF, surveillance rénale/électrolytique et non-association IEC/ARNI décrites sans dose. Bénéfice SGLT2 HFmrEF/HFpEF non converti abusivement en réduction certaine de chaque composante de mortalité. Ajout acidocétose/diabète1 conforme S7L954. |
| 12 | Suivi clinique/biologique et alertes cohérents ; gain pondéral >2kg/3jours attribué à la brochure, dyspnée pouvant alerter sans gain de poids. Pas de restriction hydrique ni adaptation autonome universelles. |

Corrections demandées puis résolues : P11, ajouter le risque d’acidocétose sous SGLT2 (apports réduits/insulinothérapie modifiée) et la non-indication dans le diabète de type1, avec conduite détaillée AIPS réservée. Pour les affirmations dépendant de S5, demander un passage ouvert ou rendre la limite visible : la version finale retient explicitement la seconde option à chaque citation concernée. Cette transparence ne transforme pas des extraits indexés en recommandation intégralement lue.

## Réserves qui persistent

1. Les deux cours restent préparatoires et non prescriptifs : aucune notice AIPS exacte lue, aucune posologie validée. Les seuils diagnostiques, de FEVG et d’alerte pondérale ne sont pas des doses médicamenteuses.
2. DX2 : modalités cantonales, indications vaccinales et protocole de prophylaxie actuels à réconcilier avec les autorités suisses ; OFSP2022 ne certifie pas leur état2026. Une source ancienne correctement datée demeure une limite réelle.
3. DX7 : S5 est partiel ; le document ESC2026 repéré n’a pas été ouvert. Ne pas présenter le traitement comme vérifié sur une recommandation ESC2026 ni comme protocole aigu exhaustif. La mention d’une référence2026 repérée n’en valide ni la portée complète ni le contenu.
4. La conversion HTML devra préserver les réserves, citations, branches aiguë/chronique, population adulte et absence de doses. Rendu, navigation, quiz interactifs, iconographie et correspondance finale HTML ne sont pas contrôlés par ce présent verdict sur Markdown.

Aucune correction bloquante supplémentaire identifiée pour l’intégration **préparatoire aux SHA exacts précités**. Une modification substantielle ou l’introduction d’une dose exige une nouvelle contrelecture ciblée. Aucune validation médicale humaine ou publication n’est attestée ici.


## Complément — concordance HTML ciblée après intégration

À la demande du coordinateur, extraction avec `harness/cache_controles.py extraire` de DX2 parties11,12 et DX7 partie11, incluant leurs fenêtres liées. Lecture effective des trois corps extraits, sans lecture intégrale des HTML. Les contrôles statiques19/19 sont déclarés par le coordinateur ; ils ne sont pas revendiqués comme exécutés par cet auditeur.

| HTML contrôlé | Taille | SHA-256 exact final |
|---|---:|---|
| `LOT_133_Phase_B_V0_DX.2.html` | 98 758 octets | `2d8786b50e94b97db99b6fa2f62214b95bc9e72a10624b4f82697385bd63b798` |
| `LOT_133_Phase_B_V0_DX.7.html` | 94 478 octets | `25000d74dde9338305030ee50338b54298027fc28dd5ac309cde5f559233f9fb` |

DX2P11 conserve traitement immédiat, soutien parallèle, individualisation du remplissage, décisions spécialisées et réserve AIPS. DX2P12 conserve le complément demandé sur l’éradication du portage du cas index avant sortie, les critères de contacts, les réserves OFSP2022 et le suivi contextualisé. Aucune divergence clinique relevée avec les Markdown audités sur ces parties.

DX7P11 conserve la séparation aigu/chronique, les quatre classes de fond, les précautions IEC/ARNI, le complément acidocétose/diabète1, les limites d’interprétation des bénéfices SGLT2 et les réserves AIPS/ESC2026.

Deux défauts de conversion documentaire ont été signalés au coordinateur puis corrigés par lui : références après point-virgule initialement non liées (notamment S6), et qualification « extrait indexé » de S5 perdue dans la citation. La version finale lie les références sans déplacer les identifiants ni leurs qualifications : `[S5 : extrait indexé sur l’oxygénothérapie ; S6 : passages ouverts sur congestion et choc]`. La notice S5 contient aussi la portée réellement lue et l’échec d’accès intégral. Vérification DOM des liens puis réextraction finale concordante.

**Verdict complémentaire : concordance documentaire et clinique ciblée recevable aux SHA HTML ci-dessus, toujours préparatoire et hors validation clinique.** Aucun test d’interaction navigateur, aucune inspection visuelle et aucun contrôle intégral des autres parties n’est ajouté par ce complément. Les réserves du rapport principal restent applicables.
