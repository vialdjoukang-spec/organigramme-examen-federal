# -*- coding: utf-8 -*-
# Banque G1 — chaque item: correct listé en premier dans opts; position finale fixée par KEYS.
A="../../../repo/LOT_Claude_Finaux/LOT_001/LOT_001_Phase_A_V0.html"
def B(n,p): return (f"../../../repo/LOT_Claude_Finaux/LOT_001/LOT_001_Phase_B_V0_DX.{n}.html#dx{n}-p{p}", f"Phase B DX.{n} §{p}")
def PA(sec,label): return (f"{A}#{sec}", f"Phase A {label}")

Q=[]
def q(bloc,dx,tache,setting,stem,question,opts,why,pearl,src,pol="positive",niv="examen",spe=None,media=None):
    Q.append(dict(bloc=bloc,dx=dx,tache=tache,setting=setting,stem=stem,question=question,
                  opts=opts,why=why,pearl=pearl,src=src,polarite=pol,niveau=niv,specialite=spe,media=media))
# opts = [(texte, pourquoi_pas)] ; opts[0] = bonne réponse (pourquoi_pas ignoré)

# ───────────── BLOC 1 · RAISONNER (Phase A, avant de nommer le DX)
q("R","E1 · DX.4","assessment_diagnosis","EMS",
 "Un homme de 81 ans, résident d'un EMS, est retrouvé par l'infirmière pâle, couvert de sueurs et confus vers 10 h. Il est diabétique de type 2 sous insuline. Il respire normalement, pouls 96/min, PA 138/82 mmHg. Il n'a pas pris son petit déjeuner.",
 "Quel est le premier geste le plus approprié ?",
 [("Glycémie capillaire immédiate",""),
  ("ECG 12 dérivations","Utile ensuite si oppression ou glycémie normale ; ne précède pas une glycémie corrigible en minutes."),
  ("Température centrale mesurée","Pertinente, mais la confusion sudorale du diabétique traité impose d'abord le glucose."),
  ("Hémocultures en deux paires","Réservées à la fièvre avec défaillance (E2) ; aucun argument infectieux ici."),
  ("Dosage de la TSH sérique","Thyrotoxicose = E5 ; jamais avant d'avoir écarté l'hypoglycémie (E1).")],
 "Pâleur + sueur + confusion chez un diabétique sous insuline = hypoglycémie jusqu'à preuve du contraire (E1). La glycémie capillaire tranche et se corrige en minutes.",
 "Si la mesure est impossible, traiter sans attendre le résultat. Une glycémie normale ne clôt rien : penser cœur, infection, toxique, chaleur.",
 PA("ssp-p10","§10 Arbre, nœuds 0 et 3"))

q("R","hors liste · SCA","management","cabinet",
 "Un homme de 64 ans, diabétique depuis 15 ans, consulte au cabinet pour des sueurs profuses apparues il y a 40 min au repos, avec nausées et « oppression » mal définie, sans douleur thoracique franche. Glycémie capillaire 7,4 mmol/L. PA 150/90 mmHg, pouls 92/min.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("ECG 12 dérivations interprété dans les 10 minutes",""),
  ("Troponine unique, puis retour à domicile si normale","Une première troponine normale ne rassure pas ; l'ECG passe avant."),
  ("Anxiolytique et réévaluation dans 1 heure","Attribuer la sueur à l'anxiété fait manquer l'ischémie."),
  ("Holter ECG de 24 heures en ambulatoire","Délai incompatible avec un SCA possible."),
  ("Dosage de la TSH et de la fT4","Ne répond pas à l'urgence coronarienne.")],
 "La sueur peut être le seul signe d'ischémie, surtout chez le diabétique âgé. Oppression/dyspnée + sueur = filière coronarienne, ECG en 10 min (hors liste, avant E1).",
 "Sus-décalage persistant : reperfusion sans attendre la troponine ; jamais de retour seul.",
 PA("ssp-p4","§4 Démarche, drapeaux rouges"))

q("R","DX.5 vs DX.10","assessment_diagnosis","cabinet",
 "Une femme de 34 ans consulte pour une transpiration qui la gêne au travail. Vous cherchez l'élément d'anamnèse qui doit vous faire quitter l'hypothèse d'une hyperhidrose primaire.",
 "Quel élément impose le plus fortement de rechercher une cause secondaire ?",
 [("Réveils nocturnes avec draps trempés",""),
  ("Début des symptômes à l'âge de 16 ans","Début ≤ 25 ans = critère de forme primaire."),
  ("Atteinte palmaire bilatérale et symétrique","Profil focal symétrique typique du primaire."),
  ("Mère présentant la même sudation","Agrégation familiale (30–65 %) : critère primaire."),
  ("Gêne pour serrer la main des clients","Retentissement fonctionnel : critère primaire, pas un signe secondaire.")],
 "La forme primaire cesse pendant le sommeil ; l'absence de sueur nocturne est un des 7 critères. Une nuit mouillée oriente vers fièvre, ménopause, tumeur (OR 23,2).",
 "Nocturne, généralisée, asymétrique ou début > 25 ans → bilan secondaire.",
 B(5,14))

q("R","mécanisme","mechanisms","urgences",
 "Une femme de 41 ans est vue aux urgences pendant un accès de 15 min : sueurs, céphalée, palpitations. La peau des extrémités est froide et pâle. Pouls 124/min.",
 "Quel mécanisme explique le mieux cet aspect cutané pendant l'accès ?",
 [("Décharge sympathique catécholaminergique avec vasoconstriction",""),
  ("Déplacement de la consigne thermique par les cytokines","Mécanisme de la fièvre : peau chaude, frissons."),
  ("Vasodilatation par les amines tumorales","Flush carcinoïde : peau rouge, sèche."),
  ("Signalisation NK3 hypothalamique","Bouffée ménopausique : peau chaude et rouge, humide."),
  ("Surstimulation focale de glandes eccrines normales","Hyperhidrose primaire : focale, sans pâleur ni tachycardie.")],
 "Pendant un accès, peau froide et pâle = décharge sympathique (phéochromocytome, panique) ; peau chaude et rouge = vasodilatation (ménopause, carcinoïde).",
 "Triade céphalée-palpitations-sueurs + pâleur : métanéphrines, pas d'étiquette « panique » d'emblée.",
 PA("ssp-p6","§6 Examen physique"))

q("R","hors liste · coup de chaleur","management","autre (chantier)",
 "Un ouvrier de 58 ans travaille sur un chantier pendant une canicule. Il prend de l'oxybutynine. Ses collègues l'amènent car il tient des propos incohérents. La peau est chaude et sèche, sans sueur.",
 "Quelle est la conduite immédiate la plus appropriée ?",
 [("Appel du 144 et refroidissement immédiat",""),
  ("Paracétamol IV puis réévaluation à 1 heure","Les antipyrétiques ne corrigent pas l'hyperthermie du coup de chaleur."),
  ("Hémocultures puis antibiothérapie empirique","Retarde le refroidissement ; le contexte est thermique."),
  ("Hydratation orale et retour au domicile","Confusion = trouble neurologique : urgence vitale."),
  ("Antitranspirant et conseils d'hygiène","Jamais d'antitranspirant sur une peau qui ne transpire plus.")],
 "Sans sueur, la température centrale monte sans frein (anhidrose, ici aggravée par un anticholinergique). Chaleur + trouble neurologique = 144 et refroidissement.",
 "L'absence de sueur à la chaleur n'est jamais rassurante. Cible Suva : < 40 °C en 30 min.",
 PA("ssp-p11","§11 Urgences hors liste"))

q("R","E2 · DX.9","management","EMS",
 "Une femme de 79 ans, en EMS, présente depuis la nuit des frissons et des sueurs. Température 39,1 °C (tympanique), confusion nouvelle, FR 24/min, PA 86/50 mmHg malgré 500 mL de cristalloïdes.",
 "Quelle est la conduite la plus appropriée ?",
 [("Hémocultures, antibiotique dans l'heure, hôpital",""),
  ("Paracétamol et réévaluation à 48 h","Un antipyrétique normalise la température sans fermer l'hypothèse ; défaillance présente."),
  ("Antibiotique oral, hémocultures si persistance","Prélever avant de traiter ; voie orale inadaptée au choc."),
  ("IGRA et radiographie thoracique ambulatoires","Hors sujet devant un choc."),
  ("Échocardiographie transthoracique en ambulatoire","N'est pas l'étape immédiate d'une défaillance.")],
 "Fièvre + défaillance (confusion, hypotension, FR ≥ 22) = E2. Prélever avant l'antibiotique (en < 30 min si choc), antibiotique dans l'heure, hospitaliser.",
 "Le qSOFA ne sert jamais seul à exclure un sepsis.",
 B(9,13))

q("R","DX.4 / DX.8","mechanisms","cabinet",
 "Une femme de 66 ans, diabétique sous insuline, prend du métoprolol pour une cardiopathie. Elle rapporte des épisodes de malaise avant le repas, avec glycémie capillaire mesurée à 3,2 mmol/L.",
 "Quel signe d'alerte de l'hypoglycémie est le plus atténué par son traitement ?",
 [("La tachycardie",""),
  ("La sueur","Commande cholinergique : non inhibée, parfois renforcée sous bêtabloquant."),
  ("La faim","Signe non masqué par le bêtablocage."),
  ("La confusion","Signe neuroglycopénique, non masqué."),
  ("La vision floue","Signe neuroglycopénique, non masqué.")],
 "Le bêtabloquant masque la tachycardie (et prolonge l'hypoglycémie sous insuline) ; la sueur, cholinergique, persiste : elle devient le signal clé.",
 "AIPS Inderal® : « ne doit pas être utilisé chez les patients qui ont tendance à faire des hypoglycémies ».",
 B(8,14))

q("R","sueurs nocturnes","assessment_diagnosis","cabinet",
 "Un homme de 47 ans consulte pour des sueurs nocturnes depuis 6 semaines. Pas de fièvre mesurée, poids stable, pas de toux, aucun nouveau médicament, alcool occasionnel. Examen complet normal, aucune adénopathie.",
 "Quel bilan de première intention est le plus approprié ?",
 [("Hémogramme, CRP et TSH",""),
  ("TEP-TDM corps entier","Jamais en dépistage ; réservé à la stadification d'un lymphome prouvé."),
  ("Biopsie ganglionnaire","Aucune adénopathie : pas de cible."),
  ("5-HIAA urinaire de 24 h","Réservé au flush sec avec diarrhée ou sibilances."),
  ("Métanéphrines libres plasmatiques","Réservées aux accès adrénergiques.")],
 "Sueurs nocturnes inexpliquées : hémogramme, CRP, TSH ; IGRA + radiographie si tuberculose plausible ; test VIH 4e génération selon le risque.",
 "Bilan négatif et stable : suivi programmé ; la disparition des sueurs ne ferme jamais une branche dangereuse.",
 PA("ssp-p9","§9.b Première intention"))

q("R","DX.5","assessment_diagnosis","cabinet",
 "Une femme de 22 ans consulte pour des paumes et des aisselles moites depuis l'âge de 14 ans, bilatérales, plusieurs fois par semaine, jamais la nuit. Sa mère a le même problème. Elle évite d'écrire au tableau. À l'examen, la peau est sèche.",
 "Quelle est la conduite la plus appropriée ?",
 [("Retenir une hyperhidrose primaire clinique et grader le HDSS",""),
  ("Bilan sanguin systématique (TSH, glycémie, hémogramme)","Tableau typique : aucun examen de routine (S1)."),
  ("Test de Minor pour confirmer le diagnostic","Le Minor cartographie un territoire, il ne pose pas le diagnostic."),
  ("Rassurer : l'examen sec exclut une maladie","La sueur survient par épisodes ; l'histoire prime."),
  ("Gravimétrie avec seuil obligatoire","Aucun seuil universel ; l'exiger est une erreur.")],
 "Sudation focale > 6 mois avec ≥ 4/7 critères suisses (ici bilatérale, ≥ 1/sem, pas nocturne, début ≤ 25 ans, famille, gêne) : diagnostic clinique (Se 99 %, Sp 82 %).",
 "Le HDSS initial fixe la cible ; réévaluer à 4 semaines.",
 PA("ssp-p8","§8 Diagnostic positif"))

q("R","DX.5","assessment_diagnosis","cabinet",
 "Un homme de 25 ans présente une hyperhidrose axillaire primaire typique. Avant de choisir le traitement, vous voulez documenter le retentissement initial pour pouvoir juger l'effet à 4 semaines.",
 "Quel outil est le plus approprié ?",
 [("Échelle HDSS",""),
  ("Test de Minor","Cartographie la zone active, sans mesurer la gêne."),
  ("Gravimétrie","Quantifie le débit, très variable, sans référence admise."),
  ("Hémogramme et CRP","Sans intérêt dans une forme primaire typique."),
  ("Dosage de la TSH","Pas d'indication devant un tableau primaire typique.")],
 "Le HDSS (1–4) mesure l'interférence avec les activités : 3–4 = forme sévère. C'est la cible du traitement.",
 "Minor = où ; gravimétrie = combien ; HDSS = à quel point ça gêne.",
 PA("ssp-p14","§14 Pièges"))

# ───────────── BLOC 2 · DISCRIMINER (vignettes → DX / examen / traitement)
q("D","DX.1","assessment_diagnosis","cabinet",
 "Une femme de 51 ans consulte pour des accès de chaleur brutale du visage et du haut du corps, suivis d'une sueur profuse, plusieurs fois par jour et la nuit, depuis 8 mois. Cycles irréguliers. Pas de diarrhée, poids stable, température normale, examen normal entre les accès.",
 "Quel est le diagnostic le plus probable ?",
 [("Symptômes vasomoteurs de la ménopause",""),
  ("Syndrome carcinoïde (tumeur neuroendocrine)","Flush sec, avec diarrhée aqueuse ou sibilances."),
  ("Hyperthyroïdie par maladie de Basedow","Thermophobie, amaigrissement, tachycardie de repos absents."),
  ("Phéochromocytome surrénalien","Accès avec pâleur, céphalée, palpitations, HTA."),
  ("Trouble panique avec agoraphobie","Accès de peur intense avec ≥ 4 symptômes, non décrit.")],
 "Bouffée « humide » (chaleur puis sueur) + cycles modifiés après 45 ans, sans signe général = symptômes vasomoteurs.",
 "Humide = ménopause ; sec = carcinoïde ; froid et pâle = phéochromocytome ou panique.",
 PA("algo","Algorithme, étape 10"))

q("D","DX.1","assessment_diagnosis","cabinet",
 "Même patiente de 51 ans : bouffées humides et cycles irréguliers depuis 8 mois, aucun signe d'alarme. Elle souhaite être soulagée.",
 "Quelle est la conduite la plus appropriée ?",
 [("Diagnostic clinique et traitement adapté",""),
  ("Doser FSH et œstradiol avant tout traitement","Après 45 ans, le tableau typique suffit ; une FSH normale n'exclut pas."),
  ("5-HIAA urinaire sur deux collectes de 24 h","Pas de flush sec ni de diarrhée."),
  ("Métanéphrines libres plasmatiques à jeun","Pas d'accès adrénergique."),
  ("TEP-TDM pour exclure une néoplasie","Jamais en dépistage.")],
 "Après 45 ans, un tableau vasomoteur typique se diagnostique cliniquement (ESE 2025, NICE). Options : information, TCC, THM individualisé ou fézolinétant.",
 "Utérus intact sous œstrogène → progestatif ; voie transdermique = moins de thrombose.",
 B(1,13))

q("D","DX.15","assessment_diagnosis","cabinet",
 "Un homme de 63 ans décrit des rougeurs brèves, rouge vif, du visage, du cou et du thorax, sans transpiration, depuis 4 mois, avec 5 selles aqueuses par jour, y compris la nuit, et des épisodes sibilants. Le foie est augmenté de volume et irrégulier.",
 "Quel examen est le plus approprié pour confirmer l'hypothèse principale ?",
 [("5-HIAA urinaire de 24 h, deux collectes",""),
  ("Métanéphrines libres plasmatiques","Cherchent un phéochromocytome : accès pâles, hypertensifs."),
  ("FSH et œstradiol sériques","Bouffée ménopausique humide, sans diarrhée."),
  ("TSH avec fT4 en réflexe","N'explique pas flush sec + diarrhée sécrétoire + sibilances."),
  ("Hémocultures en deux paires","Aucun tableau fébrile.")],
 "Flush sec + diarrhée sécrétoire + sibilances + foie métastatique = syndrome carcinoïde (E9). 5-HIAA > 50 µmol/24 h compatible.",
 "Le syndrome carcinoïde d'une TNE du grêle exige en général des métastases hépatiques (le foie inactive les amines).",
 B(15,14))

q("D","DX.13","assessment_diagnosis","cabinet",
 "Une femme de 44 ans présente 3 à 4 fois par mois des accès de 10–20 min de céphalées violentes, palpitations, sueurs et pâleur. PA mesurée pendant un accès 210/115 mmHg ; entre les accès 128/80 mmHg. Examen normal.",
 "Quel examen est le plus approprié en première intention ?",
 [("Métanéphrines libres plasmatiques",""),
  ("TDM des surrénales d'emblée","L'imagerie localise après la preuve biologique."),
  ("Scintigraphie à la MIBG","Imagerie fonctionnelle de seconde ligne, moins sensible."),
  ("5-HIAA urinaire sur 24 heures","Pour le flush sec carcinoïde."),
  ("Holter ECG sur 24 heures","N'explore pas la décharge catécholaminergique.")],
 "Accès adrénergiques avec pâleur et HTA paroxystique = phéochromocytome (E6). Métanéphrines libres, couchée ≥ 20 min, à jeun (Se 99 %) ; > 2× la limite sur prélèvement correct → localisation.",
 "Pression normale entre les accès n'exclut rien ; assise et non à jeun, la spécificité chute à 71 %.",
 B(13,9))

q("D","DX.2","assessment_diagnosis","urgences",
 "Un homme de 27 ans consulte aux urgences pour un 3e épisode en 2 mois : peur intense culminant en 10 min, palpitations, sueurs, sensation d'étouffement, paresthésies, peur de mourir ; résolution en 25 min. Depuis 5 semaines, il évite les transports par crainte d'un nouvel accès. ECG normal, glycémie 5,4 mmol/L, TSH 1,8 mUI/L, PA 128/76 mmHg.",
 "Quel est le diagnostic le plus probable ?",
 [("Trouble panique",""),
  ("Phéochromocytome","Pas de pâleur, d'HTA ni de céphalée par accès."),
  ("Hyperthyroïdie","TSH normale : l'écarte presque toujours."),
  ("Hypoglycémie","Glycémie normale, pas de traitement à risque."),
  ("Syndrome coronarien aigu","ECG normal, terrain et récurrence non évocateurs.")],
 "Attaques récurrentes, inattendues, ≥ 4/13 symptômes, acmé en minutes, + ≥ 1 mois de crainte/évitement, imitateurs exclus (ECG, glycémie, TSH) = trouble panique (DSM-5).",
 "Une attaque isolée (1 personne sur 5) ne suffit pas. Traitement : TCC et/ou ISRS.",
 PA("ssp-p8","§8 Critères DSM-5"))

q("D","DX.7","assessment_diagnosis","cabinet",
 "Une femme de 40 ans se plaint de bouffées de chaleur, de nervosité et d'une perte de 5 kg malgré un bon appétit. Cycles réguliers. Pouls 108/min régulier, peau chaude et moite, tremblement fin des mains tendues.",
 "Quel examen est le plus approprié en premier ?",
 [("TSH, avec fT4 et T3 en réflexe si elle est basse",""),
  ("FSH et œstradiol","Cycles réguliers ; le tableau est thyrotoxique, pas ménopausique."),
  ("Anticorps anti-récepteur de la TSH d'emblée","Établissent la cause (Basedow) après la preuve biologique."),
  ("Scintigraphie thyroïdienne","Pas en première intention ; réservée à la nodularité."),
  ("Métanéphrines libres plasmatiques","Pas d'accès paroxystiques avec pâleur.")],
 "Thermophobie, amaigrissement malgré l'appétit, tachycardie, tremblement fin = thyrotoxicose (E5). Test réflexe suisse : TSH d'abord.",
 "Une TSH normale écarte presque toujours l'hyperthyroïdie. Ne jamais conclure « ménopause » avant la TSH.",
 B(7,14))

q("D","DX.6","assessment_diagnosis","hôpital",
 "Un homme de 49 ans, opéré d'une fracture de cheville, est hospitalisé depuis 36 h. Il devient agité et anxieux, transpire abondamment, tremble des mains tendues. Pouls 118/min, PA 158/94 mmHg, température 37,4 °C, glycémie 6,1 mmol/L. Son épouse signale 8 verres de vin par jour.",
 "Quel est le diagnostic le plus probable ?",
 [("Sevrage alcoolique",""),
  ("Thyrotoxicose","Pas de thermophobie ni d'amaigrissement ; le contexte (arrêt brutal d'alcool) prime."),
  ("Sepsis","Apyrexie, pas de foyer ni de défaillance."),
  ("Hypoglycémie","Glycémie normale."),
  ("Trouble panique","Diagnostic d'exclusion ; ici une cause somatique évidente.")],
 "Tremblement + sueurs + tachycardie 6–72 h après le dernier verre = sevrage (E4). Pic vers 72 h ; convulsions 12–48 h, delirium 48–72 h.",
 "Toujours dater le dernier verre et coter le CIWA-Ar.",
 PA("ssp-p7","§7.6 Sevrage alcoolique"))

q("D","DX.6","management","hôpital",
 "Même patient de 49 ans en sevrage : CIWA-Ar à 22. Il est orienté, pas d'hallucinations ni de convulsion. Une perfusion de glucose est prévue.",
 "Quel traitement est le plus approprié ?",
 [("Thiamine IV avant le glucose, puis oxazépam",""),
  ("Halopéridol seul à dose sédative","N'agit pas sur l'hyperactivité autonome, abaisse le seuil épileptogène."),
  ("Propranolol seul pour la tachycardie","Hors schéma du cours : la benzodiazépine est le premier choix (CBIP)."),
  ("Clométhiazole et sortie le jour même","Réservé au milieu hospitalier contrôlé ; sortie inadaptée."),
  ("Perfusion de glucose, thiamine le lendemain","Glucose sans thiamine : risque de Wernicke.")],
 "CIWA-Ar ≥ 20 = sevrage sévère : benzodiazépine en premier choix (oxazépam 15–30 mg 3–4×/j, AIPS) ; thiamine avant tout glucose.",
 "Jamais d'antipsychotique seul dans le sevrage.",
 B(6,13))

q("D","DX.11","assessment_diagnosis","cabinet",
 "Un homme de 31 ans, né dans un pays à forte incidence de tuberculose et arrivé en Suisse il y a 2 ans, tousse depuis 7 semaines, a des sueurs nocturnes et a perdu 6 kg. Radiographie : infiltrat apical droit. L'IGRA est négatif.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Deux expectorations : PCR, microscopie, culture",""),
  ("Exclure la tuberculose vu l'IGRA négatif","> 20 % des tuberculeux ont un IGRA négatif."),
  ("Test cutané tuberculinique","Comme l'IGRA, ne distingue pas infection et maladie."),
  ("TEP-TDM thoracique","N'apporte pas la preuve microbiologique."),
  ("Antibiotique de 7 jours puis contrôle","Retarde le diagnostic et la protection des contacts.")],
 "Toux persistante + sueurs nocturnes + amaigrissement + origine à risque = tuberculose (E7). La preuve est microbiologique ; précautions de transmission d'emblée.",
 "L'IGRA ne confirme ni n'exclut une tuberculose active.",
 B(11,14))

q("D","DX.12","assessment_diagnosis","cabinet",
 "Une femme de 26 ans présente une adénopathie cervicale de 3 cm, ferme, indolore, persistante depuis 6 semaines, avec sueurs nocturnes abondantes et une perte de poids de 11 % en 5 mois. Pas de foyer infectieux.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Biopsie-exérèse ganglionnaire sans délai",""),
  ("Cytoponction à l'aiguille fine","Ne rend pas l'architecture : insuffisante."),
  ("TEP-TDM de dépistage","Sert à la stadification, après l'histologie."),
  ("Antibiothérapie de 2 semaines puis contrôle","Retarde le diagnostic d'un ganglion déjà persistant."),
  ("Surveillance clinique à 3 mois","Inadaptée : ganglion > 4–6 sem avec symptômes B.")],
 "Adénopathie persistante > 4–6 semaines + symptômes B (sueurs nocturnes, perte > 10 % en 6 mois) = lymphome à prouver (E8) : seule l'histologie tranche.",
 "Des sueurs nocturnes isolées, sans ganglion ni perte de poids, ne justifient pas de biopsie.",
 B(12,13))

q("D","DX.14","assessment_diagnosis","hôpital",
 "Un homme de 67 ans, porteur d'une prothèse valvulaire aortique, présente depuis 3 semaines une fièvre jusqu'à 38,6 °C et des sueurs nocturnes. Il est hémodynamiquement stable. Hémorragies en flammèches sous-unguéales.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Trois séries d'hémocultures, puis ETT et ETO",""),
  ("Amoxicilline orale empirique","L'antibiotique préalable est la 1re cause d'hémocultures négatives."),
  ("ETT seule ; si normale, endocardite exclue","Une ETT normale n'exclut pas, surtout sur prothèse."),
  ("CRP de contrôle dans une semaine","Retard d'une infection endovasculaire grave."),
  ("IGRA et radiographie thoracique","N'explorent pas l'endocardite.")],
 "Fièvre prolongée + prothèse + lésions emboliques = endocardite (E3). Trois séries d'hémocultures espacées de 30 min, sans attendre le pic, puis ETT et ETO.",
 "Absence de souffle ou ETT normale n'exclut jamais : ETO, répétée à 5–7 jours si suspicion forte.",
 B(14,13))

q("D","DX.14","assessment_diagnosis","cabinet",
 "Un homme de 24 ans consulte pour fièvre, sueurs, maux de gorge, adénopathies et éruption cutanée depuis 5 jours. Il rapporte un rapport sexuel non protégé avec un partenaire occasionnel il y a 3 semaines.",
 "Quelle stratégie de test est la plus appropriée ?",
 [("Test de 4e génération et test moléculaire",""),
  ("Autotest VIH à domicile","Un autotest réactif ne suffit pas et la fenêtre est trop précoce."),
  ("Sérologie anticorps seule dans 3 mois","Retarde un diagnostic de primo-infection symptomatique."),
  ("Numération des CD4 isolée","Ne pose pas le diagnostic."),
  ("Test de 4e génération seul ; négatif = exclu","Fenêtre de 6 semaines : un test précoce négatif n'exclut pas.")],
 "Primo-infection symptomatique : test ≥ 4e génération (Ac + p24) et test moléculaire en parallèle ; tout test réactif se confirme.",
 "ART pour tous, dès le diagnostic, quel que soit le taux de CD4.",
 B(14,14))

q("D","DX.8","assessment_diagnosis","cabinet",
 "Une femme de 45 ans signale des sueurs diffuses apparues 3 semaines après l'introduction d'escitalopram 10 mg. Cycles réguliers, apyrexie, poids stable. Examen normal, sans clonus ni hyperréflexie. TSH, glycémie, CRP et hémogramme normaux.",
 "Quel est le diagnostic le plus probable ?",
 [("Hyperhidrose médicamenteuse",""),
  ("Syndrome sérotoninergique","Exige clonus ou hyperréflexie (critères de Hunter) ; la sueur seule ne suffit pas."),
  ("Hyperhidrose primaire","Début tardif, diffus, lié à un médicament."),
  ("Hyperthyroïdie","TSH normale."),
  ("Symptômes vasomoteurs de la ménopause","Cycles réguliers, chronologie médicamenteuse nette.")],
 "Sueurs apparues avec un ISRS, autres causes exclues (TSH, glycémie, CRP, numération) = cause médicamenteuse. Conduite : arrêt ou substitution avec le prescripteur.",
 "Ne jamais stopper brutalement un ISRS : décroissance sur ≥ 1–2 semaines (sinon sueur de sevrage).",
 B(8,13))

q("D","DX.4","management","EMS",
 "Un homme de 78 ans, en EMS, sous gliclazide (Diamicron® MR), est retrouvé en sueurs et somnolent. Glycémie 2,4 mmol/L. Il ne déglutit pas de façon sûre. Une voie veineuse est posée.",
 "Quel traitement est le plus approprié ?",
 [("Glucose IV et surveillance prolongée",""),
  ("GlucaGen® 1 mg IM puis surveillance de 2 h","Sous sulfonylurée, le glucose IV est le choix ; surveillance trop courte."),
  ("15 g de glucides par voie orale","Déglutition non sûre : aucune voie orale."),
  ("Glucagon répété toutes les 10 minutes","Répéter sans glucose IV retarde la correction."),
  ("Thiamine seule puis contrôle","Ne corrige pas l'hypoglycémie.")],
 "Sulfonylurée + troubles de conscience + voie IV : glucose IV (HUG : 32 g de glucose 40 % lent ; IP : 50 mL 20–30 %) puis glucose 10 % ; surveillance ≥ 48 h car l'hypoglycémie récidive.",
 "GlucaGen® = surtout sous insuline ; sous sulfonylurée = glucose IV et surveillance prolongée.",
 PA("ssp-p11","§11 Urgence hypoglycémie"))

q("D","DX.10","assessment_diagnosis","cabinet",
 "Un homme de 62 ans consulte pour une transpiration généralisée apparue il y a 4 mois, y compris la nuit. Aucun antécédent de sudation, aucun nouveau médicament. IMC 25 kg/m². Examen sans particularité.",
 "Quelle est la conduite la plus appropriée ?",
 [("Bilan étiologique ciblé",""),
  ("Chlorure d'aluminium le soir","Traitement de la forme primaire focale ; masque une cause."),
  ("Oxybutynine hors indication","Aucun anticholinergique qui masquerait des signes généraux."),
  ("Toxine botulique axillaire","Écarter une hyperhidrose secondaire avant (AIPS BOTOX®)."),
  ("Sympathectomie thoracique","Réservée aux formes focales primaires rebelles.")],
 "Généralisée, nocturne, début > 25 ans = hyperhidrose secondaire : bilan avant tout traitement symptomatique — électrolytes, créatinine, glycémie, TSH, hémogramme, CRP ; si nocturne, IGRA, VIH, radiographie.",
 "Bilan négatif : suivi programmé, sans TEP-TDM de dépistage.",
 B(10,13))

q("D","DX.3","assessment_diagnosis","cabinet",
 "Un homme de 55 ans, IMC 34 kg/m², tour de cou 45 cm, se réveille trempé plusieurs nuits par semaine. Il ronfle et somnole le jour. Apyrexie, poids stable ; hémogramme, CRP, TSH et glycémie normaux.",
 "Quel examen est le plus approprié ?",
 [("Étude du sommeil (polysomnographie)",""),
  ("TEP-TDM corps entier","Pas de dépistage indifférencié."),
  ("Métanéphrines libres plasmatiques","Pas d'accès adrénergiques."),
  ("5-HIAA urinaire de 24 h","Pas de flush ni de diarrhée."),
  ("Biopsie ganglionnaire","Aucune adénopathie.")],
 "Sueurs nocturnes + IMC ≥ 30 + tour de cou > 43 cm + ronflements/somnolence = apnées du sommeil à documenter.",
 "La pression positive continue ramène ces sueurs au niveau de la population.",
 B(3,13))

# ───────────── BLOC 3 · PIÈGES & ALARMES
q("P","DX.13 × DX.4","management","urgences",
 "Une femme de 52 ans, diabétique sous insuline, en cours de bilan pour un phéochromocytome (métanéphrines à 3 fois la limite), est amenée inconsciente. Glycémie 1,9 mmol/L. Une voie veineuse est en place.",
 "Quel traitement est le plus approprié ?",
 [("Glucose IV",""),
  ("GlucaGen® 1 mg IM","Contre-indiqué : libère des catécholamines, crise hypertensive."),
  ("Glucagon nasal 3 mg","Même molécule, même contre-indication."),
  ("15 g de glucides par voie orale","Patiente inconsciente : aucune voie orale."),
  ("Thiamine seule","Ne corrige pas l'hypoglycémie.")],
 "Le glucagon est contre-indiqué dans le phéochromocytome (AIPS GlucaGen®) : il déclenche une crise. Patient suspect + hypoglycémie = glucose.",
 "Éviter aussi chez le suspect : métoclopramide, corticostéroïdes, morphine.",
 B(13,14))

q("P","DX.13","management","hôpital",
 "Un homme de 46 ans a un phéochromocytome confirmé et localisé ; l'opération est prévue dans 3 semaines. Il présente encore des accès hypertensifs avec tachycardie.",
 "Quelle préparation médicamenteuse est la plus appropriée ?",
 [("Alpha-bloquant, puis bêtabloquant si besoin",""),
  ("Propranolol seul","Laisse la vasoconstriction alpha sans opposition : crise."),
  ("Métoclopramide en cas de nausées","Contre-indiqué : épisodes hypertensifs sévères."),
  ("Aucun traitement jusqu'à l'opération","Expose à une crise peropératoire."),
  ("Test au glucagon avant l'opération","Le glucagon peut déclencher une crise.")],
 "Toujours bloquer α avant β, 7–14 jours avant l'opération. Propranolol (60 mg/j 3 jours avant) seulement après l'alpha-bloquant ; le blocage préopératoire relève de l'endocrinologue.",
 "« Jamais de bêtabloquant seul » devant tout phéochromocytome non traité.",
 B(13,13))

q("P","DX.6 × DX.4","management","urgences",
 "Un homme de 57 ans, alcoolique chronique dénutri, est trouvé confus et en sueurs après 2 jours sans manger. Glycémie 2,6 mmol/L. Voie veineuse en place.",
 "Quelle conduite est la plus appropriée ?",
 [("Glucose IV sans délai, en associant la thiamine",""),
  ("GlucaGen® 1 mg IM","Agit peu sans réserve en glycogène (jeûne, alcool)."),
  ("Thiamine d'abord, glucose 1 heure plus tard","Retarder la correction d'une hypoglycémie est dangereux."),
  ("Oxazépam puis glycémie de contrôle","Ne traite pas l'hypoglycémie."),
  ("15 g de glucides oraux","Confusion : déglutition non sûre.")],
 "Hypoglycémie chez un alcoolique carencé : corriger sans délai par glucose IV et associer la thiamine (risque de Wernicke).",
 "Le glucagon est inefficace après jeûne prolongé, alcool ou insuffisance surrénale.",
 PA("ssp-p14","§14 Pièges"))

q("P","DX.15","assessment_diagnosis","cabinet",
 "Une femme de 58 ans sous sertraline et paracétamol au long cours décrit des rougeurs du visage peu typiques. Le 5-HIAA urinaire de 24 h revient à 62 µmol/24 h. Elle n'a ni diarrhée ni sibilances, foie normal.",
 "Quelle est la conduite la plus appropriée ?",
 [("Nouveau dosage après éviction encadrée",""),
  ("Retenir un syndrome carcinoïde et débuter l'octréotide","Un dosage élevé isolé, sous interférents, ne suffit pas."),
  ("TEP-TDM pour localiser la tumeur","Localiser seulement après une biologie fiable."),
  ("Doser les métanéphrines plasmatiques","Ne répond pas à la question du flush."),
  ("Classer comme bouffées ménopausiques","Ne répond pas au résultat discordant.")],
 "ISRS, paracétamol et aliments sérotoninergiques faussent le 5-HIAA. Toute suspension médicamenteuse relève d'un ordre médical ; deux collectes de 24 h.",
 "Le diagnostic exige symptômes + biologie ; ni l'un ni l'autre seul.",
 PA("ssp-p14","§14 Pièges"))

q("P","DX.14","assessment_diagnosis","hôpital",
 "Un homme de 70 ans, porteur d'une prothèse mitrale, a 3 hémocultures positives à Staphylococcus aureus, de la fièvre et des sueurs nocturnes. L'ETT ne montre pas de végétation ; aucun souffle nouveau.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Échocardiographie transœsophagienne",""),
  ("Conclure à une bactériémie sans endocardite","ETT normale + absence de souffle n'excluent pas."),
  ("Répéter l'ETT dans 3 mois","Délai inadapté à une infection endovasculaire."),
  ("TEP-TDM de dépistage d'un cancer","Hors sujet."),
  ("IGRA","N'explore pas l'endocardite.")],
 "Sur prothèse, l'ETT manque souvent la maladie : ETO, répétée à 5–7 jours si la suspicion reste forte. Équipe d'endocardite.",
 "Critères : 2 majeurs, ou 1 majeur + 3 mineurs, ou 5 mineurs (ESC / Duke-ISCVID 2023).",
 B(14,14))

q("P","DX.1 × DX.10","assessment_diagnosis","cabinet",
 "Une femme de 52 ans, en périménopause, consulte pour des sueurs nocturnes depuis 2 mois. Elle a mesuré à plusieurs reprises 38,3 °C le soir et a perdu 7 % de son poids sans le vouloir.",
 "Quelle est la conduite la plus appropriée ?",
 [("Recherche d'une infection et d'un lymphome",""),
  ("Traitement hormonal de la ménopause","Fièvre + amaigrissement : jamais conclure « ménopause »."),
  ("Fézolinétant 45 mg/j","Traite un symptôme sans écarter une cause grave."),
  ("Thérapie cognitivo-comportementale","Même erreur : cause somatique non exclue."),
  ("Oxybutynine hors indication","Masquerait des signes généraux.")],
 "Fièvre objectivée ou perte de poids involontaire avec sueurs nocturnes = exclure d'emblée infection grave (TB, endocardite, VIH) et lymphome : examen ganglionnaire, hémogramme, CRP, TSH, IGRA/radio, VIH.",
 "Les symptômes vasomoteurs se posent après exclusion, jamais avec fièvre ou amaigrissement.",
 B(10,14))

q("P","DX.5","management","cabinet",
 "Un homme de 23 ans présente une hyperhidrose axillaire primaire typique, HDSS 3. Il n'a jamais été traité.",
 "Laquelle des propositions suivantes est INAPPROPRIÉE ?",
 [("Sympathectomie thoracique en première intention",""),
  ("Chlorure d'aluminium 10–30 % le soir sur peau sèche","1re étape recommandée, simple et réversible."),
  ("Éviction des épices, de l'alcool et du café","Mesure générale associée."),
  ("Glycopyrronium topique en cas d'échec","2e ligne autorisée (Axhidrox®)."),
  ("Toxine botulique A en cas d'échec","2e ligne (BOTOX® 50 U/aisselle).")],
 "Traitement par étapes : mesures générales + sels d'aluminium, puis glycopyrronium topique ou toxine. La sympathectomie est réservée aux formes rebelles.",
 "Sympathectomie : sudation compensatrice chez 76–90 % des opérés (sévère chez 22 %).",
 B(5,13),pol="negative")

# ═════════════ v2 — niveaux (EX / AP / SPE) ═════════════
def _set(i,must,niv,spe=None):
    assert must in Q[i]['dx']+Q[i]['stem'], (i,must)
    Q[i]['niveau']=niv; Q[i]['specialite']=spe
_set(2,"DX.5 vs DX.10","approfondissement")
_set(3,"mécanisme","approfondissement")
_set(6,"DX.4 / DX.8","approfondissement")
_set(9,"documenter le retentissement","approfondissement")
_set(11,"Même patiente de 51 ans","approfondissement")
_set(21,"rapport sexuel non protégé","specialiste","Infectiologie")
_set(27,"opération est prévue dans 3 semaines","specialiste","Endocrinologie")
_set(29,"5-HIAA urinaire de 24 h revient","specialiste","Oncologie (TNE)")
_set(30,"Staphylococcus aureus","specialiste","Cardiologie")
_set(32,"jamais été traité","specialiste","Dermatologie")

# ───────────── v2 · nouvelles questions APPROFONDISSEMENT (mécanismes)
q("R","DX.9 vs coup de chaleur","mechanisms","autre (chantier)",
 "Un ouvrier de 35 ans s'effondre, confus, après un effort prolongé sur un chantier pendant une canicule. Température rectale 41 °C, peau chaude. Un collègue propose de lui donner du paracétamol.",
 "Quel mécanisme explique que l'antipyrétique soit inefficace dans cette situation ?",
 [("Consigne hypothalamique normale, élimination dépassée",""),
  ("Consigne relevée par la PGE2 sur le récepteur EP3","C'est la fièvre infectieuse : c'est précisément là que l'antipyrétique agit."),
  ("Libération de cytokines pyrogènes (IL-1β, IL-6)","Amorce de la fièvre ; absente dans l'hyperthermie d'effort."),
  ("Vasoconstriction cutanée avec frissons","Phase de montée de la fièvre (peau froide), pas l'hyperthermie."),
  ("Signalisation NK3 hypothalamique désinhibée","Mécanisme des bouffées de la ménopause.")],
 "Dans l'hyperthermie (coup de chaleur, effort, médicament), la consigne reste normale et la production de chaleur dépasse l'élimination. L'antipyrétique, qui abaisse une consigne relevée (PGE2–EP3), n'a donc pas de cible.",
 "Traiter un coup de chaleur comme une fièvre infectieuse = piège mortel : 144 et refroidissement, cible Suva < 40 °C en 30 min.",
 B(9,6),niv="approfondissement")

q("R","DX.1","mechanisms","cabinet",
 "Une femme de 54 ans, ménopausée depuis 2 ans, présente des bouffées de chaleur modérées à sévères qui fragmentent son sommeil. Elle refuse tout traitement hormonal. Vous prescrivez du fézolinétant (VEOZA™ 45 mg/j).",
 "Quel est le mécanisme d'action de ce médicament ?",
 [("Antagoniste sélectif du récepteur NK3",""),
  ("Antagoniste des récepteurs NK1 et NK3","C'est l'élinzanétant (LYNKUET®), autre molécule de la même famille."),
  ("Agoniste des récepteurs aux œstrogènes","Mécanisme du THM ; le fézolinétant est non hormonal."),
  ("Inhibition sélective de la recapture de la sérotonine","Mécanisme des ISRS, qui peuvent eux-mêmes faire transpirer."),
  ("Antagonisme compétitif des récepteurs muscariniques","Mécanisme du glycopyrronium (hyperhidrose focale).")],
 "La chute des œstrogènes désinhibe les neurones KNDy ; la neurokinine B les active via NK3 et la zone thermoneutre se rétrécit → bouffée. Le fézolinétant bloque NK3 (affinité 450× > NK1/NK2) et module le centre thermorégulateur.",
 "Bilan hépatique avant, puis chaque mois pendant 3 mois ; ictère, urines foncées ou fatigue → arrêt immédiat et ALAT/ASAT/bilirubine.",
 B(1,6),niv="approfondissement")

q("R","DX.5","mechanisms","cabinet",
 "Un homme de 29 ans souffre d'une hyperhidrose axillaire primaire HDSS 3. Les sels d'aluminium, correctement appliqués le soir sur peau sèche, ont échoué. Vous proposez de la toxine botulique A (BOTOX® 50 U par aisselle, intradermique).",
 "Quel mécanisme explique l'effet de ce traitement ?",
 [("Clivage de SNAP-25, blocage de l'exocytose d'acétylcholine",""),
  ("Blocage compétitif des récepteurs muscariniques","Mécanisme du glycopyrronium crème (Axhidrox®)."),
  ("Complexation aux mucopolysaccharides, fermeture du canal","Mécanisme des sels d'aluminium."),
  ("Blocage des récepteurs alpha-adrénergiques glandulaires","La glande eccrine reçoit une innervation sympathique cholinergique, pas adrénergique."),
  ("Destruction définitive des glandes eccrines","C'est l'objectif de la thermolyse ou du curetage ; la toxine n'abîme pas la glande.")],
 "Les glandes eccrines sont normales mais surstimulées : le défaut est dans la commande cholinergique. La toxine clive SNAP-25 (complexe SNARE) et empêche la libération d'acétylcholine à la jonction nerf–glande.",
 "Unités non interchangeables entre toxines ; pas de réinjection avant 16 semaines (BOTOX®).",
 B(5,6),niv="approfondissement")

q("D","DX.6","mechanisms","hôpital",
 "Un homme de 52 ans, buveur quotidien, est hospitalisé pour un sevrage alcoolique : tremblement, sueurs, tachycardie, CIWA-Ar 18. Un interne demande pourquoi on prescrit de l'oxazépam plutôt qu'un autre psychotrope.",
 "Quel mécanisme justifie la benzodiazépine dans le sevrage ?",
 [("Potentialisation du GABA-A, en remplacement de l'éthanol",""),
  ("Modulation glutamatergique du craving","Acamprosate : maintien de l'abstinence, pas traitement du sevrage aigu."),
  ("Antagonisme des récepteurs opioïdes","Naltrexone ou nalméfène : réduction de la consommation."),
  ("Antagonisme des récepteurs dopaminergiques D2","Halopéridol : n'agit pas sur l'hyperactivité autonome et abaisse le seuil épileptogène."),
  ("Blocage des récepteurs bêta-adrénergiques","Masque la tachycardie sans prévenir convulsions ni delirium.")],
 "L'alcool chronique diminue les récepteurs GABA-A et augmente les NMDA. À l'arrêt, perte du frein GABA + excès de glutamate et de catécholamines → hyperactivité autonome (sueur, tachycardie, tremblement), convulsions 12–48 h, delirium 48–72 h. La benzodiazépine rétablit l'inhibition GABA-A.",
 "Les catécholamines du sevrage font entrer le potassium dans les cellules (hypokaliémie) et l'alcool allonge le QT : surveiller K⁺ et ECG.",
 B(6,6),niv="approfondissement")

q("D","DX.3","mechanisms","cabinet",
 "Un homme de 55 ans, IMC 36 kg/m², ronfle fort ; sa partenaire décrit des pauses respiratoires. Il se réveille trempé plusieurs nuits par semaine. Apyrexie, poids stable, aucun traitement hypoglycémiant ; TSH et hémogramme normaux.",
 "Quel mécanisme explique le mieux ses sueurs nocturnes ?",
 [("Hypoxie et micro-éveils avec décharge sympathique",""),
  ("Consigne thermique relevée par des cytokines","Mécanisme de la fièvre ; apyrexie ici."),
  ("Signalisation NK3 hypothalamique désinhibée","Mécanisme de la bouffée ménopausique."),
  ("Libération d'amines vasoactives tumorales","Flush carcinoïde sec, avec diarrhée ou sibilances."),
  ("Contre-régulation adrénergique d'une hypoglycémie","Exige un traitement hypoglycémiant (insuline, sulfonylurée).")],
 "Collapsus pharyngé → apnée → hypoxie et micro-éveil → décharge sympathique → stimulation des glandes eccrines → sueurs nocturnes.",
 "Sueurs nocturnes fréquentes chez 33,2 % des apnéiques non traités, 11,5 % sous pression positive (niveau de la population).",
 B(3,6),niv="approfondissement")

# ───────────── v2 · nouvelles questions SPÉCIALISTE
q("D","DX.2","management","cabinet",
 "Un homme de 27 ans, chez qui un trouble panique a été posé (ECG, glycémie et TSH normaux), a débuté de l'escitalopram il y a 10 jours. Il dit que « rien n'a changé » et qu'il transpire un peu plus. Il demande un traitement plus efficace.",
 "Quelle est la conduite la plus appropriée ?",
 [("Poursuivre l'ISRS, réévaluer à 2–6 semaines, associer la TCC",""),
  ("Ajouter du lorazépam au long cours","La S3 la déconseille sauf exception ; AIPS : 2–3 mois maximum (dépendance)."),
  ("Arrêter brutalement l'escitalopram","Jamais d'arrêt brutal : décroissance ≥ 1–2 semaines."),
  ("Ajouter de l'oxybutynine contre la sueur","Pas d'antisudorifique tant que l'anxiété n'est pas traitée."),
  ("Remplacer d'emblée par la venlafaxine","Délai d'action non atteint ; la venlafaxine fait aussi transpirer.")],
 "Délai d'action des antidépresseurs dans les troubles anxieux : 2 à 6 semaines (HUG). Dix jours sans effet n'est pas un échec. La sueur sous ISRS est un effet iatrogène connu : ne pas la prendre pour un échec du traitement.",
 "Sueur iatrogène persistante : réduire la dose, changer de molécule, associer la TCC. Contrôler le QTc sous escitalopram (dose-dépendant).",
 B(2,13),niv="specialiste",spe="Psychiatrie")

q("D","DX.12","management","hôpital",
 "Une femme de 31 ans traitée pour un lymphome de Hodgkin classique termine sa chimiothérapie. Le TEP-TDM de fin de traitement montre une masse médiastinale résiduelle cotée Deauville 4.",
 "Quelle est la conduite la plus appropriée ?",
 [("Radiothérapie de site impliqué sur le résidu",""),
  ("Surveillance : réponse métabolique complète","Réponse complète = Deauville ≤ 3 ; ≥ 4 = TEP positif."),
  ("Biopsie médullaire de contrôle","Non routinière dans le LH ; le TEP l'a remplacée."),
  ("Scanner de surveillance tous les 3 mois","Pas de scanner de surveillance de routine ; ne traite pas le résidu actif."),
  ("Arrêt du suivi hématologique","Suivi à vie après un LH.")],
 "Deauville (fixation comparée au médiastin et au foie) : ≤ 3 = réponse métabolique complète ; ≥ 4 = TEP positif. Un résidu actif se consolide par radiothérapie de site impliqué (30 Gy dans le LH).",
 "« Consolider seulement ce qui reste actif. » Diagnostic : biopsie-exérèse ; stade et réponse : TEP-TDM.",
 B(12,13),niv="specialiste",spe="Hématologie")


# ───────────── META (rendu) — migré depuis QCM-banque/LOT_001 (v2) le 2026-11-01
META = dict(
 code="G1", lot="LOT_001", version="2.0.0", seed=2, date="2026-11-01",
 titre="Transpiration anormale", titre_court="Transpiration anormale", n_dx=15,
 note_version="v2 : niveau EX/AP/SPE + spécialité ; feedback masqué jusqu'au 💡",
 note_media="Aucune image, figure ni data-URI image dans les HTML LOT_001 (Phase A + DX.1–15) : media = null partout, bouton 🖼 absent.",
 intro_R="Triage, prochain pas, red flag, mécanisme.",
 intro_D="Vignettes du cabinet, des urgences, de l'EMS et de l'hôpital. Les options sont des DX réels du LOT, ou l'examen ou le traitement que le cours retient.",
 intro_P="Glucagon, bêtabloquant seul, thiamine, faux positifs, ETT rassurante à tort, « c'est la ménopause ».",
 verdict_label="Réflexe G1",
 footer="LOT_001 · G1 · Banque « Temps 1 » v2 · Faits issus exclusivement des leçons auditées LOT_001 (Phase A + Phase B DX.1–15) · Type A, une seule meilleure réponse (règles IML) · Aucun cliché dans les sources LOT_001 : aucune image affichée.",
 carte_html='<div class="reflex"><b>Les 3 questions réflexes devant tout patient qui transpire</b><ol>\n<li><b>Danger maintenant ?</b> Malaise, confusion, oppression, dyspnée, chaleur → fonctions vitales, <b>glycémie</b>, <b>ECG en 10 min</b>, refroidir.</li>\n<li><b>Quel profil ?</b> Focale-bilatérale-ancienne-jamais la nuit (primaire) <i>ou</i> généralisée / asymétrique / nocturne / après 25 ans (secondaire).</li>\n<li><b>Quel signe associé désigne la famille, et quel examen tranche ?</b> Une hypothèse = un examen qui prouve.</li></ol></div>\n<div class="map" style="margin-top:10px">\n<div class="ax"><h3>⏱ Temporalité</h3><ul>\n<li>Minutes, avec malaise → hypoglycémie, SCA (urgence)</li>\n<li>Accès de 10–30 min → panique, phéochromocytome, bouffée, flush</li>\n<li>Nocturne → fièvre, ménopause, TB, lymphome, apnées, médicament</li>\n<li>6–72 h après le dernier verre → sevrage</li>\n<li>Depuis l\'adolescence, jamais la nuit → primaire</li></ul></div>\n<div class="ax"><h3>📍 Topographie</h3><ul>\n<li>Focale bilatérale symétrique (aisselles, paumes, plantes, visage) → primaire (≥ 4/7 critères)</li>\n<li>Généralisée ou asymétrique → secondaire (DX.10)</li>\n<li>Peau <span class="red">sèche</span> à la chaleur + confusion → anhidrose, coup de chaleur</li></ul></div>\n<div class="ax"><h3>🔗 Signes associés → examen qui tranche</h3><ul>\n<li>Faim, tremblement, confusion sous traitement → glycémie capillaire</li>\n<li>Fièvre + défaillance → hémocultures, hôpital ; + prothèse/souffle → 3 hémocultures, ETT puis ETO</li>\n<li>Toux, exposition, perte de poids → 2 expectorations (PCR, culture)</li>\n<li>Adénopathie > 4–6 sem + symptômes B → biopsie-exérèse</li>\n<li>Thermophobie, tachycardie, amaigrissement → TSH (réflexe fT4/T3)</li>\n<li>Céphalée, palpitations, <b>pâleur</b>, HTA par accès → métanéphrines libres</li>\n<li>Flush <b>sec</b> + diarrhée/sibilances → 5-HIAA 24 h ×2</li>\n<li>Bouffée <b>humide</b>, cycles irréguliers, ≥ 45 ans → clinique</li></ul></div>\n<div class="ax"><h3>🧾 Contexte</h3><ul>\n<li>Médicaments : ISRS, insuline, bêtabloquants, AINS, agonistes dopaminergiques (début, arrêt, dose)</li>\n<li>Alcool : quantité, heure du dernier verre</li>\n<li>Poids, IMC ≥ 30, tour de cou, ronflements → apnées</li>\n<li>Origine à forte incidence TB, risque VIH, prothèse valvulaire, drogues IV</li>\n<li>Âge : début > 25 ans ou > 60 ans → secondaire plus probable</li></ul></div>\n<div class="ax rf"><h3>🚩 Ordre d\'exclusion (délai avant dommage irréversible)</h3><ol>\n<li>Hors liste : <b>SCA</b> — ECG 10 min</li><li>Hors liste : <b>coup de chaleur</b> — 144, refroidir</li>\n<li>E1 Hypoglycémie du diabétique traité (DX.4)</li><li>E2 Infection fébrile avec défaillance (DX.9)</li>\n<li>E3 Endocardite, VIH (DX.14)</li><li>E4 Sevrage alcoolique compliqué (DX.6)</li>\n<li>E5 Thyrotoxicose décompensée (DX.7)</li><li>E6 Phéochromocytome (DX.13)</li>\n<li>E7 Tuberculose (DX.11)</li><li>E8 Lymphome (DX.12)</li><li>E9 Tumeur carcinoïde (DX.15)</li>\n<li>Puis fréquents : ménopause, anxiété, obésité, primaire, médicament</li></ol></div>\n</div>',
 algo_html='\n<table class="algo"><tr><th>Si…</th><th>Alors…</th></tr>\n<tr class="e"><td>Malaise, confusion, oppression, dyspnée, chaleur avec trouble neurologique</td><td>Fonctions vitales + glycémie ; ECG en 10 min ; 144 et refroidir si coup de chaleur</td></tr>\n<tr class="e"><td>E1 · Diabétique sous insuline/sulfonylurée, glycémie &lt; 4,0 mmol/L</td><td>Corriger selon la conscience : 15 g (30 g si &lt; 2,5) per os ; GlucaGen® 1 mg sous insuline seulement ; glucose IV sous sulfonylurée (surveillance ≥ 48 h)</td></tr>\n<tr class="e"><td>E2 · Fièvre avec défaillance</td><td>Hémocultures avant antibiotique (&lt; 30 min si choc), hospitalisation</td></tr>\n<tr class="e"><td>E3 · Fièvre prolongée + prothèse, souffle nouveau, drogues IV ; risque VIH</td><td>3 séries d\'hémocultures, ETT puis ETO ; test VIH ≥ 4e génération (+ moléculaire si primo-infection)</td></tr>\n<tr class="e"><td>E4 · Dernier verre il y a 6–72 h, tremblement, sueurs</td><td>CIWA-Ar ; thiamine avant tout glucose ; oxazépam selon la sévérité ; hôpital si ≥ 20, convulsion, delirium</td></tr>\n<tr class="e"><td>E5 · Thermophobie, tachycardie, amaigrissement</td><td>TSH → fT4/T3 en réflexe ; propranolol ; endocrinologie</td></tr>\n<tr class="e"><td>E6 · Accès céphalée + palpitations + sueurs + pâleur</td><td>Métanéphrines libres (couché ≥ 20 min) ; ni glucagon ni bêtabloquant seul</td></tr>\n<tr class="e"><td>E7 · Toux, exposition, sueurs nocturnes</td><td>2 expectorations (PCR, culture) ; précautions de transmission ; IGRA négatif ne clôt rien</td></tr>\n<tr class="e"><td>E8 · Adénopathie &gt; 4–6 sem ou splénomégalie + symptômes B</td><td>Biopsie-exérèse (pas d\'aiguille fine)</td></tr>\n<tr class="e"><td>E9 · Flush sec + diarrhée ou sibilances</td><td>5-HIAA urinaire 24 h ×2 après éviction ; centre spécialisé</td></tr>\n<tr><td>Bouffées humides, cycles irréguliers, ≥ 45 ans</td><td>DX.1 : diagnostic clinique, sans dosage hormonal</td></tr>\n<tr><td>Accès de peur ≥ 4 symptômes, examen normal entre les accès</td><td>DX.2 : DSM-5 après TSH, glycémie, ECG ; TCC et/ou ISRS</td></tr>\n<tr><td>Médicament inducteur introduit ou augmenté</td><td>DX.8 : arrêt ou substitution avec le prescripteur (décroissance progressive)</td></tr>\n<tr><td>Focale, bilatérale, depuis l\'adolescence, jamais la nuit, ≥ 4/7</td><td>DX.5 : HDSS ; aluminium → glycopyrronium topique ou toxine</td></tr>\n<tr><td>Sueurs à l\'effort ou nocturnes, IMC ≥ 30, ronflements</td><td>DX.3 : perte de poids ; étude du sommeil</td></tr>\n<tr><td>Généralisée, asymétrique ou nocturne, sans orientation</td><td>DX.10 : électrolytes, créatinine, glycémie, TSH, hémogramme, CRP ; IGRA, VIH, radiographie ; suivi si négatif, sans TEP de dépistage</td></tr>\n</table>\n<p class="intro">Source : <a href="../../../repo/LOT_Claude_Finaux/LOT_001/LOT_001_Phase_A_V0.html#algo">Phase A · Algorithme discriminant</a> et <a href="../../../repo/LOT_Claude_Finaux/LOT_001/LOT_001_Phase_A_V0.html#ssp-p10">§10 Arbre décisionnel</a>.</p>',
)
