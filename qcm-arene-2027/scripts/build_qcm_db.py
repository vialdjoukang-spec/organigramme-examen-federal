#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur massif de la base de données QCM · Arène Examen Fédéral Suisse 2027.
Objectif : ≥ 400 QCMs distincts et structurés par SSP × 248 SSP = 100'000+ QCMs.
Architecture modulaire :
  - data/catalog.js (catalogue léger des 248 SSP + proportions + statistiques)
  - data/ssp/<CODE>.js (248 fichiers autonomes compatibles file:// et HTTP)

Proportions strictement positives :
  a ≈ 0.55 (Type A : 1 meilleure réponse sur 5)
  k' ≈ 0.30 (Type K' : 4 propositions Vrai/Faux indépendantes)
  m ≈ 0.15 (Menu Long M : vignette + sélection dans liste étendue)

Usage : python3 qcm-arene-2027/scripts/build_qcm_db.py
"""

import glob
import hashlib
import html as html_lib
import json
import os
import random
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(ROOT, "qcm-arene-2027", "data")
SSP_DIR = os.path.join(OUT_DIR, "ssp")
sys.path.insert(0, os.path.dirname(__file__))
from expert_questions import EXPERT_QUESTIONS


def strip_html(text: str) -> str:
    if not text:
        return ""
    # Unescape HTML twice in case of double-escaped entities like &lt;p&gt;
    text = html_lib.unescape(html_lib.unescape(text))
    text = text.replace("<br>", " · ").replace("<br/>", " · ").replace("<br />", " · ")
    text = text.replace("</li>", " · ").replace("</p>", " · ")
    text = re.sub(r"<[^>]+>", " ", text)
    # Remove internal app_v2 markers like §constantes, ¶M, @r:...
    text = re.sub(r"§[a-zA-Z0-9_]+", " ", text)
    text = re.sub(r"¶[a-zA-Z0-9_]+", " ", text)
    text = re.sub(r"@r:[^\s\n]+", " ", text)
    # Remove stray single-letter bullets like "• p • > • b"
    text = re.sub(r"(?:^|\s)[•·]\s*[a-zA-Z<>]{1,2}(?=\s*[•·]|$)", " ", text)
    text = re.sub(r"[<>]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^([·•\-\s]+)", "", text).strip()
    text = re.sub(r"(\s*[·•]+\s*)+$", "", text).strip()
    text = re.sub(r"(?:\s*·\s*){2,}", " · ", text)
    return text


def truncate(text: str, max_len: int = 210) -> str:
    text = strip_html(text)
    if len(text) <= max_len:
        return text
    cut = text[: max_len - 1].rsplit(" ", 1)[0]
    return cut.rstrip(".,;:") + "…"


def is_clean_fact(text: str, min_len: int = 22) -> bool:
    t = strip_html(text)
    if len(t) < min_len:
        return False
    # Reject items that are mostly "À vérifier" placeholders
    if "à vérifier" in t.lower() and len(t) < 75:
        return False
    if t.lower().startswith("à vérifier"):
        return False
    # Reject if too few alphabetic words
    words = re.findall(r"[A-Za-zÀ-ÿ]{3,}", t)
    return len(words) >= 3


def split_sentences(text: str, min_len: int = 24) -> list:
    cleaned = strip_html(text)
    # Split on sentence boundaries or bullets
    parts = re.split(r"(?<=[.!?])\s+|\s*[•·]\s*", cleaned)
    res = []
    for p in parts:
        p = p.strip(" .·•-:")
        if is_clean_fact(p, min_len=min_len):
            res.append(p)
    return res


def parse_dd_sections(raw_d: str) -> dict:
    is_red_flag = "À ne pas manquer" in raw_d
    norm = raw_d.replace("<br>", "\n").replace("<br/>", "\n")
    lines = [strip_html(ln) for ln in norm.split("\n") if strip_html(ln)]
    summary_parts = []
    fields = {}
    unlabelled = []
    for ln in lines:
        if "À ne pas manquer" in ln:
            continue
        ln_clean = ln.lstrip("•·- ").strip()
        if not ln_clean or len(ln_clean) < 8:
            continue
        m = re.match(r"^([^:]{2,48})\s*:\s*(.+)$", ln_clean)
        if m:
            k = m.group(1).strip().lower()
            v = m.group(2).strip()
            fields[k] = (fields[k] + " ; " + v) if k in fields else v
        else:
            unlabelled.append(ln_clean)

    def pick_field(keys):
        for k in keys:
            for fk, fv in fields.items():
                if k == fk or k in fk:
                    if is_clean_fact(fv, 10):
                        return fv
        return ""

    clinique = pick_field(["clinique", "sémiologie", "signe distinctif", "signe déterminant", "quand y penser", "indice d'orientation", "présentation", "symptômes"])
    confirme = pick_field(["ce qui confirme", "examen déterminant", "diagnostic", "critères", "biologie", "imagerie", "examens", "bilan"])
    biologie = pick_field(["biologie", "laboratoire"])
    imagerie = pick_field(["imagerie", "échographie", "radiologie"])
    examens = pick_field(["examens", "bilan", "examen déterminant"])
    pec = pick_field(["prise en charge", "traitement", "conduite", "urgence"])
    piege = pick_field(["piège", "attention"])
    terrain = pick_field(["terrain", "épidémiologie", "risque", "agents", "classes", "contexte"])
    summary = pick_field(["ce que c'est", "mécanisme", "définition"])

    for ul in unlabelled:
        low = ul.lower()
        if not summary:
            summary = ul
        elif any(w in low for w in ("traitement", "prise en charge", "antibiothér", "chirurg", "perfusion")) and not pec:
            pec = ul
        elif any(w in low for w in ("diagnostic", "biopsie", "irm", "tdm", "hémoculture", "échocard", "critère", "confirme")) and not confirme:
            confirme = ul
        elif any(w in low for w in ("incidence", "prévalence", "terrain", "pic", "facteur", "risque")) and not terrain:
            terrain = ul
        elif not clinique:
            clinique = ul
        else:
            summary_parts.append(ul)

    if not summary and summary_parts:
        summary = summary_parts[0]
    if not summary:
        summary = clinique or confirme or pec or terrain
    if not confirme:
        confirme = examens or biologie or imagerie

    return {
        "red_flag": is_red_flag,
        "summary": summary or "",
        "fields": fields,
        "clinique": clinique or "",
        "confirme": confirme or "",
        "biologie": biologie or "",
        "imagerie": imagerie or "",
        "examens": examens or "",
        "pec": pec or "",
        "piege": piege or "",
        "terrain": terrain or "",
    }


SECTION_LABELS = [
    "Définition & Sémantique",
    "Épidémiologie & Retentissement",
    "Physiopathologie & Bases",
    "Démarche diagnostique",
    "Anamnèse & Drapeaux rouges",
    "Examen physique ciblé",
    "Tableaux cliniques",
    "Diagnostic positif & Critères",
    "Bilan paraclinique",
    "Arbre décisionnel",
    "Prise en charge thérapeutique",
    "Suivi, Pronostic & Prévention",
    "Points clés de synthèse",
    "Pièges & Questions d'examen",
]


def extract_course_facts(c_secs: list) -> list:
    """Extrait tous les faits structurés (sec_idx, sec_label, topic, fact_text) des 14 sections."""
    facts = []
    for s_idx, raw_c in enumerate(c_secs):
        if not raw_c:
            continue
        sec_label = SECTION_LABELS[s_idx] if s_idx < len(SECTION_LABELS) else f"Section {s_idx+1}"
        unescaped = html_lib.unescape(html_lib.unescape(raw_c))
        # Find <b>Header</b> blocks
        parts = re.split(r"<b>([^<]{2,80})</b>", unescaped)
        if len(parts) > 2:
            for i in range(1, len(parts) - 1, 2):
                topic = strip_html(parts[i]).rstrip(" :-")
                body = parts[i + 1]
                for sent in split_sentences(body, min_len=24):
                    if len(topic) >= 3:
                        facts.append((s_idx, sec_label, topic, sent))
        else:
            for sent in split_sentences(unescaped, min_len=24):
                facts.append((s_idx, sec_label, sec_label, sent))
    return facts


def load_all_sources():
    html = open(os.path.join(ROOT, "app_v2.html"), encoding="utf-8").read()
    m_ssp = re.search(r"const\s+SSP\s*=\s*(\[.*?\]);", html, re.S)
    ssp_list = json.loads(m_ssp.group(1))

    idx_not = html.find("const NOT=")
    decoder = json.JSONDecoder()
    not_dict, _ = decoder.raw_decode(html[html.find("{", idx_not) :])

    doses = json.load(open(os.path.join(ROOT, "data", "ck", "doses_ch.json"), encoding="utf-8"))
    glo = json.load(open(os.path.join(ROOT, "data", "ck", "glo.json"), encoding="utf-8"))
    monos = {}
    for p in sorted(glob.glob(os.path.join(ROOT, "data", "ck", "mono", "*.json"))):
        monos.update(json.load(open(p, encoding="utf-8")))

    return ssp_list, not_dict, doses, glo, monos


def collect_refs(tip: dict) -> list:
    refs = []
    for s in tip.get("v", {}).get("S", []):
        txt = truncate(f"{s.get('t','')} ({s.get('o','')}, {s.get('a','')})", 140)
        if txt and txt not in refs:
            refs.append(txt)
    if tip.get("s"):
        t = truncate(tip["s"], 140)
        if t and t not in refs:
            refs.append(t)
    if tip.get("fs"):
        t = truncate(tip["fs"], 140)
        if t and t not in refs:
            refs.append(t)
    if not refs:
        refs.append("PROFILES Suisse · Référentiel Examen fédéral de médecine humaine (2027)")
    return refs[:8]


def collect_fond(tip: dict, not_f: list) -> list:
    fond = []
    for x in tip.get("f", []):
        c = truncate(x, 250)
        if is_clean_fact(c, 25) and c not in fond:
            fond.append(c)
    if len(tip.get("c", [])) > 2:
        for s in split_sentences(tip["c"][2], 25)[:4]:
            c = truncate(s, 250)
            if c not in fond:
                fond.append(c)
    for item in not_f:
        if isinstance(item, list) and len(item) >= 2:
            c = truncate(f"{item[0]} : {item[1]}", 240)
            if c not in fond:
                fond.append(c)
    if not fond:
        fond.append("Intégration anatomo-clinique et physiopathologique centrée sur la situation de départ PROFILES.")
    return fond


def build_ssp_questions(
    code: str,
    title: str,
    cat: str,
    tip: dict,
    not_entry: list,
    doses: list,
    glo: list,
    monos: dict,
    target_total: int = 420,
) -> dict:
    seed = int(hashlib.md5(code.encode()).hexdigest()[:8], 16)
    rng = random.Random(seed)

    dd_names = not_entry[0] if not_entry and len(not_entry) > 0 else []
    not_f = not_entry[1] if not_entry and len(not_entry) > 1 else []
    raw_ds = tip.get("d", [])
    c_secs = tip.get("c", [])

    refs = collect_refs(tip)
    fond = collect_fond(tip, not_f)

    # Parse all DDs
    dds = []
    for i, raw_d in enumerate(raw_ds):
        name = dd_names[i] if i < len(dd_names) else f"Diagnostic différentiel {i+1}"
        parsed = parse_dd_sections(raw_d)
        if parsed["summary"] or parsed["clinique"] or parsed["pec"] or parsed["confirme"]:
            dds.append({"idx": i, "name": name, **parsed})

    # Extract all course facts
    course_facts = extract_course_facts(c_secs)
    # Full text of SSP for matching doses, glossary, monographs
    ssp_blob = (title + " " + " ".join(c_secs) + " " + " ".join(raw_ds)).lower()

    matched_doses = [d for d in doses if d.get("substance", "").lower() in ssp_blob and len(d.get("substance", "")) >= 4]
    matched_glo = [g for g in glo if g.get("label", "").lower() in ssp_blob and len(g.get("label", "")) >= 5 and g.get("def")]
    matched_monos = [m for m in monos.values() if m.get("n", "").lower() in ssp_blob and len(m.get("n", "")) >= 6]

    # Target counts: ~55% A, ~30% K', ~15% M -> 231 A, 126 K', 63 M
    target_a = round(target_total * 0.55)
    target_k = round(target_total * 0.30)
    target_m = target_total - target_a - target_k

    questions = []
    seen_stems = set()

    def add_q(qid, qtype, theme, stem, options, answer, justifs, fi=None, ex="", si=0):
        norm = re.sub(r"\s+", " ", stem.strip().lower())
        if norm in seen_stems:
            return False
        if not options or any(not str(o).strip() for o in options):
            return False
        if qtype in ("A", "M") and len(set(options)) < len(options):
            return False
        seen_stems.add(norm)
        if fi is None:
            fi = rng.randrange(len(fond))
        questions.append({
            "id": qid,
            "t": qtype,
            "th": truncate(theme, 70),
            "st": stem,
            "op": options,
            "an": answer,
            "ju": justifs,
            "fi": fi,
            "ex": ex,
            "si": si % len(refs) if isinstance(si, int) else si,
        })
        return True

    # 0. Prepend expert handcrafted questions if defined
    if code in EXPERT_QUESTIONS:
        for eq in EXPERT_QUESTIONS[code]:
            f_idx = len(fond)
            fond.append(eq["rappel_base"])
            s_idx = len(refs)
            refs.append(eq["source"])
            add_q(eq["id"], eq["type"], eq["theme"], eq["stem"], eq["options"], eq["answer"], eq["justification_options"], f_idx, eq["explication_specifique"], s_idx)

    letters = ["A", "B", "C", "D", "E"]
    letters_k = ["a", "b", "c", "d"]

    # Helper to pick 4 distinct distractor DDs
    def get_dist_dds(target_dd, attr=None, k=4):
        pool = [d for d in dds if d["name"] != target_dd["name"]]
        if attr:
            pool = [d for d in pool if is_clean_fact(d.get(attr, ""), 12) and d.get(attr) != target_dd.get(attr)]
        rng.shuffle(pool)
        return pool[:k]

    # =========================================================================
    # POOL BUILDERS FOR TYPE A (Target: ~231+)
    # =========================================================================
    a_seq = 1
    def next_a_id():
        nonlocal a_seq
        val = f"{code}-A{a_seq:03d}"
        a_seq += 1
        return val

    def count_type(t):
        return sum(1 for q in questions if q["t"] == t)

    # A-Strategy 1: Vignette clinique -> Diagnostic (multiple sub-angles per DD)
    if len(dds) >= 5:
        for dd in dds:
            # Angle 1a: Clinique / Summary
            clues = []
            if is_clean_fact(dd["clinique"], 20):
                clues.append(("Présentation clinique", dd["clinique"]))
            if is_clean_fact(dd["summary"], 20) and dd["summary"] != dd["clinique"]:
                clues.append(("Tableau physiopathologique et clinique", dd["summary"]))
            if is_clean_fact(dd["terrain"], 15):
                clues.append(("Terrain et facteurs favorisants", f"{dd['terrain']} ; {dd['clinique'] or dd['summary']}"))
            for angle_lbl, clue_txt in clues:
                if count_type("A") >= target_a:
                    break
                dist = get_dist_dds(dd, k=4)
                if len(dist) < 4:
                    continue
                opts_raw = [dd] + dist
                rng.shuffle(opts_raw)
                ans_idx = opts_raw.index(dd)
                rf = " [À ne pas manquer]" if dd["red_flag"] else ""
                stem = f"Situation « {title} » ({code}) — {angle_lbl} : un patient présente {truncate(clue_txt, 200)}. Quel diagnostic devez-vous suspecter en priorité ?"
                justifs = [
                    f"{letters[i]} (Exacte · {o['name']}{rf}) : Ce tableau correspond directement à {o['name']} ({truncate(o['confirme'] or o['summary'], 125)})."
                    if i == ans_idx else
                    f"{letters[i]} (Fausse · {o['name']}) : Tableau différent ({truncate(o['clinique'] or o['summary'], 105)}), n'expliquant pas les éléments clés."
                    for i, o in enumerate(opts_raw)
                ]
                ex = f"{dd['name']}{rf} : {truncate(dd['summary'], 130)}. Confirmation : {truncate(dd['confirme'] or 'évaluation clinique', 120)}."
                add_q(next_a_id(), "A", f"Diagnostic · {dd['name']}", stem, [o["name"] for o in opts_raw], ans_idx, justifs, ex=ex)

    # A-Strategy 2: DD -> Confirmation, Bilan, Imagerie, Biologie, Prise en charge, Piège
    dd_attr_prompts = [
        ("confirme", "Confirmation diagnostique", "Quel élément ou examen permet de confirmer le diagnostic de « {name} » ?"),
        ("pec", "Prise en charge", "Quelle conduite thérapeutique ou prise en charge est la plus adaptée pour « {name} » ?"),
        ("biologie", "Bilan biologique", "Quel résultat ou examen biologique caractérise « {name} » ?"),
        ("imagerie", "Imagerie ciblée", "Quel examen d'imagerie est indiqué pour « {name} » ?"),
        ("examens", "Bilan initial", "Quel bilan paraclinique initial est recommandé devant une suspicion de « {name} » ?"),
        ("piege", "Piège clinique", "Quel piège classique faut-il impérativement éviter concernant « {name} » ?"),
        ("clinique", "Sémiologie spécifique", "Quel ensemble de signes cliniques oriente typiquement vers « {name} » ?"),
    ]
    if len(dds) >= 5:
        for attr, th_lbl, q_tmpl in dd_attr_prompts:
            for dd in dds:
                if count_type("A") >= target_a:
                    break
                val = dd.get(attr, "")
                if not is_clean_fact(val, 18):
                    continue
                dist = get_dist_dds(dd, attr=attr, k=4)
                if len(dist) < 4:
                    # fallback: use other attributes from other DDs
                    other_pool = [d for d in dds if d["name"] != dd["name"] and is_clean_fact(d.get(attr) or d.get("confirme") or d.get("pec") or d.get("clinique", ""), 18)]
                    rng.shuffle(other_pool)
                    dist = other_pool[:4]
                if len(dist) < 4:
                    continue
                opts_raw = [(dd["name"], truncate(val, 130), True)]
                for d in dist:
                    dv = d.get(attr) or d.get("confirme") or d.get("pec") or d.get("clinique")
                    opts_raw.append((d["name"], truncate(dv, 130), False))
                if len(set(x[1] for x in opts_raw)) < 5:
                    continue
                rng.shuffle(opts_raw)
                ans_idx = [i for i, x in enumerate(opts_raw) if x[2]][0]
                stem = f"Dans le cadre du SSP « {title} » ({code}), " + q_tmpl.format(name=dd["name"])
                justifs = [
                    f"{letters[i]} (Exacte) : Correspond directement à « {x[0]} »."
                    if i == ans_idx else
                    f"{letters[i]} (Fausse) : Cet élément se rapporte à « {x[0]} », et non à « {dd['name']} »."
                    for i, x in enumerate(opts_raw)
                ]
                ex = f"{dd['name']} ({th_lbl}) : {truncate(val, 220)}."
                add_q(next_a_id(), "A", f"{th_lbl} · {dd['name']}", stem, [x[1] for x in opts_raw], ans_idx, justifs, ex=ex)

    # A-Strategy 3: Comparaisons différentielles croisées (DD_i vs DD_j) & Questions "SAUF UN"
    if len(dds) >= 5:
        for i in range(len(dds)):
            for j in range(i + 1, len(dds)):
                if count_type("A") >= target_a:
                    break
                d1, d2 = dds[i], dds[j]
                # Question 3a: Distinguish d1 from d2
                c1 = d1["confirme"] or d1["clinique"] or d1["pec"]
                c2 = d2["confirme"] or d2["clinique"] or d2["pec"]
                if is_clean_fact(c1, 18) and is_clean_fact(c2, 18) and c1 != c2:
                    dist_pool = [d for d in dds if d["name"] not in (d1["name"], d2["name"]) and is_clean_fact(d["confirme"] or d["clinique"], 18)]
                    if len(dist_pool) >= 3:
                        rng.shuffle(dist_pool)
                        opts_raw = [
                            (d1["name"], truncate(c1, 125), True),
                            (d2["name"], truncate(c2, 125), False),
                        ] + [(x["name"], truncate(x["confirme"] or x["clinique"], 125), False) for x in dist_pool[:3]]
                        if len(set(x[1] for x in opts_raw)) == 5:
                            rng.shuffle(opts_raw)
                            ans_idx = [k for k, x in enumerate(opts_raw) if x[2]][0]
                            stem = f"Devant « {title} » ({code}), vous hésitez entre « {d1['name']} » et « {d2['name']} ». Quel élément permet de retenir spécifiquement « {d1['name']} » ?"
                            justifs = [
                                f"{letters[k]} (Exacte) : Caractéristique discriminante en faveur de « {x[0]} »."
                                if k == ans_idx else
                                f"{letters[k]} (Fausse) : Oriente plutôt vers « {x[0]} »."
                                for k, x in enumerate(opts_raw)
                            ]
                            ex = f"Distinction {d1['name']} vs {d2['name']} : {truncate(c1, 140)} (alors que {d2['name']} présente : {truncate(c2, 100)})."
                            add_q(next_a_id(), "A", f"Différentiel · {d1['name']} vs {d2['name']}", stem, [x[1] for x in opts_raw], ans_idx, justifs, ex=ex)

                # Question 3b: Question d'exclusion ("SAUF UN")
                if count_type("A") >= target_a:
                    break
                true_attrs = []
                for ak, albl in [("clinique", "Clinique"), ("confirme", "Confirmation"), ("pec", "Prise en charge"), ("biologie", "Biologie"), ("imagerie", "Imagerie"), ("terrain", "Terrain")]:
                    if is_clean_fact(d1.get(ak, ""), 15):
                        true_attrs.append((albl, truncate(d1[ak], 120)))
                false_attr = d2.get("confirme") or d2.get("pec") or d2.get("clinique")
                if len(true_attrs) >= 4 and is_clean_fact(false_attr, 15) and false_attr not in [x[1] for x in true_attrs]:
                    rng.shuffle(true_attrs)
                    opts_raw = [(f"{lbl} : {txt}", False, lbl) for lbl, txt in true_attrs[:4]]
                    opts_raw.append((truncate(false_attr, 125), True, d2["name"]))
                    if len(set(x[0] for x in opts_raw)) == 5:
                        rng.shuffle(opts_raw)
                        ans_idx = [k for k, x in enumerate(opts_raw) if x[1]][0]
                        stem = f"À propos de « {d1['name']} » dans le SSP « {title} » ({code}), toutes les affirmations suivantes sont exactes, SAUF UNE. Laquelle est fausse ?"
                        justifs = [
                            f"{letters[k]} (Exacte · Affirmation fausse à repérer) : Cet élément appartient en réalité à « {d2['name']} »."
                            if k == ans_idx else
                            f"{letters[k]} (Rejetée · Affirmation vraie) : Élément exact pour « {d1['name']} » ({x[2]})."
                            for k, x in enumerate(opts_raw)
                        ]
                        ex = f"Dans {d1['name']}, cet intrus provient de {d2['name']} ({truncate(false_attr, 130)})."
                        add_q(next_a_id(), "A", f"Exclusion SAUF UN · {d1['name']}", stem, [x[0] for x in opts_raw], ans_idx, justifs, ex=ex)

    # A-Strategy 4: Course Sections c[0..13] + Physical exam c[5] + Fundamentals f[]
    # Group facts to build crisp Type A questions
    all_sec_pool = [(slbl, top, txt) for (_, slbl, top, txt) in course_facts]
    for fx in fond:
        if is_clean_fact(fx, 25):
            all_sec_pool.append(("Sciences fondamentales", "Physiopathologie & Bases", fx))

    # Add matched Monographs, Swiss Doses, and Glossary items into the SSP's clinical knowledge!
    for m in matched_monos[:12]:
        m_name = m.get("n", "")
        for mk, mlbl in [("def", "Définition"), ("phy", "Physiopathologie"), ("cli", "Clinique"), ("dia", "Diagnostic"), ("but", "Objectif thérapeutique"), ("mes", "Mesures"), ("pha", "Pharmacologie")]:
            val = strip_html(m.get(mk, ""))
            if is_clean_fact(val, 25):
                all_sec_pool.append((f"Monographie · {m_name}", mlbl, truncate(val, 220)))

    for d in matched_doses[:10]:
        sub = d.get("substance", "").capitalize()
        prod = d.get("produit_ch", "")
        dose_txt = f"{sub} ({prod}) : {d.get('dose','')} {d.get('voie','')} {d.get('intervalle','')} {d.get('duree','')}".strip()
        all_sec_pool.append(("Pharmacologie CH (AIPS)", f"Posologie · {sub}", truncate(dose_txt, 210)))

    for g in matched_glo[:20]:
        lbl = g.get("label", "")
        df = strip_html(g.get("def", ""))
        if is_clean_fact(df, 25):
            all_sec_pool.append(("Sémiologie & Glossaire", lbl, truncate(df, 210)))

    rng.shuffle(all_sec_pool)
    if len(all_sec_pool) >= 5:
        for idx_f, (slbl, top, txt) in enumerate(all_sec_pool):
            if count_type("A") >= target_a:
                break
            dist_candidates = [x for x in all_sec_pool if x[2] != txt and x[1] != top]
            if len(dist_candidates) < 4:
                continue
            rng.shuffle(dist_candidates)
            # Form 4a: "Dans la rubrique [slbl] · [top], quel énoncé est exact ?"
            opts_raw = [(top, truncate(txt, 130), True)] + [(x[1], truncate(x[2], 130), False) for x in dist_candidates[:4]]
            if len(set(x[1] for x in opts_raw)) == 5:
                rng.shuffle(opts_raw)
                ans_idx = [k for k, x in enumerate(opts_raw) if x[2]][0]
                stem = f"Dans le SSP « {title} » ({code}), concernant le volet « {slbl} — {top} », quelle proposition est exacte ?"
                justifs = [
                    f"{letters[k]} (Exacte) : Correspond fidèlement aux recommandations pour « {top} »."
                    if k == ans_idx else
                    f"{letters[k]} (Fausse) : Concerne un autre axe clinique (« {x[0]} ») et ne répond pas à la question posée."
                    for k, x in enumerate(opts_raw)
                ]
                ex = f"{slbl} · {top} : {truncate(txt, 230)}"
                add_q(next_a_id(), "A", f"{slbl}", stem, [x[1] for x in opts_raw], ans_idx, justifs, ex=ex)

            # Form 4b (if still need A): "Quel concept correspond à la description suivante : [txt] ?"
            if count_type("A") < target_a and len(set([top] + [x[1] for x in dist_candidates[:4]])) == 5:
                opts_raw2 = [(top, truncate(txt, 130), True)] + [(x[1], truncate(x[2], 130), False) for x in dist_candidates[:4]]
                rng.shuffle(opts_raw2)
                ans_idx2 = [k for k, x in enumerate(opts_raw2) if x[2]][0]
                stem2 = f"SSP « {title} » ({code}) : quel concept ou rubrique clinique correspond précisément à l'énoncé suivant : « {truncate(txt, 190)} » ?"
                justifs2 = [
                    f"{letters[k]} (Exacte) : Cet énoncé décrit directement « {x[0]} »."
                    if k == ans_idx2 else
                    f"{letters[k]} (Fausse) : « {x[0]} » renvoie à une autre notion ({truncate(x[1], 80)})."
                    for k, x in enumerate(opts_raw2)
                ]
                add_q(next_a_id(), "A", f"Identification · {top}", stem2, [truncate(x[0], 110) for x in opts_raw2], ans_idx2, justifs2, ex=f"{top} : {truncate(txt, 210)}")

    # A-Strategy 5: Guarantee target_a even for smaller SSPs using paired combinations
    # Combine DDs & course facts into "Combinaison diagnostique / prise en charge" questions
    if count_type("A") < target_a and len(all_sec_pool) >= 6:
        for p_idx in range(len(all_sec_pool)):
            if count_type("A") >= target_a:
                break
            slbl, top, txt = all_sec_pool[p_idx]
            dist_c = [x for x in all_sec_pool if x[2] != txt]
            if len(dist_c) < 4:
                continue
            rng.shuffle(dist_c)
            # "SAUF UN" across course facts
            opts_raw = [(truncate(x[2], 125), True, x[1]) for x in dist_c[:4]]
            # Invert one statement cleanly by pairing wrong topic
            wrong_x = dist_c[4] if len(dist_c) > 4 else dist_c[0]
            false_stmt = f"Dans « {top} », l'élément principal retenu est : {truncate(wrong_x[2], 95)}"
            opts_raw.append((false_stmt, False, top))
            if len(set(x[0] for x in opts_raw)) < 5:
                continue
            rng.shuffle(opts_raw)
            ans_idx = [k for k, x in enumerate(opts_raw) if not x[1]][0]
            stem = f"Évaluation approfondie de « {title} » ({code}) [Module {(p_idx % 8) + 1}] : parmi les 5 assertions suivantes, laquelle est INEXACTE ?"
            justifs = [
                f"{letters[k]} (Exacte · Assertion fausse) : Attribution erronée ! « {truncate(wrong_x[2], 90)} » appartient à « {wrong_x[1]} », et non à « {top} »."
                if k == ans_idx else
                f"{letters[k]} (Rejetée · Assertion exacte) : Conforme aux données cliniques sur « {x[2]} »."
                for k, x in enumerate(opts_raw)
            ]
            add_q(next_a_id(), "A", f"Contrôle de précision · {top}", stem, [x[0] for x in opts_raw], ans_idx, justifs, ex=f"Pour « {top} », la donnée réelle est : {truncate(txt, 200)}.")

    # =========================================================================
    # POOL BUILDERS FOR TYPE K' (Target: ~126)
    # =========================================================================
    k_seq = 1
    true_k_pool = []
    false_k_pool = []

    for dd in dds:
        if is_clean_fact(dd["clinique"], 18):
            true_k_pool.append((
                f"[{dd['name']}] Le tableau clinique inclut classiquement : {truncate(dd['clinique'], 115)}.",
                f"Vrai : présentation clinique typique de {dd['name']}."
            ))
        if is_clean_fact(dd["confirme"], 18):
            true_k_pool.append((
                f"[{dd['name']}] La confirmation repose notamment sur : {truncate(dd['confirme'], 115)}.",
                f"Vrai : examen/critère diagnostique retenu pour {dd['name']}."
            ))
        if is_clean_fact(dd["pec"], 18):
            true_k_pool.append((
                f"[{dd['name']}] La prise en charge comprend : {truncate(dd['pec'], 115)}.",
                f"Vrai : mesure thérapeutique adaptée à {dd['name']}."
            ))
        if dd["red_flag"]:
            true_k_pool.append((
                f"[{dd['name']}] Ce diagnostic figure parmi les urgences « à ne pas manquer » devant {title}.",
                f"Vrai : {dd['name']} engage potentiellement le pronostic vital ou fonctionnel."
            ))
        if is_clean_fact(dd["piege"], 18):
            true_k_pool.append((
                f"[{dd['name']}] Piège clinique à éviter : {truncate(dd['piege'], 115)}.",
                f"Vrai : piège documenté dans l'évaluation de {dd['name']}."
            ))

    # Cross-swap DD attributes to create realistic FALSE K' items
    if len(dds) >= 2:
        for i in range(len(dds)):
            for shift in (1, 2, 3):
                if len(dds) <= shift:
                    continue
                d1 = dds[i]
                d2 = dds[(i + shift) % len(dds)]
                if d1["name"] == d2["name"]:
                    continue
                if is_clean_fact(d2["confirme"], 18) and d2["confirme"] != d1["confirme"]:
                    false_k_pool.append((
                        f"[{d1['name']}] L'examen de confirmation spécifique est : {truncate(d2['confirme'], 110)}.",
                        f"Faux : cet examen confirme « {d2['name']} », pas « {d1['name']} »."
                    ))
                if is_clean_fact(d2["pec"], 18) and d2["pec"] != d1["pec"]:
                    false_k_pool.append((
                        f"[{d1['name']}] Le traitement spécifique de première ligne est : {truncate(d2['pec'], 110)}.",
                        f"Faux : cette conduite thérapeutique s'applique à « {d2['name']} »."
                    ))
                if is_clean_fact(d2["clinique"], 18) and d2["clinique"] != d1["clinique"]:
                    false_k_pool.append((
                        f"[{d1['name']}] La présentation clinique cardinale associe : {truncate(d2['clinique'], 110)}.",
                        f"Faux : cette sémiologie caractérise plutôt « {d2['name']} »."
                    ))

    for slbl, top, txt in all_sec_pool:
        true_k_pool.append((
            f"[{top}] {truncate(txt, 125)}.",
            f"Vrai : énoncé conforme à la rubrique « {slbl} »."
        ))

    # Create paired false statements by mismatching sec topics
    if len(all_sec_pool) >= 4:
        for i in range(len(all_sec_pool)):
            sl1, top1, txt1 = all_sec_pool[i]
            sl2, top2, txt2 = all_sec_pool[(i + 2) % len(all_sec_pool)]
            if top1 != top2 and txt1 != txt2:
                false_k_pool.append((
                    f"[{top1}] L'élément spécifique retenu est : {truncate(txt2, 115)}.",
                    f"Faux : cet énoncé concerne en réalité « {top2} » ({sl2}), et non « {top1} »."
                ))

    # Deduplicate true/false pools by text
    def dedup_pairs(pairs):
        seen = set()
        out = []
        for s, r in pairs:
            k = s.lower()
            if k not in seen:
                seen.add(k)
                out.append((s, r))
        return out

    true_k_pool = dedup_pairs(true_k_pool)
    false_k_pool = dedup_pairs(false_k_pool)
    rng.shuffle(true_k_pool)
    rng.shuffle(false_k_pool)

    # Generate target_k Type K' questions by sampling 4 distinct items each time
    # Use sliding/rotated distinct combinations so every K' stem+options is unique
    t_idx, f_idx = 0, 0
    attempts = 0
    while count_type("K") < target_k and attempts < target_k * 5:
        attempts += 1
        n_true = rng.choice([1, 2, 2, 3])
        n_false = 4 - n_true
        if len(true_k_pool) < n_true or len(false_k_pool) < n_false:
            break
        chosen = []
        for _ in range(n_true):
            chosen.append((*true_k_pool[t_idx % len(true_k_pool)], True))
            t_idx += 1
            if t_idx % len(true_k_pool) == 0:
                rng.shuffle(true_k_pool)
        for _ in range(n_false):
            chosen.append((*false_k_pool[f_idx % len(false_k_pool)], False))
            f_idx += 1
            if f_idx % len(false_k_pool) == 0:
                rng.shuffle(false_k_pool)

        # Ensure 4 unique option texts within this K' question
        if len(set(c[0] for c in chosen)) < 4:
            continue
        rng.shuffle(chosen)
        options = [c[0] for c in chosen]
        answer = [c[2] for c in chosen]
        justifs = [f"{letters_k[i]} ({'+ Vrai' if chosen[i][2] else '- Faux'}) : {chosen[i][1]}" for i in range(4)]

        # Contextualize stem with primary subject to ensure stem uniqueness and clarity
        focus_tag = options[0].split("]")[0].lstrip("[") if "]" in options[0] else title
        stem = f"À propos de « {title} » ({code} · Série K'-{k_seq:03d}, focus {truncate(focus_tag, 40)}), indiquez pour chaque proposition si elle est vraie (+) ou fausse (-)."
        if add_q(f"{code}-K{k_seq:03d}", "K", f"Type K' · {focus_tag}", stem, options, answer, justifs, ex=f"Synthèse Type K' sur {title} ({code}) : 4/4 = 1 pt, 3/4 = 0.5 pt, ≤ 2/4 = 0 pt."):
            k_seq += 1

    # =========================================================================
    # POOL BUILDERS FOR MENU LONG M (Target: ~63)
    # =========================================================================
    m_seq = 1
    if len(dds) >= 6:
        menu_names = [d["name"] for d in dds[:16]]
        m_facets = [
            ("clinique", "Présentation clinique", "Parmi la liste des diagnostics différentiels de « {title} » ({code}), lequel correspond à la présentation clinique suivante : « {clue} » ?"),
            ("confirme", "Examen de confirmation", "Dans le bilan de « {title} » ({code}), quel diagnostic est confirmé ou exploré en priorité par : « {clue} » ?"),
            ("pec", "Stratégie thérapeutique", "Dans « {title} » ({code}), à quel diagnostic précis s'applique la prise en charge suivante : « {clue} » ?"),
            ("summary", "Mécanisme & Définition", "Pour la plainte « {title} » ({code}), quel diagnostic correspond à la définition : « {clue} » ?"),
            ("piege", "Piège diagnostique", "Concernant « {title} » ({code}), quel diagnostic est directement associé à ce piège clinique : « {clue} » ?"),
            ("biologie", "Profil biologique", "Dans « {title} » ({code}), quel diagnostic présente ce profil biologique : « {clue} » ?"),
            ("imagerie", "Imagerie évocatrice", "Devant « {title} » ({code}), à quel diagnostic correspond cet examen d'imagerie : « {clue} » ?"),
        ]
        # Round 1: single clues
        for attr, flbl, tmpl in m_facets:
            for dd in dds[:16]:
                if count_type("M") >= target_m:
                    break
                clue = dd.get(attr, "")
                if not is_clean_fact(clue, 18):
                    continue
                ans_idx = menu_names.index(dd["name"])
                stem = tmpl.format(title=title, code=code, clue=truncate(clue, 210))
                justifs = [
                    f"Option exacte · {dd['name']} : Cet élément ({flbl.lower()}) correspond spécifiquement à {dd['name']}. {truncate(dd['confirme'] or dd['summary'], 120)}",
                    f"Autres options du Menu Long : Ces diagnostics appartiennent au spectre de « {title} », mais leur {flbl.lower()} diffère."
                ]
                ex = f"{dd['name']} : {truncate(dd['summary'], 130)}. Confirmation : {truncate(dd['confirme'] or 'clinique', 110)}."
                if add_q(f"{code}-M{m_seq:03d}", "M", f"Menu Long · {flbl}", stem, menu_names, ans_idx, justifs, ex=ex):
                    m_seq += 1

        # Round 2: Combined multi-clue vignettes if still need M
        for dd in dds[:16]:
            if count_type("M") >= target_m:
                break
            c1 = dd.get("clinique") or dd.get("summary")
            c2 = dd.get("confirme") or dd.get("pec")
            if is_clean_fact(c1, 15) and is_clean_fact(c2, 15) and c1 != c2:
                ans_idx = menu_names.index(dd["name"])
                stem = f"Vignette intégrée « {title} » ({code}) : un patient présente « {truncate(c1, 120)} » et son bilan/suivi montre « {truncate(c2, 110)} ». Sélectionnez le diagnostic exact dans le Menu Long."
                justifs = [
                    f"Option exacte · {dd['name']} : La combinaison du tableau et de l'élément complémentaire désigne sans ambiguïté {dd['name']}.",
                    f"Autres options du Menu Long : Elles ne réunissent pas simultanément ces deux critères."
                ]
                if add_q(f"{code}-M{m_seq:03d}", "M", f"Menu Long · Vignette intégrée", stem, menu_names, ans_idx, justifs, ex=f"{dd['name']} : {truncate(dd['summary'], 180)}"):
                    m_seq += 1

    # Fallback Menu Long from course topics (for SSPs without DD list like S8.x)
    if count_type("M") < target_m and len(all_sec_pool) >= 8:
        topics_seen = []
        for _, top, _ in all_sec_pool:
            if top not in topics_seen and len(top) >= 4:
                topics_seen.append(top)
            if len(topics_seen) >= 14:
                break
        if len(topics_seen) >= 6:
            for slbl, top, txt in all_sec_pool:
                if count_type("M") >= target_m:
                    break
                if top not in topics_seen:
                    continue
                ans_idx = topics_seen.index(top)
                stem = f"Dans le SSP « {title} » ({code}), rattachez l'énoncé clinique suivant au volet exact du Menu Long : « {truncate(txt, 200)} »."
                justifs = [
                    f"Option exacte · {top} : Cet énoncé décrit directement le volet « {top} » ({slbl}).",
                    "Autres options du Menu Long : Elles renvoient à d'autres axes cliniques de ce même SSP."
                ]
                if add_q(f"{code}-M{m_seq:03d}", "M", f"Menu Long · {top}", stem, topics_seen, ans_idx, justifs, ex=f"{slbl} · {top} : {truncate(txt, 210)}"):
                    m_seq += 1

    # Final balance pass: if any SSP still slightly below 400 (e.g., few DDs), generate clean contextual variants
    # from remaining course facts / combinations to guarantee >= 400 per SSP
    # (only from genuine cleaned facts!)
    extra_idx = 0
    while len(questions) < 405 and len(all_sec_pool) >= 5 and extra_idx < 300:
        extra_idx += 1
        cur_a = count_type("A")
        cur_k = count_type("K")
        cur_m = count_type("M")
        # Pick type needed to keep ~55/30/15 ratio
        if cur_k / max(1, len(questions)) < 0.29 and len(true_k_pool) >= 2 and len(false_k_pool) >= 2:
            n_t = rng.choice([1, 2, 3])
            n_f = 4 - n_t
            chosen = [(*x, True) for x in rng.sample(true_k_pool, min(n_t, len(true_k_pool)))] + \
                     [(*x, False) for x in rng.sample(false_k_pool, min(n_f, len(false_k_pool)))]
            if len(chosen) == 4 and len(set(c[0] for c in chosen)) == 4:
                rng.shuffle(chosen)
                stem = f"Révision ciblée Type K' ({code} · lot #{k_seq:03d}) sur « {title} » : évaluez chaque proposition (+ Vrai / - Faux)."
                justifs = [f"{letters_k[i]} ({'+ Vrai' if chosen[i][2] else '- Faux'}) : {chosen[i][1]}" for i in range(4)]
                if add_q(f"{code}-K{k_seq:03d}", "K", f"Révision Type K' · {title}", stem, [c[0] for c in chosen], [c[2] for c in chosen], justifs, ex=f"Maîtrise transversale du SSP {code}."):
                    k_seq += 1
                    continue

        if cur_m / max(1, len(questions)) < 0.14 and len(dds) >= 6:
            menu_names = [d["name"] for d in dds[:16]]
            dd = rng.choice(dds[:16])
            c_txt = dd.get("clinique") or dd.get("confirme") or dd.get("pec") or dd.get("summary")
            if is_clean_fact(c_txt, 15):
                ans_idx = menu_names.index(dd["name"])
                stem = f"Cas de synthèse Menu Long #{m_seq:03d} ({code} · {title}) : quel diagnostic correspond à « {truncate(c_txt, 190)} » ?"
                justifs = [
                    f"Option exacte · {dd['name']} : Correspondance clinique et diagnostique établie.",
                    "Autres options du Menu Long : Diagnostics différentiels distincts."
                ]
                if add_q(f"{code}-M{m_seq:03d}", "M", f"Menu Long · Synthèse", stem, menu_names, ans_idx, justifs, ex=f"{dd['name']} : {truncate(dd['summary'], 180)}"):
                    m_seq += 1
                    continue

        # Otherwise add a Type A question combining two facts or reversed perspective
        slbl, top, txt = all_sec_pool[extra_idx % len(all_sec_pool)]
        dist_c = [x for x in all_sec_pool if x[2] != txt and x[1] != top]
        if len(dist_c) >= 4:
            chosen_dist = rng.sample(dist_c, 4)
            opts_raw = [(top, truncate(txt, 125), True)] + [(x[1], truncate(x[2], 125), False) for x in chosen_dist]
            if len(set(x[1] for x in opts_raw)) == 5:
                rng.shuffle(opts_raw)
                ans_idx = [k for k, x in enumerate(opts_raw) if x[2]][0]
                stem = f"Approfondissement #{a_seq:03d} — « {title} » ({code}) : dans la section « {slbl} », quelle proposition concerne spécifiquement « {top} » ?"
                justifs = [
                    f"{letters[k]} (Exacte) : Correspond directement à « {top} »."
                    if k == ans_idx else
                    f"{letters[k]} (Fausse) : Relève de « {x[0]} »."
                    for k, x in enumerate(opts_raw)
                ]
                if add_q(next_a_id(), "A", f"{slbl} · {top}", stem, [x[1] for x in opts_raw], ans_idx, justifs, ex=f"{top} : {truncate(txt, 210)}"):
                    continue

    return {
        "code": code,
        "title": title,
        "cat": cat,
        "dd_count": len(dds),
        "fond": fond,
        "refs": refs,
        "questions": questions,
    }


def main():
    ssp_list, not_dict, doses, glo, monos = load_all_sources()
    os.makedirs(SSP_DIR, exist_ok=True)

    # Clean old monolithic files if present
    for old in ("qcm_G.js", "qcm_S.js", "qcm_F.js", "qcm_O.js"):
        op = os.path.join(OUT_DIR, old)
        if os.path.exists(op):
            os.remove(op)

    catalog = []
    counts = {"A": 0, "K": 0, "M": 0}
    total_dds = 0
    min_q = 999999
    max_q = 0

    for entry in ssp_list:
        code, title = entry[0], entry[1]
        cat = code[0]
        tip_path = os.path.join(ROOT, "data", "tip", f"{code}.json")
        tip = json.load(open(tip_path, encoding="utf-8")) if os.path.exists(tip_path) else {}
        not_entry = not_dict.get(code, [[], []])

        ssp_obj = build_ssp_questions(code, title, cat, tip, not_entry, doses, glo, monos, target_total=420)
        qs = ssp_obj["questions"]
        q_a = sum(1 for q in qs if q["t"] == "A")
        q_k = sum(1 for q in qs if q["t"] == "K")
        q_m = sum(1 for q in qs if q["t"] == "M")

        counts["A"] += q_a
        counts["K"] += q_k
        counts["M"] += q_m
        total_dds += ssp_obj["dd_count"]
        min_q = min(min_q, len(qs))
        max_q = max(max_q, len(qs))

        # Write per-SSP JS shard
        out_path = os.path.join(SSP_DIR, f"{code}.js")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("window.QCM_SSP = window.QCM_SSP || {};\n")
            f.write(f"window.QCM_SSP[{json.dumps(code)}] = ")
            json.dump(ssp_obj, f, ensure_ascii=False, separators=(",", ":"))
            f.write(";\n")

        catalog.append({
            "code": code,
            "title": title,
            "cat": cat,
            "dds": ssp_obj["dd_count"],
            "total": len(qs),
            "A": q_a,
            "K": q_k,
            "M": q_m,
        })

    total_q = counts["A"] + counts["K"] + counts["M"]
    meta = {
        "session": 2027,
        "total_ssp": len(catalog),
        "total_dds": total_dds,
        "total_questions": total_q,
        "min_per_ssp": min_q,
        "max_per_ssp": max_q,
        "proportions": {
            "a": round(counts["A"] / total_q, 4),
            "k_prime": round(counts["K"] / total_q, 4),
            "m": round(counts["M"] / total_q, 4),
            "counts": counts,
        },
        "catalog": catalog,
    }
    with open(os.path.join(OUT_DIR, "catalog.js"), "w", encoding="utf-8") as f:
        f.write("window.QCM_CATALOG = ")
        json.dump(meta, f, ensure_ascii=False, separators=(",", ":"))
        f.write(";\n")

    print(f"Generated {total_q} QCMs across {len(catalog)} SSPs ({total_dds} DDs).")
    print(f"Per SSP min/avg/max: {min_q} / {round(total_q/len(catalog),1)} / {max_q}")
    print(f"Proportions: a={meta['proportions']['a']} (A={counts['A']}), k'={meta['proportions']['k_prime']} (K'={counts['K']}), m={meta['proportions']['m']} (M={counts['M']})")


if __name__ == "__main__":
    main()
