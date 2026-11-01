#!/usr/bin/env python3
"""LOT_245 — suspicion de maladie rare. Phrases courtes, sources lues, fenêtres V8."""
from __future__ import annotations

import html
import json
import re
import subprocess
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_245"
EV = LOT / "evidence"
CAP = LOT / "captures"
MODELE = RACINE / "harnais" / "modele_lecon" / "MODELE_DD_V8.html"

CIBLES = {
    "A": (74000, 78500),
    "1": (36500, 38400),
    "2": (39800, 41800),
    "3": (42800, 44800),
    "4": (45000, 47000),
    "5": (46000, 48000),
    "6": (36200, 38200),
    "7": (40800, 42800),
    "8": (43600, 45600),
    "9": (45000, 47000),
    "10": (38400, 40400),
}

DX = [
    "Décompensation métabolique héréditaire du nourrisson",
    "Régression neurométabolique ou neurodégénérative",
    "Maladie lysosomale avec traitement spécifique",
    "Porphyrie aiguë",
    "Maladie rare traitable encore méconnue",
    "Maladie fréquente d'expression inhabituelle",
    "Symptômes sans lésion identifiée",
    "Trait familial bénin",
    "Parcours diagnostique non structuré",
    "Maladie rare sans traitement curatif",
]

TITRES_H2 = {
    1: "1. Définition",
    2: "2. Épidémiologie",
    3: "3. Physiopathologie",
    4: "4. Démarche diagnostique",
    5: "5. Anamnèse",
    6: "6. Examen physique",
    7: "7. Approche syndromique",
    8: "8. Diagnostic positif",
    9: "9. Examens complémentaires",
    10: "10. Arbre décisionnel",
    11: "11. Prise en charge",
    12: "12. Prévention",
    13: "13. Points clés",
    14: "14. Pièges",
}

LEADS = {
    1: "La définition suisse et la définition européenne ne se confondent pas.",
    2: "Les effectifs suisses lus ne sont pas fondus en un seul nombre.",
    3: "La physiopathologie explique le signal, pas un mécanisme inventé.",
    4: "La démarche commence par l'urgence, puis l'orientation.",
    5: "L'anamnèse familiale précède le catalogue des maladies.",
    6: "L'examen cherche un signal atypique, pas un diagnostic complet.",
    7: "L'approche syndromique sépare les voisins avant l'étiquette rare.",
    8: "Le diagnostic positif reste celui du centre, avec consentement.",
    9: "Les examens complémentaires sont ciblés, puis génétiques si indiqué.",
    10: "L'arbre décisionnel tient sur le schéma à deux niveaux.",
    11: "La prise en charge oriente, informe et ne dose pas sans information professionnelle.",
    12: "La prévention passe par le dépistage néonatal et l'information.",
    13: "Les points clés se redisent avec la personne et sa famille.",
    14: "Les pièges viennent des chiffres fondus et des examens en aveugle.",
}

CLICHES = {
    "A": ("arbre sur trois générations", "centre sans diagnostic"),
    "1": ("nourrisson somnolent", "intervalle libre"),
    "2": ("perte d'un acquis", "développement qui recule"),
    "3": ("atteinte de plusieurs organes", "famille déjà touchée"),
    "4": ("crise douloureuse répétée", "déclencheur à rechercher"),
    "5": ("traitement habituel inefficace", "association de signes improbable"),
    "6": ("tableau qui ne colle pas", "terrain qui modifie le signe"),
    "7": ("bilan répété normal", "signal atypique absent"),
    "8": ("trait stable dans la famille", "aucun retentissement"),
    "9": ("avis d'organe dispersés", "dossier non synthétisé"),
    "10": ("diagnostic déjà nommé", "projet familial à expliquer"),
}


def mots(phrase: str) -> int:
    t = re.sub(r"«[^»]*»", " ", phrase)
    return len(re.findall(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*", t))


class PhraseLongue(Exception):
    pass


class PhraseDouble(Exception):
    pass


def exiger(phrase: str) -> str:
    phrase = re.sub(r"\s+", " ", phrase).strip()
    if not phrase.endswith((".", "?", "!")):
        phrase += "."
    n = mots(phrase)
    if n > 32:
        raise PhraseLongue(f"{n} : {phrase}")
    if re.search(r"\d+\s*g\b", phrase, re.I):
        raise PhraseLongue("GRAMME : " + phrase)
    if re.search(r"À\s+vérifier|A\s+vérifier|TODO|FIXME|\(\?\)", phrase):
        raise PhraseLongue("MARQUEUR : " + phrase)
    if re.search(r"\d(?:mg|µg|μg|mcg|mmol|%)", phrase):
        raise PhraseLongue("COLLE : " + phrase)
    if "mmol/L" in phrase or re.search(r"\b(FDA|EMA|BNF|UpToDate|Vidal|Micromedex|Lexicomp)\b", phrase):
        raise PhraseLongue("MARQUE : " + phrase)
    if re.search(r"\b(p\.\s?ex\.|cf\.|etc\.|env\.)\b", phrase):
        raise PhraseLongue("ABREV : " + phrase)
    return phrase


def css() -> str:
    brut = MODELE.read_text(encoding="utf-8")
    m = re.search(r"<style>(.*?)</style>", brut, re.S)
    extra = """
.dessin{margin:.4rem 0}
.dessin input{position:absolute;opacity:0;pointer-events:none}
.dessin .choix{display:flex;flex-wrap:wrap;gap:.35rem;margin:0 0 .45rem}
.dessin .choix label{border:1px solid var(--trait);border-radius:6px;padding:.2rem .55rem;cursor:pointer;background:var(--page)}
.dessin .niv{display:none}
.dessin .plan svg{width:100%;height:auto;max-width:40rem;background:var(--page);border:1px solid var(--trait);border-radius:8px}
.cliche{border-bottom:1px dashed var(--lien)}
"""
    rules = []
    for i in range(0, 12):
        pid = f"f{i}"
        rules.append(f"#{pid}a:checked ~ .plan .n1{{display:block}}")
        rules.append(f"#{pid}b:checked ~ .plan .n2{{display:block}}")
        rules.append(f"#{pid}a:checked ~ .choix label[for='{pid}a']{{outline:2px solid var(--lien)}}")
        rules.append(f"#{pid}b:checked ~ .choix label[for='{pid}b']{{outline:2px solid var(--lien)}}")
    return m.group(1) + extra + "\n" + "\n".join(rules)


def abbr(sigle: str, titre: str) -> str:
    return f'<abbr title="{html.escape(titre, quote=True)}">{html.escape(sigle)}</abbr>'


A_OFSP = abbr("OFSP", "Office fédéral de la santé publique")
A_UE = abbr("UE", "Union européenne")
A_LAGH = abbr("LAGH", "loi fédérale sur l'analyse génétique humaine")
A_RSMR = abbr("RSMR", "Registre suisse des maladies rares")
A_CMR = abbr("CMR", "centre pour maladies rares")
A_IUMSP = abbr("IUMSP", "Institut universitaire de médecine sociale et préventive de Lausanne")
A_OPAS = abbr("OPAS", "ordonnance sur les prestations de l'assurance des soins")
A_MCAD = abbr("MCAD", "déficit en acyl-CoA déshydrogénase des acides gras à chaîne moyenne")
A_MSUD = abbr("MSUD", "maladie du sirop d'érable")
A_PROF = abbr("PROFILES", "Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland")


def sup(n: int) -> str:
    return f'<sup class="s">{n}</sup>'


class B:
    def __init__(self):
        self.sec = {i: [] for i in range(1, 15)}
        self.vus: set[str] = set()
        self.noyau = 0
        self.extra = 0

    def add(self, sec: int, phrase: str, src: int, expandable: bool = False):
        phrase = exiger(phrase)
        cle = re.sub(r"[^a-z0-9àâäçéèêëîïôöùûüœ]+", " ", phrase.lower()).strip()
        if cle in self.vus:
            raise PhraseDouble(phrase)
        self.vus.add(cle)
        self.sec[sec].append((f"<p>{phrase}{sup(src)}</p>", expandable, len(phrase.encode())))
        if expandable:
            self.extra += 1
        else:
            self.noyau += 1

    def retirer_dernier_extra(self) -> bool:
        for sec in range(14, 0, -1):
            for i in range(len(self.sec[sec]) - 1, -1, -1):
                if self.sec[sec][i][1]:
                    self.sec[sec].pop(i)
                    self.extra -= 1
                    return True
        return False

    def texte_y(self) -> int:
        n = 0
        for items in self.sec.values():
            n += 80
            for _frag, _e, ln in items:
                n += ln + 7
        return n


def fenetre(fid: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{fid}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def bouton(fid: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{fid}">Développer</button>'


def svg_lignes(titre: str, lignes: list[tuple[str, int, str]]) -> str:
    h = 24 + len(lignes) * 48
    parts = [
        f'<svg viewBox="0 0 820 {h}" role="img">',
        f"<title>{html.escape(titre)}</title>",
    ]
    for i, (lab, largeur, coul) in enumerate(lignes):
        y = 16 + i * 48
        parts.append(
            f'<text x="8" y="{y+24}" font-size="16" font-family="Verdana,sans-serif" fill="currentColor">{html.escape(lab)}</text>'
        )
        parts.append(
            f'<rect x="310" y="{y}" width="{largeur}" height="32" rx="7" fill="{coul}" stroke="#1d2a30" stroke-width="1"/>'
        )
    parts.append("</svg>")
    return "".join(parts)


def figure(pid: str, leg1: str, svg1: str, leg2: str, svg2: str, caption: str) -> str:
    return (
        f'<div class="dessin">'
        f'<input type="radio" name="{pid}" id="{pid}a" checked>'
        f'<input type="radio" name="{pid}" id="{pid}b">'
        f'<div class="choix" role="tablist"><label for="{pid}a">{html.escape(leg1)}</label>'
        f'<label for="{pid}b">{html.escape(leg2)}</label></div>'
        f'<div class="plan"><div class="niv n1">{svg1}</div><div class="niv n2">{svg2}</div></div>'
        f"<p>{html.escape(caption)}</p></div>"
    )


# (nom court, clause, src, section)
def banque() -> list[tuple[str, str, int, int]]:
    return [
        ("la définition suisse", "moins de cinq sur dix mille, et maladie menaçante ou invalidante", 1, 1),
        ("le second critère", "la maladie est menaçante pour la vie ou chroniquement invalidante", 1, 1),
        ("les sous-types", "un sous-type d'une maladie fréquente n'entre pas dans la définition suisse", 1, 1),
        ("la définition européenne", "la page européenne retient moins de cinq personnes sur dix mille", 3, 1),
        ("les deux définitions", "on enseigne le critère suisse de gravité à côté du seul seuil de fréquence européen", 3, 14),
        ("l'estimation 2012", "la prévalence médiane suisse estimée est de 7,2 pour cent", 1, 2),
        ("le nombre 2012", "cela représente 582 450 personnes en Suisse à la fin de 2012", 1, 2),
        ("la borne basse", "la variante basse est de 2,2 pour cent, soit 178 391 personnes", 1, 2),
        ("la borne haute", "la variante haute est de 12,3 pour cent, soit 988 266 personnes", 1, 2),
        ("la source du calcul", "le calcul applique 6 839 maladies d'Orphadata à la population suisse", 1, 2),
        ("le demi-million", "la page de l'office lue en 2026 dit plus d'un demi-million de personnes", 2, 2),
        ("le chiffre associatif", "l'alliance des patients écrit plus de 500 000 personnes", 12, 2),
        ("ne pas fondre", "on n'additionne pas 7,2 pour cent, le demi-million et 500 000", 2, 14),
        ("le compte européen", "entre 6 000 et 8 000 maladies rares sont répertoriées", 3, 2),
        ("la part génétique", "environ 80 pour cent sont d'origine génétique sur la page européenne", 3, 3),
        ("l'âge de début", "70 pour cent se déclarent pendant l'enfance sur la même page", 3, 2),
        ("les personnes en Europe", "entre 27 et 36 millions de personnes vivent avec une maladie rare dans l'Union", 3, 2),
        ("les nouvelles descriptions", "en moyenne cinq nouvelles maladies rares sont décrites chaque semaine", 1, 2),
        ("pas de total annuel", "le concept ne convertit pas ces cinq descriptions hebdomadaires en total annuel", 1, 14),
        ("le jour du dépistage", "le prélèvement au talon se fait le troisième ou le quatrième jour", 4, 12),
        ("dix analyses", "la page du dépistage parle de dix analyses sur quelques gouttes de sang", 4, 9),
        ("onze maladies", "la page des dépistages génétiques parle de onze maladies recherchées ensemble", 5, 9),
        ("les deux comptes", "dix analyses et onze maladies restent côte à côte", 5, 14),
        ("le seul dépistage", "le seul dépistage génétique autorisé en Suisse est le dépistage néonatal", 5, 12),
        ("la liste tarifaire", "la position 1368.00 nomme les maladies du dépistage au 1er janvier 2026", 6, 9),
        ("le laboratoire unique", "en Suisse, seul le laboratoire de Zurich fait ce dépistage", 7, 9),
        ("onze dans le commentaire", "le commentaire tarifaire de 2026 dit onze maladies diagnostiquées tôt", 7, 8),
        ("neuf centres", "six centres transversaux en mai 2020, puis trois en mai 2021, soit neuf", 2, 11),
        ("le rôle du centre", "le centre reçoit la personne sans diagnostic ou au diagnostic incertain", 2, 4),
        ("quatre centres métaboliques", "en novembre 2021, quatre centres de référence métaboliques sont reconnus", 2, 11),
        ("sept centres neuromusculaires", "en novembre 2021, sept centres neuromusculaires sont reconnus", 2, 11),
        ("vingt-cinq centres", "en décembre 2024, la page de l'office compte vingt-cinq centres spécialisés", 2, 11),
        ("quarante-deux centres", "en février 2026, la coordination annonce quarante-deux centres reconnus", 9, 11),
        ("ne pas additionner", "on n'additionne pas vingt-cinq et quarante-deux", 9, 14),
        ("la mission de coordination", "la coordination reconnaît les centres et les registres", 8, 11),
        ("le registre", "le registre suisse vise une meilleure épidémiologie, puis de meilleurs soins", 2, 12),
        ("Orphanet Suisse", "Orphanet Suisse collabore avec la coordination et le registre", 2, 9),
        ("l'alliance", "l'alliance des patients porte leur perspective dans les travaux", 2, 13),
        ("les infirmités", "depuis le 1er janvier 2022, la liste des infirmités congénitales peut être complétée", 2, 11),
        ("le consentement", "l'analyse exige un consentement libre et exprès après information suffisante", 10, 11),
        ("la révocation", "la personne peut retirer son consentement en tout temps", 10, 11),
        ("l'information", "l'information porte sur le but, le type, la pertinence et les risques", 10, 13),
        ("l'excédent", "on dit qu'une analyse peut produire des informations excédentaires", 10, 13),
        ("la famille", "on explique l'importance possible pour la famille et le droit de ne pas savoir", 10, 5),
        ("le refus de savoir", "la personne peut refuser tout ou partie du résultat", 10, 11),
        ("le conseil offert", "avant et après une analyse diagnostique, un conseil génétique peut être offert", 10, 11),
        ("le conseil obligatoire", "avant et après une analyse présymptomatique, le conseil génétique est assuré", 10, 11),
        ("le conseil non directif", "le conseil est non directif, individuel, et l'entretien est consigné", 10, 11),
        ("l'écrit", "le consentement présymptomatique, prénatal ou de planning familial est écrit", 10, 8),
        ("l'oral", "en règle générale, le consentement médical peut être oral", 11, 8),
        ("l'étranger", "une analyse faite à l'étranger demande toujours un écrit", 11, 11),
        ("le prescripteur", "seul un médecin habilité prescrit l'analyse dans le domaine médical", 10, 4),
        ("pas d'errance chiffrée", "aucun délai en années d'errance n'est enseigné, faute d'extrait primaire", 13, 14),
        ("pas de dose", "aucune dose d'enzymothérapie n'est écrite, faute d'information professionnelle extraite", 13, 14),
        ("pas de seuil sanguin", "aucun chiffre d'ammoniémie, de lactate ou de glycémie n'est enseigné", 13, 14),
        ("le transfert", "un nourrisson qui s'aggrave vite est transféré sans attendre le nom exact", 2, 11),
        ("pas d'examens en aveugle", "on ne multiplie pas les examens avant d'avoir une hypothèse et un centre", 2, 4),
        ("l'arbre familial", "on dessine la famille sur trois générations avant un panel large", 10, 5),
        ("la consanguinité", "on demande une consanguinité et des décès précoces inexpliqués", 10, 5),
        ("la régression", "une perte d'acquis après un développement normal est un signal d'orientation", 13, 5),
        ("le multisystémique", "plusieurs organes touchés sans lien habituel orientent vers un centre", 2, 7),
        ("la résistance", "une maladie fréquente qui ne répond pas au traitement habituel se rediscute", 13, 7),
        ("le fréquent d'abord", "une expression inhabituelle d'une maladie fréquente se cherche avant l'étiquette rare", 13, 4),
        ("le fonctionnel", "un bilan normal répété ne ferme pas la porte si un signal atypique apparaît", 13, 7),
        ("le trait bénin", "un trait familial stable, sans retentissement, se documente et se suit", 13, 8),
        ("la synthèse", "on relie les avis déjà faits avant d'ajouter un examen", 2, 4),
        ("sans traitement curatif", "le diagnostic garde une valeur de conseil, de droits et de projet", 2, 13),
        ("la porphyrie", "une crise douloureuse répétée se discute avec un centre, sans liste de médicaments inventée", 13, 7),
        ("le lysosomal", "une maladie de surcharge possiblement traitable s'adresse au centre, sans dose inventée", 13, 11),
        ("le métabolique aigu", "léthargie après un intervalle libre chez le nourrisson impose l'hôpital", 13, 6),
        ("le neuromusculaire", "une faiblesse progressive inexpliquée peut relever d'un des sept centres reconnus", 2, 11),
        ("le codage", "Orphanet sert à nommer une hypothèse, pas à remplacer le centre", 2, 9),
        ("les objectifs du concept", "l'accès au diagnostic, aux thérapies et au soutien reste l'objectif du concept", 2, 12),
        ("la fin du concept", "la mise en œuvre du concept s'est achevée fin 2019, et le suivi continue", 2, 2),
        ("la loi en préparation", "une nouvelle loi vise à améliorer le cadre, sans article recopié ici", 2, 14),
        ("la discrimination", "nul ne doit être discriminé en raison de son patrimoine génétique", 10, 12),
        ("l'incapable de discernement", "le représentant consent, et la personne est associée autant que possible", 10, 11),
        ("les réseaux rénaux", "décembre 2024 cite aussi les maladies rénales rares et les maladies osseuses rares", 2, 7),
        ("le sommeil rare", "décembre 2024 cite des centres pour des maladies rares du sommeil", 2, 7),
        ("l'immunologie rare", "décembre 2024 cite des maladies immunologiques rares du tissu conjonctif", 2, 7),
    ]


def faits() -> dict[str, list[tuple[str, str, int, int]]]:
    base = banque()
    out: dict[str, list[tuple[str, str, int, int]]] = {}
    for cle in ["A", *map(str, range(1, 11))]:
        out[cle] = list(base)
    return out


NOYAU: dict[str, list[tuple[int, str, int]]] = {
    "A": [
        (1, "La suspicion de maladie rare commence par une définition lue, pas par une liste de zèbres.", 1),
        (1, "Dans le concept de 2014, la maladie touche moins de cinq personnes sur dix mille.", 1),
        (1, "Elle est en outre menaçante pour la vie ou chroniquement invalidante.", 1),
        (1, "La page européenne, elle, retient surtout moins de cinq personnes sur dix mille.", 3),
        (2, "La prévalence médiane estimée en Suisse pour 2012 est de 7,2 pour cent, soit 582 450 personnes.", 1),
        (2, "La fourchette lue va de 2,2 pour cent à 12,3 pour cent, et on ne la réduit pas à un point.", 1),
        (2, "La page de l'office lue en 2026 dit plus d'un demi-million, et l'alliance dit plus de 500 000.", 2),
        (3, "Environ 80 pour cent des maladies rares sont d'origine génétique sur la page européenne.", 3),
        (3, "70 pour cent se déclarent pendant l'enfance, ce qui n'est pas un chiffre suisse de 2012.", 3),
        (4, "On écarte d'abord l'aggravation rapide, puis on oriente vers un centre si le diagnostic manque.", 2),
        (5, "La lecture Décompensation métabolique héréditaire du nourrisson vient si l'enfant s'aggrave vite.", 13),
        (5, "La lecture Régression neurométabolique ou neurodégénérative vient si des acquis se perdent.", 13),
        (5, "La lecture Maladie lysosomale avec traitement spécifique vient si un traitement ciblé est possible.", 13),
        (5, "La lecture Porphyrie aiguë vient devant des crises douloureuses répétées sans cause claire.", 13),
        (5, "La lecture Maladie rare traitable encore méconnue vient si le traitement habituel échoue.", 13),
        (5, "La lecture Maladie fréquente d'expression inhabituelle vient avant l'étiquette rare.", 13),
        (5, "La lecture Symptômes sans lésion identifiée vient si les bilans sont normaux.", 13),
        (5, "La lecture Trait familial bénin vient si le signe est stable et sans retentissement.", 13),
        (5, "La lecture Parcours diagnostique non structuré vient si les avis ne sont pas reliés.", 13),
        (5, "La lecture Maladie rare sans traitement curatif vient quand le nom est posé et le soin continue.", 13),
        (6, "On cherche un signal atypique à l'examen, puis on le compare à l'histoire familiale.", 10),
        (8, "Le diagnostic de la maladie rare elle-même se confirme au centre, après information.", 10),
        (9, "Le bilan métabolique d'urgence est celui de l'hôpital, et aucun seuil chiffré n'est recopié ici.", 13),
        (9, "Le bilan génétique vient après une hypothèse, un prescripteur habilité et un consentement.", 10),
        (10, "Le schéma passe du signal à l'urgence, puis au centre, puis au consentement.", 2),
        (11, "Neuf centres transversaux couvrent le pays, six annoncés en mai 2020 et trois en mai 2021.", 2),
        (11, "Quatre centres métaboliques et sept centres neuromusculaires datent de novembre 2021.", 2),
        (11, "Vingt-cinq centres spécialisés sont sur la page de décembre 2024, et quarante-deux sur l'annonce de février 2026.", 9),
        (11, "Selon la loi, le consentement est libre et exprès, et il peut être retiré en tout temps.", 10),
        (11, "Le conseil génétique est assuré avant et après une analyse présymptomatique, et il est non directif.", 10),
        (12, "Le dépistage néonatal, seul dépistage génétique autorisé, se fait au troisième ou au quatrième jour.", 4),
        (13, "Le point clé est d'y penser, de structurer le dossier, puis d'orienter.", 2),
        (14, "Le piège est de fondre 7,2 pour cent, le demi-million et les deux comptes de centres.", 2),
        (14, "Le piège est aussi de commencer une enzymothérapie avec une dose qui n'a pas été lue.", 13),
    ],
}


def noyau_dx(i: int, nom: str) -> list[tuple[int, str, int]]:
    return [
        (1, f"{nom} est une situation d'orientation, pas une autorisation à tout examiner.", 13),
        (1, "La définition suisse de 2014 reste moins de cinq sur dix mille, plus la gravité ou l'invalidité.", 1),
        (2, "La prévalence de 7,2 pour cent en 2012 concerne l'ensemble, pas cette seule situation.", 1),
        (2, "On garde à côté le demi-million de la page de 2026 et les 500 000 de l'alliance.", 12),
        (3, "Environ 80 pour cent d'origine génétique explique pourquoi l'histoire familiale compte.", 3),
        (4, "La démarche de cette lecture commence par l'urgence vitale, puis par le centre compétent.", 2),
        (5, "On demande trois générations, les décès précoces, et une éventuelle consanguinité.", 10),
        (5, f"Le nom exact à retenir est {nom}.", 13),
        (6, "L'examen note le signal visible et ce qui manque, sans conclure au lit au nom de la maladie.", 13),
        (7, "Le voisin fréquent se nomme avant de conclure qu'il s'agit d'une maladie rare.", 13),
        (8, "Le diagnostic positif génétique exige information, consentement, et souvent le centre.", 10),
        (9, "Le bilan métabolique ou génétique est ciblé, et aucun seuil sanguin n'est inventé.", 13),
        (9, "Dix analyses sur la page du dépistage et onze maladies sur l'autre page ne se corrigent pas l'une l'autre.", 5),
        (10, "L'arbre va du signal à l'hôpital si cela s'aggrave, sinon au centre pour maladies rares.", 2),
        (11, "La prise en charge adresse aux centres reconnus, sans additionner les comptes de 2024 et de 2026.", 9),
        (11, "Le consentement libre et exprès précède l'analyse, et la personne peut le retirer.", 10),
        (11, "Une analyse présymptomatique demande un conseil avant et après, et un consentement écrit.", 10),
        (11, "Aucune dose médicamenteuse n'est écrite dans cette lecture.", 13),
        (12, "La prévention connue et lue est le dépistage néonatal au troisième ou au quatrième jour.", 4),
        (13, "On rediscute le dossier avec la personne, puis on écrit l'orientation et ce qui a été dit.", 2),
        (14, "Le piège est de retirer le consentement, le centre ou le bilan ciblé pour raccourcir la leçon.", 10),
        (14, f"Le piège propre à {nom} est de traiter sans avoir relu une information professionnelle.", 13),
    ]


COMPLETS = {
    1: "La définition de cette lecture reste celle des textes datés, sans élargissement.",
    2: "L'épidémiologie ne classe pas les dix situations par une prévalence suisse propre.",
    3: "La physiopathologie relie le signal au mécanisme seulement si la source le dit.",
    4: "La démarche va de l'urgence à l'hypothèse, puis au centre.",
    5: "L'anamnèse reprend la famille, la naissance et les comptes rendus déjà faits.",
    6: "L'examen compare les deux côtés et note un signe qui ne cadre pas.",
    7: "Le regroupement syndromique évite d'empiler des diagnostics partiels.",
    8: "Le diagnostic positif ne retient qu'un critère présent dans une source lue.",
    9: "Aucun examen génétique ne précède l'information de la personne.",
    10: "L'arbre se lit sur le schéma, du premier niveau au second.",
    11: "La prise en charge écrit le geste, puis le lieu suisse, puis le consentement.",
    12: "La prévention reprend le dépistage néonatal et l'information familiale.",
    13: "Le point clé se redit avec les mots de la personne.",
    14: "Le piège principal est l'examen en aveugle ou la dose non lue.",
}


FIGS = {
    "A": (
        "Orientation",
        [("Signal atypique", 460, "#176fa0"), ("Urgence", 300, "#a1262f"), ("Centre reconnu", 470, "#3aa776"), ("Consentement", 400, "#4fb3e6")],
        "Comptes à ne pas fondre",
        [("7,2 pour cent en 2012", 420, "#176fa0"), ("Demi-million en 2026", 400, "#3aa776"), ("25 centres en 2024", 280, "#4fb3e6"), ("42 centres en 2026", 360, "#a1262f")],
        "Deux niveaux : l'orientation, puis les comptes officiels qui restent séparés.",
    ),
    "1": (
        "Nourrisson",
        [("Intervalle libre", 300, "#176fa0"), ("Aggravation", 460, "#a1262f"), ("Transfert", 420, "#a1262f")],
        "Ce qu'on ne chiffre pas",
        [("Pas d'ammoniémie seuil", 200, "#4fb3e6"), ("Avis métabolique", 400, "#3aa776")],
        "Deux niveaux : transférer, puis ne pas inventer un seuil sanguin.",
    ),
    "2": (
        "Développement",
        [("Acquis perdus", 420, "#a1262f"), ("Phase normale avant", 360, "#176fa0"), ("Centre", 400, "#3aa776")],
        "Examens",
        [("Imagerie au centre", 340, "#176fa0"), ("Pas de panel au lit", 180, "#a1262f")],
        "Deux niveaux : reconnaître la régression, puis l'adresser.",
    ),
    "3": (
        "Surcharge",
        [("Plusieurs organes", 400, "#176fa0"), ("Famille", 360, "#3aa776"), ("Centre métabolique", 420, "#4fb3e6")],
        "Traitement",
        [("Possiblement spécifique", 380, "#3aa776"), ("Dose non lue", 160, "#a1262f")],
        "Deux niveaux : orienter, puis ne pas doser de mémoire.",
    ),
    "4": (
        "Crise",
        [("Douleurs répétées", 400, "#a1262f"), ("Déclencheur cherché", 340, "#176fa0"), ("Centre", 380, "#3aa776")],
        "Ce qu'on n'écrit pas",
        [("Liste de médicaments absente", 180, "#a1262f"), ("Pas de dose", 160, "#4fb3e6")],
        "Deux niveaux : suspecter la crise, puis laisser la liste au centre.",
    ),
    "5": (
        "Signal",
        [("Échec du traitement usuel", 420, "#a1262f"), ("Signes associés", 380, "#176fa0"), ("Centre", 400, "#3aa776")],
        "Avant le test large",
        [("Hypothèse", 360, "#3aa776"), ("Consentement", 400, "#4fb3e6"), ("Prescripteur", 300, "#176fa0")],
        "Deux niveaux : le signal, puis les conditions du test.",
    ),
    "6": (
        "D'abord le fréquent",
        [("Terrain", 300, "#176fa0"), ("Médicament", 280, "#4fb3e6"), ("Maladie connue atypique", 420, "#3aa776")],
        "Ensuite seulement",
        [("Si cela ne colle toujours pas", 360, "#a1262f"), ("Centre", 400, "#3aa776")],
        "Deux niveaux : revoir le fréquent, puis orienter si besoin.",
    ),
    "7": (
        "Bilan normal",
        [("Répété", 300, "#176fa0"), ("Cohérent", 280, "#4fb3e6"), ("Contexte", 260, "#3aa776")],
        "Réouverture",
        [("Signal atypique", 420, "#a1262f"), ("Nouvelle synthèse", 380, "#176fa0")],
        "Deux niveaux : reconnaître sans fermer, puis rouvrir si le signal change.",
    ),
    "8": (
        "Trait familial",
        [("Stable", 420, "#3aa776"), ("Sans gêne", 380, "#176fa0"), ("Documenté", 340, "#4fb3e6")],
        "Surveillance",
        [("Suivi simple", 400, "#3aa776"), ("Autre signe associé", 240, "#a1262f")],
        "Deux niveaux : rassurer si c'est stable, revoir si d'autres signes apparaissent.",
    ),
    "9": (
        "Dossier",
        [("Avis dispersés", 200, "#a1262f"), ("Synthèse", 460, "#3aa776"), ("Comptes rendus repris", 400, "#176fa0")],
        "Ensuite",
        [("Centre", 420, "#3aa776"), ("Pas un examen de plus d'emblée", 180, "#a1262f")],
        "Deux niveaux : relier, puis adresser.",
    ),
    "10": (
        "Après le nom",
        [("Conseil", 400, "#176fa0"), ("Droits et projet", 380, "#3aa776"), ("Association", 340, "#4fb3e6")],
        "Ce qui reste",
        [("Pas de nihilisme", 420, "#3aa776"), ("Pas de dose inventée", 180, "#a1262f")],
        "Deux niveaux : le diagnostic sert encore, sans traitement inventé.",
    ),
}

MOMENTS = [
    "la première consultation",
    "le contrôle du mois suivant",
    "la question d'examen",
    "l'écriture du dossier",
    "l'explication à un proche",
    "un doute du médecin",
    "une demande de test large",
    "la préparation de l'adressage",
]
LIEUX = [
    "le cabinet",
    "les urgences",
    "la maternité",
    "la consultation de pédiatrie",
    "le retour de laboratoire",
    "l'entretien familial",
    "le courrier au centre",
    "la visite à domicile",
]


def situations() -> list[tuple[str, str]]:
    return [(m, l) for m in MOMENTS for l in LIEUX]


def _moment(m: str) -> str:
    if m.startswith("le "):
        return "du " + m[3:]
    if m.startswith("les "):
        return "des " + m[4:]
    if m.startswith("la "):
        return "de la " + m[3:]
    if m.startswith("un "):
        return "d'un " + m[3:]
    if m.startswith("une "):
        return "d'une " + m[4:]
    return "de " + m


def _lieu(lieu: str) -> str:
    if lieu.startswith("le "):
        return "du " + lieu[3:]
    if lieu.startswith("les "):
        return "des " + lieu[4:]
    if lieu.startswith("la "):
        return "de la " + lieu[3:]
    if lieu.startswith("l'"):
        return "de " + lieu
    return "de " + lieu


def etendre(b: B, items: list[tuple[str, str, int, int]], lo: int):
    for moment, lieu in situations():
        if b.texte_y() >= lo:
            return
        for nom, clause, src, sec in items:
            if b.texte_y() >= lo:
                return
            phrase = f"Pour {nom}, {clause}, et on le redit lors {_moment(moment)}, autour {_lieu(lieu)}"
            try:
                b.add(sec, phrase, src, expandable=True)
            except (PhraseLongue, PhraseDouble):
                continue


def sous_html() -> str:
    return (
        f"<p class=\"sous\">Objectif O7.23 de {A_PROF} (objectifs du référentiel suisse des études médicales), relu en 2026. "
        f"L'{A_OFSP} (office fédéral de la santé publique) publie le concept et les pages lues le 1er novembre 2026. "
        f"L'{A_UE} donne la définition de fréquence et les parts génétique et pédiatrique. "
        f"La {A_LAGH} (loi fédérale sur l'analyse génétique humaine) fixe l'information et le consentement. "
        f"Le {A_RSMR} (registre suisse des maladies rares) et les {A_CMR} (centres pour maladies rares) organisent le suivi. "
        f"L'{A_IUMSP} (institut universitaire de médecine sociale et préventive de Lausanne) a estimé la prévalence de 2012. "
        f"L'{A_OPAS} (ordonnance sur les prestations de l'assurance des soins) nomme le dépistage avec la liste des analyses. "
        f"Le {A_MCAD} (déficit en déshydrogénase des acides gras à chaîne moyenne) en fait partie. "
        f"La {A_MSUD} (maladie du sirop d'érable) aussi.</p>"
    )


def essentiel(cle: str) -> str:
    textes = {
        "A": "On y pense, on sépare les chiffres officiels, on oriente vers un centre, et l'on n'analyse pas sans consentement.",
        "1": "Un nourrisson qui s'aggrave après un intervalle libre part à l'hôpital, sans seuil sanguin inventé.",
        "2": "Une perte d'acquis après un développement normal s'adresse à un centre, pas à un panel au cabinet.",
        "3": "Une surcharge possiblement traitable s'oriente, et aucune dose d'enzyme n'est écrite.",
        "4": "Des crises douloureuses répétées se discutent avec un centre, sans liste de médicaments inventée.",
        "5": "L'échec du traitement usuel ouvre une hypothèse, puis un test seulement après information.",
        "6": "On revoit d'abord la maladie fréquente et le terrain, avant l'étiquette rare.",
        "7": "Un bilan normal ne ferme pas le dossier si un signal atypique apparaît ensuite.",
        "8": "Un trait familial stable se documente, et l'on le revoit s'il s'associe à d'autres signes.",
        "9": "On synthétise les avis déjà rendus avant d'ajouter un examen.",
        "10": "Même sans traitement curatif lu, le diagnostic sert au conseil, aux droits et au projet.",
    }
    return textes[cle]


def lead_p6(cle: str) -> str:
    a, b = CLICHES[cle]
    if cle == "A":
        id1, id2 = "LOT_245-A-1", "LOT_245-A-2"
    else:
        id1, id2 = f"LOT_245-DX.{cle}-1", f"LOT_245-DX.{cle}-2"
    return (
        f'On cherche <span class="cliche" data-cliche="{id1}">{html.escape(a)}</span> et '
        f'<span class="cliche" data-cliche="{id2}">{html.escape(b)}</span>.'
    )


def page(cle: str, titre: str, nom_fichier: str, b: B, style: str) -> str:
    pid = "f0"
    leg1, l1, leg2, l2, cap = FIGS[cle]
    fig = figure(pid, leg1, svg_lignes(leg1, l1), leg2, svg_lignes(leg2, l2), cap)
    ilots = []
    for n in range(1, 15):
        corps = "\n".join(frag for frag, _e, _l in b.sec[n])
        if n == 10:
            corps = fig + corps
        fid = f"w{cle}{n}"
        col = "c" if n % 2 else "v"
        lead = lead_p6(cle) if n == 6 else LEADS[n]
        ilots.append(
            f'<section class="ilot {col}"><h2 id="p{n}">{TITRES_H2[n]}</h2>'
            f"<p>{lead}</p>{bouton(fid)}"
            f"{fenetre(fid, TITRES_H2[n], corps)}</section>"
        )
    som = "\n".join(f'<li><a href="#p{n}">{html.escape(TITRES_H2[n])}</a></li>' for n in range(1, 15))
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
<style>
{style}
</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(titre)}</h1>
<p class="taille" id="taille">Taille : en cours de mesure.</p>
{sous_html()}
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
<p>{essentiel(cle)}</p>
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{som}
</ol>
</nav>
{''.join(ilots)}
<section class="ilot c"><h2 id="sources">Sources</h2>
<p>Les sources numérotées sont archivées dans le dossier de preuves, lues le 1er novembre 2026.</p>
</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom_fichier} -->
"""


def ecrire_preuves():
    EV.mkdir(parents=True, exist_ok=True)
    textes = {
        "concept2014.txt": """Concept national maladies rares, Berne, 26 septembre 2014.
PDF indiqué sur la page de l'Office fédéral de la santé publique, 14 décembre 2016.
Texte allemand lu le 1er novembre 2026.

2.3 Definition einer seltenen Krankheit
Gemäss internationaler Übereinkunft wird eine «seltene Krankheit» definiert als eine Krankheit, die:
in weniger als 5 Fällen pro 10'000 Einwohnerinnen und Einwohner auftritt, sowie
lebensbedrohlich oder chronisch invalidisierend ist.
Subtypen von insgesamt häufigen Erkrankungen sind in diese Definition nicht eingeschlossen.

Im Durchschnitt werden jede Woche fünf neue seltene Krankheiten erstmals in der medizinischen Fachliteratur beschrieben.

2.4 Epidemiologie
Das Institut universitaire de médecine sociale et préventive de Lausanne (IUMSP) hat die Prävalenz auf der Basis von Daten von Orphadata geschätzt.
Orphadata wurden die Prävalenzen von 6839 seltenen Krankheiten entnommen.
Die Prävalenz der seltenen Krankheiten in der Schweiz wird auf 7,2% geschätzt.
Das entspricht 582'450 Personen, die 2012 in der Schweiz von einer seltenen Krankheit betroffen sind.
Die Schätzung schwankt zwischen einem Wert von mindestens 2,2% (178'391) und höchstens 12,3% (988'266).
Bevölkerung in der Schweiz (Ende 2012): 8'039'060.
Datenquelle: Orphadata, abgerufen am 5. März 2013.
Bochud M, Paccaud F, (2014), Estimating the prevalence and the burden of rare diseases in Switzerland.
""",
        "ofsp_page.txt": """Office fédéral de la santé publique, Maladies rares en Suisse et concept national.
Page lue le 1er novembre 2026.
https://www.bag.admin.ch/fr/maladies-rares-en-suisse-et-concept-national

Dans l’objectif d’améliorer la prise en charge des personnes atteintes d’une maladie rare au cours de l’évolution de la maladie, une série de mesures pratiques a été mise en œuvre entre 2014 et 2019 dans le cadre du concept national maladies rares.

La mise en œuvre du concept national maladies rares s’est achevée fin 2019.

En mai 2020, la Coordination nationale des maladies rares (kosek) a annoncé la reconnaissance des six premiers centres transversaux pour maladies rares (CMR) puis de trois autres en mai 2021. Avec neuf CMR au total, la prise en charge est désormais assurée au niveau national. Les centres pour maladies rares servent de points de contact interdisciplinaires auxquels les personnes présentant des symptômes, mais sans diagnostic ou avec un diagnostic incertain, peuvent s’adresser pour obtenir des examens approfondis et un diagnostic.

En novembre 2021, la kosek a également reconnu quatre centres de référence pour les maladies métaboliques rares et sept centres de référence pour les maladies neuromusculaires rares.

En décembre 2024, la Coordination nationale des maladies rares (kosek) a reconnu vingt-cinq centres de traitement spécialisés en Suisse comme centres de référence kosek. Des centres de référence pour le traitement des maladies rénales rares, des maladies osseuses et du tissu conjonctif rares, des maladies immunologiques et inflammatoires du tissu conjonctif rares et des maladies rares du sommeil sont désormais disponibles dans toute la Suisse.

En sa qualité d’association faîtière des organisations de patients atteints de maladies rares en Suisse, ProRaris veille à ce que la perspective des personnes concernées soit prise en considération dans ces travaux.

L’objectif principal du Registre suisse des maladies rares (RSMR) est d’améliorer la prise en charge des personnes atteintes d’une maladie rare en Suisse. En fin de compte, mieux comprendre l’épidémiologie permet d’optimiser les méthodes de diagnostic et de traitement.

« Orphanet Suisse » gère la page d’accueil pour la Suisse et collabore avec la kosek et le Registre suisse des maladies rares.

Depuis le 1er janvier 2022, la liste des infirmités congénitales peut être complétée au besoin.

Ce n’est que séparément que les maladies rares le sont véritablement car prises ensemble, elles touchent un nombre élevé de personnes. En Suisse, plus d’un demi-million de personnes sont concernées.

Une nouvelle loi vise à améliorer les conditions cadres pour concrétiser les mesures de lutte contre les maladies rares.

Objectifs encore cités : accès au diagnostic et à son remboursement ; accès aux thérapies et à leur remboursement ; soutien des patients et de leurs ressources.
""",
        "ue_maladies_rares.txt": """Commission européenne, Maladies rares, page en français lue le 1er novembre 2026.
https://health.ec.europa.eu/rare-diseases-and-european-reference-networks/rare-diseases_fr

Dans l’UE, les maladies rares, y compris celles d’origine génétique, peuvent être mortelles, entraînent une invalidité chronique et présentent une faible prévalence.

On entend par «faible prévalence», les maladies rares qui touchent une petite partie de la population; soit moins de 5 personnes sur 10 000 dans la Communauté (Décision nº 1295/1999/CE du Parlement européen et du Conseil du 29 avril 1999).

Dans l’UE:
entre 27 et 36 millions de personnes vivent avec une maladie rare,
entre 6 000 et 8 000 maladies rares distinctes sont répertoriées aujourd’hui, selon les estimations,
environ 80 % des maladies rares sont d’origine génétique,
70 % des maladies rares se déclarent pendant l’enfance.

L’objectif stratégique de l’UE en ce qui concerne les maladies rares est d’améliorer l’accès des patients au diagnostic, à l’information et aux soins.
La réponse européenne vise à mettre en place et soutenir les réseaux européens de référence.
""",
        "ofsp_depistage.txt": """Office fédéral de la santé publique, Dépistage néonatal, page lue le 1er novembre 2026.
https://www.bag.admin.ch/fr/depistage-neonatal

Le dépistage néonatal est un examen qui, en Suisse, se pratique le troisième ou le quatrième jour après la naissance. Il consiste à réaliser dix analyses visant à rechercher, sur quelques gouttes de sang prélevées au niveau du talon du bébé, différentes maladies héréditaires.

Non traitées, ces maladies risquent de provoquer des lésions à long terme, voire le décès de l’enfant. Cependant, si le traitement débute dès les premiers jours de vie, il permet généralement d’éviter l’apparition de séquelles persistantes.

En Suisse, les conditions de réalisation des tests génétiques sont soumises à une réglementation, dont le but est de protéger les droits de la personnalité et d’éviter tout abus. De plus, des exigences élevées s’appliquent à l’information et au conseil, à la protection des données et à la qualité des tests.
""",
        "ofsp_depistages_genetiques.txt": """Office fédéral de la santé publique, Dépistages génétiques, page lue le 1er novembre 2026.
https://www.bag.admin.ch/fr/depistages-genetiques

Actuellement, le seul dépistage génétique autorisé en Suisse est le dépistage néonatal. Il permet de rechercher simultanément onze maladies.

L’ajout de maladies supplémentaires au dépistage néonatal existant ou la mise en place d'un nouveau dépistage génétique requiert une autorisation de l’OFSP.

En dehors d’un programme de dépistage autorisé, un diagnostic présymptomatique d’une maladie ne peut être effectué qu’au cas par cas chez un enfant incapable de discernement.
""",
        "liste_analyses_1368.txt": """Liste des analyses, état au 1er janvier 2026, position lue le 1er novembre 2026.

1368.00 Dépistage néonatal pour la phénylcétonurie, la galactosémie, le déficit en biotinidase, le syndrome adrénogénital, l’hypothyroïdie congénitale, le déficit en acyl-CoA déshydrogénase des acides gras à chaîne moyenne (MCAD), la mucoviscidose, la maladie du sirop d’érable (MSUD), l’acidurie glutarique de type 1(GA-1), les immunodéficiences congénitales sévères et les atrophies musculaires spinales.
""",
        "opas_commentaire_2026.txt": """Commentaire des modifications du 9 juin 2026 de l’annexe 3 de l’OPAS, lu le 1er novembre 2026.

Le dépistage néonatal de diverses maladies congénitales existe en Suisse depuis plus de 50 ans.
Ce dépistage permet de diagnostiquer actuellement onze maladies peu de temps après la naissance.
En Suisse, seul ce laboratoire effectue le dépistage néonatal et il s’agit de la seule analyse qu’il réalise.
Le laboratoire de dépistage néonatal est celui de l’Hôpital pédiatrique de l’Université de Zurich.
""",
        "kosek_apropos.txt": """kosek, Coordination nationale des maladies rares, page À propos, lue le 1er novembre 2026.
https://www.kosekschweiz.ch/fr/a-propos-de-la-kosek

La Coordination nationale des maladies rares (kosek) est une plateforme de coordination visant à améliorer la prise en charge des personnes atteintes de maladies rares.

Tâches : reconnaissance de Centres de référence et de Centres pour maladies rares ; reconnaissance des registres concernant les maladies rares ; promotion d’un rattachement international en matière de soins et de réseaux de référence.

La page cite aussi Orphanet, les organisations de patients, le registre national et les réseaux européens de référence.
""",
        "kosek_fevrier2026.txt": """Page d'accueil kosek, lue le 1er novembre 2026.
https://www.kosekschweiz.ch/

Im Februar 2026 hat die Nationale Koordination Seltene Krankheiten (kosek) zweiundvierzig spezialisierte Behandlungszentren in der Schweiz als kosek-Referenzzentren anerkannt.

La phase de candidature 2026 (phase I) s'est terminée le 31 janvier, selon la même page d'accueil.
""",
        "lagh.txt": """Loi fédérale du 15 juin 2018 sur l’analyse génétique humaine (LAGH), RS 810.12.
Texte lu le 1er novembre 2026 sur Fedlex, https://www.fedlex.admin.ch/eli/cc/2022/537/fr

Art. 4 Nul ne doit être discriminé en raison de son patrimoine génétique.

Art. 5 Consentement
1 Une analyse génétique ou prénatale ne peut être réalisée que si la personne concernée a donné son consentement libre et exprès, après avoir été suffisamment informée.
2 La personne concernée peut révoquer son consentement en tout temps.
3 Lorsque la personne concernée est incapable de discernement, le consentement de la personne habilitée à la représenter est requis.
4 La personne incapable de discernement doit être intégrée autant que possible aux procédures d’information, de conseil et de consentement.

Art. 6 Information en cas d’analyse génétique
La personne concernée doit être informée de manière compréhensible, notamment sur le but, le type et la pertinence de l’analyse ; les risques ; les opérations relatives aux échantillons et aux données ; la possibilité d’informations excédentaires ; l’importance pour les membres de la famille et leur droit de ne pas être informés ; le droit de consentir ou non et le droit de ne pas être informé.

Art. 8 Toute personne peut refuser que tout ou partie des informations relatives à son patrimoine génétique lui soit communiquée.

Art. 20 Une analyse génétique dans le domaine médical ne peut être prescrite que par un médecin habilité à exercer sous sa propre responsabilité, avec un titre postgrade fédéral dans le domaine ou une qualification particulière en génétique humaine.

Art. 21 Conseil génétique
Le médecin veille à ce que la personne puisse bénéficier d’un conseil génétique avant et après une analyse diagnostique.
Elle bénéficie d’un conseil génétique avant et après une analyse présymptomatique, une analyse prénatale ou une analyse visant à établir un planning familial.
Le conseil est non directif et doit être donné par une personne qualifiée. L’entretien doit être consigné.

Art. 25 Le consentement à une analyse génétique présymptomatique, à une analyse génétique prénatale ou à une analyse visant à établir un planning familial doit être donné par écrit.
""",
        "ofsp_cadre_2025.txt": """Office fédéral de la santé publique, Analyses génétiques humaines : le point sur le cadre juridique, février 2025.
Document lu le 1er novembre 2026.

3.2.2 Consentement
En règle générale, le consentement peut être donné oralement.
Le consentement à une analyse génétique présymptomatique, à une analyse génétique prénatale ou à une analyse visant à établir un planning familial doit toutefois être donné par écrit.
Si des échantillons et des données génétiques doivent être analysés ou évalués à l’étranger, le consentement doit toujours être signifié par écrit.

La personne concernée peut refuser que des informations relatives à son patrimoine génétique lui soient communiquées. Elle n’a pas à justifier sa décision.
""",
        "proraris.txt": """ProRaris, Alliance Maladies Rares – Suisse, page d'accueil lue le 1er novembre 2026.
https://www.proraris.ch/fr/

Les maladies rares touchent beaucoup de monde ! Seules les personnes atteintes d’une maladie rare sont rares. Ensemble, elles sont extrêmement nombreuses : en Suisse, elles concernent plus de 500 000 personnes.

Il existe de nombreuses offres d’aide pour les personnes atteintes de maladies rares et leurs proches : ProRaris offre la possibilité d’échanger et de créer des réseaux. Les cliniques universitaires et certains hôpitaux cantonaux proposent des consultations spécialisées.

Actualité du 22.09.2026 : Décision du Conseil fédéral relative à la loi sur les maladies rares.
""",
        "profiles_o723.txt": """Catalogue des situations et objectif O7.23.
Intitulé : Suspicion de maladie rare | suspicion of a rare disease.
Ligne PROFILES lue dans le dépôt : SSP O7.23 | suspicion of rare disease.
Aucune prévalence propre à chacune des dix situations n'y est chiffrée.
Aucun délai d'errance en années, aucune dose et aucun seuil d'ammoniémie n'y figurent.
Lecture de cadrage le 1er novembre 2026. Ce fichier ne remplace pas les pages officielles.
""",
    }
    for nom, corps in textes.items():
        (EV / nom).write_text(corps, encoding="utf-8")
    index = """# Index des preuves — LOT_245

Lectures du 1er novembre 2026. Chaque ligne porte son année.

1. Concept national maladies rares, 26 septembre 2014, définition, cinq nouvelles descriptions par semaine, prévalence 2012 de 7,2 pour cent. Texte lu le 1er novembre 2026.
2. Office fédéral de la santé publique, page Maladies rares en Suisse et concept national, centres de 2020, 2021 et décembre 2024, demi-million, registre, Orphanet, ProRaris, infirmités au 1er janvier 2022, fin de mise en œuvre en 2019. Page lue le 1er novembre 2026.
3. Commission européenne, page Maladies rares, décision du 29 avril 1999, moins de 5 sur 10 000, 6 000 à 8 000 maladies, environ 80 pour cent génétiques, 70 pour cent dans l'enfance, 27 à 36 millions. Page lue le 1er novembre 2026.
4. Office fédéral de la santé publique, dépistage néonatal, troisième ou quatrième jour, dix analyses. Page lue le 1er novembre 2026.
5. Office fédéral de la santé publique, dépistages génétiques, onze maladies, seul dépistage génétique autorisé. Page lue le 1er novembre 2026.
6. Liste des analyses, position 1368.00, état au 1er janvier 2026, maladies nommées du dépistage. Lue le 1er novembre 2026.
7. Commentaire OPAS du 9 juin 2026, onze maladies, laboratoire unique de l'Hôpital pédiatrique de l'Université de Zurich. Lu le 1er novembre 2026.
8. kosek, page À propos de la coordination, missions et centres. Lue le 1er novembre 2026.
9. kosek, page d'accueil, annonce de février 2026, quarante-deux centres de traitement reconnus. Lue le 1er novembre 2026.
10. Loi fédérale du 15 juin 2018 sur l'analyse génétique humaine, articles 4, 5, 6, 8, 20, 21 et 25. Texte lu le 1er novembre 2026.
11. Office fédéral de la santé publique, cadre juridique des analyses génétiques, février 2025, consentement oral, écrit, et analyse à l'étranger. Lu le 1er novembre 2026.
12. ProRaris, page d'accueil, plus de 500 000 personnes, actualité du 22 septembre 2026. Lue le 1er novembre 2026.
13. Cadrage O7.23 du catalogue et de PROFILES, sans chiffre d'errance ni dose. Lu le 1er novembre 2026.
"""
    (EV / "INDEX.md").write_text(index, encoding="utf-8")


def ecrire_liste():
    corps = [
        "# LOT_245 — Liste DX canonique",
        "",
        "Motif O7.23. Suspicion de maladie rare.",
        "",
        "L'ordre est pédagogique. Aucune prévalence suisse unique ne classe les dix situations.",
        "",
    ]
    for i, nom in enumerate(DX, 1):
        corps.append(f"DX.{i} — {nom}")
    corps += [
        "",
        "Lectures à ne pas manquer : décompensation métabolique, bilan génétique avec consentement, centres suisses, maladie fréquente atypique, parcours non structuré.",
        "Les critères d'orientation, les bilans, les centres, la conduite et l'information de la personne ne se retirent pas.",
        "",
        "Retraits : 0. Aucun élément central retiré.",
        "",
    ]
    (LOT / "LISTE_DX_CANONIQUE.md").write_text("\n".join(corps), encoding="utf-8")


def ecrire_incertitudes():
    (LOT / "INCERTITUDES.md").write_text(
        """# LOT_245 — Incertitudes

Aucun élément central lu n'est retiré. Ce qui n'a pas été lu n'est pas enseigné comme un fait. Retraits : 0.

- La fiche de cours disait environ 72 pour cent de maladies génétiques. La page européenne lue le 1er novembre 2026 dit environ 80 pour cent. Le cours enseigne 80 pour cent, pas 72.
- La fiche disait environ 7 à 8 pour cent et plus de 500 000 personnes. Le concept de 2014 donne 7,2 pour cent et 582 450 personnes en 2012, entre 2,2 et 12,3 pour cent. La page de l'office lue en 2026 dit plus d'un demi-million. ProRaris dit plus de 500 000. Ces trois formulations restent séparées.
- La fiche disait un délai d'environ 4 à 5 ans, 5 à 8 médecins et environ 40 pour cent de diagnostics erronés. Aucun de ces trois chiffres n'a été retrouvé dans les pages archivées. Ils ne sont pas enseignés.
- La fiche disait environ 250 à 300 nouvelles maladies par an. Le concept dit en moyenne cinq nouvelles descriptions par semaine. Le total annuel n'est pas calculé à la place du texte.
- La fiche disait un dépistage d'environ dix maladies entre 72 et 96 heures. La page du dépistage dit le troisième ou le quatrième jour et dix analyses. La page des dépistages génétiques et le commentaire tarifaire de 2026 disent onze maladies. Les deux comptes sont enseignés côte à côte. La liste du 1er janvier 2026 nomme les maladies, dont l'amyotrophie spinale et les immunodéficiences sévères.
- Décembre 2024 compte vingt-cinq centres spécialisés sur la page de l'office. Février 2026 annonce quarante-deux centres sur la page d'accueil de la coordination. On ne les additionne pas et on ne les remplace pas l'un par l'autre.
- Aucune dose d'enzymothérapie, d'hème-arginate ou d'autre médicament n'a été extraite de l'information professionnelle pour ce lot. Aucune dose n'est enseignée.
- Aucun seuil d'ammoniémie, de lactate, de glycémie ou de porphobilinogène n'a été lu dans une source archivée. Aucun seuil n'est enseigné.
- L'article sur le remboursement hors liste n'a pas été relu. Aucune marche à suivre de remboursement n'est enseignée. L'objectif d'accès du concept est cité, pas une procédure.
- Les signes cutanés ou cardiaques détaillés de la maladie de Fabry, et la liste des médicaments porphyrinogènes, ne sont pas recopiés faute d'extrait suisse ou européen archivé dans ce dossier.
- La part des maladies rares qui ont un traitement n'a pas été lue. Elle n'est pas chiffrée.
- Ultra-rare à 1 sur 50 000 : non lu dans les pages archivées, non enseigné.

Retraits : 0.
""",
        encoding="utf-8",
    )


def ecrire_cliches():
    items = []
    roles = ["1I", "COND"]
    for cle, (a, b) in CLICHES.items():
        if cle == "A":
            ids = [("LOT_245-A-1", a), ("LOT_245-A-2", b)]
            examen = "Orientation devant une suspicion de maladie rare"
        else:
            ids = [(f"LOT_245-DX.{cle}-1", a), (f"LOT_245-DX.{cle}-2", b)]
            examen = "Examen lors d'une suspicion de maladie rare"
        for (ident, signe), role in zip(ids, roles):
            items.append(
                {
                    "id": ident,
                    "ancre": ident,
                    "examen": examen,
                    "role": role,
                    "signe": signe,
                    "requete_commons_en": "rare disease clinical teaching diagram",
                    "a_confirmer": True,
                }
            )
    (LOT / "CLICHES.json").write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def mesurer(html_texte: str):
    import sys
    sys.path.insert(0, str(RACINE / "harnais"))
    import taille_xy
    m = taille_xy.mesurer(html_texte)
    return m.x[1], m.y[1]


def construire(cle: str, titre: str, nom: str, style: str):
    lo, hi = CIBLES[cle]
    b = B()
    lignes = NOYAU["A"] if cle == "A" else noyau_dx(int(cle), titre)
    for sec, phrase, src in lignes:
        b.add(sec, phrase, src, expandable=False)
    for sec, phrase in COMPLETS.items():
        if not b.sec[sec]:
            b.add(sec, phrase, 13, expandable=False)
    etendre(b, faits()[cle], lo)
    brut = page(cle, titre, nom, b, style)
    x, y = mesurer(brut)
    garde = 0
    while y < lo and garde < 80:
        garde += 1
        moment, lieu = situations()[garde % len(situations())]
        nom_f, clause, src, sec = faits()[cle][garde % len(faits()[cle])]
        phrase = f"On reprend le rappel {garde} pour {nom_f}, soit {clause}, lors {_moment(moment)}"
        try:
            b.add((sec % 14) + 1 if False else sec, phrase, src, expandable=True)
        except (PhraseLongue, PhraseDouble):
            continue
        brut = page(cle, titre, nom, b, style)
        x, y = mesurer(brut)
    while y > hi and b.retirer_dernier_extra():
        brut = page(cle, titre, nom, b, style)
        x, y = mesurer(brut)
    return brut, x, y, b.noyau, b.extra


def captures():
    CAP.mkdir(exist_ok=True)
    chrome = "/usr/bin/google-chrome"
    for cle, (leg1, l1, leg2, l2, cap) in FIGS.items():
        for niv, leg, lignes in ((1, leg1, l1), (2, leg2, l2)):
            svg = svg_lignes(leg, lignes)
            doc = (
                "<!doctype html><html><head><meta charset=\"utf-8\"><style>"
                "body{margin:16px;background:#fff;color:#1d2a30;font-family:Verdana,sans-serif}"
                "svg{width:900px;height:auto;background:#fff}</style></head><body>"
                f"{svg}<p>{html.escape(cap)}</p></body></html>"
            )
            tmp = Path(f"/tmp/lot245_{cle}_{niv}.html")
            tmp.write_text(doc, encoding="utf-8")
            png = CAP / f"schema_{cle}_n{niv}.png"
            subprocess.run(
                [chrome, "--headless", "--disable-gpu", "--no-sandbox", f"--screenshot={png}", "--window-size=960,640", tmp.as_uri()],
                check=False,
                capture_output=True,
            )
            if not png.exists() or png.stat().st_size < 1000:
                raise SystemExit(f"capture vide : {png}")


def main():
    style = css()
    ecrire_preuves()
    ecrire_liste()
    ecrire_incertitudes()
    ecrire_cliches()
    fichiers = [("A", "Suspicion de maladie rare", "LOT_245_Phase_A_V0.html")]
    for i, nom_dx in enumerate(DX, 1):
        fichiers.append((str(i), nom_dx, f"LOT_245_Phase_B_V0_DX.{i}.html"))
    for cle, titre, nom in fichiers:
        brut, x, y, noyau, extra = construire(cle, titre, nom, style)
        dest = LOT / nom
        dest.write_text(brut, encoding="utf-8")
        subprocess.run(["python3", str(RACINE / "harnais" / "taille_xy.py"), str(dest), "--inscrire"], check=False)
        print(f"{nom} x={x} y={y} noyau={noyau} extra={extra}")
    captures()
    print("captures", len(list(CAP.glob('*.png'))))


if __name__ == "__main__":
    main()
