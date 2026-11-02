# Audit documentaire indépendant — LOT 133, reprise 0240

Date : 02.11.2026 UTC. Auditeur : `astra_audit_reprise`, distinct des agents de recherche et de rédaction. Périmètre : nouveaux éléments documentaires pour une Phase A destinée à la population adulte. Aucun score, aucune modification HTML, aucune validation médicale humaine.

**Verdict final après intégration : gel pédagogique possible de la sélection adulte et de ses orientations confirmatoires.** La version HTML de 102 806 octets, SHA-256 `60d1fdf9b889cf36a6e46af3255bd1fe58ae73a397e4b87ecbd75fe6f3dfd5e1`, a été contre-lue sur les points médicaux modifiés après QA mécanique verte déclarée par root. Aucune correction médicale bloquante identifiée dans ce périmètre. Ce verdict ne constitue ni une validation médicale humaine ni une validation de protocoles spécialisés exhaustifs. Les réserves provisoires ci-dessous sont historisées ; le tableau final d'intégration précise leur résolution.

Le harnais et le bracelet sont déclarés verts par le coordinateur ; les trois instructions locales et `CONTRE_AUDIT_ASTRA.md` ont été lus. Le verdict antérieur sur le HTML inchangé est réutilisé, sans nouvelle lecture du HTML. Les réserves documentaires antérieures restent ouvertes jusqu'à examen des nouvelles sources.

| Objet | Preuve nécessaire pour lever la réserve | État avant réception |
|---|---|---|
| Population | Adultes explicitement définis ; contexte clinique et exclusions pédiatriques précisés. | À documenter |
| Sélection des dix DD | Justification pédagogique explicite, périmètre non exhaustif ; ne pas présenter un classement suisse de fréquence sans données correspondantes. | À documenter |
| DX.1 | Source adulte CH/UE distinguant suspicion AVC/AIT, alerte et examens de confirmation ; la page d'information d'alerte seule ne couvre pas tout le parcours. | Réserve ouverte |
| DX.2 | Source adulte CH/UE pour l'évaluation du purpura et les situations graves ; ne pas transposer l'algorithme pédiatrique HUG comme protocole adulte. | Réserve ouverte |
| DX.3 | Source spécifique CH/UE, population compatible, signes discriminants, bilan initial et confirmation explicitement nommés. | Réserve ouverte |
| DX.4 | Source spécifique CH/UE, population compatible, signes discriminants, bilan initial et confirmation explicitement nommés. | Réserve ouverte |
| DX.5 | Source spécifique CH/UE, population compatible, signes discriminants, bilan initial et confirmation explicitement nommés. | Réserve ouverte |
| DX.6 | Source spécifique CH/UE, population compatible, signes discriminants, bilan initial et confirmation explicitement nommés. | Réserve ouverte |
| DX.7 | Source adulte CH/UE de démarche diagnostique ; distinguer suspicion et confirmation d'IC du suivi d'une IC déjà connue. | Réserve ouverte |
| DX.8 | Parcours de suspicion de TVP précisant probabilité clinique, place des D-dimères et échographie selon la source ; évaluation même sans symptômes respiratoires. | Réserve ouverte |
| DX.9 | Source spécifique adulte CH/UE pour thrombopénie : confirmation biologique et recherche d'une fausse thrombopénie, signes de gravité et orientation selon le contexte effectivement documenté. | Réserve ouverte |
| DX.10 | Source spécifique pour constat d'hippocratisme, limites des signes, causes et exploration bronchopulmonaire motivée par le contexte. | Réserve ouverte |
| P8/P9 | Chaque moyen de confirmation doit être nommé et rattaché à un passage probant ; une promesse de sourçage futur ne lève pas la réserve. | Réserve ouverte |
| Provenance | URL exacte, organisme, date/version disponible, population, passage effectivement consulté et limites pour chaque DD. | À contrôler |
| Géographie | Source CH/UE identifiée par contenu ; le NHS britannique ne satisfait pas ce seul critère. Une introduction UNESS ne prouve pas des chapitres non lus. | À contrôler |
| Prescriptions | Ne pas déduire une validation posologique de sources diagnostiques ; toute dose ultérieure relève d'une lecture AIPS ciblée. | Hors validation présente |

## Méthode de contrelecture prévue

| Contrôle | Critère |
|---|---|
| Attribution | Séparer ce que dit la source, la reformulation proposée et une éventuelle extrapolation. |
| Traçabilité par DD | Associer chaque proposition clinique nouvelle à un passage ou emplacement précis, et non seulement à une page d'accueil ou un titre de recommandation. |
| Consultation | Ouvrir le passage source exact ou son cache acquis ; signaler toute preuve non accessible ou seulement rapportée par un tiers. |
| Applicabilité | Vérifier adultes, contexte de soins, date/version, niveau de recommandation et limites explicites. |
| Proportionnalité | Une source d'alerte justifie l'alerte ; une brochure de suivi justifie le suivi ; aucune ne valide automatiquement un parcours diagnostique complet. |
| Décision | Distinguer réserve levée, partiellement levée ou persistante. Aucun gel imposé si la couverture reste insuffisante. |

## Résultat de contrelecture des nouvelles recherches

Les deux Markdown ont été lus après signal du coordinateur. Les réponses sources ont été inspectées dans `_travail/_cache/recherche_a/web_lecture_1.json` à `web_lecture_4.json` et les quatre caches JSON de `recherche_b/`. Il s'agit d'une contrelecture indépendante de passages acquis par les chercheurs, pas d'une nouvelle acquisition réseau. La matrice précédente consigne l'état initial ; les résultats ci-dessous la complètent.

| DD | Preuves effectivement contrôlées | Verdict et limite |
|---|---|---|
| DX.1 — AVC/AIT | A1, HUG CH, lignes 21–25 : scanner/IRM et recherche artérielle ; page d'information adulte. | Imagerie initiale et séparation du bilan étiologique recevables. Ne pas affirmer qu'une imagerie normale exclut tout AVC/AIT. Pas de validation du protocole de reperfusion adulte ; A2 pédiatrique ne comble pas cette lacune. |
| DX.2 — Purpura/sepsis | A4, CeMIR France, lignes 109,168–177,194–239 : défaillances, purpura fulminans, bilan, prélèvements ciblés sans retard antibiotique. | Socle adulte d'alerte et bilan recevable. A3 pédiatrique demeure hors parcours adulte. A5 HAS : passages précis revendiqués non présents dans les caches, donc réserve sur attribution des phrases scores/biomarqueurs ambulatoires. |
| DX.3 — Insuffisance respiratoire aiguë | A6, CeMIR France, lignes 108–136 et 227–252 : clinique, limites SpO2, gazométrie, radiographie/ECG et capnie. | Réserve principale de bilan initial adulte levée pour ces propositions ; confirmation du syndrome distincte de l'étiologie. L'absence de protocole pédiatrique n'est pas une lacune du périmètre adulte. |
| DX.4 — Anémie | A7, HUG CH 2022, lignes 241,258–275 : ferritine, vitamines, réticulocytes, hémolyse/saignement, causes multiples. | Orientation biologique adulte recevable. Nommer explicitement NFS/Hb pour confirmer l'anémie avant classification. Les unités incohérentes de diagrammes extraits ne doivent pas être reprises. A8 pédiatrique non nécessaire à l'adulte. |
| DX.5 — Obstruction biliaire | CH5 HUG, L87 ; UE5a SNFGE France, L44–51 et L74 ; UE5b L57–65 : biologie, échographie, IRM/écho-endoscopie et triade parfois incomplète. | Propositions recevables au niveau de la Phase A. Les sources grand public ne justifient pas un protocole interventionnel universel. Confirmation d'un obstacle à distinguer de son étiologie tumorale ou lithiasique. |
| DX.6 — Cirrhose décompensée | UE6, CeMIR France, L202–205 et L283–296 : ponction, neutrophiles/culture, culture négative, endoscopie ; CH6 HUG : procédure de ponction. | Réserve documentaire levée après complément `cemir_bilan_259_300.json` relu : L274–282 justifient le bilan, L300 le Doppler selon le point d’appel. Garder « peut comporter » ou une adaptation au contexte, comme dans la source. |
| DX.7 — Insuffisance cardiaque | CH7a HUG L46–56 ; CH7b L46,126,141–142 : symptômes, peptides, fonction échographique, ECG. | Examens désormais nommés et sourcés. La concordance clinique/objectivation est prudente ; aucune valeur élevée isolée ne confirme l'IC. Réserve sur algorithme complet de dyspnée aiguë, seuils et facteurs modifiant les peptides, non couverts ici. |
| DX.8 — TVP | CH8 HUG 2023, page 2, L40–56 : probabilité, Wells, échographie/D-dimères, répétition 5–7 jours. | Parcours proposé cohérent avec le texte extrait. Page 2 PNG désormais inspectée directement par cet auditeur : branche vraisemblable vers Doppler, invraisemblable vers D-dimères, positifs vers Doppler, Doppler négatif avec probabilité élevée vers répétition 5–7 jours. Absence de symptômes d'EP ne supprime pas l'indication d'évaluer une TVP. |
| DX.9 — Thrombopénie | A9 Berne CH, L5–6 : frottis, agrégats/EDTA et contrôle ; A10 CHU Saint-Pierre Belgique 08/2024, L50–64 : cytopénies, hémolyse, MAT et orientation urgente. | Réserve principale de confirmation levée. Conserver bilan contextuel, ne pas transformer les sérologies ou myélogramme en prescription universelle ni reprendre son seuil d'âge. A11 pédiatrique hors parcours adulte. |
| DX.10 — Hippocratisme/cancer pulmonaire | UE10 CEP France 2009–2010, L3408–3476 : signe et autres causes ; CH10 HUG L125–151 : imagerie, biopsie et extension. | Réserves sémiologie/confirmation levées pour ces propositions limitées. Le CEP ancien est une source de sémiologie, pas une recommandation oncologique actuelle. L'hippocratisme ne confirme pas un cancer ; filière oncologique seulement si suspicion clinique. |

## Points à régler avant décision de gel

| Priorité | Constat factuel | Action attendue |
|---|---|---|
| Bloquant pour l'attribution A5 | Le cache HAS contient une ouverture initiale L0–43 et un résultat de recherche ; les lignes 329–331,462,1014–1020 invoquées ne sont pas conservées. | Fournir la réponse source exacte correspondant à ces passages, ou ne pas intégrer les propositions qui en dépendent. L'absence de cache ne prouve pas que le chercheur ne les a jamais lus. |
| Résolu — UE6 | Complément `cemir_bilan_259_300.json`, L259–300, effectivement relu. | Bilan et imagerie recevables avec leur caractère contextuel. |
| Population | A développe aussi quatre branches pédiatriques. | Retenir uniquement les passages adultes dans cette Phase A ; ne pas fusionner les algorithmes. |
| Liste | Aucun résultat ne mesure les fréquences suisses relatives des dix DD. | Justifier une sélection pédagogique de dix exemples non exhaustifs ; aucun rang de fréquence ne peut être inféré. |
| Résolu — parcours TVP | Image `tvp2023_page2.png` affichée et inspectée directement par cet auditeur ; concordance avec `TVP_VISUEL_0240.md`. | Branches confirmées ; ne pas ajouter un seuil universel FEU/DDU ou ajusté à l’âge. |
| P8/P9 et rendu | Aucun HTML nouveau n'a été lu. | Une intégration doit nommer les examens au bon DD, rattacher les sources et supprimer toute promesse de sourçage ultérieur ; vérification ciblée ultérieure nécessaire. |

## Pays, ancienneté et prescriptions

Les apports retenus proviennent de Suisse (HUG, Université de Berne), France (CeMIR, HAS, SNFGE, CEP) et Belgique (CHU Saint-Pierre). Aucune référence britannique n'est nécessaire aux nouveaux parcours. Le CEP est ancien (2009–2010), HUG anémie daté 2022, HUG TVP 2023, fiche belge 08/2024 et HAS janvier 2025 ; plusieurs pages institutionnelles et la date précise de la huitième édition CeMIR ne sont pas établies. Une date de crawl ne les actualise pas.

Aucune posologie médicamenteuse n'est proposée dans les deux synthèses. Cela ne signifie pas que les documents sources sont dépourvus de doses : les passages CeMIR sepsis et le protocole pédiatrique AVC en contiennent. Ces doses n'ont pas été validées dans AIPS et ne doivent pas être récupérées par simple copie. Le délai d'échographie de 5–7 jours et l'angle unguéal sont des critères diagnostiques, pas des posologies.

**Conclusion :** documentation recevable pour un cours adulte d’inspection et d’orientation confirmatoire, sous exclusion ou preuve complémentaire des propositions A5 non vérifiées. Un gel pédagogique pourra être décidé après contrelecture ciblée de l’intégration ; l’absence de protocoles spécialisés exhaustifs n’est pas un obstacle à ce périmètre limité. Aucune donnée ne justifie un classement suisse fictif. Aucun HTML, fichier global ou Git modifié par cet auditeur.



## Contre-audit de l'intégration HTML

Le coordinateur a annoncé QA statique 20/20 et autorisé la contrelecture. Empreinte et taille ont été recalculées et concordent avec la remise du rédacteur. Lecture ciblée des points 2,3,4,7,8,9,10,11,12, de leurs fenêtres, de la déclaration adulte P1 et des vingt entrées de sources ; aucune lecture intégrale du HTML. L'extracteur fourni n'a pas reconnu les identifiants Phase A (`a-pN`) et a échoué explicitement ; une extraction locale des sections et fenêtres identifiées a servi de solution de lecture, sans modifier le harnais ni le HTML. Aucun contenu n'a été déduit d'un contrôle mécanique.

| Contrôle du rendu | Résultat |
|---|---|
| Population / sélection | Adulte explicite en P1/P7/P9 ; grossesse et pédiatrie nécessitent une adaptation ; exemples non exhaustifs sans classement suisse de fréquence. Le rappel pédiatrique P4 est clairement isolé. |
| Sources par DD | P7 rattache chaque ligne aux références appropriées : DX.1→2/5 ; DX.2→6 ; DX.3→7 ; DX.4→8 ; DX.5→11/12/13 ; DX.6→14/15 ; DX.7→3/16/17 ; DX.8→18 ; DX.9→9/10 ; DX.10→19/20. |
| Confirmation / bilan | P7–P9 nomment désormais les examens ; NFS/Hb pour anémie, frottis et numération contrôlée pour thrombopénie, imagerie/biologie contextualisées pour les autres DD. La promesse de sourçage futur a été remplacée dans ces points. |
| Urgences | 144 et régression du déficit conservés ; défaillances et purpura fulminans traités sans attendre les prélèvements ; diagnostic visuel non assimilé à confirmation. |
| TVP | Branches et répétition 5–7 jours concordent avec la page 2 HUG inspectée visuellement ; absence de symptôme respiratoire ne clôt pas le bilan. Aucun seuil D-dimères universel ajouté. |
| Cirrhose | Le bilan rendu correspond au complément CeMIR relu ; complication et terrain séparés, culture négative non excluante, endoscopie hospitalière urgente si hémorragie. P9 donne le contexte cirrhotique correspondant au libellé plus large du tableau. |
| Hippocratisme | Critères et causes multiples nommés ; CEP 2009–2010 explicitement ancien et limité à la sémiologie ; scanner et confirmation tissulaire rattachés à HUG. |
| A5 / NHS | Recherche ciblée dans le HTML : références HAS/NHS et formulations contestées A5 absentes. La réserve A5 ne bloque donc plus cette intégration. |
| Posologies | Aucune dose nouvelle dans les points médicaux contrôlés ; P11 exige une future vérification AIPS. Les doses présentes dans les sources n'ont pas été importées. |
| Limites du gel | Le gel concerne une sélection pédagogique et une orientation de confirmation chez l'adulte ; il ne valide pas le diagnostic sur photographie, une hiérarchie épidémiologique, la pédiatrie, la grossesse ou dix algorithmes thérapeutiques complets. |

La mention « liste non gelée » reste logiquement présente dans la version soumise à audit ; le coordinateur peut maintenant décider de son gel pédagogique et consigner cette décision. La définition du parcours spécialisé AVC, d'un algorithme exhaustif de dyspnée aiguë et des posologies demeure hors du périmètre demandé, sans faire obstacle à ce gel limité. Aucun score ajouté ; aucune modification de HTML, de fichiers globaux ou de Git par l'auditeur.
