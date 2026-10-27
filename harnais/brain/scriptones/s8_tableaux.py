#!/usr/bin/env python3
"""Scriptone S8 · tableaux d'épidémiologie à en-têtes explicites (doléance 8 de Vial). Région AUF.
Exigence : lire une ligne seule et comprendre le lien entre ses cellules (« pour CE stade, X % des cas, Y % de mortalité DANS ce stade »).
  T1 tableau sans en-têtes <th>                       T2 en-tête générique (« Donnée », « Valeur », « Chiffre », « Résultat », « % »…)
  T3 unité absente de l'en-tête alors que les cellules la portent (%, ans, °C, pour 100 000) → ajoutée par script
  T4 portée du pourcentage ambiguë : colonne dont la somme ≈ 100 (« part des N cas ») ou taux propre à la ligne (« dans ce stade »)
  T5 première colonne sans intitulé de dimension (la ligne n'a pas de sujet)
  T6 légende absente ou incomplète (quoi, où, quand, n = N)    T7 colonne de valeurs hétérogènes (nombres, %, texte mêlés)
RÈGLE DE RÉÉCRITURE : 1re colonne = « <dimension> (<critère>) » ; colonne chiffrée = « <mesure> <portée> (<unité>) », portée =
« parmi les N cas » si la colonne totalise 100 %, sinon « dans ce <dimension> » ; légende = « <mesure>, <population>, <lieu>, <période>, n = N ».
Le script propose l'en-tête réécrit (preuve) ; seule l'unité (T3) est ajoutée automatiquement : aucune cellule n'est jamais modifiée."""
import html as H, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s8_tableaux", "AUF", "1.0.0"
GENERIQUES = {"donnée", "données", "valeur", "valeurs", "chiffre", "chiffres", "résultat", "résultats", "%", "n", "nombre", "taux", "fréquence",
              "information", "info", "détail", "détails", "remarque", "commentaire", "élément", "éléments", "paramètre", "item", "-", ""}
UNITES = [("%", r"\d\s?%"), ("ans", r"\d\s?ans\b"), ("°C", r"\d\s?°C"), ("pour 100 000", r"pour 100 000"), ("pour 1000", r"pour 1 ?000\b")]
GEN_COURANT = {"donnée", "données", "valeur", "valeurs", "chiffre", "chiffres", "information", "info", "élément", "éléments", "item", "-", ""}   # « Résultat » reste permis (grille Q9.4)
EPI_LEG = re.compile(r"(?i)incidence|prévalence|mortalit|létalit|épidémiolog")
EPI = re.compile(r"(?i)incidence|prévalence|mortalit|létalit|fréquence|\bcas\b|patients|décès|%|pour 100", re.I)
PORTEE = re.compile(r"(?i)\b(?:parmi|des|du|de la|dans|sur|par|chez|pour|n\s*=|/)\b|/")


def _cellules(row):
    return [(m.group(1).lower(), m.group(2)) for m in re.finditer(r"(?is)<(th|td)\b[^>]*>(.*?)</\1>", row)]


def tableaux(t):
    a, f = bus.bornes_cours(t); out = []
    for m in re.finditer(r"(?is)<table\b[^>]*>(.*?)</table>", t[a:f]):
        if bus.dans_fenetre(t, a + m.start()) or 'id="rm"' in t[max(0, a + m.start() - 200):a + m.start()]: continue
        corps = m.group(1); cap = re.search(r"(?is)<caption[^>]*>(.*?)</caption>", corps)
        rows = [_cellules(r) for r in re.findall(r"(?is)<tr\b[^>]*>(.*?)</tr>", corps)]
        out.append(dict(debut=a + m.start(), fin=a + m.end(), caption=bus.texte(cap.group(1)) if cap else "", rows=[r for r in rows if r]))
    return out


def _num(x):
    m = re.search(r"(\d+(?:[,.]\d+)?)\s?%", x); return float(m.group(1).replace(",", ".")) if m else None


def analyser(t, nom, opt=None):
    me = sys.modules[__name__]; D = []; S = bus.sections(t); p2 = S.get(2, (-1, -1)); n_epi = 0
    for k, tb in enumerate(tableaux(t)):
        rows = tb["rows"]; anc = bus.ancre(t, tb["debut"], tb["caption"] or "tableau")
        if not rows: continue
        epi = p2[0] <= tb["debut"] < p2[1] or bool(EPI_LEG.search(tb["caption"]))
        n_epi += epi
        tete = rows[0] if all(k_ == "th" for k_, _ in rows[0]) else None
        if not tete:
            D.append(bus.doleance(me, "T1", nom, anc, "GRAVE" if epi else "MOYEN", "tableau sans ligne d'en-têtes <th>",
                                  "ajouter une ligne <tr><th>…</th></tr> : 1re colonne = dimension (critère), puis « mesure portée (unité) »", "agent"))
            continue
        H_ = [bus.texte(c) for _, c in tete]; corps = [[bus.texte(c) for _, c in r] for r in rows[1:] if len(r) == len(tete)]
        if not epi:
            for j, h in enumerate(H_):
                if h.lower().strip(" :") in GEN_COURANT:
                    D.append(bus.doleance(me, "T2", nom, anc, "MOYEN", f"en-tête générique « {h} » (colonne {j + 1})", "nommer ce que la colonne mesure", "agent", " | ".join(H_)))
            continue
        nN = re.search(r"n\s*=\s*([\d  ]+)", tb["caption"]); N = nN.group(1).strip() if nN else None
        dim = re.sub(r"\s*\(.*$", "", H_[0]).strip().lower() if H_ and H_[0].lower().strip(" :") not in GENERIQUES else "ligne"
        for j, h in enumerate(H_):
            col = [r[j] for r in corps if j < len(r)]; hl = h.lower().strip(" :")
            if j == 0:
                if hl in GENERIQUES:
                    D.append(bus.doleance(me, "T5", nom, anc, "GRAVE", f"1re colonne « {h} » : la ligne n'a pas de sujet nommé",
                                          "intituler la 1re colonne par sa dimension et son critère (ex. « Stade (température centrale) », « Cause (groupe IFSI) »)", "agent", " | ".join(H_)))
                continue
            pct = [x for x in col if re.search(r"\d\s?%", x)]
            unites = [u for u, rx in UNITES if col and sum(bool(re.search(rx, x)) for x in col) >= 0.6 * len(col)]
            if hl in GENERIQUES:
                prop = f"<mesure> {'parmi les ' + N + ' cas' if N else 'dans ce ' + dim} ({unites[0] if unites else 'unité'})"
                D.append(bus.doleance(me, "T2", nom, anc, "GRAVE", f"en-tête générique « {h} » (colonne {j + 1}) : le lien entre les cellules de la ligne n'est pas lisible",
                                      f"réécrire l'en-tête selon la règle « mesure portée (unité) » : {prop} ; si chaque ligne porte une mesure différente, la 1re colonne nomme la mesure et chaque cellule s'écrit « n/N (x %) »", "agent", " | ".join(H_)))
                continue
            for u in unites:
                if u.lower() not in h.lower():
                    D.append(bus.doleance(me, "T3", nom, anc, "MOYEN", f"colonne « {h} » : unité « {u} » portée par les cellules, absente de l'en-tête",
                                          f"en-tête « {h} ({u}) » : s8_tableaux.py --appliquer (aucune cellule modifiée)", "script", f"{len(col)} cellules"))
            if len(pct) >= 2 and len(pct) >= 0.6 * len(col) and not PORTEE.search(h):
                v = [_num(x) for x in col if _num(x) is not None]; tot = sum(v)
                portee = f"parmi les {N} cas" if (98 <= tot <= 102 and N) else ("parmi tous les cas (total 100 %)" if 98 <= tot <= 102 else f"dans ce {dim}")
                h0 = re.sub(r"\s*\(%\)", "", h)
                D.append(bus.doleance(me, "T4", nom, anc, "GRAVE", f"« {h} » : on ne sait pas de quoi le pourcentage est la part (somme de la colonne {tot:.1f} %)",
                                      f"réécrire l'en-tête : « {h0} {portee} (%) »", "agent", f"cellules : {', '.join(col[:5])}"))
            kinds = {("pct" if "%" in x else "frac" if re.search(r"\d+\D{0,25}\bsur \d+|\d+\s?/\s?\d+", x) else "num" if re.fullmatch(r"[\d  ,.<>≥≤–-]+", x) else "txt") for x in col if x}
            if len(kinds) >= 2 and kinds & {"pct", "frac", "num"}:
                D.append(bus.doleance(me, "T7", nom, anc, "MOYEN", f"colonne « {h} » mêle nombres, pourcentages et texte : la ligne ne se lit pas seule",
                                      "scinder en colonnes homogènes (« effectif (n/N) », « part (%) »), ou écrire chaque cellule « n/N (x %) »", "agent", " | ".join(col[:4])))
        cap = tb["caption"]
        manque = [x for x, rx in (("population", r"(?i)patients|adultes|enfants|cas|population|habitants|personnes|hémodialysés|consultations"),
                                  ("lieu", r"(?i)suisse|berne|bernois|genève|lausanne|zurich|bâle|lucerne|tessin|europ|pays|canton|monde|international|france|allemagne|espagne|italie|états-unis|écosse|pologne|urgences|hôpital|registre"),
                                  ("période", r"(?:19|20)\d\d"), ("effectif n = N", r"n\s*=\s*\d")) if not re.search(rx, cap)]
        if not cap or len(manque) >= 2:
            D.append(bus.doleance(me, "T6", nom, anc, "MOYEN", f"légende {'absente' if not cap else 'incomplète'} : manque {', '.join(manque)}",
                                  "légende = « mesure, population, lieu, période, n = N » (ex. « Gravité et mortalité, adultes aux urgences de Berne, 2000–2019, n = 439 »)", "agent", cap[:120]))
    return D, dict(tableaux=len(tableaux(t)), tableaux_epi=n_epi)


def corriger(t, opt=None):
    """T3 seulement : ajoute l'unité dominante des cellules à l'en-tête (texte de l'en-tête complété, jamais une cellule)."""
    for tb in sorted(tableaux(t), key=lambda x: -x["debut"]):
        rows = tb["rows"]
        if not rows or not all(k == "th" for k, _ in rows[0]): continue
        seg = t[tb["debut"]:tb["fin"]]; tr = re.search(r"(?is)<tr\b[^>]*>.*?</tr>", seg); ths = list(re.finditer(r"(?is)(<th\b[^>]*>)(.*?)(</th>)", tr.group(0)))
        corps = [[bus.texte(c) for _, c in r] for r in rows[1:] if len(r) == len(ths)]; neuf = tr.group(0)
        for j in range(len(ths) - 1, 0, -1):
            col = [r[j] for r in corps]; h = bus.texte(ths[j].group(2))
            for u, rx in UNITES:
                if col and sum(bool(re.search(rx, x)) for x in col) >= 0.6 * len(col) and u.lower() not in h.lower() and h.lower().strip(" :") not in GENERIQUES:
                    m = ths[j]; neuf = neuf[:m.start(2)] + m.group(2).rstrip() + f" ({u})" + neuf[m.end(2):]
                    break
        seg = seg[:tr.start()] + neuf + seg[tr.end():]
        t = t[:tb["debut"]] + seg + t[tb["fin"]:]
    return t


def _tb_epi(t):
    S = bus.sections(t); return [tb for tb in tableaux(t) if S[2][0] <= tb["debut"] < S[2][1]][0]
def _m_generique(t, r):
    tb = _tb_epi(t); seg = t[tb["debut"]:tb["fin"]]; ths = list(re.finditer(r"(?is)<th\b[^>]*>(.*?)</th>", seg)); m = r.choice(ths[1:])
    seg = seg[:m.start(1)] + r.choice(["Valeur", "Donnée", "Chiffre", "Résultat"]) + seg[m.end(1):]; return t[:tb["debut"]] + seg + t[tb["fin"]:]
def _m_portee(t, r):
    tb = _tb_epi(t); seg = t[tb["debut"]:tb["fin"]]; ths = list(re.finditer(r"(?is)<th\b[^>]*>(.*?)</th>", seg)); m = ths[-1]
    seg = seg[:m.start(1)] + r.choice(["Mortalité (%)", "Létalité (%)", "Part (%)"]) + seg[m.end(1):]; return t[:tb["debut"]] + seg + t[tb["fin"]:]
def _m_legende(t, r):
    tb = _tb_epi(t); seg = re.sub(r"(?is)<caption[^>]*>.*?</caption>", "", t[tb["debut"]:tb["fin"]]); return t[:tb["debut"]] + seg + t[tb["fin"]:]
def _m_sans_th(t, r):
    tb = _tb_epi(t); seg = re.sub(r"(?is)<(/?)th\b", r"<\1td", t[tb["debut"]:tb["fin"]]); return t[:tb["debut"]] + seg + t[tb["fin"]:]
MUTANTS = [("en-tête générique", _m_generique, "T2"), ("portée ambiguë", _m_portee, "T4"), ("légende absente", _m_legende, "T6"), ("sans en-têtes", _m_sans_th, "T1")]

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
