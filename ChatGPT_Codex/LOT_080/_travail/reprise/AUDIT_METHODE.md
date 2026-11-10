# LOT_080 — réexamen de la méthode P1

Date : 10 novembre 2026. Auditeur : `/root/audit_p1_lot080`.

Cette note concerne la méthode et le dossier précédent. Elle ne valide aucune nouvelle liste et ne constitue pas l'audit des preuves en cours de collecte dans `reprise/`. Je reste indépendant des auteurs des fragments.

## Ce que demande la référence

Référence normative unique : `PROMPT_Casern/PROMPT_LOTS_Lo_9.11.26.claude.md`, version du commit `037545b80fe03166dec9e05f70e24fb9f008821d`. Les passages ci-dessous sont ceux du prompt fournis dans le contexte de cette session ; cette reprise n'a effectué aucune lecture par Git.

- µ1.2 impose des DX qui sont de vrais concurrents cliniques, distincts et sans catégorie fourre-tout. Il demande un ordre de fréquence décroissante en Suisse, ou en Europe à défaut, et un rang sourcé.
- µ1.3 permet un rang accompagné de son argument sourcé lorsque aucun pourcentage n'est affiché. Un pourcentage n'est donc pas nécessaire pour justifier une position.
- A-2 demande pour chaque DX une phrase expliquant pourquoi il entre dans la liste et pourquoi il occupe ce rang, à partir des extraits.
- µ1.6 et M5 prévoient un audit avant le gel des noms et de l'ordre. La gravité et le rang d'exclusion E restent distincts du rang de fréquence.

Le texte n'impose ni une cohorte unique, ni une enquête suisse couvrant simultanément tous les âges, ni un pourcentage pour chacun des dix diagnostics. Il n'impose pas non plus qu'une source énonce littéralement chaque numéro de rang : une synthèse clinique argumentée à partir d'extraits est prévue par le rôle A-2.

## Exigence ajoutée dans mon précédent examen

Mon audit précédent emploie, dans son deuxième motif, la formulation « leur ordre relatif dans une population clinique commune ». Ma première conclusion orale évoquait aussi un ordre global tous âges. Ces formulations ont pu transformer un problème de portée des sources en une condition supplémentaire de cohorte commune ou de classement universel.

Je retire cette condition en tant qu'exigence du prompt. L'absence de cohorte commune tous âges ne suffit pas à refuser P1. La comparabilité reste une question d'interprétation scientifique : elle sert à empêcher une extrapolation trompeuse, sans imposer un dessin d'étude particulier.

Je dois également distinguer absence de justification dans le paquet examiné et impossibilité scientifique de rédiger le LOT. Le premier constat ne démontre pas le second. Le verdict précédent porte sur l'ancien fichier `preparation_sources.json`, dont l'empreinte auditée est `09c7e65dedc6199a5938234f4f69122c3a709acf70957cbc87355e93db845d2e` ; il ne préjuge pas d'un dossier enrichi.

## Comment examiner une proposition stratifiée

Une présentation par croissance, âge adulte et âge avancé peut être exploitable si chaque comparaison précise son champ. Pour chaque diagnostic, l'audit examinera séparément :

1. Son nom exact et sa distinction des neuf autres entités.
2. Le contexte clinique ou la population où il concurrence effectivement les autres diagnostics.
3. L'extrait qui établit son caractère fréquent, moins fréquent ou rare dans ce contexte, et l'argument clinique qui en est tiré pour sa position.
4. Les limites de portée : une proportion parmi les scolioses n'est pas présentée comme une proportion parmi toutes les postures anormales.
5. Les signes discriminants et les rangs E des diagnostics graves retenus.

Des arguments qualitatifs convergents peuvent justifier une position sans pourcentage et sans comparaison directe publiée entre chaque paire voisine. L'audit doit apprécier leur force réelle ; il ne doit pas exiger arbitrairement dix estimations statistiques indépendantes ou une seule étude décisive.

À l'inverse, la juxtaposition de comparaisons conditionnelles ne prouve pas automatiquement un ordre universel. Par exemple, « fréquent pendant la croissance » et « fréquent chez la personne âgée » ne déterminent pas, à eux seuls, lequel est le plus fréquent dans un ensemble non défini de patients. Ce point doit être examiné dans la nouvelle proposition, et non présumé bloquant avant sa lecture.

## Présentation honnête et limites de validation

La Phase A peut exposer un tableau indiquant, pour chaque entité, le contexte où elle est prioritaire, l'argument qualitatif sourcé, le discriminant et le rang d'exclusion. Les comparaisons stratifiées restent alors visibles et ne deviennent pas des pourcentages universels inventés.

Il faut néanmoins expliquer ce que signifie l'ordre canonique DX.1 à DX.10. Si cet ordre est justifié par une synthèse clinique contextualisée, l'audit l'évaluera sur ses arguments, sans réclamer une cohorte commune. Si les numéros servent seulement d'identifiants pédagogiques entre plusieurs strates non comparées, ils ne devront pas être présentés comme dix rangs épidémiologiques universels : µ1.2 demande toujours un ordre de fréquence. Je ne déclarerai pas cette exigence satisfaite par un simple changement d'étiquette.

Une distinction utile est donc possible : cohérence et précision des dix entités d'une part, justification du sens et des positions de leur ordre d'autre part. Un défaut de la seconde ne doit pas effacer le travail établi sur la première. Les paquets, contrats et preuves peuvent continuer à être préparés ; leur existence ne doit pas être annoncée comme un gel P1 ou comme une validation de leçon.

## Prochain examen indépendant

Je lirai les nouvelles preuves et la proposition précise avant de rendre un nouveau verdict. J'indiquerai les comparaisons soutenues, les inférences raisonnablement justifiées et tout point encore insuffisant. Aucune dose, fréquence, preuve de lecture ou validation ne sera ajoutée pour rendre le dossier artificiellement acceptable.

Conclusion de méthode : une cohorte commune tous âges n'est pas imposée. Une synthèse qualitative stratifiée mérite un audit effectif et peut permettre de progresser ; sa validité dépend des preuves et du sens explicitement donné à l'ordre proposé.
