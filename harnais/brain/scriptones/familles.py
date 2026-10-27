#!/usr/bin/env python3
"""BRAIN-HARNESS · familles des synapses α et β (moteur commun des 140 scriptones générés par outils/gabarit.py). Stdlib seule.

Zone α (grillage losangique, 14 synapses α1…α14, une par point de la GRILLE À 14 POINTS) : CONCISION et FORME, écrivain des corrections sûres.
  S structure du point · R récit négatif interdit · H phrases verbales · Q continuité (bloc, lignes séparées) · D termes dédiés, zéro méta-conception
Zone β (second grillage, β1…β14) : INDÉPENDANTE d'α par la méthode et par le but (relecture adverse) : EXHAUSTIVITÉ et FOND.
  X exhaustivité (contre la sur-contraction) · C cohérence chiffrée et unités · S sources du point · M contre-épreuve par mutation · L langue adverse
Chaque synapse lit SON point (paquet du collecteur) et n'écrit que dans SES zones (règle anti-conflit : un seul écrivain par zone) :
  αn·S → Pn:titre · αn·R → Pn:absence · α2·Q → P2:blocs · βn·C → Pn:typo-chiffres · βn·L → Pn:typo-texte ; toutes les autres sont lectrices.
Aucune famille ne crée de contenu médical ni n'invente un chiffre : une absence se tait (règle 5 de Vial), une lacune devient une doléance."""
import functools, html as H, json, random, re, sys
from pathlib import Path
D = Path(__file__).resolve().parent
if str(D) not in sys.path: sys.path.insert(0, str(D))
import bus

SYN = json.loads((D / "synapses.json").read_text(encoding="utf-8"))
P = {int(k): v for k, v in SYN["points"].items()}
FAM_A, FAM_B = list(SYN["familles_alpha"]), list(SYN["familles_beta"])
VERSION = "1.0.0"


class Ident:
    """Identité d'une synapse (ID, REGION) pour bus.doleance."""
    def __init__(self, ID, REGION): self.ID, self.REGION = ID, REGION


def ident(z, f, n):
    return Ident(f"{'a' if z == 'A' else 'b'}{n:02d}_{f}", "ALP" if z == "A" else "BET")


@functools.lru_cache(maxsize=1)
def verbes():
    try: return frozenset(json.loads((D / "verbes.json").read_text(encoding="utf-8"))["formes"])
    except (OSError, ValueError, KeyError): return frozenset()


# ───────────────────────── lecture d'un point ─────────────────────────
def zone(t, n):
    return bus.sections(t).get(n)


def titre(t, n):
    """(début, fin) de l'élément <h3> du point n."""
    z = zone(t, n)
    if not z: return None
    m = re.compile(r"(?is)<h3\b[^>]*>.*?</h3>").match(t, z[0])
    return (m.start(), m.end()) if m else (z[0], t.find(">", z[0]) + 1)


@functools.lru_cache(maxsize=32)
def _spans(t, motif):
    """Intervalles des éléments ouverts par `motif` (details, table, div.arb) : profondeur comptée sur le nom de balise."""
    out = []
    for m in re.finditer(motif, t):
        tag = re.match(r"<(\w+)", m.group(0)).group(1).lower(); k = 0
        for x in re.finditer(r"(?i)<(/?)%s\b[^>]*>" % tag, t[m.start():]):
            k += -1 if x.group(1) else 1
            if k == 0: out.append((m.start(), m.start() + x.end())); break
    return tuple(out)


def dans(spans, p):
    return any(a <= p < b for a, b in spans)


def details(t): return _spans(t, r"(?i)<details\b[^>]*>")
def arbres(t): return _spans(t, r'(?i)<details\b[^>]*class="arbre"[^>]*>|<div\b[^>]*class="arb"[^>]*>')
def tableaux(t): return _spans(t, r"(?i)<table\b[^>]*>")


def blocs(t, n, tags=("p", "li"), hors_details=False):
    """Blocs de texte du point n (hors fenêtres .df/.dxc et bandes) ; hors_details : seulement le texte affiché sans clic."""
    z = zone(t, n)
    if not z: return []
    Ar = arbres(t)
    B = [b for b in bus.blocs(t, z[0], z[1], tags) if not re.search(r"(?i)<(?:p|li)\b", b[2]) and not dans(Ar, b[0])]
    if hors_details:
        Dt = details(t); B = [b for b in B if not dans(Dt, b[0])]
    return B


ETIQ = re.compile(r"(?is)^\s*<(b|strong)>[^<]{0,80}?[.:]\s*</\1>\s*")
SOUS_TITRE = re.compile(r"^[•▪◦–\s-]*\d{1,2}(?:\.[\dA-Za-z]+)+\b|^[•▪◦–\s-]*[A-Z]\s?[.)-]\s")


def phrases(t, n, tags=("p", "li"), hors_details=False):
    """[(position du bloc, phrase visible)] du point n : étiquettes de tête (« Amorce. »), sous-titres (« 11.B Moyens »), libellés « … : » exclus."""
    out = []
    for pa, pf, inner in blocs(t, n, tags, hors_details):
        inner = ETIQ.sub("", inner)
        for ph in bus.phrases(bus.texte_visible(inner)):
            ph = re.sub(r"^[•▪◦–-]\s*", "", ph).strip()
            if not ph or SOUS_TITRE.match(ph) or ph.endswith(":"): continue
            out.append((pa, ph))
    return out


def texte_point(t, n, complet=True):
    z = zone(t, n)
    if not z: return ""
    seg = bus.masque(t[z[0]:z[1]], bus.RX_STYLE)
    return bus.texte(seg) if complet else bus.texte_visible(seg)


# ───────────────────────── carte texte visible ↔ HTML (suppression sûre d'une phrase) ─────────────────────────
VIDES_TAG = {"br", "img", "wbr", "hr", "input", "meta", "link", "col", "source"}


def _caches(inner):
    """Intervalles cachés d'un bloc : fenêtres .df/.dxc et exposants de source (ne font pas partie de la phrase lue)."""
    out = []
    for m in re.finditer(r'(?i)<(span|sup)\b[^>]*class="(?:df|dxc|r)"[^>]*>', inner):
        tag = m.group(1).lower(); k = 0
        for x in re.finditer(r"(?i)<(/?)%s\b[^>]*>" % tag, inner[m.start():]):
            k += -1 if x.group(1) else 1
            if k == 0: out.append((m.start(), m.start() + x.end())); break
    return out


def carte(inner):
    """(texte visible V, début HTML de chaque caractère, fin HTML de chaque caractère)."""
    C = _caches(inner); V = []; deb = []; fin = []
    for m in re.finditer(r"<[^>]*>|&#?\w+;|[^<&]+|[<&]", inner):
        x = m.group(0)
        if dans(C, m.start()) or x.startswith("<") and len(x) > 1: continue
        if x.startswith("&") and x.endswith(";"):
            c = H.unescape(x); V.append(c[:1] or " "); deb.append(m.start()); fin.append(m.end()); continue
        for i, c in enumerate(x): V.append(c); deb.append(m.start() + i); fin.append(m.start() + i + 1)
    return "".join(V), deb, fin


def equilibre(frag):
    k = {}
    for m in re.finditer(r"<(/?)([a-zA-Z][\w-]*)[^>]*?(/?)>", frag):
        tag = m.group(2).lower()
        if tag in VIDES_TAG or m.group(3): continue
        k[tag] = k.get(tag, 0) + (-1 if m.group(1) else 1)
    return all(v == 0 for v in k.values())


def segments(V):
    """[(début, fin)] des phrases de V (positions dans V)."""
    prot = re.sub(bus.ABREV, lambda m: m.group(0).replace(".", "\x00"), V)
    prot = re.sub(r"(?<=\d)\.(?=\d)", "\x00", prot)
    out = []; k = 0
    for m in re.finditer(r"(?<=[.!?])\s+(?=[A-ZÀ-ÖØ-Ý«(\d])", prot):
        out.append((k, m.start())); k = m.end()
    out.append((k, len(V)))
    res = []
    for a, b in out:
        while a < b and V[a].isspace(): a += 1
        while b > a and V[b - 1].isspace(): b -= 1
        if b > a: res.append((a, b))
    return res


def phrases_html(inner):
    """[(début HTML, fin HTML, texte)] de chaque phrase d'un bloc ; bornes étendues aux balises ouvertes ou fermées au ras de la phrase."""
    V, deb, fin = carte(inner); out = []
    for a, b in segments(V):
        hs, he = deb[a], fin[b - 1]
        for _ in range(6):
            if equilibre(inner[hs:he]): break
            m = re.search(r"(?s)<[a-zA-Z][^>]*>\s*$", inner[:hs]); m2 = re.match(r"(?s)\s*</[a-zA-Z][^>]*>", inner[he:])
            if m2 and not equilibre(inner[hs:he]) and inner[hs:he].count("<") > inner[hs:he].count("</") * 2: he += m2.end(); continue
            if m: hs = m.start()
            elif m2: he += m2.end()
            else: break
        out.append((hs, he, V[a:b]))
    return out


# ───────────────────────── outils de mutation (communs) ─────────────────────────
def _p_haut(t, n):
    """Blocs <p> du point n affichés sans clic (hors tableaux, details, fenêtres), dans l'ordre."""
    Tb = tableaux(t); return [b for b in blocs(t, n, ("p",), True) if not dans(Tb, b[0])]


def inserer(t, n, html_phrase, r, nouveau=False):
    """Ajoute une phrase à la fin d'un <p> du point n (ou un nouveau <p> après le titre)."""
    B = _p_haut(t, n)
    if B and not nouveau:
        pa, pf, inner = r.choice(B); q = t.rindex("</p>", pa, pf); return t[:q] + " " + html_phrase + t[q:]
    h = titre(t, n); return t[:h[1]] + "<p>" + html_phrase + "</p>" + t[h[1]:]


def texte_sub(seg, rx, rep, flags=0):
    """Applique une substitution au texte seulement (jamais aux balises ni aux styles)."""
    prot = bus.masque(seg, bus.RX_STYLE)
    out = []; k = 0
    for m in re.finditer(r"<[^>]*>", prot):
        out.append(re.sub(rx, rep, seg[k:m.start()], flags=flags) if k < m.start() else ""); out.append(seg[m.start():m.end()]); k = m.end()
    out.append(re.sub(rx, rep, seg[k:], flags=flags))
    return "".join(out)


def sur_point(t, n, fn, avec_titre=False):
    z = zone(t, n)
    if not z: return t
    a = z[0] if avec_titre else titre(t, n)[1]
    return t[:a] + fn(t[a:z[1]]) + t[z[1]:]


def retirer(t, n, rx):
    """Retire d'un point ce qui satisfait rx : l'élément entier pour un motif de balise, le texte sinon."""
    z = zone(t, n); h = titre(t, n)
    if not z: return t
    seg = t[h[1]:z[1]]
    if rx.lstrip("(?is)").startswith("<"):
        while True:
            m = re.search(rx, seg)
            if not m: break
            tag = re.match(r"<(\w+)", seg[m.start():m.start() + 40]).group(1).lower(); k = 0; fin = len(seg)
            for x in re.finditer(r"(?i)<(/?)%s\b[^>]*>" % tag, seg[m.start():]):
                k += -1 if x.group(1) else 1
                if k == 0: fin = m.start() + x.end(); break
            seg = seg[:m.start()] + seg[fin:]
    else:
        seg = texte_sub(seg, rx, " ")
    return t[:h[1]] + seg + t[z[1]:]


# ═════════════════════════ ZONE α ═════════════════════════
# ── α·S structure du point ──
def a_S(me, n, t, nom, opt):
    D, p = [], P[n]; z = zone(t, n); M = dict(present=bool(z))
    if not z:
        a0 = bus.bornes_cours(t)[0]
        D.append(bus.doleance(me, "AS1", nom, bus.ancre(t, a0, f"{n}. {p['titre']}"), "CRITIQUE", f"point {n} « {p['titre']} » absent (aucun titre <h3> « {n}. … »)",
                              f"écrire le point {n} « {p['titre']} » à sa place, titre <h3><strong>{n}. {p['titre']}</strong></h3>, selon la GRILLE À 14 POINTS", "agent"))
        return D, M
    h = titre(t, n); th = t[h[0]:h[1]]
    if not re.search(r"(?i)<(?:strong|b)\b", th):
        D.append(bus.doleance(me, "AS2", nom, bus.ancre(t, h[0], bus.texte(th)), "MOYEN", f"titre du point {n} sans gras (règle de forme de la grille)",
                              f"mettre le titre en <strong> : a{n:02d}_S --appliquer", "script", th[:120]))
    a, f = bus.bornes_cours(t)
    titres = [m.start() for m in re.finditer(r"<h3[^>]*>\s*(?:<(?:strong|b)>)?\s*%d\.\s" % n, t[a:f])]
    if len(titres) > 1:
        D.append(bus.doleance(me, "AS3", nom, bus.ancre(t, a + titres[1], f"{n}."), "GRAVE", f"point {n} présent {len(titres)} fois",
                              f"fusionner les doublons du point {n} en un seul point (aucune notion retranchée)", "agent"))
    S = bus.sections(t)
    if n > 1 and (n - 1) in S and S[n - 1][0] > z[0]:
        D.append(bus.doleance(me, "AS5", nom, bus.ancre(t, z[0], f"{n}."), "MOYEN", f"point {n} placé avant le point {n - 1}", f"replacer le point {n} après le point {n - 1}", "agent"))
    seg = t[h[1]:z[1]]; manq = []
    for lab, rx in p.get("requis", []):
        if not re.search(rx, seg):
            manq.append(lab)
            D.append(bus.doleance(me, "AS4", nom, bus.ancre(t, h[0], f"{n}. {p['titre']}"), "GRAVE", f"point {n} : {lab} absent",
                                  f"ajouter au point {n} : {lab} (contenu sourcé ; jamais inventé)", "agent", f"motif {rx[:80]}"))
    M.update(requis=len(p.get("requis", [])), requis_absents=manq)
    return D, M


def c_S(n, t, opt):
    h = titre(t, n)
    if not h: return t
    th = t[h[0]:h[1]]
    if re.search(r"(?i)<(?:strong|b)\b", th): return t
    m = re.match(r"(?is)(<h3\b[^>]*>)(.*?)(</h3>)", th)
    return t[:h[0]] + m.group(1) + "<strong>" + m.group(2).strip() + "</strong>" + m.group(3) + t[h[1]:] if m else t


def m_S(n):
    def absent(t, r):
        h = titre(t, n); th = t[h[0]:h[1]]; inner = re.sub(r"^\s*(?:<(?:strong|b)>)?\s*\d{1,2}\.\s*", "", re.sub(r"(?is)^<h3[^>]*>|</h3>$", "", th))
        return t[:h[0]] + "<h4>" + inner + "</h4>" + t[h[1]:]
    def maigre(t, r):
        h = titre(t, n); th = re.sub(r"(?i)</?(?:strong|b)>", "", t[h[0]:h[1]]); return t[:h[0]] + th + t[h[1]:]
    def doublon(t, r):
        h = titre(t, n); z = zone(t, n); return t[:z[1]] + t[h[0]:h[1]] + "<p>Ce point reprend le précédent.</p>" + t[z[1]:]
    L = [("point absent", absent, "AS1"), ("titre sans gras", maigre, "AS2"), ("point en double", doublon, "AS3")]
    for lab, rx in P[n].get("requis", []):
        L.append((f"requis absent : {lab}", (lambda rx: lambda t, r: retirer(t, n, rx))(rx), "AS4"))
    return L


# ── α·R récit négatif interdit ──
NEG = re.compile(r"(?i)\b(?:"
                 r"(?:n['’](?:a|ont|est|sont)|ne (?:sont|est)) pas (?:encore |non plus |été |encore été |non plus été )*(?:lue?s?|relue?s?|vérifiée?s?|retrouvée?s?|trouvée?s?|chiffrée?s?|quantifiée?s?|publiée?s?|documentée?s?|disponibles?|connue?s?|sourcée?s?|établie?s?)"
                 r"|non (?:encore )?(?:lue?s?|relue?s?|chiffrée?s?|quantifiée?s?|sourcée?s?|retrouvée?s?|vérifiée?s?|trouvée?s?|documentée?s?)"
                 r"|(?:à|a) vérifier|reste(?:nt)? à (?:vérifier|confirmer|préciser|chiffrer|documenter|lire)"
                 r"|aucun(?:e|s|es)? (?:chiffres?|sources?|statistiques?|estimations?|registres?)\b"
                 r"|aucune? données? (?:suisses?|européennes?|spécifiques?|chiffrées?|publiées?|fiables?|épidémiologiques?|disponibles?|nationales?|locales?|lues?|n['’])"
                 r"|(?:pas|peu) de (?:chiffres?|données?) (?:suisses?|européennes?|spécifiques?|chiffrées?|publiées?|fiables?|disponibles?|nationales?)"
                 r"|données? (?:non|pas) (?:trouvée?s?|disponibles?)|dans les sources consultées|faute de (?:sources?|données?|chiffres?)"
                 r"|fréquence non quantifiée|non disponible dans les sources)")
DONNEE = re.compile(r"(?i)\b(?:chiffres?|données?|incidences?|prévalences?|fréquences?|mortalités?|létalités?|taux|statistiques?|registres?|sources?|estimations?|valeurs?|proportions?|pourcentages?|épidémiolog\w*|nombres?)\b")
FAIBLE = re.compile(r"(?i)(?:n['’](?:a|est|ont|sont)|ne (?:sont|est)) pas (?:encore |non plus |été )*(?:connue?s?|disponibles?|établie?s?|documentée?s?)")
DOSE = re.compile(r"(?i)posolog|\bdoses?\b|\bmg\b|µg|\bUI\b|AIPS|swissmedic|®")
GENERIQUE = set("suisse suisses europe europé nation nation canton annuel ofs ofsp obsan oms who regist plus encore non aussi lue lues relue relues lu lus vérifi chiffr "
                "quantif publié publiée disponi trouvé trouvée retrou docume connue connu sourcé établi spécif fiable consul source donnée donnée chiffre incide préval "
                "fréque mortal létali taux statis estima valeur propor pource épidém nombre reste confir préci aucun aucune faute dans".split())


def negatif(ph):
    m = NEG.search(ph)
    if not m: return None
    if FAIBLE.fullmatch(m.group(0)) and not DONNEE.search(ph): return None     # « Le mécanisme n'est pas connu » : un fait médical, pas un récit négatif
    return m.group(0)


def pure(ph):
    """Phrase d'absence pure : sans chiffre ni dose, et sans notion autre que la donnée absente (≤ 2 mots de contenu résiduels)."""
    if re.search(r"\d", ph) or DOSE.search(ph): return False
    reste = {w for w in bus.jetons(NEG.sub(" ", ph)) if w not in GENERIQUE and not DONNEE.match(w)}
    return len(reste) <= 2


def candidats_R(t, n):
    """[(début absolu, fin absolue, phrase, type)] : type pure (supprimable), mixte, dose, fenetre."""
    out = []
    z = zone(t, n)
    if not z: return out
    Tb = tableaux(t)
    for pa, pf, inner in blocs(t, n, ("p", "li", "td")):
        tag = re.match(r"<(\w+)", t[pa:pa + 5]).group(1).lower(); off = t.index(">", pa) + 1
        for hs, he, ph in phrases_html(inner):
            if not negatif(ph): continue
            apres = inner[he:he + 80]
            ok = tag == "p" and not dans(Tb, pa) and re.search(r"[.!?]$", ph) and pure(ph) and equilibre(inner[hs:he]) and 'class="r"' not in re.split(r"[A-Za-zÀ-ÿ]", apres, 1)[0]
            typ = "pure" if ok else ("dose" if DOSE.search(ph) and n == 11 or DOSE.search(ph) and "AIPS" in ph else "mixte")
            out.append((off + hs, off + he, ph, typ, pa))
    # fenêtres du point (contenu caché) : jamais supprimé par script
    seg = t[z[0]:z[1]]
    for m in re.finditer(r'(?s)<span class="(?:df|dxc)">(.*?)</span>', seg):
        for ph in bus.phrases(bus.texte(m.group(1))):
            if negatif(ph): out.append((z[0] + m.start(), z[0] + m.end(), ph, "fenetre", z[0] + m.start()))
    return out


def a_R(me, n, t, nom, opt):
    D, C = [], candidats_R(t, n); k = {"pure": 0, "mixte": 0, "dose": 0, "fenetre": 0}
    for a, b, ph, typ, _ in C:
        k[typ] += 1; f = negatif(ph)
        if typ == "pure":
            D.append(bus.doleance(me, "AR1", nom, bus.ancre(t, a, ph), "GRAVE", f"récit négatif au point {n} : « {f} » (règle 5 de Vial : l'absence se tait)",
                                  f"supprimer la phrase entière (aucun chiffre ni notion perdus) : a{n:02d}_R --appliquer ; la lacune reste au registre HELP", "script", ph[:200]))
        elif typ == "dose":
            D.append(bus.doleance(me, "AR3", nom, bus.ancre(t, a, ph), "GRAVE", f"dose ou posologie laissée « {f} » au point {n}",
                                  "lire l'AIPS suisse (python3 harnais/aips_texte.py --nom <spécialité> --section posologie) et écrire la dose lue ; sinon retirer la mention de dose. Jamais de dose de mémoire", "agent", ph[:200]))
        elif typ == "mixte":
            reste = re.sub(r"\s+([,;:.])", r"\1", NEG.sub("", ph)).strip(" ;:,")
            D.append(bus.doleance(me, "AR2", nom, bus.ancre(t, a, ph), "GRAVE", f"récit négatif dans une phrase porteuse au point {n} : « {f} »",
                                  f"réécrire en ne disant que ce qui est trouvé (chiffre suisse, sinon européen ou international valide) ; retirer « {f} » sans toucher au reste : « {reste[:120]} »", "agent", ph[:200]))
        else:
            D.append(bus.doleance(me, "AR4", nom, bus.ancre(t, a, ph), "MOYEN", f"récit négatif dans une fenêtre du point {n} : « {f} »",
                                  "retirer la phrase d'absence de la fenêtre ; garder le reste de la fenêtre intact", "agent", ph[:200]))
    return D, dict(recits_negatifs=sum(k.values()), **{f"recits_{x}": v for x, v in k.items()})


def c_R(n, t, opt):
    """Supprime les phrases d'absence pures (dans les <p> du point n), de la fin vers le début ; un <p> vidé disparaît avec elles."""
    for a, b, ph, typ, pa in sorted(candidats_R(t, n), key=lambda x: -x[0]):
        if typ != "pure": continue
        if re.match(r"\s*</p>", t[b:]):           # dernière phrase du bloc : retirer l'espace qui précède
            k = a
            while k > pa and t[k - 1] in " \t\n": k -= 1
            t = t[:k] + t[b:]
        else: t = t[:a] + t[b + len(re.match(r"\s*", t[b:]).group(0)):]
        m = re.compile(r"(?is)<p\b[^>]*>((?:(?!</?p\b).)*)</p>").match(t, pa)
        if m and not bus.texte(m.group(1)).strip(): t = t[:pa] + t[m.end():]
    return t


NEG_PURES = ["Aucun chiffre suisse n'a été lu.", "L'incidence suisse n'a pas été lue : À vérifier.", "La prévalence européenne reste à vérifier.",
             "Aucune donnée spécifique n'est publiée pour ce groupe.", "Le taux de récidive n'est pas chiffré.", "La mortalité suisse n'a pas non plus été relue.",
             "Les données suisses ne sont pas disponibles."]


def m_R(n):
    L = [("phrase d'absence pure", lambda t, r: inserer(t, n, r.choice(NEG_PURES), r), "AR1"),
         ("phrase porteuse avec absence", lambda t, r: inserer(t, n, f"La létalité atteint {r.randint(2, 40)} % chez l'adulte ; le chiffre suisse n'a pas été lu.", r), "AR2"),
         ("absence dans une fenêtre", lambda t, r: inserer(t, n, '<span class="tm" tabindex="0">registre<span class="df">Aucune donnée suisse n\'a été lue.</span></span> national', r), "AR4")]
    if P[n].get("doses"):
        L.append(("dose à vérifier", lambda t, r: inserer(t, n, f"La posologie pédiatrique de l'Adrénaline® reste à vérifier dans l'AIPS.", r), "AR3"))
    return L


# ── α·H phrases verbales et longueur ──
SUJETS = re.compile(r"(?i)\b(?:qui|il|elle|ils|elles|on|cela|ceci|ce|ne|n['’]|se|s['’]|y)\s+([a-zà-ÿ]+)")
DET = r"(?:le|la|les|l['’]|un|une|des|ce|cet|cette|ces|son|sa|ses|leur|leurs|chaque|tout|toute|tous|toutes|aucun|aucune)"
SUITE = r"(?:le|la|les|l['’]|un|une|des|du|de|d['’]|à|au|aux|en|par|pour|sur|dans|avec|sans|vers|chez|sous|entre|que|qu['’]|si|pas|plus|moins|très|\d|[a-zà-ÿ]+ment\b|[,.;:]|$)"
RX_SV = re.compile(r"(?i)\b%s\s+(?:[\w’'()-]+\s+){0,4}?([a-zà-ÿ]{3,}(?:e|ent|it|ait|aient|ont|ra|ront|ut|ue))\s*%s" % (DET, SUITE))
NON_VERBE = re.compile(r"(?:ique|ale|elle|ive|euse|aire|ée|ible|able|ienne|ème|ure|ance|ence|ie|té|ose|ite|ome|ine|ole|isme|ide|ate|gie|thie|émie|ase|ège|ane|one|ule|ève|ade|age|ette|ire|èle|ette|ude|ure|tre|bre|cle|gue|que)$")


def _infinitif(w, V):
    if w.endswith("er"): s = w[:-2]; return any(s + x in V for x in ("e", "ent", "ait", "era", "ent"))
    if w.endswith("ir"): return w[:-1] + "t" in V or w[:-2] + "issent" in V or w[:-2] + "it" in V
    if w.endswith("re"): return w[:-2] + "t" in V or w[:-1] + "nt" in V or w[:-3] + "t" in V
    return False


def verbale(ph):
    """Phrase verbale ? (stdlib) : forme finie du lexique (verbes.json, tiré de spaCy sur 177 cours) ; « sujet + mot à désinence verbale + suite » ;
    pronom sujet + verbe ; consigne à l'infinitif (« Poser une voie veineuse. ») ; flèche ou question."""
    if "→" in ph or "?" in ph or "⇒" in ph: return True
    V = verbes(); mots = re.findall(r"[a-zà-ÿœ]+(?:['’][a-zà-ÿ]+)?", ph.lower())
    if any(w in V or w.split("'")[-1].split("’")[-1] in V for w in mots): return True
    if mots and _infinitif(mots[0], V): return True
    if any(not NON_VERBE.search(m.group(1).lower()) for m in RX_SV.finditer(ph)): return True
    return any(m.group(1) not in bus.VIDES and len(m.group(1)) > 2 for m in SUJETS.finditer(ph))


def a_H(me, n, t, nom, opt):
    D = []; nom_ = longs = 0; L = phrases(t, n); cap = 10 ** 6 if opt.get("sans_plafond") else 12
    for pa, ph in L:
        nm = len(ph.split())
        if nm >= 4 and not verbale(ph) and not re.match(r"[a-zà-ÿ]", ph):       # « critère a ; » : suite d'une phrase introduite par « : »
            nom_ += 1
            if nom_ <= cap:
                D.append(bus.doleance(me, "AH1", nom, bus.ancre(t, pa, ph), "MOYEN", f"phrase nominale au point {n} (aucun verbe conjugué)",
                                      "réécrire en phrase verbale (sujet + verbe conjugué), sans retrancher aucune notion ni aucun chiffre", "agent", ph[:200]))
        if nm > 35:
            longs += 1
            D.append(bus.doleance(me, "AH2", nom, bus.ancre(t, pa, ph), "MOYEN", f"phrase de {nm} mots au point {n} (cible 8 à 20 mots)",
                                  "scinder en deux ou trois phrases verbales reliées par un connecteur (car, donc, alors que) ; tout reste", "agent", ph[:200]))
    if nom_ > cap:
        D.append(bus.doleance(me, "AH1", nom, bus.ancre(t, zone(t, n)[0], f"{n}."), "MOYEN", f"{nom_ - 12} autres phrases nominales au point {n}",
                              "réécrire chaque phrase nominale du point en phrase verbale", "agent", f"{nom_} au total"))
    mots = [len(ph.split()) for _, ph in L]
    return D, dict(phrases=len(L), nominales=nom_, longues=longs, mots_moyens=round(sum(mots) / max(1, len(mots)), 1))


NOMINALES = ["Surveillance clinique rapprochée et bilan biologique complet.", "Prise en charge multidisciplinaire précoce du patient.",
             "Évaluation initiale de la gravité selon le stade clinique.", "Bilan biologique complet et imagerie thoracique de contrôle."]
LONGUE = ("Le médecin évalue la température centrale, la conscience, le rythme cardiaque, la ventilation, la glycémie, la natrémie, la kaliémie, "
          "les lactates, la fonction rénale et la coagulation avant de décider du lieu de transfert du patient vers un centre adapté à sa gravité et à son âge.")


def m_H(n):
    return [("phrase nominale", lambda t, r: inserer(t, n, r.choice(NOMINALES), r), "AH1"),
            ("phrase trop longue", lambda t, r: inserer(t, n, LONGUE, r), "AH2")]


# ── α·Q continuité ──
def _p_bloc2(t, n):
    """<p> affichés du point n hors tableaux, details, listes et divs : candidats à la fusion en un seul bloc."""
    z = zone(t, n); Tb = tableaux(t); Dt = details(t)
    L = _spans(t, r"(?i)<(?:ul|ol)\b[^>]*>"); Dv = _spans(t, r'(?i)<div\b(?![^>]*class="(?:tw|ox)")[^>]*>')
    return [b for b in blocs(t, n, ("p",)) if not dans(Tb, b[0]) and not dans(Dt, b[0]) and not dans(L, b[0])
            and not any(a < b[0] < e and a > z[0] for a, e in Dv)]


def _fusionnable(inner):
    return not re.search(r"(?i)<(?:p|div|ul|ol|table|details|h\d)\b", inner) and re.search(r"[.!?»)]\s*(?:<sup class=\"r\">.*?</sup>)?\s*(?:</[^>]+>\s*)*$", inner.strip())


def a_Q(me, n, t, nom, opt):
    D = []; c = P[n].get("continuite", {}); M = {}
    if not zone(t, n): return D, M
    if c.get("bloc"):
        B = _p_bloc2(t, n); Z = zone(t, n); seg = t[titre(t, n)[1]:Z[1]]
        lis = [m for m in re.finditer(r"(?is)<(ul|ol)\b.*?</\1>", seg) if not dans(details(t), titre(t, n)[1] + m.start()) and not dans(tableaux(t), titre(t, n)[1] + m.start())]
        brs = sum(len(re.findall(r"(?i)<br\s*/?>", b[2])) for b in B)
        M.update(blocs=len(B), listes=len(lis), sauts=brs)
        if len(B) > 1 or brs:
            ok = all(_fusionnable(b[2]) for b in B) and not brs
            D.append(bus.doleance(me, "AQ1", nom, bus.ancre(t, B[1][0] if len(B) > 1 else B[0][0], bus.texte_visible(B[-1][2])[:60]), "GRAVE",
                                  f"point {n} en {len(B)} paragraphes{' et ' + str(brs) + ' sauts de ligne' if brs else ''} : un seul bloc de phrases continues est exigé (doléance 4 de Vial)",
                                  f"fusionner en un seul bloc : a{n:02d}_Q --appliquer (aucun mot retranché) ; puis relier par des connecteurs logiques" if ok else
                                  "réécrire le point en un seul paragraphe de phrases continues (3 à 4 lignes), chiffres sourcés entre parenthèses ; le détail chiffré va dans le tableau",
                                  "script" if ok else "agent", f"{len(B)} <p>"))
        if lis:
            D.append(bus.doleance(me, "AQ1", nom, bus.ancre(t, titre(t, n)[1] + lis[0].start(), "liste"), "GRAVE", f"point {n} écrit en liste : lignes séparées",
                                  "réécrire la liste en phrases continues dans le bloc unique du point (chaque chiffre garde sa source)", "agent", bus.texte(lis[0].group(0))[:160]))
        et = [b for b in B if ETIQ.match(b[2]) or re.search(r"(?is)[.!?]\s*<(b|strong)>[^<]{0,60}[.:]</\1>", b[2])]
        for b in et[:3]:
            D.append(bus.doleance(me, "AQ2", nom, bus.ancre(t, b[0], bus.texte_visible(b[2])[:60]), "MOYEN", f"étiquette en gras en tête de phrase au point {n} (allure de brouillon)",
                                  "remplacer l'étiquette par une phrase verbale reliée à la précédente par un connecteur (aucune notion retranchée)", "agent", bus.texte(b[2])[:160]))
    if c.get("phrases"):
        k = len(phrases(t, n)); lo, hi = c["phrases"]; M["phrases"] = k
        if not lo <= k <= hi:
            D.append(bus.doleance(me, "AQ3", nom, bus.ancre(t, zone(t, n)[0], f"{n}."), "MOYEN", f"point {n} : {k} phrases (attendu {lo} à {hi})",
                                  f"{'regrouper' if k > hi else 'compléter'} pour obtenir {lo} à {hi} phrases courtes, verbales, mémorisables, chacune portant une décision ou un fait critique", "agent"))
    if c.get("hache"):
        B = _p_bloc2(t, n); serie = []; hache = 0
        for i, b in enumerate(B + [None]):
            court = b is not None and len(bus.phrases(bus.texte_visible(b[2]))) <= 1 and len(bus.texte_visible(b[2]).split()) <= 14 \
                and (not serie or re.fullmatch(r"\s*", bus.masque(t[serie[-1][1]:b[0]], bus.RX_STYLE)))
            if court: serie.append(b); continue
            if len(serie) >= c["hache"]:
                hache += 1
                D.append(bus.doleance(me, "AQ4", nom, bus.ancre(t, serie[0][0], bus.texte_visible(serie[0][2])), "MOYEN", f"{len(serie)} lignes isolées d'une phrase au point {n} : texte haché",
                                      "relier ces phrases en un paragraphe par des connecteurs logiques (car, donc, alors que), sans rien retrancher", "agent", " | ".join(bus.texte_visible(x[2])[:40] for x in serie)))
            serie = [b] if court else []
        M["hache"] = hache
    return D, M


def c_Q(n, t, opt):
    c = P[n].get("continuite", {})
    if not c.get("bloc"): return t
    B = _p_bloc2(t, n)
    if len(B) < 2 or not all(_fusionnable(b[2]) for b in B) or any(re.search(r"(?i)<br", b[2]) for b in B): return t
    corps = " ".join(b[2].strip() for b in B)
    for pa, pf, inner in sorted(B[1:], key=lambda b: -b[0]):
        e = pf + len(re.match(r"\s*", t[pf:]).group(0)); t = t[:pa] + t[e:]
    pa, pf, inner = B[0]; ouv = t[pa:t.index(">", pa) + 1]
    return t[:pa] + ouv + corps + "</p>" + t[pf:]


def m_Q(n):
    c = P[n].get("continuite", {}); L = []
    if c.get("bloc"):
        def scinde(t, r):
            pa, pf, inner = _p_bloc2(t, n)[0]; S = phrases_html(inner)
            if len(S) < 2: return t
            off = t.index(">", pa) + 1; k = off + S[r.randrange(1, len(S))][0]
            return t[:k] + "</p><p>" + t[k:]
        L.append(("bloc scindé en lignes", scinde, "AQ1"))
        L.append(("étiquette en tête", lambda t, r: inserer(t, n, "", r, True).replace("<p></p>", "<p><strong>Âge et sexe.</strong> La fréquence augmente avec l'âge.</p>", 1), "AQ2"))
    if c.get("phrases"):
        L.append(("trop de points clés", lambda t, r: inserer(t, n, " ".join(["Le froid ralentit le cœur.", "Le réchauffement suit le stade.", "La sonde mesure la température.",
                                                                               "Le transport reste doux.", "Le patient froid n'est pas mort."]), r), "AQ3"))
    if c.get("hache"):
        def hache(t, r):
            h = titre(t, n); B = _p_haut(t, n); q = B[-1][1] if B else h[1]
            return t[:q] + "<p>Le pouls ralentit.</p><p>La peau pâlit.</p><p>Le patient frissonne.</p>" + t[q:]
        L.append(("texte haché", hache, "AQ4"))
    return L


# ── α·D termes dédiés, zéro méta-conception ──
CONCEPTION = re.compile(r"(?i)\bLOT[_ ]?\d|\bPhase [AB]\b|\bDX\.\d+|\bcheckpoint\b|\brédacteur|\bauditeur|\bautre IA\b|\bune IA\b|intelligence artificielle|"
                        r"\bcycle \d\b|\bbrouillon\b|\bevidence\b|\bce fichier\b|\ble fichier\b|date de rédaction|sources lues et datées|dose AIPS prime|\bgabarit\b|\bprompt\b")


def a_D(me, n, t, nom, opt):
    D = []; z = zone(t, n); M = {}
    if not z: return D, M
    h = titre(t, n); seg = bus.masque(t[h[1]:z[1]], bus.RX_STYLE); txt = bus.texte(seg)
    for m in list(CONCEPTION.finditer(txt))[:5]:
        e = txt[max(0, m.start() - 40):m.end() + 40]
        D.append(bus.doleance(me, "AD1", nom, bus.ancre(t, h[1], e), "GRAVE", f"mention de conception « {m.group(0)} » au point {n} : le texte est le cours, pas sa fabrication",
                              "réécrire la phrase en langage de cours, sans parler du fichier, du LOT, de l'audit ni de l'IA ; garder la notion médicale", "agent", e))
    tm = len(re.findall(r'class="tm(?: med)?"(?![^>]*data-auto)', seg)); M["termes"] = tm
    if tm < P[n].get("termes_min", 0):
        D.append(bus.doleance(me, "AD2", nom, bus.ancre(t, h[0], f"{n}."), "MOYEN", f"point {n} : {tm} terme cliquable (au moins {P[n]['termes_min']} attendu)",
                              "rendre cliquables les termes techniques du point : <span class=\"tm\" tabindex=\"0\">terme<span class=\"df\">définition brève sourcée</span></span>", "agent"))
    if P[n].get("fenetres_interdites") and tm:
        D.append(bus.doleance(me, "AD3", nom, bus.ancre(t, h[1], "fenêtre"), "MOYEN", f"{tm} fenêtre(s) au point {n} : une fenêtre coupe la phrase porteuse (Q13.1)",
                              "retirer les fenêtres du point 13 (le terme reste en clair, sa définition vit dans les autres points)", "agent"))
    if re.search(r'(?i)class="tm|<a\b|class="ab"', t[h[0]:h[1]]):
        D.append(bus.doleance(me, "AD4", nom, bus.ancre(t, h[0], f"{n}."), "GRAVE", f"mot cliquable dans le titre du point {n} (interdit)",
                              "retirer la fenêtre du titre et la placer à la première occurrence du terme dans le texte", "agent"))
    return D, M


def m_D(n):
    L = [("mention de conception", lambda t, r: inserer(t, n, r.choice(["Ce fichier du LOT_008 reprend la Phase A.", "Le rédacteur a vérifié cette dose au cycle 2.",
                                                                       "Une autre IA a écrit ce passage."]), r), "AD1"),
         ("mot cliquable dans le titre", lambda t, r: (lambda h: t[:h[1] - 5] + '<span class="tm" tabindex="0">clé<span class="df">mot</span></span>' + t[h[1] - 5:])(titre(t, n)), "AD4")]
    if P[n].get("termes_min"):
        L.append(("termes rendus muets", lambda t, r: sur_point(t, n, lambda s: re.sub(r'(?s)<span class="tm(?: med)?" tabindex="0">((?:(?!<span).)*?)<span class="df">(?:(?!</span>).)*</span></span>', r"\1", s)), "AD2"))
    if P[n].get("fenetres_interdites"):
        L.append(("fenêtre dans un point clé", lambda t, r: inserer(t, n, 'Le <span class="tm" tabindex="0">réchauffement<span class="df">apport de chaleur</span></span> suit le stade.', r), "AD3"))
    return L


# ═════════════════════════ ZONE β ═════════════════════════
# ── β·X exhaustivité ──
def b_X(me, n, t, nom, opt):
    D = []; z = zone(t, n)
    if not z: return D, dict(mots=0)
    txt = texte_point(t, n); mots = len(txt.split()) - len(P[n]["titre"].split()) - 1
    if mots < P[n]["plancher"]:
        D.append(bus.doleance(me, "BX1", nom, bus.ancre(t, z[0], f"{n}."), "GRAVE", f"point {n} réduit à {mots} mots (plancher {P[n]['plancher']}) : omission ou contraction excessive",
                              f"compléter le point {n} selon la grille ({P[n]['titre']}) ; une notion contractée doit être rétablie (règle absolue de la contraction)", "agent", f"{mots} mots"))
    absentes = []
    for lab, rx in P[n].get("notions", []):
        if not re.search(rx, txt) and not re.search(rx, bus.masque(t[z[0]:z[1]], bus.RX_STYLE)):
            absentes.append(lab)
            D.append(bus.doleance(me, "BX2", nom, bus.ancre(t, z[0], f"{n}."), "MOYEN", f"point {n} : {lab} absent",
                                  f"traiter au point {n} : {lab} (contenu sourcé, jamais inventé)", "agent", rx[:120]))
    return D, dict(mots=mots, notions_absentes=absentes)


def m_X(n):
    def tronque(t, r):
        z = zone(t, n); h = titre(t, n); return t[:h[1]] + "<p>Ce point reste bref.</p>" + t[z[1]:]
    L = [("point tronqué", tronque, "BX1")]
    for lab, rx in P[n].get("notions", []):
        L.append((f"notion retirée : {lab}", (lambda rx: lambda t, r: sur_point(t, n, lambda s: texte_sub(s, rx, " ")))(rx), "BX2"))
    return L


# ── β·C cohérence chiffrée et unités ──
UNITE = r"(?:%|mg|µg|mcg|g|kg|mmol|µmol|mL|ml|L|°C|ans|cm|mm|UI|ng|pg|mmHg|kPa|mEq|h|min)"
RX_BC = [("BC1", re.compile(r"(\d)·(\d)"), r"\1,\2", "point médian entre deux chiffres (« 13·4 ») : la virgule décimale est la règle française", True),
         ("BC2", re.compile(r"(?<![\w.])(\d+)\.(\d+)(\s?)(%s)(?![\w/])" % UNITE), r"\1,\2\3\4", "décimale à point devant une unité : virgule décimale exigée", True),
         ("BC5", re.compile(r"&gt;\s?=|>\s?=(?!>)"), "≥", "comparateur ASCII « >= » : écrire ≥", True),
         ("BC5", re.compile(r"&lt;\s?=|<\s?=(?!<)"), "≤", "comparateur ASCII « <= » : écrire ≤", True),
         ("BC6", re.compile(r"(\d)(%|‰)(?![\w])"), r"\1 \2", "pourcentage collé au nombre : espace avant % (typographie française)", True)]
NON_SI = re.compile(r"(?i)\b\d+(?:[,.]\d+)?\s?(mg/dl|°F|lbs?|livres?|pouces?|inch(?:es)?|feet|pieds)\b")
NOMBRE = re.compile(r"(?<![\w,.])(\d+(?:[,.]\d+)?)(?:\s?(%|‰|°C|ans|mmol|mg|µg|kg|g|L|mL|UI|cm|mm|h|min|j))?")


def _texte_brut(seg):
    """Texte des nœuds, balises retirées sans décoder les entités (pour BC5)."""
    return re.sub(r"<[^>]+>", " ", bus.masque(seg, bus.RX_STYLE))


def nombres(txt):
    return {m.group(1).replace(".", ",") for m in NOMBRE.finditer(txt) if not re.fullmatch(r"(?:19|20)\d\d", m.group(1)) and m.group(1) not in {"0", "1"}}


def b_C(me, n, t, nom, opt):
    D = []; z = zone(t, n); M = {}
    if not z: return D, M
    h = titre(t, n); seg = t[h[1]:z[1]]; brut = _texte_brut(seg); k = 0
    noeuds = [x for x in re.split(r"<[^>]*>", bus.masque(seg, bus.RX_STYLE)) if x.strip()]
    for code, rx, rep, msg, scr in RX_BC:
        for m in [m for x in noeuds for m in rx.finditer(x)][:4]:
            k += 1
            D.append(bus.doleance(me, code, nom, bus.ancre(t, h[1], m.string[max(0, m.start() - 30):m.end() + 20]), "MOYEN", f"{msg} (point {n})",
                                  f"corriger la typographie du nombre : b{n:02d}_C --appliquer (valeur inchangée)", "script", m.group(0)))
    for m in list(NON_SI.finditer(brut))[:4]:
        D.append(bus.doleance(me, "BC4", nom, bus.ancre(t, h[1], m.group(0)), "MOYEN", f"unité non SI « {m.group(1)} » au point {n}",
                              "convertir en unité SI suisse (mmol/L, °C, kg, cm) avec la valeur recalculée par un outil ; garder la source", "agent", m.group(0)))
    if P[n].get("points_cles"):
        S = bus.sections(t); corps = set()
        for p in range(1, 13):
            if p in S: corps |= nombres(bus.texte(bus.masque(t[S[p][0]:S[p][1]], bus.RX_STYLE)))
        ici = nombres(bus.texte(bus.masque(t[h[1]:z[1]], bus.RX_STYLE))); hors = sorted(ici - corps)
        M["chiffres_hors_corps"] = hors
        for x in hors[:5]:
            D.append(bus.doleance(me, "BC3", nom, bus.ancre(t, h[1], x), "GRAVE", f"le chiffre {x} du point {n} n'apparaît dans aucun des points 1 à 12",
                                  f"aligner {x} sur la valeur sourcée du corps du cours, ou le retirer du point {n} (un point clé ne crée aucun chiffre)", "agent", x))
    M["typo_chiffres"] = k
    return D, M


def c_C(n, t, opt):
    def f(seg):
        for code, rx, rep, msg, scr in RX_BC: seg = texte_sub(seg, rx, rep)
        return seg
    return sur_point(t, n, f)


def m_C(n):
    L = [("point médian décimal", lambda t, r: inserer(t, n, f"Le score atteint {r.randint(10, 99)}·{r.randint(1, 9)} points.", r), "BC1"),
         ("décimale à point", lambda t, r: inserer(t, n, f"La dose atteint {r.randint(2, 9)}.{r.randint(1, 9)} mg par kilo.", r), "BC2"),
         ("unité non SI", lambda t, r: inserer(t, n, f"La glycémie dépasse {r.randint(126, 199)} mg/dl.", r), "BC4"),
         ("comparateur ASCII", lambda t, r: inserer(t, n, f"Le seuil reste &gt;= {r.randint(3, 9)} points.", r), "BC5"),
         ("pourcentage collé", lambda t, r: inserer(t, n, f"Elle touche {r.randint(11, 89)}% des cas.", r), "BC6")]
    if P[n].get("points_cles"):
        L.append(("chiffre hors du corps", lambda t, r: inserer(t, n, f"Le risque atteint {r.randint(400, 899)} pour mille.", r), "BC3"))
    return L


# ── β·S sources du point ──
FIG = re.compile(r"\d+(?:[,.]\d+)?\s?(?:%|‰)|pour 1[  ]?000\b|pour 100[  ]?000|/\s?100[  ]?000|\bn\s?=\s?\d|\b(?:OR|RR|HR|IC)\s?(?:95\s?%)?\s?[=:]?\s?\d")
MARQ = re.compile(r'<sup class="r">|\[S\d+\]|href="#sb-\d+"|\((?:[^()]*\b(?:OFS|OFSP|Obsan|OMS|WHO|ESC|ERC|EAACI|KDIGO|SSMIG)\b[^()]*|[^()]*\b(?:19|20)\d\d\b[^()]*)\)')
DOSE_V = re.compile(r"(?<![\w,.])\d+(?:[,.]\d+)?\s?(?:mg|µg|mcg|g|UI|mmol|mL)(?:\s?/\s?(?:kg|j|jour|h|m²|dose))*(?![\w])(?!\s?/\s?(?:L|l|dL|dl|mL)\b)")


def b_S(me, n, t, nom, opt):
    D = []; z = zone(t, n); M = {}
    if not z: return D, M
    ids = set(re.findall(r'\sid="([^"]+)"', t)); a, f = bus.bornes_cours(t); liste = t[f:]
    k1 = k3 = 0
    for pa, pf, inner in blocs(t, n, ("p", "li")):
        vis = bus.texte_visible(inner)
        if FIG.search(vis) and not MARQ.search(inner):
            k1 += 1
            D.append(bus.doleance(me, "BS1", nom, bus.ancre(t, pa, vis), "GRAVE" if n in (2, 8, 9, 11) else "MOYEN", f"bloc chiffré sans source au point {n}",
                                  "ajouter le renvoi [Sn] de la source lue qui porte ce chiffre ; sinon retirer le chiffre (jamais inventé)", "agent", vis[:200]))
        if P[n].get("doses") and DOSE_V.search(vis) and not MARQ.search(inner):
            k3 += 1
            D.append(bus.doleance(me, "BS3", nom, bus.ancre(t, pa, vis), "GRAVE", f"dose sans source au point {n}",
                                  "ancrer la dose sur l'AIPS suisse lue (renvoi [Sn] vers swissmedicinfo.ch) ; sinon la retirer", "agent", DOSE_V.search(vis).group(0)))
    seg = t[z[0]:z[1]]
    for m in re.finditer(r'href="#(sb-\d+)"', seg):
        if m.group(1) not in ids:
            D.append(bus.doleance(me, "BS2", nom, bus.ancre(t, z[0] + m.start(), m.group(1)), "GRAVE", f"renvoi {m.group(1)} sans source correspondante (point {n})",
                                  "relier le renvoi à une source de la liste, ou le retirer", "agent", m.group(0)))
    for m in re.finditer(r"\[S(\d+)\]", seg):
        if not re.search(r"\[S%s\]" % m.group(1), liste) and f"src-{m.group(1)}" not in ids and f"sb-{m.group(1)}" not in ids:
            D.append(bus.doleance(me, "BS2", nom, bus.ancre(t, z[0] + m.start(), m.group(0)), "GRAVE", f"renvoi {m.group(0)} absent de la liste des sources (point {n})",
                                  "ajouter la source lue à la liste, ou retirer le renvoi", "agent", m.group(0)))
    return D, dict(blocs_sans_source=k1, doses_sans_source=k3)


def m_S_(n):
    L = [("bloc chiffré sans source", lambda t, r: inserer(t, n, f"Elle concerne {r.randint(11, 89)} % des malades.", r, True), "BS1"),
         ("renvoi orphelin", lambda t, r: inserer(t, n, f'La règle s\'applique à tous.<sup class="r"><a href="#sb-{r.randint(90, 99)}">9</a></sup>', r), "BS2")]
    if P[n].get("doses"):
        L.append(("dose sans source", lambda t, r: inserer(t, n, f"Le traitement débute à {r.randint(2, 9)} mg/kg par jour.", r, True), "BS3"))
    return L


# ── β·M contre-épreuve par mutation (sentinelle sur le fichier réel) ──
def b_M(me, n, t, nom, opt):
    D = []; M = dict(testees=0, aveugles=[], non_applicables=0)
    if not zone(t, n): return D, M
    av = (opt or {}).get("aveugler")
    for f in FAM_A:
        mu = FAM["A"][f]["mutants"](n)
        if not mu: continue
        lab, fn, code = mu[0]; r = random.Random(f"{nom}|{n}|{f}")
        try:
            x = fn(t, r)
            if x == t: raise ValueError("mutant inapplicable")
        except Exception:
            M["non_applicables"] += 1; continue
        an = (lambda *a: ([], {})) if av == f else FAM["A"][f]["analyser"]
        i = ident("A", f, n); sig = lambda y: {(d["code"], d["constat"], d["preuve"]) for d in an(i, n, y, nom, {"sans_plafond": 1})[0] if d["code"][:2] == code[:2]}
        s0 = sig(t); s1 = sig(x); c0, c1 = len(s0), len(s1 - s0)
        M["testees"] += 1
        if not (s1 - s0):
            M["aveugles"].append(f)
            D.append(bus.doleance(me, "BM1", nom, bus.ancre(t, zone(t, n)[0], f"{n}."), "GRAVE", f"la synapse α{n}·{f} ne voit pas « {lab} » injecté dans ce fichier : elle est aveugle ici",
                                  f"relire à la main le point {n} pour « {SYN['familles_alpha'][f]['nom']} » ; escalade au nœud Opus du domaine ; signaler au gardien", "agent", f"{code} : {c0} signalées avant, aucune nouvelle après injection"))
    return D, M


def m_M(n):
    return [(f"α{n}·{f} aveuglée", (lambda f: lambda t, r: (t, {"aveugler": f}))(f), "BM1") for f in FAM_A if FAM["A"][f]["mutants"](n)]


# ── β·L langue adverse ──
VAGUE = re.compile(r"(?i)\b(?:souvent|parfois|en général|généralement|habituellement|peut-être|il semblerait|probablement|relativement|plutôt)\b")
ANGL = {"screening": "dépistage", "follow-up": "suivi", "cut-off": "seuil", "outcome": "devenir", "guidelines": "recommandations", "management": "prise en charge",
        "timing": "moment", "setting": "contexte", "feedback": "retour", "workup": "bilan", "triggers": "facteurs déclenchants", "check-up": "bilan de santé"}
RX_ANGL = re.compile(r"(?i)\b(%s)\b" % "|".join(map(re.escape, ANGL)))
RX_BL = [("BL3", re.compile(r'"([^"<>]{1,80})"'), "« \\1 »", "guillemets droits : guillemets français « »"),
         ("BL3", re.compile(r"(?<=\w) +([,.])(?=\s|$)"), r"\1", "espace avant une virgule ou un point"),
         ("BL4", re.compile(r"(?i)\b(le|la|les|de|des|du|un|une|et|à|en)\s+\1\b"), r"\1", "mot doublé")]


def b_L(me, n, t, nom, opt):
    D = []; z = zone(t, n); M = {}
    if not z: return D, M
    h = titre(t, n); v = 0
    for pa, ph in phrases(t, n):
        m = VAGUE.search(ph)
        if m and not re.search(r"\d", ph):
            v += 1
            if v <= 6:
                D.append(bus.doleance(me, "BL1", nom, bus.ancre(t, pa, ph), "DETAIL", f"nuance vague « {m.group(0)} » sans chiffre (point {n})",
                                      f"remplacer « {m.group(0)} » par la fréquence chiffrée et sourcée, ou retirer la nuance si elle ne change pas la conduite", "agent", ph[:200]))
    txt = texte_point(t, n)
    for m in list(RX_ANGL.finditer(txt))[:4]:
        D.append(bus.doleance(me, "BL2", nom, bus.ancre(t, h[1], m.group(0)), "MOYEN", f"anglicisme « {m.group(0)} » (point {n})",
                              f"écrire « {ANGL[m.group(0).lower()]} »", "agent", txt[max(0, m.start() - 30):m.end() + 30]))
    noeuds = [x for x in re.split(r"<[^>]*>", bus.masque(t[h[1]:z[1]], bus.RX_STYLE)) if x.strip()]
    for code, rx, rep, msg in RX_BL:
        for m in [m for x in noeuds for m in rx.finditer(x)][:3]:
            D.append(bus.doleance(me, code, nom, bus.ancre(t, h[1], m.string[max(0, m.start() - 20):m.end() + 20]), "DETAIL", f"{msg} (point {n})",
                                  f"corriger la typographie : b{n:02d}_L --appliquer (aucun mot changé)", "script", m.group(0)))
    return D, dict(vagues=v)


def c_L(n, t, opt):
    def f(seg):
        for code, rx, rep, msg in RX_BL: seg = texte_sub(seg, rx, rep)
        return seg
    return sur_point(t, n, f)


def m_L(n):
    return [("nuance vague", lambda t, r: inserer(t, n, r.choice(["La fièvre apparaît souvent le soir.", "Le pronostic reste généralement bon.", "Le patient se plaint parfois de nausées."]), r), "BL1"),
            ("anglicisme", lambda t, r: inserer(t, n, r.choice(["Le screening repose sur l'examen clinique.", "Le follow-up reste clinique.", "Le cut-off guide la décision."]), r), "BL2"),
            ("guillemets droits", lambda t, r: inserer(t, n, 'Le patient décrit une douleur "en étau" typique.', r), "BL3"),
            ("mot doublé", lambda t, r: inserer(t, n, "La fièvre monte de de façon brutale.", r), "BL4")]


# ═════════════════════════ registre des familles ═════════════════════════
ident_ = lambda t, n, o: t
FAM = {"A": {"S": dict(analyser=a_S, corriger=c_S, mutants=m_S, zones=lambda n: [f"P{n}:titre"]),
             "R": dict(analyser=a_R, corriger=c_R, mutants=m_R, zones=lambda n: [f"P{n}:absence"]),
             "H": dict(analyser=a_H, corriger=ident_, mutants=m_H, zones=lambda n: []),
             "Q": dict(analyser=a_Q, corriger=c_Q, mutants=m_Q, zones=lambda n: [f"P{n}:blocs"] if P[n].get("continuite", {}).get("bloc") else []),
             "D": dict(analyser=a_D, corriger=ident_, mutants=m_D, zones=lambda n: [])},
       "B": {"X": dict(analyser=b_X, corriger=ident_, mutants=m_X, zones=lambda n: []),
             "C": dict(analyser=b_C, corriger=c_C, mutants=m_C, zones=lambda n: [f"P{n}:typo-chiffres"]),
             "S": dict(analyser=b_S, corriger=ident_, mutants=m_S_, zones=lambda n: []),
             "M": dict(analyser=b_M, corriger=ident_, mutants=m_M, zones=lambda n: []),
             "L": dict(analyser=b_L, corriger=c_L, mutants=m_L, zones=lambda n: [f"P{n}:typo-texte"])}}


def analyseur(z, f, n):
    me = ident(z, f, n); fn = FAM[z][f]["analyser"]
    def analyser(t, nom, opt=None): return fn(me, n, t, nom, opt or {})
    return analyser


def correcteur(z, f, n):
    fn = FAM[z][f]["corriger"]
    def corriger(t, opt=None): return fn(n, t, opt or {})
    return corriger


def mutants(z, f, n): return FAM[z][f]["mutants"](n)
def zones(z, f, n): return FAM[z][f]["zones"](n)
def signal(z, f): return SYN["familles_alpha" if z == "A" else "familles_beta"][f]["signal"]
