#!/usr/bin/env python3
"""Scriptone S5 · arbre de classification déroulant et cliquable (doléances 5 et 6 de Vial). Région AUF.
Depuis la cascade qui mène à la notion (ex. Prurit → Prurit systémique → Prurit urémique), CHAQUE parent est cliquable et déroule
ses enfants, c'est-à-dire les homologues du niveau suivant (autres types de prurit), chacun explicité en une ligne ; la notion étudiée
reste visible parmi ses homologues (surlignée) et en bout de cascade. Applicable à toute notion.
  A1 arbre absent du point 1                 A2 arbre statique (parents non cliquables) → rendu par script
  A3 parent sans homologues (seul l'enfant de la cascade est donné)    A4 homologue sans explication
  A5 notion étudiée non marquée              A6 homologues regroupés dans une seule étiquette (« hépatique, rénal, endocrinien »)
Entrées lues : <details class="arbre"> brut (ul/li, <b> = notion) ou <div class="arb"> converti (forme_interactive.py).
Correction (--appliquer) : rendu natif <details>/<summary> (clavier, sans JavaScript), modèle JSON conservé dans data-modele ;
les homologues manquants restent prescrits à l'agent (A3, A4, A6) : le script ne crée jamais de contenu médical."""
import html as H, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s5_arbre", "AUF", "1.0.0"
CSS = ('<style id="brain-arbre">div.arb[data-brain]{margin:12px 0}div.arb[data-brain] .arbt{display:block;font-weight:700;color:#4c1d95;margin-bottom:6px}'
       'details.arbn{border:1px solid #c4b5fd;background:#f5f3ff;border-radius:10px;padding:6px 12px;margin:0 0 6px}details.arbn>summary{cursor:pointer;list-style:none}'
       'details.arbn>summary::-webkit-details-marker{display:none}details.arbn>summary::before{content:"▸ ";color:#7c3aed}details.arbn[open]>summary::before{content:"▾ "}'
       'details.arbn>summary:focus-visible{outline:2px solid #7c3aed;border-radius:6px}details.arbn b{color:#3b0764}details.arbn .org{float:right;font-size:.8em;background:#fff;'
       'color:#4c1d95;border:1px solid #c4b5fd;border-radius:6px;padding:0 6px;margin-left:8px}details.arbn .dfn,ul.hom .dfn{display:block;font-size:.88em;color:#475569}'
       'ul.hom{margin:6px 0 2px;padding-left:1.1em;border-left:2px dashed #a78bfa}ul.hom li{margin:3px 0}ul.hom li.voie>b::after{content:" ↓ suite de la cascade";font-weight:400;'
       'font-size:.8em;color:#7c3aed}ul.hom li.cible{background:#6d28d9;color:#fff;border-radius:6px;padding:2px 8px}ul.hom li.cible b,ul.hom li.cible .dfn{color:#fff}'
       'ul.hom li.cible>b::after{content:" ← notion étudiée";font-weight:400;font-size:.8em}details.arbn.cible{background:#6d28d9;border-color:#4c1d95}'
       'details.arbn.cible b,details.arbn.cible .dfn,details.arbn.cible>summary::before{color:#fff}details.arbn.cible ul.hom li,details.arbn.cible ul.hom .dfn{color:#f5f3ff}'
       '@media(prefers-color-scheme:dark){details.arbn{background:#241d3f}details.arbn b{color:#e9d5ff}details.arbn .dfn,ul.hom .dfn{color:#cbd5e1}}</style>')
TITRE = "Où se situe le problème ? Du général au particulier"


def _nd(nom, org="", dfn="", cible=False):
    return dict(nom=nom.strip(), org=org.strip(), dfn=dfn.strip(), cible=cible, enfants=[])


def _nom_org(x):
    m = re.match(r"^(.*?)\s*\(([^()]{2,80})\)\s*$", x)
    return (m.group(1), m.group(2)) if m and re.search(r"CIM|DSM|ATC|OMS|IFSI|ICD|classification|groupe|chapitre|\d{4}", m.group(2), re.I) else (x, "")


def _chip(x):
    """« Nom : explication » ou « Nom (explication) » → (nom, explication)."""
    m = re.match(r"^([^:]{2,80}?)\s*:\s*(.{3,})$", x)
    if m: return m.group(1), m.group(2)
    m = re.match(r"^(.*?)\s*\(([^()]{6,})\)\s*$", x)
    return (m.group(1), m.group(2)) if m and len(m.group(2).split()) >= 3 else (x, "")


def lire_brut(seg):
    """<details class="arbre"> : ul/li imbriqués, <b> = notion étudiée → racine (liste de nœuds)."""
    racine = []; pile = [racine]; cur = []
    for tok in re.finditer(r"(?is)<ul[^>]*>|</ul>|<li[^>]*>|</li>|<summary.*?</summary>|<[^>]+>|[^<]+", seg):
        x = tok.group(0); xl = x.lower()
        if xl.startswith("<li"):
            n = _nd(""); n["_h"] = ""; pile[-1].append(n); cur.append(n); pile.append(n["enfants"])
        elif xl.startswith("</li"):
            if cur: cur.pop(); pile.pop()
        elif xl.startswith("<ul") or xl.startswith("</ul") or xl.startswith("<summary"): continue
        elif cur and cur[-1] is not None and len(pile) - 1 == len(cur): cur[-1]["_h"] += x
    def fin(L):
        for n in L:
            h = n.pop("_h", ""); m = re.search(r'(?s)class="tm"[^>]*>(.*?)<span class="df">(.*?)</span></span>', h)
            nom, dfn = (bus.texte(m.group(1)), bus.texte(m.group(2))) if m else (bus.texte(h), "")
            n["cible"] = "<b>" in h.lower() or "<strong>" in h.lower(); n["nom"], n["org"] = _nom_org(nom); n["dfn"] = dfn; fin(n["enfants"])
    fin(racine)
    return racine


def lire_converti(seg):
    """<div class="arb"> de forme_interactive : cascade .niv, puces « Comprend » (enfants) et « Voisins » (homologues de la notion)."""
    niv = []
    for m in re.finditer(r'(?is)<div class="niv( cible)?"[^>]*>(.*?)</div>', seg):
        h = m.group(2); b = re.search(r"(?is)<b>(.*?)</b>", h); o = re.search(r'(?is)<span class="org">(.*?)</span>(?=<span class="dfn"|$)', h)
        d = re.search(r'(?is)<span class="dfn">(.*?)</span>', h)
        niv.append(_nd(bus.texte(b.group(1)) if b else bus.texte(h), bus.texte(o.group(1)) if o else "", bus.texte(d.group(1)) if d else "", bool(m.group(1))))
    puces = lambda cl: [_chip(bus.texte(x)) for m in re.finditer(r'(?is)<div class="liste%s"[^>]*>(.*?)</div>' % cl, seg) for x in re.findall(r'(?is)<span class="chip">(.*?)</span>', m.group(1))]
    if not niv: return []
    for a, b in zip(niv, niv[1:]): a["enfants"].append(b)
    ci = next((n for n in niv if n["cible"]), niv[-1])
    ci["enfants"] += [_nd(n, dfn=d) for n, d in puces("")]
    if len(niv) >= 2:
        par = niv[niv.index(ci) - 1] if niv.index(ci) else None
        if par is not None: par["enfants"] += [_nd(n, dfn=d) for n, d in puces(" voisin")]
    return [niv[0]]


def chemin(L, anc=()):
    for n in L:
        if n["cible"]: return list(anc) + [n]
        r = chemin(n["enfants"], list(anc) + [n])
        if r: return r
    return None


def fin_div(t, a):
    """Position après le </div> qui ferme le <div> ouvert en a (profondeur comptée)."""
    k = 0
    for m in re.finditer(r"(?i)<div\b|</div>", t[a:]):
        k += 1 if m.group(0).lower().startswith("<div") else -1
        if k == 0: return a + m.end()
    return len(t)


def trouver(t):
    """(début, fin, type, modèle) du premier arbre du point 1 (sinon du cours)."""
    S = bus.sections(t); a, f = S.get(1, bus.bornes_cours(t))
    m = re.search(r'(?is)<div class="arb" data-brain="arbre" data-modele="([^"]*)">', t[a:f])
    if m:
        try: mod = json.loads(H.unescape(m.group(1)))
        except ValueError: mod = []          # modèle abîmé (fichier tronqué, édition à la main) : arbre signalé, jamais une panne
        return a + m.start(), fin_div(t, a + m.start()), "brain", mod if isinstance(mod, list) else []
    m = re.search(r'(?is)<details class="arbre"[^>]*>.*?</details>', t[a:f])
    if m: return a + m.start(), a + m.end(), "brut", lire_brut(m.group(0))
    m = re.search(r'(?is)<div class="arb">', t[a:f])
    if m:
        e = fin_div(t, a + m.start()); return a + m.start(), e, "converti", lire_converti(t[a + m.start():e])
    return None


def analyser(t, nom, opt=None):
    me = sys.modules[__name__]; D = []; M = {}
    r = trouver(t)
    S = bus.sections(t); p1 = S.get(1, (0, 0))[0]
    if not r:
        D.append(bus.doleance(me, "A1", nom, bus.ancre(t, t.find(">", p1) + 1, "1. Définition"), "GRAVE", "aucun arbre de classification au point 1",
                              "écrire <details class=\"arbre\"> : ul/li du général au particulier, classification d'origine entre parenthèses, notion en <b>, homologues explicités à chaque niveau", "agent"))
        return D, dict(arbre=None)
    a, f, typ, mod = r; ch = chemin(mod) or []
    M.update(arbre=typ, profondeur=len(ch))
    anc = lambda x: bus.ancre(t, a, x)
    rendu_ok = typ == "brain" and len(re.findall(r'<details class="arbn', t[a:f])) == len(ch)
    if not rendu_ok:
        D.append(bus.doleance(me, "A2", nom, anc(TITRE), "GRAVE", f"arbre {typ} : les parents ne sont pas cliquables et ne déroulent pas leurs homologues",
                              "rendre l'arbre déroulant : s5_arbre.py --appliquer (details/summary natifs, notion surlignée parmi ses homologues)", "script", f"{len(ch)} niveaux"))
    if not ch or not ch[-1]["cible"]:
        D.append(bus.doleance(me, "A5", nom, anc(TITRE), "GRAVE", "la notion étudiée n'est pas marquée dans l'arbre", "mettre la notion étudiée en <b> dans son <li>", "agent"))
        return D, M
    sans_h = sans_e = groupes = 0
    for i, p in enumerate(ch[:-1]):
        suite = ch[i + 1]; hom = [e for e in p["enfants"] if e is not suite]
        if not hom:
            sans_h += 1
            D.append(bus.doleance(me, "A3", nom, anc(p["nom"]), "GRAVE", f"« {p['nom']} » ne déroule aucun homologue de « {suite['nom']} »",
                                  f"sous « {p['nom']} », ajouter les autres catégories de même niveau que « {suite['nom']} » (classification d'origine), chacune en "
                                  f"<li><span class=\"tm\" tabindex=\"0\">Nom<span class=\"df\">explication en une phrase</span></span></li>", "agent", f"niveau {i + 1} sur {len(ch)}"))
        for e in hom:
            if not e["dfn"]:
                sans_e += 1
                D.append(bus.doleance(me, "A4", nom, anc(e["nom"]), "MOYEN", f"homologue « {e['nom'][:60]} » sans explication",
                                      f"expliciter « {e['nom'][:60]} » en une phrase (ce qui le distingue de « {suite['nom'][:50]} »)", "agent"))
            if not e["dfn"] and len([x for x in re.split(r",| et ", e["nom"]) if x.strip()]) >= 3:
                groupes += 1
                D.append(bus.doleance(me, "A6", nom, anc(e["nom"]), "MOYEN", f"homologues regroupés dans une seule étiquette : « {e['nom'][:80]} »",
                                      "un homologue par élément, chacun avec sa phrase d'explication", "agent"))
    cible = ch[-1]
    for e in cible["enfants"]:
        if not e["dfn"] and len([x for x in re.split(r",| et ", e["nom"]) if x.strip()]) >= 3:
            groupes += 1
            D.append(bus.doleance(me, "A6", nom, anc(e["nom"]), "MOYEN", f"sous-types regroupés dans une seule étiquette : « {e['nom'][:80]} »",
                                  "un sous-type par élément, chacun avec sa phrase d'explication", "agent"))
    M.update(parents_sans_homologues=sans_h, homologues_sans_explication=sans_e, etiquettes_groupees=groupes)
    return D, M


def _li(e, cl=""):
    c = f' class="{cl}"' if cl else ""
    return f'<li{c}><b>{H.escape(e["nom"])}</b>' + (f'<span class="dfn">{H.escape(e["dfn"])}</span>' if e["dfn"] else "") + "</li>"


def rendre(mod):
    ch = chemin(mod) or []
    if not ch: return None
    out = [f'<div class="arb" data-brain="arbre" data-modele="{H.escape(json.dumps(mod, ensure_ascii=False), quote=True)}"><span class="arbt">{TITRE}</span>']
    for i, n in enumerate(ch):
        cl = "arbn cible" if n["cible"] else "arbn"
        org = f'<span class="org">{H.escape(n["org"])}</span>' if n["org"] else ""
        dfn = f'<span class="dfn">{H.escape(n["dfn"])}</span>' if n["dfn"] else ""
        if n["cible"] and not n["enfants"]:
            out.append(f'<details class="{cl}" style="margin-left:{i * 20}px" open aria-current="true"><summary><b>{H.escape(n["nom"])}</b>{org}{dfn}</summary></details>'); continue
        suite = ch[i + 1] if i + 1 < len(ch) else None
        lis = "".join(_li(e, "cible" if (e is suite and suite["cible"]) else "voie" if e is suite else "") for e in n["enfants"])
        out.append(f'<details class="{cl}" style="margin-left:{i * 20}px"{" aria-current=\"true\"" if n["cible"] else ""}><summary><b>{H.escape(n["nom"])}</b>{org}{dfn}</summary><ul class="hom">{lis}</ul></details>')
    return "".join(out) + "</div>"


def corriger(t, opt=None):
    r = trouver(t)
    if not r: return t
    a, f, typ, mod = r
    if typ != "brain":
        h = rendre(mod)
        if h: t = t[:a] + h + t[f:]
    return bus.pose_style(t, "brain-arbre", CSS)


# ── mutants : modèle altéré dans un arbre rendu (data-modele) ou HTML statique ──
def _alt(t, fn, r):
    a, f, typ, mod = trouver(t); ch = chemin(mod); fn(ch, r)
    return t[:a] + rendre(mod) + t[f:]
def _m_hom(t, r):
    def f(ch, r):
        p = r.choice(ch[:-1]); p["enfants"][:] = [ch[ch.index(p) + 1]]
    return _alt(t, f, r)
def _m_expl(t, r):
    def f(ch, r):
        p = r.choice(ch[:-1]); hom = [e for e in p["enfants"] if e is not ch[ch.index(p) + 1]]; r.choice(hom)["dfn"] = ""
    return _alt(t, f, r)
def _m_statique(t, r):
    a, f, typ, mod = trouver(t); ch = chemin(mod)
    niv = "".join(f'<div class="niv{" cible" if n["cible"] else ""}" style="margin-left:{i * 20}px"><b>{n["nom"]}</b></div>' for i, n in enumerate(ch))
    return t[:a] + f'<div class="arb"><div class="arbt">{TITRE}</div>{niv}</div>' + t[f:]
def _m_cible(t, r):
    a, f, typ, mod = trouver(t); chemin(mod)[-1]["cible"] = False
    m = re.compile(r'data-modele="[^"]*"').search(t, a)
    return t[:m.start()] + f'data-modele="{H.escape(json.dumps(mod, ensure_ascii=False), quote=True)}"' + t[m.end():]
MUTANTS = [("parent sans homologues", _m_hom, "A3"), ("homologue non explicité", _m_expl, "A4"), ("arbre statique", _m_statique, "A2"), ("notion non marquée", _m_cible, "A5")]

ECRIT = ["P1:arbre", "CSS:brain-arbre"]

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
