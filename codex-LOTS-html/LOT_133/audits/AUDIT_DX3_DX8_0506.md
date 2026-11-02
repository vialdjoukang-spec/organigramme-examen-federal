# Audit indépendant documentaire — DX.3 et DX.8 — reprise 0506

02.11.2026 UTC. Auditeur `audit_0506`, distinct des auteurs `dx3_0506` et `dx8_0506`. Écriture limitée à ce rapport ; aucun Git, fichier auteur, registre global ou sous-agent. Aucun score ni validation clinique.

**Verdict : les deux brouillons sont recevables pour intégration préparatoire aux empreintes exactes ci-dessous.** Les corrections demandées aux auteurs ont été intégrées puis relues. Ce verdict ne constitue pas une validation médicale humaine, un protocole prescriptif complet ou une vérification du futur rendu HTML.

| Fichier relatif au LOT133 | SHA-256 exact |
|---|---|
| `_travail/DX3_REDACTION_0506.md` | `a5f6776bc76f05a0589f218535808d69c679fca7a83e20455beead5ba3f4eb4d` |
| `_travail/DX8_REDACTION_0506.md` | `272c6a27434b55dfbafc062f74ae9c2fa56556c1d71c78837fed4a6db6c09dcc` |
| `evidence/DX3_0506.json` | `a50c3c802ea6821b7b7eaade4a3d5386658e491b7716dc02c3879735012b87e8` |
| `evidence/DX8_0506.json` | `ef5005bb88821e7c0de92469898faf8df6c11d206557f037d228491f8eaab5f2` |
| `LISTE_DX_CANONIQUE.md` | `4902f35db88823c5307089e7b955ec7fdb2ab8e0917d81e3c0ca1369f5d3c7eb` |

## Méthode et lectures effectives

Instructions locales, ARSENAL, `harness/GUIDE.md`, liste canonique, audits Phase A documentaire et médical lus. Leur verdict n'est pas transféré automatiquement aux nouveaux cours. `controler_brouillons.py` exécuté sur chaque remise avant audit, puis sur les deux versions finales : parties1–14 et questions1–14 présentes, sans doublon ; tailles finales DX3 31 422 octets et DX8 26 609 octets. Ce résultat mécanique ne valide pas le fond.

Les Markdown et preuves ont été lus, avec examen renforcé des points2,3,4,8,9,11,12. Les caches déclarés dans les preuves ont tous des SHA concordants. Contrelecture directe des caches acquis par les auteurs, sans nouvelle acquisition réseau par cet auditeur :

- DX3 S1 HUG haut débit : principes, précautions et surveillance pages1–3 ; S2 HUG chronique : définition, diagnostic, domicile, réadaptation et coordination ; S3 CeMIR21 : gravité et désobstruction, bilan, mécanismes, examens et raisonnement étiologique ; S4 SRLF-SFMU : définitions, cibles SpO₂, recommandations gaz3A–D, haut débit/VNI, critères d'intubation, soins intensifs et limitation d'intubation ; S5 CeMIR22 : passages gaz de référence/acidémie et VNI, dont coma hypercapnique et autres défaillances. Caches `_travail/_cache/dx3_0506/S1_texte_source.txt` à `S5_texte_source.txt`.
- DX8 S1 HUG2023 : pages3–12, dont texte diagnostique p5–7, attente d'imagerie p8, durée p10 et distal p12. Le graphe p2 n'a pas fait l'objet d'une nouvelle inspection visuelle par cet auditeur ; ses branches sont également écrites p5–6 et déjà auditées en Phase A. S2 ESC : les deux extractions diagnostic/traitement ; S3 ESC2018 : passages imagerie, récidive, symptômes d'EP, compression et suivi. S4 AIPS Eliquis : schéma TVP/EP, fonctions rénale/hépatique, contre-indications, interactions, SAPL et EP instable, mise à jour août2026. S5 HUG brochure2017 : pages3–5 et8, plan écrit, saignement, recours urgent et interactions. Caches `_travail/_cache/dx8_0506/` explicités dans la preuve.

HUG/AIPS sont suisses ; CeMIR/SRLF-SFMU français ; ESC est une société européenne, son éditeur Oxford britannique. Une acquisition du fournisseur antérieure au jour de lecture n'atteste pas l'absence de mise à jour ultérieure. Les extraits ESC ne sont pas une lecture intégrale ; leurs bibliographies ne sont pas réputées consultées.

## Résultats ciblés et corrections

| Objet | Constat et décision préparatoire |
|---|---|
| DX3 P2–3 | Causes et terrains sans fréquence suisse inventée ; shunt/effet shunt, pompe, hypercapnie et transport tissulaire distingués. Normocapnie interprétée selon évolution, pas intubation automatique. |
| DX3 P4 | Urgence clinique avant gaz/imagerie ; obstacle complet et toux efficace distingués ; support et recherche causale en parallèle. |
| DX3 P8–9 | Critères S4 PaO₂<60, SpO₂<90 ou besoin d'oxygène ; acidose pH≤7,35 avec PaCO₂>45 fidèles. Seuil CeMIR80 distinct. Gaz veineux pour exclure hypercapnie, gaz artériel si doute SpO₂/PvCO₂ élevée ou indications particulières ; PO₂ veineuse non substitutive. |
| DX3 P11 | Cibles94–98/88–92 sourcées, pas doses ni réglages. Champ S4 excluant OAP et BPCO hypercapnique conservé ; complément S5 couvre VNI BPCO et exception très surveillée du coma hypercapnique. Intubation non retardée. |
| DX3 correction P11 | Alternative générale « surveillance spécialisée équivalente validée localement » non étayée par S4 : supprimée à ma demande. Version finale exige soins intensifs dans le champ S4 ; initiation aux urgences sans retard de transfert et exception sanitaire clairement limitée. |
| DX3 correction P12 | S2 chronique n'étayait pas la transition oxygène aigu→long cours : réserve explicite ajoutée à ma demande, également Q12. Critères/calendrier restent à documenter dans une source dédiée ; coordination et réadaptation S2 conservées. |
| DX8 P2–4 | Proximal incluant poplitée/distal, facteurs transitoires/persistants et menaces EP/membre distingués ; pas traitement invasif systématique. |
| DX8 P8–9 | Probabilité prétest avant D-dimères ; positifs non confirmatoires ; forte probabilité vers échographie. Seuil HUG500µg/L rattaché au laboratoire avec réserve FEU/DDU. Examen limité/complet et résidu/récidive distingués ; contrôle5–7j si discordance, avant si aggravation. |
| DX8 correction P9 | Condition « sans symptômes d'EP » ajoutée à ma demande à la possibilité de clore le parcours après examen complet négatif, fidèle à S3. |
| DX8 P11 | Proximal au moins3mois ; distal à faible risque pouvant relever d'une surveillance organisée, durées courtes ESC non importées. HUG sur-généralise les limites ACOD : le cours ne copie pas cette généralisation. |
| DX8 AIPS | Eliquis oral10mg deux fois/j7j puis5mg deux fois/j ; prévention2,5mg deux fois/j seulement après au moins6mois, concordants avec notice exacte. Critères FANV non transférés. ClCr15–29 : prudence sans réduction automatique TVP ; <15 ou dialyse non recommandé. Child-PughC/coagulopathie et saignement, interactions inducteurs/inhibiteurs, SAPL et EP instable concordants. Nom exact « clairance de la créatinine » ajouté à ma demande. |
| DX8 P12 | Surveillance clinique/rénale malgré absence d'INR, mobilité/compression et réserve artériopathie cohérentes. Nouveau S5 relu : plan écrit et signes de saignement documentés ; rattrapage/doses de brochure ancienne non importés. |
| Références DX8 | À ma demande, les références sont désormais identifiables dans le Markdown avec URL/date/portée/limites, au lieu d'un seul renvoi à la preuve JSON. |

## Limites et intégration

DX3 : aucune notice AIPS exacte lue, aucune posologie validée ; cibles physiologiques non assimilées à des réglages d'oxygène. S1 technique2018 et S2 chronique restent limités ; pas protocole SDRA exhaustif, pas transition oxygène à domicile documentée. DX8 : contrôle AIPS limité à l'apixaban et aux passages cités ; aucune dose des autres anticoagulants approuvée. Les informations générales de ce cours ne remplacent pas l'évaluation individuelle des contre-indications, interactions et du risque hémorragique. Sources HUG2023, ESC2021/2022 et imagerie2018 reconnues comme telles ; brochure2017 limitée à l'éducation.

Les deux cours concernent l'adulte, hors parcours grossesse/pédiatrie. Les synthèses éducatives explicitement désignées restent des synthèses, pas des citations littérales. Aucun contrôle iconographique ou navigateur n'est effectué par ce rapport. Une concordance HTML ciblée doit encore vérifier les corrections et réserves, particulièrement DX3P11–12 et DX8P9,11–12, ainsi que les références. Toute modification substantielle exige une nouvelle contrelecture ciblée.

## Complément — concordance HTML ciblée

Extraction réelle par `harness/cache_controles.py extraire` et lecture des corps/fenêtres DX3P11–12 et DX8P9,11–12, puis contrôle des notices sources et liens externes dans le DOM. Aucun HTML lu intégralement. Les contrôles statiques et navigateur sont conduits par root, pas revendiqués ici comme exécutés par cet auditeur.

| HTML final contrôlé | Octets | SHA-256 exact |
|---|---:|---|
| `LOT_133_Phase_B_V0_DX.3.html` | 104942 | `27ab4c6c396ae52b29a8065ed508c8859196b240aee691cdd31339564d3de7d5` |
| `LOT_133_Phase_B_V0_DX.8.html` | 95100 | `09d614dbfb7c8c1ffd1a0781de7526d3ea69088dc17fc93d8d688ef016c54c7b` |

DX3 conserve les cibles physiologiques, l'exclusion OAP/BPCO du champ S4, l'exception encadrée du coma hypercapnique S5, le transfert en soins intensifs, la réserve AIPS et celle de transition vers oxygène long cours. DX8 conserve l'absence de symptômes d'EP requise dans la branche échographie complète négative, les doses et séquences exactes apixaban, la clairance de la créatinine nommée, les précautions/contre-indications, la durée individualisée et les conseils de surveillance sans rattrapage universel.

Un défaut de conversion documentaire a été signalé à root puis corrigé : `date_publication` des sources DX8 et `reserve_fraicheur` DX3 étaient absents des notices HTML. Leur présence finale a été directement vérifiée, notamment AIPS août2026 et brochure HUG juin2017. Les cinq liens de chaque chapitre et les portées de lecture sont conservés. Le libellé brut du titre DX3S1 demeure peu élégant, sans altérer sa source identifiée ni son ancienneté2018.

**Verdict complémentaire : concordance ciblée recevable pour intégration préparatoire aux SHA HTML ci-dessus.** Les réserves du rapport restent applicables ; pas de validation clinique, de contrôle intégral des autres parties, d'interaction navigateur ni d'inspection iconographique par cet audit.
