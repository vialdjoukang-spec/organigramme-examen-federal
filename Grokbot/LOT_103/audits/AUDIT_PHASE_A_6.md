# Audit médical 6 — LOT_103 Phase A (S7.9 Troubles de la sensibilité)

- Date : 15.11.2026. Contre-auditeur neuf, lecture seule. Base : `959939eb9681ca2674cad057075aba5a2c57c131`.
- Fichier : `Grokbot/LOT_103/LOT_103_Phase_A_V0.html`, 108 154 octets, SHA-256 `634162d6a453e1b6cb3109abcaf1aea89b473199f862c9b675f7f4fe5ef97e55`.
- Liste : `LISTE_DX_CANONIQUE.md`, non gelée. Question finale : **non**. Gel : **non**.
- **Verdict : NON CONFORME. Score : 96/100.** Critiques : 0. Graves : 1. Mineurs : 2.
- Grille Θ3 (2, 1 ou 0) : p1=2, p2=2, p3=2, p4=1, p5=2, p6=2, p7=2, p8=2, p9=2, p10=2, p11=2, p12=2, p13=2, p14=2. Somme 27/28.

## Portes

`controle3.py --script-ok` : VERT, 108 154 octets, 395 phrases, connecteur 32 %, paragraphes sans connecteur 0, aucun défaut. `verif_aips.py` : OK, 0 AIPS citée. `aips_fiche.py verifier` : 0 défaut bloquant. `abreviations.py` : 0 sigle non développé. « car » : 0. Les phrases du corps tiennent dans 12 à 28 mots, hors légendes de fermeture. Ce n'est ni le « car » plaqué, ni le style télégraphique. Ne pas ajouter de connecteur pour franchir 35 %.

## Liste

Les dix noms sont des maladies concurrentes. E1 attaque, E2 Guillain-Barré, E3 myélopathie cervicale, E4 vasculite provisoire suivent le délai et la létalité lus. Le rang 1 (3,8 %, dénominateur dit) et le rang 2 (30 à 40 % des polyneuropathies) sont honnêtes. Les rangs 4 à 10 n'ont pas de cohorte commune : le texte le dit, donc le gel reste fermé. La lombalgie irradiée (9,4 et 17,2 pour 1 000 ; 53 radiculopathies sur 103 dossiers, Spijker 2015) et la neuropathie des chimiothérapies ne sont pas numérotées. La queue de cheval n'est plus attribuée à Schaller.

## Ce qui a été ouvert et qui tient

IASP : page 403, définitions du cours conformes à la taxonomie 2011 déjà citée (paresthésie non désagréable au point 8). MonAM, cube `_113` lu le 15.11.2026 : 6,2 % (5,84 à 6,60), femmes 5,6 %, hommes 6,9 %, 2017 : 4,8 %, femmes 4,5 à 5,6 %, hommes 5,1 à 6,9 % ; 75 ans et plus, tous sexes, 15,4 %. OFS, asset 34027818 : 22 517 attaques en 2023, hommes 12 132, femmes 10 385, 2 580 décès. Obsan `_013`, 2019-2023, Suisse : incidence 249,4 (247,9 à 251,0), brut 249,5, moyenne 21 729, létalité 12,2 % (12,0 à 12,4), 2 651 décès. Atroshi, JAMA 1999 : 14,4 % (13,0 à 15,8), clinique 3,8 % (3,1 à 4,6), électrique symptomatique 4,9 % (4,1 à 5,8), les deux méthodes 2,7 % (2,1 à 3,4), 18,4 % (12,0 à 26,3) sur 125 témoins ; 2 466 réponses, 83 %, 3 000 tirés, région de 170 000 habitants. Société suisse SEP, 27.01.2024 : 18 000 (17 400 à 18 700), 2,7 pour 1, 15 000 en 2016, hausse d'environ 20 %, un cinquième lié à la population. Du Pasquier, RMS 28.01.2015, page lue : début 20-30 ans, deux poussées dans le temps et le territoire, syndrome clinique isolé, immunomodulateurs plus efficaces tôt. Espagne, Eur J Neurol 2024, texte intégral : 1,78, 1,71, 1,41, 1,66, moyenne 1,67, ventilation 11 %, hommes 63,9 %, âge 53,2 ans, 2,18 et 1,18, pic 3,26 entre 70 et 79 ans. Keddie, manuscrit accepté d'Oxford (doi 10.1093/brain/awaa433) : 1,65 à 1,88/100 000 ; Campylobacter et le confinement ; grade de Hughes **supérieur à 4**. EAN/PNS 2023, PDF lu : immunoglobulines ou échanges si le patient ne marche plus sans aide (GBS-DS ≥ 3) ; compte inférieur à 20 vers les soins intensifs ; chute de la capacité vitale de plus de 30 % en 24 heures. RMS 2015, RMS 20.11.2019, RMS sujet âgé et cours de Liège : chiffres du cours retrouvés dans les extraits (diapason 6,9/5,5 et 6,2/4,7, alcool > 30 g, 53 %, chimiothérapie 60 % puis 30 %, urémie 90 %, cohorte 2 290, 42 % puis 70 %, vignette 108 g/L, 101 fL, 35 G/L, 100 pmol/L, 8 %, 49 mL/min, 77 %, biopsie 17,5 %, C7 puis C6, plus de 90 %, 6 à 8 mois, 85 %, compression 30 s, 87 % et 90 %, déficit absent 20 à 50 %, attelle 3 mois). Image Wikimedia `1313_Spinal_Cord_Cross_Section.jpg` : JPEG réel, CC BY 4.0, OpenStax, 18 mai 2016, corne latérale thoracique, pas un SVG. Aucun milligramme.

## Anciens défauts (audits 1 à 5)

Le critique de l'audit 5 est corrigé : la question du point 14 répond « Oui » et retient l'IRM cervicale. Le grave de l'audit 5 est corrigé : l'arbre exige un signe de moelle cervicale, puis dit que la revue de 2015 ne décrit pas un niveau sous le cou. Le mineur 1 est corrigé : l'incidence 1,67 et les 11 % restent sous l'Espagne ; Campylobacter reste sous Keddie. Le mineur 3 est tenu : liens Eurorad 18806 et 18552, sans copie (pages en 403 à cette relecture). Le mineur 2 n'est pas tenu : la correction proposée parlait déjà d'« à partir du grade 4 », et le cours l'a recopiée. Les graves des audits 1 à 4 ne sont pas revenus.

## Critique

Aucun. Aucune dose en milligrammes, aucune voie contraire à un extrait AIPS.

## Grave

1. **Le seuil britannique est abaissé d'un grade, et le « ou » ne porte pas le bon critère.** « Au Royaume-Uni, les échanges sont rares et l'immunoglobuline est autorisée à partir du grade de Hughes 4, ou si la ventilation est proche. » La même erreur est dans la notice `sb-gbsuk`. Le manuscrit d'Oxford dit : « IVIG is also only authorised in the UK for patients with Hughes Grade >4, progressing towards intubation and ventilation, with a high likelihood of respiratory support (mEGRIS score ≥ 3) or a predicted poor prognosis (mEGOS ≥ 4). » « À partir du grade 4 » inclut le patient alité qui ne ventile pas. Le « ou » du papier introduit le mEGOS ≥ 4, pas une ventilation proche isolée. La ligne EAN du point 11, elle, est juste : immunoglobulines ou échanges si le patient ne marche plus sans aide. Correction de la cellule et de la notice : « Elle n'est autorisée que si le grade de Hughes dépasse 4, avec évolution vers l'intubation et un mEGRIS d'au moins 3, ou si le mEGOS atteint 4. »

## Mineur

1. **L'aréflexie achilléenne ne signe pas à elle seule la polyneuropathie.** « L'abolition bilatérale des réflexes achilléens signe la polyneuropathie, comme dans la vignette qui décrit l'ataxie. » La vignette du sujet âgé associe ataxie, aréflexie, hypopallesthésie à 2/8 et hypoesthésie en chaussettes. Correction : « Dans la vignette, l'aréflexie achilléenne accompagne l'ataxie et l'hypoesthésie, et elle ne suffit pas seule à poser la polyneuropathie. »

2. **Trois questions du point 14 reviennent dans le tableau.** « Faut-il poursuivre un symptomatique qui provoque des vertiges, une ataxie ou une confusion ? » puis « Poursuit-on un symptomatique qui provoque des vertiges, une ataxie ou une confusion chez la personne âgée ? » La septième décennie et le diabète sont repris de la même façon. Correction : garder ces trois questions dans le texte, et ne laisser dans le tableau que des questions qui n'y sont pas déjà.

Prompt L1 lu et appliqué.
