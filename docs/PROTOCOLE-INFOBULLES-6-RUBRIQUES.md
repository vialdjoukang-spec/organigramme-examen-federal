# Prototype obligatoire des diagnostics différentiels · périmètre corrigé le 19.10.2026

Interaction actualisée : ouverture uniquement après clic, toucher ou activation clavier. Le survol ne déclenche aucune infobulle, y compris pour les termes imbriqués et les repères. Aucun appui long automatique.

Périmètre : les six rubriques monographiques s’appliquent uniquement aux diagnostics différentiels. Les SSP et leurs quatorze parties de cours conservent chacun leur contenu antérieur spécifique : définition, épidémiologie, physiopathologie, démarche, anamnèse, examen, etc. Le clic sur une partie du cours doit afficher cette partie seule avec son titre et sa source ; il ne doit jamais la remplacer par une monographie commune. La fiche éclair SSP conserve définition et points clés. Cette correction de périmètre prime sur les anciennes consignes qui étendaient le prototype aux SSP.

L’ouverture reste au clic, au toucher ou au clavier uniquement, y compris pour les termes imbriqués ; le survol n’ouvre rien. Dans les monographies DD, les intitulés et sous-titres seuls sont en gras ; le corps reste en texte normal. Le contenu existant est réorganisé puis enrichi avec des sources suisses ou européennes effectivement relues. Une migration de mise en page ne vaut pas une relecture clinique.

**Titre du diagnostic différentiel**

**1- Généralité & Définition**
Une définition précise situe la maladie ou le problème.

**2- Épidémiologie et Sex Ratio**
Préciser population, lieu et période pour chaque chiffre ; garder « À vérifier » lorsque la source adaptée manque. Ne pas confondre une prévalence de population et la fréquence parmi les patients consultant pour la plainte.

**3- Physiopathologie**
- Expliquer le mécanisme causal en phrases courtes et compréhensibles.
- Relier l’anomalie aux manifestations et aux choix diagnostiques ou thérapeutiques.

**4- Sémiologie clinique**
- Nommer chaque syndrome, puis ses symptômes et signes cliniques spécifiques sur une ligne.
- Signaler les manifestations discriminantes et les urgences applicables, sans réduire la fiche à une liste générique.

**5- Sémiologie aux explorations**
**Examen de référence diagnostique :** nommer l’examen ou la démarche qui établit le diagnostic, lorsque cela s’applique. Un diagnostic clinique doit être annoncé comme tel ; aucun « gold standard » universel n’est inventé.
**Chronologie du bilan (prototypes `chronologie_version: 1`) :** placer la référence en tête, puis ordonner `bilan_ordre` de un à six temps. Le premier porte le titre « À faire en premier » et reprend mot pour mot `exp_premier`. Chaque temps indique le bilan concret et le résultat recherché. Séparer le bilan initial urgent de l’examen de référence ; aucun examen ne retarde une mesure urgente.
**Biologie :** examen précis → anomalie ou résultat recherché.
**Morphologie :** examen précis → signe ou lésion recherchée.
**Explorations fonctionnelles :** examen précis → anomalie recherchée, si applicable.
**Critères diagnostiques :** intégrer ici les éléments nécessaires du précédent champ Diagnostic ; ne pas perdre d’information ni créer une septième rubrique.

**6- Prise en charge**
**A- But :** objectif clinique spécifique, concis et précis.
**B- Moyens**
**Mesures générales :** mesures adaptées au contexte.
**Pharmacologie :** traitement, indication, limites et précautions utiles ; posologie uniquement si AIPS suisse effectivement relue, sinon « À vérifier (AIPS) ».
**Autres :** gestes, chirurgie, intervention, soutien ou suivi selon le contexte ; sous-titres supplémentaires possibles si justifiés.
**Chronologie de la prise en charge (prototypes `chronologie_version: 1`) :** ordonner `pec_ordre` en une à six phases sous B-Moyens. Dans chaque phase, présenter seulement les catégories présentes (`mes`, `pha`, `aut`) ; au moins une phase couvre les mesures générales et une couvre la pharmacologie. Lorsque des actions d’une même phase sont simultanées, le dire explicitement ; ne pas supposer que toutes le sont. Les mesures urgentes commencent sans attendre la fin du bilan ou un examen de confirmation. Chaque phase contient au moins une action.

La chronologie est déclarée par `chronologie_version: 1`, avec `bilan_ordre` (`titre`, `texte`) et `pec_ordre` (`titre`, et au moins un champ parmi `mes`, `pha`, `aut`). Dans le rendu prototype, la timeline remplace les anciens champs d’exploration pour éviter les répétitions ; garder `exp_ref` avant le bilan ordonné et afficher `dia` une fois après celui-ci. Le premier texte du bilan doit égaler `exp_premier`. Les fiches sans ces champs restent des fiches legacy : le compilateur conserve leur rendu antérieur et ne fabrique aucun ordre. Une fiche legacy n’est pas comptée comme prototype chronologique.

## Exigences de fonctionnement

- Les termes médicaux spécialisés des fiches corrigées renvoient à une définition courte cliquable ; les alias ne doivent pas détourner un autre sens du terme.
- Le même contenu corrigé doit s’afficher au clic, au toucher et au clavier ; les retours entre infobulles et les sources restent accessibles.
- La liste des diagnostics est classée par fréquence décroissante dans un cadre comparable. Une valeur inconnue n’est ni zéro ni un chiffre à inventer. Un classement qualitatif exige une source et un contexte ; à défaut, l’incertitude du rang reste explicite et le point reste ouvert.
- Le suivi distingue : structure affichée, contenu spécifique relu, terminologie définie, classement documenté et publication vérifiée. Aucun compteur de volume ne certifie ces critères à lui seul.
- Les jauges `chronologie_structures` et `chronologie_relectures` suivent séparément la présence des deux chronologies valides et le registre central `tools/coordination/relectures.json`. La jauge exige l’attestation documentaire actuelle déjà liée à l’empreinte SHA-256 de la fiche, à un rapport existant dont l’empreinte correspond et à des sources présentes dans le catalogue, avec `chronologie_relue: true`. Une mention dans un rapport seule ne suffit pas. Aucun marqueur n’est ajouté automatiquement ; ces jauges ne certifient pas une validation médicale ni la qualité de la source.

## Priorité exclusive et lots

Reprise à G1 (sueurs / hyperhidrose), puis progression dans l’ordre du catalogue par petits lots. Le lot G10 radiculalgie/polyneuropathie arrêté reste conservé localement, non publié. Aucun autre chantier clinique, station, croquis ou enrichissement hors de cette correction ne doit être relancé pendant la cellule de correction. Les vérifications, scripts et publications nécessaires à cette mission restent actifs.

Les entrées du cours dans Notions CK ouvrent exclusivement le contenu spécifique de leur rubrique dans TIP.c. L’index c5 (sixième rubrique : examen physique) conserve son rendu par région et ses renvois de gestes ; le titre d’un SSP conserve sa fiche éclair. Les données de monographies SSP créées par erreur restent archivées sans être affichées ni proposées comme travaux à poursuivre. Les monographies DD continuent à s’ouvrir depuis leurs seuls diagnostics différentiels.
