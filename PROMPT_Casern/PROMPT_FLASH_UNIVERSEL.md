# PROMPT FLASH — fiche de révision d'un SSP (valable pour toute IA)

**Projet.** Produire, pour chaque SSP du catalogue suisse PROFILES 2023 (248 LOT), des fiches Flash HTML de 100 à 150 Ko destinées aux médecins en spécialisation qui préparent l'examen fédéral suisse.

## Exigences de rédaction
- **Fiche Flash = loi de Pareto** : ne garder que les 20 % d'information qui donnent 80 % de la compréhension. Le reste est du bruit : le retirer. Du mécanisme vers la clinique, puis vers le traitement qui s'en déduit.
- **Volume** : 100 à 150 Ko par fichier (200 Ko toléré ; 298 Ko = limite absolue). Mesurer avant de livrer ; couper le superflu, jamais un chiffre sourcé.
- **Style universitaire** : registre soutenu, phrases complètes (sujet, verbe conjugué, complément), une idée par phrase, termes dédiés, abréviations développées à la première occurrence, unités SI, virgule décimale. Zéro phrase nominale, zéro bavardage, zéro redite.
- **Interactivité** : chaque terme technique, symptôme, signe, examen, médicament ou score est un mot cliquable ouvrant une vraie fenêtre (modale) ; le survol est réservé aux précisions courtes. Un syndrome ouvre un tableau à 2 colonnes : *symptôme | signes physiques*. Les détails d'algorithme vivent dans les fenêtres.
- **Mise en page** : chaque point est un îlot à bordure, texte justifié ; points 1-4 dans un même îlot, 5-6 dans un autre, le reste replié. Page aérée, jamais d'îlot saturé. Algorithme en cases (rectangles, losanges) reliées par traits horizontaux et verticaux uniquement.
- **Vérité** : jamais de chiffre ni de dose inventés. Doses : AIPS suisse seulement (spécialité®, dose, voie). Local (épidémiologie, recommandations, filières) : source suisse d'abord ; source non suisse admise pour l'universel. Source lue et datée, sinon « À vérifier ». Sources en dernière page ; dans le texte, numéro en exposant entre crochets.
- **Prise en charge (point 11)** : titre gras, bande colorée, souligné. 1- But. 2- Moyens et méthodes : A. Urgences (non-spécialiste, puis service spécialisé ; actes cliquables) ; B. Hors urgences (mesures générales, puis spécifiques par priorité : pharmacologique, puis non pharmacologique, social, professionnel).
- **Rien de personnel** : aucune donnée personnelle ; jamais modifier `/workspace/ssp/app.html`.

## Grille des 14 points : questions à se poser, contenu attendu
Après chaque point, relire et répondre honnêtement ; un seul « non » impose de réécrire le point avant de passer au suivant.

| N° | Question que l'IA doit se poser | Contenu attendu |
|---|---|---|
| 1 Définition | La définition est-elle exacte, brève, et distingue-t-elle l'entité de ses voisines ? | 1 à 4 phrases, du général au particulier, classification d'origine entre parenthèses (CIM-11, DSM-5…) |
| 2 Épidémiologie | Le lecteur voit-il qui est touché, combien, et pourquoi cela compte ? | Prévalence/incidence Suisse d'abord (OFS, OFSP, Obsan), puis Europe ; âge, sexe, risques, enjeux ; chiffres sourcés et datés |
| 3 Physiopathologie | Chaque étape (amorce, développement, installation, maintien) se comprend-elle, et se relie-t-elle au traitement ? | Cascade moléculaire → clinique ; tableau lésion → exploration → thérapeutique |
| 4 Démarche diagnostique | Les drapeaux rouges sont-ils cités et expliqués, et chaque DD dangereux a-t-il son signe qui tranche ? | Étapes graduelles jusqu'au diagnostic ; drapeaux rouges cliquables ; DD utiles en fenêtre |
| 5 Anamnèse ciblée | Chaque question change-t-elle la décision, et pourquoi ? | Questions clés avec leur raison physiopathologique ; drapeaux rouges actionnables (urgence, imagerie, avis) |
| 6 Examen physique | Le normal précède-t-il le pathologique, et chaque signe a-t-il sa technique et sa valeur ? | Région par région ; chaque signe cliquable : geste, seuil, sensibilité/spécificité |
| 7 Approche syndromique | Chaque syndrome sépare-t-il symptômes fonctionnels et signes physiques, et dit-il comment chercher chaque signe ? | 7.1, 7.2… ; fenêtre-tableau 2 colonnes ; mécanisme de chaque signe |
| 8 Diagnostic positif | Sait-on ce qui suffit au diagnostic, et ce qui ne suffit pas ? | Critères de la société savante (année), seuils, exclusions, scores avec usage clinique |
| 9 Examens complémentaires | Gold standard nommé, 1re et 2e intention, interprétation et cas limites donnés ? | 9.a gold standard ; 9.b 1re intention ; 9.c alternatives ; 9.d 2e intention ; tableau résultat → signification → conduite ; grossesse, enfant, DFGe, allergies |
| 10 Arbre décisionnel | Chaque embranchement dit-il quel signe ou résultat mène à quelle décision ? | Algorithme en cases : exclure les graves, puis discriminer les fréquents ; chaque nœud cliquable |
| 11 Prise en charge | Le but est-il chiffré, l'ordre justifié, les médicaments complets et les populations spéciales couvertes ? | But ; A. urgences, B. hors urgences ; AIPS suisse ; enceinte/allaitante, âgé, enfant, insuffisances ; surveillance, sortie, pronostic ; social (LAMal, LAA, LAI) |
| 12 Prévention | Les trois niveaux sont-ils traités avec la recommandation suisse ? | Primaire, secondaire, tertiaire ; organisme et année ; gestes, populations, seuils |
| 13 Points clés | Ces phrases suffisent-elles la veille de l'examen ? | 3 à 6 phrases courtes, verbales, mémorisables, chacune portant une décision ou un fait critique |
| 14 Pièges d'examen | Les confusions classiques sont-elles posées en questions avec leur bonne réponse ? | Pièges de doses, critères, gravité, conduite ; question puis réponse puis raison courte ; rien d'inventé |

## Avant de livrer
Quatorze points présents ET correctement affectés ; volume 100–150 Ko ; chiffres et doses vérifiés ; fenêtres, îlots et algorithme fonctionnels. **Question finale : un médecin peut-il, avec cette fiche seule, gagner 90 à 100 % des points et traiter ce patient en sécurité ?**
