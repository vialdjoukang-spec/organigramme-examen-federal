#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de la base de données QCM · Arène Examen Fédéral Suisse 2027.
Proportions officielles déterminées :
  a = 0.55 (Type A : choix simple, 1 meilleure réponse parmi 5)
  k' = 0.30 (Type K' : 4 propositions Vrai/Faux indépendantes)
  m = 0.15 (Menu Long M : vignette + sélection dans une liste étendue)
  a + k' + m = 1.00 (a, k', m > 0)

Usage : python3 qcm-arene-2027/scripts/build_qcm_db.py
"""

import hashlib
import html as html_lib
import json
import os
import random
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(ROOT, "qcm-arene-2027", "data")
sys.path.insert(0, os.path.dirname(__file__))
from expert_questions import EXPERT_QUESTIONS


def strip_html(text: str) -> str:
    if not text:
        return ""
    text = text.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
    text = text.replace("</li>", " · ").replace("</p>", " ")
    text = re.sub(r"<[^>]+>", "", text)
    text = html_lib.unescape(text)
    # Remove internal app_v2 markers like §constantes, ¶M, @r:...
    text = re.sub(r"§[a-zA-Z0-9_]+", "", text)
    text = re.sub(r"¶[a-zA-Z0-9_]+", "", text)
    text = re.sub(r"@r:[^\s\n]+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"(\s*·\s*)+$", "", text).strip()
    return text


def truncate(text: str, max_len: int = 220) -> str:
    text = strip_html(text)
    if len(text) <= max_len:
        return text
    cut = text[: max_len - 1].rsplit(" ", 1)[0]
    return cut.rstrip(".,;:") + "…"


def parse_dd_sections(raw_d: str) -> dict:
    """Extrait les sous-sections d'un diagnostic différentiel (Clinique, Biologie, Imagerie, Ce qui confirme, Prise en charge, Piège)."""
    is_red_flag = "À ne pas manquer" in raw_d
    lines = [strip_html(ln) for ln in raw_d.split("\n") if strip_html(ln)]
    summary = ""
    fields = {}
    for ln in lines:
        if "À ne pas manquer" in ln:
            continue
        ln_clean = ln.lstrip("•- ").strip()
        m = re.match(r"^([^:]{2,35})\s*:\s*(.+)$", ln_clean)
        if m:
            k = m.group(1).strip().lower()
            v = m.group(2).strip()
            fields[k] = v
        elif not summary:
            summary = ln_clean
    return {
        "red_flag": is_red_flag,
        "summary": summary,
        "fields": fields,
        "clinique": fields.get("clinique", ""),
        "confirme": fields.get("ce qui confirme", fields.get("biologie", fields.get("examens", ""))),
        "pec": fields.get("prise en charge", ""),
        "piege": fields.get("piège", ""),
        "biologie": fields.get("biologie", ""),
        "imagerie": fields.get("imagerie", ""),
    }


def extract_bullets(raw_c: str) -> list:
    """Extrait les paires (titre, contenu) d'une section c[i] de data/tip."""
    if not raw_c:
        return []
    # Split by <b>Title :</b> or <li>
    items = []
    # Find <b>...</b> followed by text
    parts = re.split(r"<b>([^<]{2,60})</b>", raw_c)
    if len(parts) > 2:
        for i in range(1, len(parts) - 1, 2):
            title = strip_html(parts[i]).rstrip(" :")
            body = strip_html(parts[i + 1])
            if body and len(body) > 15:
                items.append((title, body))
    if not items:
        for li in re.findall(r"<li>(.*?)</li>", raw_c, re.S):
            txt = strip_html(li)
            if len(txt) > 15:
                items.append(("Point clinique", txt))
    if not items:
        txt = strip_html(raw_c)
        if len(txt) > 15:
            items.append(("Synthèse", txt))
    return items


def format_source(tip: dict) -> str:
    v_s = tip.get("v", {}).get("S", [])
    if v_s:
        s0 = v_s[0]
        org = s0.get("o", "")
        yr = s0.get("a", "")
        t = s0.get("t", "")
        return truncate(f"{t} ({org}, {yr})", 140)
    s_str = tip.get("s", "")
    if s_str:
        return truncate(s_str, 140)
    return "PROFILES Suisse · Référentiel Examen fédéral de médecine humaine"


def extract_rappel_base(tip: dict, not_f: list, rng: random.Random) -> str:
    f_list = [strip_html(x) for x in tip.get("f", []) if len(strip_html(x)) > 25]
    if f_list:
        chosen = rng.choice(f_list)
        return truncate(chosen, 260)
    c2 = strip_html(tip.get("c", [""])[2] if len(tip.get("c", [])) > 2 else "")
    if c2:
        return truncate(c2, 260)
    if not_f:
        return f"{not_f[0][0]} : {not_f[0][1]}."
    return "Raisonnement physiopathologique et anatomo-clinique centré sur la plainte initiale."


def load_app_data():
    html = open(os.path.join(ROOT, "app_v2.html"), encoding="utf-8").read()
    m_ssp = re.search(r"const\s+SSP\s*=\s*(\[.*?\]);", html, re.S)
    ssp_list = json.loads(m_ssp.group(1))

    idx_not = html.find("const NOT=")
    # Parse JSON object starting at {
    start_brace = html.find("{", idx_not)
    decoder = json.JSONDecoder()
    not_dict, _ = decoder.raw_decode(html[start_brace:])
    return ssp_list, not_dict


def build_questions_for_ssp(code: str, title: str, cat: str, tip: dict, not_entry: list, target_n: int) -> list:
    seed = int(hashlib.md5(code.encode()).hexdigest()[:8], 16)
    rng = random.Random(seed)

    dd_names = not_entry[0] if not_entry and len(not_entry) > 0 else []
    not_f = not_entry[1] if not_entry and len(not_entry) > 1 else []
    raw_ds = tip.get("d", [])
    c_secs = tip.get("c", [])
    source_str = format_source(tip)

    # Pair DD names with parsed sections
    dds = []
    for i, raw_d in enumerate(raw_ds):
        name = dd_names[i] if i < len(dd_names) else f"Étiologie {i+1}"
        parsed = parse_dd_sections(raw_d)
        if parsed["summary"] or parsed["clinique"] or parsed["pec"]:
            dds.append({"idx": i, "name": name, **parsed})

    questions = []
    # 1. Include expert handcrafted questions first if any
    if code in EXPERT_QUESTIONS:
        questions.extend(EXPERT_QUESTIONS[code])

    # Determine how many of each type to reach target_n while respecting 55% A, 30% K', 15% M
    # For target_n = 14 -> 8 A, 4 K, 2 M (0.57, 0.29, 0.14)
    # For target_n = 20 -> 11 A, 6 K, 3 M (0.55, 0.30, 0.15)
    n_a_target = round(target_n * 0.55)
    n_k_target = round(target_n * 0.30)
    n_m_target = max(1, target_n - n_a_target - n_k_target)

    cur_a = sum(1 for q in questions if q["type"] == "A")
    cur_k = sum(1 for q in questions if q["type"] == "K")
    cur_m = sum(1 for q in questions if q["type"] == "M")

    need_a = max(0, n_a_target - cur_a)
    need_k = max(0, n_k_target - cur_k)
    need_m = max(0, n_m_target - cur_m)

    # Helper to pick 4 distinct distractor DDs
    def pick_distractors(correct_dd, k=4):
        pool = [d for d in dds if d["name"] != correct_dd["name"]]
        rng.shuffle(pool)
        return pool[:k]

    # --- GENERATE TYPE A QUESTIONS ---
    a_idx = 1
    dd_shuffled = list(dds)
    rng.shuffle(dd_shuffled)

    # Strategy A1: Diagnostic / Vignette clinique from DD
    for dd in dd_shuffled:
        if need_a <= 0:
            break
        if len(dds) < 5:
            break
        clue = dd["clinique"] or dd["summary"]
        if not clue or len(clue) < 20:
            continue
        distractors = pick_distractors(dd, 4)
        if len(distractors) < 4:
            continue

        opts_raw = [dd] + distractors
        rng.shuffle(opts_raw)
        ans_idx = opts_raw.index(dd)
        options = [o["name"] for o in opts_raw]

        rf_tag = " (diagnostic « à ne pas manquer »)" if dd["red_flag"] else ""
        stem = (
            f"Dans le cadre d'une consultation pour « {title} » ({code}), un patient présente le tableau suivant : "
            f"{truncate(clue, 210)}. Quel diagnostic devez-vous évoquer en priorité ?"
        )
        justifs = []
        letters = ["A", "B", "C", "D", "E"]
        for i, o in enumerate(opts_raw):
            if i == ans_idx:
                detail = o["confirme"] or o["summary"] or o["clinique"]
                justifs.append(f"{letters[i]} (Exacte · {o['name']}{rf_tag}) : Ce tableau correspond typiquement à cette entité ({truncate(detail, 150)}).")
            else:
                diff = o["clinique"] or o["summary"]
                justifs.append(f"{letters[i]} (Fausse · {o['name']}) : Présentation distincte ({truncate(diff, 120)}), ne rendant pas compte des éléments clés de la vignette.")

        pec_info = f" Prise en charge : {truncate(dd['pec'], 150)}" if dd["pec"] else ""
        conf_info = f" Confirmation : {truncate(dd['confirme'], 140)}." if dd["confirme"] else ""
        questions.append({
            "id": f"{code}-A{a_idx:02d}",
            "type": "A",
            "theme": f"Orientation diagnostique · {dd['name']}",
            "stem": stem,
            "options": options,
            "answer": ans_idx,
            "justification_options": justifs,
            "rappel_base": extract_rappel_base(tip, not_f, rng),
            "explication_specifique": f"{dd['name']}{rf_tag} : {truncate(dd['summary'], 140)}.{conf_info}{pec_info}",
            "source": source_str,
        })
        a_idx += 1
        need_a -= 1

    # Strategy A2: Examen de confirmation / Bilan ciblé from DD
    for dd in dd_shuffled:
        if need_a <= 0:
            break
        if len(dds) < 5 or not dd["confirme"] or len(dd["confirme"]) < 18:
            continue
        distractors = pick_distractors(dd, 4)
        valid_dist = [d for d in distractors if d["confirme"] and d["confirme"] != dd["confirme"]]
        if len(valid_dist) < 4:
            continue
        opts_raw = [dd] + valid_dist[:4]
        rng.shuffle(opts_raw)
        ans_idx = opts_raw.index(dd)
        options = [truncate(o["confirme"], 130) for o in opts_raw]
        # Ensure uniqueness of options
        if len(set(options)) < 5:
            continue
        stem = (
            f"Devant une plainte de « {title} » ({code}), vous suspectez fortement : {dd['name']}. "
            f"Quel élément ou examen permet le mieux de confirmer ce diagnostic ?"
        )
        letters = ["A", "B", "C", "D", "E"]
        justifs = []
        for i, o in enumerate(opts_raw):
            if i == ans_idx:
                justifs.append(f"{letters[i]} (Exacte) : Critère/examen de confirmation spécifique pour {o['name']}.")
            else:
                justifs.append(f"{letters[i]} (Fausse) : Cet élément oriente ou confirme plutôt « {o['name']} », pas {dd['name']}.")
        questions.append({
            "id": f"{code}-A{a_idx:02d}",
            "type": "A",
            "theme": f"Confirmation diagnostique · {dd['name']}",
            "stem": stem,
            "options": options,
            "answer": ans_idx,
            "justification_options": justifs,
            "rappel_base": extract_rappel_base(tip, not_f, rng),
            "explication_specifique": f"Pour {dd['name']} ({truncate(dd['summary'], 100)}), la confirmation repose sur : {truncate(dd['confirme'], 180)}.",
            "source": source_str,
        })
        a_idx += 1
        need_a -= 1

    # Strategy A3: Prise en charge / Conduite à tenir from DD
    for dd in dd_shuffled:
        if need_a <= 0:
            break
        if len(dds) < 5 or not dd["pec"] or len(dd["pec"]) < 18:
            continue
        distractors = pick_distractors(dd, 4)
        valid_dist = [d for d in distractors if d["pec"] and d["pec"] != dd["pec"]]
        if len(valid_dist) < 4:
            continue
        opts_raw = [dd] + valid_dist[:4]
        rng.shuffle(opts_raw)
        ans_idx = opts_raw.index(dd)
        options = [truncate(o["pec"], 130) for o in opts_raw]
        if len(set(options)) < 5:
            continue
        stem = (
            f"Un patient consultant pour « {title} » ({code}) reçoit le diagnostic de {dd['name']}. "
            f"Quelle prise en charge est la plus appropriée ?"
        )
        letters = ["A", "B", "C", "D", "E"]
        justifs = []
        for i, o in enumerate(opts_raw):
            if i == ans_idx:
                justifs.append(f"{letters[i]} (Exacte) : Conduite adaptée et conforme aux recommandations pour {o['name']}.")
            else:
                justifs.append(f"{letters[i]} (Fausse) : Prise en charge correspondant à « {o['name']} », inadaptée ici.")
        questions.append({
            "id": f"{code}-A{a_idx:02d}",
            "type": "A",
            "theme": f"Prise en charge · {dd['name']}",
            "stem": stem,
            "options": options,
            "answer": ans_idx,
            "justification_options": justifs,
            "rappel_base": extract_rappel_base(tip, not_f, rng),
            "explication_specifique": f"Dans {dd['name']}, la priorité thérapeutique est : {truncate(dd['pec'], 200)}. Toujours vérifier les posologies dans l'AIPS suisse.",
            "source": source_str,
        })
        a_idx += 1
        need_a -= 1

    # Strategy A4 (Fallback / Complementary from c_secs for S8.x or remaining need_a)
    sec_bullets = []
    for s_idx, raw_c in enumerate(c_secs):
        if s_idx == 5:  # skip raw physical exam markup if messy
            continue
        for b_title, b_body in extract_bullets(raw_c):
            if len(b_body) > 30:
                sec_bullets.append((s_idx, b_title, b_body))
    rng.shuffle(sec_bullets)

    b_cursor = 0
    while need_a > 0 and b_cursor < len(sec_bullets):
        s_idx, b_title, b_body = sec_bullets[b_cursor]
        b_cursor += 1
        # Collect 4 other distinct bullets as distractors
        other_bullets = [x for x in sec_bullets if x[1] != b_title and x[2] != b_body]
        if len(other_bullets) < 4:
            break
        rng.shuffle(other_bullets)
        chosen_dist = other_bullets[:4]
        opts_raw = [(b_title, b_body, True)] + [(x[1], x[2], False) for x in chosen_dist]
        rng.shuffle(opts_raw)
        ans_idx = [i for i, x in enumerate(opts_raw) if x[2]][0]
        options = [truncate(x[1], 135) for x in opts_raw]
        if len(set(options)) < 5:
            continue
        stem = f"Concernant « {title} » ({code}), à propos de l'aspect « {b_title} », quel énoncé est exact ?"
        letters = ["A", "B", "C", "D", "E"]
        justifs = []
        for i, x in enumerate(opts_raw):
            if i == ans_idx:
                justifs.append(f"{letters[i]} (Exacte) : Correspond fidèlement aux données cliniques pour « {b_title} ».")
            else:
                justifs.append(f"{letters[i]} (Fausse) : Concerne un autre volet (« {x[0]} ») et ne répond pas exactement à l'item demandé.")
        questions.append({
            "id": f"{code}-A{a_idx:02d}",
            "type": "A",
            "theme": f"Clinique · {b_title}",
            "stem": stem,
            "options": options,
            "answer": ans_idx,
            "justification_options": justifs,
            "rappel_base": extract_rappel_base(tip, not_f, rng),
            "explication_specifique": f"{b_title} : {truncate(b_body, 220)}",
            "source": source_str,
        })
        a_idx += 1
        need_a -= 1

    # --- GENERATE TYPE K' QUESTIONS ---
    k_idx = 1
    # Build pool of true and false clinical statements from DDs and c_secs
    true_stmts = []
    false_stmts = []

    for dd in dds:
        if dd["clinique"]:
            true_stmts.append((
                f"Dans « {dd['name']} », le tableau clinique inclut classiquement : {truncate(dd['clinique'], 125)}.",
                f"Vrai : c'est une caractéristique clinique documentée de {dd['name']}."
            ))
        if dd["confirme"]:
            true_stmts.append((
                f"La confirmation ou le bilan clé de « {dd['name']} » repose notamment sur : {truncate(dd['confirme'], 120)}.",
                f"Vrai : élément diagnostique pertinent pour {dd['name']}."
            ))
        if dd["red_flag"]:
            true_stmts.append((
                f"Parmi les étiologies de « {title} », « {dd['name']} » constitue un diagnostic à ne pas manquer en raison de sa gravité potentielle.",
                f"Vrai : {dd['name']} est classé parmi les urgences/diagnostics critiques à écarter."
            ))

    # Cross-assign attributes between distinct DDs to create plausible FALSE statements
    if len(dds) >= 2:
        for i in range(len(dds)):
            for shift in (1, 2):
                if len(dds) <= shift:
                    continue
                d1 = dds[i]
                d2 = dds[(i + shift) % len(dds)]
                if d1["name"] == d2["name"]:
                    continue
                if d2["confirme"]:
                    false_stmts.append((
                        f"L'examen ou critère de confirmation spécifique de « {d1['name']} » est : {truncate(d2['confirme'], 115)}.",
                        f"Faux : cet élément concerne en réalité « {d2['name']} », et non « {d1['name']} »."
                    ))
                if d2["pec"]:
                    false_stmts.append((
                        f"La prise en charge de première intention de « {d1['name']} » repose sur : {truncate(d2['pec'], 115)}.",
                        f"Faux : cette conduite thérapeutique s'applique à « {d2['name']} »."
                    ))
                if shift == 1 and d2["clinique"]:
                    false_stmts.append((
                        f"Le tableau clinique typique de « {d1['name']} » se caractérise classiquement par : {truncate(d2['clinique'], 115)}.",
                        f"Faux : cette présentation clinique caractérise plutôt « {d2['name']} »."
                    ))

    for _, b_title, b_body in sec_bullets:
        true_stmts.append((
            f"À propos de « {title} » ({b_title}) : {truncate(b_body, 130)}.",
            f"Vrai : conforme aux recommandations cliniques sur {b_title}."
        ))

    # Add general Swiss exam methodology false statements if needed
    generic_false = [
        ("En présence de drapeaux rouges lors d'une plainte de « " + title + " », il faut toujours attendre la confirmation biologique complète avant d'initier les mesures urgentes.",
         "Faux : les mesures urgentes (stabilisation, ECG, traitement vital) s'engagent sans attendre un examen de confirmation."),
        ("Une plainte de « " + title + " » permet à elle seule, sans anamnèse ni status ciblé, de poser un diagnostic étiologique définitif.",
         "Faux : l'anamnèse orientée, l'examen clinique et le tri des drapeaux rouges sont indispensables."),
        ("Les posologies médicamenteuses mémorisées hors contexte clinique remplacent la vérification dans l'information professionnelle suisse (AIPS).",
         "Faux : en Suisse, toute posologie et contre-indication doit être vérifiée selon l'AIPS en vigueur."),
    ]
    false_stmts.extend(generic_false)

    rng.shuffle(true_stmts)
    rng.shuffle(false_stmts)
    t_ptr, f_ptr = 0, 0

    while need_k > 0 and (len(true_stmts) - t_ptr) + (len(false_stmts) - f_ptr) >= 4:
        avail_t = len(true_stmts) - t_ptr
        avail_f = len(false_stmts) - f_ptr
        n_false = min(rng.choice([1, 2, 2, 3]), avail_f)
        n_true = min(4 - n_false, avail_t)
        if n_true + n_false < 4:
            n_false = min(4 - n_true, avail_f)
        if n_true + n_false < 4:
            break

        chosen = []
        for _ in range(n_true):
            chosen.append((true_stmts[t_ptr][0], True, true_stmts[t_ptr][1]))
            t_ptr += 1
        for _ in range(n_false):
            chosen.append((false_stmts[f_ptr][0], False, false_stmts[f_ptr][1]))
            f_ptr += 1
        if len(chosen) < 4:
            break
        rng.shuffle(chosen)

        letters_k = ["a", "b", "c", "d"]
        options = [c[0] for c in chosen]
        answer = [c[1] for c in chosen]
        justifs = [
            f"{letters_k[i]} ({'+ Vrai' if chosen[i][1] else '- Faux'}) : {chosen[i][2]}"
            for i in range(4)
        ]

        questions.append({
            "id": f"{code}-K{k_idx:02d}",
            "type": "K",
            "theme": f"Synthèse Type K' · {title}",
            "stem": f"Concernant la situation « {title} » ({code}), indiquez pour chacune des quatre propositions suivantes si elle est vraie (+) ou fausse (-).",
            "options": options,
            "answer": answer,
            "justification_options": justifs,
            "rappel_base": extract_rappel_base(tip, not_f, rng),
            "explication_specifique": f"Le format K' évalue la maîtrise fine de plusieurs aspects indépendants du SSP {code} ({title}). Rappel de notation suisse : 4/4 = 1 pt, 3/4 = 0.5 pt, ≤ 2/4 = 0 pt.",
            "source": source_str,
        })
        k_idx += 1
        need_k -= 1

    # --- GENERATE MENU LONG (M) QUESTIONS ---
    m_idx = 1
    if len(dds) >= 6:
        menu_pool = dds[:14]
        menu_names = [d["name"] for d in menu_pool]
        candidates = list(menu_pool)
        rng.shuffle(candidates)
        for dd in candidates:
            if need_m <= 0:
                break
            clue = dd["clinique"] or dd["summary"]
            if not clue or len(clue) < 18:
                continue
            ans_idx = menu_names.index(dd["name"])
            conf_txt = f" Confirmation : {truncate(dd['confirme'], 130)}." if dd["confirme"] else ""
            pec_txt = f" Prise en charge : {truncate(dd['pec'], 130)}." if dd["pec"] else ""
            justifs = [
                f"Option exacte · {dd['name']} : Le tableau clinique ({truncate(clue, 130)}) correspond spécifiquement à cette entité.{conf_txt}",
                f"Autres options du Menu Long : Elles appartiennent au diagnostic différentiel de « {title} », mais leurs signes cardinaux, leur terrain ou leur bilan de confirmation diffèrent."
            ]
            questions.append({
                "id": f"{code}-M{m_idx:02d}",
                "type": "M",
                "theme": f"Menu Long · Diagnostic précis ({code})",
                "stem": f"Parmi la liste étendue des diagnostics différentiels de « {title} » ({code}), sélectionnez celui qui correspond le mieux à cette présentation : {truncate(clue, 220)}.",
                "options": menu_names,
                "answer": ans_idx,
                "justification_options": justifs,
                "rappel_base": extract_rappel_base(tip, not_f, rng),
                "explication_specifique": f"{dd['name']} : {truncate(dd['summary'], 140)}.{conf_txt}{pec_txt}",
                "source": source_str,
            })
            m_idx += 1
            need_m -= 1
    elif len(sec_bullets) >= 8:
        # Fallback Menu Long for SSPs without DD list (e.g. S8.x)
        menu_titles = []
        seen_t = set()
        for _, bt, bb in sec_bullets:
            if bt not in seen_t:
                seen_t.add(bt)
                menu_titles.append((bt, bb))
            if len(menu_titles) >= 10:
                break
        if len(menu_titles) >= 6:
            opts = [x[0] for x in menu_titles]
            for bt, bb in menu_titles:
                if need_m <= 0:
                    break
                ans_idx = opts.index(bt)
                questions.append({
                    "id": f"{code}-M{m_idx:02d}",
                    "type": "M",
                    "theme": f"Menu Long · Domaine clinique ({code})",
                    "stem": f"Dans le SSP « {title} » ({code}), à quel volet clinique précis correspond l'énoncé suivant : « {truncate(bb, 200)} » ?",
                    "options": opts,
                    "answer": ans_idx,
                    "justification_options": [
                        f"Option exacte · {bt} : Cet énoncé décrit directement ce volet clinique.",
                        "Autres options du Menu Long : Elles renvoient à d'autres axes distincts du même SSP."
                    ],
                    "rappel_base": extract_rappel_base(tip, not_f, rng),
                    "explication_specifique": f"{bt} : {truncate(bb, 220)}",
                    "source": source_str,
                })
                m_idx += 1
                need_m -= 1

    return questions


def main():
    ssp_list, not_dict = load_app_data()
    os.makedirs(OUT_DIR, exist_ok=True)

    by_cat = {"G": {}, "S": {}, "F": {}, "O": {}}
    catalog = []
    counts = {"A": 0, "K": 0, "M": 0}

    for entry in ssp_list:
        code, title, subcat = entry[0], entry[1], entry[2]
        cat = code[0]
        tip_path = os.path.join(ROOT, "data", "tip", f"{code}.json")
        tip = json.load(open(tip_path, encoding="utf-8")) if os.path.exists(tip_path) else {}
        not_entry = not_dict.get(code, [[], []])

        # Deeper target for G (20 QCMs) and 14 QCMs for S/F/O -> ~3'500+ total QCMs!
        target_n = 20 if cat == "G" else 14
        qs = build_questions_for_ssp(code, title, cat, tip, not_entry, target_n)

        by_cat[cat][code] = {
            "code": code,
            "title": title,
            "cat": cat,
            "questions": qs,
        }
        q_a = sum(1 for q in qs if q["type"] == "A")
        q_k = sum(1 for q in qs if q["type"] == "K")
        q_m = sum(1 for q in qs if q["type"] == "M")
        counts["A"] += q_a
        counts["K"] += q_k
        counts["M"] += q_m

        catalog.append({
            "code": code,
            "title": title,
            "cat": cat,
            "total": len(qs),
            "A": q_a,
            "K": q_k,
            "M": q_m,
        })

    # Write JS data files (works in file:// AND HTTP without CORS!)
    for cat in ("G", "S", "F", "O"):
        out_path = os.path.join(OUT_DIR, f"qcm_{cat}.js")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"window.QCM_DATA = window.QCM_DATA || {{}};\n")
            f.write(f"window.QCM_DATA['{cat}'] = ")
            json.dump(by_cat[cat], f, ensure_ascii=False, separators=(",", ":"))
            f.write(";\n")

    total_q = counts["A"] + counts["K"] + counts["M"]
    meta = {
        "session": 2027,
        "total_ssp": len(catalog),
        "total_questions": total_q,
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

    print(f"Generated {total_q} QCMs across {len(catalog)} SSPs.")
    print(f"Proportions: a={meta['proportions']['a']} (A={counts['A']}), k'={meta['proportions']['k_prime']} (K'={counts['K']}), m={meta['proportions']['m']} (M={counts['M']})")


if __name__ == "__main__":
    main()
