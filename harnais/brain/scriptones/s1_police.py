#!/usr/bin/env python3
"""Scriptone S1 · police Atkinson Hyperlegible partout (doléance 1 de Vial). Région AUF.
Lit le CSS réel (toutes les balises <style>, attributs style=, SVG font-family=) et signale :
  P1 police non embarquée (aucun @font-face Atkinson)      P2 police externe (url non data: → rien hors ligne)
  P3 graisse 400 ou 700 absente                              P4 règle concurrente non neutralisée (ex. #rm{font:… system-ui})
  P5 pile de repli absente (Verdana, system-ui, sans-serif)  P6 attribut style= ou font-family SVG concurrent
  P7 police embarquée CASSÉE : saut de ligne dans une url(data:…) non citée (coupe_lignes) → @font-face ignoré, Atkinson jamais chargée
Correction (--appliquer, executant = script) : @font-face embarqué (harnais/atkinson.b64.json, woff2 400 et 700, font-display:swap)
+ <style id="brain-police"> qui impose Atkinson à tout le texte (code et pre exceptés), repli Verdana → Segoe UI → system-ui → sans-serif."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s1_police", "AUF", "1.0.0"
FAM = '"Atkinson Hyperlegible",Verdana,"Segoe UI",system-ui,sans-serif'
REGLE = f'html,body,body *:not(code):not(pre):not(kbd):not(samp),body *::before,body *::after{{font-family:{FAM}!important}}'
BLOC = f'<style id="brain-police">{REGLE}</style>'
MONO = re.compile(r"mono|courier|consolas|menlo", re.I)


def _fonte():
    f = bus.R / "harnais/atkinson.b64.json"
    F = json.loads(f.read_text())
    q = lambda b: "\\\n".join(b[i:i + 2000] for i in range(0, len(b), 2000))   # continuation CSS : aucune ligne > 3 000, url valide
    return "".join(f'@font-face{{font-family:"Atkinson Hyperlegible";font-weight:{w};font-display:swap;src:url("data:font/woff2;base64,{q(F[w])}") format("woff2")}}' for w in ("400", "700"))


def cassee(ff):
    """Un @font-face embarqué est-il illisible par le navigateur ? (saut de ligne dans une url() non citée, chaîne non continuée, base64 faux)"""
    import base64
    m = re.search(r'(?is)url\(\s*(["\']?)data:font/woff2;base64,(.*?)\1\s*\)', ff)
    if not m: return False
    b = m.group(2)
    if m.group(1): b = b.replace("\\\n", "").replace("\\\r\n", "")
    if re.search(r"\s", b): return True
    try: return base64.b64decode(b[:16] + "=" * (-len(b[:16]) % 4))[:4] != b"wOF2"
    except Exception: return True


def _styles(t):
    return [(m.start(1), m.group(1), m.group(0)) for m in re.finditer(r"(?is)<style\b[^>]*>(.*?)</style>", t)]


def _familles(decl):
    m = re.search(r"(?i)font-family\s*:\s*([^;}!]+)", decl)
    if m: return m.group(1).strip()
    m = re.search(r"(?i)(?<![-\w])font\s*:\s*([^;}!]+)", decl)
    if m:   # raccourci font: [style] [graisse] taille[/interligne] familles
        mm = re.search(r"\d[\w.%]*(?:/[\w.%]+)?\s+(.+)$", m.group(1).strip())
        return mm.group(1).strip() if mm else ""
    return None


def analyser(t, nom, opt=None):
    D, M = [], {}
    st = _styles(t); css = "".join(s for _, s, _ in st)
    ff = re.findall(r"(?is)@font-face\s*\{([^}]*)\}", css)
    atk = [x for x in ff if "atkinson" in x.lower()]
    poids = {re.search(r"font-weight\s*:\s*(\d+)", x).group(1) for x in atk if re.search(r"font-weight\s*:\s*(\d+)", x)}
    externes = [x for x in atk if re.search(r"url\(\s*(?!['\"]?data:)", x)]
    garde = any(c.strip() == REGLE for _, c, b in st if 'id="brain-police"' in b)
    M.update(fontface_atkinson=len(atk), graisses=sorted(poids), garde_brain=garde)
    pos0 = t.find("<style") if "<style" in t else 0
    if not atk:
        D.append(bus.doleance(sys.modules[__name__], "P1", nom, bus.ancre(t, pos0, "<head>"), "CRITIQUE", "Atkinson Hyperlegible n'est pas embarquée (aucun @font-face) : le cours s'affiche dans une autre police",
                              "embarquer la police : s1_police.py --appliquer (woff2 400 et 700 en data:, font-display:swap)", "script", f"{len(ff)} @font-face, aucun Atkinson"))
    if externes:
        D.append(bus.doleance(sys.modules[__name__], "P2", nom, bus.ancre(t, pos0, "@font-face"), "GRAVE", "Atkinson chargée depuis une URL externe : rien hors ligne",
                              "remplacer par la police embarquée (data:) : s1_police.py --appliquer", "script", externes[0][:160]))
    casses = [x for x in atk if cassee(x)]; M["fontface_cassees"] = len(casses)
    if casses:
        D.append(bus.doleance(sys.modules[__name__], "P7", nom, bus.ancre(t, pos0, "@font-face"), "CRITIQUE",
                              f"{len(casses)} @font-face Atkinson illisibles (saut de ligne dans l'url data: non citée) : le navigateur les ignore, le cours s'affiche en Verdana",
                              "réembarquer la police en url citée à continuation CSS : s1_police.py --appliquer", "script", "url(data:… coupée par un saut de ligne"))
    if atk and not {"400", "700"} <= poids:
        D.append(bus.doleance(sys.modules[__name__], "P3", nom, bus.ancre(t, pos0, "@font-face"), "MOYEN", f"graisses embarquées {sorted(poids)} : 400 et 700 attendues (gras synthétique sinon)",
                              "embarquer les graisses 400 et 700 : s1_police.py --appliquer", "script", ",".join(sorted(poids))))
    # règles concurrentes
    regles = []
    for off, c, b in st:
        if 'id="brain-police"' in b: continue
        for m in re.finditer(r"([^{}@]+)\{([^{}]*)\}", c):
            if m.group(1).strip() == "font-face": continue
            fam = _familles(m.group(2))
            if fam is None: continue
            regles.append((off + m.start(), m.group(1).strip(), fam))
    concurrentes = 0; bonnes = [s for _, s, f in regles if f.lower().lstrip("'\"").startswith("atkinson")]
    couvert = {x.strip() for s in bonnes for x in s.split(",")}
    dern_atk = max([p for p, s, f in regles if f.lower().lstrip("'\"").startswith("atkinson")] or [-1])
    for pos, sel, fam in regles:
        f0 = fam.lower().lstrip("'\"")
        if f0.startswith("atkinson"):
            if not re.search(r"sans-serif|system-ui|verdana", fam, re.I):
                D.append(bus.doleance(sys.modules[__name__], "P5", nom, bus.ancre(t, pos, sel), "MOYEN", f"« {sel[:60]} » : Atkinson sans pile de repli",
                                      f"écrire font-family:{FAM}", "script", fam[:120]))
            continue
        if MONO.search(fam) and re.search(r"\b(code|pre|kbd|samp)\b", sel): continue
        sels = {x.strip() for x in sel.split(",")}
        neutralisee = garde or (sels <= couvert and pos < dern_atk)   # une règle Atkinson plus tardive couvre les mêmes sélecteurs
        if not neutralisee:
            concurrentes += 1
            D.append(bus.doleance(sys.modules[__name__], "P4", nom, bus.ancre(t, pos, sel), "GRAVE", f"règle « {sel[:60]} » impose {fam[:50]} : ce texte ne s'affiche pas en Atkinson",
                                  "neutraliser par la garde de police : s1_police.py --appliquer (aucune règle de fond à toucher)", "script", f"{sel[:80]}{{font-family:{fam[:80]}}}"))
    if not garde:
        for m in re.finditer(r'(?i)\sstyle="([^"]*font(?:-family)?\s*:[^"]*)"|\sfont-family="([^"]+)"', t):
            fam = _familles(m.group(1)) if m.group(1) else m.group(2)
            if fam and not fam.lower().lstrip("'\"").startswith("atkinson"):
                D.append(bus.doleance(sys.modules[__name__], "P6", nom, bus.ancre(t, m.start(), m.group(0)), "MOYEN", f"attribut impose {fam[:40]}",
                                      "neutraliser par la garde de police : s1_police.py --appliquer", "script", m.group(0)[:120]))
    M.update(regles_police=len(regles), concurrentes=concurrentes)
    return D, M


def corriger(t, opt=None):
    st = _styles(t); css = "".join(s for _, s, _ in st)
    atk = [x for x in re.findall(r"(?is)@font-face\s*\{([^}]*)\}", css) if "atkinson" in x.lower()]
    ok = atk and all(not re.search(r"url\(\s*(?!['\"]?data:)", x) and not cassee(x) for x in atk) and \
        {"400", "700"} <= {m.group(1) for x in atk for m in [re.search(r"font-weight\s*:\s*(\d+)", x)] if m}
    if not ok:
        t = re.sub(r'(?is)@font-face\s*\{[^}]*atkinson[^}]*\}', "", t)
        t = bus.pose_style(t, "brain-fonte", f'<style id="brain-fonte">{_fonte()}</style>')
    return bus.pose_style(t, "brain-police", BLOC)


# ── mutants (test par mutation) : chaque injection doit être détectée par le code attendu ──
POLICES = ["Georgia,serif", "Arial,sans-serif", "system-ui", "Times New Roman,serif", "Helvetica"]
def _m_fonte(t, r): return re.sub(r"(?is)@font-face\s*\{[^}]*\}", "", t).replace('<style id="brain-police">', '<style>')
def _m_regle(t, r):
    sel = r.choice(["#rm", "p", "td", ".tm .df", "#__tabs a", "h3", "li", "summary"])
    t = t.replace('<style id="brain-police">', "<style>")
    return t.replace("</head>", f"<style>{sel}{{font-family:{r.choice(POLICES)}}}</style></head>", 1)
def _m_externe(t, r): return re.sub(r"url\(\"?data:font/woff2;base64,[^)]+\)", "url(https://fonts.example.invalid/atk.woff2)", t, count=1)
def _m_casse(t, r):
    def f(m):
        x = m.group(0).replace("\\\n", "").replace('url("', "url(").replace('") format', ") format"); k = r.randint(200, 3000)
        i = x.index("base64,") + k; return x[:i] + "\n" + x[i:]
    return re.sub(r'(?is)@font-face\s*\{[^}]*font-weight:400[^}]*\}', f, t, count=1)
def _m_graisse(t, r): return re.sub(r'(?is)@font-face\s*\{[^}]*font-weight:700[^}]*\}', "", t)
MUTANTS = [("police non embarquée", _m_fonte, "P1"), ("règle concurrente", _m_regle, "P4"), ("police externe", _m_externe, "P2"), ("graisse 700 absente", _m_graisse, "P3"), ("police cassée par un saut de ligne", _m_casse, "P7")]

ECRIT = ["CSS:brain-fonte", "CSS:brain-police", "CSS:@font-face"]

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
