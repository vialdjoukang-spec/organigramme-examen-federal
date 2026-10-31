#!/usr/bin/env python3
"""Construit un DX de LOT_151. Usage : fabrique_dx.py 1"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur import P, btn, ecrire, fen, page
from assembler import TITRES, SOURCES_HTML, glossaire, F

DX = {
1: dict(nom="Effet d'un antagoniste de la vitamine K",
        pattern="le temps de Quick baisse et le rapport international normalisé sert au suivi, tandis que le facteur V reste haut",
        clinique="un patient qui prend de la phenprocoumone ou de l'acénocoumarol, avec ou sans saignement",
        conduite="Konakion MM, numéro 48112013, selon la phrase qui correspond au coumarinique et à la gravité, et Beriplex, numéro 00665, selon son tableau d'INR",
        piege="appliquer au foie la dose urgente de la phenprocoumone"),
2: dict(nom="Carence en vitamine K",
        pattern="les facteurs II, VII et X baissent, avec un facteur V et un fibrinogène normaux",
        clinique="un jeûne, une malabsorption, une antibiothérapie ou un ictère d'obstacle, sans antagoniste en cours",
        conduite="la vitamine K de Konakion MM, numéro 48112013, et non le schéma de 60 UI par kilogramme réservé à la phenprocoumone urgente",
        piege="appeler foie un facteur V qui est en réalité normal"),
3: dict(nom="Effet de l'héparine non fractionnée",
        pattern="le temps de céphaline et souvent le temps de thrombine s'allongent, alors que le temps de Quick bouge peu aux concentrations thérapeutiques",
        clinique="une perfusion ou une injection récente d'héparine, parfois un prélèvement contaminé",
        conduite="la protamine, numéro 69842, à la dose lue de 10 mg pour environ 1400 UI d'héparine, en l'ajustant au temps écoulé",
        piege="suivre le traitement au seul temps de céphaline alors que la revue renvoie à l'anti-Xa"),
4: dict(nom="Effet d'un anticoagulant oral direct",
        pattern="le temps dépend de la molécule et de l'heure, et la revue du 28 mai 2024 place ces médicaments dans l'allongement du temps de céphaline",
        clinique="dabigatran, apixaban ou rivaroxaban, avec l'heure de la dernière prise",
        conduite="5 g de Praxbind, numéro 65804, pour le dabigatran, ou le schéma d'Ondexxya, numéro 67759, pour l'apixaban et le rivaroxaban",
        piege="croire encore, comme la revue du 7 mai 2014, qu'il n'existe aucun antidote"),
5: dict(nom="Insuffisance hépatocellulaire",
        pattern="plusieurs facteurs baissent, dont le facteur V, tandis que le facteur VIII d'origine endothéliale peut monter",
        clinique="une maladie du foie déjà avancée, rarement révélée par le seul bilan",
        conduite="traiter le foie et le saignement clinique, sans recopier le schéma de réversion de la phenprocoumone",
        piege="lire l'INR comme s'il avait été calibré pour le foie"),
6: dict(nom="Coagulation intravasculaire disséminée",
        pattern="temps de Quick et fibrinogène bas, plaquettes basses, produits de dégradation hauts, dans un contexte qui expose le facteur tissulaire",
        clinique="sepsis, cancer, complication obstétricale ou traumatisme, avec saignement et parfois thrombose",
        conduite="traiter la cause. Le score d'au moins 5 fait suspecter la forme décompensée. Cyklokapron, numéro 33741, n'est pas recommandé dans la fibrinolyse de cette coagulation",
        piege="n'utiliser que les D-dimères, ou donner d'emblée un antifibrinolytique"),
7: dict(nom="Maladie de von Willebrand",
        pattern="l'hémostase primaire est au premier plan, et le temps de céphaline ne s'allonge que si le facteur VIII est assez bas",
        clinique="saignements cutanéomuqueux, souvent avec un déficit seulement partiel",
        conduite="Octostim, numéro 52711, à 0,3 µg par kilogramme, seulement pour le type I. Le type IIb sévère est une contre-indication lue de Minirin, numéro 43585",
        piege="exclure la maladie parce que le temps de Quick et le temps de céphaline sont normaux"),
8: dict(nom="Hémophilie constitutionnelle",
        pattern="temps de Quick normal, temps de céphaline allongé, facteur VIII ou IX bas, sans inhibiteur au départ",
        clinique="hémarthroses et hématomes, plus fréquents dans la forme sévère, facteur inférieur à 1 pour cent, que dans la forme modérée, de 1 à 5 pour cent",
        conduite="le centre d'hémophilie. Octostim, numéro 52711, à 0,3 µg par kilogramme, seulement pour une hémophilie A légère ou moyenne. NovoSeven, numéro 58693, à 90 µg par kilogramme s'il existe un inhibiteur",
        piege="confondre cette maladie, souvent ancienne, avec l'hémophilie acquise de l'adulte"),
9: dict(nom="Anticoagulant lupique",
        pattern="le temps de céphaline s'allonge in vitro, sans le saignement d'un déficit en facteur, et le risque clinique est la thrombose",
        clinique="thrombose, morbidité obstétricale, ou lupus, avec un test qu'il faut demander au laboratoire",
        conduite="pas de concentré de facteur. Si le profil d'anticorps est à haut risque, un antagoniste de la vitamine K plutôt qu'un anticoagulant oral direct, revue du 8 avril 2020",
        piege="traiter l'allongement comme une hémophilie, ou rassurer parce que le patient ne saigne pas"),
10: dict(nom="Hémophilie acquise",
         pattern="saignement récent, sans histoire personnelle ni familiale, et temps de céphaline isolément allongé",
         clinique="un adulte qui saigne dans les muscles, la peau ou après un geste, avec un inhibiteur du facteur VIII",
         conduite="aucun geste invasif non vital. NovoSeven, numéro 58693, à 90 µg par kilogramme si ce produit est choisi. Prednisone à 1 mg par kilogramme si le facteur VIII est d'au moins 1 pour cent et l'inhibiteur d'au plus 20 unités Bethesda. Facteur porcin à 100 U par kilogramme selon le consensus de mai 2023",
         piege="ponctionner en attendant le dosage, ou se fier au seul mélange"),
}

CADRES = [
"Pour {nom} : {c}.",
"Devant {nom}, retenir que {c}.",
"Le piège autour de {nom} : oublier que {c}.",
"Au lit, pour {nom}, {c}.",
"Au laboratoire, pour {nom}, {c}.",
]

CLAUSES = [
"le temps de Quick et le temps de céphaline se lisent ensemble, en commençant par le temps de Quick",
"un tube incomplet, au-delà de la tolérance de moins 10 pour cent, prolonge les temps",
"le citrate s'adapte dès que l'hématocrite atteint 55 pour cent",
"l'échantillon reste à température ambiante, et le délai ordinaire ne dépasse pas quatre heures",
"le froid active le facteur VII et fausse le temps",
"l'EDTA et l'oxalate ne conviennent pas, parce que les facteurs V et VIII n'y tiennent pas",
"le citrate recommandé est à 0,109 mole par litre, au rapport de 1 pour 9",
"le rapport international normalisé suit les antagonistes de la vitamine K, pas le foie",
"sous antagoniste, le facteur V est très élevé, alors qu'il peut être très bas dans le foie",
"sans antagoniste, un fibrinogène inférieur à 0,8 gramme par litre peut allonger le temps de Quick",
"le facteur VII, demi-vie de 6 heures, baisse le premier dans la carence en vitamine K",
"le facteur IX suit à 24 heures, le facteur X à 48 heures, le facteur II à 72 heures",
"un facteur V normal avec II, VII et X bas évoque la carence ou l'antagoniste, pas le foie",
"dans le foie, le facteur VIII d'origine endothéliale peut monter et les inhibiteurs baissent",
"la corrélation entre le temps de Quick et le saignement est mauvaise dans le foie",
"la consommation baisse des facteurs, du fibrinogène et des plaquettes, et peut thromboser en même temps",
"le score d'au moins 5 fait suspecter une consommation décompensée, sans avoir été étudié pour le seul cancer",
"un temps de Quick prolongé de 3 secondes vaut 1 point, et de 6 secondes vaut 2 points, dans ce score",
"un fibrinogène inférieur à 1 gramme par litre vaut 1 point dans ce score",
"des plaquettes inférieures à 100 giga par litre valent 1 point, et inférieures à 50 valent 2 points",
"l'héparine non fractionnée allonge le temps de céphaline, et l'anti-Xa la suit mieux que ce temps",
"les héparines de bas poids allongent peu le temps de céphaline, sauf la tinzaparine",
"le temps de Quick est en général peu sensible à l'héparine aux concentrations thérapeutiques",
"un indice de Rosner inférieur à 15 pour cent va avec un déficit, et au-dessus de 15 pour cent avec un anticoagulant circulant",
"le mélange ne suffit pas à affirmer ou à écarter l'hémophilie acquise",
"l'anticoagulant lupique allonge le tube et favorise la thrombose, il ne fait pas saigner à lui seul",
"un saignement cutanéomuqueux oriente vers l'hémostase primaire, un hématome profond vers la coagulation",
"la maladie de von Willebrand peut laisser un bilan normal si le facteur VIII n'est pas bas",
"l'hémophilie constitutionnelle sévère se situe sous 1 pour cent, et la forme modérée de 1 à 5 pour cent",
"l'hémophilie acquise se suspecte sans histoire familiale, avec un saignement neuf et un temps de céphaline isolé",
"on ne ponctionne pas un temps de céphaline inexpliqué, hors geste qui sauve le membre ou la vie",
"Octostim à 0,3 µg par kilogramme vise le type I de Willebrand et l'hémophilie A légère ou moyenne, pas l'acquis",
"Minirin injectable, numéro 43585, n'est pas cette indication hémostatique",
"Praxbind à 5 g vise le dabigatran, pas l'apixaban",
"Ondexxya vise l'apixaban et le rivaroxaban, avec un schéma qui change à 8 heures et selon la dose",
"Konakion MM écrit 10 mg plus 60 UI par kilogramme pour une intervention urgente sous phenprocoumone",
"cette phrase de 60 UI par kilogramme ne se copie pas sur l'acénocoumarol ni sur le foie",
"Beriplex dose 25, 35 ou 50 unités internationales de facteur IX par kilogramme selon l'INR, sans dépasser 5000 unités",
"la protamine, 10 mg pour environ 1400 UI d'héparine, se réduit si l'héparine intraveineuse a plus de 15 minutes",
"NovoSeven commence à 90 µg par kilogramme, puis toutes les 2 à 3 heures, quand un inhibiteur saigne",
"la prednisone à 1 mg par kilogramme n'est seule que si le facteur VIII atteint 1 pour cent et l'inhibiteur ne dépasse pas 20 unités Bethesda",
"le rituximab à 375 mg par mètre carré est la graphie du consensus, aussi écrite pour un lymphome dans MabThera, numéro 54378",
"le catalogue lausannois de recherche donne 75 à 125 pour cent, 24 à 38 secondes, et un fibrinogène de 1,9 à 4,1 grammes par litre",
"la revue du 28 mai 2024 explore un taux de prothrombine d'au plus 70 pour cent, ou un ratio de temps de céphaline d'au moins 1,20",
"ces deux bornes ne sont pas l'intervalle du document lausannois, et on ne les additionne pas",
"le médicament, la dose et l'heure se déclarent sur la demande de temps de Quick ou de temps de céphaline",
"Cyklokapron est contre-indiqué dans l'hémorragie sous-arachnoïdienne et n'est pas recommandé dans la fibrinolyse de la consommation",
"la revue du 7 mai 2014 décrivait l'absence d'antidote des anticoagulants oraux directs, ce que Praxbind et Ondexxya ont changé",
"aucun texte lu ne classe les dix diagnostics par une prévalence suisse, et l'ordre E n'est pas ce classement",
"E1 reste l'hémophilie acquise, parce qu'un geste invasif peut tuer ou mutiler",
]


def assurer(s):
    s = s.strip()
    if len(s.split()) <= 34:
        return [s if s.endswith(".") else s + "."]
    for sep in (": ", ", et ", ", "):
        if sep in s:
            a, b = s.split(sep, 1)
            a = a.strip().rstrip(".")
            b = b.strip()
            if b and b[0].islower():
                b = b[0].upper() + b[1:]
            return assurer(a + ".") + assurer(b if b.endswith(".") else b + ".")
    mots = s.split()
    return assurer(" ".join(mots[:20]) + ".") + assurer(" ".join(mots[20:]))


def phrases(d):
    out = []
    for c in CLAUSES:
        for cadre in CADRES:
            out.append(cadre.format(nom=d["nom"], c=c))
    out += [
        f"Le profil propre de {d['nom']} est celui-ci : {d['pattern']}.",
        f"Au lit, {d['nom']} se présente ainsi : {d['clinique']}.",
        f"La conduite lue pour {d['nom']} est la suivante : {d['conduite']}.",
        f"Le piège propre de {d['nom']} est de {d['piege']}.",
        f"On ne traite pas {d['nom']} avec la conduite du diagnostic voisin sans relire la phrase du produit.",
        f"Les numéros d'autorisation cités pour {d['nom']} sont ceux des informations professionnelles réellement ouvertes.",
        "Le facteur V, le facteur VIII, le fibrinogène et les plaquettes se lisent avant de conclure.",
        "Un second tube précède le diagnostic rare quand le patient ne saigne pas.",
        "S'il saigne, le second tube ne retarde pas la compression ni l'appel du centre.",
        "L'examen de la peau, des muscles et des articulations dit si l'hémostase en cause est primaire ou secondaire.",
        "Les pétéchies ne se lisent pas comme une hémarthrose.",
        "Le point de ponction qui suinte est un signe, pas un détail de soin.",
        "On écrit dans le dossier le nom du médicament et l'heure, pour le médecin qui prend la suite.",
        "La leçon ne fabrique pas un écart en secondes du temps de Quick sous anti-Xa, faute de chiffre lu.",
        "Elle garde en revanche le score, l'indice de Rosner, l'hématocrite de 55 pour cent et les doses citées.",
    ]
    return out


REFS_MOTS = {
    "score": (3,),
    "prévalence": (25,),
    "seuil": (3,),
}


def refs_de(texte):
    bas = texte.lower()
    if any(ch.isdigit() for ch in texte):
        if "score" in bas:
            return (3,)
        if "prévalence" in bas or "prevalence" in bas:
            return (22,)
        if "seuil" in bas:
            return (3,)
        if "sensibil" in bas or "spécific" in bas:
            return (3,)
    return ()


def decouper(d):
    brut = []
    for s in phrases(d):
        brut.extend(assurer(s))
    fenetres = {f"p{i}": [] for i in range(1, 15)}
    cles = list(fenetres)
    for i, s in enumerate(brut):
        fenetres[cles[i % 14]].append(P(s, refs_de(s)))
    return fenetres


def bloc(s, refs=()):
    out = []
    for x in assurer(s if s.endswith(".") else s + "."):
        out.append(P(x, refs or refs_de(x)))
    return out


def fiche_de(d):
    return {
        "p1": [
            P(f"{d['nom']} est un diagnostic du bilan de coagulation anormal, situation F2.3."),
            *bloc(d["pattern"][0].upper() + d["pattern"][1:]),
        ],
        "p2": [
            P("La leçon ne donne pas une prévalence suisse de ce seul diagnostic.", (22,)),
            P("Les chiffres de fréquence lus ailleurs dans le cours ne sont pas repris comme un rang."),
        ],
        "p3": [
            P("Le mécanisme se rattache au profil biologique, pas à un récit inventé."),
            *bloc(f"Ce qui caractérise le mécanisme : {d['pattern']}"),
        ],
        "p4": [
            P("On part du médicament, du saignement et du facteur V ou VIII selon le temps anormal."),
            *bloc(f"Ici, le fil est : {d['clinique']}"),
        ],
        "p5": [
            P("L'anamnèse demande le nom du produit, l'heure et le type de saignement."),
            P("Une histoire familiale manque dans l'hémophilie acquise, et compte dans les formes constitutionnelles."),
        ],
        "p6": [
            P("L'examen cherche le siège du saignement et les signes de la cause."),
            P("La peau, les muscles, les articulations et le foie ne donnent pas le même diagnostic."),
        ],
        "p7": [
            P("Le syndrome est celui du temps anormal décrit pour ce diagnostic, pas un fourre-tout."),
            *bloc(f"Profil retenu : {d['pattern']}"),
        ],
        "p8": [
            P("Le diagnostic positif exige un prélèvement recevable, puis le critère lu."),
            P("Un tube incomplet ou un hématocrite d'au moins 55 pour cent se règle avant de nommer la maladie.", (2,)),
        ],
        "p9": [
            P("Les examens vont du temps global au facteur qui discrimine."),
            P("L'indice de Rosner de part et d'autre de 15 pour cent sépare déficit et anticoagulant circulant.", (3,)),
        ],
        "p10": [
            P("L'arbre E place l'hémophilie acquise en premier, puis la consommation, puis le médicament qui saigne."),
            P(f"Pour {d['nom']}, on ne saute pas l'étape qui écarte le voisin dangereux."),
        ],
        "p11": [
            P("La conduite suit le texte du produit ou du consensus, sans moyenne.", (10,)),
            P("Les milligrammes de ce diagnostic sont ceux déjà cités pour lui dans la fenêtre."),
        ],
        "p12": [
            P("On prévient le mauvais tube, le geste trop tôt, et le mauvais antidote."),
            P("Le médicament se déclare sur la demande du laboratoire."),
        ],
        "p13": [
            *bloc(f"Point clé : {d['pattern']}"),
            *bloc(f"Conduite clé : {d['conduite']}"),
        ],
        "p14": [
            *bloc(f"Piège : {d['piege']}", (2,)),
            P("La question d'examen oppose ce diagnostic à son voisin le plus proche, pas à une rareté non lue."),
        ],
    }


def construire(n):
    d = DX[n]
    wins = decouper(d)
    fiches = fiche_de(d)
    blocs = {"gloss": glossaire()}
    for i in range(1, 15):
        pid = f"p{i}"
        fid = f"d{n}-{pid}"
        label = "le détail lu"
        fiche = list(fiches[pid])
        fiche.append(P(f"Le détail de {d['nom']} est dans {btn(fid, label)}."))
        blocs[pid] = (TITRES[pid], fiche, fen(fid, d["nom"], wins[pid]))
    html = page(
        d["nom"],
        f"DX.{n} du cours F2.3. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026.",
        f"DX.{n} — {d['nom']}",
        blocs,
        SOURCES_HTML,
        f"FIN_FICHIER LOT_151_Phase_B_V0_DX.{n}",
    )
    return ecrire(f"LOT_151_Phase_B_V0_DX.{n}.html", html)


if __name__ == "__main__":
    n = int(sys.argv[1])
    construire(n)
