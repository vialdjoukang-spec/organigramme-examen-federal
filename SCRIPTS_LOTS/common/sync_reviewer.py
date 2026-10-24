#!/usr/bin/env python3
"""SCRIPT SYNCHRONE — relecteur en direct, STRICTEMENT EN LECTURE SEULE sur les LOT, sans aucune IA.

Commandes :
  review FICHIER.html [--appel-a FICHIER] [--etiquette LOT_X_...] [--sans-lt]   un passage
  watch  DOSSIER_LOT [--intervalle 5]                                          passages après chaque pause de rédaction
  retours --lot LOT_X [--fichier NOM]                                          affiche les derniers retours
Il applique les règles du V7-Tunder en citant leur section, sans les réécrire. Il écrit uniquement dans son dossier de sortie.
Codes de sortie : 0 aucun P1 · 1 au moins un P1 · 2 refus (isolation, série, droits) · 3 LOT modifié pendant le passage (alerte)."""
import argparse, hashlib, json, os, re, sys, time
from html.parser import HTMLParser
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import config as cfgmod, lot_readonly, v7_rules
from controle_v7 import controler
from languagetool import LanguageTool
from lot_readonly import ViolationLectureSeule

ICI = Path(__file__).resolve().parent
REGLES = json.loads((ICI / "rules_langue.json").read_text("utf-8"))
MAX_PHRASES = 4            # V7-Tunder §7.2 : « 1 à 4 phrases courtes et denses »
VERBES = set("est sont était étaient sera seront serait a ont avait avaient aura auront peut peuvent pourrait doit doivent devrait fait font "
             "va vont reste restent permet permettent signe signent indique indiquent impose imposent exige exigent survient surviennent "
             "apparaît apparaissent touche touchent provoque provoquent entraîne entraînent oriente orientent confirme confirment exclut "
             "excluent traduit traduisent associe associent comporte comportent comprend comprennent nécessite nécessitent suffit suffisent "
             "correspond correspondent concerne concernent dépend dépendent repose reposent vise visent recherche recherchent reçoit reçoivent "
             "devient deviennent tient tiennent prend prennent mesure mesurent baisse augmente diminue diminuent augmentent existe existent "
             "définit définissent désigne désignent précède suit suivent".split())
RE_VERBE_SUFFIXE = re.compile(r"\b\w{3,}(?:ent|ons|ez|ait|aient|era|eront|erait|ira|iront|isse|issent)\b|\b(?:se|s'|il|elle|on|ils|elles|qui|nous|vous|on)\s+\w+", re.I)
RE_ABBR = re.compile(r"\b[A-Z][A-Z0-9]{1,5}\b")
ABBR_OK = {"DX", "SSP", "LOT", "HTML", "OK", "II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII", "PDF", "URL", "FIN", "CH", "UE", "S1", "A", "B", "C", "D"}

# ---------- mini-DOM ----------
class Noeud:
    __slots__ = ("tag", "attrs", "enfants", "texte", "ligne", "parent")
    def __init__(s, tag, attrs, ligne, parent):
        s.tag, s.attrs, s.enfants, s.texte, s.ligne, s.parent = tag, dict(attrs), [], "", ligne, parent

class _Dom(HTMLParser):
    VIDES = {"br", "hr", "meta", "link", "img", "input", "col", "wbr", "source"}
    def __init__(s):
        super().__init__(convert_charrefs=True); s.racine = Noeud("#doc", [], 0, None); s.cour = s.racine
    def handle_starttag(s, t, a):
        n = Noeud(t, a, s.getpos()[0], s.cour); s.cour.enfants.append(n)
        if t not in s.VIDES: s.cour = n
    def handle_endtag(s, t):
        n = s.cour
        while n is not s.racine and n.tag != t: n = n.parent
        if n is not s.racine: s.cour = n.parent
    def handle_data(s, d):
        s.cour.enfants.append(d)

BLOCS_ESPACE = {"p", "li", "td", "th", "tr", "div", "br", "summary", "caption", "h1", "h2", "h3", "h4", "table"}
def texte(n):
    return "".join(c if isinstance(c, str) else (" " + texte(c) + " " if c.tag in BLOCS_ESPACE else texte(c)) for c in n.enfants)

def est_monographie(n):
    return n.tag == "details" and "open" in n.attrs and "inline" not in (n.attrs.get("style") or "").replace(" ", "")

def monographies(racine):
    res = []
    def par(n):
        for c in n.enfants:
            if isinstance(c, Noeud):
                if est_monographie(c): res.append(c)
                else: par(c)
    par(racine); return res

def phrases(t):
    t = re.sub(r"\s+", " ", t).strip()
    if not t: return []
    morceaux = re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-ÝÉÈ«(0-9])", t)
    return [m for m in morceaux if len(m.split()) >= 3]

def a_verbe(ph):
    mots = set(re.findall(r"[a-zàâçéèêëîïôûùüÿœ']+", ph.lower()))
    return bool(mots & VERBES) or bool(RE_VERBE_SUFFIXE.search(ph))

def court(msg, n=25):
    m = msg.split(); return " ".join(m[:n]) + (" …" if len(m) > n else "")

# ---------- analyse d'une monographie ----------
def analyser_monographie(mono, idx, prompt):
    summ = next((c for c in mono.enfants if isinstance(c, Noeud) and c.tag == "summary"), None)
    nom = re.sub(r"\s+", " ", texte(summ)).strip()[:60] if summ else f"monographie {idx}"
    m = re.search(r"DX\.\s?\d+", nom); lieu0 = m.group(0).replace(" ", "") if m else (nom.split("—")[0].strip() or f"M{idx}")
    points = {}; ordre = []; cour = {"n": None}
    def nouveau(n):
        points.setdefault(n, {"principal": "", "fenetres": 0, "fenetres_titres": [], "complet": "", "hors_table": "", "tableaux": 0, "ligne": None}); ordre.append(n); cour["n"] = n
    def parc(n, dans_fenetre, dans_table):
        for c in n.enfants:
            if isinstance(c, str):
                if cour["n"] is not None:
                    p = points[cour["n"]]; p["complet"] += c
                    if not dans_table: p["hors_table"] += c
                    if not dans_fenetre and not dans_table: p["principal"] += c
                continue
            if c.tag == "summary" and c.parent is mono:
                continue
            if c.tag == "strong" and not dans_fenetre:
                t = texte(c); mm = re.match(r"\s*(\d{1,2})\s*[.)]", t)
                if mm and 1 <= int(mm.group(1)) <= 14:
                    nouveau(int(mm.group(1))); points[cour["n"]]["ligne"] = c.ligne; points[cour["n"]]["titre"] = t.strip(); continue
            if c.tag == "details":
                if cour["n"] is not None:
                    points[cour["n"]]["fenetres"] += 1
                    s = next((x for x in c.enfants if isinstance(x, Noeud) and x.tag == "summary"), None)
                    if s: points[cour["n"]]["fenetres_titres"].append(texte(s))
                parc(c, True, dans_table); continue
            if c.tag == "table" and cour["n"] is not None and not dans_fenetre:
                points[cour["n"]]["tableaux"] += 1
            if c.tag in BLOCS_ESPACE and cour["n"] is not None:
                p = points[cour["n"]]; p["complet"] += " "; p["hors_table"] += " "
                if not dans_fenetre and not dans_table: p["principal"] += " "
            parc(c, dans_fenetre, dans_table or c.tag == "table")
            if c.tag in BLOCS_ESPACE and cour["n"] is not None:
                p = points[cour["n"]]; p["complet"] += " "; p["hors_table"] += " "
                if not dans_fenetre and not dans_table: p["principal"] += " "
    parc(mono, False, False)
    items = []
    def ajout(g, sec, lieu, msg, ext=""):
        assert sec.split(" ")[0] in prompt["refs"] or sec in prompt["refs"], f"référence inconnue {sec}"
        items.append({"gravite": g, "section": sec, "lieu": lieu, "message": court(msg), "extrait": ext[:120]})
    attendus = dict(prompt["points"])
    manquants = [n for n in range(1, 15) if n not in points]
    if manquants:
        ajout("P1", "§6", lieu0, f"points absents : {', '.join(map(str, manquants))} (« Aucun point ne manque »)")
    if ordre != sorted(ordre):
        ajout("P2", "§6", lieu0, f"ordre des points non conforme : {ordre}")
    for n in sorted(points):
        p = points[n]; lieu = f"{lieu0} · point {n}"
        titre = p.get("titre", "")
        if n in attendus and v7_rules.mot_cle(attendus[n]) not in titre.lower():
            ajout("P3", "§6", lieu, f"intitulé éloigné du plan : attendu « {attendus[n]} »", titre)
        corps = p["principal"].replace(titre, "", 1)
        phs = phrases(corps); mots = len(corps.split())
        # §7.2 : « chaque point du texte principal tient en 1 à 4 phrases » ; une sous-partie (9.a, 11.B, 7.1…) compte comme un point.
        segs = re.split(r"(?<![\w.])(?:\d{1,2}\.[a-dA-D]|\d{1,2}\.\d)(?=[\s\-–—:])", corps)
        trop = [ss for ss in (phrases(x) for x in segs) if len(ss) > MAX_PHRASES]
        if trop:
            ajout("P1", "§7.2", lieu, f"{len(trop[0])} phrases dans le texte principal (maximum {MAX_PHRASES}) : déplacer les explications dans des fenêtres <details>", trop[0][MAX_PHRASES])
        longues = [ph for ph in phs if len(ph.split()) > 35]
        if longues:
            ajout("P2", "§7.2", lieu, "phrase longue dans le texte principal : la scinder ou la déplacer dans une fenêtre", longues[0])
        if mots > 90 * max(1, len(segs)) and not trop:
            ajout("P2", "§8.2", lieu, f"{mots} mots dans le texte principal : l'explication détaillée relève d'une fenêtre")
        if len(phs) >= 2 and p["fenetres"] == 0:
            ajout("P2", "§8.1", lieu, "aucune fenêtre cliquable : termes, signes, examens et médicaments doivent ouvrir une fenêtre")
        for ph in phrases(p["hors_table"]):
            if len(ph.split()) <= 12 and not a_verbe(ph):
                ajout("P2", "§7.1", lieu, "phrase nominale probable (aucun verbe conjugué repéré)", ph); break
    def contient(n, *mots):
        t = points.get(n, {}).get("complet", "").lower(); return any(m in t for m in mots)
    if 11 in points:
        t11 = points[11]["complet"]
        absents = [x for x in "ABCD" if not re.search(rf"\b11\.?\s?{x}\b|(?:^|\s){x}\s?[-–—.)]\s?(?:But|Moyens|Surveillance|Pronostic)", t11)]
        if absents: ajout("P1", "§14", f"{lieu0} · point 11", f"sous-parties 11.{'/'.join(absents)} non repérées")
        specs = {"grossesse": ("grossesse", "enceinte"), "allaitement": ("allaitement", "allaitante"), "sujet âgé": ("âgé", "gériatr"),
                 "enfant": ("enfant", "pédiatr"), "insuffisance hépatique": ("hépatique",), "insuffisance rénale": ("rénal", "dfge")}
        manq = [k for k, v in specs.items() if not contient(11, *v)]
        if manq: ajout("P1", "§14", f"{lieu0} · point 11", "situations spéciales non repérées : " + ", ".join(manq))
        if not contient(11, "sortie", "retour à domicile"): ajout("P1", "§14", f"{lieu0} · point 11", "critères de sortie d'hospitalisation non repérés")
        if contient(11, "compliqu") and not any("urgence" in f.lower() for f in points[11]["fenetres_titres"]):
            ajout("P1", "§8.5", f"{lieu0} · point 11", "forme compliquée sans fenêtre « Urgence — conduite chronologique »")
        if not contient(11, "surveill"): ajout("P2", "§16", f"{lieu0} · point 11", "surveillance (quoi, quand, pourquoi) non repérée")
    if 9 in points:
        manq = [x for x in "abcd" if not re.search(rf"\b9\.?\s?{x}\b", points[9]["complet"])]
        if manq: ajout("P2", "§6", f"{lieu0} · point 9", f"sous-parties 9.{'/'.join(manq)} non repérées")
    if 3 in points and points[3]["tableaux"] == 0 and "<table" not in points[3]["complet"]:
        ajout("P2", "§16", f"{lieu0} · point 3", "tableau de corrélation lésion → exploration → thérapeutique non repéré")
    textes = {n: p["complet"] for n, p in points.items()}
    return {"nom": nom, "lieu": lieu0, "items": items, "textes": textes}

# ---------- règles de langue ----------
def regles_langue(txt_par_lieu):
    items = []
    for lieu, t in txt_par_lieu:
        tl = " " + re.sub(r"\s+", " ", t.lower()) + " "
        for cat in ("remplissage", "pleonasmes"):
            r = REGLES[cat]
            for mo in r["motifs"]:
                if re.search(rf"(?<![\w']){re.escape(mo)}(?!\w)", tl):
                    items.append({"gravite": r["gravite"], "section": r["section"], "lieu": lieu, "message": f"{r['message']} : « {mo} »", "extrait": ""})
        for cat in ("anglicismes", "abus_de_langage"):
            r = REGLES[cat]
            for mo, rempl in r["motifs"].items():
                base = mo.split(" (")[0]
                if re.search(rf"(?<![\w']){re.escape(base.lower())}(?!\w)", tl):
                    items.append({"gravite": r["gravite"], "section": r["section"], "lieu": lieu, "message": f"{r['message']} : « {base} » → {rempl}", "extrait": ""})
        vag = REGLES["termes_vagues"]
        for ph in phrases(t):
            if re.search(r"\d", ph): continue
            for mo in vag["motifs"]:
                if re.search(rf"(?<!\w){re.escape(mo)}(?!\w)", ph.lower()):
                    items.append({"gravite": vag["gravite"], "section": vag["section"], "lieu": lieu, "message": f"{vag['message']} : « {mo} »", "extrait": ph[:120]}); break
        con = REGLES["connecteurs"]
        phs = phrases(t)
        if len(phs) >= 3 and not any(re.search(rf"(?<!\w){re.escape(c)}(?!\w)", t.lower()) for c in con["motifs"]):
            items.append({"gravite": con["gravite"], "section": con["section"], "lieu": lieu, "message": con["message"], "extrait": ""})
        m = re.search(r"\b\d+\.\d+\s?(?:mg|µg|g|kg|ml|mL|mmol|µmol|%|L|U|UI)\b", t)
        if m: items.append({"gravite": "P2", "section": "§7.8", "lieu": lieu, "message": "virgule décimale attendue", "extrait": m.group(0)})
        m = re.search(r"\bmg/dl\b|\bmg/dL\b|°F", t)
        if m: items.append({"gravite": "P3", "section": "§7.8", "lieu": lieu, "message": "unité non SI : vérifier la conversion en mmol/L", "extrait": m.group(0)})
        if re.search(r"\"[^\"]{2,80}\"", t): items.append({"gravite": "P3", "section": "§7.8", "lieu": lieu, "message": "guillemets droits : utiliser « »", "extrait": ""})
    return items

def abreviations(texte_complet):
    vues, items = set(), []
    for m in RE_ABBR.finditer(texte_complet):
        a = m.group(0)
        if a in vues or a in ABBR_OK or a.isdigit() or re.fullmatch(r"S\d+", a): continue
        vues.add(a)
        autour = texte_complet[max(0, m.start() - 3): m.end() + 3]
        apres = texte_complet[m.end(): m.end() + 80]
        if f"({a})" in autour or re.match(r"\s*\(", apres):
            continue
        items.append({"gravite": "P2", "section": "§7.4", "lieu": "fichier", "message": f"abréviation « {a} » non développée à sa première apparition", "extrait": texte_complet[max(0, m.start() - 50): m.end() + 30].strip()})
    return items[:15]

def coherence_dx(html, html_a):
    def liste(h):
        return {int(n): re.sub(r"\s+", " ", t).strip().lower() for n, t in re.findall(r"DX\.(\d{1,2})\s*[—:–-]\s*([^<\n]{3,80}?)\s*(?:<|\n|$)", h)}
    a, b = liste(html_a), liste(html); items = []
    for n, nom in b.items():
        if n in a and a[n] != nom:
            items.append({"gravite": "P1", "section": "§9.5", "lieu": f"DX.{n}", "message": f"nom différent de l'Appel A : « {a[n]} »", "extrait": nom})
    return items

# ---------- passage complet ----------
class Relecteur:
    def __init__(self, cfg):
        self.cfg = cfg; self.prompt = v7_rules.charger(cfg["prompt_path"])
        self.cache_f = Path(cfg["cache_dir"]) / "relecteur_segments.json"   # aucun dossier créé avant la garde
        try: self.cache = json.loads(self.cache_f.read_text())
        except Exception: self.cache = {}

    def _garde(self, fichier):
        n = lot_readonly.numero_lot(fichier)
        if n is None or not cfgmod.lot_autorise(self.cfg, n):
            raise ViolationLectureSeule(f"{fichier} hors de la série LOT_{self.cfg['lot_min']}–{self.cfg['lot_max']} de l'agent {self.cfg['agent']}")
        dossier_lot = str(Path(fichier).resolve().parent)
        dossiers = [dossier_lot] + ([self.cfg["lots_root"]] if self.cfg.get("lots_root") else [])
        for cle in ("output_dir", "cache_dir", "shared_state_dir"):
            lot_readonly.verifier_isolation(self.cfg[cle], dossiers)
        if self.cfg.get("enforce_os_readonly"):
            lot_readonly.verifier_droits_os(dossier_lot)
        return n, dossier_lot, dossiers

    def passage(self, fichier, appel_a=None, etiquette=None, avec_lt=True):
        t0 = time.perf_counter()
        n, dossier_lot, dossiers = self._garde(fichier)          # refus AVANT toute création de dossier ou lecture
        Path(self.cfg["cache_dir"]).mkdir(parents=True, exist_ok=True)
        avant = lot_readonly.empreintes(dossier_lot)
        raw = lot_readonly.lire_octets(fichier); html = raw.decode("utf-8", "replace")
        if not etiquette:
            m = re.search(r"<!--\s*FIN_FICHIER\s+(\S+)\s*-->", html); etiquette = m.group(1) if m else Path(fichier).stem
        items = [{"gravite": "P1", "section": s, "lieu": "fichier", "message": court(e), "extrait": ""} for s, e in controler(raw, etiquette)]
        from source_engine import verifier_sources
        pb, st = verifier_sources(html)
        items += [{"gravite": x["gravite"], "section": x["section"], "lieu": f"ligne {x['ligne']}" if x["ligne"] else "Sources", "message": court(x["message"]), "extrait": x["extrait"]} for x in pb]
        dom = _Dom(); dom.feed(html)
        monos = monographies(dom.racine); segments_evites = 0; textes = []
        if not monos:
            items.append({"gravite": "P1", "section": "§10", "lieu": "fichier", "message": "aucune monographie <details open> repérée", "extrait": ""})
        for i, mo in enumerate(monos, 1):
            h = hashlib.sha256((texte(mo) + str(len(mo.enfants))).encode()).hexdigest()
            if h in self.cache:
                r = self.cache[h]; segments_evites += 1
            else:
                r = analyser_monographie(mo, i, self.prompt)
                r["items"] += regles_langue([(f"{r['lieu']} · point {k}", v) for k, v in sorted(r["textes"].items())])
                self.cache[h] = r
            items += r["items"]; textes.append(" ".join(r["textes"].values()))
        corps_html = re.split(r"<h[1-4][^>]*>\s*Sources", html)[0]
        corps_html = re.sub(r"<title>.*?</title>", " ", corps_html, flags=re.S)
        items += abreviations(re.sub(r"<[^>]+>", " ", corps_html))
        if appel_a:
            items += coherence_dx(html, lot_readonly.lire_octets(appel_a).decode("utf-8", "replace"))
        lt = {"statut": "NON VÉRIFIÉ", "raison": "désactivé pour ce passage", "correspondances": []}
        if avec_lt and textes:
            lt = LanguageTool(self.cfg).verifier("\n".join(textes))
            for x in lt["correspondances"][:30]:
                items.append({"gravite": "P2" if x["categorie"] in ("GRAMMAR", "TYPOS", "CONFUSED_WORDS") else "P3", "section": "§0.5",
                              "lieu": "LanguageTool", "message": court(f"{x['message']} ({x['regle']})" + (f" → {x['suggestions'][0]}" if x["suggestions"] else "")), "extrait": x["contexte"]})
        apres = lot_readonly.empreintes(dossier_lot)
        lot_readonly.ecrire_sortie(self.cache_f, json.dumps(dict(list(self.cache.items())[-500:]), ensure_ascii=False), self.cfg["cache_dir"], dossiers)
        ordre = {"P1": 0, "P2": 1, "P3": 2}; items.sort(key=lambda x: ordre[x["gravite"]])
        res = {"fichier": str(fichier), "lot": f"LOT_{n}", "agent": self.cfg["agent"], "horodatage": time.strftime("%Y-%m-%d %H:%M (%Z)"),
               "duree_ms": round(1000 * (time.perf_counter() - t0), 1), "monographies": len(monos), "segments_evites": segments_evites,
               "languagetool": {"statut": lt["statut"], "raison": lt.get("raison")}, "stats_sources": st,
               "compte": {g: sum(1 for x in items if x["gravite"] == g) for g in ordre}, "items": items,
               "integrite": "ok" if avant == apres else "ALERTE"}
        sortie = Path(self.cfg["output_dir"]) / f"LOT_{n}"
        if avant != apres:
            diff = sorted(k for k in set(avant) | set(apres) if avant.get(k) != apres.get(k))
            lot_readonly.ecrire_sortie(sortie / f"ALERTE_{int(time.time())}.md", f"# ALERTE — LOT_{n} modifié pendant le passage\n\nFichiers : {diff}\nPassage annulé ; aucun retour publié. Le relecteur n'écrit jamais dans le LOT : vérifier l'origine de la modification.\n", self.cfg["output_dir"], dossiers)
            res["code"] = 3; return res
        lot_readonly.ecrire_sortie(sortie / f"{Path(fichier).stem}.retours.json", json.dumps(res, ensure_ascii=False, indent=1), self.cfg["output_dir"], dossiers)
        lot_readonly.ecrire_sortie(sortie / f"{Path(fichier).stem}.retours.md", rendu_md(res), self.cfg["output_dir"], dossiers)
        res["code"] = 1 if res["compte"]["P1"] else 0
        return res

def rendu_md(r, maxi=10):
    noms = {"P1": "P1 bloquant", "P2": "P2 important", "P3": "P3 amélioration"}
    l = [f"{r['lot']} · {Path(r['fichier']).name} · {r['horodatage']} · {r['duree_ms']} ms · {r['monographies']} monographie(s)"]
    for g in ("P1", "P2", "P3"):
        sel = [x for x in r["items"] if x["gravite"] == g]
        if not sel: continue
        l.append(f"{noms[g]} ({len(sel)})")
        for x in sel[: maxi if g == "P1" else max(0, maxi - r["compte"]["P1"]) or 3]:
            l.append(f"- [{x['section']}] {x['lieu']} : {x['message']}" + (f" — « {x['extrait'][:80]} »" if x["extrait"] else ""))
    l.append(f"Langue (LanguageTool) : {r['languagetool']['statut']}" + (f" — {r['languagetool']['raison']}" if r["languagetool"].get("raison") else ""))
    l.append("Non vérifiable par machine : exactitude des doses, actualité des recommandations (audit Tunder). Détail complet : fichier .json.")
    return "\n".join(l) + "\n"

def surveiller(rel, dossier, intervalle=5):
    debounce = rel.cfg["languagetool"]["debounce_s"]; vus = {}
    print(f"Surveillance de {dossier} (lecture seule ; pause de rédaction {debounce} s)", file=sys.stderr)
    while True:
        for f in sorted(Path(dossier).glob("LOT_*.html")):
            mt = f.stat().st_mtime
            etat = vus.setdefault(str(f), {"mt": None, "fait": None})
            if mt != etat["mt"]:
                etat["mt"] = mt; etat["depuis"] = time.time()
            elif etat["fait"] != mt and time.time() - etat["depuis"] >= debounce:
                r = rel.passage(str(f)); etat["fait"] = mt
                print(f"{f.name} : P1={r['compte']['P1']} P2={r['compte']['P2']} P3={r['compte']['P3']} · {r['duree_ms']} ms · intégrité {r['integrite']}", file=sys.stderr)
        time.sleep(intervalle)

def main(config_path, argv=None):
    cfg = cfgmod.charger(config_path)
    ap = argparse.ArgumentParser(prog=f"script_synchrone (agent {cfg['agent']})", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    r = sp.add_parser("review"); r.add_argument("fichier"); r.add_argument("--appel-a"); r.add_argument("--etiquette"); r.add_argument("--sans-lt", action="store_true")
    w = sp.add_parser("watch"); w.add_argument("dossier"); w.add_argument("--intervalle", type=float, default=5)
    t = sp.add_parser("retours"); t.add_argument("--lot", required=True); t.add_argument("--fichier")
    a = ap.parse_args(argv)
    try:
        rel = Relecteur(cfg)
        if a.cmd == "review":
            res = rel.passage(a.fichier, a.appel_a, a.etiquette, not a.sans_lt)
            print(rendu_md(res)); return res["code"]
        if a.cmd == "watch":
            surveiller(rel, a.dossier, a.intervalle); return 0
        if a.cmd == "retours":
            d = Path(cfg["output_dir"]) / a.lot
            fs = sorted(d.glob(f"{a.fichier or '*'}.retours.md"), key=lambda p: p.stat().st_mtime)
            if not fs: print("aucun retour"); return 0
            print(fs[-1].read_text("utf-8")); return 0
    except ViolationLectureSeule as e:
        print(f"REFUS (lecture seule) : {e}", file=sys.stderr); return 2

if __name__ == "__main__":
    print("Utilisez agent_N/script_synchrone.py", file=sys.stderr); sys.exit(2)
