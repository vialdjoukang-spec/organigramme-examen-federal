#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recherche gratuite et obsessionnelle de clichés radiologiques candidats (normal + pathologique).

Sources (licences libres seulement : CC0, domaine public, CC BY, CC BY-SA ; NC/ND et rétractés exclus) :
  1. Index locaux MultiCaRe v3 + ROCOv2 (métadonnées Zenodo, légendes filtrées par regex) -> images originales PMC (AWS)
  2. Europe PMC REST : FIG:"<terme>" AND FIG:<modalité> AND OPEN_ACCESS:y AND licence libre -> fullTextXML -> AWS
  3. Wikimedia Commons : recherche EN + DE (namespace 6), imageinfo/extmetadata ; bibliothèque de normaux
     (recherches « normal … » / « Normalbefund … » + séries d'auteurs Häggström, Hellerhoff via list=allimages)

Usage :
  python3 chercher.py --de IMG-042 --a IMG-344            # recherche + téléchargement (reprise automatique)
  python3 chercher.py --stats                             # avancement chiffré
Ne choisit PAS l'image finale ; ne pose pas de repères. N'écrit jamais dans enrichi/*.json.
"""
import argparse, csv, glob, hashlib, html, io, json, os, re, sys, time, urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime

import requests

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from termes import charger_diag, detecter_modalite, detecter_details, MODALITE_INFO  # noqa: E402

RECENS = os.path.dirname(ICI)
CACHE = os.path.join(ICI, "cache")
HTTP_CACHE = os.path.join(CACHE, "http")
INDEX = os.path.join(CACHE, "index")
CANDIDATS = os.path.join(ICI, "candidats")
JOURNAL = os.path.join(ICI, "journal.log")
UA = "ProgressionEdu-ImageSearch/1.0 (educational, non-commercial; Swiss medical exam teaching) python-requests"
MAX_PAR_ROLE = 6
LARGEUR_MAX = 900

LIC_OK_PMC = {"CC BY", "CC BY-SA", "CC0", "CC-BY", "CC BY 4.0", "CC0 1.0"}
SESSION = requests.Session()
SESSION.headers["User-Agent"] = UA
_dernier = {}
# Disjoncteur Commons : après des 429 répétés, Commons est mis en pause et les id concernés repassent plus tard
ETAT_COMMONS = {"bloque_jusqua": 0.0, "echecs": 0}
PAUSE_COMMONS = 600
INTERVALLES = {"commons": 2.0, "upload": 1.0, "epmc": 0.25, "s3": 0.05, "autre": 0.2}


def log(msg):
    ligne = f"{datetime.now():%Y-%m-%d %H:%M:%S} {msg}"
    print(ligne, flush=True)
    with open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")


# ---------------------------------------------------------------- HTTP + cache disque maison
def _cle(url, params):
    brut = url + "?" + urllib.parse.urlencode(sorted((params or {}).items()))
    return brut, hashlib.sha1(brut.encode()).hexdigest()


def http_get(url, params=None, source="autre", binaire=False, essais=7):
    """GET avec cache disque (réponses 200 et 404), throttling par source et backoff exponentiel sur 429/5xx."""
    brut, h = _cle(url, params)
    chemin = os.path.join(HTTP_CACHE, h[:2], h + (".bin" if binaire else ".txt"))
    meta = chemin + ".status"
    if os.path.exists(meta):
        st = open(meta).read().strip()
        if st == "200" and os.path.exists(chemin):
            with open(chemin, "rb") as f:
                d = f.read()
            return 200, (d if binaire else d.decode("utf-8", "replace"))
        if st == "404":
            return 404, None
    attente = 10
    if source == "commons" and time.time() < ETAT_COMMONS["bloque_jusqua"]:
        ETAT_COMMONS["echecs"] += 1
        return 0, None
    for essai in range(essais):
        dt = time.time() - _dernier.get(source, 0)
        if dt < INTERVALLES[source]:
            time.sleep(INTERVALLES[source] - dt)
        _dernier[source] = time.time()
        try:
            r = SESSION.get(url, params=params, timeout=60)
        except requests.RequestException as e:
            log(f"  ! réseau {source} {e.__class__.__name__} ; nouvel essai dans {attente}s")
            time.sleep(attente); attente = min(attente * 2, 60); continue
        if r.status_code == 200:
            os.makedirs(os.path.dirname(chemin), exist_ok=True)
            with open(chemin, "wb") as f:
                f.write(r.content)
            open(meta, "w").write("200")
            return 200, (r.content if binaire else r.text)
        if r.status_code in (404, 410):
            os.makedirs(os.path.dirname(chemin), exist_ok=True)
            open(meta, "w").write("404")
            return 404, None
        if r.status_code in (429, 500, 502, 503, 504) or (source == "commons" and "ratelimited" in r.text[:500]):
            if source == "commons" and essai >= 1:
                ETAT_COMMONS["bloque_jusqua"] = time.time() + PAUSE_COMMONS
                ETAT_COMMONS["echecs"] += 1
                log(f"  ~ Commons saturé (429 répétés) : pause de {PAUSE_COMMONS}s, id reportés au complément")
                return 0, None
            ra = r.headers.get("Retry-After")
            pause = max(attente, int(ra)) if ra and ra.isdigit() else attente
            log(f"  ~ {source} HTTP {r.status_code} ; pause {pause}s")
            time.sleep(min(pause, 90)); attente = min(attente * 2, 60); continue
        log(f"  ! {source} HTTP {r.status_code} {brut[:160]}")
        return r.status_code, None
    return 0, None


def http_json(url, params=None, source="autre"):
    st, txt = http_get(url, params, source)
    if st != 200 or not txt:
        return None
    try:
        return json.loads(txt)
    except ValueError:
        return None


# ---------------------------------------------------------------- outils texte
def sans_html(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def rx_terme(terme):
    """Regex souple : chaque mot significatif doit apparaître (préfixe de 6 lettres), dans l'ordre libre."""
    mots = [m for m in re.findall(r"[A-Za-zÀ-ÿ0-9']+", terme) if len(m) > 2 or m.isupper()]
    return [re.compile(r"\b" + re.escape(m[:6] if len(m) > 6 else m), re.I) for m in mots]


def match_terme(terme, texte):
    if re.search(r"\b" + re.escape(terme) + r"", texte, re.I):
        return 2  # phrase exacte
    rxs = rx_terme(terme)
    if rxs and all(r.search(texte) for r in rxs):
        return 1
    return 0


REGION_RX = {
    "pituitary": r"pituitar|sella|hypophys", "sella": r"sella|pituitar|suprasellar", "orbit": r"orbit|optic nerve|globe",
    "eye": r"\beye\b|ocular|globe|orbit|retina", "paranasal sinuses": r"sinus|nasal", "temporal bone": r"temporal bone|mastoid|middle ear|petrous|cochlea",
    "face": r"facial|face|maxill|zygom|midface", "mandible": r"mandib|jaw|maxill|dental|panoram|orthopantom",
    "neck": r"neck|cervical|pharyn|laryn|hyoid", "thyroid": r"thyroid", "parotid": r"parotid|salivary", "salivary gland": r"salivary|submandibular|parotid",
    "carotid": r"carotid", "brain": r"brain|cerebr|head|intracranial", "temporal artery": r"temporal arter", "vertebral artery": r"vertebral arter|subclavian",
    "lumbar spine": r"lumbar|lumbosacral|L[1-5]", "cervical spine": r"cervical spine|C[1-7]\b|odontoid|cervical", "spine": r"spine|spinal|vertebra|lumbar|thoracic",
    "thoracolumbar spine": r"thoracolumbar|lumbar|thoracic spine|vertebra", "sacroiliac joint": r"sacroiliac|sacro-iliac|SIJ",
    "spinal cord": r"spinal cord|cord|thoracic spine|cervical spine", "chest": r"chest|thora|lung|pulmonar|thorax", "mediastinum": r"mediastin|chest|thora",
    "heart": r"heart|cardiac|ventric|atri|coronar|myocard", "aorta": r"aort", "breast": r"breast|mammo", "liver": r"liver|hepat",
    "gallbladder": r"gallbladder|gall bladder|biliary", "bile duct": r"bile duct|biliary|choledoch|cholangio|MRCP", "pancreas": r"pancrea",
    "spleen": r"splen|spleen", "abdomen": r"abdom|bowel|intestin|perito", "appendix": r"appendi|right lower quadrant", "colon": r"colon|colonic|sigmoid|bowel",
    "stomach": r"stomach|gastr", "small bowel": r"small bowel|ileum|ileal|jejun|enterograph", "pylorus": r"pylor", "esophagus": r"esophag|oesophag",
    "abdominal wall": r"abdominal wall|inguinal|rectus|psoas", "retroperitoneum": r"retroperiton", "kidney": r"kidney|renal|ureter",
    "adrenal": r"adrenal", "bladder": r"bladder|vesic", "prostate": r"prostat", "testis": r"testi|scrot", "inguinal": r"inguinal|testi|scrot",
    "ovary": r"ovar|adnex|pelvi", "uterus": r"uter|endometr|pelvi", "fetus": r"fetal|fetus|foetal", "placenta": r"placent", "pregnancy": r"pregnan|gestation",
    "anal canal": r"anal|perianal|pelvi", "pelvic floor": r"pelvic floor|pelvi", "shoulder": r"shoulder|glenohumeral|humer|clavic",
    "elbow": r"elbow", "forearm": r"forearm|radius|ulna", "wrist": r"wrist|carp|scaph|radius", "hand": r"hand|finger|metacarp|wrist|phalan",
    "arm": r"arm|axillary|subclavian|brachial|upper extremit|upper limb", "hip": r"hip|femoral head|pelvi", "pelvis": r"pelvi|acetab|sacr",
    "knee": r"knee|patell|tibial|femoral condyle|popliteal", "ankle": r"ankle|achilles|malleol|talus", "foot": r"foot|feet|metatars|calcane|toe",
    "leg": r"leg|femoral|popliteal|lower extremit|lower limb|calf", "groin": r"groin|femoral|inguinal", "bone": r"bone|femur|tibia|humer|osseous|skelet",
    "soft tissue": r"soft tissue|subcutaneous|fascia|thigh|leg", "muscle": r"muscle|muscul|thigh|calf", "whole body": r"whole[- ]body|PET|MIP",
    "head": r"head|skull|brain|cranial",
}

HISTO_RX = re.compile(r"H&E|hematoxylin|haematoxylin|eosin|micrograph|microscop|histolog|histopath|immunohisto|magnification|"
                      r"endoscop|colonoscop|bronchoscop|intraoperative|intra-operative|gross (specimen|appearance)|resected specimen|"
                      r"photograph|clinical (photo|picture|image)|fundus|OCT\b|electrocardiogr|\bECG\b|\bEKG\b|flow chart|flowchart|schematic|diagram|illustration|"
                      r"algorithm|\btable\b|graph showing|Kaplan|forest plot|PRISMA", re.I)
NEG_PATHO_RX = re.compile(r"no (evidence|sign|signs) of|without (evidence|signs?) of|ruled out|was excluded|follow-?up|"
                          r"resolution|resolved|improvement|improved|months later|weeks later|years later|after (treatment|therapy|antibiotic)|"
                          r"post-?treatment|remission|unremarkable|within normal limits|normal (appearance|findings?|study|examination|scan|CT|MRI|"
                          r"radiograph|x-ray|ultrasound|chest|anatomy|control)", re.I)
NORMAL_FAUX_RX = re.compile(r"(absence|loss|lack|effacement|displacement|compression) of (the )?normal|compared (with|to) (the )?normal|"
                            r"instead of|rather than (the )?normal|thicken|enlarg|replaced|obliterat|than normal|"
                            r"normal (size|caliber|calibre)d? .{0,40}(but|with)|postoperative|post-operative", re.I)
POSTOP_RX = re.compile(r"post-?operative|after surgery|surgical bed", re.I)
NORMAL_RX = re.compile(r"\bnormal\b|unremarkable|healthy (volunteer|subject|control)|no abnormalit|Normalbefund|\bnormale?[rsn]?\b|gesund", re.I)
NORMAL_NEG_RX = re.compile(r"abnormal|lesion|tumou?r|mass\b|fracture|hemorrhag|haemorrhag|infarct|metasta|carcinoma|cancer|effusion|"
                           r"thrombo|stenosis|abscess|cyst\b|aneurysm|dissection|pneumonia|consolidation|insuffic|ectop|\w{3,}oma\b|\w{4,}itis\b|"
                           r"Fraktur|Tumor|Zyste|Blutung|Infarkt", re.I)
FLECHES_RX = re.compile(r"arrow|arrowhead|asterisk|Pfeil", re.I)
PANNEAU_RX = re.compile(r"(?:^|[\s;.,])\(?([A-Ha-h])[\)\.:](?=\s)|\(([A-Ha-h])(?:[,\-–][A-Ha-h])?\)")


def panneaux(texte):
    """Découpe une légende multi-panneaux. Renvoie (préambule, [(lettre, segment)])."""
    pos = [(m.start(), (m.group(1) or m.group(2)).upper()) for m in PANNEAU_RX.finditer(texte)]
    lettres = []
    for p, l in pos:
        if l not in [x[1] for x in lettres]:
            lettres.append((p, l))
    if len({l for _, l in lettres}) < 2:
        return texte, []
    segs = []
    for i, (p, l) in enumerate(lettres):
        fin = lettres[i + 1][0] if i + 1 < len(lettres) else len(texte)
        segs.append((l, texte[p:fin]))
    return texte[:lettres[0][0]], segs


# ---------------------------------------------------------------- contexte par id
def contexte(item, enr, diag):
    ctx = {"id": item["id"], "diagnostic": item["diagnostic"], "gold": (enr.get("gold") or {}).get("examen", ""),
           "termes_en": diag["en"], "terme_de": diag["de"], "region": diag["region"], "region_de": diag["region_de"],
           "region_rx": REGION_RX.get(diag["region"], re.escape(diag["region"])), "roles": {}}
    ac = (enr.get("images") or {}).get("a_chercher") or {}
    techs = [t["tech"] for t in item.get("techniques", [])]
    defaut = {"TDM": "CT", "IRM": "MRI", "US": "US", "RX": "XR", "MN": "NM", "INT": "ANGIO"}.get(techs[0] if techs else "", "CT")
    for role in ("normal", "patho"):
        desc = ac.get(role) or ""
        mod = detecter_modalite(desc) or defaut
        ctx["roles"][role] = {"desc": desc, "modalite": mod, "details": detecter_details(desc)}
    return ctx


def score_legende(texte, ctx, role, exige_modalite=True, panneau_connu=None):
    """Score d'une légende ; None = rejet. Renvoie (score, motifs, panneau)."""
    r = ctx["roles"][role]
    mi = MODALITE_INFO[r["modalite"]]
    if not texte or HISTO_RX.search(texte):
        return None
    pre, segs = panneaux(texte) if panneau_connu is None else (texte, [])
    cibles = [(None, texte)]
    if segs:
        cibles = []
        for l, s in segs:
            cibles.append((l, pre + " " + s))
    meilleur = None
    for lettre, t in cibles:
        seg_seul = t[len(pre):] if lettre else t
        motifs, sc = [], 0.0
        mod_ok = re.search(mi["rx"], t, re.I)
        if mod_ok:
            sc += 2; motifs.append("modalité")
        elif exige_modalite:
            continue
        else:
            autres = [k for k, v in MODALITE_INFO.items() if k != r["modalite"] and re.search(v["rx"], seg_seul if lettre else t, re.I)]
            if autres:
                continue
            sc -= 1
        if role == "patho":
            best = 0
            for i, terme in enumerate(ctx["termes_en"]):
                m = match_terme(terme, seg_seul if lettre else t)
                if not m and lettre:
                    m = match_terme(terme, pre) * 0.75
                if m:
                    best = max(best, (2.5 if m >= 2 else 1.5) + (1 if i == 0 else 0) + m)
            if ctx["terme_de"] and re.search(re.escape(ctx["terme_de"].split()[0][:8]), t, re.I):
                best = max(best, 3.5)
            if not best:
                continue
            sc += best; motifs.append("diagnostic")
            if NEG_PATHO_RX.search(seg_seul):
                continue
            if POSTOP_RX.search(seg_seul) and not re.search(r"post|transplant|leak|endoleak|fibrosis|recurren|implant|TIPS|repair",
                                                            " ".join(ctx["termes_en"]), re.I):
                continue
            if re.search(r"\bnormal\b", seg_seul, re.I):
                sc -= 1.5; motifs.append("contient «normal»")
        else:
            if not NORMAL_RX.search(seg_seul if lettre else t) or NORMAL_FAUX_RX.search(seg_seul if lettre else t):
                continue
            sc += 2.5; motifs.append("normal")
            if NORMAL_NEG_RX.search(seg_seul if lettre else t):
                sc -= 1.5; motifs.append("mot pathologique")
        if re.search(ctx["region_rx"], t, re.I):
            sc += 1.5; motifs.append("région")
            if role == "normal" and re.search(r"normal\W+(?:\w+\W+){0,3}?(?:" + ctx["region_rx"] + ")", seg_seul if lettre else t, re.I):
                sc += 1.5; motifs.append("«normal + région»")
        elif role == "normal":
            sc -= 2; motifs.append("région absente")
        for etiq, rx in r["details"]:
            if re.search(rx, seg_seul if lettre else t, re.I):
                sc += 1; motifs.append(etiq)
        if role == "patho" and FLECHES_RX.search(seg_seul if lettre else t):
            sc += 0.5; motifs.append("flèches")
        if lettre:
            sc -= 0.5; motifs.append(f"panneau {lettre}")
        if len(t) > 700:
            sc -= 0.5
        if meilleur is None or sc > meilleur[0]:
            meilleur = (round(sc, 2), motifs, lettre or panneau_connu)
    return meilleur


# ---------------------------------------------------------------- index locaux MultiCaRe / ROCOv2
SUBTYPE = {"ct": "CT", "mri": "MRI", "x_ray": "XR", "ultrasound": "US", "pet": "PET", "mammography": "MAMMO",
           "angiography": "ANGIO", "nuclear_medicine": "NM", "scintigraphy": "NM", "fluoroscopy": "FLUORO", "spect": "NM"}
ROCO_CUI = {"C0040405": "CT", "C1306645": "XR", "C0024485": "MRI", "C0041618": "US", "C0002978": "ANGIO",
            "C0032743": "PET", "C0203668": "NM", "C0034606": "NM", "C1699633": "PET", "C0016356": "FLUORO"}


def lic_libre(l):
    l = (l or "").upper().replace("-", " ")
    if "NC" in l.split() or "ND" in l.split() or "NC ND" in l or "NC SA" in l:
        return False
    return bool(re.match(r"^(CC BY( SA)?|CC0|CC 0|PUBLIC DOMAIN|PD)\b", l.strip()))


def charger_index():
    recs = []
    f = os.path.join(INDEX, "mc_captions_and_labels.csv")
    if os.path.exists(f):
        csv.field_size_limit(10 ** 8)
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row["image_type"] != "radiology" or not lic_libre(row["license"]):
                    continue
                m = re.match(r"(PMC\d+)_\d+_(.+)$", row["main_image"])
                if not m:
                    continue
                recs.append({"src": "MultiCaRe", "pmcid": m.group(1), "fichier": m.group(2), "legende": row["caption"],
                             "mod": SUBTYPE.get(row["image_subtype"]), "licence": row["license"],
                             "panneau": None if row["image_component"] in ("undivided", "") else row["image_component"].upper()})
    lic = {}
    f = os.path.join(INDEX, "roco_license_information.csv")
    if os.path.exists(f):
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                lic[row["ID"]] = (row["PMCID"], row["Attribution"])
    cui = {}
    for f in glob.glob(os.path.join(INDEX, "roco_*_concepts_manual.csv")):
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                for c in row["CUIs"].split(";"):
                    if c in ROCO_CUI:
                        cui[row["ID"]] = ROCO_CUI[c]; break
    for f in glob.glob(os.path.join(INDEX, "roco_*_captions.csv")):
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                pm, att = lic.get(row["ID"], (None, ""))
                if not pm or not lic_libre(att):
                    continue
                recs.append({"src": "ROCOv2", "pmcid": pm, "fichier": None, "legende": row["Caption"],
                             "mod": cui.get(row["ID"]), "licence": (re.match(r"^(CC0|CC BY(?:-SA)?)", att) or re.match(r".*", att)).group(0)[:12],
                             "panneau": None, "roco_id": row["ID"]})
    log(f"Index locaux : {len(recs)} images radiologiques sous licence libre (MultiCaRe + ROCOv2)")
    return recs


def chercher_index(recs, ctx, role, limite=40):
    mod = ctx["roles"][role]["modalite"]
    groupe = {mod} | ({"NM", "PET"} if mod in ("NM", "PET") else set()) | ({"XR", "MAMMO"} if mod == "MAMMO" else set())
    res = []
    if role == "patho":
        pre = [max(rx_terme(t), key=lambda r: len(r.pattern)) for t in ctx["termes_en"] if rx_terme(t)]
    for r in recs:
        if r["mod"] and r["mod"] not in groupe:
            continue
        leg = r["legende"]
        if role == "patho" and not any(p.search(leg) for p in pre):
            continue
        if role == "normal" and not NORMAL_RX.search(leg):
            continue
        s = score_legende(leg, ctx, role, exige_modalite=not bool(r["mod"]), panneau_connu=r["panneau"])
        if s is None:
            continue
        sc, motifs, pan = s
        if r["mod"] and "modalité" not in motifs:
            sc += 2; motifs = motifs + ["modalité (index)"]
        res.append({"source": r["src"], "pmcid": r["pmcid"], "fichier": r["fichier"], "legende": leg, "score": sc,
                    "motifs": motifs, "panneau": pan, "licence_index": r["licence"]})
    res.sort(key=lambda x: -x["score"])
    return res[:limite]


# ---------------------------------------------------------------- PMC : XML + AWS
NS_XLINK = "{http://www.w3.org/1999/xlink}href"


def figures_pmc(pmcid):
    st, txt = http_get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML", source="epmc")
    if st != 200 or not txt:
        return [], ""
    try:
        racine = ET.fromstring(txt.encode("utf-8"))
    except ET.ParseError:
        return [], ""
    titre = "".join(racine.find(".//article-title").itertext()) if racine.find(".//article-title") is not None else ""
    figs = []
    for fig in racine.iter("fig"):
        cap = fig.find("caption")
        leg = re.sub(r"\s+", " ", "".join(cap.itertext())).strip() if cap is not None else ""
        lab = fig.find("label")
        g = fig.find(".//graphic")
        href = g.get(NS_XLINK) if g is not None else None
        if href:
            figs.append({"label": (lab.text or "").strip() if lab is not None else "", "legende": leg, "href": href})
    return figs, re.sub(r"\s+", " ", titre).strip()


def meta_aws(pmcid):
    for v in (1, 2, 3, 4):
        j = http_json(f"https://pmc-oa-opendata.s3.amazonaws.com/{pmcid}.{v}/{pmcid}.{v}.json", source="s3")
        if j:
            j["_version"] = v
            # prendre la dernière version disponible
            j2 = http_json(f"https://pmc-oa-opendata.s3.amazonaws.com/{pmcid}.{v+1}/{pmcid}.{v+1}.json", source="s3")
            if j2:
                continue
            return j
    return None


def resoudre_pmc(c):
    """Complète un candidat PMC : licence AWS, rétractation, citation, URL d'image. False si inutilisable."""
    meta = meta_aws(c["pmcid"])
    if not meta:
        return False
    lic = (meta.get("license_code") or "").strip()
    if meta.get("is_retracted") or not lic_libre(lic):
        return False
    v = meta["_version"]
    medias = [u.split("?")[0].split("/")[-1] for u in meta.get("media_urls", [])]
    if not c.get("fichier"):  # ROCOv2 : retrouver la figure par la légende
        figs, _ = figures_pmc(c["pmcid"])
        tete = re.sub(r"\W+", " ", c["legende"].lower())[:60]
        for f in figs:
            if tete and tete in re.sub(r"\W+", " ", f["legende"].lower()):
                c["fichier"] = f["href"]; break
        if not c.get("fichier"):
            return False
    tige = os.path.splitext(c["fichier"])[0]
    choix = [m for m in medias if os.path.splitext(m)[0] == tige and m.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp", ".tif"))]
    choix.sort(key=lambda m: not m.lower().endswith((".jpg", ".jpeg")))
    if not choix:
        return False
    c["url_image"] = f"https://pmc-oa-opendata.s3.amazonaws.com/{c['pmcid']}.{v}/{choix[0]}"
    c["licence"] = lic
    c["auteur"] = meta.get("citation", "")
    c["titre_article"] = meta.get("title", "")
    c["url_source"] = f"https://europepmc.org/article/PMC/{c['pmcid']}"
    if meta.get("doi"):
        c["doi"] = meta["doi"]
    return True


LIC_Q = '(LICENSE:"cc by" OR LICENSE:"cc by-sa" OR LICENSE:"cc0")'


def chercher_epmc(ctx, role, max_articles=10):
    r = ctx["roles"][role]
    mi = MODALITE_INFO[r["modalite"]]
    if role == "patho":
        reqs = [f'FIG:"{t}" AND {mi["epmc"]} AND OPEN_ACCESS:y AND {LIC_Q} AND IN_EPMC:y' for t in ctx["termes_en"][:3]]
    else:
        reqs = [f'(FIG:normal OR FIG:unremarkable) AND FIG:"{ctx["region"]}" AND {mi["epmc"]} AND OPEN_ACCESS:y AND {LIC_Q} AND IN_EPMC:y']
    pmcids = []
    for q in reqs:
        j = http_json("https://www.ebi.ac.uk/europepmc/webservices/rest/search",
                      {"query": q, "format": "json", "resultType": "lite", "pageSize": 12}, source="epmc")
        for res in ((j or {}).get("resultList") or {}).get("result", []):
            if res.get("pmcid") and res["pmcid"] not in pmcids:
                pmcids.append(res["pmcid"])
    out = []
    for pm in pmcids[:max_articles]:
        figs, titre = figures_pmc(pm)
        for f in figs:
            s = score_legende(f["legende"], ctx, role)
            if s:
                out.append({"source": "EuropePMC", "pmcid": pm, "fichier": f["href"], "legende": f"{f['label']} {f['legende']}".strip(),
                            "score": s[0], "motifs": s[1], "panneau": s[2]})
    return out


# ---------------------------------------------------------------- Wikimedia Commons
API = "https://commons.wikimedia.org/w/api.php"


def commons_search(q, n=20):
    j = http_json(API, {"action": "query", "list": "search", "srsearch": q + " filetype:bitmap", "srnamespace": 6,
                        "srlimit": n, "format": "json", "formatversion": 2, "maxlag": 5}, source="commons")
    return [x["title"] for x in ((j or {}).get("query") or {}).get("search", [])]


def commons_info(titres):
    infos = {}
    for i in range(0, len(titres), 50):
        lot = titres[i:i + 50]
        j = http_json(API, {"action": "query", "prop": "imageinfo", "titles": "|".join(lot), "iiprop": "url|extmetadata|size|mime",
                            "iiurlwidth": 960, "iiextmetadatalanguage": "en", "format": "json", "formatversion": 2, "maxlag": 5,
                            "iiextmetadatafilter": "LicenseShortName|LicenseUrl|Artist|Credit|ImageDescription|AttributionRequired|UsageTerms|Copyrighted"},
                      source="commons")
        for p in ((j or {}).get("query") or {}).get("pages", []):
            ii = (p.get("imageinfo") or [None])[0]
            if ii:
                infos[p["title"]] = ii
    return infos


AUTEURS_NORMAUX = ["Mikael Häggström", "Hellerhoff"]


def bibliotheque_normaux():
    """Titres « normal / Normalbefund » des séries d'auteurs (Häggström CC0, Hellerhoff CC BY-SA), mis en cache."""
    f = os.path.join(CACHE, "bibliotheque_normaux.json")
    if os.path.exists(f):
        return json.load(open(f, encoding="utf-8"))
    biblio, complet = {}, True
    partiel = f + ".partiel"
    if os.path.exists(partiel):
        biblio = json.load(open(partiel, encoding="utf-8"))
    for auteur in AUTEURS_NORMAUX:
        if biblio.get(auteur):
            continue
        cont, titres, pages = None, [], 0
        while pages < 60:
            p = {"action": "query", "list": "allimages", "aiuser": auteur, "aisort": "timestamp", "ailimit": 500,
                 "format": "json", "formatversion": 2, "maxlag": 5}
            if cont:
                p["aicontinue"] = cont
            j = http_json(API, p, source="commons")
            if not j:
                break
            titres += ["File:" + x["name"].replace("_", " ") for x in j.get("query", {}).get("allimages", [])]
            cont = (j.get("continue") or {}).get("aicontinue"); pages += 1
            if not cont:
                break
        if cont or not titres:
            complet = False
        biblio[auteur] = [t for t in titres if re.search(r"normal|Normalbefund|unauff|gesund|healthy", t, re.I)]
        log(f"Bibliothèque de normaux : {auteur} -> {len(titres)} fichiers, {len(biblio[auteur])} « normaux »")
    json.dump(biblio, open(f if complet else partiel, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    if complet and os.path.exists(partiel):
        os.remove(partiel)
    return biblio


def candidats_commons(ctx, biblio):
    rn, rp = ctx["roles"]["normal"], ctx["roles"]["patho"]
    mn, mp = MODALITE_INFO[rn["modalite"]], MODALITE_INFO[rp["modalite"]]
    plan = next((e for e, _ in rn["details"] if e in ("axial", "coronal", "sagittal", "frontal", "lateral")), "")
    titres = {"patho": [], "normal": []}
    for q in [f'{ctx["termes_en"][0]} {mp["en"]}', f'{ctx["terme_de"]} {mp["de"]}'] + \
             ([f'{ctx["termes_en"][1]} {mp["en"]}'] if len(ctx["termes_en"]) > 1 else []):
        titres["patho"] += commons_search(q, 15)
    for q in [f'normal {mn["en"]} {ctx["region"]} {plan}'.strip(), f'Normalbefund {mn["de"]} {ctx["region_de"]}']:
        titres["normal"] += commons_search(q, 15)
    # bibliothèque : titres d'auteurs « normal » qui citent la région ou la modalité
    rx_reg = re.compile(ctx["region_rx"] + "|" + re.escape(ctx["region_de"]), re.I)
    rx_mod = re.compile(mn["rx"] + "|" + re.escape(mn["de"]), re.I)
    lib = []
    for auteur, ts in biblio.items():
        for t in ts:
            s = (2 if rx_reg.search(t) else 0) + (1 if rx_mod.search(t) else 0) + (0.5 if plan and plan in t.lower() else 0)
            if s >= 2:
                lib.append((s, t))
    lib.sort(key=lambda x: -x[0])
    titres["normal"] += [t for _, t in lib[:12]]
    tous = list(dict.fromkeys(titres["patho"] + titres["normal"]))
    infos = commons_info(tous)
    out = {"patho": [], "normal": []}
    for role in ("patho", "normal"):
        for t in dict.fromkeys(titres[role]):
            ii = infos.get(t)
            if not ii or ii.get("mime") not in ("image/jpeg", "image/png", "image/gif", "image/tiff", "image/webp"):
                continue
            em = ii.get("extmetadata", {})
            lic = sans_html((em.get("LicenseShortName") or {}).get("value", ""))
            if not lic_libre(lic) and not re.search(r"public domain|^PD", lic, re.I):
                continue
            desc = sans_html((em.get("ImageDescription") or {}).get("value", ""))
            texte = t[5:].rsplit(".", 1)[0].replace("_", " ") + ". " + desc
            s = score_legende(texte, ctx, role, exige_modalite=False)
            if not s:
                continue
            sc, motifs, pan = s
            if any(a.lower() in sans_html((em.get("Artist") or {}).get("value", "")).lower() for a in AUTEURS_NORMAUX) and role == "normal":
                sc += 1; motifs = motifs + ["série d'auteur"]
            if min(ii.get("width", 0), 10000) < 400:
                sc -= 1; motifs = motifs + ["petite image"]
            out[role].append({"source": "Commons", "titre": t, "legende": texte[:900], "score": round(sc, 2), "motifs": motifs,
                              "panneau": pan, "licence": lic, "url_image": miniature_standard(ii),
                              "url_source": ii.get("descriptionurl"), "auteur": sans_html((em.get("Artist") or {}).get("value", ""))[:300],
                              "credit": sans_html((em.get("Credit") or {}).get("value", ""))[:300],
                              "taille": f'{ii.get("width")}x{ii.get("height")}'})
    return out


# ---------------------------------------------------------------- téléchargement
def miniature_standard(ii):
    """Les originaux Commons sont souvent bloqués (429) : miniature de largeur standard 960/500/330/250 px."""
    w = max([x for x in (960, 500, 330, 250) if x < ii.get("width", 0)] or [250])
    o = ii["url"].split("?")[0]
    base, fn = o.rsplit("/", 1)
    return base.replace("/commons/", "/commons/thumb/") + "/" + fn + "/" + str(w) + "px-" + fn + \
        (".jpg" if fn.lower().endswith((".tif", ".tiff")) else "")


def telecharger(c, dossier, nom):
    from PIL import Image
    st, data = http_get(c["url_image"], source="upload" if "wikimedia" in c["url_image"] else "s3", binaire=True)
    if st != 200 or not data:
        return False
    try:
        im = Image.open(io.BytesIO(data))
        im.load()
        if im.width < 150 or im.height < 150:
            return False
        if im.mode not in ("RGB", "L"):
            im = im.convert("RGB")
        if im.width > LARGEUR_MAX:
            im = im.resize((LARGEUR_MAX, round(im.height * LARGEUR_MAX / im.width)), Image.LANCZOS)
        chemin = os.path.join(dossier, nom + ".jpg")
        im.save(chemin, "JPEG", quality=85)
        c["fichier_local"] = os.path.relpath(chemin, ICI)
        c["dimensions"] = f"{im.width}x{im.height}"
        return True
    except Exception as e:  # image corrompue ou format exotique
        log(f"  ! image illisible {c['url_image']} ({e.__class__.__name__})")
        return False


def selectionner(liste, dossier, role):
    """Trie, déduplique, limite à 3 par article, résout les URL PMC et télécharge jusqu'à MAX_PAR_ROLE."""
    liste.sort(key=lambda x: -x["score"])
    vus, par_art, garde = set(), {}, []
    for c in liste:
        cle = (c.get("pmcid"), (c.get("fichier") or "")[:40], c.get("titre"), c["legende"][:80] if c["source"] == "ROCOv2" else "")
        if cle in vus:
            continue
        vus.add(cle)
        art = c.get("pmcid") or c.get("titre")
        if par_art.get(art, 0) >= 3:
            continue
        if c["source"] != "Commons" and not resoudre_pmc(c):
            continue
        if any(g.get("url_image") == c["url_image"] for g in garde):
            continue
        if not telecharger(c, dossier, f"{role}_{len(garde) + 1}"):
            continue
        par_art[art] = par_art.get(art, 0) + 1
        garde.append(c)
        if len(garde) >= MAX_PAR_ROLE:
            break
    for c in garde:
        c.pop("fichier", None) if c["source"] == "Commons" else None
    return garde


def traiter(item, enr, diag, recs, biblio, force=False, complement=False, sans_commons=False):
    iid = item["id"]
    dossier = os.path.join(CANDIDATS, iid)
    sortie = os.path.join(dossier, "candidats.json")
    if os.path.exists(sortie) and not force:
        anc = json.load(open(sortie, encoding="utf-8"))
        if not (complement and anc.get("commons_a_completer")):
            return anc
    os.makedirs(dossier, exist_ok=True)
    ctx = contexte(item, enr, diag)
    fpool = os.path.join(dossier, "pool_pmc.json")
    if os.path.exists(fpool):
        pool = json.load(open(fpool, encoding="utf-8"))
    else:
        pool = {"patho": [], "normal": []}
        for role in ("patho", "normal"):
            pool[role] += chercher_index(recs, ctx, role)
            pool[role] += chercher_epmc(ctx, role)
        json.dump(pool, open(fpool, "w", encoding="utf-8"), ensure_ascii=False)
    # re-score à chaque passe : les règles de filtrage évoluent, le pool brut reste en cache
    pool2 = {}
    for role, liste in pool.items():
        pool2[role] = []
        for c in liste:
            idx = c["source"] in ("MultiCaRe", "ROCOv2")
            s = score_legende(c["legende"], ctx, role, exige_modalite=not idx,
                              panneau_connu=c.get("panneau") if c["source"] == "MultiCaRe" else None)
            if not s:
                continue
            c = dict(c, score=s[0], motifs=s[1], panneau=s[2])
            if idx and "modalité" not in s[1]:
                c["score"] += 2; c["motifs"] = s[1] + ["modalité (index)"]
            pool2[role].append(c)
    pool = pool2
    if sans_commons:
        commons_incomplet = True
    else:
        e0 = ETAT_COMMONS["echecs"]
        com = candidats_commons(ctx, biblio)
        commons_incomplet = ETAT_COMMONS["echecs"] > e0
        for role in ("patho", "normal"):
            pool[role] += com[role]
    for vieux in glob.glob(os.path.join(dossier, "*.jpg")):
        os.remove(vieux)
    res = {"id": iid, "diagnostic": item["diagnostic"], "gold": ctx["gold"], "date": f"{datetime.now():%Y-%m-%d %H:%M}",
           "commons_a_completer": commons_incomplet,
           "requete": {"termes_en": ctx["termes_en"], "terme_de": ctx["terme_de"], "region": ctx["region"]}}
    for role in ("normal", "patho"):
        r = ctx["roles"][role]
        res[role] = {"a_chercher": r["desc"], "modalite": r["modalite"], "details": [e for e, _ in r["details"]],
                     "nb_bruts": len(pool[role]), "candidats": selectionner(pool[role], dossier, role)}
    tmp = sortie + ".tmp"
    json.dump(res, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    os.replace(tmp, sortie)
    log(f"{iid} {item['diagnostic'][:45]} : normal {len(res['normal']['candidats'])}/{res['normal']['nb_bruts']}, "
        f"patho {len(res['patho']['candidats'])}/{res['patho']['nb_bruts']}")
    return res


def charger_donnees():
    rec = json.load(open(os.path.join(RECENS, "recensement.json"), encoding="utf-8"))
    enr = {}
    for f in glob.glob(os.path.join(RECENS, "enrichi", "*.json")):
        try:
            enr.update(json.load(open(f, encoding="utf-8")))
        except ValueError:
            log(f"  ! {f} illisible (en cours d'écriture ?)")
    return rec["imagerie"], enr


def stats(de, a):
    items, _ = charger_donnees()
    ids = [x["id"] for x in items if de <= x["id"] <= a]
    faits = [json.load(open(p, encoding="utf-8")) for i in ids for p in [os.path.join(CANDIDATS, i, "candidats.json")] if os.path.exists(p)]
    n = len(faits)
    if not n:
        print("Aucun diagnostic traité."); return
    p1 = sum(1 for r in faits if r["patho"]["candidats"])
    n1 = sum(1 for r in faits if r["normal"]["candidats"])
    deux = sum(1 for r in faits if r["patho"]["candidats"] and r["normal"]["candidats"])
    tp = sum(len(r["patho"]["candidats"]) for r in faits); tn = sum(len(r["normal"]["candidats"]) for r in faits)
    src = {}
    for r in faits:
        for role in ("normal", "patho"):
            for c in r[role]["candidats"]:
                src[c["source"]] = src.get(c["source"], 0) + 1
    print(f"Traités : {n}/{len(ids)} ({100*n/len(ids):.0f} %)")
    print(f"≥1 patho : {p1} ({100*p1/n:.0f} %) ; ≥1 normal : {n1} ({100*n1/n:.0f} %) ; les deux : {deux} ({100*deux/n:.0f} %)")
    print(f"Candidats : patho {tp} (moy. {tp/n:.1f}), normal {tn} (moy. {tn/n:.1f}) ; par source : {src}")
    vides = [r["id"] for r in faits if not r["patho"]["candidats"]]
    print(f"Commons reporté (à compléter) : {sum(1 for r in faits if r.get('commons_a_completer'))}")
    print(f"Sans patho : {', '.join(vides) or '—'}")
    print(f"Sans normal : {', '.join(r['id'] for r in faits if not r['normal']['candidats']) or '—'}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--de", default="IMG-042")
    ap.add_argument("--a", default="IMG-344")
    ap.add_argument("--ids", nargs="*")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--complement", action="store_true", help="repasse les id dont la partie Commons a été reportée")
    ap.add_argument("--sans-commons", action="store_true", help="passe 1 rapide : index locaux + Europe PMC seulement")
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()
    if a.stats:
        return stats(a.de, a.a)
    if a.de < "IMG-042" and not a.ids:
        sys.exit("Refus : IMG-001 à IMG-041 appartiennent au pilote en cours.")
    os.makedirs(CANDIDATS, exist_ok=True)
    items, enr = charger_donnees()
    diag = charger_diag()
    recs = charger_index()
    biblio = {} if a.sans_commons else bibliotheque_normaux()
    cibles = [x for x in items if (x["id"] in a.ids if a.ids else a.de <= x["id"] <= a.a) and x["id"] >= "IMG-042"]
    log(f"Début : {len(cibles)} diagnostics")
    for item in cibles:
        if item["id"] not in diag:
            log(f"  ! {item['id']} absent de la table de traduction"); continue
        try:
            traiter(item, enr.get(item["id"], {}), diag[item["id"]], recs, biblio, a.force, a.complement, a.sans_commons)
        except Exception as e:
            log(f"  ! {item['id']} échec {e.__class__.__name__}: {e}")
    log("Fin.")


if __name__ == "__main__":
    main()
