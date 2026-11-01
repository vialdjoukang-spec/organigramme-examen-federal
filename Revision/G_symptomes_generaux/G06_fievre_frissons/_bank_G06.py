# -*- coding: utf-8 -*-
# Banque G6 — Fièvre, frissons, hyperthermie (LOT_006).
# Sources : exclusivement LOT_Claude_Finaux/LOT_006 (Phase A + Phase B DX.1–15, audités C7 : 0 critique).
# Convention : opts[0] = bonne réponse (son « pourquoi pas » est ignoré) ; position finale fixée par build_ssp.py (seed).
# dx : le PREMIER DX.n cité = DX cible (couverture) ; les suivants = discrimination croisée.
R = "../../../repo/LOT_Claude_Finaux/LOT_006/"
def PA(sec, label): return (f"{R}LOT_006_Phase_A_V0.html#{sec}", f"Phase A {label}")
def B(n, p): return (f"{R}LOT_006_Phase_B_V0_DX.{n}.html#dx{n}-p{p}", f"Phase B DX.{n} §{p}")

# ═════════════ BLOC R · RAISONNER (danger d'abord, puis prochain pas)
q("R","DX.11 · fébrile et hypotendu","management","urgences",
 "Un homme de 71 ans est amené pour fièvre à 39,2 °C et frissons depuis la veille. Il est confus. FC 118/min, PA 88/52 mmHg, FR 26/min, SpO2 92 %. Pas de purpura.",
 "Quelle est la conduite la plus appropriée ?",
 [("Hémocultures, puis antibiotique i.v. dans l'heure",""),
  ("Attendre le lactate avant de décider de l'antibiotique","On traite dès le soupçon ; le lactate ne doit pas retarder l'antibiotique."),
  ("Rechercher le foyer par scanner, puis traiter","L'imagerie du foyer vient après l'antibiotique, dans les 6 à 12 heures."),
  ("Paracétamol 1 g i.v. et réévaluation à 1 heure","L'antipyrétique ne ferme aucune branche dangereuse."),
  ("Antibiotique oral et contrôle le lendemain","Un patient en choc probable reçoit un traitement i.v. et une surveillance continue.")],
 "Hypotension, confusion et polypnée : qSOFA à 3, sepsis probable (DX.11, 🚩 E2). On prélève deux séries d'hémocultures et le lactate sans retarder l'antibiotique i.v. à large spectre, donné dans l'heure, puis on remplit.",
 "Chaque heure de retard de l'antibiotique augmente la mortalité.",
 PA("ssp-p11","§11 Prise en charge"))

q("R","DX.11 · remplissage","management","urgences",
 "Une femme de 68 ans, 60 kg, est traitée pour un sepsis d'origine urinaire. Les hémocultures sont prélevées et la ceftriaxone est en cours. PA 82/48 mmHg, lactate 4,2 mmol/L.",
 "Quel remplissage est le plus approprié ?",
 [("Cristalloïde balancé ≥ 30 mL/kg en 3 h",""),
  ("Glucose 5 % 500 mL sur 6 heures","Le glucose apporte de l'eau libre et n'a pas d'effet volémique durable."),
  ("Aucun soluté avant de débuter la noradrénaline","Le remplissage précède le vasopresseur."),
  ("Albumine 20 % en première intention","Les cristalloïdes balancés restent la première ligne."),
  ("NaCl 0,9 % 250 mL en 24 heures","Volume très insuffisant pour corriger l'hypoperfusion.")],
 "Lactate > 2 mmol/L et hypotension : hypoperfusion. La SSC 2021 recommande au moins 30 mL/kg de cristalloïde, de préférence balancé, dans les 3 premières heures, soit 1 800 mL pour 60 kg (DX.11).",
 "Le remplissage est guidé par des mesures dynamiques et le temps de recoloration capillaire.",
 B(11,11))

q("R","DX.11 · PAM basse","management","urgences",
 "Un homme de 75 ans en sepsis pulmonaire a reçu 30 mL/kg de cristalloïde et l'antibiotique. Sa PA reste à 80/45 mmHg (PAM 57 mmHg). Lactate 3,8 mmol/L.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Noradrénaline pour une PAM ≥ 65 mmHg",""),
  ("Nouveau bolus de 3 litres en 1 heure","Au-delà du remplissage initial, on évite la surcharge ; le vasopresseur s'impose."),
  ("Hydrocortisone avant tout vasopresseur","Elle n'est envisagée qu'en cas de besoin persistant de vasopresseur."),
  ("Dobutamine en première ligne","Le vasopresseur de première ligne est la noradrénaline."),
  ("Attendre le résultat des hémocultures","Les cultures ne modifient pas la prise en charge hémodynamique immédiate.")],
 "Hypotension persistante après remplissage avec lactate > 2 mmol/L : choc septique (DX.11). La noradrénaline vise une PAM de 65 mmHg ; elle peut passer par une voie périphérique en attendant la voie centrale.",
 "Choc septique : mortalité hospitalière > 40 %.",
 B(11,10))

q("R","DX.12 vs DX.11 · purpura fébrile","management","domicile",
 "Une étudiante de 19 ans a 40 °C, des céphalées et des vomissements depuis 6 heures. Le médecin de garde découvre des taches violacées des jambes qui ne s'effacent pas à la pression. PA 96/60 mmHg.",
 "Quelle est la conduite immédiate la plus appropriée ?",
 [("Ceftriaxone i.v. immédiate, puis transfert",""),
  ("Ponction lombaire avant tout antibiotique","Le purpura fébrile impose l'antibiotique avant tout examen."),
  ("Scanner cérébral, puis antibiotique","L'imagerie ne doit pas retarder l'antibiotique."),
  ("Paracétamol et contrôle dans 6 heures","La méningococcie évolue en heures vers le choc."),
  ("Prélever une sérologie et attendre le résultat","Aucun examen ne justifie d'attendre devant un purpura fébrile.")],
 "Un purpura fébrile est une méningococcémie jusqu'à preuve du contraire (DX.12, 🚩 E3). La ceftriaxone se donne immédiatement, avant toute imagerie ou ponction, puis le patient est isolé par gouttelettes.",
 "Létalité de l'infection invasive à méningocoques en Suisse : 7,3 %.",
 B(12,13))

q("R","DX.12 · conscient, sans déficit","management","urgences",
 "Un homme de 34 ans consulte pour céphalée intense, fièvre à 39,4 °C et raideur de nuque depuis 12 heures. Glasgow 15, aucun déficit focal, pas de crise, pas de purpura. Les hémocultures sont prélevées.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Ponction lombaire, puis dexaméthasone et antibiotique",""),
  ("Scanner cérébral avant toute ponction","Sans trouble de conscience, déficit ni crise, l'imagerie n'est pas requise."),
  ("Aciclovir seul en attendant le LCR","La méningite bactérienne reste à couvrir en premier."),
  ("Antibiotique oral à domicile et contrôle clinique à 24 heures","La méningite bactérienne évolue en heures."),
  ("IRM cérébrale programmée dans la semaine","Le délai est incompatible avec l'urgence.")],
 "Conscience conservée, sans déficit focal ni crise nouvelle : la ponction lombaire se fait sans délai, puis dexaméthasone et antibiotique (DX.12). L'antibiotique démarre si possible dans l'heure suivant l'arrivée.",
 "Le scanner d'abord seulement si conscience altérée, déficit focal, crise nouvelle, œdème papillaire ou immunodépression.",
 B(12,10))

q("R","DX.12 · conscience altérée","management","urgences",
 "Une femme de 45 ans est amenée fébrile à 39,8 °C, avec raideur de nuque. Glasgow 9. Elle a convulsé dans l'ambulance. Les hémocultures viennent d'être prélevées.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Dexaméthasone et antibiotique, puis scanner",""),
  ("Scanner, puis décision de l'antibiotique","L'imagerie ne doit pas retarder l'antibiotique."),
  ("Ponction lombaire immédiate, sans imagerie préalable","Coma et crise imposent l'imagerie avant la ponction."),
  ("EEG, puis traitement selon le tracé","L'EEG ne précède pas le traitement de la méningite."),
  ("Dexaméthasone seule en attendant le LCR","La dexaméthasone accompagne l'antibiotique ; elle ne le remplace pas.")],
 "Trouble de conscience sévère ou crise nouvelle : hémocultures, dexaméthasone et antibiotique d'abord, puis tomodensitométrie, puis ponction si l'imagerie ne la contre-indique pas (DX.12).",
 "La dexaméthasone se donne juste avant ou avec la première dose d'antibiotique (essai de Gans : RR de décès 0,48).",
 B(12,14))

q("R","DX.15 · coureur confus","management","terrain",
 "Un coureur de 28 ans s'effondre au 18e kilomètre d'un semi-marathon par 31 °C. Il est agité et désorienté. Sa peau est moite. Température rectale 41,2 °C.",
 "Quel est le premier geste le plus approprié ?",
 [("Immersion du corps en eau froide",""),
  ("Paracétamol 1 g i.v.","La consigne hypothalamique est normale : l'antipyrétique n'agit pas."),
  ("Bilan sanguin complet avant tout refroidissement","On refroidit avant les examens."),
  ("Boisson sucrée et repos à l'ombre","Réponse de l'épuisement par la chaleur, pas d'un coup de chaleur."),
  ("Scanner cérébral pour la confusion","La confusion s'explique par l'hyperthermie ; refroidir d'abord.")],
 "Température centrale > 40 °C avec dysfonction neurologique après effort : coup de chaleur d'effort (DX.15, 🚩 E1). L'immersion en eau froide du corps entier refroidit le plus vite ; on appelle le 144.",
 "La peau peut rester moite dans la forme d'effort ; la sueur n'exclut pas le diagnostic.",
 B(15,14))

q("R","DX.15 · personne âgée en canicule","management","domicile",
 "Une femme de 86 ans est trouvée somnolente dans son appartement surchauffé pendant une canicule. Température rectale 40,8 °C. Aucun foyer infectieux apparent.",
 "Quelle est la conduite la plus appropriée ?",
 [("Refroidissement actif immédiat et appel du 144",""),
  ("Ibuprofène 400 mg et surveillance","Les antipyrétiques n'agissent pas dans l'hyperthermie."),
  ("Hémocultures et attente des résultats","Le refroidissement passe avant les examens."),
  ("Couverture chauffante pour calmer les frissons ressentis","Elle aggrave l'hyperthermie."),
  ("Hospitalisation programmée le lendemain","Chaque minute de température élevée aggrave le pronostic.")],
 "Coup de chaleur classique (exposition passive) : sortir de la chaleur, retirer les vêtements, appeler le 144, refroidir sans délai (DX.15). Mortalité en soins intensifs : 63,2 % dans la forme classique.",
 "La durée de la température élevée détermine les lésions.",
 B(15,8))

q("R","DX.14 · fièvre sous chimiothérapie","management","urgences",
 "Une femme de 52 ans sous chimiothérapie pour un cancer du sein (dernière cure il y a 9 jours) a 38,6 °C. Elle se sent bien. PA 124/76 mmHg. Aucun foyer à l'examen.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Formule sanguine et hémocultures en urgence",""),
  ("Paracétamol et contrôle dans 48 heures","Toute fièvre sous chimiothérapie est une urgence."),
  ("Radiographie de thorax seule","La numération oriente d'abord la conduite."),
  ("Attendre un foyer clinique avant tout bilan","Sans neutrophiles, les signes locaux manquent."),
  ("CRP seule pour décider","Une CRP normale ne rassure pas chez le neutropénique.")],
 "Toute fièvre sous chimiothérapie impose une formule sanguine en urgence (DX.14, 🚩 E4). Si les neutrophiles sont < 0,5 G/L : deux séries d'hémocultures puis antibiotique i.v. dans l'heure suivant le triage.",
 "La fièvre est parfois le seul signe d'infection chez le neutropénique.",
 B(14,13))

q("R","DX.14 · neutrophiles effondrés","management","urgences",
 "Un homme de 60 ans traité pour un lymphome a 38,9 °C. Neutrophiles 0,2 G/L. PA 118/70 mmHg, aucun foyer. Les hémocultures sont prélevées.",
 "Quel traitement est le plus approprié ?",
 [("Pipéracilline-tazobactam i.v. dans l'heure",""),
  ("Amoxicilline orale et contrôle à 48 heures","Le spectre et la voie sont inadaptés au neutropénique à haut risque."),
  ("Ceftriaxone i.m. dose unique","Elle ne couvre pas Pseudomonas."),
  ("Filgrastim seul","Il raccourcit la neutropénie ; il ne remplace pas l'antibiotique."),
  ("Antibiotique après le résultat des hémocultures","L'antibiotique ne doit pas attendre les cultures.")],
 "Neutropénie fébrile à haut risque : une bêtalactamine antipseudomonale en monothérapie i.v. dans l'heure (pipéracilline-tazobactam, céfépime ou méropénème) (DX.14).",
 "Céfépime : 2 g toutes les 8 h ; méropénème : 1 g toutes les 8 h (AIPS).",
 B(14,11))

q("R","DX.6 · retour d'Afrique","assessment_diagnosis","cabinet",
 "Un ingénieur de 41 ans rentré du Cameroun il y a 10 jours consulte pour fièvre à 39 °C, frissons et céphalées depuis 2 jours. Il a pris une prophylaxie antipaludique. Examen sans foyer.",
 "Quel examen faut-il demander en premier ?",
 [("Test rapide et frottis-goutte épaisse le jour même",""),
  ("Sérologie de la dengue, à répéter dans deux semaines","Le paludisme, mortel, passe en premier."),
  ("Aucun test grâce à la prophylaxie","La prophylaxie ne protège pas totalement."),
  ("Radiographie de thorax seule","Sans signe respiratoire, elle n'exclut pas le paludisme."),
  ("Coproculture et contrôle à 1 semaine","Le délai est dangereux pour un P. falciparum.")],
 "Toute fièvre au retour d'une zone d'endémie se teste le jour même par test rapide, frottis et goutte épaisse, même sous prophylaxie (DX.6, 🚩 E5).",
 "Le paludisme représente 21,1 % des fièvres aiguës sans foyer chez 455 voyageurs européens.",
 B(6,14))

q("R","DX.6 vs DX.7 · frottis négatif","assessment_diagnosis","urgences",
 "Une femme de 29 ans revient du Mali il y a 8 jours et a 39,5 °C avec des frissons. Le test rapide et le frottis sont négatifs. Plaquettes 98 G/L. Elle reste fébrile.",
 "Quelle est la conduite la plus appropriée ?",
 [("Répéter les tests du paludisme à 12–24 h",""),
  ("Exclure le paludisme et la renvoyer à domicile","Un premier test négatif n'exclut pas : la parasitémie peut être basse."),
  ("Artésunate i.v. sans nouveau test","Le traitement se décide sur un diagnostic parasitologique."),
  ("Corticoïde d'épreuve","Aucune place dans une fièvre aiguë du voyageur."),
  ("Sérologie palustre dans 3 semaines","Elle ne sert pas au diagnostic de l'accès aigu.")],
 "Une parasitémie basse échappe au premier examen : on répète frottis et test rapide à 12–24 h si la suspicion persiste, et l'on cherche la dengue ou une bactérie (DX.6, DX.7).",
 "La thrombopénie oriente mais ne prouve pas le paludisme.",
 B(6,10))

q("R","DX.6 · paludisme grave","management","urgences",
 "Un homme de 50 ans revenu du Ghana a 40 °C. Il est confus. Frottis : P. falciparum, parasitémie 12 %. Glycémie 3,1 mmol/L, créatinine en hausse.",
 "Quel traitement est le plus approprié ?",
 [("Artésunate i.v. en soins intensifs",""),
  ("Riamet® per os avec un repas gras","Riamet® est contre-indiqué dans le paludisme grave (AIPS)."),
  ("Malarone® 4 comprimés par jour pendant 3 jours","La voie orale ne convient pas à un paludisme grave."),
  ("Hydroxychloroquine 800 mg","Elle n'est pas indiquée dans le paludisme grave à P. falciparum."),
  ("Doxycycline seule","Elle n'est pas un schizonticide rapide.")],
 "Confusion, hypoglycémie, atteinte rénale et parasitémie ≥ 10 % : paludisme grave (DX.6). Artésunate i.v. en soins intensifs, au moins 24 h, puis cure orale complète de 3 jours ; on corrige l'hypoglycémie.",
 "La quinine reste l'alternative si l'artésunate manque ; surveiller l'hémolyse après le traitement.",
 B(6,11))

q("R","DX.13 vs DX.11 · fièvre et drogues injectées","assessment_diagnosis","urgences",
 "Un homme de 32 ans qui s'injecte des drogues a de la fièvre à 39 °C depuis 5 jours. Souffle systolique nouveau au bord gauche du sternum. PA 120/70 mmHg.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Trois paires d'hémocultures avant l'antibiotique",""),
  ("Antibiotique empirique immédiat sans prélèvement","Un antibiotique préalable rend les hémocultures négatives."),
  ("Échocardiographie seule, sans hémocultures","Microbiologie et imagerie sont deux critères majeurs."),
  ("Une hémoculture unique, puis attente","Une hémoculture isolée ne suffit pas."),
  ("CRP et contrôle à 1 semaine","Le retard de traitement augmente la mortalité.")],
 "Fièvre avec drogues injectées et souffle nouveau : endocardite à évoquer (DX.13, 🚩 E6). On prélève trois paires d'hémocultures avant tout antibiotique, puis échocardiographie et avis de l'équipe d'endocardite.",
 "Patient stable : le prélèvement correct passe avant l'antibiotique.",
 B(13,13))

q("R","DX.13 · ETT négative","assessment_diagnosis","hôpital",
 "Une femme de 70 ans porteuse d'une prothèse valvulaire aortique a de la fièvre depuis 10 jours. Deux hémocultures sur trois montrent Staphylococcus aureus. L'échocardiographie transthoracique est normale.",
 "Quel examen faut-il demander ensuite ?",
 [("Échocardiographie transœsophagienne",""),
  ("Aucun : l'ETT normale exclut l'endocardite","Une ETT négative n'exclut pas l'endocardite."),
  ("Radiographie de thorax","Elle ne montre pas les lésions valvulaires."),
  ("Nouvelle ETT dans 6 mois","Le délai est incompatible avec la gravité."),
  ("Ponction lombaire","Elle n'a pas sa place sans signe méningé.")],
 "Suspicion forte avec ETT négative : passer à la voie transœsophagienne, puis scanner ou TEP au FDG si besoin (Duke-ISCVID 2023) (DX.13).",
 "Germe typique dans au moins deux hémocultures = critère majeur.",
 B(13,10))

q("R","DX.1 · score à 0","management","cabinet",
 "Un homme de 45 ans sans antécédent a de la toux, une fièvre à 38,7 °C et des crépitants basaux droits. Radiographie : opacité nouvelle du lobe inférieur droit. Conscience normale, FR 18/min, PA 132/80 mmHg. Il vit avec sa femme.",
 "Quel traitement est le plus approprié ?",
 [("Co-amoxicilline 2 × 1 g/j per os, contrôle à 48–72 h",""),
  ("Ceftriaxone i.v. en hospitalisation","Score à 0 et contexte sûr : le domicile suffit."),
  ("Oseltamivir seul","Il ne traite pas une pneumonie bactérienne."),
  ("Pas d'antibiotique, réévaluation clinique dans une semaine","Une pneumonie radiologique se traite."),
  ("Ciprofloxacine 2 × 500 mg/j","Elle ne cible pas en premier le pneumocoque.")],
 "Pneumonie communautaire avec score de gravité à 0 et contexte sûr : traitement ambulatoire par amoxicilline-acide clavulanique 2 × 1000 mg ou 3 × 625 mg par jour, réévaluation à 48–72 h (DX.1).",
 "Mortalité à 30 jours : 0,7 % avec un CURB-65 à 0.",
 B(1,10))

q("R","DX.1 vs DX.11 · pneumonie sévère","management","urgences",
 "Une femme de 78 ans a une pneumonie lobaire. Elle est confuse. FR 32/min, PA 86/54 mmHg, urée élevée.",
 "Quel traitement antibiotique est le plus approprié ?",
 [("Ceftriaxone et clarithromycine i.v., soins intensifs",""),
  ("Co-amoxicilline per os à domicile","Score très élevé : hospitalisation et voie i.v."),
  ("Doxycycline 100 mg per os","Inadaptée à une pneumonie sévère."),
  ("Clarithromycine seule per os","Le pneumocoque doit être couvert par une bêtalactamine i.v."),
  ("Antibiotique seulement après le résultat de l'antigène urinaire","L'antibiotique ne doit pas attendre les résultats.")],
 "Confusion, FR ≥ 30/min, PA basse, urée et âge : score de gravité maximal (DX.1, DX.11). Hospitalisation, ceftriaxone i.v. 1 à 2 g/j associée à la clarithromycine i.v. 500 mg 2 fois par jour, 5 jours au maximum ; évaluer les soins intensifs.",
 "CURB-65 à 4 : mortalité à 30 jours 41,5 %.",
 B(1,14))

q("R","DX.2 · pyélonéphrite simple","management","cabinet",
 "Une femme de 31 ans, non enceinte, sans antécédent, a 38,9 °C, des brûlures mictionnelles et une douleur lombaire droite. Ébranlement positif. Elle boit et tolère les comprimés. Bandelette : leucocytes et nitrites positifs.",
 "Quelle est la conduite la plus appropriée ?",
 [("Uroculture, puis ciprofloxacine 2 × 500 mg/j 7 jours",""),
  ("Fosfomycine en dose unique","Traitement de la cystite, pas de l'atteinte rénale."),
  ("Hospitalisation et ceftriaxone i.v. pendant au moins 7 jours","Forme simple sans sepsis : la voie orale suffit."),
  ("Antibiotique sans uroculture préalable","La culture se prélève avant l'antibiotique."),
  ("Scanner abdominal en urgence","L'imagerie est réservée au choc, à l'obstruction ou à l'échec à 72 h.")],
 "Pyélonéphrite simple de la femme non enceinte : ECBU avant l'antibiotique, puis ciprofloxacine 500 mg deux fois par jour pendant 7 jours (AIPS) (DX.2). Réévaluation à 48–72 h.",
 "Guérison clinique 97 % à 7 jours, non inférieure à 14 jours (essai suédois).",
 B(2,13))

q("R","DX.2 vs DX.11 · obstruction et choc","management","urgences",
 "Un homme de 66 ans avec un calcul urétéral gauche connu a 39,6 °C, des frissons et une douleur lombaire. PA 84/50 mmHg. L'échographie montre une dilatation des cavités gauches.",
 "Quelle est la conduite la plus appropriée après les hémocultures ?",
 [("Ceftriaxone i.v. et drainage urologique urgent",""),
  ("Ciprofloxacine per os et contrôle à 72 h","Choc et obstruction imposent l'hospitalisation et le drainage."),
  ("Antalgique et attente de l'expulsion du calcul","Une obstruction infectée ne se surveille pas."),
  ("Antibiotique i.v. seul, sans geste urologique","L'antibiotique ne stérilise pas une cavité obstruée."),
  ("Lithotripsie programmée dans 2 semaines","Le drainage est urgent, la lithotripsie différée.")],
 "Pyélonéphrite obstructive avec sepsis : antibiotique i.v. (ceftriaxone), remplissage, puis avis urologique et drainage en urgence (DX.2, DX.11).",
 "Une obstruction infectée exige un drainage en plus de l'antibiotique.",
 B(2,11), niv="specialiste", spe="Urologie")

q("R","DX.3 · douleur disproportionnée","management","urgences",
 "Un homme diabétique de 58 ans a une rougeur de la cuisse apparue hier. La douleur est intense, sans commune mesure avec l'aspect de la peau. Bulles violacées. FC 122/min, PA 94/58 mmHg.",
 "Quelle est la conduite la plus appropriée ?",
 [("Avis chirurgical immédiat pour exploration",""),
  ("Flucloxacilline per os et contrôle à 48 h","Fasciite suspectée : la chirurgie seule sauve le tissu."),
  ("Marquer la limite et réévaluer demain","Le délai fait progresser la nécrose en heures."),
  ("IRM avant toute décision","L'imagerie ne doit pas retarder la chirurgie."),
  ("Calculer le LRINEC et opérer seulement s'il est ≥ 6","Un LRINEC bas n'exclut pas la fasciite ; la clinique l'emporte.")],
 "Douleur disproportionnée, bulles et choc : fasciite nécrosante jusqu'à preuve du contraire (DX.3). Antibiotique large i.v. avec clindamycine, et exploration-débridement chirurgical en urgence.",
 "La confondre avec une cellulite simple retarde le débridement.",
 B(3,10))

q("R","DX.4 · FUO stable","management","policlinique",
 "Une femme de 48 ans a de la fièvre documentée à 38,5 °C à plusieurs reprises depuis 5 semaines. Anamnèse, examen, laboratoire de base, radiographie du thorax et échographie abdominale sont sans diagnostic. Elle est stable. VIH négatif.",
 "Quelle est la conduite la plus appropriée ?",
 [("Aucun antibiotique ; poursuivre le bilan",""),
  ("Essai d'amoxicilline-acide clavulanique 10 jours","L'antibiotique d'épreuve masque la cause."),
  ("Prednisone 40 mg d'épreuve","Le corticoïde masque un lymphome ou une infection."),
  ("Arrêt des investigations et réassurance","Il faut poursuivre la recherche structurée."),
  ("Antibiothérapie large i.v. en hospitalisation","Aucun signe d'instabilité ne la justifie.")],
 "Trois semaines ou plus, 38,3 °C documentés deux fois, sans immunosuppression, bilan de base négatif : FUO (DX.4). Chez le patient stable, ni antibiotique ni corticoïde d'épreuve : ils masquent la cause.",
 "Arrêter ou remplacer tous les médicaments, même anciens, et conserver un sérum de départ.",
 B(4,13))

q("R","DX.4 · FUO et VS élevée","assessment_diagnosis","hôpital",
 "Un homme de 63 ans a une FUO depuis 6 semaines. Le bilan de base est négatif. VS 78 mm/h, CRP 64 mg/L. Il est stable.",
 "Quel examen a le meilleur rendement à ce stade ?",
 [("FDG-TEP-TDM",""),
  ("Scanner thoraco-abdominal seul","Rendement de 25 à 35 %, inférieur au TEP."),
  ("Scintigraphie osseuse","Elle n'est pas l'examen de choix de la FUO."),
  ("IRM cérébrale","Sans signe neurologique, rendement faible."),
  ("Répéter l'échographie abdominale","Elle a déjà été faite sans diagnostic.")],
 "FUO avec VS ou CRP élevée : FDG-TEP-TDM tôt, puis biopsie de la cible (DX.4). Rendement de 40 à 60 % contre 25 à 35 % pour le scanner.",
 "Avec VS et CRP normales, le TEP n'a aidé aucun patient dans l'étude néerlandaise.",
 B(4,14))

q("R","DX.5 · céphalée et vue","management","cabinet",
 "Une femme de 74 ans a une céphalée temporale nouvelle, une claudication de la mâchoire et une baisse de vision de l'œil droit depuis ce matin. Fébricule à 38,1 °C. VS 92 mm/h.",
 "Quelle est la conduite la plus appropriée ?",
 [("Corticothérapie le jour même, sans attendre la biopsie",""),
  ("Biopsie de l'artère temporale d'abord, puis traitement selon l'histologie","La perte visuelle est irréversible : on traite d'abord."),
  ("AINS et contrôle dans 1 semaine","Traitement inadapté de l'artérite."),
  ("TEP au FDG avant de décider","L'imagerie ne doit pas retarder les corticoïdes."),
  ("Antibiotique empirique pour la fièvre","Le tableau est inflammatoire, non infectieux.")],
 "Après 50 ans, céphalée nouvelle et trouble visuel : artérite à cellules géantes (DX.5). Corticothérapie immédiate, hospitalisation et avis ophtalmologique le jour même ; échographie ou biopsie ensuite.",
 "Classification ACR/EULAR 2022 : sensibilité 87,0 %, spécificité 94,8 %.",
 B(5,14))

q("R","DX.7 · défervescence","management","cabinet",
 "Un homme de 36 ans rentré de Thaïlande a une dengue confirmée par NS1. Au 6e jour, la fièvre tombe et il se dit mieux, mais il a une douleur abdominale intense et vomit à répétition.",
 "Quelle est la conduite la plus appropriée ?",
 [("Hospitalisation pour surveillance stricte",""),
  ("Retour à domicile, la fièvre ayant disparu","La défervescence est la phase critique de la dengue."),
  ("Ibuprofène pour la douleur","Les AINS augmentent le risque hémorragique."),
  ("Transfusion de plaquettes préventive","Aucune indication préventive ; risque de surcharge."),
  ("Corticoïde i.v.","Les corticoïdes n'ont pas de place dans la dengue.")],
 "Douleur abdominale intense et vomissements persistants : signes d'alarme, à la défervescence qui est la phase critique (DX.7). Hospitalisation, hydratation et contrôles répétés de l'hématocrite et des signes vitaux.",
 "La fuite plasmatique peut apparaître au moment où la fièvre tombe.",
 B(7,14))

q("R","DX.7 vs DX.6 · NS1 positif","assessment_diagnosis","urgences",
 "Une femme de 27 ans rentre du Burkina Faso, où circulent paludisme et dengue. Fièvre à 39,4 °C depuis 3 jours, myalgies, douleur rétro-orbitaire. L'antigène NS1 de la dengue revient positif.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Test rapide et frottis du paludisme le jour même",""),
  ("Arrêter toute recherche : la dengue est confirmée","Le paludisme se cherche quand même : il est mortel et peut coexister."),
  ("Sérologie IgG de la dengue","Les IgG ne servent pas au diagnostic aigu."),
  ("Ibuprofène et retour à domicile","Les AINS sont à éviter dans la dengue."),
  ("Corticoïde pour prévenir le choc","Aucune place des corticoïdes.")],
 "Devant une fièvre au retour des tropiques, le paludisme s'exclut le jour même par test rapide et frottis, même si une autre cause est trouvée (DX.7, DX.6).",
 "La dengue représente 85,2 % des arboviroses chez 455 voyageurs fébriles européens.",
 B(7,14))

q("R","DX.9 · grippe chez un patient à risque","management","cabinet",
 "Un homme de 72 ans avec une BPCO a, depuis hier soir, une fièvre brutale à 39 °C, des frissons, une toux et des courbatures. C'est l'épidémie de grippe. SpO2 95 %, auscultation normale. Clairance de la créatinine 80 mL/min.",
 "Quel traitement est le plus approprié ?",
 [("Oseltamivir 75 mg 2×/j pendant 5 jours",""),
  ("Co-amoxicilline 2 × 1 g/j pendant 7 jours","Les antibiotiques ne traitent pas la grippe."),
  ("Oseltamivir 30 mg 1×/j","Dose réservée à une clairance de 10 à 30 mL/min."),
  ("Traitement symptomatique seul","Le terrain à risque justifie l'antiviral précoce."),
  ("Prednisone 40 mg pendant 5 jours","Aucune indication dans la grippe non compliquée.")],
 "Grippe sur terrain à risque, vue dans les 36 premières heures : oseltamivir 75 mg deux fois par jour pendant 5 jours (AIPS Tamiflu®) (DX.9).",
 "Sous oseltamivir, les hospitalisations toutes causes passent de 1,7 % à 0,6 %.",
 B(9,13))

q("R","DX.9 vs DX.1 · fièvre qui repart","assessment_diagnosis","cabinet",
 "Une femme de 67 ans a eu une grippe confirmée il y a 6 jours. Elle allait mieux, mais la fièvre repart à 39 °C avec une toux productive. Crépitants à la base gauche.",
 "Quel examen faut-il demander ?",
 [("Radiographie du thorax",""),
  ("Nouvelle PCR grippale","Elle ne recherche pas la surinfection bactérienne."),
  ("Sérologie grippale","Sans intérêt pour la décision."),
  ("Aucun examen, poursuivre le symptomatique","Fièvre qui repart et signe focal évoquent une surinfection."),
  ("Échocardiographie","Pas d'indication sans souffle ni facteur de risque.")],
 "Fièvre qui repart après amélioration ou crépitants focaux : radiographie du thorax à la recherche d'une pneumonie (DX.9, DX.1).",
 "Les antibiotiques traitent la surinfection, pas la grippe.",
 B(9,10))

q("R","DX.10 · déshydratation modérée","management","cabinet",
 "Un garçon de 3 ans, 14 kg, a des vomissements et une diarrhée aqueuse depuis 1 jour, dans un contexte d'épidémie à la crèche. Il a soif, urine peu, pli cutané discret. Conscience normale.",
 "Quel traitement est le plus approprié ?",
 [("Réhydratation orale 40–50 mL/kg en 4–6 h",""),
  ("Perfusion i.v. d'emblée à l'hôpital, puis réévaluation","La voie orale est supérieure ; la perfusion est réservée à l'échec."),
  ("Lopéramide","Interdit avant 6 ans."),
  ("Diète hydrique stricte de 24 heures","L'alimentation habituelle se poursuit."),
  ("Antibiotique empirique","Il n'est pas indiqué en routine.")],
 "Déshydratation modérée (perte de 5 à 8 % du poids) : solution de réhydratation orale 40 à 50 mL/kg dans les 4 à 6 premières heures, soit 560 à 700 mL pour 14 kg (DX.10).",
 "L'enfant qui vomit reçoit de petites quantités fréquentes.",
 B(10,14))

q("R","DX.10 · diarrhée sanglante fébrile","management","cabinet",
 "Un homme de 42 ans a une diarrhée sanglante depuis 2 jours, avec 39,2 °C et des crampes abdominales. Pas de voyage récent. Il boit sans difficulté.",
 "Quelle est la conduite la plus appropriée ?",
 [("Coproculture ou PCR, sans lopéramide",""),
  ("Lopéramide pour réduire les selles","Contre-indiqué dans l'entérite invasive fébrile."),
  ("Ondansétron et retour à domicile","Il ne répond pas au problème et n'a pas d'indication AIPS ici."),
  ("Ciprofloxacine d'emblée sans prélèvement","Pas d'antibiotique avant d'écarter un EHEC."),
  ("Coloscopie en urgence","Elle n'est pas le premier examen.")],
 "Sang dans les selles et fièvre élevée : entérite invasive à documenter par coproculture ou PCR (DX.10). Le lopéramide est contre-indiqué, et l'on écarte une colite ou un EHEC avant tout traitement.",
 "La réhydratation reste le traitement principal.",
 B(10,10))

q("R","DX.8 vs DX.5 · ganglions et fièvre","management","policlinique",
 "Un homme de 57 ans a une fièvre à 38,6 °C depuis 4 semaines, des sueurs nocturnes, une perte de 6 kg et des adénopathies cervicales fermes de 2 cm. Il est stable.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Biopsie ganglionnaire",""),
  ("Prednisone 50 mg d'épreuve","Sans histologie, elle masque un lymphome."),
  ("Antibiotique d'épreuve 2 semaines","Il retarde le diagnostic chez un patient stable."),
  ("Surveillance à 3 mois","Les signes généraux imposent un diagnostic rapide."),
  ("Dosage de marqueurs tumoraux seuls","Ils ne posent pas le diagnostic de néoplasie.")],
 "Fièvre prolongée, sueurs nocturnes, perte de poids et adénopathie : néoplasie, surtout lymphome, à prouver par l'histologie (DX.8). On biopsie la lésion accessible ; aucun corticoïde avant la biopsie.",
 "FUO néoplasique : mortalité de 38 % à 6 mois, la plus élevée.",
 B(8,14))

q("R","DX.3 · cellulite simple","management","cabinet",
 "Une femme de 55 ans a une rougeur chaude, douloureuse et bien limitée de la jambe gauche depuis 2 jours, avec un intertrigo des orteils. 38,4 °C. Pas de douleur disproportionnée. FC 88/min.",
 "Quelle est la conduite la plus appropriée ?",
 [("Bêtalactamine orale, limites marquées, contrôle à 48 h",""),
  ("Hospitalisation et antibiotique i.v. jusqu'à l'apyrexie complète","Forme non compliquée et stable : traitement ambulatoire."),
  ("Hémocultures systématiques avant traitement","Rarement positives dans la cellulite simple."),
  ("Compression et soins cutanés sans antibiotique","Conduite de la dermite de stase, pas de la cellulite."),
  ("Exploration chirurgicale","Aucun signe de fasciite nécrosante.")],
 "Cellulite non purulente stable : bêtalactamine orale active sur le streptocoque, limites marquées au feutre, élévation du membre et traitement de la porte d'entrée, contrôle à 48 h (DX.3).",
 "Traiter 5 jours si l'amélioration est nette (IDSA).",
 B(3,13))

# ═════════════ BLOC D · DISCRIMINER (un signe, un examen qui tranche)
q("D","DX.1 vs DX.9 · radiographie normale","assessment_diagnosis","urgences",
 "Un homme de 59 ans a, depuis 24 heures, une fièvre à 39 °C, une toux et une douleur pleurale droite. Crépitants focaux à droite, FR 24/min. La radiographie du thorax initiale ne montre pas d'opacité.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("TDM thoracique ou nouvelle radiographie",""),
  ("Conclure à une bronchite virale et arrêter","La radiographie peut être normale au début ; la clinique prime."),
  ("Spirométrie","Elle n'explore pas une condensation."),
  ("Bronchoscopie en urgence","Examen invasif sans indication de première ligne."),
  ("Échocardiographie","Rien n'oriente vers une cause cardiaque.")],
 "Au début d'une pneumonie, la radiographie peut sembler normale (DX.1). Si la clinique est évocatrice, on répète l'imagerie ou l'on demande une TDM avant de conclure à une autre cause (DX.9).",
 "Le diagnostic exige une opacité nouvelle : c'est le critère décisif.",
 B(1,14))

q("D","DX.1 · critère décisif","assessment_diagnosis","cabinet",
 "Une femme de 50 ans a une toux fébrile à 38,5 °C depuis 3 jours. CRP 85 mg/L. Crépitants isolés à la base gauche.",
 "Quel élément pose le diagnostic de pneumonie communautaire ?",
 [("Opacité nouvelle à la radiographie",""),
  ("CRP supérieure à 50 mg/L au premier bilan","Une CRP élevée seule ne pose pas le diagnostic."),
  ("Score CURB-65 à 1","Il mesure la gravité, pas le diagnostic."),
  ("Fièvre de plus de 3 jours","La fièvre seule ne pose pas le diagnostic."),
  ("Crépitants à l'auscultation","Un crépitant isolé ne suffit pas.")],
 "La pneumonie associe un symptôme respiratoire aigu, un signe infectieux et une opacité nouvelle à l'imagerie (DX.1). L'opacité est le critère décisif, car la clinique seule manque de précision.",
 "Le score de gravité choisit le lieu de traitement, il ne pose pas le diagnostic.",
 B(1,8), niv="approfondissement")

q("D","DX.1 · hydrocortisone en soins intensifs","management","hôpital",
 "Un homme de 64 ans est admis aux soins intensifs pour une pneumonie communautaire sévère, sous ceftriaxone et clarithromycine. Il nécessite de l'oxygène à haut débit.",
 "Quel traitement adjuvant a réduit la mortalité à 28 jours dans l'essai CAPE COD ?",
 [("Hydrocortisone 200 mg/j i.v.",""),
  ("Dexaméthasone 0,15 mg/kg toutes les 6 heures","Schéma de la méningite bactérienne."),
  ("Oseltamivir 75 mg 2×/j","Antiviral de la grippe, non évalué dans cet essai."),
  ("Filgrastim","Indiqué selon l'hématologie dans la neutropénie, pas ici."),
  ("Méthylprednisolone 1 g/j pendant 3 jours","Schéma de l'artérite avec perte visuelle.")],
 "Dans l'essai CAPE COD (Dequin, NEJM 2023), l'hydrocortisone 200 mg/j i.v. pendant 4 à 8 jours, puis réduite, abaisse la mortalité à 28 jours de 11,9 % à 6,2 % (DX.1). Hors AIPS : à valider avec un spécialiste.",
 "Indication limitée aux formes graves en soins intensifs.",
 B(1,11), niv="specialiste", spe="Médecine intensive")

q("D","DX.2 · pyélonéphrite et grossesse","management","cabinet",
 "Une femme de 28 ans enceinte de 22 semaines a 39 °C, des frissons et une douleur lombaire droite. Bandelette positive.",
 "Quelle est la conduite la plus appropriée après l'uroculture ?",
 [("Hospitalisation et ceftriaxone i.v.",""),
  ("Ciprofloxacine 2 × 500 mg/j 7 jours","Contre-indiquée pendant la grossesse (AIPS)."),
  ("Lévofloxacine per os","Toute la classe des fluoroquinolones est évitée pendant la grossesse."),
  ("Fosfomycine en dose unique","Traitement de la cystite, pas de la pyélonéphrite."),
  ("Doxycycline 100 mg/j","À éviter pendant la grossesse.")],
 "Pyélonéphrite pendant la grossesse : forme compliquée (DX.2). Hospitalisation, ceftriaxone i.v. et avis obstétrical ; la ciprofloxacine est contre-indiquée selon l'AIPS.",
 "Le piège : croire les autres fluoroquinolones permises ; on choisit une bêtalactamine.",
 B(2,14))

q("D","DX.2 · fièvre persistante à 72 h","assessment_diagnosis","hôpital",
 "Une femme de 61 ans diabétique est traitée depuis 72 heures pour une pyélonéphrite par ceftriaxone, selon un antibiogramme sensible. Elle reste à 39 °C avec une douleur lombaire.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Échographie ou TDM des voies urinaires",""),
  ("Changer pour un carbapénème sans imagerie","Le germe est sensible : on cherche d'abord un foyer non drainé."),
  ("Arrêter l'antibiotique","L'infection n'est pas contrôlée."),
  ("Ajouter un antipyrétique et attendre","L'antipyrétique ne ferme aucune branche dangereuse."),
  ("Répéter seulement la bandelette","Elle n'explique pas l'échec.")],
 "Fièvre persistante après 72 heures d'antibiotique adapté : imagerie (échographie ou TDM) à la recherche d'une obstruction ou d'un abcès (DX.2).",
 "Une obstruction infectée exige un drainage.",
 B(2,13))

q("D","DX.3 vs pseudo-cellulite","assessment_diagnosis","EMS",
 "Une résidente d'EMS de 82 ans a les deux jambes rouges, froides et peu douloureuses depuis plusieurs semaines, avec des varices et un œdème. Apyrétique. Leucocytes normaux.",
 "Quel est le diagnostic le plus probable ?",
 [("Dermite de stase",""),
  ("Érysipèle bilatéral","Une cellulite bilatérale, froide et sans fièvre est improbable."),
  ("Fasciite nécrosante","Aucune douleur disproportionnée ni signe systémique."),
  ("Endocardite infectieuse","Aucun argument cardiaque ni fièvre."),
  ("Thrombose veineuse profonde bilatérale","Rougeur chronique froide bilatérale : imitateur cutané plus probable.")],
 "Rougeur bilatérale, froide, sans fièvre : pseudo-cellulite, en premier lieu la dermite de stase (DX.3). Compression et soins cutanés, sans antibiotique.",
 "Dermite de stase, eczéma et lymphœdème expliquent 54 % des erreurs devant une jambe rouge.",
 B(3,14))

q("D","DX.3 · LRINEC bas","assessment_diagnosis","urgences",
 "Un homme de 49 ans a une rougeur de l'avant-bras après une piqûre. Il décrit une douleur intense, croissante, disproportionnée. Le score LRINEC calculé est de 4.",
 "Quelle interprétation du score est correcte ?",
 [("Un score bas n'exclut pas la fasciite",""),
  ("Un score < 6 exclut la fasciite","La valeur prédictive négative de la cohorte de développement ne s'applique pas au cas clinique évocateur."),
  ("Le score pose le diagnostic de cellulite","Il ne confirme pas la cellulite."),
  ("Le score remplace l'avis chirurgical","La clinique l'emporte sur le score."),
  ("Le score doit être répété avant toute décision","Attendre un nouveau calcul retarde la chirurgie.")],
 "Le LRINEC (leucocytes, hémoglobine, sodium, glucose, créatinine, CRP) a montré une VPP de 92 % et une VPN de 96 % au seuil de 6 dans sa cohorte, mais un score bas n'exclut pas la fasciite nécrosante (DX.3). La douleur disproportionnée impose l'avis chirurgical.",
 "Signe d'appel principal : douleur disproportionnée aux signes cutanés.",
 B(3,8), niv="approfondissement")

q("D","DX.3 · allergie aux bêtalactamines","management","cabinet",
 "Une femme de 44 ans a une cellulite non compliquée du mollet. Elle a fait un choc anaphylactique sous amoxicilline.",
 "Quel antibiotique est le plus approprié ?",
 [("Clindamycine per os",""),
  ("Amoxicilline-acide clavulanique","Contre-indiquée en cas d'allergie aux pénicillines."),
  ("Flucloxacilline","Pénicilline : contre-indiquée."),
  ("Pénicilline V","Pénicilline : contre-indiquée."),
  ("Ceftriaxone i.m.","Risque croisé après une anaphylaxie aux bêtalactamines.")],
 "En cas d'allergie aux bêtalactamines, la clindamycine est l'alternative : 600 à 1200 mg/j per os en 3 ou 4 prises (AIPS Dalacin® C) (DX.3).",
 "La clindamycine bloque aussi la production de toxines dans les formes nécrosantes.",
 B(3,14), niv="specialiste", spe="Infectiologie")

q("D","DX.4 · 10 jours de fièvre","assessment_diagnosis","cabinet",
 "Un homme de 39 ans a de la fièvre depuis 10 jours, documentée à 38,6 °C. Il est stable. L'examen ne trouve pas de foyer.",
 "Quelle affirmation est correcte ?",
 [("Ce n'est pas encore une FUO",""),
  ("C'est une FUO : demander un FDG-TEP-TDM","La FUO exige 3 semaines ou plus et un bilan de base négatif."),
  ("C'est une FUO : débuter un antibiotique d'épreuve","Ni la définition ni la conduite ne sont remplies."),
  ("C'est une FUO de l'immunodéprimé","Rien n'indique une immunosuppression."),
  ("C'est une fièvre factice certaine","Rien ne permet de l'affirmer.")],
 "La FUO exige au moins 3 semaines de fièvre, 38,3 °C documentés deux fois, l'absence d'immunosuppression et un bilan de base négatif (DX.4). À 10 jours, on réévalue et on surveille.",
 "La durée seule ne suffit pas, une fièvre non objectivée non plus.",
 B(4,8))

q("D","DX.4 · corticothérapie au long cours","assessment_diagnosis","policlinique",
 "Une femme de 66 ans sous prednisone 15 mg/j pour une polyarthrite a de la fièvre depuis 4 semaines. Le bilan de base est négatif.",
 "Pourquoi ne parle-t-on pas de FUO classique ?",
 [("Le corticoïde ≥ 10 mg/j l'immunodéprime",""),
  ("La durée de la fièvre est inférieure à 3 semaines","Elle dépasse 3 semaines."),
  ("Le bilan de base n'a pas été fait","Il a été fait et il est négatif."),
  ("La fièvre n'est pas objectivée","Rien ne l'indique."),
  ("L'âge dépasse 65 ans","L'âge n'est pas un critère d'exclusion.")],
 "Critère d'immunité de la FUO : VIH négatif, immunoglobulines normales, pas de neutropénie, pas de corticoïde ≥ 10 mg de prednisone par jour (DX.4). Sinon, prise en charge de l'immunodéprimé.",
 "L'immunodéprimé fébrile suit une autre démarche, plus urgente.",
 B(4,8), niv="approfondissement")

q("D","DX.4 · VS et CRP normales","assessment_diagnosis","hôpital",
 "Un homme de 46 ans a une fièvre rapportée depuis 2 mois. Le bilan de base est négatif. VS et CRP sont normales à plusieurs reprises.",
 "Quelle démarche est la plus appropriée ?",
 [("Objectiver la fièvre devant témoin",""),
  ("FDG-TEP-TDM en urgence, puis biopsie de la cible","Avec VS et CRP normales, le TEP est peu utile."),
  ("Biopsie médullaire systématique","Aucune piste ne l'oriente."),
  ("Antibiotique d'épreuve 4 semaines","Il masque la cause."),
  ("Prednisone d'épreuve","Elle masque la cause.")],
 "Si la VS et la CRP sont normales, le PET n'a aidé aucun patient dans l'étude néerlandaise (DX.4). On objective la mesure devant témoin et l'on recherche une fièvre factice ou une fièvre périodique.",
 "Fièvre factice : température simulée ou provoquée, à mesurer devant témoin.",
 B(4,10), niv="approfondissement")

q("D","DX.5 vs DX.8 · pics quotidiens et éruption","assessment_diagnosis","hôpital",
 "Une femme de 31 ans a, depuis 5 semaines, des pics fébriles quotidiens à 39,5 °C, une éruption saumonée fugace, des arthralgies et un mal de gorge. Leucocytose. Facteur rhumatoïde et anticorps antinucléaires négatifs.",
 "Que faut-il faire avant de retenir une maladie de Still ?",
 [("Exclure infection et cancer",""),
  ("Rien : les critères de Yamaguchi suffisent","Les critères ne suffisent pas sans exclusion des infections et des cancers."),
  ("Biopsie de l'artère temporale","L'artérite à cellules géantes exige un âge ≥ 50 ans."),
  ("Débuter un antibiotique d'épreuve","Il masque une cause infectieuse."),
  ("Doser les IgG de la dengue","Sans voyage, rien ne l'oriente.")],
 "Maladie de Still de l'adulte : 5 critères de Yamaguchi dont 2 majeurs (sensibilité 96,2 %, spécificité 92,1 %), mais diagnostic d'exclusion : infection et cancer doivent être écartés (DX.5, DX.8).",
 "Maladie inflammatoire non infectieuse : 22 % des FUO néerlandaises.",
 B(5,13))

q("D","DX.5 · premier examen de l'ACG","assessment_diagnosis","policlinique",
 "Un homme de 71 ans a une céphalée temporale nouvelle et une raideur matinale des épaules, sans trouble visuel. CRP 48 mg/L. La prednisone est débutée.",
 "Quel examen d'imagerie vient en premier ?",
 [("Échographie des artères temporales et axillaires",""),
  ("Angiographie cérébrale par cathétérisme en urgence","Examen invasif sans place en première intention."),
  ("Scanner cérébral sans contraste","Il ne montre pas l'artérite."),
  ("Scintigraphie osseuse","Elle n'explore pas les artères."),
  ("IRM du rachis cervical","Sans rapport avec la question.")],
 "En cas de suspicion d'artérite à cellules géantes, l'échographie des artères temporales et axillaires vient en premier ; le signe du halo vaut 5 points dans la classification ACR/EULAR 2022 (DX.5).",
 "L'échographie ou la biopsie s'organise dans les jours qui suivent, sans retarder la prednisone.",
 B(5,14))

q("D","DX.5 · seuils de classification","mechanisms","policlinique",
 "Une femme de 68 ans est évaluée pour une artérite à cellules géantes. Le rhumatologue applique les critères ACR/EULAR 2022.",
 "Quels seuils biologiques rapportent 3 points ?",
 [("CRP ≥ 10 mg/L ou VS ≥ 50 mm/h",""),
  ("CRP ≥ 100 mg/L ou VS ≥ 100 mm/h","Seuils trop élevés : ce ne sont pas ceux du score."),
  ("Ferritine > 1000 µg/L","Évoque plutôt une maladie de Still ou un syndrome d'activation macrophagique."),
  ("Leucocytes > 15 G/L","Ce n'est pas un critère du score."),
  ("Procalcitonine > 0,5 µg/L","Marqueur d'infection bactérienne, hors du score.")],
 "Critères ACR/EULAR 2022 : âge ≥ 50 ans obligatoire ; biopsie positive ou halo +5 ; VS ≥ 50 mm/h ou CRP ≥ 10 mg/L +3 ; perte visuelle soudaine +3. Un score ≥ 6 classe l'ACG (DX.5).",
 "Ce sont des critères de classification pour la recherche : ils ne remplacent pas le jugement clinique.",
 B(5,8), niv="approfondissement")

q("D","DX.5 · ferritine et cytopénies","management","hôpital",
 "Une femme de 35 ans suivie pour une maladie de Still a une fièvre élevée, une bicytopénie et une ferritine très élevée. Elle se dégrade.",
 "Quelle est la conduite la plus appropriée ?",
 [("Soins intensifs, avis hématologique et rhumatologique",""),
  ("Naproxène et contrôle dans 1 semaine","Traitement du Still léger, inadapté à une complication grave."),
  ("Méthotrexate en urgence","Traitement de fond, pas de l'urgence."),
  ("Transfusion plaquettaire puis retour à domicile sous surveillance","Le syndrome menace la vie."),
  ("Biopsie de l'artère temporale","Sans rapport avec le tableau.")],
 "Cytopénies et ferritine très élevée chez un patient atteint de Still : suspicion de syndrome d'activation macrophagique (MAS). Hospitalisation en soins intensifs, avis de l'hématologue et du rhumatologue (DX.5).",
 "Le MAS est la complication grave à reconnaître dans le Still.",
 B(5,10), niv="specialiste", spe="Rhumatologie")

q("D","DX.6 · Riamet® non compliqué","management","hôpital",
 "Un homme de 38 ans, 75 kg, a un accès palustre à P. falciparum non compliqué (parasitémie 1 %). Il est conscient et ne vomit pas.",
 "Quel schéma de Riamet® est correct ?",
 [("4 cp à 0 et 8 h, puis 4 cp 2×/j 2 jours, avec des lipides",""),
  ("1 cp par jour pendant 3 jours","Dose très insuffisante."),
  ("4 cp en dose unique","Cure incomplète : 24 comprimés en 3 jours."),
  ("4 cp une fois par jour pendant 3 jours, à jeun, sans lipides","Schéma de Malarone® ; Riamet® se prend avec des lipides."),
  ("2 cp 2×/j pendant 7 jours","Schéma inexact.")],
 "Riamet® (AIPS) : 4 comprimés au diagnostic, 4 comprimés 8 h plus tard, puis 4 deux fois par jour pendant 2 jours, soit 24 comprimés, avec un aliment contenant des lipides (DX.6).",
 "Le P. falciparum non compliqué s'hospitalise pour observation et pour la première dose.",
 B(6,14))

q("D","DX.6 · seuil d'hyperparasitémie","mechanisms","hôpital",
 "Une femme de 45 ans a un P. falciparum avec une parasitémie de 6 %. Elle est consciente, sans hypoglycémie, sans atteinte rénale, sans détresse respiratoire.",
 "Comment classer cet accès selon l'OMS 2023 ?",
 [("Hyperparasitémie non compliquée",""),
  ("Paludisme grave","Le seuil de gravité de la parasitémie est ≥ 10 %."),
  ("Paludisme à P. vivax","L'espèce est P. falciparum."),
  ("Accès simple à faible parasitémie","Entre 4 et 10 %, on parle d'hyperparasitémie."),
  ("Paludisme cérébral","Elle est consciente.")],
 "Selon l'OMS 2023, une hyperparasitémie ≥ 10 % des globules rouges est un critère de gravité ; de 4 à 10 %, c'est une hyperparasitémie non compliquée (DX.6). Créatinine > 3 mg/dL, oligo-anurie, lactate ≥ 5 mmol/L et confusion prédisent la forme critique.",
 "La surveillance de la parasitémie continue jusqu'à sa négativation.",
 B(6,8), niv="approfondissement")

q("D","DX.6 · P. vivax","management","hôpital",
 "Un homme de 33 ans revenu d'Inde a un accès à P. vivax, traité par Riamet®. Il va mieux.",
 "Quelle étape reste nécessaire ?",
 [("Doser la G6PD, puis traiter les hypnozoïtes",""),
  ("Aucune : Riamet® élimine les formes hépatiques","Riamet® agit sur les formes sanguines, pas sur les hypnozoïtes."),
  ("Artésunate i.v. 3 jours","Réservé au paludisme grave."),
  ("Prophylaxie par Malarone® à vie","Ce n'est pas le traitement des formes dormantes."),
  ("Splénectomie","Aucune indication.")],
 "P. vivax et P. ovale rechutent à partir des hypnozoïtes hépatiques (DX.6). Après l'accès sanguin, un traitement contre les hypnozoïtes suit, après dosage de la G6PD.",
 "Le dosage de la G6PD précède le traitement des formes hépatiques.",
 B(6,10), niv="specialiste", spe="Médecine tropicale")

q("D","DX.7 · antipyrétique","management","cabinet",
 "Une femme de 30 ans, 60 kg, a une dengue confirmée sans signe d'alarme. Fièvre à 39 °C et myalgies. Elle boit bien.",
 "Quel antipyrétique est le plus approprié ?",
 [("Paracétamol, 4 g/j au maximum",""),
  ("Ibuprofène 400 mg 3×/j","Les AINS augmentent le risque hémorragique."),
  ("Acide acétylsalicylique 500 mg","L'aspirine est à éviter dans la dengue."),
  ("Métamizole i.v.","Réservé à la forte fièvre qui résiste, avec risque d'agranulocytose."),
  ("Naproxène 500 mg 2×/j","AINS : à éviter.")],
 "Dengue : paracétamol et hydratation ; l'aspirine et les AINS sont à éviter (risque hémorragique, recommandation OMS) (DX.7). Paracétamol 500 à 1000 mg par prise, au plus 4 g/j chez l'adulte.",
 "Le patient reçoit la liste écrite des signes d'alarme et reconsulte s'ils apparaissent.",
 B(7,14))

q("D","DX.7 · RT-PCR négative au 9e jour","assessment_diagnosis","policlinique",
 "Un homme de 40 ans rentré du Brésil a de la fièvre depuis 9 jours, une éruption et des myalgies. Paludisme exclu. La RT-PCR dengue est négative.",
 "Quel examen faut-il demander ?",
 [("IgM antidengue",""),
  ("Aucun : la dengue est exclue","Après le 7e jour, la virémie baisse et la RT-PCR perd sa sensibilité."),
  ("IgG antidengue sur un seul sérum","Les IgG persistent à vie et ne datent pas l'infection."),
  ("Nouvelle RT-PCR dans 1 semaine","La virémie aura encore baissé."),
  ("Antigène NS1 au 15e jour","Utile dans les 7 premiers jours.")],
 "RT-PCR et NS1 confirment la dengue dans les 7 premiers jours (DX.7). Après, on dose les IgM, détectables dès le 4e jour ; une IgM sur un seul sérum signe une dengue probable.",
 "Réactions croisées entre flavivirus : une IgM isolée ne donne pas la certitude.",
 B(7,8))

q("D","DX.7 · pression normale","assessment_diagnosis","hôpital",
 "Une femme de 25 ans hospitalisée pour une dengue avec signes d'alarme a une PA à 104/92 mmHg, une FC à 118/min et une recoloration capillaire allongée.",
 "Quelle interprétation est correcte ?",
 [("Pression pulsée étroite : choc débutant",""),
  ("PA normale : pas de choc","La pression pulsée se rétrécit avant l'effondrement de la systolique."),
  ("Tachycardie due seulement à la fièvre élevée","La pression pulsée étroite oriente vers la fuite plasmatique."),
  ("Hypertension réactionnelle","La diastolique élevée traduit la vasoconstriction."),
  ("Signe de guérison","La phase critique n'est pas terminée.")],
 "Dans la dengue, le choc se reconnaît d'abord par une pression pulsée étroite, une tachycardie et une recoloration lente, avant l'hypotension (DX.7). On traite alors comme une dengue sévère.",
 "Un choc reconnu tôt et traité diminue la mortalité d'au moins 20 fois.",
 B(7,14), niv="approfondissement")

q("D","DX.7 · IgG positives","assessment_diagnosis","cabinet",
 "Un voyageur de 52 ans fébrile depuis 3 jours au retour du Vietnam a des IgG antidengue positives sur un seul sérum. Il avait déjà voyagé en Asie.",
 "Quelle interprétation est correcte ?",
 [("Elles ne posent pas un diagnostic aigu",""),
  ("Elles confirment une dengue aiguë","Les IgG persistent à vie."),
  ("Elles excluent la dengue","Elles ne disent rien de l'épisode actuel."),
  ("Elles prédisent une dengue sévère","Aucune valeur pronostique ici."),
  ("Elles dispensent de tester le paludisme","Le paludisme se teste toujours le jour même.")],
 "Les IgG persistent à vie et réagissent avec les autres flavivirus et leurs vaccins : elles ne servent pas au diagnostic aigu (DX.7). Avant le 7e jour, on demande la RT-PCR ou le NS1.",
 "RT-PCR ou NS1 positifs ne prédisent pas la gravité.",
 B(7,8), niv="approfondissement")

q("D","DX.7 · choc de dengue","management","hôpital",
 "Un homme de 29 ans a une dengue sévère avec choc par fuite plasmatique. Plaquettes 18 G/L, sans saignement actif. Le remplissage par cristalloïde est en cours.",
 "Quelle mesure est la plus appropriée ?",
 [("Pas de plaquettes préventives ni de corticoïdes",""),
  ("Transfusion plaquettaire préventive","Elle favorise la surcharge liquidienne sans bénéfice."),
  ("Méthylprednisolone i.v.","Les corticoïdes ne sont pas indiqués."),
  ("Albumine en première intention","Le cristalloïde isotonique est la référence."),
  ("Remplissage libéral de 6 L de cristalloïde en 2 heures","On donne le volume minimal qui restaure la perfusion.")],
 "Choc de dengue : cristalloïde isotonique au volume minimal, diurèse cible ≥ 0,5 mL/kg/h ; transfusion de globules rouges seulement si saignement actif ; ni plaquettes préventives ni corticoïdes (DX.7).",
 "Les perfusions ne durent habituellement que 24 à 48 h, pendant la phase critique.",
 B(7,11), niv="specialiste", spe="Médecine intensive")

q("D","DX.8 · captation au TEP","assessment_diagnosis","hôpital",
 "Un homme de 68 ans a une FUO. Le FDG-TEP-TDM montre une captation intense d'un ganglion rétropéritonéal.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Biopsie de la zone captante",""),
  ("Chimiothérapie d'emblée","Sans histologie, la néoplasie n'est pas prouvée."),
  ("Conclure à un lymphome et adresser en soins palliatifs","La captation vaut aussi pour l'inflammation et l'infection."),
  ("Prednisone d'épreuve","Elle masque l'histologie."),
  ("Répéter le TEP dans 6 mois","Retarde le diagnostic.")],
 "Le FDG-PET/CT localise une zone à biopsier mais ne prouve pas la néoplasie : la captation vaut aussi pour l'inflammation et l'infection (DX.8). L'histologie seule pose le diagnostic.",
 "Rendement du TEP précoce dans la FUO : 40 à 60 %.",
 B(8,14))

q("D","DX.8 vs DX.14 · fièvre après chimiothérapie","assessment_diagnosis","hôpital",
 "Une femme de 59 ans traitée par chimiothérapie pour une leucémie est fébrile depuis 4 semaines. Neutrophiles 0,3 G/L.",
 "Comment classer cette situation ?",
 [("Neutropénie fébrile, pas une FUO",""),
  ("FUO d'origine néoplasique","La neutropénie exclut la définition de la FUO."),
  ("FUO idiopathique","Le critère d'immunité n'est pas rempli."),
  ("Fièvre factice","Rien ne l'oriente."),
  ("Maladie inflammatoire non infectieuse","La neutropénie domine le tableau.")],
 "Un patient neutropénique n'entre pas dans la FUO (DX.8) : il relève de la neutropénie fébrile, avec antibiotique i.v. dans l'heure (DX.14).",
 "Après 4 à 7 jours de fièvre sous antibiotique, on cherche une infection fongique.",
 B(8,14))

q("D","DX.8 · test au naproxène","mechanisms","hôpital",
 "Un homme de 64 ans a une FUO stable. Une néoplasie est suspectée, la biopsie est programmée. Le médecin discute un test au naproxène.",
 "Quelle est la portée de ce test ?",
 [("Il oriente, sans prouver la néoplasie",""),
  ("Il pose à lui seul le diagnostic de néoplasie","Seule l'histologie le pose."),
  ("Il remplace la biopsie","Il ne la remplace pas."),
  ("Il exclut une infection","Aucune sensibilité chiffrée ne l'autorise."),
  ("Il guérit la fièvre néoplasique","Il soulage, sans traiter la cause.")],
 "Le test au naproxène oriente vers une fièvre néoplasique plutôt qu'infectieuse, mais il ne remplace pas l'histologie, et aucune sensibilité n'est chiffrée dans les sources lues (DX.8).",
 "Naproxène contre-indiqué si la clairance est < 30 mL/min (AIPS).",
 B(8,13), niv="approfondissement")

q("D","DX.8 · pics fébriles élevés","mechanisms","policlinique",
 "Un étudiant demande quelles néoplasies donnent classiquement des pics fébriles élevés dans la FUO.",
 "Quelle réponse est correcte ?",
 [("Cancer du rein et lymphomes",""),
  ("Myélome multiple","Il ne donne habituellement pas de fièvre aiguë."),
  ("Syndromes myéloprolifératifs","Ils n'en donnent habituellement pas."),
  ("Leucémie lymphoïde chronique","Les leucémies n'en donnent habituellement pas."),
  ("Cancer de la prostate localisé","Il n'est pas cité parmi les causes de pics fébriles.")],
 "Le cancer du rein et les lymphomes donnent classiquement des pics fébriles élevés ; les leucémies, les syndromes myéloprolifératifs et le myélome n'en donnent habituellement pas (DX.8).",
 "Néoplasie : 7 à 15 % des FUO selon les séries lues.",
 B(8,14), niv="approfondissement")

q("D","DX.9 · adulte sain","management","cabinet",
 "Une femme de 35 ans, sans antécédent, a depuis 6 heures une fièvre brutale à 38,9 °C, des courbatures et une toux, en pleine épidémie de grippe. SpO2 98 %.",
 "Quelle est la conduite la plus appropriée ?",
 [("Traitement symptomatique, sans PCR obligatoire",""),
  ("Attendre le résultat de la PCR avant toute décision","Chez l'adulte sain, le résultat ne change pas la prise en charge."),
  ("Co-amoxicilline préventive","Les antibiotiques ne traitent pas la grippe."),
  ("Hospitalisation pour antiviral i.v.","Forme non compliquée chez un adulte sain."),
  ("Radiographie du thorax systématique","Aucun signe de pneumonie.")],
 "Grippe non compliquée de l'adulte sain : traitement symptomatique à domicile ; l'antiviral se décide selon le risque (DX.9). On teste si le résultat change la prise en charge.",
 "Avant de conclure à la grippe, chercher sepsis, pneumonie et méningite.",
 B(9,14))

q("D","DX.9 · grippe sans fièvre","assessment_diagnosis","EMS",
 "Pendant une épidémie de grippe dans un EMS, une résidente de 88 ans devient confuse, tousse et mange moins. Température 37,4 °C.",
 "Quelle affirmation est correcte ?",
 [("L'absence de fièvre n'exclut pas la grippe",""),
  ("Sans fièvre, la grippe est exclue","Chez la personne âgée, la grippe survient parfois sans fièvre."),
  ("Une PCR est inutile chez elle","Le résultat peut changer la prise en charge (antiviral, isolement)."),
  ("La confusion exclut une infection respiratoire","Elle peut en être le signe."),
  ("Seule une sérologie tardive peut conclure","La PCR sur frottis nasopharyngé fait le diagnostic.")],
 "Chez la personne âgée, la grippe survient parfois sans fièvre (DX.9). La PCR sur frottis nasopharyngé confirme Influenza A ou B.",
 "Syndrome grippal ECDC 2018 : sensible mais non spécifique.",
 B(9,8), niv="approfondissement")

q("D","DX.9 · clairance 45 mL/min","management","cabinet",
 "Un homme de 79 ans, insuffisant cardiaque, a une grippe confirmée depuis 20 heures. Clairance de la créatinine 45 mL/min.",
 "Quelle posologie d'oseltamivir est correcte ?",
 [("30 mg 2×/j pendant 5 jours",""),
  ("75 mg 2×/j pendant 5 jours","Dose de la fonction rénale normale."),
  ("30 mg 1×/j pendant 5 jours","Dose d'une clairance de 10 à 30 mL/min."),
  ("75 mg 1×/j pendant 10 jours","Schéma de la prophylaxie après contact."),
  ("150 mg 2×/j pendant 5 jours","Dose excessive.")],
 "Oseltamivir (AIPS Tamiflu®) : clairance de 30 à 60 mL/min → 30 mg deux fois par jour ; de 10 à 30 mL/min → 30 mg une fois par jour (DX.9).",
 "Débuter dans les 36 premières heures si possible.",
 B(9,14), niv="approfondissement")

q("D","DX.9 · baloxavir","management","cabinet",
 "Un homme de 45 ans, 70 kg, a des symptômes de grippe depuis 30 heures. Il souhaite un traitement en prise unique.",
 "Quelle posologie de baloxavir est correcte selon l'AIPS ?",
 [("40 mg en dose unique dans les 48 h",""),
  ("80 mg en dose unique","Dose réservée aux patients de 80 kg ou plus."),
  ("40 mg 2×/j pendant 5 jours","Le baloxavir se donne en une seule prise."),
  ("75 mg 2×/j pendant 5 jours","Schéma de l'oseltamivir."),
  ("20 mg une fois par jour pendant 3 jours","Schéma inexact.")],
 "Baloxavir (Xofluza®, AIPS) : dose unique dans les 48 h, 40 mg de 20 à moins de 80 kg, 80 mg dès 80 kg ; éviter calcium, laitages et antiacides pris en même temps (DX.9).",
 "Délai médian d'amélioration : 53,7 h contre 80,2 h sous placebo.",
 B(9,14), niv="specialiste", spe="Infectiologie")

q("D","DX.10 · vomissements bilieux","assessment_diagnosis","urgences",
 "Un nourrisson de 7 mois vomit depuis 8 heures. Les vomissements sont devenus verts. Il pleure par crises. Selles peu abondantes.",
 "Quelle est la conduite la plus appropriée ?",
 [("Imagerie et avis chirurgical en urgence",""),
  ("Solution de réhydratation orale et contrôle à 24 h","Des vomissements bilieux évoquent une urgence abdominale."),
  ("Ondansétron et retour à domicile","Il masquerait une urgence chirurgicale."),
  ("Coproculture","Elle ne répond pas à la question urgente."),
  ("Diète et reprise progressive","Retarde le diagnostic.")],
 "Des vomissements bilieux ne sont pas une gastro-entérite : urgence abdominale, échographie et avis chirurgical (DX.10). Avant de conclure à une gastro-entérite, on exclut un abdomen chirurgical.",
 "Douleur localisée, défense ou vomissements bilieux : arbre décisionnel N1.",
 B(10,14))

q("D","DX.10 · ondansétron","management","urgences",
 "Une fille de 5 ans a une gastro-entérite avec des vomissements qui empêchent la réhydratation orale. Le médecin envisage l'ondansétron.",
 "Quelle affirmation sur l'ondansétron est correcte ?",
 [("Pas d'indication AIPS dans la gastro-entérite",""),
  ("Il est l'antidiarrhéique de choix","C'est un antiémétique, pas un antidiarrhéique."),
  ("Il remplace la réhydratation orale","La réhydratation reste le traitement principal."),
  ("Il est interdit avant 6 ans par l'AIPS","Ce n'est pas la règle citée : l'interdit sous 6 ans vise le lopéramide."),
  ("Il est indiqué en routine dès le premier vomissement","On le discute seulement si les vomissements empêchent l'apport oral.")],
 "L'AIPS de l'ondansétron cite la chimiothérapie, la radiothérapie et les nausées postopératoires, pas la gastro-entérite (DX.10). L'arbre propose de le discuter si les vomissements empêchent l'apport oral.",
 "L'enfant qui vomit reçoit d'abord de petites quantités fréquentes.",
 B(10,14), niv="approfondissement")

q("D","DX.10 · EHEC suspecté","management","hôpital",
 "Un garçon de 6 ans a une diarrhée sanglante depuis 4 jours. Il est pâle, urine peu. Hémoglobine basse, plaquettes 60 G/L, créatinine en hausse.",
 "Quelle est la conduite la plus appropriée ?",
 [("Hospitaliser, sans antidiarrhéique ni antibiotique",""),
  ("Lopéramide et réhydratation orale à domicile avec contrôle","Les antidiarrhéiques sont proscrits dans l'entérite sanglante à EHEC."),
  ("Ciprofloxacine d'emblée","Pas d'antibiotique avant l'avis spécialisé."),
  ("Ibuprofène contre la douleur","Les AINS sont à éviter."),
  ("Coloscopie en urgence","Elle n'est pas indiquée.")],
 "Entérite sanglante avec anémie, thrombopénie et atteinte rénale : syndrome hémolytique et urémique suspect (DX.10). Arrêter tout antidiarrhéique, éviter les AINS, pas d'antibiotique avant l'avis ; hospitaliser, surveiller diurèse et créatinine, avis néphrologique.",
 "Créatinine et diurèse se contrôlent chaque jour.",
 B(10,11), niv="specialiste", spe="Néphrologie")

q("D","DX.11 · définition Sepsis-3","mechanisms","hôpital",
 "Une femme de 63 ans a une pneumonie. Son SOFA de base est 0. Aujourd'hui, plaquettes 85 G/L et Glasgow 13.",
 "Quel élément définit le sepsis selon Sepsis-3 ?",
 [("Infection et hausse du SOFA ≥ 2 points",""),
  ("Deux critères SIRS ou plus présents au triage","Le SIRS seul ne pose pas le sepsis."),
  ("qSOFA ≥ 2","Le qSOFA ne pose ni n'exclut le sepsis."),
  ("Hémoculture positive","Sans dysfonction d'organe, c'est une bactériémie."),
  ("CRP > 100 mg/L","Une CRP élevée seule ne suffit pas.")],
 "Sepsis-3 (2016) : infection suspectée ou prouvée et hausse du SOFA ≥ 2 points par rapport à la base (DX.11). Ici, plaquettes < 100 G/L (2 points) et Glasgow 13 (1 point) : SOFA à 3.",
 "SOFA ≥ 2 : mortalité hospitalière > 10 %.",
 B(11,8), niv="approfondissement")

q("D","DX.11 · bactériémie ou sepsis","mechanisms","hôpital",
 "Un homme de 55 ans a une hémoculture positive à E. coli. Il est apyrétique sous antibiotique, ses constantes et ses fonctions d'organes sont normales.",
 "Comment qualifier cette situation ?",
 [("Bactériémie sans sepsis",""),
  ("Sepsis","Il manque la dysfonction d'organe."),
  ("Choc septique","Aucun vasopresseur ni lactate élevé."),
  ("Endocardite certaine","Une hémoculture isolée à E. coli ne remplit pas les critères."),
  ("Contamination certaine du prélèvement","E. coli n'est pas un contaminant cutané habituel.")],
 "Une hémoculture positive sans dysfonction d'organe est une bactériémie, pas un sepsis (DX.11). Inversement, des hémocultures négatives n'excluent pas le sepsis.",
 "Le sepsis est une dysfonction d'organe par réponse dérégulée à l'infection.",
 B(11,8), niv="approfondissement")

q("D","DX.11 · vasopresseur persistant","management","hôpital",
 "Une femme de 70 ans en choc septique abdominal reçoit de la noradrénaline à dose croissante, avec vasopressine ajoutée. La PAM reste à 62 mmHg.",
 "Quelle mesure peut être envisagée selon la SSC 2021 ?",
 [("Hydrocortisone",""),
  ("Dexaméthasone 10 mg toutes les 6 heures","Schéma de la méningite à pneumocoque."),
  ("Procalcitonine pour décider de l'antibiotique","La SSC 2021 la déconseille pour cette décision."),
  ("Arrêt de l'antibiotique","Le foyer n'est pas contrôlé."),
  ("Albumine 20 % seule","Elle ne répond pas au besoin de vasopresseur.")],
 "Si la pression reste basse sous noradrénaline : vasopressine, puis adrénaline, et l'on envisage l'hydrocortisone (DX.11). Elle n'est pas de routine : l'AIPS ne la recommande pas en usage systématique.",
 "Contrôle du foyer dans les 6 à 12 heures ; soins intensifs dans les 6 heures.",
 B(11,11), niv="specialiste", spe="Médecine intensive")

q("D","DX.11 · procalcitonine","management","urgences",
 "Un homme de 62 ans est fébrile à 38,9 °C, FC 112/min, PA 92/55 mmHg, lactate 3,1 mmol/L. L'interne propose d'attendre la procalcitonine avant l'antibiotique.",
 "Quelle réponse est la plus appropriée ?",
 [("Antibiotique sans attendre la procalcitonine",""),
  ("Attendre la procalcitonine","La SSC 2021 la déconseille pour décider du début de l'antibiotique."),
  ("Attendre la CRP de contrôle à 24 h","Le retard aggrave le pronostic."),
  ("Attendre les hémocultures positives","On prélève sans attendre le résultat."),
  ("Attendre l'apparition d'un foyer clinique évident","Le foyer se cherche en parallèle.")],
 "La procalcitonine ne décide pas du début de l'antibiotique (SSC 2021) (DX.11). En cas de sepsis probable, l'antibiotique se donne dans l'heure ; en cas de sepsis possible sans choc, dans les 3 heures.",
 "Une procalcitonine élevée seule ne pose pas le sepsis.",
 B(11,14), niv="approfondissement")

q("D","DX.12 · après 50 ans","management","urgences",
 "Une femme de 72 ans a une méningite bactérienne probable : fièvre, raideur de nuque, LCR trouble. La dexaméthasone et la ceftriaxone ont été débutées.",
 "Quel antibiotique faut-il ajouter ?",
 [("Ampicilline ou amoxicilline i.v.",""),
  ("Aciclovir systématique","Il s'ajoute seulement si une encéphalite herpétique reste possible."),
  ("Gentamicine","Elle n'est pas le complément de la ceftriaxone ici."),
  ("Clarithromycine","Elle ne couvre pas Listeria."),
  ("Aucun : la ceftriaxone suffit à elle seule","Les céphalosporines ne couvrent pas Listeria.")],
 "Listeria monocytogenes n'est pas couvert par les céphalosporines (DX.12). Après 50 ans ou en cas d'immunodépression, on ajoute l'ampicilline ou l'amoxicilline i.v. à la ceftriaxone.",
 "La DGN 2023 retient ceftriaxone plus ampicilline comme schéma empirique de l'adulte.",
 B(12,14))

q("D","DX.12 · contact étroit","management","cabinet",
 "Un étudiant de 20 ans a une infection invasive à méningocoque confirmée. Plusieurs personnes demandent une prophylaxie.",
 "Quelle personne est un contact étroit ?",
 [("Son colocataire du même appartement",""),
  ("Un passager assis dans le même train","La proximité d'un train ne suffit pas."),
  ("Un collègue du même étage","Pas de contact intense avec les sécrétions."),
  ("Un voisin de l'immeuble","Il ne partage pas le foyer."),
  ("Un passager du même avion à 10 rangs","La proximité d'un avion ne suffit pas.")],
 "Contact étroit : même foyer, contact intense avec les sécrétions, partenaire de sport très proche (DX.12). La proximité d'un train ou d'un avion ne suffit pas.",
 "Déclarer tout cas de méningocoque dans les 24 heures (OFSP).",
 B(12,14))

q("D","DX.12 · LCR peu cellulaire","assessment_diagnosis","urgences",
 "Un homme de 66 ans a une fièvre à 39,5 °C et une confusion. Ponction lombaire : 640 cellules/µL à prédominance neutrophile, protéines 2,1 g/L, quotient glucose 0,2, lactate 6 mmol/L.",
 "Quelle interprétation est correcte ?",
 [("Méningite bactérienne probable",""),
  ("Méningite virale : < 1000 cellules","Lactate > 3,5 mmol/L, glucose abaissé et neutrophiles orientent vers une cause bactérienne."),
  ("LCR normal","Il est nettement pathologique."),
  ("Méningite tuberculeuse certaine","La cytologie est mixte dans la tuberculose ; rien ne la prouve."),
  ("Hémorragie méningée","Le profil est inflammatoire.")],
 "Jusqu'à un tiers des méningites à pneumocoque ont moins de 1000 cellules/µL (33 % dans une série de 1816 patients) (DX.12). Neutrophiles, protéines > 1 g/L, quotient glucose < 0,3 et lactate > 3,5 mmol/L signent l'origine bactérienne.",
 "L'absence de raideur de nuque n'exclut pas non plus la méningite.",
 B(12,8), niv="approfondissement")

q("D","DX.12 · contact enceinte","management","cabinet",
 "Une femme de 31 ans, enceinte de 20 semaines, vit avec un patient hospitalisé pour méningococcie.",
 "Quelle prophylaxie est la plus appropriée ?",
 [("Ceftriaxone 250 mg i.m. en dose unique",""),
  ("Ciprofloxacine 500 mg per os","Déconseillée pendant la grossesse."),
  ("Rifampicine 600 mg 2×/j pendant 2 jours","Déconseillée pendant la grossesse."),
  ("Aucune prophylaxie","Elle est contact étroit."),
  ("Vaccin seul sans antibiotique","Il ne remplace pas la prophylaxie immédiate.")],
 "Chez la femme enceinte contact étroit, la prophylaxie est la ceftriaxone 250 mg i.m. en dose unique (BAG 2025) ; ciprofloxacine et rifampicine sont déconseillées (DX.12).",
 "La rifampicine réduit aussi l'efficacité des contraceptifs hormonaux.",
 B(12,14), niv="specialiste", spe="Infectiologie")

q("D","DX.13 · indication opératoire urgente","management","hôpital",
 "Un homme de 58 ans a une endocardite aortique à S. aureus. Brutalement, il devient dyspnéique avec un œdème pulmonaire, en rapport avec une régurgitation aortique sévère.",
 "Quel délai opératoire est le plus approprié ?",
 [("Chirurgie dans les 24 heures",""),
  ("Chirurgie après 6 semaines d'antibiotique","L'œdème pulmonaire impose une chirurgie d'urgence."),
  ("Chirurgie dans les 3 mois","Délai incompatible avec le pronostic."),
  ("Aucune chirurgie : l'antibiotique suffit","La valve détruite ne guérit pas par l'antibiotique seul."),
  ("Chirurgie à la négativation des hémocultures","On n'attend pas en cas d'œdème pulmonaire.")],
 "Œdème pulmonaire ou choc par régurgitation, obstruction ou fistule : opération d'urgence dans les 24 heures (ESC 2023) (DX.13). Insuffisance cardiaque ou abcès : urgente dans les 3 à 5 jours.",
 "Pas d'anticoagulant en cas de déficit neurologique avant l'imagerie.",
 B(13,11))

q("D","DX.13 · critères de Duke","assessment_diagnosis","hôpital",
 "Une femme de 64 ans a une fièvre à 38,6 °C, une prothèse mitrale et des streptocoques typiques dans deux hémocultures. L'ETO montre une végétation.",
 "Comment classer l'endocardite selon Duke-ISCVID 2023 ?",
 [("Certaine : deux critères majeurs",""),
  ("Possible : un majeur et un mineur","Il y a deux critères majeurs."),
  ("Rejetée faute de souffle","L'absence de souffle n'exclut pas."),
  ("Possible : trois mineurs","Microbiologie et imagerie sont des critères majeurs."),
  ("Inclassable sans chirurgie","L'inspection chirurgicale n'est pas indispensable.")],
 "Duke-ISCVID 2023 : certain = deux critères majeurs, ou un majeur et trois mineurs, ou cinq mineurs (DX.13). Germe typique dans au moins deux hémocultures et végétation à l'échocardiographie sont deux majeurs.",
 "Les critères guident ; la décision finale revient à l'équipe de l'endocardite.",
 B(13,8), niv="approfondissement")

q("D","DX.13 · SARM du cœur droit","management","hôpital",
 "Un homme de 30 ans qui s'injecte des drogues a une endocardite tricuspide à S. aureus résistant à la méticilline.",
 "Quel antibiotique est indiqué selon l'AIPS ?",
 [("Daptomycine 6 mg/kg/24 h i.v.",""),
  ("Flucloxacilline 12 g/j","Inactive sur le SARM."),
  ("Ceftriaxone 2 g/j","Inactive sur le SARM."),
  ("Amoxicilline-acide clavulanique","Inactive sur le SARM."),
  ("Clarithromycine i.v.","Ce n'est pas un traitement de l'endocardite.")],
 "SARM de l'endocardite droite : daptomycine 6 mg/kg i.v. toutes les 24 h pendant 2 à 6 semaines, ou vancomycine selon l'AIPS (DX.13). La CPK se dose avant puis chaque semaine.",
 "La daptomycine n'est établie par l'AIPS que pour l'endocardite droite, pas gauche.",
 B(13,14), niv="specialiste", spe="Infectiologie")

q("D","DX.13 · aminoside sur valve native","management","hôpital",
 "Une femme de 47 ans a une endocardite sur valve mitrale native à S. aureus sensible à la méticilline. Elle reçoit de la flucloxacilline.",
 "Faut-il ajouter de la gentamicine ?",
 [("Non, pas d'aminoside sur valve native",""),
  ("Oui, pendant 6 semaines","Néphrotoxique, sans bénéfice sur valve native selon l'ESC 2023."),
  ("Oui, à la place de la flucloxacilline","La flucloxacilline reste le traitement du SASM."),
  ("Oui, seulement si la créatinine est normale","Ce n'est pas le critère retenu."),
  ("Oui, en dose unique avant la chirurgie","Aucune indication systématique.")],
 "Endocardite à SASM sur valve native : flucloxacilline 12 g/j en perfusions de 2 g au plus ; pas d'aminoside selon l'ESC 2023, car la gentamicine est néphrotoxique (DX.13).",
 "L'équipe d'endocardite décide selon la valve (native ou prothétique) et le germe.",
 B(13,14), niv="specialiste", spe="Cardiologie")

q("D","DX.14 · faible risque","management","policlinique",
 "Une femme de 44 ans sous chimiothérapie pour un cancer du sein a une neutropénie fébrile. Score MASCC 23. Elle est fiable, entourée, et vit à 10 minutes de l'hôpital.",
 "Quelle conduite est possible ?",
 [("Antibiotique oral en ambulatoire",""),
  ("Hospitalisation obligatoire en soins intensifs","Le score indique un faible risque."),
  ("Aucun antibiotique","La neutropénie fébrile se traite toujours."),
  ("Antifongique empirique d'emblée","Réservé à la fièvre persistante au-delà de 4 à 7 jours."),
  ("Filgrastim seul","Il ne remplace pas l'antibiotique.")],
 "Un score MASCC ≥ 21 identifie un faible risque : chez un patient fiable, un traitement oral ambulatoire est possible, par exemple une fluoroquinolone avec l'amoxicilline-acide clavulanique (DX.14).",
 "MASCC ≥ 21 : VPP 91 %, spécificité 68 %, sensibilité 71 %.",
 B(14,8))

q("D","DX.14 vs DX.4 · fièvre persistante","management","hôpital",
 "Un homme de 49 ans en aplasie après chimiothérapie pour une leucémie aiguë reste fébrile après 6 jours de méropénème. Cultures négatives.",
 "Que faut-il rechercher ?",
 [("Une infection fongique",""),
  ("Une fièvre factice","Rien ne l'oriente."),
  ("Un coup de chaleur","Aucun contexte de chaleur."),
  ("Une FUO classique","La neutropénie exclut la FUO."),
  ("Une maladie de Still","Diagnostic d'exclusion hors de propos ici.")],
 "Après 4 à 7 jours de fièvre persistante sous antibiotique, on cherche une infection fongique : scanner thoracique, marqueurs fongiques, antifongique empirique selon l'hématologue (DX.14).",
 "Réévaluer à 48–72 h, puis à nouveau si la fièvre persiste.",
 B(14,13), niv="specialiste", spe="Hématologie")

q("D","DX.14 · cathéter infecté","management","hôpital",
 "Une femme de 57 ans neutropénique fébrile sous céfépime a une rougeur et du pus au point d'entrée de son cathéter veineux central.",
 "Quel antibiotique faut-il ajouter ?",
 [("Vancomycine",""),
  ("Clarithromycine","Elle ne couvre pas les staphylocoques résistants du cathéter."),
  ("Métronidazole","Il vise les anaérobies abdominaux."),
  ("Oseltamivir","Antiviral sans rapport."),
  ("Aucun : le céfépime suffit","Le foyer de cathéter impose de couvrir les germes résistants.")],
 "Foyer de cathéter, instabilité, pneumonie ou peau : ajouter la vancomycine à la bêtalactamine antipseudomonale (DX.14). La vancomycine se dose sur le creux sérique.",
 "Abdomen : couvrir les anaérobies.",
 B(14,10), niv="specialiste", spe="Hématologie")

q("D","DX.14 · CRP normale","assessment_diagnosis","urgences",
 "Un homme de 66 ans sous chimiothérapie a 38,4 °C depuis 1 heure. Neutrophiles 0,3 G/L. CRP 6 mg/L. Il se sent bien et n'a aucun foyer.",
 "Quelle interprétation est correcte ?",
 [("La CRP normale ne rassure pas",""),
  ("La CRP normale exclut une infection bactérienne","Sans neutrophiles, la réponse inflammatoire manque."),
  ("L'absence de foyer exclut une infection","Les signes locaux sont absents chez le neutropénique."),
  ("La fièvre est due à la chimiothérapie, sans infection","Attribution prématurée."),
  ("Une surveillance sans antibiotique suffit","L'antibiotique i.v. se donne dans l'heure.")],
 "Le neutropénique ne fait pas de réponse inflammatoire locale : l'absence de foyer n'exclut rien et une CRP normale ne rassure pas (DX.14). Hémocultures puis antibiotique i.v. dans l'heure.",
 "Sans neutrophiles, une infection bactérienne progresse et tue en quelques heures.",
 B(14,8), niv="approfondissement")

q("D","DX.15 vs DX.11 · épuisement par la chaleur","assessment_diagnosis","terrain",
 "Un ouvrier de 45 ans travaille sur un toit par 33 °C. Il a des crampes, des nausées et une grande fatigue. Il est parfaitement orienté. Température rectale 38,9 °C.",
 "Quel est le diagnostic le plus probable ?",
 [("Épuisement par la chaleur",""),
  ("Coup de chaleur d'effort","Il faut une température > 40 °C avec un trouble neurologique."),
  ("Méningite bactérienne","Aucun signe méningé ni fièvre élevée."),
  ("Sepsis","Aucun foyer ni dysfonction d'organe."),
  ("Paludisme","Aucun voyage.")],
 "Symptômes de chaleur sans atteinte neurologique, température plus basse : épuisement par la chaleur, à traiter par repos au frais et boissons en surveillant l'évolution (DX.15).",
 "Un coup de chaleur au travail peut relever de la LAA et de la Suva.",
 B(15,14))

q("D","DX.15 · site de mesure","assessment_diagnosis","terrain",
 "Une femme de 22 ans s'effondre confuse à la fin d'une course par forte chaleur. La température tympanique indique 38,7 °C.",
 "Quelle mesure faut-il prendre pour décider ?",
 [("Mesurer la température rectale",""),
  ("Se fier à la mesure tympanique","Elle sous-estime la température centrale."),
  ("Mesurer la température buccale","Elle sous-estime aussi la valeur."),
  ("Palper la peau","La peau peut rester moite dans la forme d'effort."),
  ("Attendre la CK","Aucun examen n'est nécessaire pour décider de refroidir.")],
 "Le coup de chaleur se diagnostique sur la température centrale : on la mesure au rectum, et on la répète toutes les 5 minutes pendant le refroidissement (DX.15). Les mesures buccale, tympanique et cutanée sous-estiment.",
 "Une confusion après effort dans la chaleur impose de refroidir sans attendre les examens.",
 B(15,14))

q("D","DX.15 vs DX.1 · hyperthermie ou fièvre","mechanisms","hôpital",
 "Un étudiant compare la fièvre d'une pneumonie et l'hyperthermie d'un coup de chaleur.",
 "Quel mécanisme distingue l'hyperthermie de la fièvre ?",
 [("Consigne hypothalamique normale",""),
  ("Consigne relevée par la prostaglandine E2","Mécanisme de la fièvre."),
  ("Libération d'interleukine 1 et de TNF-α","Cytokines pyrogènes de la fièvre."),
  ("Induction de la COX-2 cérébrale","Étape de la fièvre."),
  ("Action sur les récepteurs EP3 préoptiques","Étape de la fièvre.")],
 "Dans la fièvre, IL-1, IL-6 et TNF-α induisent la COX-2, la PGE2 agit sur les récepteurs EP3 et relève la consigne. Dans l'hyperthermie, la consigne reste normale : la production ou l'apport de chaleur dépasse les pertes (DX.15, DX.1).",
 "Les antipyrétiques inhibent la COX ; ils n'agissent donc pas dans l'hyperthermie.",
 PA("ssp-p3","§3 Physiopathologie"), niv="approfondissement")

q("D","DX.15 · soluté et foie","management","hôpital",
 "Un homme de 34 ans est en soins intensifs pour un coup de chaleur d'effort. ASAT et ALAT sont très élevées, l'INR augmente. Il reste hypovolémique.",
 "Quel soluté de remplissage est le plus approprié ?",
 [("NaCl 0,9 %",""),
  ("Ringer-lactate","Contre-indiqué en cas de graves lésions hépatiques (AIPS)."),
  ("Glucose 5 %","Il n'a pas d'effet volémique durable."),
  ("Albumine 20 % en première intention","Le cristalloïde isotonique reste la référence."),
  ("Aucun soluté","Le remplissage est nécessaire.")],
 "Coup de chaleur : remplissage par NaCl 0,9 % ; le Ringer-lactate est contre-indiqué en cas de graves lésions hépatiques selon l'AIPS (DX.15). On surveille créatinine, potassium, CK, ASAT, ALAT, INR et plaquettes pendant 48 heures.",
 "Mortalité en soins intensifs : 26,5 % dans la forme d'effort.",
 B(15,14), niv="specialiste", spe="Médecine intensive")

# ═════════════ BLOC P · PIÈGES & ALARMES
q("P","DX.11 · qSOFA rassurant","assessment_diagnosis","urgences",
 "Un homme de 69 ans a une fièvre à 38,8 °C et des frissons solennels depuis ce matin. FR 20/min, conscience normale, PA 108/66 mmHg : qSOFA 0. Il est pâle et marbré aux genoux.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Mesurer le lactate et prélever des hémocultures",""),
  ("Retour à domicile, car le qSOFA à 0 exclut le sepsis","Le qSOFA est peu sensible ; il n'exclut pas le sepsis."),
  ("Paracétamol et réévaluation le lendemain","L'antipyrétique ne ferme aucune branche dangereuse."),
  ("Calculer le SIRS et conclure","Le SIRS seul ne pose ni n'exclut le sepsis."),
  ("Attendre que la PA baisse avant d'agir","On réévalue avant la décompensation, pas après.")],
 "Un qSOFA à 0 ou 1 n'exclut pas le sepsis : la SSC 2021 déconseille le qSOFA comme seul outil de dépistage (DX.11). Frissons solennels et marbrures imposent lactate et hémocultures, avec réévaluation horaire.",
 "Les frissons solennels accompagnent la décharge de cytokines d'une bactériémie.",
 PA("ssp-p14","§14 Pièges"))

q("P","DX.2 · bactériurie sans symptôme","management","EMS",
 "Une résidente d'EMS de 85 ans, apyrétique et sans plainte, a une bandelette urinaire positive et une uroculture à E. coli faites lors d'un contrôle systématique. Constantes normales.",
 "Quelle est la conduite la plus appropriée ?",
 [("Pas d'antibiotique",""),
  ("Ciprofloxacine 7 jours","Une bactériurie asymptomatique ne se traite pas ici."),
  ("Ceftriaxone i.v. en hospitalisation","Aucun signe systémique."),
  ("Échographie rénale en urgence","Aucun signe d'atteinte rénale."),
  ("Nouvelle uroculture et traitement si positive","La répétition ne change pas l'absence de symptôme.")],
 "La pyélonéphrite exige des signes systémiques ou une douleur lombaire avec une culture positive (DX.2). Une bactériurie asymptomatique seule ne pose pas le diagnostic.",
 "Une bandelette positive ne dit pas si l'infection touche le rein ou la vessie.",
 B(2,14))

q("P","DX.3 · hémocultures systématiques ?","assessment_diagnosis","cabinet",
 "Un homme de 50 ans a un érysipèle de jambe non compliqué, sans sepsis ni immunodépression. L'assistante demande s'il faut des hémocultures.",
 "Quelle réponse est la plus appropriée ?",
 [("Non : réservées au sepsis ou à l'immunodépression",""),
  ("Oui : elles posent le diagnostic","Le diagnostic est clinique."),
  ("Oui : trois paires avant tout antibiotique","Conduite de l'endocardite."),
  ("Oui : une culture négative exclut la cellulite","Elles sont rarement positives ; un résultat négatif n'exclut rien."),
  ("Non : un prélèvement cutané suffit à confirmer","Il est lui aussi rarement positif.")],
 "Dans la cellulite simple, les hémocultures sont rarement positives : elles sont indiquées en cas de sepsis ou d'immunodépression (IDSA) (DX.3). Le diagnostic est clinique.",
 "Une CRP normale n'exclut pas la cellulite.",
 B(3,14))

q("P","DX.10 · enfant de 4 ans","management","cabinet",
 "Une fillette de 4 ans a une gastro-entérite aqueuse sans sang, sans fièvre élevée. Elle boit bien. La mère demande un médicament.",
 "Quel médicament est contre-indiqué ?",
 [("Lopéramide",""),
  ("Solution de réhydratation orale","Traitement principal."),
  ("Paracétamol à dose adaptée au poids","Antipyrétique possible en cas de besoin."),
  ("Petites quantités de boisson fréquentes","Mesure recommandée."),
  ("Alimentation habituelle","Elle protège l'intestin.")],
 "Le lopéramide est interdit avant 6 ans (AIPS Imodium®) (DX.10). Chez l'adulte, il est aussi exclu en cas de sang dans les selles ou de fièvre élevée.",
 "Arrêter le lopéramide après 2 jours sans amélioration, ou dès constipation ou ballonnement.",
 B(10,13), pol="negative")

q("P","DX.14 · examen du neutropénique","assessment_diagnosis","urgences",
 "Une femme de 61 ans neutropénique fébrile (neutrophiles 0,1 G/L) se plaint d'une gêne anale. Les hémocultures sont prélevées et l'antibiotique est en cours.",
 "Quel geste est contre-indiqué ?",
 [("Toucher rectal",""),
  ("Inspection de la région périanale","Geste recommandé."),
  ("Examen de la cavité buccale","Recherche de mucite, utile."),
  ("Inspection du point du cathéter","Recherche d'un foyer, utile."),
  ("Auscultation pulmonaire","Recherche d'une pneumonie, utile.")],
 "Chez le neutropénique, le toucher rectal est contre-indiqué ; on inspecte la région périanale (DX.14).",
 "Hygiène des mains et soins de bouche font partie des mesures générales.",
 B(14,14), pol="negative")

q("P","DX.14 · fièvre sous métamizole","assessment_diagnosis","cabinet",
 "Une femme de 63 ans prend du métamizole depuis 3 semaines pour des douleurs. Elle consulte pour une fièvre à 38,8 °C et une angine.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Arrêter le métamizole et faire une formule sanguine",""),
  ("Augmenter le métamizole pour la fièvre","Le médicament est la cause suspecte."),
  ("Pénicilline V pour l'angine et contrôle à 1 semaine","Fièvre et angine sous métamizole : agranulocytose à exclure d'abord."),
  ("Test rapide streptococcique seul","Il ne répond pas au danger principal."),
  ("Ibuprofène et gargarismes","Traitement symptomatique inadapté.")],
 "Le métamizole peut causer une agranulocytose, indépendante de la dose : fièvre ou angine imposent l'arrêt immédiat et une numération (DX.14). Neutrophiles < 0,5 G/L : neutropénie fébrile.",
 "Novalgin® est réservé à la forte fièvre qui résiste aux autres mesures.",
 PA("ssp-p11","§11 Prise en charge"))

q("P","DX.9 · dose de paracétamol","management","domicile",
 "Un homme de 40 ans, 78 kg, grippé, prend Dafalgan® 1 g quatre fois par jour. Il ajoute un sachet « grippe » contenant du paracétamol.",
 "Quel conseil est le plus approprié ?",
 [("Ne pas dépasser 4 g/j, toutes sources comprises",""),
  ("Passer à 6 g/j pendant la fièvre","Dose maximale adulte : 4 g/j."),
  ("Raccourcir l'intervalle à 2 heures","Intervalle de 4 à 8 h entre les prises."),
  ("Associer de l'acide acétylsalicylique pour la fièvre","Il n'apporte rien et ajoute un risque."),
  ("Doubler la dose du soir","Dose maximale dépassée.")],
 "Paracétamol chez l'adulte de plus de 40 kg : 500 à 1000 mg par prise, toutes les 4 à 8 h, maximum 4 g/j (AIPS Dafalgan®) (DX.9). Vérifier que les autres médicaments ne contiennent pas de paracétamol.",
 "L'antipyrétique vise le confort ; il ne traite pas la cause.",
 B(9,14))

q("P","DX.9 · troisième trimestre","management","cabinet",
 "Une femme de 32 ans enceinte de 34 semaines a une grippe avec fièvre à 38,8 °C et myalgies.",
 "Quel médicament est contre-indiqué ?",
 [("Ibuprofène",""),
  ("Paracétamol","Utilisable en cas de nécessité, à la dose efficace la plus faible, le moins longtemps possible."),
  ("Oseltamivir","Possible en cas de nécessité absolue, sans ajustement de dose."),
  ("Ceftriaxone i.v.","Possible si formellement indiquée ; seule la voie i.m. est contre-indiquée."),
  ("Flucloxacilline","À utiliser avec la plus grande prudence, sans contre-indication formelle.")],
 "L'ibuprofène est contre-indiqué au 3e trimestre (AIPS Brufen®) ; dès la 20e semaine, risque d'oligohydramnios et d'insuffisance rénale néonatale (DX.9). Le paracétamol reste possible à la dose efficace la plus faible.",
 "Le métamizole est aussi contre-indiqué au 3e trimestre.",
 B(9,14), pol="negative", niv="approfondissement")

q("P","DX.13 · pas de souffle","assessment_diagnosis","hôpital",
 "Un homme de 67 ans porteur d'une prothèse aortique a une fièvre à 38,5 °C depuis 2 semaines. Aucun souffle n'est entendu. Les hémocultures ne sont pas encore faites.",
 "Quelle affirmation est correcte ?",
 [("L'absence de souffle n'exclut pas l'endocardite",""),
  ("Sans souffle, l'endocardite est exclue","Le souffle peut manquer, surtout au début ou dans la régurgitation aiguë."),
  ("Une antibiothérapie empirique précède les hémocultures","Les hémocultures se prélèvent avant l'antibiotique."),
  ("Une seule hémoculture suffit","Il en faut trois paires."),
  ("Une ETT normale clôt le bilan","Une ETT négative n'exclut pas.")],
 "Un souffle absent et une ETT négative n'excluent pas l'endocardite (DX.13). Prothèse valvulaire et fièvre : trois paires d'hémocultures, puis échocardiographie, ETO si l'ETT est normale.",
 "Une hémoculture isolée à germe peu typique ne remplit pas le critère majeur.",
 B(13,14))

q("P","DX.2 · co-trimoxazole et rein","management","hôpital",
 "Un homme de 76 ans a une pyélonéphrite à E. coli sensible au co-trimoxazole. Clairance de la créatinine 10 mL/min.",
 "Quelle affirmation est correcte ?",
 [("Bactrim® forte ne doit pas être utilisé",""),
  ("Bactrim® forte à pleine dose","Contre-indiqué sous 15 mL/min."),
  ("Bactrim® forte à demi-dose","L'AIPS interdit son emploi sous 15 mL/min."),
  ("Bactrim® forte avec un supplément de potassium","Risque d'hyperkaliémie, sans lever l'interdiction."),
  ("Bactrim® forte en dose unique","Cure inadaptée à une pyélonéphrite.")],
 "Sous 15 mL/min, l'AIPS interdit l'emploi de Bactrim® forte, qui expose aussi à l'hyperkaliémie (DX.2). On choisit une alternative selon l'antibiogramme.",
 "Co-amoxicilline : 625 mg toutes les 12 h de 10 à 30 mL/min.",
 B(2,14), niv="approfondissement")

q("P","DX.1 · clairance 25 mL/min","management","cabinet",
 "Une femme de 81 ans a une pneumonie ambulatoire. Clairance de la créatinine 25 mL/min.",
 "Quelle posologie de co-amoxicilline est correcte ?",
 [("625 mg toutes les 12 heures",""),
  ("1000 mg 2×/j","Pas de 2 × 1000 mg sous 30 mL/min."),
  ("1000 mg 3×/j","Dose maximale de la fonction rénale normale."),
  ("625 mg 3×/j","Dose sans insuffisance rénale."),
  ("625 mg toutes les 24 heures","Dose d'une clairance < 10 mL/min.")],
 "Amoxicilline-acide clavulanique (AIPS) : de 10 à 30 mL/min, 625 mg toutes les 12 heures ; sous 10 mL/min, 625 mg toutes les 24 heures ; pas de 2 × 1000 mg sous 30 mL/min (DX.1).",
 "Réévaluer à 48–72 h et chercher une complication si pas d'amélioration.",
 B(1,14))

q("P","DX.4 · médicament fébrigène","management","cabinet",
 "Un homme de 58 ans a une fièvre à 38,4 °C sans foyer depuis 2 semaines. Il a commencé un nouvel anticonvulsivant il y a 5 semaines. Il est stable et l'examen est normal.",
 "Quelle mesure est la plus appropriée ?",
 [("Arrêter ou remplacer le médicament suspect",""),
  ("Ajouter un antibiotique d'épreuve","Il masquerait la cause."),
  ("Prednisone d'épreuve","Elle masquerait la cause."),
  ("FDG-TEP-TDM d'emblée","Le critère de durée de la FUO n'est pas rempli et une cause simple est à tester."),
  ("Ignorer le médicament, présent depuis plus de 4 semaines","Un médicament des 8 dernières semaines peut être fébrigène.")],
 "Un médicament fébrigène explique une fièvre sans foyer ; la fièvre cède quelques jours après l'arrêt (DX.4). On demande les médicaments des 8 dernières semaines et l'on arrête ou remplace le suspect.",
 "Dans la FUO, on arrête ou remplace tous les médicaments, même pris depuis des années.",
 PA("ssp-p5","§5 Anamnèse"))

q("P","DX.5 · méthotrexate","management","policlinique",
 "Une femme de 55 ans traitée pour une maladie inflammatoire reçoit du méthotrexate. La pharmacienne vérifie l'ordonnance.",
 "Quel rythme d'administration est correct ?",
 [("Une fois par semaine",""),
  ("Une fois par jour","Erreur dangereuse : surdosage."),
  ("Deux fois par jour","Erreur dangereuse : surdosage."),
  ("Un jour sur deux","Rythme incorrect."),
  ("Une fois par mois","Rythme incorrect.")],
 "En rhumatologie, le méthotrexate se prend une fois par semaine : 7,5 mg au début, maximum habituel 25 mg par semaine (AIPS) ; il est contre-indiqué pendant la grossesse (DX.5).",
 "La corticothérapie se réduit sous le seuil de Cushing (5 à 7,5 mg/j de prednisone).",
 B(5,14), niv="specialiste", spe="Rhumatologie")

q("P","DX.15 · dantrolène","management","hôpital",
 "Un homme de 24 ans en coup de chaleur d'effort est en cours d'immersion en eau froide. Un collègue propose du dantrolène.",
 "Quelle affirmation est correcte ?",
 [("Le refroidissement rapide reste le seul traitement",""),
  ("Le dantrolène accélère le refroidissement","Aucun effet démontré dans le coup de chaleur."),
  ("Le paracétamol i.v. complète utilement le refroidissement","La consigne est normale ; il charge le foie."),
  ("Le dantrolène remplace l'immersion","Aucun traitement ne remplace le refroidissement."),
  ("L'ibuprofène protège le rein","Les AINS n'ont aucune place ici.")],
 "Le paracétamol et le dantrolène ne traitent pas le coup de chaleur : aucun traitement spécifique n'existe hors refroidissement rapide (DX.15). Une hyperthermie après anesthésie récente fait discuter une hyperthermie maligne.",
 "Agitation, frissons ou convulsions : midazolam titré.",
 B(15,13), niv="approfondissement")

q("P","DX.12 · sortie après pénicilline","management","hôpital",
 "Un homme de 25 ans a été traité par pénicilline G pour une méningococcie. Il va bien et sort demain.",
 "Que faut-il prévoir avant la sortie ?",
 [("Une prophylaxie d'éradication du portage",""),
  ("Rien : la pénicilline éradique le germe","La pénicilline n'éradique pas le germe du nasopharynx."),
  ("Une ponction lombaire de contrôle","Aucune indication systématique."),
  ("Un TEP au FDG","Aucune indication."),
  ("Une corticothérapie orale","Aucune indication.")],
 "La pénicilline n'éradique pas le méningocoque du nasopharynx : le patient reçoit une prophylaxie avant la sortie (BAG 2025) (DX.12). Le cas est déclaré dans les 24 heures et les contacts étroits reçoivent la prophylaxie.",
 "Séquelles chez 10 à 20 % des survivants : contrôler l'audition.",
 B(12,14), niv="approfondissement")

META = dict(
 code="G6", lot="LOT_006", version="1.0.0", seed=19, date="2026-11-01",
 titre="Fièvre, frissons, hyperthermie",
 titre_court="Fièvre, frissons, hyperthermie", n_dx=15,
 note_version="v1 : gabarit Revision (EX/AP/SPE, 💡 fermé) — 1re production G6",
 note_media="Aucune image clinique dans les HTML LOT_006 (Phase A + DX.1–15) : media = null partout, bouton 🖼 absent.",
 intro_R="Devant une fièvre : drapeau rouge d'abord (sepsis, méningite, coup de chaleur, neutropénie, paludisme, endocardite), puis le foyer, puis le terrain et l'exposition. Un antipyrétique ne ferme aucune branche dangereuse.",
 intro_D="Les 15 DX du LOT face à face : un signe, un examen qui tranche, une conduite. Les questions AP (bleu) et SPE (violet) sont mêlées aux EX : filtrez par niveau en haut.",
 intro_P="qSOFA rassurant à tort, bactériurie asymptomatique, hémocultures de la cellulite, lopéramide avant 6 ans, toucher rectal du neutropénique, métamizole, dose de paracétamol, AINS au 3e trimestre, souffle absent, doses rénales.",
 verdict_label="Réflexe G6",
 footer="LOT_006 · G6 · Banque « Temps 1 » v1 · Faits issus exclusivement des leçons auditées LOT_006 (Phase A + Phase B DX.1–15) · Type A, une seule meilleure réponse (règles IML) · Aucun cliché dans les sources LOT_006 : aucune image affichée.",
 carte_html="""<div class="reflex"><b>Les 3 questions réflexes devant une fièvre</b><ol>
<li><b>Drapeau rouge ?</b> Hypotension, confusion ou polypnée ; céphalée, raideur, purpura ; &gt; 40 °C avec confusion après chaleur ou effort ; chimiothérapie ; retour de zone palustre ; prothèse valvulaire, souffle nouveau, drogues injectées.</li>
<li><b>Fièvre ou hyperthermie ?</b> Consigne relevée (cytokines → COX-2 → PGE2) ou consigne normale (chaleur, effort) : l'antipyrétique n'agit que sur la première.</li>
<li><b>Depuis quand, où est le foyer ?</b> Poumon, urine, peau, digestif ; voyage, médicaments des 8 dernières semaines ; <b>≥ 3 semaines</b> avec bilan de base négatif : démarche du FUO, sans antibiotique ni corticoïde d'épreuve si stable.</li></ol></div>
<div class="map" style="margin-top:10px">
<div class="ax"><h3>🫁 Foyers fréquents</h3><ul>
<li>Opacité nouvelle = pneumonie ; score de gravité → domicile ou hôpital (DX.1)</li>
<li>Fièvre + lombalgie + culture = pyélonéphrite ; pas de ciprofloxacine si grossesse (DX.2)</li>
<li>Douleur disproportionnée → chirurgien (DX.3)</li>
<li>Réhydratation orale ; pas de lopéramide si sang ou &lt; 6 ans (DX.10)</li></ul></div>
<div class="ax"><h3>✈️ Retour de voyage</h3><ul>
<li>Test rapide + frottis le jour même ; répéter à 12–24 h (DX.6)</li>
<li>Grave → artésunate i.v. ; Riamet® contre-indiqué</li>
<li>Dengue : PCR/NS1 ≤ 7 j, paracétamol, pas d'AINS ; défervescence = phase critique (DX.7)</li></ul></div>
<div class="ax"><h3>⏳ FUO</h3><ul>
<li>≥ 3 sem, 38,3 °C × 2, immunité normale, bilan de base négatif (DX.4)</li>
<li>VS/CRP élevées → FDG-TEP-TDM → biopsie (DX.8)</li>
<li>&gt; 50 ans, céphalée et vue → prednisone le jour même (DX.5)</li></ul></div>
<div class="ax"><h3>🤧 Viral</h3><ul>
<li>Grippe à risque → oseltamivir 75 mg 2×/j 5 j, dans les 36 h (DX.9)</li>
<li>Fièvre qui repart → radiographie (surinfection)</li>
<li>Paracétamol ≤ 4 g/j ; pas d'ibuprofène au 3e trimestre</li></ul></div>
<div class="ax rf"><h3>🚩 Ordre d'exclusion</h3><ol>
<li>E1 Coup de chaleur (DX.15)</li><li>E2 Sepsis (DX.11)</li><li>E3 Méningite, méningococcie (DX.12)</li>
<li>E4 Neutropénie fébrile (DX.14)</li><li>E5 Paludisme à P. falciparum (DX.6)</li><li>E6 Endocardite (DX.13)</li></ol>
<p class="red" style="margin:6px 0 0">Choc septique : mortalité hospitalière &gt; 40 % ; méningocoque invasif : létalité 7,3 % en Suisse ; FUO néoplasique : 38 % à 6 mois.</p></div>
</div>""",
 algo_html=f"""<table class="algo"><tr><th>Si…</th><th>Alors…</th></tr>
<tr class="e"><td>&gt; 40 °C et confusion après chaleur ou effort</td><td>DX.15 : refroidissement externe immédiat (immersion), 144 ; pas d'antipyrétique</td></tr>
<tr class="e"><td>Hypotension, confusion ou polypnée</td><td>DX.11 : lactate, hémocultures, antibiotique en &lt; 1 h, cristalloïde ≥ 30 mL/kg, noradrénaline si PAM &lt; 65</td></tr>
<tr class="e"><td>Céphalée, raideur, purpura</td><td>DX.12 : hémocultures, dexaméthasone puis ceftriaxone ; ponction sans retarder ; scanner d'abord si coma, déficit, crise</td></tr>
<tr class="e"><td>Neutrophiles &lt; 0,5 G/L</td><td>DX.14 : bêtalactamine antipseudomonale i.v. dans l'heure ; MASCC</td></tr>
<tr class="e"><td>Séjour en zone palustre</td><td>DX.6 : test rapide et frottis le jour même ; répéter à 12–24 h ; artésunate si grave</td></tr>
<tr class="e"><td>Prothèse, souffle nouveau, drogues injectées</td><td>DX.13 : 3 paires d'hémocultures, échocardiographie, ETO si ETT négative</td></tr>
<tr><td>Toux, dyspnée, infiltrat</td><td>DX.1 : score de gravité ; co-amoxicilline à domicile ou ceftriaxone + clarithromycine à l'hôpital</td></tr>
<tr><td>Douleur lombaire, culture positive</td><td>DX.2 : culture puis antibiotique ; imagerie si choc, obstruction ou échec à 72 h</td></tr>
<tr><td>Placard rouge, chaud, bien limité</td><td>DX.3 : bêtalactamine ; marquer la limite ; douleur disproportionnée → chirurgien</td></tr>
<tr><td>Diarrhée aiguë, vomissements</td><td>DX.10 : réhydratation orale ; coproculture si sang ou fièvre élevée</td></tr>
<tr><td>Fièvre brutale, toux, myalgies en saison</td><td>DX.9 : oseltamivir si terrain à risque, dans les 36 h</td></tr>
<tr><td>Retour de voyage, éruption, douleur rétro-orbitaire</td><td>DX.7 : PCR ou NS1 ; paracétamol, pas d'AINS ; signes d'alarme → hôpital</td></tr>
<tr><td>Fièvre ≥ 3 semaines, bilan de base négatif</td><td>DX.4 : FDG-TEP-TDM si VS/CRP élevées ; pas d'antibiotique ni de corticoïde si stable</td></tr>
<tr><td>&gt; 50 ans, céphalée, trouble visuel, CRP élevée</td><td>DX.5 : corticoïde le jour même, échographie ou biopsie ensuite</td></tr>
<tr><td>Perte de poids, sueurs nocturnes, adénopathie</td><td>DX.8 : biopsie de la lésion accessible, sans corticoïde préalable</td></tr>
</table>
<p class="intro">Source : <a href="{R}LOT_006_Phase_A_V0.html#algo">Phase A · Algorithme discriminant</a> et <a href="{R}LOT_006_Phase_A_V0.html#ssp-p10">§10 Arbre décisionnel</a>.</p>""",
)
