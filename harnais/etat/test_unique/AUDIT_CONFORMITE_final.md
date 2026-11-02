# Audit de conformité (langue et forme) — LOT_001_Phase_B_V0_DX.1.html (itération 8)

Portée : langue, forme de la directive de Vial, affectation des 14 points. Cohérence A↔B et décompte des fichiers ignorés (ordre de Vial). Cours non modifié.

## Mesures
| Outil | Résultat |
|---|---|
| circuit_vial mesurer | 0 ligne longue, 0 balise, 0 grave S21, langue 96,2 (0 crit.), médical 96,0 (0 crit.), 72 doléances MOYEN et 3 DETAIL (non détaillées par l'outil) |
| scanner (points 1,5,6,7,10,11,13,14) | Texte extrait sans alerte critique ; lecture manuelle des points 6, 7, 10, 11, 13, 14 |
| Points présents | 1 à 14, titres et ancres `dx1-p1` à `dx1-p14` corrects |

## Conformité à la directive
| Exigence | Constat |
|---|---|
| Phrases complètes, registre soutenu | Conforme : sujet « Le médecin… », verbes conjugués, y compris dans les fenêtres |
| Puces pour les énumérations (cellules incluses) | Conforme : listes `<ul>` en point 7 ; critères d'arrêt en puces |
| 7.n « Syndrome de… » | Conforme : 7.1 à 7.8 (« Syndrome vasomoteur… », « Syndrome carcinoïde »…) |
| Symptômes fonctionnels / Signes physiques | Conforme : sous-cellules cliquables (`input checkbox` + `label.dxt`) ; la fenêtre contient Recherche, Valeur, Piège |
| Point 10 : algorithme | Conforme : losanges et cases, tracés `path` horizontaux (H) et verticaux (V), aucun cercle ni trait oblique (0 occurrence de circle/ellipse/line/L), cases cliquables avec détail |
| Point 11 : But, Moyens, A, B | Conforme : « 1- But », « 2- Moyens et méthodes », A (algorithme, non-spécialiste avant transfert, service spécialisé, actes cliquables), B (mesures générales puis spécifiques par priorité, pharmacologique avant non pharmacologique) |
| Bande colorée et soulignement du titre du point 11 | Non vérifié visuellement (rendu non ouvert) |

## Constats
| Gravité | Emplacement | Constat | Correction attendue |
|---|---|---|---|
| Léger | Point 14, Q17 : « Pas forcément : l'hypoglycémie nocturne provoque des sueurs… » | Tournure faible, réponse elliptique ; plusieurs réponses débutent par « Non : » | Rédiger « L'hypoglycémie nocturne provoque aussi des sueurs ; la glycémie capillaire tranche. » |
| Léger | Point 6, cellules « Technique : … Valeur : … Piège : … » | Majuscule irrégulière après « Valeur : » (« L'érythème… » / « la fièvre… ») ; point 7 emploie « Recherche : » au lieu de « Technique : » | Harmoniser majuscules et étiquettes |
| Léger | Point 7, « Signes physiques : cou et visage / peau / extrémités : » | Double deux-points | Supprimer le second |
| Léger | Point 10, nœud q3 et q3b | Répétition de « Le médecin dose la TSH » | Supprimer dans q3 |
| Léger | Point 10 et 11, « Hyperthyroïdie ( DX .7) » | Espaces parasites autour de l'abréviation | Corriger le balisage |
| Léger | Point 11.B, « Choix entre THM et traitement non hormonal. », « Voie d'administration. », « Efficacité attendue » | Intertitres nominaux ; la phrase verbale suit chaque fois | Acceptable ; conserver |
| Léger | Point 11.A | Les filières coronarienne, AVC et embolie reparaissent dans l'algorithme, chez le non-spécialiste puis en service spécialisé | Voulu par la directive ; réduire les redites des fenêtres |

Aucun constat Critique, Grave ou Moyen : aucun écart ne fausse la conduite clinique, la préparation à l'examen ou la directive de forme.

## Limites
Fond médical, sources et doses hors périmètre (audit de langue et de forme). Rendu graphique, bande colorée et clic des cases non testés dans un navigateur.

## Question finale
« Un médecin spécialiste universitaire du domaine valide-t-il cette leçon telle quelle ? » **Oui** pour la langue et la forme. Il manque seulement les corrections légères ci-dessus et la validation du fond par l'auditeur médical.

VERDICT: oui · critiques 0 · graves 0 · moyens 0
