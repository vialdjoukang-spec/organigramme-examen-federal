#!/usr/bin/env python3
"""Construit recensement.json à partir des tableaux texte (outil ponctuel, hors dépôt)."""
import json, glob, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = "/home/user/organigramme-examen-federal"
SORTIE = os.path.join(DEPOT, "Claude/_progression/recensement/recensement.json")

REGIONS = [
    ("TC", "Tête et cou", "#e11d48"), ("RA", "Rachis", "#7c3aed"), ("TH", "Thorax", "#0284c7"),
    ("AB", "Abdomen", "#ea580c"), ("PE", "Pelvis", "#c026d3"), ("MS", "Membres supérieurs", "#0d9488"),
    ("MI", "Membres inférieurs", "#16a34a"), ("TR", "Transversal et systémique", "#475569"),
]
LETTRES = [
    ("V", "V", "Vasculaire", "#dc2626"), ("I", "I", "Infectieux", "#16a34a"), ("T", "T", "Tumoral", "#7c3aed"),
    ("D", "D", "Dégénératif", "#a16207"), ("I2", "I", "Iatrogène", "#db2777"), ("Tr", "T", "Traumatique", "#ea580c"),
    ("C", "C", "Congénital", "#0891b2"), ("A", "A", "Auto-immun et inflammatoire", "#4f46e5"),
    ("F", "F", "Fonctionnel et métabolique", "#0d9488"),
]
TECH_IMG = [
    ("RX", "Radiographie", "Rayons X", "#2563eb"), ("TDM", "TDM", "Rayons X", "#7c3aed"),
    ("IRM", "IRM", "Résonance magnétique", "#db2777"), ("US", "Échographie et Doppler", "Ultrasons", "#059669"),
    ("MN", "Médecine nucléaire", "Rayonnements gamma et positons", "#ea580c"),
    ("INT", "Interventionnel", "Guidage par l'image", "#dc2626"),
]
TECH_EXP = [
    ("ELEC", "Électrophysiologie et tracés", "#0891b2"), ("EFF", "Effort, hémodynamique, vasculaire", "#dc2626"),
    ("ECHO", "Ultrasons fonctionnels", "#059669"), ("VENT", "Ventilation et gaz du sang", "#2563eb"),
    ("SOM", "Sommeil et vigilance", "#4f46e5"), ("SENS", "Sensoriel et optique", "#ca8a04"),
    ("PRES", "Pressions, débits, transit", "#c026d3"), ("DYN", "Tests dynamiques et métaboliques", "#ea580c"),
]

def lire(nom, ncol):
    lignes = []
    for i, l in enumerate(open(os.path.join(ICI, nom), encoding="utf-8")):
        l = l.rstrip("\n")
        if not l.strip():
            continue
        p = l.split("|")
        if len(p) != ncol:
            sys.exit(f"{nom}:{i+1}: {len(p)} colonnes au lieu de {ncol}: {l[:80]}")
        lignes.append(p)
    return lignes

def techs(s, codes):
    out = []
    for bloc in s.split(";"):
        code, _, det = bloc.partition(":")
        code = code.strip()
        if code not in codes:
            sys.exit(f"technologie inconnue {code!r} dans {s!r}")
        out.append({"tech": code, "detail": det.strip()})
    return out

codes_img = {t[0] for t in TECH_IMG}
codes_exp = {t[0] for t in TECH_EXP}
lettres = {l[0] for l in LETTRES}
regions = {r[0] for r in REGIONS}

imagerie = []
for n, (reg, sy, le, niv, dx, te, si) in enumerate(lire("imagerie.txt", 7), 1):
    assert reg in regions and le in lettres and niv in "MC", (reg, le, niv, dx)
    imagerie.append({"id": f"IMG-{n:03d}", "region": reg, "systeme": sy, "lettre": le, "niveau": niv,
                     "diagnostic": dx, "techniques": techs(te, codes_img), "signe": si})

explorations = []
for n, (reg, sy, fo, le, niv, dx, te, an) in enumerate(lire("explorations.txt", 8), 1):
    assert reg in regions and le in lettres and niv in "MC", (reg, le, niv, dx)
    explorations.append({"id": f"EXP-{n:03d}", "region": reg, "systeme": sy, "fonction": fo, "lettre": le,
                         "niveau": niv, "diagnostic": dx, "explorations": techs(te, codes_exp), "anomalie": an})

# Fiches transversales de technique (imagerie) : tech, niveau, titre, phrase, existant
FT_IMG = [
 ("RX","M","Physique des rayons X et les cinq densités radiologiques","Les rayons X s'atténuent selon l'épaisseur et le numéro atomique des tissus, si bien que l'air apparaît noir, la graisse gris foncé, l'eau gris clair, le calcium blanc et le métal blanc éclatant.",""),
 ("RX","M","Lecture systématique de la radiographie du thorax","On vérifie d'abord la qualité du cliché, puis on lit les contours grâce au signe de la silhouette, qui localise une opacité en effaçant le bord qu'elle touche.","Radiographie du thorax"),
 ("RX","M","Lecture de la radiographie osseuse et choix des incidences","On demande toujours deux incidences orthogonales et l'on analyse l'alignement, l'os, le cartilage et les parties molles, parce qu'un seul cliché masque les déplacements.","Radiographie standard et âge osseux"),
 ("RX","C","Abdomen sans préparation : indications résiduelles","L'abdomen sans préparation ne garde que quelques indications (corps étranger, suivi de calcul radio-opaque), car la TDM l'a remplacé dans l'urgence.",""),
 ("RX","M","Mammographie : incidences et classification BI-RADS","La mammographie compare deux incidences par sein, et la classification BI-RADS traduit le degré de suspicion en conduite à tenir.","Mammographie"),
 ("RX","M","Radioprotection : justification, optimisation, dose efficace et grossesse","On justifie chaque examen irradiant et l'on optimise sa dose selon l'ORaP, tandis que l'OFSP publie des niveaux de référence diagnostiques.",""),
 ("RX","M","Absorptiométrie biphotonique (DXA)","La DXA mesure la densité minérale osseuse au rachis et à la hanche, puis elle l'exprime en T-score par rapport à l'adulte jeune.","Ostéodensitométrie"),
 ("TDM","M","Unités Hounsfield et fenêtrage","L'eau vaut 0 UH, la graisse une valeur négative et l'os plusieurs centaines d'UH, puis le fenêtrage choisit la plage de densités que l'œil distingue.",""),
 ("TDM","M","Phases d'injection et indications","On choisit la phase selon la question posée : sans injection pour le sang et le calcium, artérielle pour l'hypervascularisation, portale pour le bilan courant, excrétoire pour les voies urinaires.","Radiographie et TDM du système nerveux central"),
 ("TDM","M","Produits de contraste iodés : allergie, fonction rénale, metformine, thyroïde","On évalue le DFG, les antécédents de réaction et la fonction thyroïdienne avant l'injection, puis on suit les recommandations de l'ESUR pour la prévention.",""),
 ("TDM","C","TDM double énergie, faible dose et score calcique","La double énergie distingue l'iode, l'acide urique et le calcium, tandis que les protocoles faible dose réduisent l'irradiation du dépistage.",""),
 ("TDM","C","Angio-TDM : principes et artéfacts","Le bolus de contraste opacifie les vaisseaux au moment choisi, mais le mouvement et le métal créent des artéfacts qu'il faut reconnaître.","Angio-TDM thoracique"),
 ("IRM","M","Physique de l'IRM et pondérations T1 et T2","Le T1 rend la graisse brillante et l'eau sombre, alors que le T2 rend l'eau brillante, ce qui permet de reconnaître la pondération d'une image.","IRM encéphalique et médullaire"),
 ("IRM","M","FLAIR et STIR : supprimer le liquide ou la graisse","Le FLAIR annule le signal du liquide cérébro-spinal pour révéler les lésions périventriculaires, tandis que le STIR annule la graisse pour montrer l'œdème osseux.",""),
 ("IRM","M","Diffusion et coefficient apparent de diffusion","La diffusion devient hyperintense lorsque les molécules d'eau ne bougent plus, et un ADC bas confirme la vraie restriction (ischémie, abcès, tumeur cellulaire).",""),
 ("IRM","M","T2* et SWI : sang, calcium et fer","Ces séquences amplifient les artéfacts de susceptibilité magnétique, si bien que les microsaignements apparaissent comme des points noirs.",""),
 ("IRM","M","Gadolinium : rehaussement, fibrose systémique néphrogénique, grossesse","On préfère un chélate macrocyclique à la dose minimale, surtout si le DFG est bas, et l'on évite le gadolinium pendant la grossesse sauf nécessité.",""),
 ("IRM","M","Angio-IRM (TOF, avec gadolinium) et veino-IRM","Le TOF montre le sang qui circule sans injection, alors que l'angio-IRM injectée couvre de longs segments vasculaires.",""),
 ("IRM","M","Sécurité IRM : implants, stimulateurs, corps étrangers","On vérifie la compatibilité de chaque dispositif avant l'examen, parce que le champ magnétique peut déplacer, chauffer ou dérégler un implant.",""),
 ("IRM","C","Perfusion, spectroscopie et IRM fonctionnelle","La perfusion mesure le volume sanguin tumoral, et la spectroscopie dose des métabolites comme la choline ou le lactate.",""),
 ("IRM","C","IRM cardiaque : ciné, rehaussement tardif, cartographies","Le ciné mesure la fonction, puis le rehaussement tardif localise la fibrose et oriente vers la cause d'une cardiomyopathie.","IRM cardiaque"),
 ("US","M","Physique des ultrasons, échogénicité et artéfacts","Le liquide apparaît anéchogène avec un renforcement postérieur, tandis que le calcul crée un cône d'ombre, ce qui aide à caractériser une lésion.","Échographie abdominale"),
 ("US","M","Doppler couleur, pulsé et énergie","Le Doppler pulsé mesure des vitesses, le couleur montre le sens du flux et l'énergie détecte des flux lents, mais un mauvais angle fausse les vitesses.","Doppler porte"),
 ("US","C","Élastographie","L'élastographie mesure la rigidité d'un tissu, ce qui estime la fibrose hépatique sans biopsie.",""),
 ("US","C","Échographie de contraste","Les microbulles restent dans les vaisseaux, si bien que l'on peut caractériser une lésion hépatique ou rénale sans irradier ni léser le rein.",""),
 ("US","M","Échographie au lit du patient (POCUS, eFAST)","Le clinicien répond à une question binaire au lit du patient, par exemple la présence d'un épanchement ou d'un pneumothorax.","Imagerie des urgences : FAST, polytraumatisé"),
 ("US","C","Échographie obstétricale et fœtale","On date la grossesse, puis on dépiste les malformations et l'on surveille la croissance par les biométries et le Doppler.","Échographie pelvienne et fœtale"),
 ("MN","M","Principes de la scintigraphie et du SPECT","Un traceur radioactif se fixe selon une fonction, puis la gamma-caméra en cartographie la répartition.","Scintigraphie osseuse"),
 ("MN","M","TEP-FDG : principe et pièges physiologiques","Le FDG suit la consommation de glucose, si bien que le cerveau, le cœur, la vessie et l'inflammation fixent aussi le traceur et peuvent tromper.","TEP-TDM"),
 ("MN","C","Traceurs spécifiques (PSMA, DOTATATE, amyloïde, ioflupane)","Chaque traceur cible une molécule propre à une maladie, ce qui augmente la spécificité au prix d'une moindre disponibilité.","Médecine nucléaire cérébrale"),
 ("MN","C","Radioprotection en médecine nucléaire et allaitement","On interrompt parfois l'allaitement selon le traceur, et l'on limite le contact rapproché après une forte activité administrée.",""),
 ("INT","M","Principes de l'imagerie interventionnelle : hémostase, anticoagulants, consentement","On vérifie la coagulation et l'on gère les anticoagulants avant tout geste, puis on informe le patient des risques et des alternatives.","Neuroradiologie interventionnelle"),
 ("INT","M","Biopsies et ponctions guidées","Le guidage échographique ou scanographique conduit l'aiguille jusqu'à la cible en évitant les vaisseaux et les organes creux.","Ponction et biopsie guidées"),
 ("INT","C","Embolisation et drainage percutané","L'embolisation occlut l'artère qui saigne, tandis que le drainage percutané évacue une collection sans chirurgie.",""),
 ("US","M","Classification EU-TIRADS du nodule thyroïdien","On classe le nodule selon ses caractères échographiques, puis la catégorie et la taille fixent le seuil de cytoponction.","Échographie thyroïdienne"),
 ("TDM","C","Recommandations de Fleischner pour le nodule pulmonaire","La taille, la nature solide ou en verre dépoli et le risque du patient fixent l'intervalle de contrôle (non vérifié CH).","TDM thoracique haute résolution"),
 ("IRM","C","Scores LI-RADS, PI-RADS, O-RADS et Bosniak","Ces scores traduisent une probabilité de malignité en catégorie standardisée, ce qui harmonise le compte rendu et la conduite à tenir.","IRM rénale et prostatique"),
 ("RX","M","Bon usage de l'imagerie : choisir l'examen juste","On choisit l'examen qui répond à la question clinique avec la moindre irradiation, et l'on évite les examens qui ne changeront pas la prise en charge.","Imagerie oncologique"),
]

FT_EXP = [
 ("ELEC","M","ECG à 12 dérivations : lecture systématique","On lit dans l'ordre rythme, fréquence, axe, P, PR, QRS, ST, T et QTc, ce qui évite d'oublier une anomalie.","ECG"),
 ("ELEC","M","Holter ECG et enregistreurs d'événements","L'enregistrement prolongé corrèle les symptômes au rythme, et l'on choisit sa durée selon la fréquence des symptômes.","Holter ECG"),
 ("ELEC","M","EEG de l'adulte, de l'enfant et du nouveau-né","L'EEG enregistre l'activité corticale de surface, et les épreuves d'activation (hyperpnée, stimulation lumineuse, privation de sommeil) augmentent son rendement.","EEG de l'adulte, de l'enfant et du nouveau-né"),
 ("ELEC","C","EEG en psychiatrie","L'EEG distingue un delirium ou un état de mal non convulsif d'un trouble psychiatrique primaire.","EEG en psychiatrie : delirium, catatonie, avant électroconvulsivothérapie"),
 ("ELEC","M","Électroneuromyogramme","Les vitesses de conduction distinguent l'atteinte démyélinisante de l'atteinte axonale, tandis que l'EMG de détection recherche la dénervation.","Électroneuromyogramme"),
 ("ELEC","M","Potentiels évoqués (visuels, auditifs, somesthésiques, moteurs)","On mesure la latence d'une réponse provoquée, et un allongement révèle un ralentissement de conduction.","Potentiels évoqués"),
 ("ELEC","M","Cardiotocographie","On analyse le rythme de base, la variabilité, les accélérations et les décélérations, puis on classe le tracé selon FIGO.","Cardiotocographie"),
 ("ELEC","C","ECG sous psychotropes : QT","On mesure le QTc avant et pendant un traitement qui l'allonge, et l'on corrige les facteurs favorisants.","ECG sous psychotropes : QT"),
 ("EFF","M","Épreuve d'effort","On augmente la charge jusqu'aux symptômes ou à la fréquence cible, puis on interprète le segment ST, la pression artérielle et la capacité d'effort.","Épreuve d'effort"),
 ("EFF","C","Ergospirométrie","On mesure les échanges gazeux pendant l'effort, ce qui distingue une limitation cardiaque, respiratoire ou musculaire.",""),
 ("EFF","M","Mesure ambulatoire de la pression artérielle","On enregistre la pression sur 24 heures, ce qui démasque l'effet blouse blanche et l'hypertension masquée.","Mesure ambulatoire de la pression artérielle"),
 ("EFF","M","Index de pression systolique et explorations vasculaires","On divise la pression à la cheville par la pression humérale, et le rapport dépiste l'artériopathie.","Index de pression systolique et explorations vasculaires"),
 ("EFF","M","Test de marche de 6 minutes","Le patient marche le plus loin possible pendant six minutes, et l'on note la distance et la saturation.","Test de marche de 6 minutes"),
 ("EFF","C","Tilt-test et massage sinocarotidien","On redresse le patient sur une table basculante, ce qui reproduit une syncope réflexe ou une hypotension orthostatique.",""),
 ("EFF","C","Capillaroscopie","On examine les capillaires du repli unguéal au microscope, ce qui distingue un Raynaud primaire d'une connectivite.","Capillaroscopie"),
 ("EFF","C","Cathétérisme cardiaque droit","On mesure directement les pressions pulmonaires et le débit cardiaque, ce qui affirme et classe une hypertension pulmonaire.",""),
 ("EFF","C","Explorations motrices, posturales et gériatriques","Des tests chronométrés et la posturographie quantifient la marche et l'équilibre, ce qui prédit les chutes.","Explorations motrices et posturales"),
 ("ECHO","M","Échocardiographie transthoracique et transœsophagienne","L'échocardiographie mesure la fraction d'éjection, les pressions de remplissage et les gradients valvulaires, puis l'ETO précise les structures postérieures.","Échocardiographie transthoracique et transœsophagienne"),
 ("ECHO","C","Échocardiographie de stress","On recherche une anomalie de cinétique segmentaire provoquée par l'effort ou la dobutamine, ce qui signe l'ischémie.",""),
 ("ECHO","C","Élastographie hépatique impulsionnelle","La vitesse d'une onde de cisaillement augmente avec la rigidité hépatique, ce qui estime la fibrose.",""),
 ("VENT","M","Spirométrie et test de réversibilité","On mesure le VEMS et la CVF avant et après bronchodilatateur, puis on interprète selon les valeurs GLI et la limite inférieure de la normale.","Spirométrie et test de réversibilité"),
 ("VENT","M","Pléthysmographie","Le pléthysmographe mesure la CPT et le VR, ce que la spirométrie ne peut pas faire.","Pléthysmographie"),
 ("VENT","M","DLCO","On mesure le transfert du monoxyde de carbone, puis on le corrige pour l'hémoglobine.","DLCO"),
 ("VENT","M","Gazométrie artérielle","On ponctionne l'artère radiale après test d'Allen, puis on interprète pH, PaCO2, bicarbonates et PaO2 dans cet ordre.",""),
 ("VENT","C","Test de provocation bronchique","On inhale des doses croissantes de métacholine, et une chute du VEMS de 20 % affirme l'hyperréactivité.","Test de provocation bronchique"),
 ("VENT","C","FeNO","On mesure le monoxyde d'azote expiré, qui reflète l'inflammation bronchique éosinophilique.",""),
 ("VENT","C","Pressions respiratoires maximales et SNIP","On mesure la force des muscles inspiratoires et expiratoires, ce qui dépiste une atteinte neuromusculaire.","Pressions respiratoires"),
 ("VENT","C","Rhinomanométrie","On mesure le débit et la pression nasale, ce qui objective une obstruction.",""),
 ("SOM","M","Polysomnographie","On enregistre EEG, ventilation, oxymétrie et tonus musculaire pendant la nuit, ce qui classe les stades du sommeil et ses événements.","Polysomnographie"),
 ("SOM","M","Polygraphie ventilatoire nocturne","On enregistre la ventilation et l'oxymétrie sans EEG, ce qui suffit souvent à affirmer un syndrome d'apnées.","Polygraphie ventilatoire nocturne"),
 ("SOM","C","Tests itératifs de latence d'endormissement","On propose cinq siestes, puis on mesure la latence d'endormissement et les endormissements en sommeil paradoxal.","Test itératif de latence d'endormissement"),
 ("SOM","C","Test de maintien de l'éveil","Le patient doit rester éveillé dans l'obscurité, ce qui évalue son aptitude à conduire.","Test de maintien de l'éveil"),
 ("SOM","C","Actimétrie","Un capteur au poignet enregistre l'activité sur plusieurs semaines, ce qui estime le rythme veille-sommeil.","Actimétrie"),
 ("SOM","C","Agenda du sommeil","Le patient note chaque jour ses heures de coucher, de réveil et ses éveils, ce qui objective son rythme.","Agenda du sommeil"),
 ("SOM","C","Oxymétrie nocturne","L'oxymètre enregistre la saturation toute la nuit, ce qui dépiste désaturations et apnées.","Oxymétrie nocturne"),
 ("SENS","M","Audiométrie tonale et vocale","On compare les seuils en conduction aérienne et osseuse, ce qui distingue surdité de transmission et surdité de perception.","Audiométrie"),
 ("SENS","C","Tympanométrie et réflexes stapédiens","On mesure la compliance du tympan, ce qui révèle un épanchement de l'oreille moyenne.",""),
 ("SENS","C","Otoémissions acoustiques et PEA","Les otoémissions testent les cellules ciliées externes, tandis que les PEA testent la voie auditive jusqu'au tronc cérébral.",""),
 ("SENS","M","Vidéonystagmographie et vHIT","On enregistre les mouvements oculaires, puis on teste chaque canal semi-circulaire, ce qui localise un déficit vestibulaire.","Vidéonystagmographie"),
 ("SENS","M","Champ visuel automatisé","On présente des stimuli lumineux d'intensité croissante, puis la topographie du déficit localise la lésion sur la voie visuelle.","Champ visuel automatisé"),
 ("SENS","C","Pachymétrie et tonométrie","On mesure l'épaisseur cornéenne, qui corrige l'interprétation de la pression intraoculaire.","Pachymétrie cornéenne"),
 ("SENS","C","Tomographie par cohérence optique","L'OCT mesure les couches de la rétine et des fibres optiques, ce qui suit le glaucome et les maladies maculaires.",""),
 ("SENS","C","Dermatoscopie","La loupe éclairée révèle les structures pigmentaires sous la surface, ce qui améliore le diagnostic du mélanome.","Dermatoscopie"),
 ("PRES","M","Manométrie œsophagienne haute résolution","Des capteurs rapprochés mesurent les pressions à chaque déglutition, puis la classification de Chicago classe les troubles moteurs.","Manométrie œsophagienne et anorectale"),
 ("PRES","C","Manométrie anorectale","On mesure les pressions sphinctériennes et le réflexe recto-anal inhibiteur, ce qui explore incontinence et constipation terminale.","Manométrie œsophagienne et anorectale"),
 ("PRES","M","pH-impédancemétrie de 24 heures","Une sonde détecte les reflux acides et non acides, puis on corrèle les symptômes aux épisodes.","pH-impédancemétrie"),
 ("PRES","C","Temps de transit colique","Le patient avale des marqueurs radio-opaques, puis une radiographie les compte quelques jours plus tard.","Temps de transit colique"),
 ("PRES","M","Débitmétrie et résidu post-mictionnel","On mesure le débit urinaire et le volume résiduel, ce qui dépiste une obstruction ou une vessie hypoactive.","Débitmétrie"),
 ("PRES","M","Cystomanométrie et bilan urodynamique","On remplit la vessie en mesurant ses pressions, ce qui révèle hyperactivité, compliance basse ou obstruction.","Cystomanométrie"),
 ("PRES","C","Explorations pelvi-périnéales","On combine manométrie, échographie endoanale et défécographie, ce qui explore les troubles du plancher pelvien.","Explorations pelvi-périnéales"),
 ("PRES","C","Vidéofluoroscopie et FEES de la déglutition","On observe le passage d'un bol radio-opaque ou l'on filme le larynx à l'endoscope, ce qui révèle les fausses routes.",""),
 ("DYN","M","Tests respiratoires (Helicobacter pylori, lactose, pullulation)","On mesure un gaz expiré après une charge en substrat, ce qui révèle une infection ou une malabsorption.","Tests respiratoires (H. pylori, lactose)"),
 ("DYN","M","Épreuves endocriniennes dynamiques (stimulation et freinage)","On stimule un axe déficitaire et l'on freine un axe hyperactif, parce qu'un dosage isolé ne suffit pas.","Épreuves dynamiques : Synacthène, HGPO, freinage"),
 ("DYN","C","Épreuves fonctionnelles rénales dynamiques","On teste la concentration, l'acidification ou la fonction séparée des reins, ce qui localise un trouble tubulaire.","Épreuves fonctionnelles rénales dynamiques"),
 ("DYN","C","Calorimétrie indirecte","On mesure la consommation d'oxygène et la production de CO2, puis on calcule la dépense énergétique de repos.","Calorimétrie indirecte"),
 ("DYN","C","Impédancemétrie corporelle","Un faible courant traverse le corps, ce qui estime l'eau totale, la masse maigre et l'angle de phase.","Impédancemétrie"),
 ("DYN","M","Tests allergologiques (prick-tests, tests épicutanés, provocation)","On expose la peau ou l'organisme à l'allergène suspect, puis on interprète la réaction à la lumière de l'histoire clinique.",""),
 ("DYN","C","Test de restriction hydrique et de la desmopressine","On prive le patient d'eau sous surveillance, puis on injecte de la desmopressine, ce qui classe la polyurie.",""),
]

def fiches(lst, prefixe):
    return [{"id": f"{prefixe}-{i:02d}", "tech": t, "niveau": n, "titre": ti, "phrase": ph, "existant": ex}
            for i, (t, n, ti, ph, ex) in enumerate(lst, 1)]

# Titres existants (titres seulement)
existants = {"imagerie": [], "explorations": []}
for f in sorted(glob.glob(os.path.join(DEPOT, "Claude/_progression/donnees/examens/*.json"))):
    d = json.load(open(f, encoding="utf-8"))
    if d.get("sous_onglet") == 2:
        existants["imagerie"].append({"titre": d["titre"], "systeme_site": d.get("systeme")})
    elif d.get("sous_onglet") == 3:
        existants["explorations"].append({"titre": d["titre"], "systeme_site": d.get("systeme")})

ALL = "*"
CORR_IMG = {
 "Échographie transfontanellaire": ["TC|Encéphale"],
 "IRM encéphalique et médullaire": ["TC|Encéphale", "RA|Moelle et racines"],
 "Médecine nucléaire cérébrale": ["TC|Encéphale"],
 "Neuroradiologie interventionnelle": ["TC|Vaisseaux cervico-encéphaliques", "TC|Encéphale"],
 "Radiographie et TDM du système nerveux central": ["TC|Encéphale"],
 "Échographie ganglionnaire": ["TC|Cou : thyroïde, salivaires, ganglions"],
 "IRM médullaire": ["RA|Moelle et racines", "RA|Rachis osseux et disco-ligamentaire"],
 "TDM d'extension": ["TR|Oncologie"],
 "TEP-TDM": ["TR|Oncologie", "TR|Maladies systémiques et inflammatoires"],
 "Imagerie des troubles neurocognitifs (renvoi S1)": ["TC|Encéphale"],
 "IRM cérébrale du premier épisode psychotique": ["TC|Encéphale"],
 "Cytoponctions guidées": ["TC|Cou : thyroïde, salivaires, ganglions"],
 "Échographie et IRM cervico-faciales": ["TC|Cou : thyroïde, salivaires, ganglions", "TC|Pharynx, larynx, cavité orale"],
 "Radiographie et TDM des sinus, rochers et massif facial": ["TC|ORL : sinus, rocher, face"],
 "Coroscanner": ["TH|Cœur et péricarde"],
 "Écho-Doppler des troncs supra-aortiques, des membres et des fistules": ["TC|Vaisseaux cervico-encéphaliques", "MS|Vaisseaux du membre supérieur", "MI|Vaisseaux du membre inférieur"],
 "IRM cardiaque": ["TH|Cœur et péricarde"],
 "Radiographie et TDM thorax-cœur": ["TH|Cœur et péricarde", "TH|Poumon"],
 "Scintigraphie myocardique": ["TH|Cœur et péricarde"],
 "Angio-TDM thoracique": ["TH|Aorte et vaisseaux thoraciques", "TH|Poumon"],
 "Échographie pleurale": ["TH|Plèvre"],
 "Ponction et biopsie guidées": ["TH|Poumon", "TH|Plèvre"],
 "Radiographie du thorax": ["TH|Poumon", "TH|Plèvre", "TH|Médiastin"],
 "Scintigraphie de ventilation-perfusion": ["TH|Poumon"],
 "TDM thoracique haute résolution": ["TH|Poumon"],
 "Bili-IRM": ["AB|Voies biliaires et vésicule", "AB|Pancréas"],
 "Biopsie guidée du foie et du pancréas": ["AB|Foie", "AB|Pancréas"],
 "Doppler porte": ["AB|Foie"],
 "Échographie abdominale": ["AB|Foie", "AB|Voies biliaires et vésicule", "AB|Rate", "AB|Péritoine, paroi, rétropéritoine", "AB|Aorte et vaisseaux abdominaux"],
 "TDM abdomino-pelvienne": ["AB|Tube digestif", "AB|Péritoine, paroi, rétropéritoine", "AB|Foie", "AB|Pancréas", "AB|Rate"],
 "Biopsie guidée du rein et de la prostate": ["AB|Reins, uretères, surrénales", "PE|Prostate et scrotum"],
 "Échographie rénale et vésicale": ["AB|Reins, uretères, surrénales", "PE|Vessie et urètre"],
 "IRM rénale et prostatique": ["AB|Reins, uretères, surrénales", "PE|Prostate et scrotum"],
 "Scintigraphie rénale": ["AB|Reins, uretères, surrénales"],
 "Uro-TDM": ["AB|Reins, uretères, surrénales", "PE|Vessie et urètre"],
 "Biopsie guidée du sein": ["TH|Sein et paroi thoracique"],
 "Échographie pelvienne et fœtale": ["PE|Utérus et annexes", "PE|Obstétrique"],
 "IRM mammaire et pelvienne": ["TH|Sein et paroi thoracique", "PE|Utérus et annexes", "PE|Rectum et périnée"],
 "Mammographie": ["TH|Sein et paroi thoracique"],
 "Échographie thyroïdienne": ["TC|Cou : thyroïde, salivaires, ganglions"],
 "IRM hypophysaire": ["TC|Selle turcique"],
 "Ostéodensitométrie": ["TR|Squelette systémique et métabolique"],
 "Scintigraphies thyroïdienne, parathyroïdienne et MIBG": ["TC|Cou : thyroïde, salivaires, ganglions", "AB|Reins, uretères, surrénales"],
 "TDM des surrénales": ["AB|Reins, uretères, surrénales"],
 "Biopsie osseuse guidée": ["TR|Oncologie", "RA|Rachis osseux et disco-ligamentaire"],
 "Échographie ostéo-articulaire": ["MS|*", "MI|Hanche et bassin osseux", "MI|Genou", "MI|Cheville et pied"],
 "IRM du rachis et des membres": ["RA|Rachis osseux et disco-ligamentaire", "MS|*", "MI|*"],
 "Radiographie standard et âge osseux": ["RA|Rachis osseux et disco-ligamentaire", "MS|*", "MI|*", "TR|Squelette systémique et métabolique"],
 "Scintigraphie osseuse": ["TR|Oncologie", "TR|Squelette systémique et métabolique"],
 "TDM ostéo-articulaire": ["RA|Rachis osseux et disco-ligamentaire", "MS|*", "MI|*"],
 "Imagerie oncologique": ["TR|Oncologie"],
 "Imagerie pédiatrique": ["TR|Pédiatrie"],
 "Imagerie des urgences : FAST, polytraumatisé": ["TR|Urgences et polytraumatisé"],
}
CORR_EXP = {
 "EEG de l'adulte, de l'enfant et du nouveau-né": ["TC|Système nerveux central"],
 "Électroneuromyogramme": ["RA|Nerf périphérique et muscle", "MS|Nerfs et fonction de la main", "MI|Marche, posture et force"],
 "Potentiels évoqués": ["TC|Système nerveux central", "RA|Moelle et voies longues"],
 "Capillaroscopie": ["MS|Microcirculation et vaisseaux du membre supérieur"],
 "Actimétrie": ["TR|Sommeil et vigilance"], "Agenda du sommeil": ["TR|Sommeil et vigilance"],
 "ECG sous psychotropes : QT": ["TR|Psychiatrie et neurosciences", "TH|Cœur : rythme et conduction"],
 "EEG en psychiatrie : delirium, catatonie, avant électroconvulsivothérapie": ["TR|Psychiatrie et neurosciences"],
 "Polygraphie ventilatoire nocturne": ["TR|Sommeil et vigilance"], "Polysomnographie": ["TR|Sommeil et vigilance"],
 "Test itératif de latence d'endormissement": ["TR|Sommeil et vigilance"], "Test de maintien de l'éveil": ["TR|Sommeil et vigilance"],
 "Dermatoscopie": ["TR|Peau"],
 "Audiométrie": ["TC|Oreille et équilibre"], "Champ visuel automatisé": ["TC|Œil et vision"],
 "Pachymétrie cornéenne": ["TC|Œil et vision"], "Vidéonystagmographie": ["TC|Oreille et équilibre"],
 "ECG": ["TH|Cœur : rythme et conduction", "TH|Cœur : ischémie et pompe"],
 "Échocardiographie transthoracique et transœsophagienne": ["TH|Cœur : ischémie et pompe"],
 "Épreuve d'effort": ["TH|Cœur : ischémie et pompe"], "Holter ECG": ["TH|Cœur : rythme et conduction"],
 "Index de pression systolique et explorations vasculaires": ["MI|Artères et veines du membre inférieur"],
 "Mesure ambulatoire de la pression artérielle": ["TH|Cœur : ischémie et pompe"],
 "DLCO": ["TH|Respiration : échanges gazeux"], "Oxymétrie nocturne": ["TR|Sommeil et vigilance"],
 "Pléthysmographie": ["TH|Respiration : ventilation"], "Pressions respiratoires": ["TH|Respiration : muscles et contrôle"],
 "Spirométrie et test de réversibilité": ["TH|Respiration : ventilation"],
 "Test de marche de 6 minutes": ["TH|Respiration : échanges gazeux"], "Test de provocation bronchique": ["TH|Respiration : ventilation"],
 "Manométrie œsophagienne et anorectale": ["AB|Œsophage et estomac", "PE|Anorectum et plancher pelvien"],
 "pH-impédancemétrie": ["AB|Œsophage et estomac"], "Temps de transit colique": ["AB|Intestin et côlon"],
 "Tests respiratoires (H. pylori, lactose)": ["AB|Œsophage et estomac", "AB|Intestin et côlon"],
 "Cystomanométrie": ["PE|Vessie et miction"], "Débitmétrie": ["PE|Vessie et miction"],
 "Épreuves fonctionnelles rénales dynamiques": ["AB|Rein et équilibre hydro-électrolytique"],
 "Cardiotocographie": ["PE|Grossesse et fœtus"], "Explorations pelvi-périnéales": ["PE|Anorectum et plancher pelvien", "PE|Vessie et miction"],
 "Calorimétrie indirecte": ["TR|Métabolisme et composition corporelle"],
 "Épreuves dynamiques : Synacthène, HGPO, freinage": ["TR|Endocrinologie dynamique", "PE|Grossesse et fœtus"],
 "Impédancemétrie": ["TR|Métabolisme et composition corporelle"],
 "Explorations motrices et posturales": ["MI|Marche, posture et force"],
}
for cle, corr in (("imagerie", CORR_IMG), ("explorations", CORR_EXP)):
    for e in existants[cle]:
        if e["titre"] not in corr:
            sys.exit(f"titre existant sans correspondance : {e['titre']}")
        e["couvre"] = corr[e["titre"]]

SIGLES = {
 "ADC": "coefficient apparent de diffusion", "AIT": "accident ischémique transitoire", "AMH": "hormone anti-müllérienne",
 "AO": "Arbeitsgemeinschaft für Osteosynthesefragen (classification des fractures)", "ASSM": "Académie suisse des sciences médicales",
 "ATS": "American Thoracic Society", "AVC": "accident vasculaire cérébral", "AASM": "American Academy of Sleep Medicine",
 "BAV": "bloc auriculo-ventriculaire", "BI-RADS": "Breast Imaging Reporting and Data System",
 "BPCO": "bronchopneumopathie chronique obstructive", "CC BY-NC-SA": "Creative Commons, attribution, pas d'utilisation commerciale, partage dans les mêmes conditions",
 "CH": "Suisse (Confoederatio Helvetica)", "CHC": "carcinome hépatocellulaire", "CIA": "communication interauriculaire",
 "CIV": "communication interventriculaire", "CISS": "constructive interference in steady state (séquence IRM T2 très fine)",
 "CKD-EPI": "Chronic Kidney Disease Epidemiology Collaboration (formule d'estimation du DFG)", "COVID-19": "maladie à coronavirus 2019",
 "CPRE": "cholangio-pancréatographie rétrograde endoscopique", "CPT": "capacité pulmonaire totale", "CV": "capacité vitale",
 "CVF": "capacité vitale forcée", "CO2": "dioxyde de carbone", "DEP": "débit expiratoire de pointe",
 "DESH": "disproportionately enlarged subarachnoid-space hydrocephalus", "DFG": "débit de filtration glomérulaire",
 "DISH": "hyperostose squelettique diffuse idiopathique", "DLCO": "capacité de diffusion du monoxyde de carbone",
 "DMSA": "acide dimercaptosuccinique (traceur cortical rénal)", "DOTATATE": "analogue de la somatostatine marqué (traceur TEP)",
 "DP": "densité de protons", "DXA": "absorptiométrie biphotonique à rayons X", "EBUS": "échoendoscopie bronchique",
 "ECG": "électrocardiogramme", "EEG": "électroencéphalogramme", "EMG": "électromyogramme", "ENMG": "électroneuromyogramme",
 "EPI": "echo-planar imaging", "ERS": "European Respiratory Society", "ESC": "Société européenne de cardiologie",
 "ESE": "Société européenne d'endocrinologie", "ESUR": "Société européenne de radiologie urogénitale", "ETO": "échocardiographie transœsophagienne",
 "EU-TIRADS": "European Thyroid Imaging Reporting and Data System", "EWGSOP2": "European Working Group on Sarcopenia in Older People, 2e version",
 "FAST": "focused assessment with sonography for trauma", "eFAST": "FAST étendu au thorax", "FDG": "fluorodésoxyglucose (marqué au fluor 18)",
 "FEES": "évaluation endoscopique de la déglutition par fibroscopie", "FeNO": "fraction expirée de monoxyde d'azote",
 "FEVG": "fraction d'éjection du ventricule gauche", "FIGO": "Fédération internationale de gynécologie et d'obstétrique",
 "FLAIR": "fluid-attenuated inversion recovery (T2 sans signal du liquide)", "FRAX": "outil d'évaluation du risque fracturaire à dix ans",
 "GH": "hormone de croissance", "GINA": "Global Initiative for Asthma", "GIST": "tumeur stromale gastro-intestinale",
 "GLI": "Global Lung Function Initiative (valeurs de référence)", "GnRH": "gonadolibérine", "GOLD": "Global Initiative for Chronic Obstructive Lung Disease",
 "HbA1c": "hémoglobine glyquée", "hCG": "hormone chorionique gonadotrope", "HGPO": "hyperglycémie provoquée par voie orale",
 "HINTS": "head impulse, nystagmus, test of skew", "HNF": "hyperplasie nodulaire focale", "HTA": "hypertension artérielle",
 "IAH": "index d'apnées-hypopnées", "IADPSG": "International Association of Diabetes and Pregnancy Study Groups",
 "IDH": "isocitrate déshydrogénase", "IGF-1": "facteur de croissance analogue à l'insuline de type 1", "IgE": "immunoglobulines E",
 "IgG4": "immunoglobulines G de sous-classe 4", "IOTA": "International Ovarian Tumor Analysis", "IPP": "inhibiteurs de la pompe à protons",
 "IPS": "index de pression systolique", "IRM": "imagerie par résonance magnétique", "LH": "hormone lutéinisante",
 "LI-RADS": "Liver Imaging Reporting and Data System", "MAG3": "mercaptoacétyltriglycine (traceur rénal)", "MAPA": "mesure ambulatoire de la pression artérielle",
 "MAV": "malformation artério-veineuse", "MELD": "Model for End-stage Liver Disease", "MIBG": "méta-iodobenzylguanidine",
 "MOGAD": "maladie associée aux anticorps anti-MOG", "NASCET": "North American Symptomatic Carotid Endarterectomy Trial (méthode de mesure)",
 "NEXUS": "National Emergency X-Radiography Utilization Study (règle de décision)", "NMO": "neuromyélite optique",
 "O-RADS": "Ovarian-Adnexal Reporting and Data System", "OCT": "tomographie par cohérence optique", "OFSP": "Office fédéral de la santé publique",
 "OMS": "Organisation mondiale de la santé", "ORaP": "ordonnance sur la radioprotection", "ORL": "oto-rhino-laryngologie",
 "PaCO2": "pression artérielle partielle en dioxyde de carbone", "PaO2": "pression artérielle partielle en oxygène",
 "PC20": "concentration provoquant une chute de 20 % du VEMS", "PEA": "potentiels évoqués auditifs", "PECARN": "Pediatric Emergency Care Applied Research Network",
 "PEM": "potentiels évoqués moteurs", "PES": "potentiels évoqués somesthésiques", "PEV": "potentiels évoqués visuels",
 "PI-RADS": "Prostate Imaging Reporting and Data System", "PIC": "pneumopathie interstitielle commune", "PImax": "pression inspiratoire maximale",
 "PINS": "pneumopathie interstitielle non spécifique", "PISA": "proximal isovelocity surface area", "POCUS": "échographie au point de soins",
 "PR": "intervalle PR de l'ECG", "PRES": "syndrome d'encéphalopathie postérieure réversible", "PROFILES": "Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland",
 "PSMA": "antigène membranaire spécifique de la prostate", "PTH": "parathormone", "QRS": "complexe de dépolarisation ventriculaire",
 "QTc": "intervalle QT corrigé", "RECIST": "Response Evaluation Criteria in Solid Tumors", "RUSH": "rapid ultrasound in shock",
 "SA": "semaines d'aménorrhée", "SCLO": "Swiss Catalogue of Learning Objectives", "SDRA": "syndrome de détresse respiratoire aiguë",
 "SEP": "sclérose en plaques", "SIADH": "sécrétion inappropriée d'hormone antidiurétique", "SNIP": "pression inspiratoire nasale au reniflement",
 "SPECT": "tomographie d'émission monophotonique", "ST": "segment ST de l'ECG", "STIR": "short tau inversion recovery (suppression de la graisse)",
 "SVGO": "Association suisse contre l'ostéoporose", "SWI": "imagerie de susceptibilité magnétique", "T1": "pondération en temps de relaxation longitudinale",
 "T2": "pondération en temps de relaxation transversale", "TcPO2": "pression transcutanée en oxygène", "TDM": "tomodensitométrie (scanner)",
 "TEP": "tomographie par émission de positons", "TIPMP": "tumeur intracanalaire papillaire et mucineuse du pancréas",
 "TIPS": "shunt porto-systémique intrahépatique transjugulaire", "TNM": "tumeur, ganglions, métastases (classification)",
 "TOF": "time of flight (angio-IRM sans injection)", "UH": "unités Hounsfield", "VEMS": "volume expiratoire maximal en une seconde",
 "VFA": "évaluation des fractures vertébrales par DXA", "vHIT": "test vidéo d'impulsion céphalique", "VI-RADS": "Vesical Imaging Reporting and Data System",
 "VNG": "vidéonystagmographie", "VO2": "consommation d'oxygène", "VR": "volume résiduel", "HTA masquée": "hypertension présente hors du cabinet seulement",
 "aVR": "dérivation unipolaire du bras droit", "ESUR 2018": "lignes directrices de l'ESUR sur les produits de contraste, version 10",
 "Radiopaedia": "encyclopédie collaborative de radiologie", "LITFL": "Life in the Fast Lane (bibliothèque ECG en ligne)",
 "MedPix": "base d'images de la National Library of Medicine", "PhysioNet": "banque de signaux physiologiques",
 "NLM": "National Library of Medicine (États-Unis)", "ACR": "American College of Radiology", "SSR": "Société suisse de radiologie",
}
SIGLES.pop("HTA masquée"); SIGLES.pop("ESUR 2018"); SIGLES.pop("Radiopaedia"); SIGLES.pop("MedPix"); SIGLES.pop("PhysioNet")

SOURCES = [
 {"nom": "PROFILES (catalogue suisse des objectifs d'apprentissage, SCLO)", "role": "Le cadre fédéral définit les situations cliniques et les activités attendues ; ce recensement s'y aligne sans en recopier de liste officielle d'imagerie.", "statut": "Cadre de référence, non recopié ici"},
 {"nom": "ORaP 2017 et niveaux de référence diagnostiques de l'OFSP", "role": "Ces textes fixent la justification et l'optimisation des examens irradiants en Suisse.", "statut": "Source suisse, version à dater"},
 {"nom": "Lignes directrices de l'ESUR sur les produits de contraste (version 10, 2018)", "role": "Elles encadrent la prévention des réactions et du risque rénal.", "statut": "Source européenne"},
 {"nom": "Recommandations ESC (insuffisance cardiaque 2021, endocardite 2023, hypertension pulmonaire ESC/ERS 2022)", "role": "Elles fournissent les seuils cardiologiques cités.", "statut": "Source européenne"},
 {"nom": "Standards ERS/ATS de spirométrie (2019) et d'interprétation (2022), valeurs GLI", "role": "Ils fixent la technique et la limite inférieure de la normale.", "statut": "Source européenne et internationale"},
 {"nom": "EU-TIRADS (European Thyroid Association, 2017)", "role": "Il classe le nodule thyroïdien.", "statut": "Source européenne"},
 {"nom": "ESE 2023 sur l'incidentalome surrénalien", "role": "Il fixe le seuil de 10 UH et le suivi.", "statut": "Source européenne"},
 {"nom": "BI-RADS, LI-RADS, PI-RADS, O-RADS (ACR), Bosniak 2019, Fleischner", "role": "Ces classifications structurent les comptes rendus.", "statut": "Sources internationales (non vérifié CH)"},
 {"nom": "AASM (sommeil), GINA, GOLD, FIGO 2015, IADPSG", "role": "Ces organismes fournissent des seuils diagnostiques largement repris.", "statut": "Sources internationales (non vérifié CH)"},
 {"nom": "Directives de l'ASSM sur le diagnostic de la mort", "role": "Elles encadrent le diagnostic de mort cérébrale en Suisse.", "statut": "Source suisse, version à dater"},
]
IMAGES = [
 {"nom": "Radiopaedia", "licence": "CC BY-NC-SA 3.0 annoncée pour la plupart des cas", "statut": "À vérifier cas par cas ; l'usage non commercial convient à un site d'étude gratuit."},
 {"nom": "Wikimedia Commons", "licence": "Licence propre à chaque fichier (domaine public, CC BY, CC BY-SA…)", "statut": "À vérifier fichier par fichier, avec attribution exacte."},
 {"nom": "MedPix et Open-i (NLM)", "licence": "Conditions propres à chaque image", "statut": "À vérifier."},
 {"nom": "LITFL (bibliothèque ECG)", "licence": "Licence Creative Commons annoncée", "statut": "À vérifier ; utile pour les tracés ECG."},
 {"nom": "PhysioNet", "licence": "Licences ouvertes variables selon la base", "statut": "À vérifier ; utile pour EEG, ECG et polysomnographie."},
]

data = {
 "meta": {"titre": "Recensement topo-systémique : imagerie et explorations fonctionnelles", "date": "13.11.2026",
          "niveau": "Examen fédéral suisse de médecine humaine (PROFILES/SCLO)",
          "existant": {"imagerie": len(existants["imagerie"]), "explorations": len(existants["explorations"])},
          "images": {"min_par_fiche_diag": 1, "min_par_fiche_tech": 1, "cible_par_technique": 1, "cible_normale_par_fiche_tech": 2}},
 "regions": [{"code": c, "nom": n, "couleur": col} for c, n, col in REGIONS],
 "lettres": [{"code": c, "lettre": l, "nom": n, "couleur": col} for c, l, n, col in LETTRES],
 "technologies_imagerie": [{"code": c, "nom": n, "physique": p, "couleur": col} for c, n, p, col in TECH_IMG],
 "technologies_explorations": [{"code": c, "nom": n, "couleur": col} for c, n, col in TECH_EXP],
 "imagerie": imagerie, "explorations": explorations,
 "fiches_technique_imagerie": fiches(FT_IMG, "FTI"), "fiches_technique_explorations": fiches(FT_EXP, "FTE"),
 "existants": existants, "sigles": SIGLES, "sources": SOURCES, "sources_images": IMAGES,
}
for f in data["fiches_technique_imagerie"]:
    if f["existant"] and f["existant"] not in CORR_IMG: sys.exit("existant inconnu " + f["existant"])
for f in data["fiches_technique_explorations"]:
    if f["existant"] and f["existant"] not in CORR_EXP: sys.exit("existant inconnu " + f["existant"])
json.dump(data, open(SORTIE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("imagerie", len(imagerie), "explorations", len(explorations), "FTI", len(FT_IMG), "FTE", len(FT_EXP))
print("existants", {k: len(v) for k, v in existants.items()})
