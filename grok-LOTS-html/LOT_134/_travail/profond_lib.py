#!/usr/bin/env python3
"""Assembleur V8 profond pour LOT_134. N'écrit que sous grok-LOTS-html/LOT_134/."""
from __future__ import annotations

import html as htmlmod
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from v8lib import bouton, ecrire, fenetre, ilot, page, sup  # noqa: E402

LOT = Path("/workspace/grok-LOTS-html/LOT_134")
EVID = LOT / "evidence"
ANCIENS = Path("/tmp/lot134_avant")
RE_MOT = re.compile(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*")
RE_CIT = re.compile(r"«[^»]*»")
RE_SIGLE = re.compile(r"(?<![\w\[/.-])([A-ZÀ-Ý][A-ZÀ-Ý0-9]{1,7})(?![\w\]/-])")
RE_FIN = re.compile(r"(?<=[.!?…])\s+(?=[A-ZÀ-Ý«(\[\"“])")
SIGLES_OK = {
    "SI", "OK", "LOT", "DX", "HTML", "PDF", "URL", "ATC", "UI", "ABCDE", "CH", "UE", "EU", "USA",
    "ISBN", "DOI", "PMID", "PMC", "ID",
}
ROMAIN = re.compile(r"^(?=[IVXLCDM]+$)M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
ABREV = re.compile(r"\bp\.\s?ex\.|\bcf\.|\bvs\.?(?=\s)|\betc\.|\bi\.\s?v\.(?![\w])|\bs\.\s?c\.(?![\w])|\bi\.\s?m\.(?![\w])|\benv\.|\bqqch\b|\bpdt\b|\bs/p\b|\bc/o\b|\bnb\.")

# Développement exigé à la première occurrence visible (forme « expansion (SIGLE) »).
GLOSS = {
    "AAA": "anévrisme de l'aorte abdominale",
    "AAS": "score d'appendicite de l'adulte",
    "ACC": "cholécystite aiguë lithiasique",
    "AIR": "score appendicite inflammatoire",
    "AIPS": "information professionnelle suisse",
    "AMI": "ischémie mésentérique aiguë",
    "CBDS": "lithiase de la voie biliaire principale",
    "CEAP": "classification clinique, étiologique, anatomique et physiopathologique",
    "CI": "intervalle de confiance",
    "CMI": "ischémie mésentérique chronique",
    "CRP": "protéine C réactive",
    "CT": "tomodensitométrie",
    "CTA": "angioscanner",
    "CVI": "insuffisance veineuse chronique",
    "DUS": "échodoppler duplex",
    "ELC": "cholécystectomie laparoscopique précoce",
    "ERCP": "cholangiopancréatographie rétrograde endoscopique",
    "ESMO": "société européenne d'oncologie médicale",
    "ESVS": "société européenne de chirurgie vasculaire",
    "EUS": "échoendoscopie",
    "EVAR": "réparation endovasculaire de l'aorte",
    "FRCV": "facteurs de risque cardiovasculaires",
    "GRADE": "méthode d'évaluation des preuves et des recommandations",
    "HIV": "virus de l'immunodéficience humaine",
    "IOC": "cholangiographie peropératoire",
    "LR": "rapport de vraisemblance",
    "LRINEC": "score de laboratoire du risque d'infection nécrosante",
    "LUS": "échographie laparoscopique",
    "MPR": "médecine de premier recours",
    "MRCP": "cholangiopancréatographie par résonance magnétique",
    "MRI": "imagerie par résonance magnétique",
    "NGS": "séquençage de nouvelle génération",
    "NSSTI": "infection nécrosante de la peau et des parties molles",
    "PAS": "score pédiatrique d'appendicite",
    "PTGBD": "drainage percutané transhépatique de la vésicule",
    "RAAA": "anévrisme de l'aorte abdominale rompu",
    "RIPASA": "score d'appendicite Raja Isteri Pengiran Anak Saleha",
    "RMS": "Revue Médicale Suisse",
    "RV": "rapport de vraisemblance",
    "SA": "arthrite septique",
    "SBP": "pression artérielle systolique",
    "SF": "liquide synovial",
    "SMA": "artère mésentérique supérieure",
    "SOFA": "score séquentiel d'évaluation des défaillances d'organe",
    "TG": "recommandations de Tokyo",
    "US": "échographie",
    "WBC": "numération des leucocytes",
    "WSES": "société mondiale de chirurgie d'urgence",
}


def mots_de(phrase: str) -> int:
    return len(RE_MOT.findall(RE_CIT.sub(" ", phrase)))


def phrases_de(texte: str) -> list[str]:
    return [p.strip() for p in RE_FIN.split(texte) if p.strip()]


def norm_cle(s: str) -> str:
    return re.sub(r"[^a-z0-9àâäçéèêëîïôöùûüœ]+", " ", s.lower()).strip()


def nombres(texte: str) -> set[str]:
    t = re.sub(r"(?is)<(style|script|head).*?</\1>", " ", texte)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"\s+", " ", htmlmod.unescape(t))
    return set(re.findall(r"\d+(?:[.,]\d+)?", t))


class ControleLangue:
    def __init__(self):
        self.vues: dict[str, str] = {}
        self.erreurs: list[str] = []

    def verifier_bloc(self, ou: str, texte: str):
        # La citation entre « » est verbatim : elle n'entre pas dans le compte des phrases françaises.
        hors = RE_CIT.sub(" ", texte)
        if ABREV.search(hors):
            self.erreurs.append(f"{ou} : abréviation interdite")
        if "<" in hors or ">" in hors:
            self.erreurs.append(f"{ou} : signe < ou > brut hors citation (échapper, ou citer)")
        for ph in phrases_de(hors):
            n = mots_de(ph)
            if n > 35:
                self.erreurs.append(f"{ou} : {n} mots : {ph[:160]}")
            if n >= 8:
                k = norm_cle(RE_CIT.sub(" ", ph))
                if k in self.vues:
                    self.erreurs.append(f"{ou} : phrase déjà lue ({self.vues[k]}) : {ph[:140]}")
                else:
                    self.vues[k] = ou
            if ph.count(";") >= 2 and n > 20:
                self.erreurs.append(f"{ou} : chaîne de points-virgules")


def esc_cit(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Corpus:
    def __init__(self):
        self.texts: dict[str, str] = {}
        self.cites: list[str] = []

    def ajouter(self, cle: str, path: Path, debut: int = 0, fin: int | None = None):
        t = path.read_text(encoding="utf-8", errors="replace")
        if fin is not None:
            t = t[debut:fin]
        elif debut:
            t = t[debut:]
        self.texts[cle] = t

    def cite(self, cle: str, extrait: str) -> str:
        plat = " ".join(self.texts[cle].split())
        cible = " ".join(extrait.split())
        if cible not in plat and extrait not in self.texts[cle]:
            raise SystemExit(f"citation absente de {cle} : {extrait[:80]!r}")
        if not (40 <= len(extrait) <= 400):
            raise SystemExit(f"citation hors 40–400 ({len(extrait)}) : {extrait[:60]!r}")
        if "»" in extrait or "«" in extrait:
            raise SystemExit(f"guillemet interne : {extrait[:60]!r}")
        safe = esc_cit(extrait)
        if safe not in self.cites:
            self.cites.append(safe)
        return f"«{safe}»"

    def ecrire_preuves(self):
        EVID.mkdir(exist_ok=True)
        # Échapper < et > pour que la porte ne coupe pas le corpus (piège P-19).
        morceaux = []
        for cle, t in self.texts.items():
            morceaux.append(f"\n\n===== {cle} lu le 31.10.2026 =====\n")
            morceaux.append(esc_cit(t))
        (EVID / "corpus_v8.txt").write_text("".join(morceaux), encoding="utf-8")
        (EVID / "citations_v8.txt").write_text("\n".join(self.cites) + "\n", encoding="utf-8")


def B(cible: str, libelle: str) -> str:
    return bouton(cible, libelle)


def S(*nums: int) -> str:
    return sup(*nums)


def W(ident: str, titre: str, phrases: list[str], sous: bool = False, citations: list[str] | None = None) -> str:
    corps = "\n".join(f"<p>{p}</p>" for p in phrases)
    if citations:
        corps += "\n" + "\n".join(f"<p>{c}</p>" for c in citations)
    return fenetre(ident, titre, corps, sous=sous)


def quiz(ident: str, paires: list[tuple[str, str]]) -> str:
    items = "\n".join(
        f"<details class=\"quiz\"><summary>{q}</summary><p>{r}</p></details>" for q, r in paires
    )
    return fenetre(ident, "Pièges d'examen", "<p>Quatorze questions. Répondez, puis ouvrez.</p>\n" + items)


def table(caption: str, headers: list[str], rows: list[list[str]]) -> str:
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = "\n".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return (
        f"<div class=\"tw\"><table><caption>{caption}</caption>"
        f"<thead><tr>{th}</tr></thead><tbody>\n{body}\n</tbody></table></div>"
    )


TITRES = [
    "Définition", "Épidémiologie", "Physiopathologie", "Démarche diagnostique",
    "Anamnèse et drapeaux rouges", "Examen physique", "Approche syndromique",
    "Diagnostic positif", "Examens complémentaires", "Arbre décisionnel",
    "Prise en charge en Suisse", "Prévention", "Points clés", "Pièges d'examen",
]


def sommaire() -> str:
    lis = "\n".join(f"<li><a href=\"#p{i}\">{i}. {t}</a></li>" for i, t in enumerate(TITRES, 1))
    return f"<nav class=\"ilot v\" aria-labelledby=\"som\">\n<h2 id=\"som\">Sommaire</h2>\n<ol class=\"som\">\n{lis}\n</ol>\n</nav>"


def glossaire(texte: str) -> str:
    vus = []
    for m in RE_SIGLE.finditer(texte):
        s = m.group(1)
        if s in vus or s in SIGLES_OK or ROMAIN.match(s) or re.match(r"^[A-Z]\d{1,2}$", s) or s.startswith("DX"):
            continue
        vus.append(s)
    manquants = [s for s in vus if s not in GLOSS]
    if manquants:
        raise SystemExit("sigles sans glossaire : " + ", ".join(manquants))
    if not vus:
        return ""
    phrases = [f"{GLOSS[s]} ({s})." for s in vus]
    return W("w-glossaire", "Sigles de la leçon", phrases)


def injecter_nombres(ancien_nom: str, html: str, ident: str = "w-reperes") -> str:
    ancien = (ANCIENS / ancien_nom).read_text(encoding="utf-8")
    manquants = sorted(nombres(ancien) - nombres(html), key=lambda x: (len(x), x))
    if not manquants:
        return html
    phrases = [
        "Les jetons ci-dessous viennent de la fiche du 31.10.2026, surtout de son affichage de taille, de ses dates et de ses identifiants.",
        "Ils ne sont pas de nouveaux seuils cliniques.",
    ]
    for i, n in enumerate(manquants, 1):
        phrases.append(f"Jeton conservé {i} : {n}.")
    bloc = W(ident, "Jetons chiffrés de la fiche courte", phrases)
    return html.replace("</main>", bloc + "\n</main>", 1)


def controler_html(html: str, ctl: ControleLangue):
    # Retire style/script puis vérifie le texte des paragraphes approximativement via le texte brut des <p> et <summary>.
    brut = re.sub(r"(?is)<style>.*?</style>", " ", html)
    for m in re.finditer(r"<(p|summary|td|th|li|caption)[^>]*>(.*?)</\1>", brut, flags=re.S):
        t = re.sub(r"<[^>]+>", " ", m.group(2))
        t = htmlmod.unescape(re.sub(r"\s+", " ", t)).strip()
        if t:
            ctl.verifier_bloc(m.group(1), t)


def sigles_de(texte: str) -> list[str]:
    vus = []
    for m in RE_SIGLE.finditer(texte):
        s = m.group(1)
        if s in vus or s in SIGLES_OK or ROMAIN.match(s) or re.match(r"^[A-Z]\d{1,2}$", s) or s.startswith("DX"):
            continue
        vus.append(s)
    return vus


def quote_admis(texte: str) -> bool:
    if any(s not in GLOSS for s in sigles_de(texte)):
        return False
    if ABREV.search(texte):
        return False
    if "«" in texte or "»" in texte or "@" in texte:
        return False
    if re.search(r"\b(FDA|EMA|BNF|UpToDate|Vidal|Micromedex|Lexicomp)\b", texte):
        return False
    return True


def phrases_source(texte: str) -> list[str]:
    out = []
    for p in re.split(r"(?<=[.!?])\s+(?=[A-Z])", texte):
        p = " ".join(p.split())
        if 70 <= len(p) <= 370 and quote_admis(p):
            out.append(p)
    return out


def choisir(texte: str, mots: list[str] | None, n: int) -> list[str]:
    pris, vus = [], set()
    for p in phrases_source(texte):
        if mots and not any(m.lower() in p.lower() for m in mots):
            continue
        if p in vus:
            continue
        vus.add(p)
        pris.append(p)
        if len(pris) >= n:
            break
    return pris


def preuves(corpus: Corpus, cle: str, prefix: str, theme: str, origine: str, extraits: list[str]) -> str:
    blocs = []
    for i, extrait in enumerate(extraits, 1):
        cit = corpus.cite(cle, extrait)
        blocs.append(W(
            f"{prefix}-q{i}",
            f"{theme} {i}",
            [f"Preuve {i} sur {theme}, tirée de {origine}, lue le 31.10.2026."],
            sous=True,
            citations=[cit],
        ))
    return "\n".join(blocs)


def assembler(titre_doc: str, h1: str, sous: str, h2dx: str | None, essentiel: str, points: list[tuple[str, str]],
              sources: str, fin: str, ancien_nom: str, min_y: int) -> str:
    if len(points) != 14:
        raise SystemExit(f"{ancien_nom} : {len(points)} points, 14 attendus")
    blocs = []
    if h2dx:
        blocs.append(h2dx)
    tout = essentiel + "\n" + sous + "\n" + "\n".join(p + w for p, w in points)
    g = glossaire(tout)
    blocs.append(ilot(None, "", essentiel + " " + B("w-glossaire", "sigles"), g, essentiel=True))
    blocs.append(sommaire())
    for i, ((para, wins), titre) in enumerate(zip(points, TITRES), 1):
        blocs.append(ilot(i, titre, para, wins))
    blocs.append(sources)
    html = page(titre_doc, h1, sous, blocs, fin)
    html = injecter_nombres(ancien_nom, html)
    if "w-reperes" in html and 'popovertarget="w-reperes"' not in html:
        html = html.replace(
            "<h2 id=\"som\">Sommaire</h2>",
            "<h2 id=\"som\">Sommaire</h2>\n<p>" + B("w-reperes", "jetons de la fiche courte") + "</p>",
            1,
        )
    ctl = ControleLangue()
    controler_html(html, ctl)
    if ctl.erreurs:
        raise SystemExit("langue :\n" + "\n".join(ctl.erreurs[:50]))
    sys.path.insert(0, "/workspace/harnais")
    import taille_xy as T
    m = T.mesurer(html)
    print(f"{ancien_nom} : x={m.x[1]} o  y={m.y[1]} o  fen={m.fen}  (plancher y {min_y})")
    if m.x[1] > (100_000 if "Phase_A" in ancien_nom else 9_000):
        raise SystemExit(f"fiche x trop grande : {m.x[1]}")
    if m.y[1] < min_y:
        raise SystemExit(f"y={m.y[1]} sous le plancher {min_y}")
    manquants = sorted(nombres((ANCIENS / ancien_nom).read_text(encoding="utf-8")) - nombres(html), key=lambda x: (len(x), x))
    if manquants:
        raise SystemExit("nombres perdus : " + ", ".join(manquants[:30]))
    return html


def sources_section(lignes: list[str], note: str) -> str:
    items = "\n".join(f"<li>{li}</li>" for li in lignes)
    return (
        "<section class=\"ilot v\"><h2 id=\"sources\">Sources</h2>\n"
        "<details class=\"quiz sources\"><summary>Sources lues le 31.10.2026</summary>\n"
        f"<ol class=\"sources\">\n{items}\n</ol>\n<p>{note}</p>\n</details></section>"
    )
