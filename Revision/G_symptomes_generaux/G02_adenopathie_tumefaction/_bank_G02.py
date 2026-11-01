# -*- coding: utf-8 -*-
# Banque G2 — Tuméfaction, tumeur, adénopathie (LOT_002). Sources : exclusivement LOT_Claude_Finaux/LOT_002 (Phase A + Phase B DX.1–15).
# Convention : opts[0] = bonne réponse (son « pourquoi pas » est ignoré) ; position finale fixée par build_ssp.py (seed).
# dx : le PREMIER DX.n cité = DX cible (couverture) ; les suivants = discrimination croisée.
R = "../../../repo/LOT_Claude_Finaux/LOT_002/"
def PA(sec, label): return (f"{R}LOT_002_Phase_A_V0.html#{sec}", f"Phase A {label}")
def B(n, p): return (f"{R}LOT_002_Phase_B_V0_DX.{n}.html#dx{n}-p{p}", f"Phase B DX.{n} §{p}")

# ═════════════ BLOC R · RAISONNER (avant de nommer le DX)
q("R","DX.11 🚩E3 vs DX.1","management","cabinet",
 "Un homme de 58 ans, fumeur (40 UPA), consulte pour une « boule » au-dessus de la clavicule gauche remarquée il y a 3 semaines. Ganglion de 1,5 cm, ferme, indolore, mobile. Pas de fièvre, pas de plaie, pas d'angine. Examen ORL normal.",
 "Quelle est la conduite la plus appropriée ?",
 [("TDM thoraco-abdominale puis prélèvement histologique, sans période d'observation",""),
  ("Surveillance clinique et contrôle dans 4 semaines","L'observation de 3 à 4 semaines vaut pour un ganglion localisé au tableau bénin, jamais pour le creux sus-claviculaire (≈ 50 % de malignité en médecine de famille)."),
  ("Amoxicilline-clavulanate 3 × 625 mg/j pendant 10 jours d'essai","L'antibiotique d'essai retarde le diagnostic ; ce siège n'est presque jamais réactif."),
  ("Prednisone 20 mg/j pendant une semaine","Un corticoïde avant la biopsie peut effacer l'image histologique d'un lymphome."),
  ("Sérologie EBV et test hétérophile","Le syndrome mononucléosique ne rend pas bénin un ganglion sus-claviculaire ; et rien ici n'oriente vers l'EBV (58 ans, pas d'angine).")],
 "Tout ganglion sus-claviculaire palpable est malin jusqu'à preuve du contraire (DX.11, rang E3). À gauche, il oriente vers l'abdomen (ganglion de Virchow) ; la conduite est imagerie et prélèvement dans la semaine.",
 "Sus-claviculaire = pas d'observation, pas d'antibiotique d'essai, pas de corticoïde. Chercher d'abord stridor, œdème du visage, dysphagie.",
 B(11,13))

q("R","DX.1 vs DX.2","management","cabinet",
 "Une femme de 24 ans présente depuis 5 jours une douleur dentaire (molaire inférieure droite) et un ganglion sous-maxillaire droit de 1,8 cm, sensible, élastique, mobile, peau légèrement chaude. Température 37,9 °C. Pas de perte de poids ni de sueurs nocturnes.",
 "Quelle est la conduite la plus appropriée ?",
 [("Traiter la porte d'entrée dentaire et réexaminer le ganglion à 3 à 4 semaines",""),
  ("Biopsie-exérèse du ganglion dans la semaine","La biopsie s'impose si le ganglion persiste au-delà de 4 à 6 semaines ou s'il existe un drapeau rouge ; aucun ici."),
  ("TEP-TDM corps entier","Le TEP-TDM sert à stadifier un lymphome confirmé ou à chercher un primitif inconnu, pas à explorer une adénite réactionnelle."),
  ("Cytoponction à l'aiguille fine d'emblée","Inutile devant un ganglion inflammatoire avec porte d'entrée évidente ; elle ne vient qu'en 2e intention après échographie."),
  ("Prednisone courte pour réduire l'inflammation","Jamais de corticoïde devant une adénopathie avant d'avoir exclu un lymphome.")],
 "Ganglion sensible, élastique, mobile + porte d'entrée dans le territoire de drainage = adénopathie réactionnelle (DX.1). On traite la cause, puis on revoit : le diagnostic est confirmé rétrospectivement par la régression en 3 à 4 semaines.",
 "Une amélioration sous antibiotique ne suffit pas à clore le dossier : il faut revoir le ganglion. La douleur seule n'exclut pas un lymphome.",
 B(1,8))

q("R","DX.2 🚩E2 · persistance","assessment_diagnosis","cabinet",
 "Un homme de 46 ans a un ganglion cervical jugulaire de 2,2 cm apparu il y a 7 semaines, sans porte d'entrée retrouvée. Un traitement antibiotique n'a rien changé. L'échographie montre un ganglion rond, sans hile graisseux visible.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Biopsie-exérèse du ganglion le plus anormal (histologie, immunohistochimie, part fraîche, mycobactéries)",""),
  ("Cytoponction à l'aiguille fine et arrêt du bilan si elle est négative","Précision de la cytoponction ≈ 84 % : un résultat négatif n'exclut pas un lymphome ; il faut l'architecture du ganglion entier."),
  ("Nouvelle période d'observation de 4 semaines","Le délai d'observation est déjà dépassé (> 4–6 semaines) et l'échographie est suspecte."),
  ("Deuxième antibiotique à spectre élargi","Un ganglion qui ne régresse pas sous traitement contredit la réaction bénigne ; un 2e essai retarde le diagnostic."),
  ("IRM cervicale avant toute décision","L'imagerie n'apporte pas l'histologie ; l'échographie a déjà montré les critères de malignité.")],
 "Persistance au-delà de 4 à 6 semaines + ganglion rond avec perte du hile = indication de biopsie-exérèse, gold standard qui conserve l'architecture (DX.2, rang E2).",
 "Demandez à la fois histologie avec immunohistochimie, un fragment frais pour cytométrie et un prélèvement pour PCR/culture mycobactériennes : un seul geste pour trancher lymphome, métastase et tuberculose.",
 PA("ssp-p9","§9.a Gold standard"))

q("R","DX.2 🚩 compression médiastinale","management","urgences",
 "Un homme de 31 ans arrive aux urgences pour une dyspnée croissante depuis 4 jours, une voix rauque et un visage bouffi le matin. Il a des adénopathies cervicales et sus-claviculaires dures et confluentes. SpO₂ 92 % à l'air ambiant, stridor discret en décubitus.",
 "Quelle est la priorité immédiate ?",
 [("Position assise, oxygène, voie veineuse, imagerie thoracique en urgence et appel immédiat de l'hématologue",""),
  ("Biopsie-exérèse programmée en ambulatoire dans la semaine","La compression médiastinale (dyspnée, stridor, œdème du visage) précède tout le reste de l'algorithme : c'est une urgence vitale."),
  ("Prednisone 60 mg/j et contrôle à la consultation dans 7 jours","Un corticoïde lyse le lymphome et masque l'histologie ; il ne se discute qu'en urgence vitale, décidé avec l'hématologue, pas en ambulatoire."),
  ("Échographie cervicale ambulatoire","L'échographie cervicale n'évalue pas la masse médiastinale et retarde la prise en charge."),
  ("Amoxicilline-clavulanate et revoir à 3 semaines","Aucune porte d'entrée ; tableau tumoral compressif.")],
 "Étape 0 de l'algorithme : dyspnée, stridor, œdème du visage = masse médiastinale compressive. On sécurise voies aériennes, respiration, circulation, puis bilan (hémogramme, LDH, uricémie, créatinine) et hématologue.",
 "Une compression de la veine cave est une urgence vitale. Dans l'ordre : ABC, voie veineuse + bilan de lyse, hospitalisation-hématologie, pas de corticoïde « réflexe » avant le prélèvement.",
 PA("ssp-p11","§11.B Urgence"))

q("R","DX.13 🚩E5 · DX.14 · ≥ 2 régions","assessment_diagnosis","cabinet",
 "Un homme de 29 ans consulte pour une fatigue depuis 3 semaines. Vous palpez des ganglions cervicaux, axillaires et inguinaux de 1,5 cm, mobiles, peu sensibles. Il a eu des rapports non protégés avec un nouveau partenaire il y a 6 semaines. Pas de splénomégalie.",
 "Quel bilan de première intention est le plus approprié ?",
 [("Test VIH combiné de 4e génération, sérologies syphilis, EBV et CMV, hémogramme",""),
  ("Biopsie-exérèse d'un ganglion inguinal","Des adénopathies généralisées après exposition imposent d'abord les tests infectieux ; la biopsie vient si le bilan est négatif et que les ganglions persistent."),
  ("Surveillance de 4 semaines sans examen","Deux régions ou plus = risque relatif de cancer 6,41 et indication d'un bilan étendu ; l'exposition sexuelle impose des tests."),
  ("TEP-TDM corps entier","Le TEP-TDM ne précède pas les sérologies ; il sert à la stadification d'un lymphome confirmé."),
  ("Anticorps antinucléaires isolés","Les ANA font partie du bilan étendu mais ne sont pas prioritaires devant une exposition sexuelle récente.")],
 "Au moins deux régions atteintes → test VIH, syphilis, EBV, CMV, ANA, hémogramme, échographie (Phase A §10). L'exposition sexuelle place E5 (VIH) et E6 (syphilis) en tête.",
 "Deux régions ganglionnaires atteintes imposent de tester le VIH ET la syphilis : les deux coexistent souvent.",
 PA("ssp-p10","§10 Arbre décisionnel"))

q("R","DX.1 · ganglion normal","assessment_diagnosis","cabinet",
 "Une femme de 35 ans, en bonne santé, a senti une petite « bille » dans le pli de l'aine droite. Vous trouvez un ganglion inguinal de 1,2 cm, souple, mobile, indolore. Pas d'autre ganglion, pas de lésion des jambes ni du périnée, pas de symptômes généraux.",
 "Quelle est la conduite la plus appropriée ?",
 [("Rassurer : variante normale, aucun examen ; reconsulter si le ganglion grossit ou durcit",""),
  ("Échographie inguinale dans la semaine","Les ganglions inguinaux atteignent 1 à 1,5 cm sans maladie : une imagerie ici est un examen inutile."),
  ("Biopsie-exérèse","Aucun critère de biopsie : ni persistance documentée, ni drapeau rouge, ni imagerie suspecte."),
  ("Sérologies VIH et syphilis","Pas d'adénopathie généralisée ni d'exposition rapportée ; le ganglion est dans la norme inguinale."),
  ("TDM abdomino-pelvienne","Irradiation et coût sans indication.")],
 "Un ganglion normal est < 1 cm, souple, mobile, indolore — mais à l'aine et en sous-maxillaire, 1 à 1,5 cm reste une variante normale. Confondre cette variante avec une adénopathie conduit à des examens inutiles.",
 "Expliquez le signe d'alerte : croissance, durcissement, fixation ou persistance → reconsulter. C'est cela, la « surveillance ».",
 PA("ssp-p1","§1 Notions voisines"))

q("R","DX.2 · mécanisme","mechanisms","cours",
 "On compare deux ganglions cervicaux : le premier est sensible, élastique, avec hile graisseux conservé à l'échographie ; le second est dur, fixé, indolore, rond, sans hile.",
 "Quel mécanisme explique le mieux l'aspect du second ganglion ?",
 [("Une prolifération clonale ou métastatique qui détruit l'architecture ganglionnaire",""),
  ("Une distension capsulaire rapide par hyperplasie réactive","La distension capsulaire explique la DOULEUR d'un ganglion inflammatoire ; l'hyperplasie réactive conserve le hile."),
  ("Une hyperplasie folliculaire B en réponse à un antigène du territoire","Réaction bénigne : elle régresse avec la cause et garde l'architecture."),
  ("Un œdème lymphatique par obstruction d'aval","Non décrit comme cause de ganglion dur sans hile dans le cours."),
  ("Une activation macrophagique avec chaleur locale","La chaleur et la sensibilité signent l'inflammation, pas l'infiltration.")],
 "L'infiltration tumorale fige et durcit le ganglion ; la prolifération clonale ou la métastase détruit l'architecture, d'où dureté, fixation et perte du hile.",
 "Le mécanisme prédit l'évolution : l'hyperplasie réactive régresse avec la cause, l'infiltration persiste et progresse. Un ganglion qui grossit ou durcit contredit la réaction bénigne.",
 PA("ssp-p3","§3.1 Physiopathologie"), niv="approfondissement")

q("R","DX.11 · anatomie","mechanisms","cours",
 "Chez un patient de 63 ans, on palpe un ganglion sus-claviculaire gauche (ganglion de Virchow).",
 "Pourquoi ce siège gauche oriente-t-il classiquement vers un cancer abdominal ?",
 [("Le canal thoracique, qui draine la lymphe abdominale, se jette dans l'angle veineux gauche",""),
  ("Le ganglion gauche draine exclusivement le poumon gauche","Le côté droit oriente vers le thorax ; le gauche reçoit le canal thoracique."),
  ("Le nerf phrénique gauche transporte les cellules tumorales","Aucun mécanisme nerveux ne dissémine les métastases ganglionnaires."),
  ("La veine cave inférieure longe le creux sus-claviculaire gauche","Anatomiquement faux ; la veine cave inférieure n'atteint pas le cou."),
  ("Le ganglion gauche est le relais unique de la thyroïde","La thyroïde draine vers les chaînes cervicales, sans latéralisation abdominale.")],
 "Le côté gauche oriente vers l'abdomen parce que le canal thoracique se jette dans l'angle veineux gauche ; le côté droit oriente vers le thorax.",
 "Piège : Virchow ne signe pas toujours un cancer gastrique — dans la série lue, les cancers digestifs ne formaient que 9 % des métastases, le poumon dominait.",
 B(11,14), niv="approfondissement")

q("R","DX.12 🚩E4 vs DX.11","assessment_diagnosis","cabinet",
 "Un homme de 34 ans, arrivé d'une région à forte incidence de tuberculose il y a 2 ans, présente un ganglion cervical de 3 cm, froid, indolore, avec une fistule cutanée qui suinte. Sueurs nocturnes. Radiographie de thorax en cours.",
 "Quel examen est le plus utile pour établir le diagnostic ?",
 [("PCR et culture mycobactériennes sur ponction ou biopsie du ganglion",""),
  ("IGRA sanguin seul","Un IGRA positif indique une infection latente ou active, il ne prouve pas la maladie ; négatif, il n'exclut rien (sensibilité ≈ 0,89)."),
  ("Incision-drainage de la fistule sans prélèvement","L'incision d'un abcès froid sans prélèvement crée une fistule chronique ; il faut ponctionner et cultiver."),
  ("Sérologie Bartonella","Pas de contact avec un chat ; la fistule froide et le contexte orientent vers la tuberculose."),
  ("Test hétérophile","Le syndrome mononucléosique ne donne pas de ganglion froid fistulisé.")],
 "Ganglion froid, fistulisé, sueurs, origine endémique = tuberculose ganglionnaire (DX.12, E4). La preuve est bactériologique sur le ganglion : PCR (Xpert) et culture, avec histologie si biopsie.",
 "Toujours chercher une atteinte pulmonaire : la forme ganglionnaire isolée n'est pas contagieuse, la forme pulmonaire associée l'est. Tester aussi le VIH et déclarer à l'OFSP.",
 B(12,8))

q("R","DX.15 🚩E1 vs DX.6","assessment_diagnosis","pédiatrie",
 "Un garçon de 3 ans a de la fièvre à 39,5 °C depuis 5 jours malgré le paracétamol. Il a les yeux rouges sans sécrétion, les lèvres rouges et fissurées, une éruption polymorphe du tronc et un ganglion cervical unilatéral de 2 cm. Il est très irritable.",
 "Quel est le diagnostic le plus probable ?",
 [("Maladie de Kawasaki complète",""),
  ("Pharyngite à streptocoque du groupe A","Ganglions cervicaux antérieurs sensibles et exsudat, mais pas de conjonctivite bilatérale ni d'atteinte des lèvres et de la peau."),
  ("Mononucléose infectieuse à EBV","Pic d'âge 15 à 24 ans ; angine et ganglions postérieurs, sans conjonctivite non exsudative ni lèvres fissurées."),
  ("Adénopathie réactionnelle d'une infection ORL","Elle n'explique pas la fièvre de 5 jours avec conjonctivite, atteinte buccale et éruption."),
  ("Primo-infection VIH","Ni exposition ni contexte ; tableau typique des critères AHA.")],
 "Fièvre ≥ 5 jours + 4 critères sur 5 (conjonctivite non exsudative, atteinte buccale, extrémités, éruption, ganglion cervical ≥ 1,5 cm) = Kawasaki complet (AHA 2017). C'est E1 : le premier DD grave à exclure.",
 "Le ganglion doit faire ≥ 1,5 cm et est souvent unilatéral. Avec ≥ 4 critères, surtout extrémités, on peut poser le diagnostic dès le 4e jour.",
 B(15,8))

q("R","DX.10 vs DX.13","assessment_diagnosis","hôpital",
 "Un homme de 41 ans, traité par phénytoïne depuis 3 semaines après un traumatisme crânien, présente une fièvre à 38,8 °C, une éruption maculeuse diffuse, des adénopathies cervicales et axillaires. Éosinophiles 1,8 G/L, ALAT 3 fois la norme. Pas d'exposition sexuelle à risque.",
 "Quel diagnostic est le plus probable ?",
 [("Réaction d'hypersensibilité médicamenteuse (DRESS) à la phénytoïne",""),
  ("Primo-infection VIH","Fièvre, éruption et adénopathies, mais pas d'exposition ; l'éosinophilie et la chronologie avec le médicament orientent ailleurs."),
  ("Mononucléose infectieuse","Les lymphocytes atypiques peuvent exister dans les deux, mais l'éosinophilie, l'âge et le délai après le médicament orientent vers le DRESS."),
  ("Lymphome non hodgkinien","Installation trop aiguë, avec éosinophilie, atteinte hépatique et chronologie médicamenteuse."),
  ("Syphilis secondaire","Pas d'éruption palmo-plantaire décrite, pas d'exposition.")],
 "Fièvre, éruption, adénopathie, éosinophilie, atteinte d'organe 2 à 8 semaines après l'introduction = DRESS (score RegiSCAR). L'AIPS de la phénytoïne cite fièvre et lymphadénopathie comme signes précoces d'hypersensibilité.",
 "Toute adénopathie récente impose le recensement de TOUS les médicaments des 3 derniers mois. Délai médian du DRESS ≈ 22 jours ; antiépileptiques = 35 % des cas, allopurinol 18 %.",
 B(10,8))

# ═════════════ BLOC D · DISCRIMINER (un signe, un examen qui tranche)
q("D","DX.4 vs DX.6","assessment_diagnosis","cabinet",
 "Une étudiante de 18 ans a depuis 6 jours une angine exsudative, de la fièvre et une grande fatigue. Ganglions cervicaux postérieurs bilatéraux, rate palpable. Hémogramme : lymphocytes 55 %, lymphocytes atypiques 15 %.",
 "Quel est le diagnostic le plus probable ?",
 [("Mononucléose infectieuse à EBV",""),
  ("Pharyngite à streptocoque du groupe A","Ganglions cervicaux ANTÉRIEURS sensibles, sans splénomégalie ni lymphocytose atypique ; l'exsudat seul ne tranche pas."),
  ("Infection à cytomégalovirus","Syndrome mononucléosique plutôt chez l'adulte, avec angine moins marquée ; on y pense quand l'EBV est négatif."),
  ("Toxoplasmose ganglionnaire","Ganglions cervicaux indolores, peu d'angine ; contexte chat ou viande peu cuite."),
  ("Leucémie aiguë","Elle se présente avec cytopénies ou blastes, pas avec une lymphocytose atypique et une angine fébrile.")],
 "Angine + fièvre + ganglions cervicaux postérieurs + splénomégalie chez un 15–24 ans, lymphocytes > 40 % dont > 10 % atypiques = mononucléose (DX.4).",
 "Signe de Hoagland : œdème bilatéral indolore des paupières supérieures. Le patient n'a pas besoin d'être isolé (séroprévalence > 90 %).",
 B(4,8))

q("D","DX.4 vs DX.5","assessment_diagnosis","cabinet",
 "Un lycéen de 16 ans a un tableau typique de mononucléose depuis 3 jours (angine, fièvre, ganglions cervicaux postérieurs). Le test hétérophile rapide est négatif.",
 "Quelle est la conduite la plus appropriée ?",
 [("Demander une sérologie EBV (VCA-IgM, EBNA) ou répéter le test plus tard",""),
  ("Conclure que la mononucléose est exclue et chercher un lymphome","Le test hétérophile a des faux négatifs en 1re semaine et avant 5 ans ; sa sensibilité n'est que de 87 %."),
  ("Prescrire de l'amoxicilline pour une angine bactérienne présumée","Contre-indiquée si une mononucléose est possible (exanthème > 90 %) ; et pas de test streptocoque positif."),
  ("Sérologie CMV comme seul examen","Le CMV se cherche quand l'EBV est négatif ; ici l'EBV n'est pas encore écarté."),
  ("Biopsie-exérèse d'un ganglion postérieur","Aucun drapeau rouge ; tableau aigu typique.")],
 "Un test hétérophile négatif la première semaine n'exclut pas la mononucléose. La sérologie EBV est plus sensible et plus spécifique ; VCA-IgM positif avec EBNA négatif prouve la primo-infection.",
 "VCA-IgG isolé = infection ancienne possible : ne suffit pas. Lymphocytose seule : ne suffit pas.",
 B(4,14))

q("D","DX.5 vs DX.4","assessment_diagnosis","cabinet",
 "Un homme de 32 ans a depuis 12 jours une fièvre, une fatigue intense, une angine discrète et des ganglions cervicaux. Lymphocytes atypiques 14 %, ALAT 2 fois la norme. Test hétérophile négatif ; sérologie EBV : VCA-IgM négatif, EBNA positif.",
 "Quel examen est le plus approprié ensuite ?",
 [("Sérologie CMV (IgM et IgG) avec avidité des IgG",""),
  ("Répéter le test hétérophile dans 1 semaine","L'EBV aigu est déjà écarté par la sérologie (EBNA positif = infection ancienne)."),
  ("Biopsie-exérèse ganglionnaire","Syndrome mononucléosique aigu sans drapeau rouge : on termine d'abord l'enquête virale."),
  ("PCR CMV sanguine et traitement si faiblement positive","Une PCR faiblement positive chez l'immunocompétent ne suffit pas : excrétion prolongée sans maladie."),
  ("Test rapide streptocoque","Angine discrète, adulte, lymphocytose atypique : le streptocoque n'explique pas le tableau.")],
 "Syndrome mononucléosique avec EBV négatif → CMV (DX.5). IgM positives + IgG de faible avidité = primo-infection probable ; séroconversion sur deux sérums = preuve certaine.",
 "Chez l'adulte à hétérophile négatif, pensez aussi au VIH et à la toxoplasmose.",
 B(5,8))

q("D","DX.5","management","cabinet",
 "Une infirmière de 28 ans, non enceinte, immunocompétente, a une primo-infection à CMV prouvée (séroconversion IgG). Fièvre modérée, fatigue, ALAT 1,5 fois la norme. Elle va bien par ailleurs.",
 "Quel traitement est le plus approprié ?",
 [("Traitement symptomatique par paracétamol, sans antiviral",""),
  ("Valganciclovir 900 mg 2 fois par jour pendant 21 jours","Dose d'induction de la rétinite ; l'antiviral n'est pas indiqué chez l'immunocompétent bien portant."),
  ("Ganciclovir IV 5 mg/kg toutes les 12 h","Réservé à l'immunodéprimé ou aux formes graves, à l'hôpital."),
  ("Amoxicilline 10 jours","Jamais d'amoxicilline dans un syndrome mononucléosique ; pas d'infection bactérienne."),
  ("Prednisone 30 mg/j","Pas de corticoïde de routine ; et jamais avant d'avoir exclu un lymphome si le ganglion persiste.")],
 "Le médecin ne traite pas par antiviral l'immunocompétent bien portant ; le traitement est symptomatique. L'immunodéprimé fébrile, lui, est hospitalisé (ganciclovir ou valganciclovir adapté à la clairance).",
 "Valganciclovir : jamais pendant la grossesse ni l'allaitement (AIPS). Ganglion persistant > 4 semaines ou sus-claviculaire → biopsie, même si un CMV est prouvé.",
 B(5,13))

q("D","DX.6 vs DX.4","assessment_diagnosis","cabinet de pédiatrie",
 "Une fillette de 9 ans a depuis hier une fièvre à 38,6 °C, une odynophagie, pas de toux. Amygdales tuméfiées avec exsudat, ganglions cervicaux antérieurs douloureux. Pas de rate palpable.",
 "Quelle est la prochaine étape la plus appropriée ?",
 [("Test de diagnostic rapide (TDR) du streptocoque, antibiotique seulement s'il est positif",""),
  ("Antibiotique d'emblée sur le score clinique seul","Un score élevé seul trie mal les patients à traiter ; on teste avec 3 à 4 critères et on traite si le test est positif."),
  ("Test hétérophile","Pas de ganglions postérieurs ni de rate ; l'âge et le score orientent vers le streptocoque."),
  ("Dosage des ASLO","Les ASLO montent des semaines plus tard : inutiles en phase aiguë."),
  ("Aucun test : angine virale probable","Avec 4 critères de Centor (+1 McIsaac pour 3–14 ans), le test est indiqué.")],
 "Fièvre > 38 °C, absence de toux, adénopathie cervicale antérieure douloureuse, exsudat = 4 critères de Centor ; McIsaac +1 pour l'âge 3–14 ans. Score 3–4 → TDR ; traiter seulement si positif.",
 "L'exsudat seul ne tranche pas : EBV et adénovirus donnent le même aspect. Un test positif sans symptôme peut n'être qu'un portage.",
 B(6,8))

q("D","DX.6","assessment_diagnosis","cabinet de pédiatrie",
 "Un garçon de 7 ans a 4 critères de Centor (fièvre, pas de toux, exsudat, ganglions cervicaux antérieurs douloureux). Le TDR du streptocoque revient négatif.",
 "Quelle est la conduite la plus appropriée ?",
 [("Culture pharyngée",""),
  ("Conclure à une angine virale sans autre test","Valable chez l'ADULTE (l'ESCMID n'exige pas de culture après TDR négatif) ; chez l'enfant, le TDR manque 14 malades sur 100."),
  ("Amoxicilline 10 jours malgré le test négatif","On ne traite que sur un test positif."),
  ("Dosage des ASLO","Inutiles en phase aiguë."),
  ("Test hétérophile systématique","Rien n'oriente vers l'EBV chez cet enfant de 7 ans.")],
 "Chez l'enfant, un TDR négatif impose une culture pharyngée (critère de référence) ; chez l'adulte, non.",
 "Retenez l'asymétrie enfant/adulte : c'est une question classique de l'examen fédéral.",
 B(6,14))

q("D","DX.1 vs DX.8","management","cabinet",
 "Un jardinier de 50 ans s'est blessé à l'avant-bras droit avec un rosier il y a 6 jours. La plaie est rouge et chaude ; un ganglion axillaire droit de 2 cm est sensible et mobile. Pas de contact avec des chats. Fonction rénale normale, 80 kg, pas d'allergie.",
 "Quel traitement est le plus approprié ?",
 [("Amoxicilline-clavulanate 3 × 625 mg par jour, puis réexamen du ganglion à 3 à 4 semaines",""),
  ("Benzathine benzylpénicilline 2,4 MUI IM dose unique","Dose de la syphilis précoce ; elle ne couvre pas le staphylocoque d'une plaie cutanée."),
  ("Azithromycine 500 mg/j pendant 3 jours","Option (hors AIPS) de la maladie des griffes du chat ; ici pas de chat et une infection cutanée banale."),
  ("Prednisone courte","Jamais de corticoïde devant une adénopathie inexpliquée ; il ne traite pas l'infection."),
  ("Biopsie-exérèse du ganglion axillaire","Adénite réactionnelle avec porte d'entrée évidente : traiter et revoir.")],
 "Adénite bactérienne d'une infection de la peau ou des tissus mous (DX.1) : Augmentin® 3 × 625 mg/j (adulte > 40 kg) couvre staphylocoque et streptocoque.",
 "Clairance 10–30 mL/min : 625 mg toutes les 12 h. Persistance du ganglion après traitement → échographie.",
 PA("ssp-p11","§11.B Traitement par cause"))

q("D","DX.2 🚩E2 vs DX.12","assessment_diagnosis","cabinet",
 "Un homme de 67 ans a perdu 9 kg en 4 mois (12 % de son poids), a des sueurs nocturnes et de la fièvre vespérale. Ganglions cervicaux et axillaires bilatéraux, durs, indolores ; rate palpable. IGRA négatif il y a 2 semaines.",
 "Quelle est la démarche la plus appropriée ?",
 [("Hémogramme et LDH, puis biopsie-exérèse du ganglion le plus anormal, sans corticoïde préalable",""),
  ("Cytoponction cervicale et conclusion si elle est négative","La cytoponction peut passer à côté d'un lymphome ; négative, elle n'exclut rien."),
  ("Prednisone 40 mg/j pour les symptômes B","Le corticoïde lyse le lymphome et masque l'histologie."),
  ("TEP-TDM d'emblée sans histologie","Le TEP-TDM stadifie un lymphome confirmé ; il ne remplace pas la biopsie."),
  ("Traitement antituberculeux d'épreuve","Un IGRA négatif n'exclut pas la tuberculose, mais on ne traite pas à l'aveugle : la biopsie avec culture tranche entre tuberculose et lymphome.")],
 "Symptômes B (fièvre, sueurs nocturnes, perte > 10 % en 6 mois) + ganglions durs dans plusieurs régions + splénomégalie = néoplasie hématologique jusqu'à preuve du contraire (DX.2, E2) : hémogramme, LDH, biopsie-exérèse.",
 "Demandez sur la même pièce l'histologie ET la PCR/culture mycobactériennes : le même ganglion répond aux deux hypothèses graves.",
 PA("algo","Algorithme, étape 2"))

q("D","DX.3 vs DX.9","assessment_diagnosis","hôpital",
 "La biopsie-exérèse d'un ganglion cervical de 2,5 cm chez une femme de 38 ans revient : « inflammation granulomateuse non nécrosante ». La radiographie montre des adénopathies hilaires. L'IGRA est négatif.",
 "Quelle est l'étape suivante la plus appropriée ?",
 [("Compléter par PCR et culture mycobactériennes (et fongiques) avant de retenir une sarcoïdose",""),
  ("Retenir une sarcoïdose et débuter la prednisone","Un granulome seul ne suffit pas : il faut un tableau compatible ET l'exclusion des autres granulomatoses (ATS 2020)."),
  ("Conclure que la tuberculose est exclue par l'IGRA négatif","Un IGRA négatif n'exclut pas la tuberculose : biopsie avec culture et PCR."),
  ("Arrêter le bilan : granulome bénin","Un granulome ganglionnaire décrit un motif histologique, pas une maladie : il impose de chercher la cause."),
  ("Anticorps antinucléaires seuls","Ils orientent vers le lupus, pas vers la cause d'un granulome.")],
 "Le granulome est un motif histologique (DX.3). Critères ATS 2020 de sarcoïdose : tableau compatible + granulome non nécrosant + exclusion des autres causes (tuberculose, mycobactéries, champignons, médicaments, cancer). Les trois sont nécessaires.",
 "Tuberculose et sarcoïdose sont les deux causes principales ; un tiers des cas reste sans diagnostic.",
 B(3,8))

q("D","DX.3 vs DX.12","assessment_diagnosis","hôpital",
 "La biopsie d'un ganglion cervical froid chez un homme de 45 ans montre des granulomes avec nécrose caséeuse centrale.",
 "Vers quelle cause l'histologie oriente-t-elle d'abord ?",
 [("Une infection, en premier lieu la tuberculose",""),
  ("Une sarcoïdose","La sarcoïdose donne des granulomes NON nécrosants, après exclusion de l'infection."),
  ("Un lupus érythémateux","Le lupus n'est pas une cause classique de granulome caséeux."),
  ("Un pseudolymphome médicamenteux","Infiltrat polymorphe sans clonalité, pas de nécrose caséeuse."),
  ("Une hyperplasie réactive banale","Elle conserve l'architecture, sans granulome.")],
 "Granulome nécrosant → infection (tuberculose, mycobactérie non tuberculeuse, Bartonella, champignon) ; non nécrosant → sarcoïdose après exclusion de l'infection.",
 "Granulome caséeux + PCR positive = tuberculose certaine ; granulome caséeux + tableau compatible, culture en attente = probable, on traite.",
 B(3,13))

q("D","DX.7 vs DX.4","assessment_diagnosis","cabinet",
 "Une femme de 27 ans, non enceinte, a depuis 3 semaines une fébricule et deux ganglions occipitaux et cervicaux postérieurs de 1,5 cm, indolores. Elle a adopté deux chats et mange volontiers du tartare. Sérologie toxoplasmose : IgM positives, IgG positives.",
 "Quelle est l'étape suivante la plus appropriée ?",
 [("Demander l'avidité des IgG anti-toxoplasme",""),
  ("Conclure à une toxoplasmose aiguë sur les IgM","Les IgM peuvent persister des mois, voire des années : elles ne suffisent jamais."),
  ("Pyriméthamine + sulfadiazine + acide folinique","Réservés aux formes oculaire, congénitale ou de l'immunodéprimé ; et l'infection n'est pas encore datée."),
  ("Biopsie-exérèse immédiate","Ganglions récents, indolores, sans drapeau rouge ; on date d'abord l'infection."),
  ("Sérologie Bartonella seule","Pas de papule d'inoculation ni de ganglion régional sur le trajet d'une griffure.")],
 "IgM positives isolées ne suffisent pas : l'avidité des IgG tranche (faible = infection récente). Une adénopathie cervicale ou occipitale isolée chez un patient fébrile en bonne santé évoque la toxoplasmose (DX.7).",
 "IgG positives seules = contact ancien (un tiers des Suisses). Le dépistage systématique en grossesse est abandonné en Suisse depuis 2008.",
 B(7,8))

q("D","DX.7","management","cabinet",
 "Une femme de 27 ans, immunocompétente, non enceinte, a une toxoplasmose ganglionnaire récente confirmée (IgG de faible avidité). Fond d'œil normal. Elle va bien.",
 "Quelle est la prise en charge la plus appropriée ?",
 [("Abstention thérapeutique et surveillance du ganglion",""),
  ("Pyriméthamine 100 mg puis 25–50 mg/j + sulfadiazine + acide folinique pendant 3 à 6 semaines","Schéma réservé aux atteintes oculaire, congénitale ou de l'immunodéprimé."),
  ("Cotrimoxazole","Non indiqué dans la toxoplasmose selon l'AIPS (alternative d'études seulement)."),
  ("Azithromycine 3 jours","Option de la maladie des griffes du chat, pas de la toxoplasmose."),
  ("Prednisone","Aucune indication ; masque un lymphome si le ganglion persiste.")],
 "La forme ganglionnaire bénigne de l'immunocompétent guérit seule : abstention (traitement réservé aux formes sévères ou persistantes, oculaires, congénitales, immunodéprimé).",
 "Ganglion sus-claviculaire, dur ou persistant > 4 semaines → biopsie, même avec une sérologie toxo positive.",
 B(7,14))

q("D","DX.8 vs DX.7","assessment_diagnosis","cabinet de pédiatrie",
 "Un garçon de 8 ans a un ganglion axillaire gauche de 3 cm, sensible, apparu il y a 10 jours. Sa famille a adopté un chaton ; il y a 3 semaines, une petite papule est apparue sur son avant-bras gauche griffé. Apyrétique, état général conservé.",
 "Quel est le diagnostic le plus probable ?",
 [("Maladie des griffes du chat (Bartonella henselae)",""),
  ("Toxoplasmose ganglionnaire","Contact avec le chat aussi, mais ganglions cervicaux ou occipitaux indolores, sans papule d'inoculation sur le territoire."),
  ("Tuberculose ganglionnaire","Ganglion froid, souvent fistulisé, contage ; pas de papule d'inoculation."),
  ("Lymphome","Ganglion dur, fixe, indolore, symptômes B ; ici ganglion sensible sur le trajet d'une griffure."),
  ("Maladie de Kawasaki","Fièvre ≥ 5 jours et critères cutanéo-muqueux absents.")],
 "Papule d'inoculation + adénopathie régionale subaiguë sur le trajet d'une griffure de chat = maladie des griffes du chat (DX.8) ; le diagnostic est clinique dans la forme typique.",
 "Bartonella henselae est un bacille à Gram négatif transmis par les puces du chat. La papule manque dans de nombreux cas ; une sérologie négative précoce n'exclut pas (séroconversion tardive, PCR utile).",
 B(8,8))

q("D","DX.9 vs DX.3","assessment_diagnosis","cabinet",
 "Une femme de 30 ans consulte pour des nodules rouges douloureux des jambes, une fièvre à 38 °C et des chevilles gonflées et douloureuses depuis 10 jours. La radiographie de thorax montre des adénopathies hilaires bilatérales.",
 "Quelle est la conduite la plus appropriée ?",
 [("Retenir un syndrome de Löfgren sur le tableau clinique, sans biopsie",""),
  ("Biopsie ganglionnaire médiastinale obligatoire","Le Löfgren typique se diagnostique cliniquement sans biopsie."),
  ("Prednisone 60 mg/j d'emblée","Le Löfgren guérit le plus souvent sans séquelle ; pas de corticothérapie d'emblée."),
  ("Quadrithérapie antituberculeuse","Érythème noueux + adénopathies hilaires bilatérales + périarthrite des chevilles = Löfgren, pas tuberculose."),
  ("TEP-TDM pour exclure un lymphome","Le tableau typique suffit ; la TEP n'est pas indiquée.")],
 "Adénopathies hilaires bilatérales + érythème noueux ou périarthrite des chevilles + fièvre = syndrome de Löfgren (sarcoïdose, DX.9), diagnostic clinique sans biopsie si le tableau est typique.",
 "Prévalence vie entière de la sarcoïdose en Suisse : 121/100 000 ; incidence 7/100 000/an. La calcémie fait partie du bilan de toute sarcoïdose suspectée.",
 B(9,8))

q("D","DX.9 vs DX.11","management","cabinet",
 "Une femme de 44 ans, suivie pour un lupus érythémateux systémique stable, présente un ganglion sus-claviculaire droit de 2 cm, dur, indolore, apparu en un mois.",
 "Quelle est la conduite la plus appropriée ?",
 [("Biopsie sans attendre, après imagerie",""),
  ("Attribuer le ganglion à une poussée de lupus et augmenter la prednisone","Une adénopathie ne se range jamais dans une maladie auto-immune sans exclure lymphome et tuberculose ; le corticoïde masquerait un lymphome."),
  ("Surveillance de 4 semaines","Le siège sus-claviculaire n'autorise aucune observation."),
  ("Dosage des anticorps anti-ADN natif pour confirmer la poussée","Il n'explique pas un ganglion sus-claviculaire dur."),
  ("Hydroxychloroquine à dose majorée","Le ganglion dur sus-claviculaire évoque un cancer ou un lymphome, pas l'activité lupique.")],
 "Chez un lupique, un ganglion sus-claviculaire dur se biopsie sans attendre : il évoque un cancer ou un lymphome. Le terrain auto-immun ne protège pas de la néoplasie.",
 "Même réflexe sous méthotrexate : un nouveau ganglion impose l'arrêt du produit, un avis spécialisé et une biopsie.",
 B(9,14))

q("D","DX.10","management","hôpital",
 "Un homme de 41 ans sous phénytoïne depuis 3 semaines présente un DRESS probable (fièvre, éruption, adénopathies, éosinophilie, cytolyse hépatique). Il n'a pas fait de crise depuis son traumatisme crânien.",
 "Quelle est la conduite la plus appropriée ?",
 [("Arrêter la phénytoïne immédiatement et organiser un relais antiépileptique avec le neurologue",""),
  ("Poursuivre la phénytoïne et ajouter un antihistaminique","Fièvre et éruption sous phénytoïne imposent l'arrêt immédiat (AIPS)."),
  ("Remplacer la phénytoïne par la carbamazépine","Réaction croisée connue entre antiépileptiques aromatiques."),
  ("Biopsie-exérèse avant toute décision thérapeutique","L'arrêt du médicament est urgent ; la biopsie ne se discute que si l'adénopathie persiste après l'arrêt."),
  ("Réduire la dose de moitié en surveillant le taux plasmatique","Une hypersensibilité n'est pas dose-dépendante : arrêt.")],
 "Le traitement de l'adénopathie médicamenteuse est l'arrêt du médicament en cause ; pour un antiépileptique, l'arrêt brusque sans relais expose à un état de mal, d'où le relais organisé avec le neurologue.",
 "Après une réaction cutanée grave à la phénytoïne : jamais de réintroduction, jamais de test de réintroduction.",
 B(10,13))

q("D","DX.10 vs DX.2","assessment_diagnosis","cabinet",
 "Chez un patient dont la phénytoïne a été arrêtée il y a 7 semaines pour une hypersensibilité, un ganglion cervical de 2,5 cm ne régresse pas. Les autres signes ont disparu.",
 "Quelle est l'étape suivante la plus appropriée ?",
 [("Biopsie-exérèse du ganglion",""),
  ("Rassurer : le pseudolymphome médicamenteux peut persister des mois","Le pseudolymphome RÉGRESSE à l'arrêt ; un lymphome vrai persiste."),
  ("Réintroduire la phénytoïne pour tester l'imputabilité","Interdit : l'AIPS exclut toute reprise après une réaction cutanée grave."),
  ("Prednisone pour accélérer la régression","Le corticoïde masquerait un lymphome."),
  ("Répéter l'hémogramme dans 2 mois","Persistance > 4–6 semaines : on prélève, on n'attend plus.")],
 "Le pseudolymphome médicamenteux régresse à l'arrêt du médicament ; s'il persiste, un lymphome vrai est possible : biopsie excisionnelle (infiltrat polymorphe sans clonalité = compatible, mais il faut exclure la clonalité).",
 "Diagnostic de pseudolymphome = rétrospectif : adénopathie après introduction + régression à l'arrêt.",
 B(10,14))

q("D","DX.11 🚩E3","assessment_diagnosis","hôpital",
 "Chez un homme de 61 ans avec un ganglion sus-claviculaire droit de 2 cm, la ponction à l'aiguille fine revient « non diagnostique ». La TDM montre un ganglion isolé.",
 "Quelle est l'étape suivante la plus appropriée ?",
 [("Biopsie chirurgicale d'exérèse du ganglion",""),
  ("Conclure à un ganglion bénin et surveiller","Une ponction non diagnostique n'exclut rien : 50 ponctions sur 270 étaient non diagnostiques dans la série lue."),
  ("Antibiotique d'essai de 2 semaines","Il retarde le diagnostic ; ce siège n'est presque jamais réactif."),
  ("TEP-FDG comme examen final","Le TEP vient si le primitif reste inconnu ; il ne donne pas l'histologie."),
  ("Prednisone d'épreuve","Elle peut effacer l'image histologique d'un lymphome.")],
 "Une ponction non diagnostique d'un ganglion sus-claviculaire impose une biopsie chirurgicale d'exérèse : l'image ne donne pas l'histologie.",
 "La tuberculose ganglionnaire imite la métastase sus-claviculaire : 25,9 % des cytologies de la série étaient granulomateuses. D'où PCR/culture sur la pièce.",
 B(11,8))

q("D","DX.12","management","cabinet",
 "Un homme de 34 ans a une tuberculose ganglionnaire cervicale isolée prouvée (culture positive, souche sensible). Radiographie de thorax et expectorations négatives. Test VIH négatif.",
 "Quel schéma thérapeutique standard est le plus approprié ?",
 [("6 mois : 2 mois de rifampicine-isoniazide-pyrazinamide-éthambutol, puis 4 mois de rifampicine-isoniazide",""),
  ("2 mois de quadrithérapie seulement","La phase intensive de 2 mois est suivie de 4 mois de bithérapie."),
  ("Isoniazide seul pendant 9 mois","Schéma de la prophylaxie de l'infection latente, pas de la maladie."),
  ("Exérèse chirurgicale sans antituberculeux","La chirurgie ne remplace pas le traitement de la maladie active."),
  ("Rifampicine-isoniazide 12 mois sans phase intensive","Pas de standard sans phase intensive ; la durée prolongée concerne les formes disséminées ou neuroméningées.")],
 "Standard : 6 mois, 2 HRZE + 4 HR. La forme ganglionnaire isolée n'est pas contagieuse (pas d'isolement), mais elle se déclare à l'OFSP.",
 "Surveiller ASAT/ALAT toutes les 2 à 4 semaines, l'acuité et la vision rouge-vert sous éthambutol, ajouter la pyridoxine sous isoniazide.",
 B(12,13))

q("D","DX.13 🚩E5 vs DX.4","assessment_diagnosis","cabinet",
 "Un homme de 24 ans ayant des rapports avec des hommes consulte 3 semaines après un rapport anal non protégé : fièvre à 38,7 °C, angine, éruption maculeuse du tronc, adénopathies cervicales et axillaires, aphtes.",
 "Quel examen est le plus approprié ?",
 [("Test VIH combiné de 4e génération, complété par l'ARN du VIH (charge virale)",""),
  ("Test hétérophile seul","L'EBV ressemble à la primo-infection VIH, mais l'exposition impose le test VIH ; on teste les quatre (VIH, EBV, CMV, syphilis)."),
  ("Autotest VIH rapide","Un test rapide ou un autotest négatif ne suffit pas, surtout en phase aiguë."),
  ("Biopsie-exérèse ganglionnaire","Tableau aigu post-exposition : le diagnostic est biologique."),
  ("Aucun test avant 3 mois","La fenêtre sérologique se contourne par l'antigène p24 et l'ARN ; attendre 3 mois retarde le traitement.")],
 "Fièvre + pharyngite + éruption + adénopathies après exposition = primo-infection VIH jusqu'à preuve du contraire (DX.13, E5). Le test combiné (anticorps + p24) et l'ARN posent le diagnostic.",
 "Dépister aussi la syphilis et les autres IST chez tout nouveau cas de VIH.",
 B(13,8))

q("D","DX.13","management","cabinet",
 "Chez un homme de 24 ans, l'ARN du VIH-1 est élevé et le test combiné positif. Le génotype de résistance est demandé, résultat attendu dans 10 jours. Méningite, sepsis et infection opportuniste sont exclus.",
 "Quand débuter le traitement antirétroviral ?",
 [("Le jour même du diagnostic, sans attendre le génotype",""),
  ("Après le résultat du génotype","Le génotype ajuste le traitement ensuite ; il ne le retarde pas."),
  ("Quand les CD4 passent sous 350/µL","Ancienne stratégie : on traite tout diagnostic d'emblée."),
  ("Après séroconversion complète au Western blot","Le traitement n'attend pas la séroconversion."),
  ("Après 3 mois pour laisser le système immunitaire contrôler le virus","Aucune base ; le traitement précoce est la règle.")],
 "Le traitement antirétroviral commence le jour du diagnostic, sans attendre le génotype (EACS 2025), initié par un médecin expérimenté (infectiologue).",
 "But : charge virale indétectable.",
 B(13,13))

q("D","DX.14 🚩E6 vs DX.13","assessment_diagnosis","cabinet",
 "Un homme de 37 ans a depuis 2 semaines une éruption de macules rosées sur les paumes et les plantes, non prurigineuse, des adénopathies cervicales, axillaires et épitrochléennes, et une fébricule. Il se souvient d'une « petite plaie » génitale indolore il y a 2 mois.",
 "Quels examens posent le diagnostic ?",
 [("Un test tréponémique et un test non tréponémique avec titre",""),
  ("Un test tréponémique seul","Il reste positif à vie : il ne juge pas l'activité."),
  ("Un test non tréponémique seul","Faux positifs possibles (grossesse, lupus, mononucléose)."),
  ("Une biopsie cutanée","Le diagnostic est sérologique ; la PCR ou le fond noir servent sur une lésion accessible."),
  ("Le test VIH comme unique examen","Indispensable aussi, mais l'éruption palmo-plantaire oriente vers la syphilis secondaire, qui se prouve par les sérologies.")],
 "Éruption palmo-plantaire non prurigineuse + adénopathies généralisées = syphilis secondaire (DX.14, E6). Diagnostic : test tréponémique + test non tréponémique actif (quantitatif).",
 "Ganglion épitrochléen > 0,5 cm = pathologique (syphilis, lymphome, infection de la main). Test non tréponémique négatif avec éruption typique : phénomène de zone, diluer le sérum.",
 B(14,8))

q("D","DX.14","management","cabinet",
 "Un homme de 37 ans a une syphilis secondaire confirmée, sans atteinte neurologique, oculaire ni otique. Pas d'allergie. Test VIH négatif.",
 "Quel traitement est le plus approprié ?",
 [("Benzathine benzylpénicilline (Extencilline®) 2,4 MUI IM en dose unique, et traitement des partenaires récents",""),
  ("Benzathine benzylpénicilline 1,2 MUI IM dose unique","Dose de l'infection streptococcique de l'adulte, insuffisante pour la syphilis."),
  ("Benzathine benzylpénicilline 2,4 MUI IM une fois par semaine pendant 3 semaines","Schéma de la syphilis TARDIVE."),
  ("Amoxicilline-clavulanate 10 jours","Pas de schéma de la syphilis."),
  ("Pénicilline G intraveineuse 14 jours","Réservée à la neurosyphilis (atteint le LCR) ; pas nécessaire ici.")],
 "Syphilis précoce (primaire, secondaire) : Extencilline® 2,4 MUI IM en dose unique (AIPS). Traiter les partenaires, déclarer à l'OFSP.",
 "Prévenir le patient de la réaction de Jarisch-Herxheimer (fièvre dans les 2 à 12 h).",
 B(14,13))

q("D","DX.15 🚩E1","management","pédiatrie",
 "Un garçon de 3 ans au Kawasaki complet est au 6e jour de fièvre. L'échocardiographie n'est disponible que demain matin.",
 "Quelle est la conduite la plus appropriée ?",
 [("Immunoglobulines IV 2 g/kg en dose unique avec acide acétylsalicylique, sans attendre l'échocardiographie",""),
  ("Attendre l'échocardiographie avant tout traitement","Une échographie normale au début n'exclut pas la maladie ; on traite avant le 10e jour sans la retarder."),
  ("Prednisone seule","Les corticoïdes s'ajoutent en cas de résistance aux immunoglobulines, pas seuls en première intention."),
  ("Antibiothérapie IV pour une infection bactérienne","Le tableau remplit les critères ; l'antibiotique ne protège pas les coronaires."),
  ("Acide acétylsalicylique seul en ambulatoire","Il ne remplace pas les immunoglobulines qui réduisent le risque coronarien.")],
 "Kawasaki : immunoglobulines 2,0 g/kg en dose unique (ou 1,6–2,0 g/kg sur 2 à 5 jours) avec aspirine, avant le 10e jour de fièvre ; l'échocardiographie avec Z-score se fait sans retarder le traitement.",
 "Non traité, l'anévrisme touche ≈ 25 % des cas. Échographie au diagnostic, à 1–2 semaines et à 4–6 semaines.",
 B(15,13))

# ═════════════ BLOC P · PIÈGES & ALARMES
q("P","DX.2 🚩 corticoïde","management","cabinet",
 "Un homme de 52 ans a des ganglions cervicaux de 2 cm depuis 6 semaines, sans diagnostic. Il demande « une cortisone pour faire dégonfler », comme un ami qui « avait la même chose ».",
 "Quelle est la réponse la plus appropriée ?",
 [("Refuser tout corticoïde avant la biopsie, car il peut masquer un lymphome",""),
  ("Prednisone 20 mg/j pendant 5 jours puis réévaluer","Le corticoïde lyse le lymphome et masque l'histologie."),
  ("Prednisone si l'échographie est rassurante","Ganglion > 6 semaines = biopsie ; et jamais de corticoïde avant."),
  ("Corticoïde local injecté dans le ganglion","Même piège : altération histologique."),
  ("Dexaméthasone en une seule dose","Même une dose peut fausser l'histologie d'un lymphome.")],
 "Point clé : ne jamais donner de corticoïde avant d'avoir exclu un lymphome. Un ganglion > 1 cm persistant au-delà de 4 à 6 semaines impose la biopsie-exérèse.",
 "Le corticoïde favorise aussi la tuberculose en cas de granulome méconnu.",
 PA("ssp-p13","§13 Points clés"))

q("P","DX.2 🚩 cytopénie","management","cabinet",
 "Un homme de 22 ans consulte pour des ganglions cervicaux et une grande fatigue. L'hémogramme montre hémoglobine 82 g/L, plaquettes 38 G/L et des blastes au frottis.",
 "Quelle est la conduite la plus appropriée ?",
 [("Avis hématologique le jour même",""),
  ("Test hétérophile et contrôle de l'hémogramme dans 2 semaines","Les cytopénies avec blastes signent une infiltration médullaire, pas une mononucléose."),
  ("Biopsie-exérèse programmée en ambulatoire","Le frottis oriente déjà vers une leucémie : l'urgence est hématologique."),
  ("Supplément de fer et contrôle à 1 mois","L'anémie est ici centrale, pas carentielle."),
  ("Échographie cervicale","Ne change rien à l'urgence.")],
 "Cytopénie ou blastes à l'hémogramme = infiltration médullaire (DX.2, leucémie) : frottis et avis hématologique le jour même.",
 "Chaque drapeau rouge a son action : blastes → hématologue aujourd'hui.",
 PA("ssp-p4","§4 Drapeaux rouges"))

q("P","DX.4","management","cabinet",
 "Un joueur de rugby de 19 ans a une mononucléose confirmée depuis 8 jours ; rate palpable. Il veut rejouer le match du week-end prochain.",
 "Quel conseil est le plus approprié ?",
 [("Pas de sport de contact pendant au moins 3 semaines, parfois jusqu'à disparition de la splénomégalie",""),
  ("Reprise autorisée dès l'apyrexie","Le risque de rupture splénique persiste surtout dans les 3 premières semaines, indépendamment de la fièvre."),
  ("Reprise autorisée avec une protection abdominale","Aucune protection ne remplace l'éviction."),
  ("Reprise après une cure courte de corticoïde","Pas de corticoïde de routine ; aucun effet démontré sur le risque splénique."),
  ("Reprise si le test hétérophile se négative","Le test ne guide pas la reprise.")],
 "Rupture splénique : 0,1 à 0,5 %, le plus souvent dans les 3 semaines. Pas de sport de contact avant 3 semaines, parfois jusqu'à 8 semaines ou disparition de la splénomégalie.",
 "Douleur de l'hypocondre ou de l'épaule gauche = exclure une rupture splénique en urgence.",
 B(4,14))

q("P","DX.4 vs DX.6","management","cabinet",
 "Une jeune femme de 20 ans a une angine exsudative fébrile, des ganglions cervicaux postérieurs et une splénomégalie. Le TDR streptocoque est négatif, le test hétérophile positif.",
 "Quel médicament est contre-indiqué ?",
 [("Amoxicilline",""),
  ("Paracétamol","Traitement symptomatique de référence (max 4 g/j chez l'adulte)."),
  ("Ibuprofène","Antalgique accepté pour la gorge dans le cours."),
  ("Solution de réhydratation orale","Mesure de soutien sans contre-indication."),
  ("Pastilles de lidocaïne pour la gorge","Antalgique local sans contre-indication liée à la mononucléose.")],
 "L'amoxicilline est contre-indiquée dans la mononucléose (AIPS) : exanthème dans plus de 90 % des cas.",
 "Cet exanthème est le plus souvent non allergique : ne pas étiqueter « allergie à la pénicilline » sans confirmation.",
 B(4,13), pol="negative")

q("P","DX.8","management","cabinet de pédiatrie",
 "Un garçon de 8 ans avec maladie des griffes du chat typique revient : le ganglion axillaire est devenu fluctuant et très douloureux. Apyrétique, immunocompétent.",
 "Quelle est la conduite la plus appropriée ?",
 [("Aspiration à l'aiguille pour soulager la douleur",""),
  ("Incision-drainage chirurgicale","On n'incise pas : risque de fistule chronique ; on aspire."),
  ("Exérèse chirurgicale du ganglion","Maladie spontanément résolutive ; l'exérèse n'est pas le geste de la forme typique fluctuante."),
  ("Gentamicine IV","Réservée à l'endocardite à Bartonella (avec doxycycline)."),
  ("Prednisone","Aucune indication.")],
 "Ganglion fluctuant de la maladie des griffes du chat : aspiration à l'aiguille, pas d'incision. L'antibiotique est facultatif chez l'immunocompétent.",
 "Azithromycine (hors AIPS) : réduction plus rapide du volume du ganglion le 1er mois (7/14 contre 1/15), sans différence ensuite.",
 B(8,14))

q("P","DX.12 🚩E4","assessment_diagnosis","hôpital",
 "Chez une femme de 29 ans née en Érythrée, la ponction d'un ganglion cervical froid montre un granulome caséeux. L'IGRA est négatif ; l'interne propose de « classer la tuberculose ».",
 "Quelle est la conduite la plus appropriée ?",
 [("Poursuivre : PCR et culture mycobactériennes sur le prélèvement",""),
  ("Exclure la tuberculose sur l'IGRA négatif","Sensibilité groupée de l'IGRA ≈ 0,89 : environ un cas sur dix passe à travers."),
  ("Retenir une sarcoïdose","Le granulome caséeux oriente vers l'infection, pas la sarcoïdose."),
  ("Répéter l'IGRA dans 3 mois","L'IGRA ne prouve ni n'exclut la maladie ganglionnaire ; la preuve est sur le ganglion."),
  ("Débuter une prednisone pour le ganglion","Le corticoïde favorise la tuberculose et masque un lymphome.")],
 "Un IGRA négatif avec ganglion caséeux ne dispense pas de la PCR et de la culture : seule la preuve du bacille (ou le faisceau granulome caséeux + tableau) pose le diagnostic.",
 "Les trois quarts des tuberculoses suisses sont d'origine étrangère ; l'Xpert sur ganglion n'est pas parfait non plus (sensibilité ≈ 79 %).",
 B(12,14))

q("P","DX.12","management","cabinet",
 "Une femme de 31 ans, enceinte de 14 semaines, a une tuberculose ganglionnaire prouvée. Vous préparez le schéma avec le pneumologue.",
 "Quel antituberculeux l'AIPS interdit-il pendant la grossesse ?",
 [("Pyrazinamide",""),
  ("Rifampicine","Pas d'interdiction de grossesse citée dans le cours ; interaction avec les contraceptifs hormonaux."),
  ("Isoniazide","Pas d'interdiction de grossesse citée ; associer la pyridoxine."),
  ("Éthambutol","Pas d'interdiction de grossesse citée ; surveiller la vision."),
  ("Pyridoxine","Supplément vitaminique associé à l'isoniazide, sans interdiction.")],
 "Le pyrazinamide ne doit pas être pris pendant la grossesse ni l'allaitement (AIPS) ; il est aussi contre-indiqué en cas d'hépatite aiguë ou de clairance < 50 mL/min.",
 "Point clé de la monographie G2 : « Le pyrazinamide est interdit pendant la grossesse selon l'AIPS. »",
 PA("ssp-p11","§11.B Situations spéciales"), pol="negative")

q("P","DX.13 🚩E5","assessment_diagnosis","cabinet",
 "Un homme de 33 ans consulte 10 jours après un rapport non protégé avec un partenaire de statut inconnu. Il a de la fièvre, une angine et des ganglions cervicaux. Le test VIH combiné de 4e génération est négatif.",
 "Quelle est la conduite la plus appropriée ?",
 [("Doser l'ARN du VIH et répéter le test combiné à 2–4 semaines",""),
  ("Rassurer : le VIH est exclu","Fenêtre sérologique : un test négatif tôt après l'exposition n'exclut pas la primo-infection."),
  ("Débuter une PrEP immédiatement","Chez un patient fébrile exposé récemment, la PrEP se retarde et le statut VIH se reconfirme : la PrEP seule sur une infection aiguë sélectionne des résistances."),
  ("Démarrer une PEP","La PEP se démarre si l'exposition date de moins de 72 heures ; ici 10 jours."),
  ("Test hétérophile et arrêt du bilan VIH","On teste les quatre (VIH, EBV, CMV, syphilis) ; l'EBV ne dispense pas du VIH.")],
 "Un test combiné négatif à J10 n'exclut pas le VIH : l'ARN (stade de Fiebig I) et la répétition du test tranchent.",
 "Exposition < 72 h → PEP aussitôt ; au-delà, avec symptômes → ARN.",
 B(13,14))

q("P","DX.15 🚩E1 · forme incomplète","assessment_diagnosis","pédiatrie",
 "Un nourrisson de 5 mois a de la fièvre depuis 7 jours sans foyer. CRP 120 mg/L. Il ne remplit aucun critère clinique complet de Kawasaki ; urines, hémocultures et radiographie sont négatives.",
 "Quelle est la conduite la plus appropriée ?",
 [("Échocardiographie et algorithme de forme incomplète de Kawasaki",""),
  ("Exclure le Kawasaki faute de 4 critères","Le nourrisson fait souvent des formes incomplètes : fièvre de 7 jours sans autre cause suffit à y penser."),
  ("Poursuivre la surveillance de la fièvre jusqu'au 10e jour","Les immunoglobulines se donnent avant le 10e jour ; attendre expose les coronaires."),
  ("Antibiothérapie IV empirique seule","Bilan infectieux négatif ; elle ne protège pas les coronaires."),
  ("Biopsie ganglionnaire","Aucun rôle dans le Kawasaki.")],
 "Nourrisson < 6 mois, fièvre ≥ 7 jours, CRP élevée, sans autre cause : échocardiographie même sans critère complet ; traiter si positive.",
 "Forme incomplète = piège n°1 du Kawasaki chez le nourrisson.",
 B(15,13))

# ═════════════ APPROFONDISSEMENT (AP) — mécanismes, nuances
q("D","DX.3 · enfant","assessment_diagnosis","pédiatrie",
 "Un garçon de 3 ans, en bonne santé, a un ganglion sous-mandibulaire de 3 cm, indolore, violacé, évoluant depuis 6 semaines. La biopsie montre des granulomes nécrosants ; pas de contage tuberculeux.",
 "Quelle cause est la plus fréquente de ce tableau granulomateux chez l'enfant ?",
 [("Une mycobactérie non tuberculeuse",""),
  ("Mycobacterium tuberculosis","Possible, mais chez l'enfant la première cause de granulome ganglionnaire est la mycobactérie non tuberculeuse (≈ 50 % dans la série danoise)."),
  ("La sarcoïdose","Granulome non nécrosant, rare à cet âge."),
  ("La toxoplasmose","Hyperplasie folliculaire avec histiocytes épithélioïdes, pas de nécrose."),
  ("Le lupus érythémateux","Pas une cause granulomateuse classique.")],
 "Chez l'enfant, la mycobactérie non tuberculeuse est la première cause d'adénopathie granulomateuse (50 % dans la série danoise lue).",
 "Le granulome nécrosant oriente vers l'infection ; PCR et culture restent indispensables pour typer la mycobactérie.",
 B(3,14), niv="approfondissement")

q("D","DX.5 · sérologie","assessment_diagnosis","cabinet",
 "Une femme de 30 ans a des IgM anti-CMV positives sur un bilan de fatigue. Les IgG sont positives.",
 "Quel examen permet le mieux de dater l'infection ?",
 [("L'avidité des IgG anti-CMV",""),
  ("Le titre des IgM","Les IgM persistent plusieurs mois et réagissent de façon croisée avec l'EBV."),
  ("Le test hétérophile","Faux positifs décrits avec le CMV aigu ; il ne date pas le CMV."),
  ("La PCR CMV sanguine","Une excrétion prolongée existe sans maladie chez l'immunocompétent."),
  ("Le dosage des transaminases","Signe de complication, pas outil de datation.")],
 "Avidité = force de liaison des IgG au virus : faible dans les 2 à 4 mois suivant l'infection, puis forte. IgM + IgG de faible avidité = primo-infection probable.",
 "La séroconversion sur deux sérums espacés de 2 à 3 semaines reste la seule preuve certaine.",
 B(5,8), niv="approfondissement")

q("D","DX.6 · allergie","management","cabinet",
 "Un homme de 27 ans a une pharyngite à streptocoque prouvée (TDR positif). Il a fait un œdème de Quincke sous pénicilline il y a 5 ans.",
 "Quel antibiotique est le plus approprié ?",
 [("Clindamycine 300 mg 2 fois par jour pendant 10 jours",""),
  ("Céfuroxime 250 mg 2 fois par jour","Réservée à l'allergie NON immédiate ; l'œdème de Quincke est une allergie de type 1."),
  ("Amoxicilline 750 mg 3 fois par jour","Pénicilline : contre-indiquée."),
  ("Benzathine benzylpénicilline 1,2 MUI IM","Pénicilline : contre-indiquée."),
  ("Ceftriaxone 2 g/j","Céphalosporine réservée à l'abcès ; même problème que la céfuroxime dans l'allergie immédiate.")],
 "Allergie de type 1 (immédiate) : clindamycine 300 mg 2×/j pendant 10 jours (AIPS), ou un macrolide. Allergie non immédiate : céfuroxime.",
 "Durée : 10 jours pour les streptocoques bêta-hémolytiques. Le traitement de référence reste la pénicilline V.",
 B(6,14), niv="approfondissement")

q("D","DX.7 · pharmacologie","mechanisms","hôpital",
 "Une patiente immunodéprimée reçoit pyriméthamine + sulfadiazine pour une toxoplasmose. L'interne propose de donner de l'acide folique plutôt que de l'acide folinique, « c'est pareil et moins cher ».",
 "Pourquoi faut-il l'acide FOLINIQUE ?",
 [("La pyriméthamine inhibe la dihydrofolate réductase : seul un folate déjà réduit (folinate) contourne le blocage",""),
  ("L'acide folique potentialiserait la toxicité rénale de la sulfadiazine","Ce n'est pas le mécanisme invoqué dans le cours."),
  ("L'acide folique est contre-indiqué chez l'immunodéprimé","Faux : le problème est pharmacologique (DHFR), pas le terrain."),
  ("Le folinate tue directement le parasite","Il protège la moelle du patient, il n'est pas antiparasitaire."),
  ("L'acide folique inactive la pyriméthamine dans l'intestin","Aucune interaction de ce type n'est décrite.")],
 "La pyriméthamine bloque la DHFR ; l'acide folique pur doit être réduit par cette enzyme et ne corrige donc pas le déficit. Le folinate (déjà réduit) protège la moelle.",
 "Hémogramme chaque semaine (2×/sem chez l'immunosupprimé) ; pyriméthamine exclue au 1er trimestre de grossesse.",
 B(7,14), niv="approfondissement")

q("D","DX.10 · réaction croisée","management","hôpital",
 "Après un DRESS à la phénytoïne, le neurologue cherche un antiépileptique de relais.",
 "Quel antiépileptique faut-il éviter en raison d'une réaction croisée connue ?",
 [("Carbamazépine",""),
  ("Lévétiracétam","Non aromatique : pas de réaction croisée décrite dans le cours."),
  ("Valproate","Non aromatique : pas de réaction croisée décrite dans le cours."),
  ("Clobazam","Benzodiazépine non aromatique, pas de réaction croisée décrite."),
  ("Lacosamide","Non cité parmi les aromatiques à réaction croisée.")],
 "Réaction croisée entre antiépileptiques aromatiques (phénytoïne, carbamazépine, phénobarbital) : on ne remplace pas la phénytoïne par la carbamazépine.",
 "L'arrêt brusque d'un antiépileptique expose à un état de mal : relais organisé.",
 B(10,13), pol="negative", niv="approfondissement")

q("D","DX.12 · réaction paradoxale","management","cabinet",
 "Un patient traité depuis 7 semaines pour une tuberculose ganglionnaire cervicale sensible, observant, voit son ganglion grossir et devenir fluctuant. Il va bien, sans fièvre ; la culture du pus est négative.",
 "Quelle est l'interprétation la plus probable ?",
 [("Une réaction paradoxale : on poursuit le traitement et on demande un avis",""),
  ("Un échec thérapeutique par résistance","Sur souche sensible, avec observance et culture négative, l'aggravation évoque d'abord une réaction paradoxale."),
  ("Un lymphome associé, à exclure par l'arrêt du traitement","On n'arrête pas un traitement efficace ; l'avis spécialisé décide d'un éventuel prélèvement."),
  ("Une toxicité de l'éthambutol","L'éthambutol donne une névrite optique, pas un ganglion."),
  ("Une indication à une incision large","L'incision d'un abcès froid crée une fistule chronique.")],
 "Une aggravation du ganglion sous traitement évoque une réaction paradoxale, pas un échec : on poursuit et on demande un avis.",
 "Sous rifampicine : contraception non hormonale. Sous isoniazide : pyridoxine 10–20 mg/j.",
 B(12,14), niv="approfondissement")

q("D","DX.13 · U=U","mechanisms","cabinet",
 "Un homme de 40 ans, séropositif, traité depuis 2 ans, a un ARN du VIH indétectable de façon stable. Son partenaire séronégatif demande s'il risque une transmission sexuelle.",
 "Quelle réponse est la plus juste ?",
 [("Non : avec un ARN durablement indétectable, le VIH ne se transmet pas par voie sexuelle (U=U)",""),
  ("Oui, le risque reste celui d'un patient non traité","Faux : principe U=U."),
  ("Oui, sauf si le partenaire prend une PEP après chaque rapport","La PEP traite une exposition ponctuelle, ce n'est pas une stratégie de couple."),
  ("Le risque dépend uniquement des CD4","C'est la charge virale indétectable qui fonde U=U."),
  ("Non, mais seulement si les anticorps ont disparu","Les anticorps persistent ; ils ne déterminent pas la transmission.")],
 "U=U (Undetectable = Untransmittable) : un patient traité avec un ARN indétectable ne transmet pas le virus par voie sexuelle.",
 "Le but du traitement est la charge virale indétectable — bénéfice individuel ET de santé publique.",
 B(13,14), niv="approfondissement")

q("D","DX.14 · Jarisch-Herxheimer","management","cabinet",
 "Quatre heures après l'injection d'Extencilline® 2,4 MUI pour une syphilis secondaire, le patient rappelle : frissons, fièvre à 38,9 °C, céphalées, éruption plus visible. Pas de dyspnée, pas d'urticaire.",
 "Quelle est l'explication et la conduite la plus appropriées ?",
 [("Réaction de Jarisch-Herxheimer : rassurer et donner un antipyrétique",""),
  ("Allergie à la pénicilline : adrénaline et contre-indication définitive","Délai de 2 à 12 h, fièvre et majoration de l'éruption sans signe anaphylactique : réaction attendue, pas une allergie."),
  ("Échec du traitement : 2e injection immédiate","La réaction témoigne de la lyse des tréponèmes, pas d'un échec."),
  ("Neurosyphilis : pénicilline G IV en urgence","Aucun signe neurologique ; la réaction est systémique et transitoire."),
  ("Primo-infection VIH : test combiné en urgence","Le test VIH est utile, mais n'explique pas la fièvre post-injection.")],
 "Jarisch-Herxheimer : fièvre dans les 2 à 12 heures après la première injection ; rassurer et donner un antipyrétique. Il faut en prévenir le patient avant l'injection.",
 "Toujours associer le test VIH et le traitement des partenaires récents.",
 B(14,14), niv="approfondissement")

q("D","DX.15 · résistance IVIG","management","pédiatrie",
 "Un enfant de 4 ans avec Kawasaki a reçu des immunoglobulines 2 g/kg et de l'aspirine. 40 heures après la fin de la perfusion, la fièvre persiste à 39 °C.",
 "Quelle est la conduite la plus appropriée ?",
 [("Retenir une résistance aux immunoglobulines : ajouter un corticoïde ou une deuxième cure",""),
  ("Attendre 7 jours de plus","Fièvre ≥ 36 h après la fin de la perfusion = résistance ; l'attente expose les coronaires."),
  ("Ajouter de l'ibuprofène","L'ibuprofène est évité sous aspirine : il peut inhiber l'effet antiagrégant."),
  ("Antibiothérapie IV","Aucun argument infectieux ; il s'agit de la maladie."),
  ("Arrêter l'aspirine","Elle reste indiquée.")],
 "Une fièvre persistante ou récurrente ≥ 36 heures après la fin des immunoglobulines signe une résistance : corticoïde ou deuxième cure.",
 "Le score de Kobayashi (risque de résistance) est peu fiable chez l'enfant européen : ne pas s'y fier en Suisse.",
 B(15,14), niv="approfondissement")

# ═════════════ SPÉCIALISTE (SPE) — sentir la spécialité (🔥)
q("D","DX.2 · Lugano","assessment_diagnosis","hématologie",
 "Un lymphome de Hodgkin est confirmé chez une femme de 34 ans. Le PET-TDM montre des ganglions cervicaux et médiastinaux, ainsi que des ganglions rétropéritonéaux ; pas d'atteinte extra-ganglionnaire.",
 "Quel stade de Lugano retenez-vous ?",
 [("Stade III",""),
  ("Stade I","Une seule aire ganglionnaire."),
  ("Stade II","Deux aires ou plus du MÊME côté du diaphragme ; ici les deux côtés sont atteints."),
  ("Stade IV","Exige une atteinte extra-ganglionnaire non contiguë."),
  ("Stade non déterminable sans biopsie médullaire","La biopsie médullaire n'est plus indiquée en routine pour le Hodgkin ; le PET-TDM stadifie.")],
 "Lugano 2014 : I = une aire ; II = ≥ 2 aires du même côté du diaphragme ; III = des deux côtés ; IV = extra-ganglionnaire non contigu. Le PET-TDM est intégré à la stadification des lymphomes avides de FDG.",
 "Suffixes A/B réservés au Hodgkin. Ne jamais associer bléomycine et brentuximab (toxicité pulmonaire).",
 B(2,8), niv="specialiste", spe="Hématologie")

q("D","DX.3 · sarcoïdose","assessment_diagnosis","pneumologie",
 "Une sarcoïdose ganglionnaire médiastinale est retenue chez un homme de 42 ans après exclusion des infections.",
 "Quel examen de base a une recommandation forte dans le bilan initial ?",
 [("La calcémie",""),
  ("Le dosage de l'ECA comme critère diagnostique","L'ECA aide mais ne pose pas le diagnostic ; la recommandation forte vise la calcémie."),
  ("Le TEP-TDM systématique","Non systématique dans le bilan de base."),
  ("La biopsie médullaire","Sans objet dans la sarcoïdose."),
  ("L'IGRA répété tous les 3 mois","L'IGRA ne surveille pas une sarcoïdose.")],
 "La calcémie et l'ECG font partie du bilan de toute sarcoïdose suspectée ; la calcémie a une recommandation forte.",
 "Sous immunothérapie anticancéreuse, un granulome peut être une réaction sarcoïdosique et non une progression : biopsier.",
 B(3,14), niv="specialiste", spe="Pneumologie")

q("D","DX.7 · encéphalite","management","infectiologie",
 "Un patient VIH avec CD4 effondrés a des lésions cérébrales annulaires à l'IRM et des IgG anti-toxoplasme positives. Il a une allergie documentée aux sulfamides.",
 "Quel traitement est le plus approprié ?",
 [("Pyriméthamine + clindamycine + acide folinique, sans attendre la PCR",""),
  ("Pyriméthamine + sulfadiazine","Contre-indiqué par l'allergie aux sulfamides."),
  ("Attendre la PCR avant tout traitement","Chez l'immunodéprimé avec lésions cérébrales, on traite l'encéphalite sans attendre la PCR."),
  ("Pyriméthamine seule","Elle s'associe toujours à un sulfamide ou à la clindamycine, avec folinate."),
  ("Cotrimoxazole","Non indiqué dans la toxoplasmose selon l'AIPS.")],
 "Encéphalite toxoplasmique de l'immunodéprimé : diagnostic de probabilité (image annulaire, IgG +, réponse au traitement) ; en cas d'allergie aux sulfamides, clindamycine + pyriméthamine pendant 8 à 10 semaines, avec folinate.",
 "Hémogramme deux fois par semaine chez l'immunosupprimé sous pyriméthamine.",
 B(7,13), niv="specialiste", spe="Infectiologie")

q("D","DX.8 · œil","assessment_diagnosis","ophtalmologie",
 "Une fillette de 10 ans, griffée par un chat il y a un mois, se plaint d'une baisse de vision unilatérale. Le fond d'œil montre un œdème papillaire et une étoile maculaire.",
 "Quel diagnostic est le plus probable ?",
 [("Neurorétinite à Bartonella henselae",""),
  ("Choriorétinite toxoplasmique","Lésion focale nécrosante, pas d'étoile maculaire avec œdème papillaire."),
  ("Hypertension intracrânienne idiopathique","Œdème papillaire bilatéral, sans étoile maculaire, sans contexte de griffure."),
  ("Rétinite à CMV","Terrain d'immunodépression."),
  ("Syndrome de Löfgren","Atteinte cutanée et articulaire, pas de neurorétinite.")],
 "Atteinte oculaire typique de la maladie des griffes du chat : neurorétinite avec œdème papillaire et étoile maculaire ; le syndrome oculoglandulaire de Parinaud en est une autre forme.",
 "Baisse de vision, souffle cardiaque ou immunodépression fébrile = avis spécialisé le jour même.",
 B(8,14), niv="specialiste", spe="Ophtalmologie")

q("D","DX.9 · méthotrexate","management","rhumatologie",
 "Une patiente de 55 ans traitée pour polyarthrite rhumatoïde par méthotrexate développe un nouveau ganglion axillaire de 2,5 cm, ferme, indolore.",
 "Quelle est la conduite la plus appropriée ?",
 [("Arrêter le méthotrexate, demander un avis spécialisé et biopsier le ganglion",""),
  ("Augmenter le méthotrexate : la polyarthrite est active","Un nouveau ganglion sous méthotrexate impose l'arrêt, un avis et une biopsie."),
  ("Passer le méthotrexate en prise quotidienne","Jamais quotidien : une seule prise par semaine ; le surdosage est grave."),
  ("Ajouter prednisone 30 mg/j","Masquerait un lymphome."),
  ("Surveillance de 3 mois","Ganglion nouveau, ferme, indolore sous immunosuppresseur : pas d'attente.")],
 "Sous méthotrexate, un nouveau ganglion impose l'arrêt du produit, un avis spécialisé et une biopsie.",
 "Méthotrexate : une fois par semaine ; contre-indiqué pendant la grossesse ; contraception ≥ 6 mois après l'arrêt chez la femme, ≥ 3 mois chez l'homme.",
 B(9,13), niv="specialiste", spe="Rhumatologie")

q("D","DX.10 · pharmacogénétique","mechanisms","neurologie",
 "Avant de prescrire la phénytoïne à un patient d'origine chinoise Han, le neurologue évoque un test génétique.",
 "Quel allèle augmente le risque de syndrome de Stevens-Johnson sous phénytoïne selon l'AIPS ?",
 [("HLA-B*1502",""),
  ("HLA-B*5801","Associé au syndrome d'hypersensibilité à l'allopurinol."),
  ("HLA-B27","Spondylarthropathies, sans lien avec la phénytoïne."),
  ("HLA-DR4","Polyarthrite rhumatoïde, sans lien avec la phénytoïne."),
  ("HLA-A*0201","Non cité dans le cours pour la phénytoïne.")],
 "L'AIPS de la phénytoïne cite HLA-B*1502 comme facteur de risque de SSJ chez les sujets chinois Han.",
 "Taux plasmatique thérapeutique de la phénytoïne : 10 à 20 µg/mL (AIPS).",
 B(10,14), niv="specialiste", spe="Neurologie")

q("D","DX.12 · rifampicine","management","pneumologie",
 "Une femme de 26 ans débute un traitement HRZE pour une tuberculose ganglionnaire. Elle prend une pilule œstroprogestative.",
 "Quel conseil est le plus approprié ?",
 [("Passer à une contraception non hormonale pendant le traitement par rifampicine",""),
  ("Garder la pilule, sans précaution","La rifampicine rend les contraceptifs hormonaux inefficaces."),
  ("Doubler la dose de pilule","Non recommandé ; la contraception doit être non hormonale."),
  ("Arrêter la rifampicine pour garder la pilule","On ne sacrifie pas le pilier du traitement."),
  ("Remplacer la rifampicine par l'éthambutol seul","L'éthambutol ne s'emploie jamais en monothérapie.")],
 "La rifampicine rend les contraceptifs hormonaux inefficaces : contraception non hormonale.",
 "Hépatotoxicité : arrêt envisagé si transaminases > 100 U/L avec bilirubine élevée ; sous isoniazide, arrêt au-delà de 3 fois la normale ; avis spécialisé.",
 B(12,14), niv="specialiste", spe="Pneumologie")

q("D","DX.13 · Fiebig","mechanisms","infectiologie",
 "Chez un patient exposé il y a 9 jours, l'ARN du VIH-1 est détectable, l'antigène p24 et les anticorps sont négatifs.",
 "À quel stade de Fiebig correspond ce profil ?",
 [("Stade I",""),
  ("Stade II","L'antigène p24 est apparu."),
  ("Stade III","Les anticorps de l'immunoessai sont apparus."),
  ("Stade V","Western blot positif sauf p31."),
  ("Stade VI","Western blot complet.")],
 "Fiebig I : seul l'ARN est détectable ; II : p24 ; III : anticorps à l'immunoessai ; IV : Western blot indéterminé ; V : positif sauf p31 ; VI : complet.",
 "ARN détectable avec anticorps négatifs = phase aiguë probable : confirmer par séroconversion ou 2e prélèvement ; une faible charge virale isolée peut être un faux positif.",
 B(13,8), niv="specialiste", spe="Infectiologie")

q("D","DX.14 · neurosyphilis","management","dermato-vénéréologie",
 "Un patient avec syphilis secondaire décrit une baisse d'audition et des céphalées ; la ponction lombaire confirme une neurosyphilis.",
 "Quel traitement est le plus approprié ?",
 [("Pénicilline G intraveineuse",""),
  ("Extencilline® 2,4 MUI IM dose unique","L'AIPS exclut la neurosyphilis : la benzathine n'atteint pas le LCR."),
  ("Extencilline® 2,4 MUI IM par semaine pendant 3 semaines","Schéma de la syphilis tardive, pas de la neurosyphilis."),
  ("Doxycycline 100 mg 2 fois par jour pendant 2 semaines","Alternative de la syphilis précoce chez l'allergique non enceinte."),
  ("Amoxicilline-clavulanate 10 jours","Aucun schéma de la syphilis dans le cours.")],
 "La neurosyphilis exige la pénicilline G intraveineuse, qui atteint le LCR ; d'où la recherche d'une atteinte neurologique, oculaire ou otique AVANT de traiter une syphilis secondaire.",
 "Femme enceinte : toujours la pénicilline ; la doxycycline est réservée à l'allergique non enceinte.",
 B(14,14), niv="specialiste", spe="Dermato-vénéréologie")

q("D","DX.15 · coronaires","management","cardiologie pédiatrique",
 "Chez un enfant de 6 ans avec Kawasaki, l'échocardiographie montre une artère coronaire avec Z-score à 11 (diamètre 8,5 mm).",
 "Quel traitement antithrombotique est le plus approprié ?",
 [("Aspirine associée à une anticoagulation (phenprocoumone INR 2,0–3,0 ou énoxaparine)",""),
  ("Aspirine à faible dose pendant 4 à 6 semaines seulement","Conduite de l'absence d'atteinte ou de la dilatation seule (Z < 2,5)."),
  ("Aspirine à faible dose au long cours seule","Conduite du petit anévrisme (Z 2,5 à < 5)."),
  ("Aspirine avec ou sans clopidogrel","Conduite de l'anévrisme moyen (Z 5 à < 10, < 8 mm)."),
  ("Aucun traitement si l'enfant est asymptomatique","L'anévrisme géant impose anticoagulation et suivi rapproché.")],
 "Anévrisme géant = Z-score ≥ 10 ou diamètre ≥ 8 mm (AHA 2017) : aspirine + anticoagulation, suivi rapproché.",
 "Après immunoglobulines : vaccins vivants reportés (AIPS 3 mois, jusqu'à 1 an pour la rougeole) ; aspirine + varicelle ou grippe = risque de syndrome de Reye.",
 B(15,8), niv="specialiste", spe="Cardiologie pédiatrique")

# ───────────── META (rendu)
_P = "../../../repo/LOT_Claude_Finaux/LOT_002/LOT_002_Phase_A_V0.html"
META = dict(
 code="G2", lot="LOT_002", version="2.0.0", seed=7, date="2026-11-01",
 titre="Tuméfaction, tumeur, y compris augmentation de volume des ganglions lymphatiques (adénopathie)",
 titre_court="Tuméfaction, tumeur, adénopathie", n_dx=15,
 note_version="v2 : gabarit Revision (EX/AP/SPE, 💡 fermé) — 1re production G2",
 note_media="Aucune image clinique dans les HTML LOT_002 (Phase A + DX.1–15) : media = null partout, bouton 🖼 absent.",
 intro_R="Décrire, classer, chercher le danger : quel geste maintenant, avant de nommer la cause ?",
 intro_D="Les 15 DX du LOT face à face : un signe, un examen qui tranche, une conduite. Les questions AP (bleu) et SPE (violet) sont mêlées aux EX : filtrez par niveau en haut.",
 intro_P="Corticoïde avant biopsie, blastes, amoxicilline et mononucléose, IGRA négatif, fenêtre VIH, Kawasaki incomplet.",
 verdict_label="Réflexe G2",
 footer="LOT_002 · G2 · Banque « Temps 1 » v2 · Faits issus exclusivement des leçons auditées LOT_002 (Phase A + Phase B DX.1–15) · Type A, une seule meilleure réponse (règles IML) · Aucun cliché dans les sources LOT_002 : aucune image affichée.",
 carte_html="""<div class="reflex"><b>Les 3 questions réflexes devant tout ganglion ou toute masse</b><ol>
<li><b>Danger maintenant ?</b> Dyspnée, stridor, œdème du visage → <b>compression médiastinale</b> ; enfant fébrile ≥ 5 j → <b>Kawasaki</b> ; blastes → hématologue aujourd'hui.</li>
<li><b>Quel ganglion ?</b> Siège · taille (&gt; 1 cm ; aine jusqu'à 1,5 cm) · consistance · mobilité · douleur · peau. <b>Localisé ou ≥ 2 régions ?</b></li>
<li><b>Quelle exposition, quel examen qui tranche ?</b> Porte d'entrée, chat, viande, rapports, voyage/contage, médicaments → une hypothèse = un examen.</li></ol></div>
<div class="map" style="margin-top:10px">
<div class="ax"><h3>📍 Siège</h3><ul>
<li><span class="red">Sus-claviculaire</span> → malin jusqu'à preuve du contraire (≈ 50 %) ; gauche = Virchow → abdomen</li>
<li>Cervical postérieur + angine + rate → mononucléose</li>
<li>Cervical antérieur sensible + angine sans toux → streptocoque (Centor)</li>
<li>Régional sur le trajet d'une griffure → griffes du chat</li>
<li>Épitrochléen &gt; 0,5 cm → syphilis, lymphome, main</li>
<li>≥ 2 régions → VIH, syphilis, EBV, CMV, ANA, hémogramme (RR cancer 6,41)</li></ul></div>
<div class="ax"><h3>✋ Caractères</h3><ul>
<li>Sensible, élastique, mobile, chaud → réaction (distension capsulaire)</li>
<li>Dur, fixe, indolore, conglomérat, rond sans hile → infiltration tumorale</li>
<li>Froid, fistulisé → tuberculose</li>
<li>Fluctuant → abcès (drainer) ; griffes du chat (aspirer, ne pas inciser)</li></ul></div>
<div class="ax"><h3>⏱ Temps</h3><ul>
<li>Tableau bénin localisé → revoir à 3–4 semaines</li>
<li>Persistance &gt; 4–6 semaines, croissance, durcissement → échographie puis <b>biopsie-exérèse</b></li>
<li>Fièvre ≥ 5 j chez l'enfant → Kawasaki ; traiter avant J10</li>
<li>2–8 semaines après un médicament → DRESS / pseudolymphome</li></ul></div>
<div class="ax"><h3>🧪 Ce qui tranche</h3><ul>
<li>Lymphome, métastase → <b>histologie du ganglion entier</b> (cytoponction ≈ 84 %)</li>
<li>Tuberculose → PCR + culture du ganglion (l'IGRA ne tranche pas)</li>
<li>VIH → test combiné 4e génération + ARN (fenêtre)</li>
<li>Syphilis → tréponémique + non tréponémique</li>
<li>Mononucléose → hétérophile (faux négatifs 1re semaine, &lt; 5 ans) / VCA-IgM, EBNA</li>
<li>Toxoplasmose, CMV → avidité des IgG</li></ul></div>
<div class="ax rf"><h3>🚩 Ordre d'exclusion</h3><ol>
<li>0 · <b>Compression médiastinale</b> — ABC, imagerie, hématologie</li><li>E1 Kawasaki (DX.15)</li>
<li>E2 Néoplasie : lymphome, leucémie, métastase (DX.2)</li><li>E3 Sus-claviculaire (DX.11)</li>
<li>E4 Tuberculose ganglionnaire (DX.12)</li><li>E5 Primo-infection VIH (DX.13)</li>
<li>E6 Syphilis secondaire (DX.14)</li><li>Puis : médicament, streptocoque, EBV/CMV, chat, granulome/auto-immun, réactionnel</li></ol>
<p class="red" style="margin:6px 0 0">Jamais de corticoïde avant d'avoir exclu un lymphome.</p></div>
</div>""",
 algo_html=f"""<table class="algo"><tr><th>Si…</th><th>Alors…</th></tr>
<tr class="e"><td>0 · Dyspnée, stridor, œdème du visage</td><td>Urgence : voies aériennes, imagerie, hématologie (compression médiastinale)</td></tr>
<tr class="e"><td>E1 · Enfant fébrile ≥ 5 jours, 4 critères sur 5</td><td>DX.15 : immunoglobulines 2 g/kg + aspirine, échocardiographie sans retarder</td></tr>
<tr class="e"><td>E2 · Dur, fixe, symptômes B, splénomégalie</td><td>DX.2 : hémogramme, LDH, biopsie-exérèse, pas de corticoïde</td></tr>
<tr class="e"><td>E3 · Creux sus-claviculaire</td><td>DX.11 : TDM, biopsie, sans observation</td></tr>
<tr class="e"><td>E4 · Fistule, contage, sueurs</td><td>DX.12 : PCR, culture, précautions de transmission</td></tr>
<tr class="e"><td>E5 · Exposition sexuelle, fièvre, éruption</td><td>DX.13 : test 4e génération + ARN</td></tr>
<tr class="e"><td>E6 · Éruption palmo-plantaire</td><td>DX.14 : sérologies, Extencilline® 2,4 MUI IM</td></tr>
<tr><td>Médicament récent, fièvre, éruption</td><td>DX.10 : arrêt (relais si antiépileptique)</td></tr>
<tr><td>Angine fébrile, Centor 3–4</td><td>DX.6 : TDR, antibiotique si positif (culture si TDR négatif chez l'enfant)</td></tr>
<tr><td>Angine, fatigue, rate, ganglions postérieurs</td><td>DX.4 ou DX.5 : hétérophile, sérologie ; jamais d'amoxicilline</td></tr>
<tr><td>Chat, papule, ganglion régional</td><td>DX.8 : clinique, sérologie si doute, surveillance</td></tr>
<tr><td>Granulome, arthralgies, hilaire bilatéral</td><td>DX.3, DX.9, DX.7 : histologie + microbiologie, ANA, ECA, sérologie</td></tr>
<tr><td>Plaie ou infection du territoire</td><td>DX.1 : traiter, revoir à 3–4 semaines ; au-delà de 4–6 semaines : biopsie</td></tr>
</table>
<p class="intro">Source : <a href="{_P}#algo">Phase A · Algorithme discriminant</a> et <a href="{_P}#ssp-p10">§10 Arbre décisionnel</a>.</p>""",
)
