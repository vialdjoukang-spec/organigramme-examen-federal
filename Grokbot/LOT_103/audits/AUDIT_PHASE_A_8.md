# Audit médical 8 — LOT_103 Phase A (S7.9 Troubles de la sensibilité)

- Date : 15.11.2026. Contre-auditeur neuf, lecture seule. Base : `edaa6cef4ff8fa441831708a219c279ce0cb405a`.
- Fichier : `Grokbot/LOT_103/LOT_103_Phase_A_V0.html`, 108 207 octets, SHA-256 `a1774f4df49eb918b1b8e936d34bb9e3dc7b93bc324d00ad9f805deb6e19c248`.
- Liste : `LISTE_DX_CANONIQUE.md`, non gelée. Question finale : **non**. Gel : **non**.
- **Verdict : NON CONFORME. Score : 96/100.** Critiques : 0. Graves : 1. Mineurs : 2.
- Grille Θ3 (2, 1 ou 0) : p1=2, p2=2, p3=1, p4=2, p5=2, p6=2, p7=2, p8=2, p9=2, p10=2, p11=2, p12=2, p13=2, p14=2. Somme 27/28.

## Portes

`controle3.py --script-ok` : VERT, 108 207 octets, 396 phrases, connecteur 32 %, paragraphes sans connecteur 0, aucun défaut. `verif_aips.py` : OK, 0 AIPS citée. `aips_fiche.py verifier` : 0 défaut bloquant. `abreviations.py` : 0 sigle non développé. « car » : 0. Les phrases du corps tiennent dans 12 à 28 mots, hors « Fermer » et hors la légende d'image. Ce n'est ni le « car » plaqué, ni le style télégraphique. Ne pas ajouter de connecteur pour franchir 35 %.

## Liste

Les dix noms sont des maladies concurrentes. E1 attaque, E2 Guillain-Barré, E3 myélopathie cervicale, E4 vasculite provisoire suivent le délai et la létalité lus. Le rang 1 (3,8 %, dénominateur dit) et le rang 2 (30 à 40 % des polyneuropathies) sont honnêtes. Les rangs 3 à 10 n'ont pas de cohorte commune : le texte le dit, donc ce n'est pas un Grave. La lombalgie irradiée et la neuropathie des chimiothérapies ne sont pas numérotées. La queue de cheval n'est plus attribuée à Schaller ; elle ne figure que comme description du cas Eurorad 18552.

## Ce qui a été ouvert et qui tient

NHS England, Clinical Commissioning Policy for therapeutic immunoglobulin 2025, PDF ouvert : diagnostic hospitalier du Guillain-Barré ou d'une variante, puis quatre critères alternatifs par « OR » : « Significant disability (Hughes Grade 4) OR Disease progression towards intubation and ventilation OR mEGRIS score ≥ 3 OR Poor prognosis mEGOS ≥ 4 ». Exclusion lue : « Patients with mild and/or non progressive disease not requiring intubation ». Le cours reprend ces quatre critères en « ou », Hughes 4 inclus, et il ne recopie pas les 2 g/kg. Keddie ne porte plus ce seuil. IASP Terminology : paresthésie = « an abnormal sensation, whether spontaneous or evoked ». MonAM : 6,2 % (5,8 à 6,6), n = 21 906 ; femmes 5,6 % ; hommes 6,9 % ; 75 ans et plus, tous sexes, 15,4 %. OFS, asset 34027818, texte extrait : 22 517 attaques en 2023, 12 132 hommes, 10 385 femmes, 2 580 décès. Obsan 2019-2023 : 249,4 (247,9 à 251,0), brut 249,5, moyenne 21 729, létalité 12,2 % (12,0 à 12,4), 2 651 décès. Société suisse de la SEP, 27.01.2024 : 18 000 (17 400 à 18 700), 2,7 pour 1, 15 000 en 2016, hausse d'environ 20 %, un cinquième démographique. Atroshi, JAMA 1999 : 14,4 % (13,0 à 15,8), 3,8 % (3,1 à 4,6), 4,9 % (4,1 à 5,8), 2,7 % (2,1 à 3,4), 2 466 sur 2 960 joignables, 170 000 habitants, 125 témoins à 18,4 % (12,0 à 26,3). Espagne, Eur J Neurol 2024 : 1,78, 1,71, 1,41, 1,66, moyenne 1,67, ventilation 11 %, hommes 63,9 %, âge 53,2 ans, 2,18 et 1,18, pic 3,26 entre 70 et 79 ans. Keddie, Brain 2021 : incidence 1,65 à 1,88 pour 100 000, 2016-2019. EAN/PNS 2023, van Doorn : immunoglobulines ou échanges si le patient ne marche plus sans aide (GBS-DS 3 ou plus) ; « SBC < 20 » pour le transfert en soins intensifs ; chute de la capacité vitale forcée de plus de 30 % en 24 heures. mediX, août 2022 : chirurgie après échec du conservateur, ou lésion grave avec atrophie thénarienne ou déficit moteur ; amélioration souvent après l'accouchement. HAS, septembre 2012 : chirurgie d'emblée possible pour déficit moteur, amyotrophie ou perte axonale. RMS 2015, 2019 médecine interne et 2019 sujet âgé relus sur les extraits locaux : 3,3/1 000, 6 à 8 mois, forme avancée et concordante, vignette 108 g/L, 101 fL, 35 G/L, 100 pmol/L, 8 %, 49 mL/min, 77 %, 17,5 %, alcool > 30 g. OpenStax, Wikimedia `1313_Spinal_Cord_Cross_Section.jpg` : CC BY 4.0, 18 mai 2016, lame LM × 40, Régents du Michigan 2012. Eurorad 18806 : infarctus sylvien droit en diffusion. Eurorad 18552 : rehaussement des racines de la queue de cheval. Image locale JPEG, pas un SVG, pas une image générée. Aucun milligramme.

## Anciens défauts (audits 1 à 7)

Le grave de l'audit 7 est corrigé : le seuil ne cite plus Keddie, et le PDF 2025 porte bien Hughes 4, l'intubation, le mEGRIS ≥ 3 ou le mEGOS ≥ 4, en critères alternatifs. Le mineur de l'audit 7 est corrigé : le point 4 et l'arbre disent le déficit moteur brusque ou progressif, et les 6 à 8 mois. Les graves des audits 1 à 6 ne sont pas revenus : 83,2/100 000, rapport 1,6, décomptes 2022 et fourchette SEP 2016 absents ; 15 % et 23,1/1 000 séparés ; rangs E1 à E4 ; Liège ne fixe pas l'opération ; aucun milligramme ; queue de cheval hors de Schaller ; pas de phrase de grossesse qui retarde l'IRM.

## Critique

Aucun. Aucune dose en milligrammes, aucune voie contraire à une fiche AIPS.

## Grave

1. **Le croisement sensitif est attribué à une revue qui ne l'écrit pas.** « Ces messages montent ensuite dans les cordons postérieurs de la moelle, du même côté, jusqu'au bulbe. » « Le premier relais dépend du calibre de la fibre, et la grosse fibre ne croise qu'au niveau du bulbe. » « La petite fibre synapse dans la corne postérieure et elle croise déjà dans la moelle, du côté opposé. » « Le thalamus puis le cortex pariétal reçoivent les deux canaux, de sorte qu'une lésion hémisphérique peut n'emporter qu'un hémicorps. » « Le nerf périphérique contient les deux calibres de fibres sur une grande longueur, du pied jusqu'au plexus. » Les quatre premières citent `rmsnp`, la cinquième cite `rmsage`. Bernard-Valnet, Revue médicale suisse, 20.11.2019, écrit seulement que le sens épicritique passe par les fibres de gros calibre puis les cordons postérieurs, et que la douleur et la température passent par les fibres de petit calibre puis les voies spinothalamiques. L'article du sujet âgé oppose petites et grosses fibres ; il n'écrit pas le trajet du pied au plexus. L'anatomie est classique, la source citée ne la porte pas. Correction : garder les deux voies telles que la revue les écrit, et retirer le bulbe, le croisement, le thalamus, le cortex pariétal et le plexus, sauf à les poser sur un extrait d'anatomie qui les contient.

## Mineur

1. **Le syndrome de Miller Fisher n'est pas dans l'exclusion recopiée.** « La politique britannique de 2025 autorise l'immunoglobuline si le Guillain-Barré, ou une variante, est diagnostiqué à l'hôpital et qu'un critère alternatif est rempli. » Le même PDF, dans la cellule du Guillain-Barré, ajoute : « Patients with Miller Fisher Syndrome do not usually require Ig and unless associated with GBS overlap with weakness will recover normally. » Correction : « Le syndrome de Miller Fisher n'appelle habituellement pas l'immunoglobuline, sauf s'il chevauche un Guillain-Barré avec faiblesse. »

2. **Le compte de la voix est accroché à l'étude d'incidence espagnole.** « On demande ensuite de tousser et de compter jusqu'à ce que la voix se fatigue. » Blanco-Ruiz, 2024, donne l'incidence et les 11 % de ventilation ; il ne décrit pas ce geste. Le compte jusqu'à 20 et la chute de 30 % sont déjà justes au point 11 sous l'EAN/PNS 2023. Correction : citer `eangbs` pour la toux et le compte, et laisser à l'Espagne le seul taux de ventilation.

Prompt L1 lu et appliqué.
