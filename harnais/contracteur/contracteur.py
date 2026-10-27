#!/usr/bin/env python3
"""CONTRACTEUR DE TEXTE · CONSERVATEUR DE NOTIONS (moteur, lecture seule). Un clone par auditeur : harnais/agents/KB1.py … KB5.py.
Dernier secteur de chaque fichier avant le commit. Il ne réécrit pas la médecine : il réduit le volume et PROUVE que rien d'utile n'a disparu.
  KBi.py contracter <fichier>   1re fois : photographie des notions (inventaire). Puis contraction mécanique sûre (formules creuses, doublons exacts),
                                puis liste des cibles de contraction sémantique (phrases longues, redites, points les plus lourds) pour l'auditeur Opus.
  KBi.py verifier <fichier> [--exceptions "mot,mot"]   compare à l'inventaire : notions conservées ET volume réduit ; pose le visa si OK
  KBi.py etat <fichier>         inventaire, volume, dernier verdict
Notions suivies : nombres, renvois [Sn], médicaments (®, DCI, fenêtres), termes cliquables, sigles, tableaux, 14 points, lemmes (noms, noms propres).
Seuils (CIBLE.json) : nombres 100 %, médicaments 100 %, tableaux identiques, 14 points ; termes ≥ 95 %, [Sn] ≥ 95 %, lemmes ≥ 95 % ; volume : réduction ≥ cible % OU mots ≤ plafond."""
import hashlib, json, re, sys, time
from pathlib import Path
R = Path(__file__).resolve().parent.parent.parent
H = Path(__file__).resolve().parent
sys.path.insert(0, str(R / "harnais")); sys.path.insert(0, str(R / "harnais/grille14"))

CIBLE = json.loads((H / "CIBLE.json").read_text())
import os as _os
if _os.environ.get("G14_TEST") and _os.environ.get("G14_CIBLE_PCT"): CIBLE["reduction_pct"] = float(_os.environ["G14_CIBLE_PCT"])

# ---- texte et notions ------------------------------------------------------------------------------------------
def corps(html):
    """Texte à contracter : tout sauf script/style, onglet Rappel mémoire, liste des sources."""
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html)
    t = re.sub(r"(?is)<div id=\"?rappel\"?.*?</div>\s*</div>", " ", t)
    t = re.sub(r"(?is)<h2>\s*Sources\s*</h2>.*", " ", t)
    return t

def texte(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", corps(html))).strip()

_NLP = None
def nlp():
    global _NLP
    if _NLP is None:
        import spacy
        _NLP = spacy.load("fr_core_news_sm", disable=["ner", "parser"])
        _NLP.max_length = 3_000_000
    return _NLP

def lemmes(t):
    d = nlp()(t[:2_500_000]); return {x.lemma_.lower() for x in d if x.pos_ in ("NOUN", "PROPN") and len(x.lemma_) > 2 and x.lemma_.isalpha()}

def inventaire(html):
    c = corps(html); t = texte(html); sans = re.sub(r"\[S\d+\]", " ", t)
    nombres = {m.replace(",", ".") for m in re.findall(r"(?<![\w.])\d+(?:[.,]\d+)?", sans)}
    renvois = set(re.findall(r"\[S(\d+)\]", c)) | set(re.findall(r'href="#sb-(\d+)"', c))
    meds = {x.lower() for x in re.findall(r"\b([A-Z][A-Za-zÀ-ÿ\-]{2,}(?: [A-Z][A-Za-zÀ-ÿ\-]{1,}){0,2})®", t)} | {re.sub(r"<[^>]+>", "", m).strip().lower() for m in re.findall(r'class="tm med"[^>]*>([^<]+)<', c)}
    termes = {re.sub(r"<[^>]+>", "", m).strip().lower() for m in re.findall(r'class="tm"[^>]*>([^<]+)<', c)} | {re.sub(r"<[^>]+>", "", m).strip().lower() for m in re.findall(r"<summary[^>]*>(.*?)</summary>", c, re.S)}
    termes = {re.sub(r"\s+([:;?!])", r"\1", x) for x in termes}; termes.discard("")
    sigles = set(re.findall(r"\b[A-Z][A-Z0-9]{1,6}\b", sans))
    tabl = [len(re.findall(r"<tr", x)) for x in re.findall(r"(?is)<table.*?</table>", c)]
    points = sorted({int(x) for x in re.findall(r"<h3[^>]*>\s*(?:<strong>)?\s*(\d{1,2})\.\s", c)})
    return dict(mots=len(t.split()), nombres=sorted(nombres), renvois=sorted(renvois, key=int), meds=sorted(meds), termes=sorted(termes), sigles=sorted(sigles),
                tableaux=tabl, points=points, lemmes=sorted(lemmes(t)))

def perdus(av, ap, cle):
    a, b = set(av[cle]), set(ap[cle]); return sorted(a - b), (len(a & b) / len(a) if a else 1.0)

# ---- contraction mécanique sûre -------------------------------------------------------------------------------
CREUX = [  # (motif, remplacement) ; appliqués au texte seulement, jamais dans les balises
    (r"\bIl (?:est|convient d'être) (?:important|essentiel|utile|nécessaire) de (?:noter|souligner|rappeler|signaler|préciser) que ", ""),
    (r"\bIl convient de (?:noter|souligner|rappeler|signaler|préciser) que ", ""),
    (r"\bIl faut (?:noter|souligner|rappeler|signaler|préciser|savoir) que ", ""),
    (r"\b(?:Notons|Rappelons|Soulignons|Précisons|Signalons) que ", ""),
    (r"\bEn effet, ", ""), (r"\bPar ailleurs, ", ""), (r"\bDe plus, ", ""), (r"\bDe surcroît, ", ""), (r"\bEn outre, ", ""), (r"\bÉgalement, ", ""),
    (r"\bAinsi, ", ""), (r"\bDe ce fait, ", ""), (r"\bEn pratique, ", ""), (r"\bEn règle générale, ", ""), (r"\bDe manière générale, ", ""),
    (r"\bà l'heure actuelle\b", "actuellement"), (r"\bde nos jours\b", "aujourd'hui"), (r"\ben raison du fait que\b", "car"), (r"\bétant donné que\b", "car"),
    (r"\bdans le cas où\b", "si"), (r"\bau cas où\b", "si"), (r"\bau niveau de\b", "dans"), (r"\bafin de\b", "pour"), (r"\bde manière à\b", "pour"),
    (r"\bun grand nombre de\b", "beaucoup de"), (r"\best en mesure de\b", "peut"), (r"\bsont en mesure de\b", "peuvent"), (r"\bà l'aide de\b", "avec"),
    (r"\bpar le biais de\b", "par"), (r"\bla survenue de\b", "l'apparition de"), (r"\bdans la mesure où\b", "car"), (r"\bil s'agit d'un\b", "c'est un"), (r"\bil s'agit d'une\b", "c'est une"),
    (r"\bcomme (?:nous l'avons vu|indiqué plus haut|cela a été dit)\b[, ]*", ""), (r"\bc'est-à-dire\b", "soit"), (r"\bpermet de\b", "permet de"),
]
CREUX = [x for x in CREUX if x[0] != r"\bpermet de\b"]
CREUX = [(re.compile((f"({p})(\\w)" if r == "" else p), re.I), r) for p, r in CREUX]

def contraction_mecanique(html):
    parties = re.split(r"(<[^>]+>)", html); n = 0; out = []; in_style = False
    for p in parties:
        if p.startswith("<"):
            if re.match(r"<(script|style)\b", p, re.I): in_style = True
            if re.match(r"</(script|style)\b", p, re.I): in_style = False
            out.append(p); continue
        if in_style or len(p.split()) < 2: out.append(p); continue
        q = p
        for rx, rep in CREUX:
            def sub(m):
                nonlocal n
                n += 1; s = m.string; i = m.start()
                deb = s[:i].strip() == "" or re.search(r"[.!?:]\s*$", s[:i]) is not None
                if rep == "": return m.group(m.lastindex).upper() if deb else m.group(m.lastindex)
                return rep[:1].upper() + rep[1:] if m.group(0)[:1].isupper() else rep
            q = rx.sub(sub, q)
        q = re.sub(r"\(\s*\)", "", q); q = re.sub(r"[ \t]{2,}", " ", q)
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
    h = re.sub(r"(<p[^>]*>)(.*?)(</p>)", dedup, h, flags=re.S)
    return h, n

# ---- cibles de contraction sémantique -------------------------------------------------------------------------
def cibles(html):
    from grille_agent import sections
    S = sections(re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", html)); L = []
    poids = sorted(((len(re.sub(r"<[^>]+>", " ", v).split()), p) for p, v in S.items()), reverse=True)[:5]
    L.append("POINTS LES PLUS LOURDS (mots) : " + ", ".join(f"point {p} = {w}" for w, p in poids))
    t = re.sub(r"(?s)<span class=\"(?:df|dxc)\">.*?</span></span>", " ", corps(html)); t = re.sub(r"(?is)<table.*?</table>", " ", t)
    ph = [x.strip() for x in re.split(r"(?<=[.!?;])\s+", re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t))) if len(x.split()) >= 4]
    lg = sorted(((len(x.split()), x) for x in ph if len(x.split()) > 25), reverse=True)[:8]
    L += [f"PHRASE LONGUE {n} mots : « {x[:110]}… » → scinde ou resserre" for n, x in lg]
    d = nlp().pipe([x for x in ph[:900]]); ens = []
    for x, doc in zip(ph[:900], d): ens.append((x, {w.lemma_.lower() for w in doc if w.pos_ in ("NOUN", "PROPN", "NUM", "VERB") and len(w.lemma_) > 2}))
    red = []
    for i in range(len(ens)):
        for j in range(i + 1, len(ens)):
            a, b = ens[i][1], ens[j][1]
            if len(a) >= 5 and len(b) >= 5 and len(a & b) / len(a | b) >= 0.7: red.append((len(a & b) / len(a | b), ens[i][0], ens[j][0]))
    for s, a, b in sorted(red, reverse=True)[:8]: L.append(f"REDITE {s:.2f} : « {a[:70]}… » ≈ « {b[:70]}… » → garde la meilleure, fusionne")
    return L

# ---- commandes -----------------------------------------------------------------------------------------------
def chemins(lot, nom):
    wk = R / ".cache/travail" / f"LOT_{lot}"
    import os
    if os.environ.get("G14_TEST"): wk = R / ".cache/test_g14"
    d = wk / "contracte"; d.mkdir(parents=True, exist_ok=True)
    return wk, d / f"{nom}.snap.json", d / f"{nom}.visa.json"

def sha(t): return hashlib.sha256(t.encode()).hexdigest()[:16]

def main(ag, cmd, args):
    from grille_agent import verifier_integrite; verifier_integrite()
    lot = "001"
    for i, x in enumerate(args):
        if x == "--lot": lot = args[i + 1]
    f = Path(args[0]) if args else None
    if f is None: print(__doc__); return 2
    nom = f.name
    ro = json.loads((R / f"harnais/grille14/roster_{lot}.json").read_text()); aud = ag.replace("K", "", 1)
    if nom not in ro["auditeurs"].get(aud, []): print(f"HORS TERRITOIRE : {nom} n'est pas à {aud}. STOP."); return 3
    wk, snapf, visaf = chemins(lot, nom)
    chemin = f.resolve() if f.exists() else wk / nom
    from grille_agent import reparer
    h0 = chemin.read_text(encoding="utf-8", errors="replace")
    if cmd == "etat":
        s = json.loads(snapf.read_text()) if snapf.exists() else None; v = json.loads(visaf.read_text()) if visaf.exists() else None
        print(json.dumps(dict(fichier=nom, mots_actuels=len(texte(h0).split()), mots_entree=s and s["inv"]["mots"], visa=v), ensure_ascii=False, indent=1)); return 0
    if cmd == "contracter":
        if not snapf.exists():
            snapf.write_text(json.dumps(dict(inv=inventaire(h0), t=time.strftime("%H:%M:%S")), ensure_ascii=False)); print(f"INVENTAIRE pris à l'entrée : {len(texte(h0).split())} mots, {len(inventaire(h0)['nombres'])} nombres, {len(inventaire(h0)['meds'])} médicaments.")
        h, n = contraction_mecanique(h0)
        if h != h0:
            bak = R / ".cache/bak"; bak.mkdir(exist_ok=True); (bak / f"{ag}_{nom}_avant_contraction").write_text(h0, encoding="utf-8")
            chemin.write_text(h, encoding="utf-8")
        print(f"CONTRACTION MÉCANIQUE (gratuite) : {n} formule(s) creuse(s) ou doublon(s) retiré(s) ; {len(texte(h0).split()) - len(texte(h).split())} mots en moins.")
        av = json.loads(snapf.read_text())["inv"]; mots = len(texte(h).split()); red = 100 * (1 - mots / av["mots"])
        print(f"VOLUME : {av['mots']} mots à l'entrée → {mots} maintenant (−{red:.1f} %). Cible : −{CIBLE['reduction_pct']} % OU ≤ {CIBLE['mots_max']} mots.")
        print("CIBLES POUR TA CONTRACTION SÉMANTIQUE (tu gardes toutes les notions ; tu supprimes redites, détails sans décision, tournures longues ; les détails utiles passent dans une fenêtre) :")
        for l in cibles(h): print(" -", l)
        print("Puis : verifier <fichier>"); return 0
    if cmd == "verifier":
        if not snapf.exists(): print("Pas d'inventaire : lance d'abord `contracter`."); return 1
        h, rep = reparer(h0, lot, nom)
        if h != h0: chemin.write_text(h, encoding="utf-8")
        av = json.loads(snapf.read_text())["inv"]; ap = inventaire(h); exc = set()
        if "--exceptions" in args: exc = {x.strip().lower() for x in args[args.index("--exceptions") + 1].split(",") if x.strip()}
        pb = []; L = []
        for cle, seuil, nm in (("nombres", 1.0, "nombres"), ("meds", 1.0, "médicaments"), ("termes", .95, "termes cliquables"), ("renvois", .95, "renvois [Sn]"), ("lemmes", .95, "notions (noms)")):
            manq, r = perdus(av, ap, cle); manq = [x for x in manq if x.lower() not in exc]
            r = 1 - len(manq) / len(av[cle]) if av[cle] else 1.0
            L.append(f"{nm} : {100 * r:.1f} % conservés ({len(manq)} perdus)")
            if r < seuil - 1e-9: pb.append(f"{nm} perdus ({100 * r:.1f} % < {100 * seuil:.0f} %) : " + ", ".join(manq[:25]) + (" …" if len(manq) > 25 else ""))
        if ap["tableaux"] != av["tableaux"] and (len(ap["tableaux"]) < len(av["tableaux"]) or sum(ap["tableaux"]) < .9 * sum(av["tableaux"])): pb.append(f"tableaux amputés : {av['tableaux']} → {ap['tableaux']}")
        if set(av["points"]) - set(ap["points"]): pb.append("points disparus : " + str(sorted(set(av["points"]) - set(ap["points"]))))
        mots = ap["mots"]; red = 100 * (1 - mots / av["mots"]); vol_ok = red >= CIBLE["reduction_pct"] or mots <= CIBLE["mots_max"]
        L.append(f"volume : {av['mots']} → {mots} mots (−{red:.1f} %) ; cible −{CIBLE['reduction_pct']} % ou ≤ {CIBLE['mots_max']}")
        if not vol_ok: pb.append(f"volume insuffisant : −{red:.1f} % (cible −{CIBLE['reduction_pct']} %) et {mots} mots (plafond {CIBLE['mots_max']}) : contracte encore (voir cibles de `contracter`)")
        print("\n".join(L))
        if pb:
            visaf.unlink(missing_ok=True); print("REFUSÉ :\n - " + "\n - ".join(pb)); return 1
        visaf.write_text(json.dumps(dict(sha=sha(h), mots_avant=av["mots"], mots_apres=mots, reduction_pct=round(red, 1), exceptions=sorted(exc), agent=ag, t=time.strftime("%H:%M:%S")), ensure_ascii=False))
        print(f"VISA POSÉ : −{red:.1f} % de volume, notions conservées. Tu peux lancer `fin` de ton script d'auditeur (sans modifier le fichier ensuite)."); return 0
    print(__doc__); return 2

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3:]))
