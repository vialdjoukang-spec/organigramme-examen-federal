# Audit médical 7 — LOT_103 Phase A (S7.9 Troubles de la sensibilité)

- Date : 15.11.2026. Contre-auditeur neuf, lecture seule. Base : `b83fc9fecf8617cc1c52f6665cf7a4f198f422af`.
- Fichier : `Grokbot/LOT_103/LOT_103_Phase_A_V0.html`, 107 113 octets, SHA-256 `51c4d3143aebc74dbe0a49a719a01d3fc0e0dbf5ffcf4bfc91f5befddd146dd5`.
- Liste : `LISTE_DX_CANONIQUE.md`, non gelée. Question finale : **non**. Gel : **non**.
- **Verdict : NON CONFORME. Score : 96/100.** Critiques : 0. Graves : 1. Mineurs : 1.
- Grille Θ3 (2, 1 ou 0) : p1=2, p2=2, p3=2, p4=1, p5=2, p6=2, p7=2, p8=2, p9=2, p10=2, p11=2, p12=2, p13=2, p14=2. Somme 27/28.

## Portes

`controle3.py --script-ok` : VERT, 107 113 octets, 395 phrases, connecteur 32 %, paragraphes sans connecteur 0, aucun défaut. `verif_aips.py` : OK, 0 AIPS citée. `aips_fiche.py verifier` : 0 défaut bloquant. `abreviations.py` : 0 sigle non développé. « car » : 0. Les phrases du corps tiennent dans 12 à 28 mots, hors « Fermer » et hors la légende d'image. Ce n'est ni le « car » plaqué, ni le style télégraphique. Ne pas ajouter de connecteur pour franchir 35 %.

## Liste

Les dix noms sont des maladies concurrentes. E1 attaque, E2 Guillain-Barré, E3 myélopathie cervicale, E4 vasculite provisoire suivent le délai et la létalité lus. Le rang 1 (3,8 %, dénominateur dit) et le rang 2 (30 à 40 % des polyneuropathies) sont honnêtes. Les rangs 3 à 10 n'ont pas de cohorte commune : le texte le dit, donc le gel reste fermé même après la correction du seuil britannique. La lombalgie irradiée et la neuropathie des chimiothérapies ne sont pas numérotées. La queue de cheval n'est plus attribuée à Schaller ; elle ne figure que comme description du cas Eurorad 18552.

## Ce qui a été ouvert et qui tient

IASP, page Terminology lue le 15.11.2026 : paresthésie = « an abnormal sensation, whether spontaneous or evoked » ; la note « non désagréable » est au point 8, avec hypoesthésie, hyperesthésie, dysesthésie, hyperalgésie (même mode) et hypoalgésie. MonAM, page lue : 6,2 % (5,8 à 6,6), n = 21 906 ; femmes de 4,5 à 5,6 % ; hommes de 5,1 à 6,9 % ; 75 ans et plus, tous sexes, 15,4 % (femmes de cet âge 11,7 %). OFS, asset 34027818 : 22 517 attaques en 2023 (12 132 hommes, 10 385 femmes) et 2 580 décès. Obsan, 2019-2023, Suisse : 249,4 (247,9 à 251,0), brut 249,5, moyenne 21 729, létalité 12,2 % (12,0 à 12,4), 2 651 décès. Extraits locaux relus : RMS 25.11.2015 (3,3/1 000, 15 % et 23,1/1 000 séparés, 0,6 %, 85 %, C7 puis C6, plus de 90 %, déficit brusque ou progressif, 6 à 8 mois, avancée et concordante, myélo-scanner, miction) ; RMS 20.11.2019 (30 à 40 %, diapason 6,9/5,5 et 6,2/4,7, alcool > 30 g, 3 verres et 2 verres, 53 %, chimiothérapie 60 % puis 30 %, urémie 90 %, cobalamine sans anémie, 3 à 4 %) ; RMS sujet âgé (8 %, 28 %, 35 %, vignette 108 g/L, 101 fL, 35 G/L, 100 pmol/L, 8 %, 49 mL/min, cohorte 2 290, 42 % puis 70 %, 77 %, biopsie 17,5 %, 8 à 36 % et 10 %). Cours de Liège : compression 30 s, 87 % et 90 %, déficit tactile absent chez 20 à 50 %, attelle 3 mois, nerf ulnaire nommé ; il ne fixe pas le seuil opératoire. Image `moelle-coupe-openstax.jpg` : JPEG 1 642 × 1 883, 1 677 568 octets, pas un SVG. Wikimedia, fichier `1313_Spinal_Cord_Cross_Section.jpg`, lu le 15.11.2026 : CC BY 4.0, OpenStax, 18 mai 2016. Aucun milligramme. La ligne EAN du point 11 reste juste : immunoglobulines ou échanges si le patient ne marche plus sans aide ; compte jusqu'à 20 ; chute de capacité vitale de plus de 30 % en 24 heures.

## Anciens défauts (audits 1 à 6)

Le grave de l'audit 6 n'est pas corrigé contre Keddie : la cellule a remplacé « à partir du grade 4 » par « dépasse 4 », qui est l'autre erreur. Les deux mineurs de l'audit 6 sont tenus : l'aréflexie achilléenne ne suffit plus seule ; « Poursuit-on » n'est pas repris dans un tableau. Le critique et le grave de l'audit 5 restent corrigés (réponse « Oui » et IRM cervicale ; signe de moelle cervicale, puis limite de la revue sous le cou). L'incidence 1,67 et les 11 % restent sous l'Espagne ; Campylobacter reste sous Keddie. Liens Eurorad 18806 et 18552, sans copie. Les graves des audits 1 à 4 ne sont pas revenus : 83,2/100 000, rapport 1,6, décomptes 2022 et fourchette SEP 2016 absents ; 15 % et 23,1/1 000 séparés ; rangs E1 à E4 ; Liège ne fixe pas l'opération ; aucun milligramme ; SEP dans les dix sans stock devant les 22 517 cas.

## Critique

Aucun. Aucune dose en milligrammes, aucune voie contraire à une fiche AIPS.

## Grave

1. **Le seuil britannique exclut le grade 4, et le « ou » détache le mEGOS.** « L'immunoglobuline n'est autorisée que si le grade de Hughes dépasse 4, avec évolution vers l'intubation et un score modifié d'Erasmus d'insuffisance respiratoire (mEGRIS) d'au moins 3. Ou si le score modifié d'Erasmus de pronostic (mEGOS) atteint 4, l'immunoglobuline est également autorisée. » La même phrase est dans la notice `sb-gbsuk`, dans `LISTE_DX_CANONIQUE.md` et dans `HELP.md`. Keddie, Brain 2021 (doi 10.1093/brain/awaa433), page Oxford Academic et PDF UCL `awaa433` lus le 15.11.2026, écrit : « Hughes Grade ≥4, progressing towards intubation and ventilation, with a high likelihood of respiratory support (mEGRIS score ≥ 3) or a predicted poor prognosis (mEGOS ≥ 4). » « Dépasse 4 » est strictement supérieur à 4 : le patient alité de grade 4, qui est le seuil écrit, n'est plus couvert. Le « ou » du papier oppose le mEGRIS et le mEGOS, tous deux chez le patient de grade au moins 4 qui évolue vers l'intubation. La seconde phrase autorise l'immunoglobuline sur le seul mEGOS. L'audit 6 avait cité un « > » que ces deux lectures ne portent pas. La ligne EAN du point 11 reste juste. Correction de la cellule et de la notice, puis le même sens dans la liste et dans HELP : « L'immunoglobuline n'est autorisée que si le grade de Hughes est d'au moins 4 et si le patient évolue vers l'intubation. Il faut en plus un mEGRIS d'au moins 3, ou un mEGOS d'au moins 4. »

## Mineur

1. **Le tableau comparatif raccourcit l'indication chirurgicale déjà juste au point 3.** « On propose la chirurgie si le déficit moteur apparaît d'un coup, ou si la douleur résiste 6 à 8 mois. » Schaller, RMS 25.11.2015, indique aussi le déficit moteur qui progresse sous traitement conservateur. La cellule du point 3 le dit : « On opère si un déficit moteur apparaît brusquement ou progresse, ou si la douleur résiste 6 à 8 mois. » L'arbre ne garde que les six à huit mois de douleur. Correction de la cellule du point 4 : reprendre la phrase du point 3. Dans l'arbre, ajouter : « On opère aussi si le déficit moteur apparaît brusquement ou progresse. »

Prompt L1 lu et appliqué.
