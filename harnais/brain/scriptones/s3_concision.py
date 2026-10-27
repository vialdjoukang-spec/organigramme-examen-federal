#!/usr/bin/env python3
"""Scriptone S3 · concision extrême (doléance 3 de Vial) : phrases superflues ou redondantes ; phrases verbales denses reliées. Région AUL.
  C1 formule creuse (« Il est important de noter que », « En effet, »…) : vide de notion
  C2 redite : phrase dont les notions figurent déjà dans une phrase antérieure du cours (jetons de contenu, Jaccard ≥ 0,7)
  C3 métadiscours (« Ce chapitre », « comme vu plus haut », « ci-dessous ») : parle du cours, pas de la médecine
  C4 juxtaposition : ≥ 3 phrases courtes consécutives sans connecteur logique (à relier en phrases verbales denses)
Correction (--appliquer, executant = script) : C1 en tête de phrase seulement (la formule est retirée, la phrase reste entière).
C2, C3, C4 sont prescrits à l'agent ; la RÈGLE ABSOLUE du contracteur s'applique : aucune notion, aucune explication perdue."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s3_concision", "AUL", "1.0.0"
CREUX = [r"il est (?:important|essentiel|utile|intéressant|nécessaire) de (?:noter|souligner|rappeler|préciser|signaler) qu(?:e |')",
         r"il convient de (?:noter|souligner|rappeler|préciser) qu(?:e |')", r"il faut savoir qu(?:e |')", r"il est à noter qu(?:e |')",
         r"(?:notons|rappelons|soulignons|précisons) qu(?:e |')", r"en effet, ", r"de manière générale, ", r"d'une manière générale, ",
         r"dans ce contexte, ", r"à cet égard, ", r"force est de constater qu(?:e |')", r"il va sans dire qu(?:e |')", r"bien entendu, ",
         r"en fait, ", r"globalement, ", r"par ailleurs, ", r"en outre, ", r"de plus, ", r"il apparaît qu(?:e |')", r"on peut dire qu(?:e |')"]
RX_CREUX = re.compile(r"(?i)^(?:%s)" % "|".join(CREUX))
META = re.compile(r"(?i)\b(?:ce (?:chapitre|cours|point|paragraphe|fichier|document)|cette (?:section|partie|monographie)|nous (?:allons|verrons|avons vu)|"
                  r"comme (?:vu|indiqué|mentionné|décrit) (?:plus haut|ci-dessus|précédemment|plus loin)|ci-dessous|ci-dessus|voir plus (?:haut|bas)|"
                  r"dans la suite|le lecteur)\b")
CONNECT = re.compile(r"(?i)\b(?:car|donc|ainsi|alors|puis|mais|or|cependant|toutefois|parce qu|puisqu|lorsqu|lorsque|quand|si|sauf|d'où|ce qui|"
                     r"en revanche|par conséquent|de sorte|tandis qu|alors qu|bien qu|afin d|pour qu|grâce|à cause|en raison|dès qu|après|avant)\b|[:;→]")


def _phrases_cours(t):
    """[(pos du bloc, n° du point, phrase)] : texte visible du cours (fenêtres exclues), points 1 à 14."""
    out = []
    for n, (a, f) in sorted(bus.sections(t).items()):
        for pa, pf, inner in bus.blocs(t, a, f):
            if re.search(r"(?i)<(?:p|li)\b", inner): continue          # bloc englobant : ses enfants sont lus
            inner = re.sub(r"(?is)^\s*<(b|strong)>[^<]{0,80}[.:]\s*</\1>\s*", "", inner)   # étiquette de tête (« Amorce. ») : un titre, pas une phrase
            for ph in bus.phrases(bus.texte_visible(inner)):
                ph = re.sub(r"^[•▪◦–-]\s*", "", ph)
                if len(ph.split()) <= 6 and re.search(r"[):]\s*$|\)\.$", ph): continue          # étiquette (« Développement (niveau cellulaire). »)
                out.append((pa, n, ph))
    return out


def analyser(t, nom, opt=None):
    me = sys.modules[__name__]; D = []; P = _phrases_cours(t)
    vus = []; c1 = c2 = c3 = c4 = 0
    for pa, n, ph in P:
        if RX_CREUX.match(ph):
            c1 += 1; f = RX_CREUX.match(ph).group(0)
            D.append(bus.doleance(me, "C1", nom, bus.ancre(t, pa, ph), "MOYEN", f"formule creuse « {f.strip()} » (point {n})",
                                  f"retirer « {f.strip()} » en tête de phrase ; garder tout le reste : s3_concision.py --appliquer", "script", ph[:160]))
        if META.search(ph):
            c3 += 1
            D.append(bus.doleance(me, "C3", nom, bus.ancre(t, pa, ph), "MOYEN", f"métadiscours « {META.search(ph).group(0)} » (point {n}) : parle du cours, pas du malade",
                                  "réécrire la phrase sans référence au document (garder la notion médicale, sinon supprimer la phrase vide)", "agent", ph[:160]))
        j = bus.jetons(ph)
        if len(j) >= 6:
            for pa0, n0, ph0, j0 in vus:
                s = len(j & j0) / len(j | j0)
                if s >= 0.7:
                    c2 += 1
                    D.append(bus.doleance(me, "C2", nom, bus.ancre(t, pa, ph), "MOYEN", f"redite ({int(s * 100)} % des notions déjà dites au point {n0}) au point {n}",
                                          f"supprimer cette phrase ou n'en garder que la notion nouvelle ({', '.join(sorted(j - j0)) or 'aucune'}) ; la phrase du point {n0} « {ph0[:60]}… » porte déjà le reste",
                                          "agent", f"Jaccard {s:.2f}"))
                    break
            vus.append((pa, n, ph, j))
    # C4 : séries de phrases courtes juxtaposées dans un même bloc
    blocs = {}
    for pa, n, ph in P: blocs.setdefault((pa, n), []).append(ph)
    for (pa, n), L in blocs.items():
        serie = []
        for ph in L + [None]:
            if ph and len(ph.split()) <= 12 and not CONNECT.search(ph): serie.append(ph); continue
            if len(serie) >= 3:
                c4 += 1
                D.append(bus.doleance(me, "C4", nom, bus.ancre(t, pa, serie[0]), "MOYEN", f"{len(serie)} phrases courtes juxtaposées sans connecteur (point {n})",
                                      "relier en 1 ou 2 phrases verbales denses par des connecteurs logiques (car, donc, ainsi, alors que, si) ; chaque chiffre et chaque notion restent",
                                      "agent", " | ".join(s[:50] for s in serie)))
            serie = []
    mots = [len(p.split()) for _, _, p in P]
    M = dict(phrases=len(P), mots_moyens=round(sum(mots) / max(1, len(mots)), 1), connecteurs_pct=round(100 * sum(bool(CONNECT.search(p)) for _, _, p in P) / max(1, len(P))),
             creuses=c1, redites=c2, metadiscours=c3, juxtapositions=c4)
    return D, M


def corriger(t, opt=None):
    """Retire les formules creuses en tête de phrase dans le texte des <p>/<li> du cours (jamais dans une balise ni une fenêtre)."""
    a, f = bus.bornes_cours(t); seg = t[a:f]
    def p_sub(m):
        corps = m.group(2)
        def debut(mm):
            x = mm.group(2); c = RX_CREUX.match(x)
            if not c: return mm.group(0)
            reste = x[c.end():]
            return mm.group(1) + (reste[:1].upper() + reste[1:] if reste else reste)
        corps = re.sub(r"((?:^|(?<=[.!?])\s+))([^<.!?]+)", debut, corps)
        return m.group(1) + corps + m.group(3)
    seg = re.sub(r"(?is)(<(?:p|li)\b[^>]*>)((?:(?!</?(?:p|li)\b).)*?)(</(?:p|li)>)", p_sub, seg)
    return t[:a] + seg + t[f:]


def _phr(t):
    return [x for x in _phrases_cours(t) if len(x[2].split()) >= 8]
def _m_creux(t, r):
    a, f = bus.bornes_cours(t); B = [b for b in bus.blocs(t, a, f, ("p",)) if re.match(r"[A-ZÉ]", b[2])]
    pa, pf, inner = r.choice(B); i = t.index(inner, pa); x = t[i]
    f0 = r.choice(["Il est important de noter que ", "En effet, ", "Il faut savoir que ", "Par ailleurs, ", "Notons que "])
    return t[:i] + f0 + x.lower() + t[i + 1:]
def _m_redite(t, r):
    pa, n, ph = r.choice(_phr(t)); S = bus.sections(t); k = r.choice([x for x in S if x > n] or [n]); p = bus.blocs(t, *S[k], ("p",))
    if not p: return t
    q = p[-1][1] - 4; return t[:q] + " " + ph + t[q:]
def _m_meta(t, r):
    a, f = bus.bornes_cours(t); pa, pf, inner = r.choice(bus.blocs(t, a, f, ("p",))); q = pf - 4
    return t[:q] + " " + r.choice(["Ce chapitre résume ces notions.", "Comme vu plus haut, la cause compte.", "Le tableau ci-dessous les détaille."]) + t[q:]
def _m_juxta(t, r):
    a, f = bus.bornes_cours(t); pa, pf, inner = r.choice(bus.blocs(t, a, f, ("p",))); q = pf - 4
    return t[:q] + " La fièvre monte. Le pouls accélère. La tension baisse." + t[q:]
MUTANTS = [("formule creuse", _m_creux, "C1"), ("redite", _m_redite, "C2"), ("métadiscours", _m_meta, "C3"), ("juxtaposition", _m_juxta, "C4")]

ECRIT = ["TEXTE:tête de phrase"]

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
