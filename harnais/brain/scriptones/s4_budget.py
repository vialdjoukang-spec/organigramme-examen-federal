#!/usr/bin/env python3
"""Scriptone S4 · budget de lignes par point du plan (doléance 4 de Vial). Région AUL.
Budgets : budgets.json (point 2 « Épidémiologie » : 3 à 4 lignes affichées ; autres points mesurés pour calibrage).
  B1 point au-dessus de son budget de lignes            B4 point sous son budget minimal
  B2 chiffre épidémiologique sans source dans la phrase (exposant [Sn] ou parenthèse : « (OFS 2023) »)
  B3 pourcentage sans dénominateur (n = …, sur N, des N, pour 100 000…) — à ajouter s'il est connu
La correction est prescrite à l'agent avec l'INVENTAIRE des chiffres à conserver : réécrire plus dense, jamais retrancher une notion ;
un chiffre qui ne tient pas dans le budget va dans le tableau épidémiologique (en-têtes explicites, scriptone S8)."""
import json, math, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s4_budget", "AUL", "1.0.0"
B = json.loads((Path(__file__).resolve().parent / "budgets.json").read_text())
SRC = "⟦S⟧"
RX_CHIFFRE = re.compile(r"\d[\d  ,.]*\s?(?:%|‰|pour (?:1[0  ]*000|100)\b|cas\b|/ ?1[0  ]*000)", re.I)
RX_SOURCE = re.compile(r"%s|\((?:[^()]*\b(?:OFS|OFSP|Obsan|registre|étude|enquête|cohorte|OMS|WHO|ESC|EAACI|Lancet|NEJM|JAMA|BMJ)\b[^()]*|[^()]*\b(?:19|20)\d\d\b[^()]*)\)" % SRC)
RX_NOMBRE = re.compile(r"\d[\d  ]*(?:[,.]\d+)?(?:\s?(?:%|‰|°C|ans|cas|mois|jours|pour 1[0  ]*000|pour 100\b))?")
RX_DENOM = re.compile(r"(?i)n\s*=\s*\d|\bsur \d|\bdes \d|\bparmi\b|/\s*\d|pour (?:1[0  ]*000|100)\b|\d[\d  ]* (?:patients|cas|personnes|adultes|enfants|femmes|hommes|habitants|consultations|naissances)\b")


def _texte_src(inner):
    inner = re.sub(r'(?is)<sup class="r">.*?</sup>|(?:\s*\[S\d+\])+', " " + SRC + " ", inner)
    return bus.texte_visible(inner)


def lignes_point(t, a, f, cpl):
    """Lignes affichées du texte courant d'un point : <p> et <li> hors tableaux, fenêtres et arbre."""
    seg = t[a:f]; n = 0; blocs = []
    tabs = [(m.start() + a, m.end() + a) for m in re.finditer(r"(?is)<table\b.*?</table>|<div class=\"arb\".*?</div>(?=\s*<(?:p|div|table|h|details))", seg)]
    for pa, pf, inner in bus.blocs(t, a, f):
        if any(x <= pa < y for x, y in tabs) or re.search(r"(?i)<(?:p|li)\b", inner): continue
        tx = bus.texte_visible(inner)
        if tx: k = math.ceil(len(tx) / cpl); n += k; blocs.append((pa, tx, k))
    return n, blocs


def analyser(t, nom, opt=None):
    opt = opt or {}; cpl = opt.get("cpl", B["cpl"]); me = sys.modules[__name__]; D = []; M = {}
    S = bus.sections(t)
    for p, (a, f) in sorted(S.items()):
        n, blocs = lignes_point(t, a, f, cpl); M[f"lignes_point_{p}"] = n
        b = B["points"].get(str(p)) or {}
        if b.get("max") and n > b["max"]:
            chiffres = list(dict.fromkeys(x.group(0).strip() for _, tx, _ in blocs for x in RX_NOMBRE.finditer(tx)))
            D.append(bus.doleance(me, "B1", nom, bus.ancre(t, t.find(">", a) + 1, b.get("titre", "")), "GRAVE", f"point {p} ({b.get('titre', '')}) : {n} lignes affichées pour un budget de {b.get('min', 1)} à {b['max']}",
                                  f"réécrire le texte du point {p} en {b.get('min', 1)} à {b['max']} lignes de phrases verbales denses : chaque chiffre suivi de sa source entre parenthèses et de son dénominateur ; "
                                  f"tout chiffre qui ne tient pas passe dans le tableau du point (en-têtes explicites) ; aucun chiffre ni aucune notion supprimés. Chiffres à conserver : {', '.join(chiffres[:60]) or 'aucun'}",
                                  "agent", f"{len(blocs)} blocs, {n} lignes à {cpl} caractères"))
        elif b.get("min") and n < b["min"]:
            D.append(bus.doleance(me, "B4", nom, bus.ancre(t, t.find(">", a) + 1, b.get("titre", "")), "MOYEN", f"point {p} : {n} ligne(s), sous le budget minimal de {b['min']}",
                                  f"compléter le point {p} jusqu'à {b['min']} lignes (chiffres suisses sourcés, puis Europe)", "agent", f"{n} lignes"))
    if 2 in S:
        a, f = S[2]
        for pa, pf, inner in bus.blocs(t, a, f, ("p", "li")):
            if bus.dans_fenetre(t, pa): continue
            for ph in bus.phrases(_texte_src(inner)):
                if not RX_CHIFFRE.search(ph): continue
                propre = ph.replace(SRC, "").strip()
                if not RX_SOURCE.search(ph):
                    D.append(bus.doleance(me, "B2", nom, bus.ancre(t, pa, propre), "GRAVE", "chiffre épidémiologique sans source dans sa phrase",
                                          "ajouter la source lue (exposant [Sn] de la liste, ou parenthèse « (OFS 2023) ») ; à défaut écrire « À vérifier »", "agent", propre[:200]))
                if "%" in ph and not RX_DENOM.search(ph):
                    D.append(bus.doleance(me, "B3", nom, bus.ancre(t, pa, propre), "MOYEN", "pourcentage sans dénominateur",
                                          "ajouter le dénominateur s'il est connu (« 23,7 % des 439 patients », « n = 439 ») ; sinon laisser tel quel", "agent", propre[:200]))
    return D, M


def corriger(t, opt=None):
    return t


def _pt2(t):
    a, f = bus.sections(t)[2]; return a, f, [b for b in bus.blocs(t, a, f, ("p",)) if not bus.dans_fenetre(t, b[0])]
def _m_long(t, r):
    a, f, P = _pt2(t); q = P[-1][1] - 4
    ajout = " ".join(r.sample(["La fréquence augmente avec l'âge et culmine après 75 ans dans les cohortes européennes publiées.",
                                "Les hommes et les femmes sont touchés à parts presque égales selon la plupart des séries hospitalières.",
                                "Les données de soins primaires restent rares et leur qualité varie beaucoup d'un canton à l'autre.",
                                "Les hivers rigoureux et les vagues de chaleur modifient fortement la courbe annuelle des hospitalisations."], 3))
    return t[:q] + " " + ajout + t[q:]
def _m_source(t, r):
    a, f, P = _pt2(t); pa, pf, inner = P[0]; q = pf - 4
    return t[:q] + f" La prévalence atteint {r.randint(2, 40)},{r.randint(1, 9)} % chez les adultes de plus de 65 ans." + t[q:]
def _m_denom(t, r):
    a, f, P = _pt2(t); pa, pf, inner = P[0]; q = pf - 4
    return t[:q] + f" Elle touche {r.randint(2, 40)} % des malades hospitalisés<sup class=\"r\"><a href=\"#sb-1\">1</a></sup>." + t[q:]
MUTANTS = [("épidémiologie hors budget", _m_long, "B1"), ("chiffre sans source", _m_source, "B2"), ("pourcentage sans dénominateur", _m_denom, "B3")]

ECRIT = []

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
