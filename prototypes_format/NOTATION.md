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
