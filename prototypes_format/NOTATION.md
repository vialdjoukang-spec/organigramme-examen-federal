# Notation des prototypes DX.10 (maladie d'Addison, G16) — 30.10.2026

Évaluation indépendante, en lecture seule. Elle porte sur l'ORIGINAL `LOT_Claude_Finaux/LOT_016/LOT_016_Phase_B_V0_DX.10.html` et sur les trois prototypes de `prototypes_format/`. Le même barème s'applique aux quatre fichiers.

## Résultats

| Fichier | Octets | Examen /100 | PEC /100 | Lisibilité /100 |
|---|---:|---:|---:|---:|
| ORIGINAL `LOT_016_Phase_B_V0_DX.10.html` | 138 620 | 97 | 99 | 58 |
| V1 `DX10_Addison_V1_sans_redondance.html` | 99 079 | 97 | 97 | 86 |
| V2 `DX10_Addison_V2_court.html` | 45 043 | 85 | 93 | 79 |
| V3 `DX10_Addison_V3_expert.html` | 95 815 | 98 | 96 | 88 |

## Barèmes (identiques pour les quatre fichiers)

**Examen (CK et CS).** Définition et distinction primaire, secondaire, tertiaire : 8. Épidémiologie utile : 7. Physiopathologie et rappels de base (axe corticotrope, rétrocontrôle, MSH, système rénine-angiotensine, CBG, mécanisme de la perte de poids) : 15. Signes discriminants : 12. Diagnostics différentiels discriminants : 8. Bilan de première intention et interprétation (couple cortisol-ACTH, seuils, Synacthène, œstrogènes, prélèvement avant hydrocortisone) : 15. Étiologie : 8. Piège de la TSH : 7. Crise surrénalienne : 12. Pièges d'examen : 8.

**Prise en charge quotidienne (PEC).** Urgence de l'adulte (prélèvement si sans retard, 100 mg, NaCl 0,9 %, 200 mg/24 h, glycémie, déclencheur, relais oral) : 20. Urgence de l'enfant (doses par âge et par kg, glucose 10 %, NaCl, entretien, relais) : 15. Traitement de fond et doses AIPS : 15. Règles de stress : 15. Éducation, carte, trousse, proche formé : 8. Contre-indications vitales et précautions (lévothyroxine, inducteurs du CYP3A4, Synacthen®, Florinef®, spécialités) : 12. Suivi : 10. Situations particulières et sortie : 5.

**Lisibilité.** Phrases complètes liées par des connecteurs, sans fragments : 25. Longueur des phrases et points-virgules : 10. Plan d'ouvrage (L'essentiel, sommaire en flux, h2 numérotés, h3) : 15. Fenêtres et dépliables (nombre, pertinence, conformité au cahier) : 20. Absence de redondance avec la Phase A et dans le fichier : 15. Mise en page (colonne, thème sombre, 390 px, sources) : 10. Fidélité des citations : 5.

## Mesures (outils, sans jugement)

| Mesure | ORIGINAL | V1 | V2 | V3 |
|---|---:|---:|---:|---:|
| Part du texte principal (hors fenêtres et dépliables) | 20 % | 33 % | 43 % | 38 % |
| Mots en tableaux | 50 % | 5 % | 18 % | 9 % |
| Phrases de prose avec connecteur | 14 % | 42 % | 35 % | 39 % |
| Phrases > 35 mots hors citations (`audit_langue.py`) | 10 | 37 | 7 | 25 |
| Phrases avec point-virgule (`audit_langue.py`) | 254 | 141 | 54 | 100 |
| Fenêtres `popover` / dépliables | 36 / 0 | 33 / 6 | 17 / 7 | 26 / 18 |
| 7-grammes communs avec la Phase A | 4,9 % | 1,0 % | 2,3 % | 1,8 % |

Toutes les fenêtres ont leur déclencheur et inversement. Aucun fichier ne contient de JavaScript, de `title=` ni d'espace insécable. Seule la fenêtre est en `position:fixed` ; le sommaire reste dans le flux.

## Contrôles demandés

**(a) Faits absents de l'ORIGINAL.** Un script a comparé tous les nombres des trois versions à l'ORIGINAL : aucun chiffre, dose ni seuil nouveau. Restent des énoncés modifiés :
- V1 : « c'est souvent un proche qui l'a remarquée » généralise le cas 1. Le lymphome « confirmé par biopsie ; les vomissements ont rendu les règles de stress essentielles » transforme une règle générale en fait du cas.
- V2 : « corticoïdes, anticoagulants, rifampicine ou œstrogènes, qui masquent le déficit » est faux, car seuls les œstrogènes masquent le déficit. « Une rénine entre 20 et 60 mUI/L indique une substitution correcte » perd la mention « une étude française ». « L'enfant reçoit des granulés pédiatriques » contredit « Alkindi® ou comprimés selon l'âge ». Plenadren® est cité ¹¹ au lieu de ¹⁰. La ligne « hypothyroïdie, maladie cœliaque… peuvent… la causer » est inexacte.
- V3 : « ses anticorps étaient négatifs » (cas 5) est un fait nouveau. Il est exact selon [S16], lu sur Europe PMC (PMC10735307). La phrase « cet effort fixe mieux la notion qu'une relecture » est une affirmation non sourcée. « C'est pourquoi Endo-ERN… réservent le nom » invente un lien causal. « Si bien que le scanner a montré » invente aussi une causalité. « Car l'aldostérone y reste réglée » (R 2.12) se déduit de [S6] et reste acceptable.

**(b) Citations AIPS.** Un script a comparé chaque citation entre « » aux textes AIPS du corpus `ressources_ia/aips/fi_fr` (AipsDownload_20261008) et à `.cache/aips/`. Il a couvert les n° 23533, 31095, 31723, 54949, 57970, 62068 et 68226. Il a normalisé les apostrophes, les espaces et les puces.
- ORIGINAL : toutes les citations AIPS sont conformes, une fois la mise en liste retirée (indication de l'hydrocortisone, contre-indications thérapeutiques de Synacthen®, schéma chirurgical de Solu-CORTEF®).
- V1 : 100 % conforme, sauf « ne dépasse[nt] », une adaptation entre crochets qui ne change pas le sens.
- V2 : 100 % conforme.
- V3 : une altération. Le texte de Florinef® donne « un risque d'insuffisance corticosurrénalienne aiguë », alors que l'AIPS 31095 dit « corticosurrénale ».
- Les paraphrases vérifiées sont conformes : Plenadren® (6 h–8 h, 30 minutes avant le petit déjeuner, 8 ± 2 heures, −20 %), Florinef® (30 jours à 25 °C au plus) et Alkindi® (3–4 mois, pas de sonde). Les sept numéros Swissmedic sont exacts et identiques dans les quatre fichiers.
- Seuils vérifiés à la source le 30.10.2026 : [S16] (< 100 nmol/L avec ACTH 2 fois la limite, 500/550, 412/485, 52 %, 85 %, hyperkaliémie chez moins de la moitié) et NICE NG243 (1 L en 30 minutes, 150/300 nmol/L, ≥ 40 mg/j, fludrocortisone 50–300 µg, œstrogènes arrêtés 6 semaines) : conformes.

**(c) Lisibilité et redondance.** L'ORIGINAL contenait peu de tronc commun : cohorte de Barcelone, renutrition, pesée. Les trois versions le remplacent par un renvoi. La redondance résiduelle tient surtout aux doses de crise, spécifiques et justifiées, puis à l'AIPS de Solu-CORTEF®. La Phase A contient déjà cette fenêtre en entier. V1 la renvoie à juste titre (vérifié), tandis que V2 et V3 en recopient une partie (vitesse, indications, grossesse et allaitement).

**Lacunes communes, héritées de l'ORIGINAL.** Aucun fichier ne rappelle les trois zones du cortex (glomérulée, fasciculée, réticulée). Aucun ne chiffre le traitement de l'hypoglycémie de l'adulte. `audit_langue.py` classe les trois prototypes « non conformes » au format de production (FIN_FICHIER, h2 « DX.n — nom », h3 `dxN-pM`, et pour V2 la bande 80–150 Ko).

## Appréciation par version

**ORIGINAL (138 Ko).**
- Forces : le fond est le plus complet et le plus exact. Toutes les citations AIPS sont exhaustives et les 14 questions d'examen sont présentes.
- Manques : la moitié du texte tient en tableaux télégraphiques et 80 % du contenu est caché dans 36 fenêtres-tableaux. Il n'a ni « L'essentiel » ni rappel anatomique structuré, ni thème sombre. La colonne mesure 1060 px. La dose de crise est répétée une dizaine de fois.

**V1 « sans redondance » (99 Ko).**
- Forces : la réécriture est fidèle et en prose liée. Une section « Rappel d'anatomie et de physiologie » s'y ajoute. Les dépliables sont courts, comme le prévoit le cahier. Le renvoi vers la Phase A pour Solu-CORTEF® est exact.
- Manques : 37 phrases dépassent 35 mots. Les pièges d'examen sont fondus en paragraphes, sans format question-réponse. Le schéma chirurgical AIPS de Solu-CORTEF® est annoncé mais absent (la Phase A ne l'a pas). Les sources sont abrégées, sans URL.
- Faits ajoutés : aucun chiffre ; deux généralisations mineures (point a).

**V2 « court » (45 Ko).**
- Forces : la version est la plus brève. La PEC d'urgence de l'adulte et de l'enfant est complète en fenêtre, et les pièges se déplient en question-réponse.
- Manques pour l'examen : lymphocytose et éosinophilie, Waterhouse-Friderichsen, marqueurs de l'APS1 (anticorps anti-interféron, hypoparathyroïdie), hyperthyroïdie et « TSH sans anti-TPO ». Il manque aussi la seconde moitié des données ALD et 8 des 14 pièges.
- Manques pour la PEC : contre-indication de Plenadren®, densité osseuse, sujet âgé, diabète de type 1 et vaccins.
- Forme : les exposants collés aux nombres créent des ambiguïtés (« 2,5¹⁶ʼ²² », « transglutaminase 2¹⁶ »). Les sources ne donnent pas de liens (« liens complets dans la V0 »). Trois inexactitudes de compression (point a).

**V3 « expert » (96 Ko).**
- Forces : le plan d'ouvrage est le meilleur. Il comprend un mode d'emploi, un schéma SVG accessible de l'axe et des h3 numérotés. Deux cas publiés illustrent la démarche (CS), et les 14 pièges se déplient pour un rappel actif. La version a le moins de points-virgules par mot.
- Manques : les contre-indications AIPS d'Alkindi® et de Plenadren® (hypersensibilité, dysphagie, prématuré, diarrhée chronique) manquent, ainsi que la dose d'Alkindi® en cas d'HCS (10–15 mg/m²/j). Une citation de Florinef® est altérée. Certains dépliables insèrent un paragraphe au milieu d'une phrase (thyroïde, droits sociaux).
- Faits ajoutés : un fait exact mais nouveau (cas 5), une phrase pédagogique non sourcée et deux liens causaux inventés (point a).

## Recommandation

Adopter **V3** comme modèle. Elle obtient les meilleures notes d'examen et de lisibilité, avec une PEC à 96. Avant de la généraliser, il faut corriger six points :
1. Rétablir « corticosurrénale » dans la citation de Florinef®.
2. Reprendre de V1 les contre-indications AIPS d'Alkindi® et de Plenadren®, ainsi que la dose d'Alkindi® en cas d'HCS.
3. Supprimer la phrase non sourcée et les deux liens causaux inventés.
4. Réduire la fenêtre Solu-CORTEF® à la vitesse et au schéma chirurgical, avec un renvoi à la Phase A.
5. Garder les dépliables courts (une parenthèse), comme dans V1.
6. Ajouter, avec une source lue, la zonation du cortex et, si une source européenne la donne, la conduite chiffrée de l'hypoglycémie de l'adulte.

Le harnais (`controle_lot.py`, `audit_langue.py`) doit être adapté au nouveau plan avant toute production.

**Taille cible d'un DD : 70 à 90 Ko, avec un plancher de 60 Ko et un plafond de 100 Ko.** Sous 60 Ko, la note d'examen passe sous 90, comme le montre V2 à 45 Ko (85/100). Pour atteindre 90, V2 devrait réintégrer environ 10 à 15 Ko : pièges complets, signes biologiques, APS1, contre-indications AIPS et sources. Un DD sans traitement d'urgence ni spécialités multiples peut viser 50 à 70 Ko.

## V4 « léger » (évaluation indépendante du 30.10.2026, même barème, mêmes contrôles a, b, c)

| Fichier | Octets | Examen /100 | PEC /100 | Lisibilité /100 |
|---|---:|---:|---:|---:|
| V4 `DX10_Addison_V4_leger.html` | 24 479 | 77 | 82 | 80 |

- **Forces.** (b) Les 24 citations entre « » sont conformes mot pour mot aux AIPS du corpus (23533, 31095, 31723, 54949, 57970, 62068, 68226). (a) Le script ne trouve aucun nombre nouveau, et le chiffre de 18,8 % est exact à la source ([S26], PMC12137789). Trois erreurs de la V2 sont corrigées : les œstrogènes « qui masquent », Plenadren® cité ¹¹, la ligne hypothyroïdie-cœliaque. Le plan est complet (L'essentiel, sommaire en flux, 14 h2). La fenêtre de crise adulte-enfant est exacte. Le fichier compte 4 phrases de plus de 35 mots, 56 % de texte principal et 1,6 % de 7-grammes communs avec la Phase A (c). La fenêtre Solu-CORTEF® n'est pas recopiée.
- **Manques pour l'examen.** APS1 et APS2 sont absents, ainsi que les maladies auto-immunes associées nommées (vitiligo, Biermer, maladie cœliaque). Manquent aussi la lymphocytose et l'éosinophilie, le syndrome de Waterhouse-Friderichsen, l'âge de 20 à 50 ans, le retard diagnostique chiffré, les facteurs de risque de crise, le cancer et la dysthyroïdie parmi les DD, l'arrêt des œstrogènes 6 semaines avant le test. Il reste 6 pièges sur 14.
- **Manques pour la PEC.** Le fichier ne donne aucun numéro Swissmedic ni aucune URL, et aucun proche n'est formé. Chez l'enfant manquent la répétition de la dose s'il reste instable, l'entretien hydrique et l'hyperkaliémie. Manquent aussi les contre-indications de Plenadren® et d'Alkindi®, la réserve de Synacthen® chez l'asthmatique et l'allergique, la dose d'Alkindi® en cas d'HCS, la césarienne, le post-partum, le sujet âgé, le diabète et les vaccins. 13 sigles ne sont pas développés (ACTH, MSH, CBG, BSPED…).
- **Erreurs créées par la compression (a).** *Prévention* : « le dépistage vise donc » invente un lien causal. La phrase omet la prévention primaire des causes médicamenteuses et ne garde que 2 des 5 lignes de dépistage de l'original. *Grossesse* : « 18,8 % … c'est pourquoi la substitution continue » invente aussi un lien causal, car [S26] conclut à renforcer la dose au 3e trimestre. Le dépliable « accouchement » commence par « Il reçoit » (sujet erroné), range l'hyperémèse sous l'accouchement et cite ²⁶ au lieu de ¹⁸ et ³². *Définition* : « Le terme est réservé à l'atteinte primaire, car il commande la fludrocortisone » contredit l'original, où Endo-ERN réserve « maladie d'Addison » à la forme auto-immune (erreur héritée de la V2, non relevée plus haut). *Règles de stress* : « petite intervention : 40 mg » perd « sous anesthésie locale », ce qui contredit l'AIPS de Solu-CORTEF® (« petites interventions: 200 mg d'hydrocortisone i.v. »).
- **Défauts mineurs.** « Ne pas administrer des doses inférieures à 25 mg par jour » est sorti du paragraphe pédiatrique de l'AIPS. La rénine de 20 à 60 mUI/L perd « une étude française », comme dans la V2. La TSH « chez 52 % » perd « sans hypothyroïdie connue ». « Au rang E1, car le médecin l'exclut en premier » inverse la cause. Quatre dépliables coupent une phrase, et « Selon NICE ▸ » cache les seuils du texte principal.

**Non : la V4 (77/82) ne tient pas 90/90.** Elle reste sous la V2 (85/93), ce qui confirme le plancher de 60 Ko. Elle ajoute aussi quatre inexactitudes de compression, dont les deux phrases reformulées (Prévention, grossesse).

## Notation après révision (évaluation indépendante du 30.10.2026, même barème, mêmes contrôles a, b, c)

Lecture seule des quatre versions révisées ; seule cette section est ajoutée. T = x (+ y) est lu dans l'élément `id="taille"` ; `harnais/taille_xy.py` redonne les mêmes valeurs. La couverture est mesurée par un script sur 145 notions tirées de l'ORIGINAL (69 d'examen, 76 de prise en charge) : l'ORIGINAL obtient 99 %, et les versions d'avant révision obtenaient V1 99 %, V2 81 %, V3 95 %, V4 54 %.

| Version | T = x (+ y) | Fichier (octets) | Examen /100 | PEC /100 | Lisibilité /100 | Couverture des notions |
|---|---|---:|---:|---:|---:|---:|
| V1 `DX10_Addison_V1_sans_redondance.html` | 17,6 Ko (+ 62,6 Ko) | 99 917 | 98 | 98 | 89 | 98 % |
| V2 `DX10_Addison_V2_court.html` | 13,5 Ko (+ 26,9 Ko) | 58 157 | 94 | 96 | 90 | 90 % |
| V3 `DX10_Addison_V3_expert.html` | 19,9 Ko (+ 56,6 Ko) | 97 729 | 98 | 98 | 92 | 97 % |
| V4 `DX10_Addison_V4_leger.html` | 9,6 Ko (+ 24,7 Ko) | 48 696 | 93 | 95 | 86 | 91 % |

**Contrôles communs.** (a) Le script ne trouve, dans aucune version, de nombre absent de l'ORIGINAL. (b) Toutes les citations AIPS entre « » sont conformes aux sept textes du corpus (23533, 31095, 31723, 54949, 57970, 62068, 68226) ; V3 porte de nouveau « corticosurrénale ». (c) Les 7-grammes communs avec la Phase A tombent à 0,7 % (V1), 1,9 % (V2), 1,6 % (V3) et 1,3 % (V4). `audit_langue.py` compte 29, 9, 21 et 6 phrases de plus de 35 mots, et 129, 63, 98 et 60 phrases à point-virgule. Aucun fichier ne contient de JavaScript, de `title=` ni d'espace insécable, et chaque fenêtre a son déclencheur. Les deux lacunes héritées demeurent, faute de source dans l'ORIGINAL : la zonation du cortex et la conduite chiffrée de l'hypoglycémie de l'adulte.

**V1.**
- Corrigé : la mère du cas 1 et le lymphome biopsié suivent l'ORIGINAL ; les 14 pièges se déplient en question-réponse ; le schéma chirurgical AIPS de Solu-CORTEF® figure dans les règles de stress.
- Erreurs restantes (mineures) : trois liens de cause inventés. « l'hydrocortisone parentérale, car ses soignants sont formés », « Aucune source ne prévoit l'arrêt […], car une interruption soudaine… » (l'ORIGINAL juxtapose et précise « consultée ») et « si bien que la prudence s'impose » (la prudence de l'AIPS de Plenadren® vise la dose).
- Manques : la fiche reste la plus dense (29 phrases de plus de 35 mots). La vitesse d'injection et la dose minimale de Solu-CORTEF® sont renvoyées à la Phase A, qui les contient. Les AIPS n'ont pas d'URL.

**V2.**
- Corrigé : les cinq erreurs relevées, la définition, les exposants ambigus et les liens (28 sources cliquables). Les 14 pièges, la lymphocytose, Waterhouse-Friderichsen, l'APS1, l'anti-TPO, la densité osseuse, le sujet âgé, le diabète et les vaccins sont rétablis.
- Erreurs restantes : le même lien inventé « Aucune source ne prévoit l'arrêt […], car… » ; « une dose inadaptée se traduit par un sous-dosage ou un surdosage » est une tautologie.
- Manques : données suisses de crise (4,4 pour 100 années-patients, carte 94,6 %, réserve 57,1 %) et 6 % de crises mortelles ; seuil bernois de 140 nmol/L ; alternatives au Synacthène ; réserve de Synacthen® dans l'asthme ; coloscopie ; numéros 31723 et 54949 ; sevrage ; DAX1 et MC2R.

**V3.**
- Corrigé : les points 1 à 4 de la recommandation (« corticosurrénale », contre-indications d'Alkindi® et de Plenadren® et dose d'Alkindi® en HCS mot pour mot, phrase non sourcée et deux liens inventés supprimés, Solu-CORTEF® réduit avec renvoi vérifié). Le point 5 l'est en partie, et le point 6 ne l'est pas, faute de source dans l'ORIGINAL.
- Erreurs restantes (mineures) : « Aucune source consultée ne prévoit l'arrêt […], car… » est un lien inventé. « Le syndrome mélanodermique commence souvent par un bronzage persistant que remarque un proche » généralise un signe fonctionnel (« le patient ou un proche »). « C'est la mère qui l'a vu » doit s'accorder en « vue ».
- Manques : le syndrome de sevrage, les métastases chez 40 à 60 % des cancers disséminés et le schéma ESE « 100 mg à l'induction, puis 200 mg/24 h ». Le dépliant « inducteurs du CYP3A4 » insère encore une phrase entière au milieu d'une phrase.

**V4.**
- Corrigé : les cinq erreurs de compression et les défauts mineurs. La définition reprend mot pour mot l'« usage des mots » de l'ORIGINAL, qui contient aussi la nuance d'Endo-ERN. Le reproche sur « Ne pas administrer des doses inférieures à 25 mg par jour » ne tient pas, car l'AIPS 23533 le place dans le paragraphe « Enfants et adolescents ».
- Erreurs restantes : « Maladie cœliaque, tuberculose : elles coexistent souvent avec l'ISP » est inexact pour la tuberculose, qui est une cause. Le « Sinon » de la partie 9 rend la phrase illogique. La liste des sources promet des liens que les articles n'ont pas, et deux exposants restent collés (« B12¹⁷ », « APS1¹⁶ »).
- Manques : anti-TPO, anti-transglutaminase tous les 3 ans, ferritine, densité osseuse, plage AIPS de Florinef®, règle des 16–18 ans, 140 nmol/L, alternatives au Synacthène, Kearns-Sayre. La fiche omet aussi la règle « doubler la dose en cas de fièvre », qui ne figure qu'en fenêtre et en piège.

**Règles complémentaires de Vial.** Les quatre fiches sont grammaticales et liées par des connecteurs, mais V1 reste lourde par la longueur des phrases. La prise en charge est complète dans la fiche pour V1, V2 et V3 ; V4 y omet la règle de fièvre. Tout approfondissement s'ouvre par un clic dans les quatre versions. Aucun résumé ne change plus une dose ni une conduite, mais chaque version garde un à trois liens de cause ou approximations.

**Version recommandée : V3** (98, 98, 92 ; couverture 97 %). Elle a le meilleur plan, la meilleure lisibilité, la prise en charge la plus complète dans la fiche et des citations AIPS exactes. Il reste à remettre le « ; » de l'ORIGINAL sur l'arrêt de la substitution, à rétablir « le patient ou un proche » et l'accord « vue », à ajouter le sevrage, les 40 à 60 % et le schéma ESE, et à sortir la phrase du dépliant CYP3A4.

**Meilleur compromis taille/couverture.** Pour l'objectif de Vial (95 à 100 % des notions, au moins 95/95), V3 est le meilleur compromis, car c'est la plus petite version qui l'atteint (76,5 Ko de texte, contre 80,2 Ko pour V1). Pour un seuil de 90/90, V4 donne le meilleur rendement : 34,3 Ko de texte pour 93/95 et 91 % de couverture. Le plancher de 60 Ko proposé plus haut ne tient donc plus. Le seuil de 90/90 s'atteint vers 35 Ko de texte (49 Ko de fichier), alors que 95/95 et 95 % de couverture exigent environ 75 Ko de texte.

## Notation V5 et V6 (évaluation indépendante du 30.10.2026, même barème, mêmes contrôles a, b, c)

Lecture seule de V5 et de V6 ; seule cette section est ajoutée. La méthode est celle de la notation après révision. T est lu dans `id="taille"`, et `harnais/taille_xy.py` redonne les mêmes valeurs. La couverture vient du même script, sur les mêmes 145 notions. Ce script redonne à l'identique V1 98 %, V2 90 %, V3 97 % et V4 91 %, et `audit_langue.py` redonne leurs comptes de phrases.

| Version | T = x (+ y) | Fichier (octets) | Examen /100 | PEC /100 | Lisibilité /100 | Couverture des notions |
|---|---|---:|---:|---:|---:|---:|
| V5 `DX10_Addison_V5_norme.html` | 18,3 Ko (+ 57,7 Ko) | 99 177 | 99 | 99 | 94 | 99 % |
| V6 `DX10_Addison_V6_fiche_V2_fenetres_V3.html` | 14,1 Ko (+ 53,1 Ko) | 94 521 | 96 | 96 | 87 | 94 % |

**Contrôles communs.** (a) Le script ne trouve aucun nombre absent de l'ORIGINAL. Il ne relève que la ligne de taille, les numéros de sous-parties de V5 et, dans V6, des exposants accolés. (b) Toutes les citations AIPS entre « » sont conformes aux sept textes du corpus, une fois les espaces normalisées. Les citations de l'OIC-DFI et de la liste des spécialités reprennent l'ORIGINAL. V5 donne les sept numéros Swissmedic, V6 six (54949 manque). (c) Les 7-grammes communs avec la Phase A valent 1,7 % (V5) et 1,1 % (V6) ; le même calcul redonne 4,9 % pour l'ORIGINAL. `audit_langue.py` compte 11 et 24 phrases de plus de 35 mots, puis 73 et 100 phrases à point-virgule. Aucun fichier ne contient de JavaScript, de `title=` ni d'espace insécable. Chaque fenêtre a son déclencheur, et seule leur barre de titre reste collante. Les deux lacunes héritées demeurent (zonation du cortex, hypoglycémie chiffrée de l'adulte). `audit_langue.py` classe toujours les deux fichiers non conformes au format de production (FIN_FICHIER, h2, h3).

**V5 « norme ».**
- Forces : toutes les erreurs relevées pour V2 et V3 sont corrigées. Le « car » sur l'arrêt devient « et », la tautologie de la dose inadaptée et l'accord « vue » disparaissent, et le dépliant CYP3A4 sort de la phrase. Le sevrage, les 40 à 60 % de métastases et le schéma ESE de chirurgie sont rétablis. La fiche donne toute la conduite chiffrée : urgence de l'adulte et de l'enfant par âge, glucose, relais à 40 mg/j, traitement de fond, règles de stress et grossesse.
- Erreurs restantes (mineures) : « Le patient ou un proche note souvent » ajoute « souvent » à l'ORIGINAL. « Centre de catégorie A ou B » perd « de formation ». En 11.1, le paragraphe « Il prélève… » suit le paragraphe Enfant sans antécédent clair. [S25] figure dans la liste sans appel dans le texte.
- Manques : la règle AIPS du test chez l'allergique (« jamais reçu » d'ACTH), les effets indésirables de l'hydrocortisone, les prix, le remboursement de Synacthen® et les pompes. La fenêtre Solu-CORTEF® recopie encore la durée de 48 à 72 h, déjà dans la Phase A et dans la fenêtre d'urgence. Enfin, y (57,7 Ko) dépasse de 2,7 Ko la cible de 45 à 55 Ko de la norme.

**V6 « fiche V2 + fenêtres V3 ».**
- Forces : la fiche est la plus courte des versions complètes (14,1 Ko, 13 minutes). Les fenêtres sont réécrites en prose liée et sourcées, les 28 sources sont cliquables, et Solu-CORTEF® se réduit à la vitesse et au schéma chirurgical.
- Erreurs restantes : trois erreurs déjà relevées reviennent par la fusion. Ce sont « Aucune source consultée ne prévoit l'arrêt […], car… », « c'est la mère qui l'a vu » et « une dose inadaptée se traduit par un sous-dosage ou un surdosage ». « Le scanner a montré un lymphome » omet la biopsie. L'arbre conclut à une forme secondaire « si l'ACTH est basse ou normale », sans le cortisol bas. Le dépliant « contre-indique » (Euthyrox®) coupe encore une phrase. Enfin, 10 exposants sont accolés à un nombre (« 2,5⁴ʼ¹⁶ʼ²² » se lit 2,5⁴), et ACTH, ESE, NICE, BSPED, LC-MS/MS, HbA1c et TSH ne sont jamais développés.
- Manques : le sevrage, les 4,4 crises pour 100 années-patients en Suisse, les 7 % de crises sans cause, le schéma ESE de chirurgie, le sel non restreint, la citation AIPS de Synacthen® sur l'asthme et le n° 54949. La fiche ne donne ni les doses d'urgence de l'enfant par âge (un seul exemple, à 4 ans), ni la glycémie, ni le relais oral, ni la grossesse.

**Règles complémentaires de Vial.** Les deux fiches affichent leur taille, mais le script écrit « 18.3 » avec un point. V5 respecte toutes les règles : fiche grammaticale et liée, prise en charge complète dans la fiche, approfondissement par clic (31 fenêtres, 19 dépliants), aucun résumé qui change le sens, erreurs relevées corrigées et couverture de 99 %. V6 ne respecte pleinement que la taille et l'approfondissement par clic (31 fenêtres, 15 dépliants). Sa partie 7 reste une liste, et sa fiche renvoie en fenêtre l'enfant, la glycémie, le relais et la grossesse. Elle compresse trois énoncés : la biopsie, l'arbre, puis « l'endocrinologue pédiatre » pour la pédiatrie bernoise. Ses erreurs relevées restent, et sa couverture (94 %) reste sous 95 %.

**Classement final des six versions.** L'ordre suit l'objectif de Vial : d'abord la couverture et les notes d'examen et de PEC, ensuite la lisibilité.

| Rang | Version | Examen | PEC | Lisibilité | Couverture | Texte x + y |
|---:|---|---:|---:|---:|---:|---:|
| 1 | V5 « norme » | 99 | 99 | 94 | 99 % | 76,0 Ko |
| 2 | V3 « expert » | 98 | 98 | 92 | 97 % | 76,5 Ko |
| 3 | V1 « sans redondance » | 98 | 98 | 89 | 98 % | 80,2 Ko |
| 4 | V6 « fiche V2 + fenêtres V3 » | 96 | 96 | 87 | 94 % | 67,2 Ko |
| 5 | V2 « court » | 94 | 96 | 90 | 90 % | 40,4 Ko |
| 6 | V4 « léger » | 93 | 95 | 86 | 91 % | 34,3 Ko |

V6 passe devant V2, car elle tient 95/95, ce que V2 ne fait pas, malgré une lisibilité plus basse.

**Version recommandée comme modèle : V5.** Elle obtient les meilleures notes des six versions et la couverture de l'ORIGINAL (99 %), avec moins de texte que V3 et V1. Sa fiche est aussi la plus complète en prise en charge, et elle ne contient aucune erreur de dose, de seuil ni de conduite. Elle tient la norme du compte rendu (x ≤ 20 Ko, au moins 95/95, lisibilité ≥ 85), sauf y, qui dépasse de 2,7 Ko. Avant de la généraliser, il faut retirer « souvent », rétablir « de formation » et donner un sujet au paragraphe « Il prélève… ». Il faut aussi citer ou retirer [S25] et réduire la fenêtre Solu-CORTEF® à la vitesse et au schéma chirurgical. Enfin, la règle AIPS du test chez l'allergique et les effets indésirables de l'hydrocortisone doivent être ajoutés. V6 montre qu'une fusion par script réimporte les erreurs déjà corrigées : la production doit partir de V5.
