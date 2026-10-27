#!/usr/bin/env python3
"""CONTRACTEUR DE TEXTE · CONSERVATEUR DE NOTIONS (moteur, lecture seule). Un clone par auditeur : harnais/agents/KB1.py … KB5.py.

  ╔══ RÈGLE ABSOLUE DE VIAL ══════════════════════════════════════════════════════════════════════╗
  ║ LA CONTRACTION NE DOIT PAS DU TOUT TOUCHER LES NOTIONS, NI COMPROMETTRE LE SENS, NI           ║
  ║ L'EXPLICATION DE QUOI QUE CE SOIT. On n'a pas besoin de beaucoup de mots pour transmettre      ║
  ║ des notions expliquées.                                                                        ║
  ╚════════════════════════════════════════════════════════════════════════════════════════════════╝

Dernier secteur de chaque fichier avant le commit. Il ne réécrit pas la médecine : il retire l'excès de mots et PROUVE que rien
d'utile n'a disparu. Contracter peut REFORMULER plus concis (pas seulement supprimer) ; notions, sens et explications restent.
  KBi.py contracter <fichier>   1re fois : inventaire des notions à l'entrée. Puis contraction mécanique sûre (formules creuses,
                                doublons exacts) et cibles de contraction (redites, phrases longues, phrases nominales, points lourds).
  KBi.py verifier <fichier> [--exceptions "mot,mot"]   compare à l'inventaire ; pose le visa (lié à l'empreinte) si tout est conservé
  KBi.py etat <fichier>         inventaire, volume, visa
Conservation exigée : nombres 100 %, médicaments 100 %, couples comparateur + valeur + unité 100 %, tableaux et 14 points intacts ;
termes cliquables, renvois [Sn], notions (noms) ≥ 95 % ; chaque phrase d'explication (car, parce que, donc, ainsi, provoque,
entraîne, explique, permet, mécanisme, afin de, pour que, →) couverte à ≥ 85 % par les lemmes de la meilleure phrase (ou de deux
phrases voisines : scinder est permis) ; toute autre phrase couverte à ≥ 80 %, sinon admise seulement si c'est la redite d'une phrase
conservée ; négations et conditions (ne… pas, jamais, sans, aucun, contre-indiqué, interdit, éviter, seulement, uniquement, si, sauf)
jamais diminuées. Aucun quota de volume : le gain est affiché. Seul l'excès objectif doit être résolu : redites quasi identiques ≤ 3,
phrases de plus de 30 mots ≤ 6 %, aucune phrase nominale en plus."""
import hashlib, html as H, json, os, re, sys, time
from pathlib import Path
from collections import Counter, defaultdict
R = Path(__file__).resolve().parent.parent.parent
HD = Path(__file__).resolve().parent
sys.path.insert(0, str(R / "harnais")); sys.path.insert(0, str(R / "harnais/grille14"))

def _cadre(lignes, l=96):
    out = ["╔══ RÈGLE ABSOLUE DE VIAL " + "═" * (l - 23) + "╗"]
    for x in lignes:
        mots, cur = x.split(), ""
        for m in mots:
            if len(cur) + len(m) + 1 > l: out.append("║ " + cur.ljust(l) + " ║"); cur = m
            else: cur = (cur + " " + m).strip()
        out.append("║ " + cur.ljust(l) + " ║")
    return "\n".join(out + ["╚" + "═" * (l + 2) + "╝"])
REGLE_ABSOLUE = _cadre(["LA CONTRACTION NE DOIT PAS DU TOUT TOUCHER LES NOTIONS, NI COMPROMETTRE LE SENS, NI L'EXPLICATION DE QUOI QUE CE SOIT.",
                        "On n'a pas besoin de beaucoup de mots pour transmettre des notions expliquées.",
                        "Contracter = reformuler plus concis ou retirer une redite. Jamais résumer, jamais couper un mécanisme, une négation, une condition, un seuil, une unité. En cas de doute, garde la phrase."])

CIBLE = json.loads((HD / "CIBLE.json").read_text())   # indicatif seulement (affiché) : aucun quota de volume ne bloque
SEUIL_EXPL, SEUIL_PHRASE, SEUIL_REDITE = 0.85, 0.80, 0.80
MAX_REDITES, MAX_LONGUES = 3, 0.06
EXPL = re.compile(r"\b(?:car|parce qu|donc|ainsi|provoqu\w*|entraîn\w*|expliqu\w*|permet\w*|permett\w*|mécanisme\w*|afin d|pour que|pour qu)\b|→", re.I)
MARQ = {"ne… pas": r"\bn(?:e\b|['’])[^.;:]{0,40}?\bpas\b", "jamais": r"\bjamais\b", "sans": r"\bsans\b", "aucun": r"\baucun(?:e|s|es)?\b",
        "contre-indiqué": r"\bcontre-indiqu\w*|\bcontre-indication\w*", "interdit": r"\binterdi\w*", "éviter": r"\bévit\w*",
        "seulement": r"\bseulement\b", "uniquement": r"\buniquement\b", "si": r"\bsi\b|\bs['’]il", "sauf": r"\bsauf\b"}
MARQ = {k: re.compile(v, re.I) for k, v in MARQ.items()}
CMP = {"≥": "≥", "⩾": "≥", "≤": "≤", "⩽": "≤", ">": ">", "<": "<", "au moins": "≥", "au plus": "≤", "plus de": ">", "moins de": "<", "jusqu'à": "≤",
       "dès": "≥", "au-delà de": ">", "au-dessus de": ">", "en dessous de": "<", "au-dessous de": "<"}
RX_UNITE = re.compile(r"(?:(≥|≤|⩾|⩽|>|<|(?:supérieure?s?|inférieure?s?)(?: ou égale?s?)? à|au moins|au plus|plus de|moins de|jusqu'à|dès|au-delà de|au-dessus de|en dessous de|au-dessous de)\s*)?"
                      r"(?<![\w.,])(\d+(?:[.,]\d+)?(?:\s?[–-]\s?\d+(?:[.,]\d+)?)?)\s?"
                      r"(%|‰|mg/kg/j|mg/kg|mg/j|mg/l|mg/dl|mg/min|µg/l|μg/l|µg|μg|mcg|ng/ml|ng/l|pg/ml|g/l|g/dl|kg/m2|kg/m²|kg|mg|g|ml/min|ml|mL|"
                      r"mmol/l|mmol/L|µmol/l|μmol/l|nmol/l|pmol/l|mUI/l|mU/l|UI/l|U/l|UI|mmHg|mm Hg|cm|mm|°C|bpm|/min|heures?|h|minutes?|min|"
                      r"jours?|j|semaines?|sem|mois|années?|ans?|MBq|Gy|mSv|L|l)(?![\wÀ-ÿ'’/])")
U_NORM = {"heure": "h", "heures": "h", "minute": "min", "minutes": "min", "jour": "j", "jours": "j", "semaine": "sem", "semaines": "sem", "an": "an", "ans": "an",
          "année": "an", "années": "an", "μg": "µg", "mcg": "µg", "μg/l": "µg/l", "mm hg": "mmhg", "kg/m²": "kg/m2", "μmol/l": "µmol/l"}
VERBES_VIDES = {"être", "avoir", "faire", "pouvoir", "devoir", "aller"}
BLOC = re.compile(r"</?(?:p|div|li|ul|ol|tr|td|th|h[1-6]|table|section|details|summary|main|br|caption|label)\b[^>]*>", re.I)
FIN_COURS = re.compile(r"(?is)<h2[^>]*>\s*Sources[^<]*</h2>|<details class=\"refs\"")

# ---- texte et notions ------------------------------------------------------------------------------------------
def corps(html):
    """Texte à contracter : tout sauf script/style, onglet Rappel mémoire, liste des sources."""
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html)
    t = re.sub(r"(?is)<div id=\"?rappel\"?.*?</div>\s*</div>", " ", t)
    m = FIN_COURS.search(t)
    return t[:m.start()] if m else t

def texte(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", corps(html))).strip()

_NLP = None
def nlp():
    global _NLP
    if _NLP is None:
        import spacy
        _NLP = spacy.load("fr_core_news_sm", disable=["ner", "parser"]); _NLP.max_length = 3_000_000
    return _NLP

_CACHE = {}
def analyse(phrases):
    """Pour chaque phrase : (lemmes de contenu, lemmes noms, verbale). Cache en mémoire : une phrase inchangée n'est jamais réanalysée."""
    neuves = [p for p in dict.fromkeys(phrases) if p not in _CACHE]
    for p, d in zip(neuves, nlp().pipe(neuves, batch_size=256)):
        cont = {(x.lemma_ or x.text).lower() for x in d if (x.pos_ in ("NOUN", "PROPN", "ADJ", "NUM") or (x.pos_ == "VERB" and x.lemma_.lower() not in VERBES_VIDES))
                and (len(x.text) > 2 or x.text.isdigit())}
        noms = {x.lemma_.lower() for x in d if x.pos_ in ("NOUN", "PROPN") and len(x.lemma_) > 2 and x.lemma_.isalpha()}
        verb = any(x.pos_ in ("VERB", "AUX") or "VerbForm=Fin" in str(x.morph) for x in d) or "→" in p or "?" in p
        _CACHE[p] = (frozenset(cont), frozenset(noms), verb)
    return [_CACHE[p] for p in phrases]

def decoupe(html):
    """Phrases du cours : (texte, nature) ; nature = corps, fen (contenu d'une fenêtre) ou tab (cellule de tableau)."""
    c = corps(html); fen, tabs = [], []
    c = re.sub(r"(?is)<table.*?</table>", lambda m: tabs.append(m.group(0)) or "\n", c)
    c = re.sub(r'(?s)<span class="(?:df|dxc)">(.*?)</span>', lambda m: fen.append(m.group(1)) or " ", c)
    out = []
    for src, nat in [(c, "corps")] + [(x, "fen") for x in fen] + [(x, "tab") for x in tabs]:
        s = H.unescape(re.sub(r"<[^>]+>", " ", BLOC.sub("\n", src)))
        for ligne in s.split("\n"):
            for p in re.split(r"(?<=[.!?])\s+", ligne):
                p = re.sub(r"\s+", " ", re.sub(r"\[S\d+\]", " ", p)).strip(" ·")
                if p: out.append((p, nat))
    return out

def unites(t):
    out = set()
    for m in RX_UNITE.finditer(t):
        c = m.group(1) or ""; c = CMP.get(c, c)
        if c.startswith(("supérieur", "inférieur")): c = (">" if c.startswith("sup") else "<") if "égal" not in c else ("≥" if c.startswith("sup") else "≤")
        v = re.sub(r"\s", "", m.group(2)).replace(",", ".").replace("-", "–")
        v = "–".join(f"{float(x):g}" for x in v.split("–") if x)
        u = m.group(3); u = U_NORM.get(u.lower(), U_NORM.get(u, u)); u = "l" if u == "L" else u
        out.add(f"{c} {v} {u}".strip())
    return out

def marqueurs(p): return {k: len(rx.findall(p)) for k, rx in MARQ.items() if rx.search(p)}

def inventaire(html):
    c = corps(html); t = texte(html); sans = re.sub(r"\[S\d+\]", " ", t)
    nombres = {m.replace(",", ".") for m in re.findall(r"(?<![\w.,])\d+(?:[.,]\d+)?", re.sub(r"(?<=\d)[   ](?=\d{3}\b)", "", sans))}
    renvois = set(re.findall(r"\[S(\d+)\]", c)) | set(re.findall(r'href="#sb-(\d+)"', c))
    meds = {x.lower() for x in re.findall(r"\b([A-Z][A-Za-zÀ-ÿ\-]{2,})\s?[®™]", t)} | {re.sub(r"[®™]", "", re.sub(r"<[^>]+>", "", m)).strip().lower() for m in re.findall(r'class="tm med"[^>]*>([^<]+)<', c)}
    for d in re.findall(r"DCI\s*:?\s*(?:</b>)?\s*([^<.(]+)", c): meds |= {x.strip().lower() for x in re.split(r",| et |\+|/", d) if len(x.strip()) > 3}
    termes = {re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m)).strip().lower() for m in re.findall(r'class="tm"[^>]*>([^<]+)<', c)} | {re.sub(r"<[^>]+>", "", m).strip().lower() for m in re.findall(r"<summary[^>]*>(.*?)</summary>", c, re.S)}
    termes = {re.sub(r"\s+([:;?!])", r"\1", x) for x in termes}; termes.discard("")
    sigles = set(re.findall(r"\b[A-Z][A-Z0-9]{1,6}\b", sans))
    tabl = [len(re.findall(r"<tr", x)) for x in re.findall(r"(?is)<table.*?</table>", c)]
    points = sorted({int(x) for x in re.findall(r"<h3[^>]*>\s*(?:<strong>)?\s*(\d{1,2})\.\s", c)})
    ph = decoupe(contraction_mecanique(html)[0]); an = analyse([p for p, _ in ph]); lem = set(); phrases = []
    for (p, nat), (cont, noms, verb) in zip(ph, an):
        lem |= noms
        if len(p.split()) < 4 or len(cont) < 2: continue
        phrases.append(dict(t=p, n=nat, l=sorted(cont), e=bool(EXPL.search(p)), m=marqueurs(p), v=verb, w=len(p.split())))
    return dict(mots=len(t.split()), nombres=sorted(nombres), renvois=sorted(renvois, key=int), meds=sorted(meds), termes=sorted(termes), sigles=sorted(sigles),
                tableaux=tabl, points=points, lemmes=sorted(lem), unites=sorted(unites(sans)), phrases=phrases, longues=part_longues(html))

def ident(p): return hashlib.sha1(p.encode()).hexdigest()[:6]

# ---- comparaison des phrases -------------------------------------------------------------------------------------
def couverture(av, ap, seuils=None):
    """Pour chaque phrase d'avant : (meilleure couverture par une phrase d'après ou par deux phrases voisines — scinder est permis ;
    marqueurs réunis des fenêtres qui la couvrent au seuil)."""
    L = [set(x["l"]) for x in ap]; idx = defaultdict(list)
    for j, s in enumerate(L):
        for w in s: idx[w].append(j)
    out = []
    for i, x in enumerate(av):
        A = set(x["l"]); s0 = (seuils[i] if seuils else SEUIL_PHRASE); cnt = Counter(j for w in A for j in idx.get(w, ()))
        cand = [j for j, n in cnt.most_common(8)] + [j for j, n in cnt.items() if n >= s0 * len(A) / 2]
        best, bm = 0.0, Counter(); vus = set()
        for j in cand:
            for fen in ((j,), (j - 1, j), (j, j + 1)):
                if fen in vus or min(fen) < 0 or max(fen) >= len(ap): continue
                vus.add(fen); u = set().union(*(L[k] for k in fen)); c = len(A & u) / len(A)
                best = max(best, c)
                if c >= s0 - 1e-9:
                    for k in fen:
                        for mk, n in ap[k]["m"].items(): bm[mk] = max(bm[mk], n)
        out.append((best, dict(bm)))
    return out

def redites(phr, seuil=0.8, mini=5):
    """Paires de phrases quasi identiques (Jaccard des lemmes ≥ seuil), corps du cours seulement."""
    P = [(i, set(x["l"])) for i, x in enumerate(phr) if x["n"] == "corps" and len(x["l"]) >= mini and sum(w.isalpha() for w in x["l"]) >= 3]; idx = defaultdict(list); out = []
    for k, (i, s) in enumerate(P):
        cnt = Counter(q for w in s for q in idx.get(w, ()))
        for q, n in cnt.items():
            j, s2 = P[q]
            if n / len(s | s2) >= seuil: out.append((n / len(s | s2), j, i))
        for w in s: idx[w].append(k)
    return sorted(out, reverse=True)

def nominales(phr): return [x for x in phr if x["n"] == "corps" and not x["v"]]
def part_longues(html):
    """Part des phrases de plus de 30 mots, mesurée comme le contrôle de forme (hors tableaux, découpe sur . ! ? ;)."""
    t = re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<table.*?</table>", " ", corps(html)))
    n = [len(x.split()) for x in re.split(r"(?<=[.!?;])\s+", t) if len(x.split()) > 3]
    return (sum(1 for k in n if k > 30) / len(n)) if n else 0.0

def comparer(av, ap, exc):
    """Problèmes de conservation (liste de messages) et lignes de bilan."""
    pb, L = [], []
    for cle, seuil, nm in (("nombres", 1.0, "nombres"), ("meds", 1.0, "médicaments"), ("unites", 1.0, "valeurs avec unité ou seuil (comparateur + valeur + unité)"),
                           ("termes", .95, "termes cliquables"), ("renvois", .95, "renvois [Sn]"), ("lemmes", .95, "notions (noms)")):
        a, b = set(av.get(cle, [])), set(ap.get(cle, []))
        manq = sorted(x for x in a - b if x.lower() not in exc and str(x).lower() not in exc)
        r = 1 - len(manq) / len(a) if a else 1.0
        L.append(f"{nm} : {100 * r:.1f} % conservés ({len(manq)} perdus)")
        if r < seuil - 1e-9: pb.append(f"{nm} perdus ({100 * r:.1f} % < {100 * seuil:.0f} %) : " + ", ".join(manq[:25]) + (" …" if len(manq) > 25 else ""))
    if av["tableaux"] != ap["tableaux"] and (len(ap["tableaux"]) < len(av["tableaux"]) or any(b < a for a, b in zip(av["tableaux"], ap["tableaux"]))):
        pb.append(f"tableaux amputés (lignes par tableau) : {av['tableaux']} → {ap['tableaux']}")
    if set(av["points"]) - set(ap["points"]): pb.append("points disparus : " + str(sorted(set(av["points"]) - set(ap["points"]))))
    # phrases : explications, phrases supprimées, négations et conditions
    A, B = av["phrases"], ap["phrases"]
    seuil = [SEUIL_EXPL if x["e"] else SEUIL_PHRASE for x in A]; cv = couverture(A, B, seuil); garde = [c >= s - 1e-9 for (c, _), s in zip(cv, seuil)]
    Ls = [set(x["l"]) for x in A]; idx = defaultdict(list)
    for i, s in enumerate(Ls):
        if garde[i]:
            for w in s: idx[w].append(i)
    expl, autres, sens = [], [], []
    for i, x in enumerate(A):
        if garde[i]:
            perdu = [k for k in x["m"] if cv[i][1].get(k, 0) < 1]
            if perdu: sens.append(f"« {x['t'][:90]} » perd « {', '.join(perdu)} »")
            continue
        cnt = Counter(j for w in Ls[i] for j in idx.get(w, ()) if j != i)
        redite = any(n / len(Ls[i]) >= max(SEUIL_REDITE, seuil[i]) and set(x["m"]) <= set(A[j]["m"]) for j, n in cnt.items())
        if redite: continue
        (expl if x["e"] else autres).append(f"« {x['t'][:100]} » (couverte à {100 * cv[i][0]:.0f} %, ph:{ident(x['t'])})")
    if expl: pb.append(f"EXPLICATIONS perdues ou amputées ({len(expl)} ; seuil {100 * SEUIL_EXPL:.0f} %) : " + " | ".join(expl[:8]))
    if autres: pb.append(f"phrases supprimées ou fortement réduites (< {100 * SEUIL_PHRASE:.0f} %), sans être la redite d'une phrase conservée ({len(autres)}) : " + " | ".join(autres[:8]))
    if sens: pb.append(f"SENS altéré : négation ou condition perdue ({len(sens)}) : " + " | ".join(sens[:8]))
    ga, gb = Counter(), Counter()
    for i, x in enumerate(A):
        if garde[i]: ga.update(x["m"])
    for x in B: gb.update(x["m"])
    dim = [f"« {k} » {ga[k]} → {gb[k]}" for k in ga if gb[k] < ga[k]]
    if dim and not sens: pb.append("SENS altéré : négations ou conditions diminuées : " + ", ".join(dim))
    L.append(f"phrases : {sum(garde)}/{len(A)} conservées ; explications {sum(1 for i, x in enumerate(A) if x['e'] and garde[i])}/{sum(1 for x in A if x['e'])}")
    # excès objectif encore présent
    rd = redites(B); lg = ap.get("longues", 0.0); na, nb = len(nominales(A)), len(nominales(B))
    L.append(f"excès : {len(rd)} redite(s) quasi identique(s) (≤ {MAX_REDITES}) ; {100 * lg:.1f} % de phrases > 30 mots (≤ {100 * MAX_LONGUES:.0f} %) ; phrases nominales {na} → {nb}")
    if len(rd) > MAX_REDITES: pb.append(f"redites quasi identiques restantes : {len(rd)} > {MAX_REDITES} : " + " | ".join(f"« {B[i]['t'][:60]}… » ≈ « {B[j]['t'][:60]}… »" for _, i, j in rd[:4]))
    if lg > MAX_LONGUES + 1e-9: pb.append(f"phrases de plus de 30 mots : {100 * lg:.1f} % > {100 * MAX_LONGUES:.0f} % : scinde-les (une idée par phrase, explication gardée)")
    if nb > na:
        nv = [x["t"] for x in nominales(B) if x["t"] not in {y["t"] for y in nominales(A)}]
        pb.append(f"phrases sans verbe en plus : {na} → {nb} : " + " | ".join(f"« {t[:70]} » (nv:{ident(t)})" for t in nv[:6]))
    return pb, L

# ---- contraction mécanique sûre -------------------------------------------------------------------------------
CREUX = [  # (motif, remplacement) ; appliqués au texte seulement, jamais dans les balises
    (r"\bIl (?:est|convient d'être) (?:important|essentiel|utile|nécessaire) de (?:noter|souligner|rappeler|signaler|préciser) que ", ""),
    (r"\bIl convient de (?:noter|souligner|rappeler|signaler|préciser) que ", ""),
    (r"\bIl faut (?:noter|souligner|rappeler|signaler|préciser|savoir) que ", ""),
    (r"\b(?:Notons|Rappelons|Soulignons|Précisons|Signalons) que ", ""),
    (r"\bEn effet, ", ""), (r"\bPar ailleurs, ", ""), (r"\bDe plus, ", ""), (r"\bDe surcroît, ", ""), (r"\bEn outre, ", ""), (r"\bÉgalement, ", ""),
    (r"\bEn pratique, ", ""), (r"\bEn règle générale, ", ""), (r"\bDe manière générale, ", ""),
    (r"\bà l'heure actuelle\b", "actuellement"), (r"\bde nos jours\b", "aujourd'hui"), (r"\ben raison du fait que\b", "car"), (r"\bétant donné que\b", "puisque"),
    (r"\bdans le cas où\b", "si"), (r"\bau cas où\b", "si"), (r"\bun grand nombre de\b", "beaucoup de"), (r"\best en mesure de\b", "peut"), (r"\bsont en mesure de\b", "peuvent"),
    (r"\bà l'aide de\b", "avec"), (r"\bpar le biais de\b", "par"), (r"\bil s'agit d'un\b", "c'est un"), (r"\bil s'agit d'une\b", "c'est une"),
    (r"\bcomme (?:nous l'avons vu|indiqué plus haut|cela a été dit)\b[, ]*", ""),
]   # « Ainsi, », « afin de », « de ce fait » et « dans la mesure où » sont des connecteurs d'explication : jamais retirés
CREUX = [(re.compile((f"({p})(\\w)" if r == "" else p), re.I), r) for p, r in CREUX]

def contraction_mecanique(html):
    parties = re.split(r"(<[^>]+>)", html); n = 0; out = []; dans = 0
    for p in parties:
        if p.startswith("<"):
            if re.match(r"<(script|style|h[1-6]|summary|a)\b", p, re.I): dans += 1
            if re.match(r"</(script|style|h[1-6]|summary|a)\s*>", p, re.I): dans = max(0, dans - 1)
            out.append(p); continue
        if dans or len(p.split()) < 2: out.append(p); continue
        q = p
        for rx, rep in CREUX:
            def sub(m):
                nonlocal n
                s, i = m.string, m.start()
                if rep == "":
                    deb = s[:i].strip() == "" or re.search(r"[.!?:]\s*$", s[:i]) is not None
                    if not deb: return m.group(0)   # au milieu d'une phrase (« Il est, en effet, rare ») : on ne touche pas
                    n += 1; return m.group(m.lastindex).upper()
                n += 1; return rep[:1].upper() + rep[1:] if m.group(0)[:1].isupper() else rep
            q = rx.sub(sub, q)
        out.append(q)
    h = "".join(out)
    def dedup(m):
        nonlocal n
        ph = re.split(r"(?<=[.!?])\s+", m.group(2)); vu = []; res = []
        for x in ph:
            k = re.sub(r"\W+", "", x.lower())
            if len(k) > 25 and k in vu: n += 1; continue
            vu.append(k); res.append(x)
        return m.group(1) + " ".join(res) + m.group(3)
    h = re.sub(r"(<p[^>]*>)([^<]*)(</p>)", dedup, h)
    return h, n

# ---- cibles de contraction -------------------------------------------------------------------------------------
def cibles(html, inv):
    from grille_agent import sections
    S = sections(re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", html)); L = []
    poids = sorted(((len(re.sub(r"<[^>]+>", " ", v).split()), p) for p, v in S.items()), reverse=True)[:5]
    L.append("POINTS LES PLUS LOURDS (mots) : " + ", ".join(f"point {p} = {w}" for w, p in poids))
    ph = inv["phrases"]
    for s, i, j in redites(ph, 0.7)[:8]: L.append(f"REDITE {s:.2f} : « {ph[i]['t'][:70]}… » ≈ « {ph[j]['t'][:70]}… » → garde la meilleure, fusionne")
    for x in sorted((x for x in ph if x["n"] != "tab" and x["w"] > 25), key=lambda x: -x["w"])[:8]:
        L.append(f"PHRASE LONGUE {x['w']} mots : « {x['t'][:110]}… » → scinde ou resserre, sans perdre l'explication")
    for x in nominales(ph)[:8]: L.append(f"PHRASE NOMINALE : « {x['t'][:90]} » → réécris-la avec un verbe")
    return L

# ---- commandes -----------------------------------------------------------------------------------------------
def chemins(lot, nom):
    wk = R / ".cache/travail" / f"LOT_{lot}"
    if os.environ.get("G14_TEST"): wk = R / ".cache/test_g14"
    d = wk / "contracte"; d.mkdir(parents=True, exist_ok=True)
    return wk, d / f"{nom}.snap.json", d / f"{nom}.visa.json"

def sha(t): return hashlib.sha256(t.encode()).hexdigest()[:16]

def main(ag, cmd, args):
    print(REGLE_ABSOLUE)
    from grille_agent import verifier_integrite, lot_actif; verifier_integrite()
    lot = lot_actif(); args = list(args)
    if "--lot" in args:
        i = args.index("--lot")
        if i + 1 >= len(args) or not re.fullmatch(r"\d{3}", args[i + 1]): print("ARGUMENT : --lot attend un numéro à 3 chiffres."); return 2
        lot = args[i + 1]; del args[i:i + 2]
    exc = set()
    if "--exceptions" in args:
        i = args.index("--exceptions")
        if i + 1 >= len(args) or args[i + 1].startswith("--"): print("ARGUMENT : --exceptions attend une liste « mot,mot » (10 au plus)."); return 2
        exc = {x.strip().lower() for x in args[i + 1].split(",") if x.strip()}; del args[i:i + 2]
        if len(exc) > 10: print(f"REFUSÉ : {len(exc)} exceptions > 10. Une exception = une notion conservée sous un synonyme, pas une perte."); return 1
    if cmd not in ("contracter", "verifier", "etat") or not args: print(__doc__); return 2
    f = Path(args[0]); nom = f.name
    rf = R / f"harnais/grille14/roster_{lot}.json"
    if not rf.exists(): print(f"LOT inconnu : {lot}. STOP."); return 2
    ro = json.loads(rf.read_text()); aud = ag.replace("K", "", 1)
    if nom not in ro["auditeurs"].get(aud, []): print(f"HORS TERRITOIRE : {nom} n'est pas à {aud}. STOP."); return 3
    wk, snapf, visaf = chemins(lot, nom)
    chemin = f.resolve() if f.exists() else wk / nom
    if not chemin.exists(): print(f"FICHIER INTROUVABLE : {nom}."); return 2
    from grille_agent import reparer
    h0 = chemin.read_text(encoding="utf-8", errors="replace")
    if cmd == "etat":
        s = json.loads(snapf.read_text()) if snapf.exists() else None; v = json.loads(visaf.read_text()) if visaf.exists() else None
        print(json.dumps(dict(fichier=nom, mots_actuels=len(texte(h0).split()), mots_entree=s and s["inv"]["mots"], visa=v, visa_valide=bool(v and v.get("sha") == sha(h0))), ensure_ascii=False, indent=1)); return 0
    if cmd == "contracter":
        if not snapf.exists():
            inv0 = inventaire(h0); snapf.write_text(json.dumps(dict(inv=inv0, t=time.strftime("%H:%M:%S")), ensure_ascii=False))
            print(f"INVENTAIRE pris à l'entrée : {inv0['mots']} mots, {len(inv0['nombres'])} nombres, {len(inv0['meds'])} médicaments, {len(inv0['unites'])} valeurs avec unité, "
                  f"{len(inv0['phrases'])} phrases dont {sum(1 for x in inv0['phrases'] if x['e'])} d'explication.")
        h, n = contraction_mecanique(h0)
        if h != h0:
            bak = R / ".cache/bak"; bak.mkdir(exist_ok=True); (bak / f"{ag}_{nom}_avant_contraction").write_text(h0, encoding="utf-8"); chemin.write_text(h, encoding="utf-8")
        print(f"CONTRACTION MÉCANIQUE (gratuite) : {n} formule(s) creuse(s) ou doublon(s) retiré(s) ; {len(texte(h0).split()) - len(texte(h).split())} mots en moins.")
        av = json.loads(snapf.read_text())["inv"]; mots = len(texte(h).split())
        print(f"GAIN (indicatif, jamais exigé) : {av['mots']} → {mots} mots (−{100 * (1 - mots / max(1, av['mots'])):.1f} %).")
        print("CIBLES (reformule plus concis ou retire une redite ; chaque notion, explication, négation, condition, seuil et unité reste) :")
        for l in cibles(h, inventaire(h)): print(" -", l)
        print("Puis : verifier <fichier>"); return 0
    if not snapf.exists(): print("Pas d'inventaire : lance d'abord `contracter`."); return 1
    h, rep = reparer(h0, lot, nom)
    if h != h0: chemin.write_text(h, encoding="utf-8")
    av = json.loads(snapf.read_text())["inv"]; ap = inventaire(h)
    pb, L = comparer(av, ap, exc)
    mots = ap["mots"]; red = 100 * (1 - mots / max(1, av["mots"]))
    L.append(f"gain (affiché, non exigé) : {av['mots']} → {mots} mots (−{red:.1f} %)")
    print("\n".join(L))
    if pb:
        visaf.unlink(missing_ok=True); print("REFUSÉ (règle absolue : rétablis ce qui manque, puis relance verifier) :\n - " + "\n - ".join(pb)); return 1
    visaf.write_text(json.dumps(dict(sha=sha(h), mots_avant=av["mots"], mots_apres=mots, reduction_pct=round(red, 1), exceptions=sorted(exc), agent=ag, t=time.strftime("%H:%M:%S")), ensure_ascii=False))
    print(f"VISA POSÉ : notions, sens et explications conservés (gain −{red:.1f} %). Lance `fin` de ton script d'auditeur sans modifier le fichier."); return 0

if __name__ == "__main__":
    if len(sys.argv) < 3: print(REGLE_ABSOLUE); print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3:]))
