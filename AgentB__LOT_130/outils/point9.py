#!/usr/bin/env python3
"""Point 9 : gold standard ou première intention, tableau de lecture, schéma seulement si le résultat s'y prête."""
from __future__ import annotations
from fabriquer import cite, table

# §14.8.7 : pas de schéma généré à la place d'un cliché. Le tableau reste un tableau (§14.8.8).
ABS = (
    "<p>Aucune image libre fiable trouvée — Wikimedia Commons, Open-i et la bibliothèque ouverte européenne, "
    "consultés le neuf novembre deux mille vingt-six. Aucun schéma n'est dessiné pour combler ce vide.</p>\n"
)

def _t(lignes: list[list[str]]) -> str:
    return table(lignes, ["Cas", "Interprétation", "Hypothèse"])

def bloc_p9(prefix: str) -> str:
    fn = {
        "dx1": _dx1, "dx2": _dx2, "dx3": _dx3, "dx4": _dx4, "dx5": _dx5,
        "dx6": _dx6, "dx7": _dx7, "dx8": _dx8, "dx9": _dx9, "dx10": _dx10,
    }[prefix]
    return ABS + fn()

def _dx1() -> str:
    intro = (
        "<p>Gold standard : confirmation hors cabinet. "
        "Première intention biologique : créatinine, débit de filtration, sédiment et rapport albumine sur créatinine."
        f"{cite(['ESCCONF', 'ESCLAB'])}</p>\n"
    )
    mes = _t([
        ["Positif",
         "Cabinet au moins 140 mmHg ou 90 mmHg, confirmé hors cabinet." + cite(["ESCCONF"]),
         "Hypertension retenue."],
        ["Normal",
         "Automesure sous 135/85 mmHg." + cite(["SSHM2"]),
         "Pas le seuil d'hypertension d'automesure."],
        ["Limite",
         "Écart de plus de 5 mmHg entre deux lectures." + cite(["SSHM2B"]),
         "On prend la troisième mesure."],
        ["Discordant",
         "Cabinet au moins 140 mmHg et automesure sous 135/85 mmHg." + cite(["ESCCONF", "SSHM2"]),
         "On ne traite pas à vie sur le cabinet seul."],
    ])
    bio = (
        "<p>Le bilan biologique nommé ne donne aucun seuil chiffré de créatinine ni de rapport dans l'extrait. On n'en invente pas."
        f"{cite(['ESCLAB'])}</p>\n"
        + _t([
            ["Positif", "Créatinine, débit, sédiment et rapport albumine sur créatinine sont demandés ensemble." + cite(["ESCLAB"]),
             "Retentissement et piste rénale ou rénovasculaire."],
            ["Normal", "L'extrait ne définit pas de zone normale chiffrée." + cite(["ESCLAB"]),
             "On ne fabrique pas un seuil suisse absent."],
            ["Limite", "Un seul de ces quatre examens." + cite(["ESCLAB"]),
             "Le bilan de première intention reste incomplet."],
            ["Discordant", "Une image à la place de ce laboratoire." + cite(["ESCLAB"]),
             "Le texte place d'abord le dosage et le sédiment."],
        ])
    )
    return intro + mes + bio

def _dx2() -> str:
    intro = (
        "<p>Gold standard : épreuve debout au cabinet, après 5 minutes assis ou couché. "
        "L'enregistrement ambulatoire ne pose pas formellement le diagnostic."
        f"{cite(['ESCOH'])}</p>\n"
    )
    mes = _t([
        ["Positif",
         "Baisse d'au moins 20 mmHg ou 10 mmHg à 1 minute ou à 3 minutes." + cite(["ESCOH"]),
         "Hypotension orthostatique."],
        ["Normal",
         "Baisse inférieure à 20 mmHg et à 10 mmHg." + cite(["ESCOH"]),
         "La définition n'est pas remplie."],
        ["Limite",
         "Symptôme au lever sans la baisse d'au moins 20 mmHg ou 10 mmHg." + cite(["ESCOH"]),
         "Le symptôme seul ne pose pas la définition."],
        ["Discordant",
         "Enregistrement ambulatoire sans l'épreuve debout." + cite(["ESCOH"]),
         "Ce n'est pas le test formel."],
    ])
    return intro + mes

def _dx3() -> str:
    return (
        "<p>Première intention : rénine et aldostérone à 8 h, à jeun, sous traitement neutre. "
        "Aucune image libre d'adénome de Conn n'est placée à la place de ce dosage. "
        "L'extrait suisse ne donne pas de seuil chiffré du rapport, en mmol ou autre unité."
        f"{cite(['SSHALD'])}</p>\n"
        + _t([
            ["Positif",
             "Dosages à 8 h, à jeun, sous diltiazem, vérapamil ou doxazosine." + cite(["SSHALD"]),
             "Condition suisse du dépistage remplie. Le rapport élevé se confirme ensuite."],
            ["Normal",
             "50 à 60 % des patients sont normokaliémiques." + cite(["ISHK"]),
             "Une kaliémie normale n'écarte pas l'hyperaldostéronisme."],
            ["Limite",
             "Kaliémie basse sans le couple rénine-aldostérone." + cite(["ISHK"]),
             "Oriente, ne pose pas le diagnostic."],
            ["Discordant",
             "Dosage hors des conditions de 8 h, à jeun, sous traitement neutre." + cite(["SSHALD"]),
             "Le rapport n'est pas interprétable."],
        ])
    )

def _dx4() -> str:
    return (
        "<p>Première intention : protéinurie, hématurie, leucocyturie et débit de filtration, puis échographie. "
        "Aucune échographie humaine libre d'une néphropathie n'a été retenue. "
        "L'extrait ne donne pas de créatinine en µmol/L."
        f"{cite(['ISHREN'])}</p>\n"
        + _t([
            ["Positif",
             "Protéinurie, hématurie ou leucocyturie, ou débit diminué." + cite(["ISHREN"]),
             "Maladie du parenchyme à confirmer, avec l'échographie."],
            ["Normal",
             "Sédiment sans protéinurie, hématurie ni leucocyturie, et débit non diminué." + cite(["ISHREN"]),
             "Pas d'argument parenchymateux dans ce bilan."],
            ["Limite",
             "Un seul de ces trois signes du sédiment." + cite(["ISHREN"]),
             "Piste à compléter par le débit et l'échographie."],
            ["Discordant",
             "Chute du débit de plus de 30 % sous inhibiteur." + cite(["ISHRAS"]),
             "On cherche alors une sténose, autre diagnostic."],
        ])
    )

def _dx5() -> str:
    return (
        "<p>Gold standard : imagerie de l'artère rénale. Première intention selon la fiche suisse : doppler, IRM ou artériographie. "
        "Aucune image libre d'une sténose rénale n'a été retenue. Une coronarographie trouvée sur le même moteur montre un autre vaisseau et n'est pas utilisée."
        f"{cite(['SSHRAS', 'ISHRAS'])}</p>\n"
        + _t([
            ["Positif",
             "Sténose vue au doppler, à l'IRM ou à l'artériographie." + cite(["SSHRAS"]),
             "Hypertension rénovasculaire retenue sur l'image de l'artère."],
            ["Normal",
             "Imagerie artérielle sans sténose." + cite(["SSHRAS"]),
             "Pas d'obstacle retenu sur cet examen."],
            ["Limite",
             "Chute du débit de plus de 30 % après inhibiteur, sans image encore." + cite(["ISHRAS"]),
             "Indication d'imagerie, pas la preuve seule."],
            ["Discordant",
             "Image d'un autre vaisseau, sans doppler, IRM ni artériographie rénale." + cite(["SSHRAS"]),
             "Ne montre pas l'artère rénale."],
        ])
    )

def _dx6() -> str:
    intro = (
        "<p>Gold standard : polysomnographie et index d'apnées-hypopnées. "
        "Aucun tracé libre d'apnées n'a été retenu. Les hypnogrammes trouvés dessinent des stades de sommeil, pas les apnées."
        f"{cite(['ESCOSA'])}</p>\n"
    )
    mes = _t([
        ["Positif",
         "Index de 15 à 30, ou au-dessus de 30." + cite(["ESCOSA"]),
         "Ventilation par pression positive indiquée."],
        ["Normal",
         "Index sous 15." + cite(["ESCOSA"]),
         "Poids et hygiène de sommeil le plus souvent."],
        ["Limite",
         "L'extrait ne crée pas de zone entre les trois paliers sous 15, de 15 à 30, et au-dessus de 30." + cite(["ESCOSA"]),
         "On classe dans l'un des trois, sans quatrième seuil."],
        ["Discordant",
         "Endoscopie de sommeil avant l'index." + cite(["ESCOSA"]),
         "L'endoscopie vient si la ventilation n'est pas tolérée, pas à la place de l'index."],
    ])
    return intro + mes

def _dx7() -> str:
    return (
        "<p>L'examen décisif est l'anamnèse du médicament, de l'automédication ou de la substance. "
        "Aucune image libre ne remplace cette anamnèse."
        f"{cite(['ESCMED'])}</p>\n"
        + _t([
            ["Positif",
             "Prise d'un médicament, d'une automédication ou d'une substance listée comme cause." + cite(["ESCMED"]),
             "Hypertension induite par cette prise."],
            ["Normal",
             "Aucune prise de ce type retrouvée." + cite(["ESCMED"]),
             "Cette cause n'est pas retenue."],
            ["Limite",
             "Automédication non interrogée." + cite(["ESCMED"]),
             "Le texte inclut les produits sans ordonnance. L'anamnèse reste incomplète."],
            ["Discordant",
             "Imagerie lancée avant l'anamnèse médicamenteuse." + cite(["ESCMED"]),
             "Le texte place d'abord le médicament ou la substance."],
        ])
    )

def _dx8() -> str:
    return (
        "<p>Gold standard de dépistage : métanéphrines et normétanéphrines plasmatiques ou urinaires de 24 h. "
        "L'image vient après. Aucun scanner n'est placé à la place du dosage. "
        "L'extrait suisse ne donne pas de seuil en nmol/L."
        f"{cite(['SSHMET'])}</p>\n"
        + _t([
            ["Positif",
             "Métanéphrines ou normétanéphrines plasmatiques, ou urinaires de 24 h, élevées." + cite(["SSHMET"]),
             "Dépistage positif. L'imagerie vient ensuite."],
            ["Normal",
             "Métanéphrines et normétanéphrines non élevées." + cite(["SSHMET"]),
             "Pas d'argument pour cette tumeur sur ce dosage."],
            ["Limite",
             "Aucun seuil chiffré suisse dans l'extrait." + cite(["SSHMET"]),
             "On ne fabrique pas une valeur en nmol/L."],
            ["Discordant",
             "Scanner avant le dosage des métanéphrines." + cite(["SSHMET"]),
             "Le dépistage nommé est le dosage, pas l'image."],
        ])
    )

def _dx9() -> str:
    return (
        "<p>Gold standard : pression au moins 180/110 mmHg avec atteinte aiguë d'organe. "
        "Le fond d'œil en fait partie quand il montre des hémorragies, des exsudats ou un œdème papillaire. "
        "Aucune image libre de ces lésions n'a été retenue : un cliché titré rétinopathie hypertensive a été regardé, "
        "et ces lésions n'y étaient pas assez nettes pour être entourées."
        f"{cite(['ESCURG', 'ESCFO'])}</p>\n"
        + _t([
            ["Positif",
             "Au moins 180/110 mmHg, avec hémorragies, exsudats ou œdème papillaire." + cite(["ESCURG", "ESCFO"]),
             "Urgence hypertensive, ou hypertension maligne si le fond d'œil est celui-là."],
            ["Normal",
             "Pression élevée sans atteinte aiguë d'organe." + cite(["ESCURG"]),
             "Ce n'est pas l'urgence définie."],
            ["Limite",
             "Chiffre seul au moins 180/110 mmHg, sans atteinte décrite." + cite(["ESCURG"]),
             "Le chiffre ne suffit pas."],
            ["Discordant",
             "Fond d'œil sans hémorragie, exsudat ni œdème papillaire, malgré un chiffre haut." + cite(["ESCFO", "ESCURG"]),
             "Pas l'atteinte rétinienne qui signe l'urgence maligne."],
        ])
    )

def _dx10() -> str:
    intro = (
        "<p>Première intention : lactate avec signes d'hypoperfusion. "
        "Le lactate n'a pas de cliché. Les valeurs ci-dessous sont celles de l'extrait européen, en mmol/L. "
        "Le dossier ne contient pas de seuil suisse."
        f"{cite(['SSCLAC', 'SSCLAC2'])}</p>\n"
    )
    mes = _t([
        ["Positif",
         "Lactate élevé, avec infection et hypoperfusion." + cite(["SSCLAC"]),
         "Entre dans la définition du choc septique que l'extrait rattache à un lactate élevé."],
        ["Normal",
         "Lactate non élevé. La sensibilité des seuils d'étude va de 66 à 83 %." + cite(["SSCLAC2"]),
         "Un lactate non élevé n'écarte pas le choc."],
        ["Limite",
         "Seuil d'étude entre 1,6 et 2,5 mmol/L." + cite(["SSCLAC2"]),
         "Zone de dépistage dans les études, pas un seuil diagnostique suisse."],
        ["Discordant",
         "Mauvaise perfusion clinique et lactate qui ne suit pas le même cap." + cite(["SSCCRT"]),
         "Les deux lectures existent. L'une ne remplace pas l'autre."],
    ])
    return intro + mes
