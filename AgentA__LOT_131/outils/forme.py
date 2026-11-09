#!/usr/bin/env python3
"""Forme V0 imposée par l'auditeur : îlots, justification, une fenêtre details par notion.
Aucun renvoi à Gemma."""
from __future__ import annotations
import re

# terme -> (preuve, mécanisme, exemple chiffré déjà aligné sur l'extrait, piège)
FEN = {
    "DX.1": {
        "phimosis physiologique": ("P03", "L'anneau étroit laisse sortir le prépuce interne, l'effet est une rétraction encore possible, et le signe est l'aspect en bourrelet sans cicatrice.", "L'extrait P01 retient 4 % de prépuces rétractables à la naissance, puis 50 % à un an et 89 % à trois ans.", "On ne confond pas cet aspect avec un anneau fibreux blanc."),
        "phimosis pathologique": ("P03", "La cicatrice fixe l'anneau, l'effet est l'impossibilité de laisser sortir le prépuce interne, et le signe est l'anneau blanc et épaissi.", "Le corticoïde topique de l'EAU est dosé à 0,05-0,1 % pendant 4 à 8 semaines, avec un succès supérieur à 80 %.", "On ne rétracte pas de force, sous peine de créer la cicatrice que l'on voulait éviter."),
        "paraphimosis": ("P07", "L'anneau rétracté étrangle le sillon, l'effet est l'œdème du gland, et le signe est l'impossibilité de rabattre le prépuce.", "L'EAU qualifie cette situation d'urgence exigeant un traitement immédiat.", "On ne renvoie pas l'enfant au lendemain."),
        "circoncision": ("P06", "Le prépuce est réséqué, l'effet est la perte du tissu de couverture, et le signe manquant est le capuchon qui aurait servi à reconstruire.", "La contre-indication vise l'hypospadias, le pénis enfoui, la mégaprépuce, l'épispadias et la courbure congénitale.", "On ne circoncit pas avant d'avoir écarté ces anomalies."),
    },
    "DX.2": {
        "varicocèle": ("P10", "Le reflux veineux dilate le plexus pampiniforme, l'effet est la chaleur locale, et le signe est le paquet veineux qui gonfle debout.", "L'extrait retient 14 à 20 % des adolescents, avec une incidence semblable à l'âge adulte.", "On ne traite pas toute varicocèle asymptomatique sans hypotrophie."),
        "hypotrophie": ("P12", "La chaleur et le reflux réduisent le volume, l'effet est l'asymétrie, et le signe est le testicule plus petit.", "Le seuil retenu est supérieur à 2 mL ou à 20 % par rapport à l'autre testicule.", "On ne conclut pas sur une seule mesure chez l'adolescent en croissance."),
        "échographie rénale": ("P11", "Une tumeur rétropéritonéale peut bloquer la veine rénale, l'effet est une varicocèle droite, et le signe est l'apparition prépubère ou strictement droite.", "L'EAU demande l'échographie rénale dans ces deux situations.", "On n'attribue pas une varicocèle droite isolée à une banalité gauche."),
    },
    "DX.3": {
        "cryptorchidie": ("P13", "La descente s'arrête sur son trajet, l'effet est un scrotum vide, et le signe est le testicule palpé ou non au-dessus du scrotum.", "L'incidence va de 1,0 à 4,6 % des nouveau-nés à terme, et elle reste proche de 1,0 % à un an.", "On ne rassure pas après six mois en attendant une descente devenue improbable."),
        "orchidopexie": ("P15", "On fixe le testicule dans le scrotum, l'effet est la position basse, et le signe de réussite est le testicule qui y reste.", "La chirurgie se fait dans l'année qui suit six mois d'âge corrigé, au plus tard à dix-huit mois.", "On ne prescrit pas l'hCG comme un réflexe, car il peut nuire à la spermatogenèse."),
        "testicule non palpable": ("P14", "Le testicule est intra-abdominal, inguinal ou absent, l'effet est l'impossibilité de le palper, et le signe associé d'alerte est l'hypospadias.", "Environ 80 % des testicules non descendus restent palpables.", "Devant une forme bilatérale avec variation du développement sexuel, on n'attend pas pour l'avis endocrinien."),
    },
    "DX.4": {
        "hypospadias": ("P19", "Le méat s'ouvre sur la face ventrale, l'effet est un jet dévié, et le signe est le capuchon préputial dorsal.", "La prévalence européenne est de 18,6 pour 10 000 naissances, entre 5,1 et 36,8.", "On ne circoncit pas : le prépuce sert à la reconstruction."),
        "méat": ("P20", "L'orifice urétral est ectopique, l'effet est la direction du jet, et le signe se décrit par sa position, sa forme et sa largeur.", "Le variant à méat large et prépuce intact ne se voit qu'après rétraction.", "On ne classe pas l'hypospadias sans décrire la courbure en érection."),
    },
    "DX.5": {
        "mutilation génitale féminine": ("P23", "Un geste sans raison médicale retire ou lèse le tissu génital externe, l'effet est la perte de fonction, et le signe est l'absence ou la fermeture des structures.", "L'OMS retient plus de 230 millions de filles et de femmes concernées, et l'OFSP estime près de 24 600 femmes et filles touchées ou à risque en Suisse.", "On ne parle pas d'un bénéfice sanitaire : la source dit qu'il n'y en a aucun."),
        "article 124": ("P27", "La loi interdit le geste, l'effet est la peine, et le signe médico-légal est la lésion documentée avec l'accord de la personne.", "La peine va de six mois à dix ans, y compris si le geste a été commis à l'étranger et que l'auteur est en Suisse.", "On ne délègue pas l'entretien à un enfant de la famille."),
        "infibulation": ("P24", "Les lèvres sont repositionnées en fermeture, l'effet est le rétrécissement de l'orifice, et le signe est le type 3.", "L'OMS décrit quatre types, le type 3 étant cette fermeture.", "On n'ouvre pas la cicatrice sans consentement ni hors d'une indication obstétricale ou urinaire."),
    },
    "DX.6": {
        "torsion du testicule": ("P28", "Le cordon tourne, l'effet est l'ischémie gonadique, et le signe est la douleur brutale avec vomissements.", "Une atrophie sévère a été vue après quatre heures lorsque le tour dépassait 360 degrés.", "On n'attend pas l'échographie pour explorer."),
        "réflexe crémastérien": ("P29", "L'arc réflexe remonte le testicule, l'effet de son abolition oriente vers la torsion, et le signe se cherche par un attouchement de la cuisse.", "La source donne une sensibilité de 100 % et une spécificité de 66 %.", "Un réflexe présent ne doit pas, à lui seul, faire renoncer à l'exploration si le récit est typique."),
        "échographie Doppler": ("P30", "Le Doppler cherche le flux, l'effet d'un flux présent peut rassurer à tort, et le signe du tourbillon voit le cordon tordu.", "Dans une série de 208 garçons, 24 % avaient encore un flux normal ou augmenté.", "Un flux artériel persistant n'exclut pas la torsion."),
    },
    "DX.7": {
        "hyperplasie congénitale des surrénales": ("P34", "Le déficit enzymatique accumule les précurseurs, l'effet est la virilisation et le risque de perte de sel, et le signe néonatal est l'aspect génital atypique.", "La ligne suisse se lit AGS 16 259 1:10 200.", "On ne laisse pas sortir un nouveau-né atypique sans ionogramme ni avis spécialisé."),
        "17-hydroxyprogestérone": ("P34", "Le dépistage dose ce précurseur sur papier buvard, l'effet est le repérage des formes classiques, et le signe biologique est la valeur au-dessus du seuil du programme.", "L'incidence imprimée sur la ligne du syndrome adréno-génital est 1:10 200.", "On ne rassure pas sur un seul dosage si l'enfant vomit ou perd du poids."),
    },
    "DX.8": {
        "carcinome épidermoïde": ("P45", "L'épithélium se transforme, l'effet est une tumeur invasive, et le signe est une lésion indurée, ulcérée ou végétante.", "Ce carcinome représente plus de 95 % des tumeurs malignes du pénis.", "On ne traite pas des mois par corticoïde sans biopsie."),
        "biopsie": ("P46", "Le prélèvement montre l'invasion, l'effet est le stade, et le signe histologique guide l'exérèse.", "Un punch de 2 à 3 mm suffit souvent, alors qu'une biopsie d'environ 1 mm empêchait de juger la profondeur dans 91 % des cas.", "On ne se contente pas d'un fragment trop superficiel."),
    },
    "DX.9": {
        "priapisme ischémique": ("P37", "La stase dans les corps caverneux produit l'hypoxie, puis l'hypercapnie et l'acidose, et le signe est la rigidité douloureuse qui ne cède pas.", "L'extrait place le seuil au-delà de 4 heures, à la manière d'un syndrome des loges.", "On ne traite pas cette forme comme une érection banale."),
        "hypoxie": ("P36", "Le sang ne sort plus du corps caverneux, l'effet est le manque d'oxygène, et le signe métabolique accompagne la douleur.", "La forme ischémique représente plus de 95 % des épisodes.", "On ne se fie pas à un gland encore souple pour exclure l'ischémie des corps caverneux."),
        "syndrome des loges": ("P37", "L'espace clos des corps caverneux se comporte comme une loge, l'effet est l'ischémie, et le signe est la rigidité qui dure.", "Au-delà de 4 heures, l'intervention urgente vise à limiter la nécrose du muscle lisse.", "On n'attend pas 48 à 72 heures : ce délai soulage peu la fonction érectile."),
        "syndrome de compartiment": ("P37", "L'espace clos des corps caverneux se comporte comme une loge, l'effet est l'ischémie, et le signe est la rigidité qui dure.", "Au-delà de 4 heures, l'intervention urgente vise à limiter la nécrose du muscle lisse.", "On n'attend pas 48 à 72 heures : ce délai soulage peu la fonction érectile."),
        "dysfonction érectile": ("P38", "La nécrose du muscle lisse laisse une fibrose, l'effet est la perte de rigidité utile, et le signe tardif est l'impuissance.", "Les gestes après 48 à 72 heures soulagent la douleur mais préviennent peu cette séquelle.", "On ne promet pas la récupération après un délai long."),
    },
    "DX.10": {
        "gangrène de Fournier": ("P39", "L'infection polymicrobienne diffuse dans les fascias, l'effet est la nécrose, et le signe est la douleur périnéale avec sepsis.", "Des registres ont rapporté des mortalités de 10 %, de 7,5 % et de 5 %.", "On ne se rassure pas sur une peau encore peu marquée."),
        "débridement": ("P41", "On excise le tissu mort, l'effet est le contrôle du sepsis, et le signe de suffisance est l'absence de résidu nécrotique.", "Le geste doit commencer en moins de 24 heures et être répété.", "Un seul passage opératoire incomplet augmente la mortalité."),
        "nécrose": ("P40", "Les germes thrombosent les vaisseaux de la fascia, l'effet est la mort tissulaire profonde, et le signe cutané est en retard sur la lésion.", "La nécrose interne dépasse en général les signes externes.", "On n'attend pas la crépitation pour appeler le chirurgien."),
    },
}

DIVERGENCE = {
    "DX.1": "L'EAU décrit un corticoïde topique à 0,05-0,1 % pendant 4 à 8 semaines, tandis que la posologie d'une spécialité autorisée en Suisse reste à lire dans l'information professionnelle AIPS. On ne transforme pas le schéma européen en dose Swissmedic.",
    "DX.3": "L'EAU mentionne un schéma de GnRH à 1,2 mg par jour, tandis qu'aucune notice AIPS n'a été relue dans ce lot. La posologie suisse reste : À vérifier (AIPS).",
    "DX.9": "L'EAU fixe l'urgence au-delà de 4 heures, mais elle ne tient pas lieu de posologie suisse pour un médicament injectable. Toute dose reste : À vérifier (AIPS).",
    "DX.10": "L'EAU nomme les classes d'antibiotiques à commencer d'emblée, sans que ce texte soit une posologie Swissmedic. La dose de chaque spécialité reste : À vérifier (AIPS).",
}

URGENCE = {
    "DX.1": "D'abord, on reconnaît le gland étranglé par l'anneau. Ensuite, on comprime l'œdème et l'on rabaisse le prépuce. Enfin, si la réduction échoue, on incise l'anneau sans renvoyer au lendemain.",
    "DX.6": "D'abord, on croit le récit de douleur brutale. Ensuite, on appelle le chirurgien sans attendre le Doppler. Enfin, on explore dans les 24 heures, car un flux encore présent n'exclut pas la torsion.",
    "DX.7": "D'abord, on ne rassure pas devant un aspect génital atypique. Ensuite, on dose et l'on surveille le sel et le sucre. Enfin, on obtient l'avis endocrinien avant toute assignation.",
    "DX.9": "D'abord, on note l'heure de début. Ensuite, dès 4 heures d'ischémie, on agit comme pour un syndrome des loges. Enfin, on ne promet pas la fonction érectile si le délai dépasse 48 à 72 heures.",
    "DX.10": "D'abord, on croit la douleur disproportionnée. Ensuite, on commence l'antibiotique et le débridement sans attendre que la peau noircisse. Enfin, on répète l'excision dans les 24 heures.",
    "Phase_A": "D'abord, on écarte la torsion, le priapisme ischémique, la gangrène de Fournier et la perte de sel du nouveau-né. Ensuite seulement, on classe la variation stable.",
}

def fenetre(terme: str, pid: str, mecanisme: str, exemple: str, piege: str, source: str) -> str:
    return (
        f"<details style='display:inline;'><summary>{terme}</summary>"
        f"<span class='w'>Mécanisme. {mecanisme} Exemple chiffré. {exemple} "
        f"Piège d'examen. {piege} Source {source}.</span></details>"
    )

def inserer_apres_phrase(html: str, terme: str, bloc: str) -> str:
    """Place la fenêtre après la première phrase complète qui contient le terme, hors point 13."""
    if f"<summary>{terme}</summary>" in html:
        return html
    morceaux = re.split(r'(<h3\b[^>]*>)', html)
    out, zone, interdit = [], "", False
    for i, part in enumerate(morceaux):
        if part.startswith("<h3"):
            if zone and not interdit and terme.lower() in re.sub(r"<[^>]+>", " ", zone).lower() and f"<summary>{terme}</summary>" not in "".join(out):
                zone = _poser(zone, terme, bloc)
            if zone:
                out.append(zone)
            zone = part
            interdit = bool(re.search(r'id="[^"]*-p13"', part))
        else:
            zone += part
    if zone:
        if not interdit and terme.lower() in re.sub(r"<[^>]+>", " ", zone).lower():
            zone = _poser(zone, terme, bloc)
        out.append(zone)
    return "".join(out)

def _poser(zone: str, terme: str, bloc: str) -> str:
    # Après le premier point qui suit le terme, dans un div.p qui n'est pas une fenêtre.
    bas = zone.lower()
    k = bas.find(terme.lower())
    if k < 0:
        return zone + bloc
    fin = zone.find(".", k)
    if fin < 0:
        return zone + bloc
    return zone[:fin + 1] + " " + bloc + " " + zone[fin + 1:]

def oter_fenetres_point_13(html: str) -> str:
    morceaux = re.split(r'(<h3\b[^>]*>)', html)
    out, zone, interdit = [], "", False
    for part in morceaux:
        if part.startswith("<h3"):
            if zone:
                out.append(_nettoyer_13(zone) if interdit else zone)
            zone = part
            interdit = bool(re.search(r'id="[^"]*-p13"', part))
        else:
            zone += part
    if zone:
        out.append(_nettoyer_13(zone) if interdit else zone)
    return "".join(out)

def _nettoyer_13(zone: str) -> str:
    zone = re.sub(r"(?is)<details\b[^>]*>.*?</details>", "", zone)
    zone = re.sub(r"(?is)<div[^>]*\bpopover\b[^>]*>.*?</div>", "", zone)
    return zone

def ilots(html: str) -> str:
    # Enveloppe chaque h3 et son contenu jusqu'au h3 suivant.
    parts = re.split(r'(?=<h3\b)', html)
    out = []
    for part in parts:
        if part.startswith("<h3"):
            # ferme l'îlot avant la prochaine balise de structure majeure déjà gérée par split
            m = re.search(r'(</section>|$)', part)
            corps = part[:m.start()] if m else part
            reste = part[m.start():] if m else ""
            if 'class="ilot"' not in corps[:80]:
                corps = '<section class="ilot" lang="fr">' + corps
                if "</section>" not in corps:
                    corps += "</section>"
            out.append(corps + reste)
        else:
            out.append(part)
    return "".join(out)

def appliquer(html: str, entite: str) -> str:
    html = re.sub(r"text-align:\s*justify", "text-align:justify", html)
    if "text-align:justify" not in html:
        html = html.replace("body{", "body{text-align:justify;hyphens:auto;", 1)
    if ".ilot{" not in html:
        html = html.replace("</style>",
            ".ilot{border:1px solid #d5ddd6;border-radius:.8rem;padding:1rem 1.15rem 1.2rem;margin:1rem 0 1.35rem;background:#fbfcfb}"
            ".p,.w,details,.ilot{text-align:justify;hyphens:auto;-webkit-hyphens:auto}"
            "details>span.w{display:block;margin:.4rem 0 .2rem;padding:.45rem .6rem;background:#f4f7f4;border-radius:.4rem}"
            "</style>", 1)
    for terme, (pid, mec, ex, piege) in FEN.get(entite, {}).items():
        bloc = fenetre(terme, pid, mec, ex, piege, "[S1]")
        html = inserer_apres_phrase(html, terme, bloc)
    if entite in URGENCE and "Urgence — conduite chronologique" not in html:
        bloc = fenetre("Urgence — conduite chronologique", "", URGENCE[entite],
                       "Les délais cités sont ceux des extraits du dossier, sans arrondi.",
                       "On ne commence pas par l'examen qui retarde le geste.", "[S1]")
        # placer dans le point 11 si possible
        html = html.replace('id="' + ("ssp" if entite == "Phase_A" else "dx" + entite.split(".")[1]) + '-p11"',
                            'id="' + ("ssp" if entite == "Phase_A" else "dx" + entite.split(".")[1]) + '-p11" data-urg="1"', 1)
        html = inserer_apres_phrase(html, "Urgence — conduite chronologique", bloc) if False else _poser_urgence(html, bloc)
    if entite in DIVERGENCE and "Divergence des sources" not in html:
        bloc = fenetre("Divergence des sources", "", DIVERGENCE[entite],
                       "Aucun milligramme suisse n'est ajouté ici.",
                       "On ne présente pas le texte européen comme une autorisation Swissmedic.", "[S1]")
        html = _poser_urgence(html, bloc)
    for terme, (pid, mec, ex, piege) in FEN.get(entite, {}).items():
        if f"<summary>{terme}</summary>" not in html:
            html = _poser_urgence(html, fenetre(terme, pid, mec, ex, piege, "[S1]"))
    html = oter_fenetres_point_13(html)
    html = ilots(html)
    return html

def _poser_urgence(html: str, bloc: str) -> str:
    m = re.search(r'id="[^"]*-p11"', html)
    if not m:
        return html + bloc
    fin = html.find("</div>", m.end())
    if fin < 0:
        return html + bloc
    return html[:fin + 6] + bloc + html[fin + 6:]

def compter(html: str) -> dict:
    return {
        "details": len(re.findall(r"<details\b", html, re.I)),
        "ilot": len(re.findall(r'class="ilot"', html)),
        "justifie": "text-align:justify" in html and "hyphens:auto" in html,
        "p13_details": _p13_a_details(html),
        "urgence": "Urgence — conduite chronologique" in html,
    }

def _p13_a_details(html: str) -> bool:
    m = re.search(r'(?is)<h3[^>]*id="[^"]*-p13".*?(?=<h3\b|</section>\s*<h3|$)', html)
    # plus simple : zone jusqu'au prochain h3
    m = re.search(r'(?is)<h3[^>]*id="[^"]*-p13"[^>]*>.*?(?=<h3\b)', html)
    if not m:
        m = re.search(r'(?is)<h3[^>]*id="[^"]*-p13"[^>]*>.*$', html)
    if not m:
        return False
    return "<details" in m.group(0).lower()
