# Passation de recherche — LOT 1, SSP G1

## État véridique

- La recherche ciblée est terminée pour cette invocation ; elle est suffisante pour lancer la rédaction medium, sans certifier l’exhaustivité de la littérature.
- `selection.json` contient dix diagnostics mûris ; `complete=false` reste impératif tant que la rédaction entière de l’Appel A n’est pas terminée.
- Aucun `Appel_A.html` final n’a été généré, aucun audit n’a été fait, aucun dépôt ou push n’a été effectué. B1…B5 restent bloqués.
- Le message root demandant l’arrêt high→medium est arrivé après une opération qui a créé `build_appel.py`. Ce fichier est un **brouillon interne non final et non validé**, avec une proposition des 14 points. Il n’a pas été exécuté pour générer HTML. La rédaction medium doit le reprendre, réécrire et corriger selon ses propres vérifications ; ne pas le déclarer cours terminé. Sa syntaxe Python seule a été vérifiée via `ast.parse`.
- Le brouillon contient le début HTML et les 14 points, mais **pas le Bloc 2, pas la bibliographie rendue, pas la fermeture du document ni FIN_FICHIER**. Il fait 84 166 octets en tant que script, ce qui ne dit rien de la taille d’un HTML final. Ne pas gonfler artificiellement.
- `PROMPT_V7.md` a été lu intégralement. L’index suisse et les 1 388 lignes du questionnaire de corrections ont été lus par segments. L’ancien Appel A a été exploré comme matière, jamais comme preuve, et ses catégories ont été remplacées par la sélection ci-dessous.
- La date a été vérifiée : 23.10.2026 23:30 UTC correspond au 24.10.2026 01:30 Europe/Zurich. Les dates de consultation du 24 sont donc exactes.

## Fichiers disponibles

- `evidence.json` contient 23 sources, avec URL, titre, extraits réellement reçus, date et portée.
- `research_primary_raw.json` conserve les extractions sources, dont certains documents intégraux. Il reste **interne**, ne pas publier ni redistribuer ces textes ; publier seulement un index/extraits bornés si nécessaire.
- `research_raw.json` conserve une première série de recherches ; `existing_text.tmp` est une extraction interne de l’ancien fichier et n’est pas une preuve.
- `HELP.json` formule huit questions ciblées avant audit externe, sans prétendre être un résultat d’audit.
- `selection.json` fixe noms, ordre et justifications. Les sources DX.10 doivent être complétées par S19 (la recommandation espagnole2021, ouverte) plutôt que de se reposer sur l’abstract ESH2020 seul.

## Liste à conserver identique dans A et B

1. DX.1 — Hypoglycémie.
2. DX.2 — Hyperhidrose focale primaire.
3. DX.3 — Hyperhidrose médicamenteuse.
4. DX.4 — Symptômes vasomoteurs de la périménopause et de la ménopause.
5. DX.5 — Hyperthyroïdie.
6. DX.6 — Endocardite infectieuse.
7. DX.7 — Tuberculose active.
8. DX.8 — Infection par le VIH.
9. DX.9 — Lymphome de Hodgkin.
10. DX.10 — Phéochromocytome fonctionnel.

Le critère désiré par V7 est fréquence suisse pondérée par gravité, mais les sources ouvertes ne fournissent **aucune série suisse comparable des dix causes**. Il faut le dire, refuser un faux classement statistique et présenter cet ordre comme pédagogique. DX.1 vient d’abord pour l’urgence ; DX.2–5 couvrent des phénotypes reconnaissables et modifiables ; DX.6–9 imposent de ne pas banaliser les signes généraux ; DX.10 a sa filière urgente dès le triage malgré son dixième rang pédagogique. Tous les badges disent « Ne rang — fréquence non quantifiée (Suisse) ». Aucun pourcentage de fréquence parmi les consultants suisses n’est disponible.

Le SCA, le stress thermique/coup de chaleur et les toxidromes restent au **triage urgent hors classement**. Les lymphomes non hodgkiniens restent des différentiels explicites du Hodgkin, sans unifier toute hémopathie dans une monographie. Le syndrome d’apnées obstructives et le trouble panique restent des possibilités hors dix, avec leurs indices propres (sommeil/ronflement/somnolence ; accès d’angoisse). Une limite à dix ne doit jamais être annoncée comme liste exhaustive. Les formes neurogènes, l’anhidrose et les anomalies qualitatives sont développées dans le SSP et hors dix ; ne pas les effacer parce que les dix monographies ciblent surtout l’excès de sueur.

## Sources décisives et corrections de sécurité

- **S3 AWMF/DDG2023**, document direct ouvert et sections pertinentes lues : glandes normales surstimulées ; transmission sympathique cholinergique ; aucun seuil de débit universel prouvant/excluant ; Minor cartographie et n’est pas quantitatif ; gravimétrie habituellement sur5min ; HDSS1–4 ; pas de bilan de routine dans un profil primaire typique. Le tableau3 HDSS doit être traduit en indiquant que la traduction est pédagogique, non une validation nouvelle. Le tableau1 ne reproduit pas littéralement le schéma6mois+2/6 ; **ne pas lui attribuer cette citation**.
- **S5 HUG2016**, entier texte extrait lu : présente6mois+2/6, bilan FSC/CRP/VS/TSH/radiographie/VIH si pas de piste. Source ancienne, avec une bibliographie dont certains items sont américains ; elle vaut enseignement suisse institutionnel mais ne doit pas être transformée en guideline nationale2026 ni utilisée pour les doses. Les AIPS priment sur Ditropan etc.
- **S6 Cohorte française2022** :420patients d’un centre hospitalier,119cancers,44infectieux,33médicamenteux,70sans diagnostic. Ne transposer aucun pourcentage en Suisse ou soins primaires. Le seuil exploratoire CRP5,6mg/L ne doit pas devenir un seuil suisse universel.
- **S7 HUG2025 hypoglycémie** : seuil d’action patient<4mmol/L ;15g glucides alimentaires immédiatement. C’est un conseil alimentaire CH, pas une dose de médicament AIPS.
- **S8 AIPS GlucaGen® Novo Nordisk31489**, novembre2021, numéro lu dans texte : adulte1mg IM/SC ; enfant>25kg ou>6–8ans1mg,<25kg ou<6–8ans0,5mg ; réponse normalement10min, puis glucose IV si non-réponse ; glucides après réponse pour glycogène. CIphéochromocytome ; inefficacité possible réserves épuisées/alcool/jeûne ; grossesse possible. Ne pas confondre doses diagnostiques gastro-intestinales et secours.
- **S22 AIPS Glucosum Bichsel32920** : perfusions usuelles et voie centrale préférée pour20–50%, mais aucun bolus de secours précis pertinent retrouvé. Le root a également recherché et confirmé la lacune. **Ne jamais attribuer15–20g ou75–100mL G20% à cette AIPS, ni copier JBDS/HUG/DiabèteVaud comme si AIPS.** HELP A-H02 reste ouvert.
- **S9 AIPS Axhidrox®69243**, février2024 : adulte hyperhidrose axillaire primaire sévère ; une pression270mgcrème=2,2mgglycopyrronium ; **deux pressions par aisselle**, soit4,4mg ; quotidien4semaines puis possible2fois/semaine dès5esemaine ; capuchon applicateur, pas doigts ;31traitements maximum par flacon. DFGe<30mL/min/1,73m² : bénéfice/risque et surveillance ; pas d’ajustement hépatique ; données<18ans/>65ans non établies ; grossesse peut être envisagée si nécessaire, allaitement décision individualisée/contact enfant évité. Une interdiction absolue en grossesse serait fausse.
- **S10 AIPS BOTOX®52433**, mai2025, numéro lu : indication suisse **hyperhidrose axillaire primaire adulte** (ne pas importer le libellé européen sévère/réfractaire comme indication exacte suisse) ;50UAllergan/aisselle,100U/4mL,intradermique,sites1–2cm ;pas avant16semaines ;effet4–7mois selon notice. SNAP-25 clivée → libération présynaptique ACh inhibée. La revue2026 dit improprement « bloque récepteurs » : **AIPS prime**. Les unités ne s’interchangent pas entre toxines ; palmaire/plantaire hors indication de la notice. Grossesse sauf nécessité absolue ; allaitement non recommandé. Précautions neuromusculaires, aminoglycosides, dysphagie/dyspnée.
- **S11 Guide suisse TB V1.2024**, remplace2021 : premier échantillon pour amplification moléculaire rapide ; second si contexte/forte probabilité ou selon filière ; culture/résistances. **Ne pas recopier « trois crachats obligatoires » du questionnaire ancien**. IGRA ne prouve pas maladie active et un négatif ne l’exclut pas. Isolement décidé avec probabilité/PCR/traitement/clinique ; ne pas inventer une levée à trois microscopies négatives. Les sections6.2,6.3,7.5 doivent être relues dans le brut avant précision finale.
- **S12 OFSP Dépistage VIH directive2025 version4 du10.07.2026** :>18mois ;fenêtre6semaines test4egénération ;primo-infection symptomatique→test automatisé≥4egénération **et moléculaire en parallèle**,pas test rapide. Le diagnostic repose sur confirmation selon laboratoire, pas sur sueur ni dépistage réactif seul.
- **S13 Aide Suisse contre Sida** : sueurs nocturnes fortes,fièvre,éruption,adénopathies etc. soutiennent la reconnaissance, pas un diagnostic clinique.
- **S14 ESE ménopause2025** : pas de dosage systématique>45ans si clinique typique ;ménopause absence de règles>1an ;POI<40ans ;ESE2025 indiqueFSH>25UI/L unique ou répétition si doute. **Ne pas réinjecter automatiquement « deux dosages obligatoires » de l’ancien audit**, devenu trop rigide. Une contraception/hystérectomie modifie la lecture clinique. Le brut comporte la définition et les recommandations.
- **S15 ETA2018 Basedow** : profil hormonal,anticorps récepteur TSH,échographie ;storm atteinte multiviscérale urgente. Recherche ciblée n’a pas établi un remplacement général plus récent ; ne pas certifier « dernière version2026 » sans complément.
- **S16 ESC endocardite2023** :≥3séries hémocultures30min avant antibiothérapie chez stable ;ne pas attendre pic fébrile ;absence fièvre/souffle n’exclut pas ;en choc ne pas retarder stabilisation/traitement pour remplir un intervalle mécanique. **Correction2025signalée mais non lue**→HELP.
- **S17 ESC SCA2023** : ECG au plus vite avec cible10min depuis premier contact médical ;troponines essais/temps spécifiques ;sueurs avec douleur/dyspnée/malaise ouvrent filière. Pas de doses médicamenteuses extrapolées.
- **S18 ESMO Lymphomas2025**, publié en ligneaoût2025 : diagnostic sur biopsie chirurgicale si possible,tissu pourhistologie/IHC/moléculaire ;TEP-TDM selon entité. Remplace l’usage isolé2018. Pour seuils « B », vérifier la section exacte avant inclusion ; ne jamais écrire que les trois signes sont tous obligatoires.
- **S19 Recommandation multidisciplinaire espagnole PPGL2021**, ouverte : métanéphrines libres plasmatiques ou urinaires fractionnées,conditions de posture/médicaments ;dosage avant imagerie hors découverte incidente ;alpha avant bêta. L’ESH2020direct ne donnait qu’abstract accessible ; utiliser S19 pour contenu opératoire, sans fausse lecture complète ESH.
- **S20 OFSP chaleur** :facteurs de risque,refroidissement,lieu frais,144si pas d’amélioration ;ne pas faire boire personne incapable d’avaler. Pas de protocole intensif minuteparminute entièrement vérifié.
- **S21 Revue allemande2026**, consulteAWMF2023,pas recommandation universelle ;prévalence primaireAllemagne4,6%,Suède5,5%. Ce sont des études de population, pas fréquences parmiconsultants CH ;les traitements étrangers n’équivalent pas à des autorisations suisses.
- **S23 HUGtox2025** :Hunter/exposition sérotoninergique,clonus/hyperréflexie/diaphorèse ;arrêt médicaments incriminés+support ;syndrome malin neuroleptiques→rigidité/hyperthermie/altération mentale. Ne pas déduire un toxidrome d’une sueur seule.

## Plan des14points à finaliser medium

1. Définir hyperhidrose,diaphorèse,hypon/anhidrose,odeur/couleur,primaire/secondaire ;séparer description et diagnostic.
2. Donner les rares chiffresCH/UE en nommant population et limites ;mettre l’épidémiologieCH manquante dansHELP.
3. Expliquer thermorégulation et voie cholinergique ;table perturbation→exploration→correction ;aucun schéma moléculaire ajouté de mémoire.
4. Triage avant fréquence,puis4contrastes discriminants ;ne pas banaliser symptômescardiaques ou neurotoxiques.
5. Anamnèse avec raison de chaque question et action desdrapeauxrouges.
6. Examen régionparrégion,normal avantpathologique ;ne pas inventer sensibilité/spécificité des manœuvres.
7. Syndromes numérotés avec signesfonctionnels/physiques séparés,mécanisme,technique ;lier à fenêtres du glossaire.
8. Critèresformeprimaire etHDSS,attribution exacte ;ne pas faire duSSP un diagnostic avec seuilunique.
9. Souspoints9.a–d :référencequestiondépendante,premièreintention,alternativessituationsspéciales,deuxièmeintention ;tableauxinterprétationpositif/négatif/limite/discordant ;certainsintervalleslocaux restentHELP.
10. Arbre avec signes/résultatsàchaquebranche ;garderunedécisionsuivistableinexpliqué.
11. Souspoints11.A–D,fenêtresurgentes,dosesAIPSautorisées,effets/précautions,situationsspéciales,sortie etsurveillance ;ne pas masquer leslacunesparun faux protocolecomplet.
12. Prévention3niveaux,cause/médicaments/chaleur/transmission/handicap ;pasdevaccinationG1inventée.
13.3–6phrasesdécisionnellessanscopier8ou11.
14. Questionsconstruites,explicitementnonofficielles,réponsesetsources ;pasdepromesse90–100%examen.

Bloc2 manquant dans brouillon :dixjustificationsavecchoixexclusions,tableau10lignes signeclé/examenclé/mécanisme/conduiteimmédiate,algorithmediscriminant puis sourcesnumérotées. Les noms exacts de `selection.json` restent canoniques.

## Contraintes techniques à appliquer

Contrat root :`<article data-monograph="G1">` et14`<section data-point="1">…14` ;`data-subpoint="9.a"…"9.d"` et`"11.A"…"11.D"`. Le brouillon possède ces attributs. Chaque tableau est enveloppé dans`<div style="overflow-x:auto;">`. Pasdescript,image,feuilleexterne,title= ;respect390px etlongueurlignes<3000 ;sources[Sn]etmention nonvalidation ;`<!-- FIN_FICHIER LOT_1_APPEL_A -->`final. Mettrechaquetermetechniquedansunefenêtreouuneréférencefenêtreappropriée ;le brouillon n’est **pas encore exhaustif** sur ce point. Vérifier phrasesverbales jusque dans tableaux, titres exceptés lorsqu’ils suivent le gabarit imposé.

Le moteur `build_appel.py` contient du texte potentiellement utile mais n’est pas le livrable. Le résultatdoitêtre`Appel_A.html`. Une taille correcte ne constitue pas une preuve de complétude. `complete=true` signifie rédaction réellement achevée,aucuneauditautodécerné. Si des obligations substantielles restent non satisfaites,laisser`complete=false`etnommerexactement lesmanques.

## Accès et honnêteté

Les extractions primaireCH/UE ont fonctionné. Une ancienne URL AideSuissecontreSida a retourné404 ;la bonne page a été trouvée par recherche. Une requêteAIPSerronée a retourné«Aucunrésultat»,sans être exploitée ;les numéros repris dans cours sont ensuite lus dans les notices exactes. Aucun refus réseau de sécurité n’a été reçu,aucun contournement n’a eu lieu. L’ESH2020 n’a offert que l’abstract dans l’accès direct ;la recommandationeuropéenne espagnole2021 a donc servi de source détaillée distincte.

La prochaine action est la rédaction medium, puis les contrôlesstructurels et la préparation pourl’auditexterne Tunder demandé par utilisateur. Ne pas commencerBavantAchèvementréeld’A ;ne pas publier le brut des sources.
