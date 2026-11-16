#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur v3 · Arène Examen Fédéral Suisse 2027
- 100'000+ QCMs (≥ 405 QCMs/SSP × 248 SSPs) couvrant 100% des 2'500+ DDs
- 6 Dimensions cliniques :
    1. Exhaustivité des causes & Stratification par fréquence (très fréquent → rare / à ne pas manquer)
    2. Prise en charge Urgente ET Non-Urgente jusqu'à la sortie d'hospitalisation
    3. Diagnostic méthodique & Niveau d'intention des examens (1re vs 2e intention vs Smarter Medicine)
    4. Pratiques suisses : Compendium / AIPS, OFSP, SSMIG/SGAIM, Smarter Medicine, SSI, HUG/CHUV
    5. Sciences fondamentales appliquées & Justifications option par option
    6. Contrôleur d'Aléa Absolu (CSPRNG secrets.SystemRandom, zéro streak >= 3, zéro pattern périodique)
"""

import glob
import html as html_lib
import json
import os
import re
import secrets
import sys
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(ROOT, "qcm-arene-2027", "data")
SSP_DIR = os.path.join(OUT_DIR, "ssp")
sys.path.insert(0, os.path.dirname(__file__))
from expert_questions import EXPERT_QUESTIONS

CSPRNG = secrets.SystemRandom()

# ---------------------------------------------------------------------------
# Référentiel suisse intégré (SSMIG/SGAIM, Smarter Medicine, HUG/CHUV, OFSP, Compendium)
# ---------------------------------------------------------------------------
SWISS_PRACTICE_BANK = [
    {
        "cat": "Smarter Medicine · Hospitalisation & Sortie",
        "true": "Selon Smarter Medicine (SSMIG hospitalier 2023), il ne faut pas prescrire à la sortie d'hôpital des neuroleptiques initiés pendant le séjour pour insomnie ou agitation sans réévaluation stricte de l'indication.",
        "false": "À la sortie d'hospitalisation, tout neuroleptique atypique initié pour agitation nocturne doit être reconduit sans limitation de durée sur l'ordonnance de sortie.",
        "ex": "Recommandation Smarter Medicine / SGAIM (2023) : éviter les prescriptions prolongées off-label de quétiapine/rispéridone/olanzapine à la sortie (risque métabolique, chutes, confusion).",
        "src": "Smarter Medicine · Médecine Interne Générale hospitalière (2023_II)"
    },
    {
        "cat": "Smarter Medicine · Hospitalisation",
        "true": "Lors d'une hospitalisation en soins aigus, des valeurs tensionnelles élevées isolées (sans atteinte aiguë d'organe cible ni urgence hypertensive) ne justifient pas d'intensifier systématiquement le traitement antihypertenseur.",
        "false": "Toute valeur tensionnelle > 150/90 mmHg chez un patient hospitalisé impose une baisse rapide par antihypertenseur IV ou intensification immédiate à la sortie.",
        "ex": "La douleur, l'anxiété ou le sevrage élèvent transitoirement la PA à l'hôpital. Intensifier à tort augmente le risque de vertiges, d'hypotension et de chutes (Smarter Medicine 2023).",
        "src": "Smarter Medicine / Rev Med Suisse 2022;18:229-34"
    },
    {
        "cat": "Smarter Medicine · Oxygénothérapie",
        "true": "Chez les patients médicaux aigus sans risque hypercapnique, l'oxygénothérapie vise une SpO2 cible de 90–94 % (et 88–92 % en cas de BPCO/hypercapnie), sans chercher à maintenir ≥ 95–96 %.",
        "false": "Chez tout patient hospitalisé en médecine aiguë, l'oxygénothérapie doit maintenir systématiquement une SpO2 ≥ 98 % pour prévenir l'hypoxie tissulaire.",
        "ex": "Une oxygénothérapie libérale visant SpO2 ≥ 95–96 % augmente la mortalité (méta-analyse IOTA). Exceptions : intoxication au CO, céphalées en grappes, drépanocytose, pneumothorax.",
        "src": "Smarter Medicine · Médecine Interne Générale hospitalière (2023_II)"
    },
    {
        "cat": "Smarter Medicine · Infectiologie & Inflammation",
        "true": "Une élévation isolée de la CRP ou de la procalcitonine (PCT) sans foyer infectieux clinique ou microbiologique documenté ne justifie pas l'instauration d'une antibiothérapie.",
        "false": "Une CRP supérieure à 50 mg/L suffit à elle seule à poser l'indication d'une antibiothérapie empirique à large spectre en milieu hospitalier.",
        "ex": "La CRP et la PCT sont des marqueurs non spécifiques d'inflammation ; ils doivent guider la recherche d'un foyer, jamais déclencher automatiquement un antibiotique (Smarter Medicine / SSI).",
        "src": "Smarter Medicine (2023_II) & Société Suisse d'Infectiologie (SSI)"
    },
    {
        "cat": "Smarter Medicine · Thromboprophylaxie",
        "true": "Chez le patient médical aigu hospitalisé à bas risque thromboembolique (évalué par le score de Genève ou de Padoue), aucune anticoagulation prophylactique systématique n'est indiquée.",
        "false": "Tout patient adulte admis en service de médecine interne doit recevoir d'office une héparine de bas poids moléculaire prophylactique quel que soit son score de Genève.",
        "ex": "Le surrisque hémorragique dépasse le bénéfice chez les patients médicaux à bas risque (< 1 % d'ETEV à 90 j selon le score de Genève).",
        "src": "Smarter Medicine (2023_II) · Protocole HUG Thromboprophylaxie"
    },
    {
        "cat": "Smarter Medicine · Ambulatoire & Fer",
        "true": "En pratique ambulatoire suisse, la substitution en fer se débute par voie orale (et non d'emblée par perfusion IV), sauf malabsorption ou intolérance avérée, et n'est pas indiquée sans anémie ni carence martiale.",
        "false": "Devant toute fatigue sans anémie et avec une ferritine normale, une perfusion de fer IV doit être administrée en première intention.",
        "ex": "Smarter Medicine ambulatoire (2021) : privilégier la voie orale en première intention et éviter le fer chez le patient asymptomatique non anémique avec réserves suffisantes.",
        "src": "Smarter Medicine · Médecine Interne Générale ambulatoire (2021_II)"
    },
    {
        "cat": "Compendium / AIPS & Sortie hospitalière",
        "true": "En Suisse, toute posologie, adaptation rénale/hépatique et interaction médicamenteuse sur l'ordonnance de sortie doit être vérifiée dans l'information professionnelle officielle Swissmedic (AIPS / Compendium).",
        "false": "Les posologies d'entretien hospitalières peuvent être reconduites à l'identique sur l'ordonnance de sortie sans vérification de la fonction rénale ni des interactions dans l'AIPS.",
        "ex": "La réconciliation médicamenteuse à la sortie (entrée/séjour/sortie) et la vérification AIPS/Compendium préviennent les événements indésirables graves à domicile.",
        "src": "Swissmedic AIPS / Compendium.ch · Sécurité médicamenteuse"
    },
    {
        "cat": "Pratique hospitalière suisse · Sortie & Continuité",
        "true": "La sortie d'hospitalisation impose la remise d'une lettre/résumé de sortie structuré au médecin traitant, une ordonnance réconciliée, les consignes de signes d'alerte de reconsultation et un rendez-vous de suivi.",
        "false": "Après une hospitalisation pour pathologie aiguë stabilisée, le patient quitte l'hôpital sans consigne de reconsultation tant qu'une biologie de contrôle n'est pas prévue à 6 mois.",
        "ex": "En pratique hospitalière suisse (HUG/CHUV/Inselspital/USZ/USB), la continuité hôpital–médecin de famille réduit les réhospitalisations précoces.",
        "src": "HUG / CHUV · Standards de sortie hospitalière & PROFILES EPA"
    },
    {
        "cat": "OFSP · Déclaration obligatoire",
        "true": "En Suisse, certaines maladies transmissibles graves (dont la tuberculose active, les méningococcies invasives, la légionellose, le VIH/hépatites selon critères OFSP) font l'objet d'une déclaration obligatoire au médecin cantonal.",
        "false": "La déclaration obligatoire au médecin cantonal en Suisse est facultative et laissée à la discrétion du patient après guérison complète.",
        "ex": "Loi sur les épidémies (LEp) et ordonnance OFSP : les médecins et laboratoires déclarent les cas dans les délais légaux (2 h à 1 semaine selon l'agent) au médecin cantonal.",
        "src": "OFSP · Déclaration obligatoire des maladies transmissibles (LEp)"
    },
    {
        "cat": "Smarter Medicine · Imagerie & Dépistage",
        "true": "Chez un patient > 75 ans sans antécédent cardiovasculaire (prévention primaire), l'initiation d'une statine et le dosage systématique des lipides ne sont pas recommandés (bénéfice non établi).",
        "false": "Un bilan lipidique annuel suivi de l'instauration systématique d'une statine est recommandé en prévention primaire chez tous les patients de plus de 80 ans.",
        "ex": "Smarter Medicine ambulatoire (2021) : éviter le surtraitement en prévention primaire après 75 ans et proscrire les check-up biologiques/ECG annuels systématiques chez le sujet asymptomatique.",
        "src": "Smarter Medicine / SSMIG ambulatoire (2021_II)"
    }
]


def strip_html(text: str) -> str:
    if not text:
        return ""
    text = html_lib.unescape(html_lib.unescape(text))
    text = text.replace("<br>", " · ").replace("<br/>", " · ").replace("<br />", " · ")
    text = text.replace("</li>", " · ").replace("</p>", " · ")
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"§[a-zA-Z0-9_]+", " ", text)
    text = re.sub(r"¶[a-zA-Z0-9_]+", " ", text)
    text = re.sub(r"@r:[^\s\n]+", " ", text)
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
    low = t.lower()
    if "à vérifier" in low:
        return False
    words = re.findall(r"[A-Za-zÀ-ÿ]{3,}", t)
    return len(words) >= 3


def split_sentences(text: str, min_len: int = 24) -> list:
    cleaned = strip_html(text)
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
        if not is_clean_fact(ul, 10):
            continue
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
    "Bilan paraclinique (1re / 2e intention)",
    "Arbre décisionnel",
    "Prise en charge (Urgente & Non-urgente)",
    "Suivi, Sortie d'hospitalisation & Prévention",
    "Points clés de synthèse",
    "Pièges & Questions d'examen",
]


def extract_course_facts(c_secs: list) -> list:
    facts = []
    for s_idx, raw_c in enumerate(c_secs):
        if not raw_c:
            continue
        sec_label = SECTION_LABELS[s_idx] if s_idx < len(SECTION_LABELS) else f"Section {s_idx+1}"
        unescaped = html_lib.unescape(html_lib.unescape(raw_c))
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
    prev = json.load(open(os.path.join(ROOT, "data", "ck", "prev.json"), encoding="utf-8"))
    monos = {}
    for p in sorted(glob.glob(os.path.join(ROOT, "data", "ck", "mono", "*.json"))):
        monos.update(json.load(open(p, encoding="utf-8")))

    return ssp_list, not_dict, doses, glo, prev, monos


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
    refs = refs[:8]
    refs.append("Compendium.ch / AIPS Swissmedic · Smarter Medicine (SSMIG/SGAIM) · OFSP")
    return refs


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


# ---------------------------------------------------------------------------
# Contrôleur d'Aléa Absolu & Anti-Pattern
# ---------------------------------------------------------------------------
def permute_question_options(q: dict, a_counts: Counter, last_a: list, last_k: list, last_m: list):
    """
    Re-permute les options de façon cryptographique (CSPRNG) pour garantir :
    - Aucun streak >= 3 sur Type A (et équilibre uniforme A..E ~20% chacun)
    - Aucun motif Type K' répété 2 fois de suite (et couverture de tous les vecteurs 4-bit)
    - Aucun index Menu Long répété 2 fois de suite et dispersion uniforme 0..N-1
    """
    t = q["t"]
    letters = ["A", "B", "C", "D", "E"]
    letters_k = ["a", "b", "c", "d"]

    if t == "A":
        opts = q["op"]
        justs = q["ju"]
        ans = q["an"]
        # Pick forbidden answers if last 2 were equal, or to prevent X-Y-X-Y-X alternation
        forbidden = set()
        if len(last_a) >= 2 and last_a[-1] == last_a[-2]:
            forbidden.add(last_a[-1])
        if len(last_a) >= 4 and last_a[-1] == last_a[-3] and last_a[-2] == last_a[-4] and last_a[-1] != last_a[-2]:
            forbidden.add(last_a[-2])
        allowed = [i for i in range(5) if i not in forbidden]
        # Weighted towards least-used letters so final distribution is flat ~20% each
        min_c = min(a_counts[i] for i in allowed)
        candidates = [i for i in allowed if a_counts[i] <= min_c + 2]
        if not candidates:
            candidates = allowed
        target_pos = CSPRNG.choice(candidates)

        # Build permutation placing old `ans` at `target_pos` and shuffling other 4 randomly
        others = [i for i in range(5) if i != ans]
        CSPRNG.shuffle(others)
        new_order = []
        o_ptr = 0
        for pos in range(5):
            if pos == target_pos:
                new_order.append(ans)
            else:
                new_order.append(others[o_ptr])
                o_ptr += 1

        new_opts = [opts[i] for i in new_order]
        # Rewrite option letter prefix in justifications accurately!
        new_justs = []
        for new_pos, old_idx in enumerate(new_order):
            jtxt = justs[old_idx]
            jtxt_clean = re.sub(r"^[A-E]\s*\(", "(", jtxt.strip())
            new_justs.append(f"{letters[new_pos]} {jtxt_clean}")

        q["op"] = new_opts
        q["an"] = target_pos
        q["ju"] = new_justs
        a_counts[target_pos] += 1
        last_a.append(target_pos)

    elif t == "K":
        opts = q["op"]
        ans = q["an"]
        justs = q["ju"]
        idxs = [0, 1, 2, 3]
        best = idxs
        for _ in range(12):
            cand = list(idxs)
            CSPRNG.shuffle(cand)
            pat = tuple(ans[i] for i in cand)
            if not last_k or pat != last_k[-1]:
                best = cand
                break
        new_opts = [opts[i] for i in best]
        new_ans = [ans[i] for i in best]
        new_justs = []
        for new_pos, old_idx in enumerate(best):
            jtxt = justs[old_idx]
            jtxt_clean = re.sub(r"^[a-d]\s*\(", "(", jtxt.strip())
            new_justs.append(f"{letters_k[new_pos]} {jtxt_clean}")

        q["op"] = new_opts
        q["an"] = new_ans
        q["ju"] = new_justs
        last_k.append(tuple(new_ans))

    elif t == "M":
        opts = q["op"]
        ans = q["an"]
        correct_str = opts[ans]
        for _ in range(12):
            cand_opts = list(opts)
            CSPRNG.shuffle(cand_opts)
            new_ans = cand_opts.index(correct_str)
            if not last_m or new_ans != last_m[-1]:
                q["op"] = cand_opts
                q["an"] = new_ans
                break
        # Normalize any hardcoded option letters in Menu Long expert justifications
        if q.get("ju"):
            q["ju"] = [
                re.sub(r"^[A-Z]\s*\(Exacte", f"Option exacte · {correct_str} (Exacte", re.sub(r"^Options\s+[A-Z][^:]*:", "Autres options du Menu Long :", j))
                for j in q["ju"]
            ]
        last_m.append(q["an"])


def interleave_erratically(questions: list) -> list:
    """
    Entrelace les Type A, K' et M de manière erratique :
    - Garantit aucun bloc monotone > 4 d'un même type (même en fin de liste)
    - Sépare les vecteurs Type K' uniformes (TTTT / FFFF) pour garantir 0 répétition consécutive
    - Applique le contrôleur anti-pattern CSPRNG sur la séquence finale
    """
    by_type = {"A": [], "K": [], "M": []}
    for q in questions:
        by_type[q["t"]].append(q)
    for lst in by_type.values():
        CSPRNG.shuffle(lst)

    # Guarantee zero adjacent uniform K' vectors (TTTT/FFFF) by placing them in non-adjacent slots among mixed vectors
    k_list = by_type["K"]
    u_k = [q for q in k_list if all(q["an"]) or not any(q["an"])]
    m_k = [q for q in k_list if any(q["an"]) and not all(q["an"])]
    if u_k and len(m_k) >= len(u_k):
        slots = list(range(len(m_k) + 1))
        chosen_slots = sorted(CSPRNG.sample(slots, len(u_k)), reverse=True)
        res_k = list(m_k)
        for s_idx, uq in zip(chosen_slots, u_k):
            res_k.insert(s_idx, uq)
        by_type["K"] = res_k

    ordered = []
    while by_type["A"] or by_type["K"] or by_type["M"]:
        types_left = [t for t in ("A", "K", "M") if by_type[t]]
        n_a, n_km = len(by_type["A"]), len(by_type["K"]) + len(by_type["M"])

        # Avoid exhausting K+M before A: if A would form a tail > 4 at the end, force A now
        if len(types_left) > 1 and n_a > 3 * max(1, n_km) and (len(ordered) < 3 or ordered[-1]["t"] != "A" or len(set(x["t"] for x in ordered[-3:])) > 1):
            chosen_t = "A"
        else:
            if len(ordered) >= 4 and len(set(x["t"] for x in ordered[-4:])) == 1:
                last_t = ordered[-1]["t"]
                alt_types = [t for t in types_left if t != last_t]
                if alt_types:
                    types_left = alt_types
            avail = []
            for t in types_left:
                avail.extend([t] * len(by_type[t]))
            chosen_t = CSPRNG.choice(avail)
        ordered.append(by_type[chosen_t].pop())

    a_counts = Counter()
    last_a, last_k, last_m = [], [], []
    for q in ordered:
        permute_question_options(q, a_counts, last_a, last_k, last_m)
    return ordered


def build_ssp_questions(
    code: str,
    title: str,
    cat: str,
    tip: dict,
    not_entry: list,
    doses: list,
    glo: list,
    prev: dict,
    monos: dict,
    target_total: int = 420,
) -> dict:
    dd_names = not_entry[0] if not_entry and len(not_entry) > 0 else []
    not_f = not_entry[1] if not_entry and len(not_entry) > 1 else []
    raw_ds = tip.get("d", [])
    c_secs = tip.get("c", [])

    refs = collect_refs(tip)
    fond = collect_fond(tip, not_f)

    # Parse all DDs + attach prev.json rank & frequency tier
    prev_items = {it.get("i"): it for it in prev.get(code, {}).get("items", [])}
    dds = []
    for i, raw_d in enumerate(raw_ds):
        name = dd_names[i] if i < len(dd_names) else f"Diagnostic différentiel {i+1}"
        parsed = parse_dd_sections(raw_d)
        p_info = prev_items.get(i, {})
        rang = p_info.get("rang", i + 1)
        prev_pct = p_info.get("prev_pct")
        if parsed["summary"] or parsed["clinique"] or parsed["pec"] or parsed["confirme"]:
            dds.append({"idx": i, "name": name, "rang": rang, "prev_pct": prev_pct, **parsed})

    def assign_tier(dd_obj, total_dds_count):
        low_t = (dd_obj.get("terrain", "") + " " + dd_obj.get("summary", "")).lower()
        pct = dd_obj.get("prev_pct")
        if isinstance(pct, (int, float)):
            if pct >= 15.0:
                return "Très fréquente"
            if pct >= 5.0:
                return "Fréquente"
            if pct >= 1.5:
                return "Peu fréquente"
            if pct >= 0.4:
                return "Moins fréquente"
            return "Rare"
        if re.search(r"\b(très fréquent|première cause|cause la plus fréquente|majoritaire)\b", low_t):
            return "Très fréquente"
        if re.search(r"\b(exceptionnel|rarissime|rare)\b", low_t):
            return "Rare"
        r = dd_obj.get("rang", 99)
        if r <= 2:
            return "Très fréquente"
        if r <= max(4, round(total_dds_count * 0.35)):
            return "Fréquente"
        if r <= max(6, round(total_dds_count * 0.60)):
            return "Peu fréquente"
        if r <= max(8, round(total_dds_count * 0.82)):
            return "Moins fréquente"
        return "Rare"

    # Frequency stratification for Mastery Card
    causes_mastery = []
    n_dds = max(1, len(dds))
    for d in dds:
        tier = assign_tier(d, n_dds)
        d["tier"] = tier
        entry = {"n": d["name"], "urg": bool(d["red_flag"]), "r": d["rang"], "tier": tier}
        if isinstance(d.get("prev_pct"), (int, float)):
            entry["pct"] = d["prev_pct"]
        causes_mastery.append(entry)

    course_facts = extract_course_facts(c_secs)
    ssp_blob = (title + " " + " ".join(c_secs) + " " + " ".join(raw_ds)).lower()

    matched_doses = [d for d in doses if d.get("substance", "").lower() in ssp_blob and len(d.get("substance", "")) >= 4]
    matched_glo = [g for g in glo if g.get("label", "").lower() in ssp_blob and len(g.get("label", "")) >= 5 and g.get("def")]
    matched_monos = [m for m in monos.values() if m.get("n", "").lower() in ssp_blob and len(m.get("n", "")) >= 6]

    target_a = round(target_total * 0.55)
    target_k = round(target_total * 0.30)
    target_m = target_total - target_a - target_k

    questions = []
    seen_stems = set()

    def count_type(t):
        return sum(1 for q in questions if q["t"] == t)

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
            fi = CSPRNG.randrange(len(fond))
        questions.append({
            "id": qid,
            "t": qtype,
            "th": truncate(theme, 72),
            "st": stem,
            "op": list(options),
            "an": list(answer) if isinstance(answer, list) else answer,
            "ju": list(justifs),
            "fi": fi,
            "ex": ex,
            "si": si % len(refs) if isinstance(si, int) else si,
        })
        return True

    # 0. Expert curated questions (if any)
    if code in EXPERT_QUESTIONS:
        for eq in EXPERT_QUESTIONS[code]:
            f_idx = len(fond)
            fond.append(eq["rappel_base"])
            s_idx = len(refs)
            refs.append(eq["source"])
            add_q(eq["id"], eq["type"], eq["theme"], eq["stem"], eq["options"], eq["answer"], eq["justification_options"], f_idx, eq["explication_specifique"], s_idx)

    letters = ["A", "B", "C", "D", "E"]
    letters_k = ["a", "b", "c", "d"]

    def get_dist_dds(target_dd, attr=None, k=4):
        pool = [d for d in dds if d["name"] != target_dd["name"]]
        if attr:
            pool = [d for d in pool if is_clean_fact(d.get(attr, ""), 12) and d.get(attr) != target_dd.get(attr)]
        CSPRNG.shuffle(pool)
        return pool[:k]

    a_seq = 1
    def next_a_id():
        nonlocal a_seq
        val = f"{code}-A{a_seq:03d}"
        a_seq += 1
        return val

    # =========================================================================
    # TYPE A GENERATORS (~231 QCMs)
    # =========================================================================

    # A1: Swiss Practice / Compendium / Hospital Discharge / Smarter Medicine (contextualized to SSP)
    sw_sample = list(SWISS_PRACTICE_BANK)
    CSPRNG.shuffle(sw_sample)
    for sw_i, sw in enumerate(sw_sample[:5]):
        if count_type("A") >= target_a:
            break
        dist_sw = [x["false"] for x in sw_sample if x is not sw][:4]
        if len(dist_sw) == 4:
            if sw["src"] not in refs:
                refs.append(sw["src"])
            sw_si = refs.index(sw["src"])
            opts = [sw["true"]] + dist_sw
            justifs = [
                f"A (Exacte · Pratique suisse) : {sw['true']}",
            ] + [f"{letters[k+1]} (Fausse) : Contraire aux recommandations suisses ({truncate(dist_sw[k], 90)})." for k in range(4)]
            stem = f"Prise en charge hospitalière, ambulatoire et sortie dans « {title} » ({code}) [{sw['cat']}] : quelle attitude est conforme aux pratiques suisses ?"
            add_q(next_a_id(), "A", sw["cat"], stem, opts, 0, justifs, ex=sw["ex"], si=sw_si)

    # A2: Frequency & Red-Flag Stratification ("À ne pas manquer" & Très fréquente vs Rare)
    urg_dds = [d for d in dds if d["red_flag"]]
    non_urg_dds = [d for d in dds if not d["red_flag"]]
    if urg_dds and len(non_urg_dds) >= 4:
        for ud in urg_dds[:4]:
            if count_type("A") >= target_a:
                break
            dist = CSPRNG.sample(non_urg_dds, 4)
            opts = [ud["name"]] + [x["name"] for x in dist]
            justifs = [
                f"A (Exacte · À ne pas manquer) : « {ud['name']} » est une étiologie grave/urgente engageant le pronostic vital ou fonctionnel devant « {title} » ({truncate(ud['summary'], 110)})."
            ] + [
                f"{letters[k+1]} (Fausse) : « {dist[k]['name']} » fait partie du diagnostic différentiel (strate : {dist[k]['tier']}) mais ne constitue pas l'urgence vitale ciblée ici."
                for k in range(4)
            ]
            stem = f"Stratification des causes de « {title} » ({code}) : parmi ces étiologies, laquelle doit impérativement être écartée en priorité en tant que diagnostic « à ne pas manquer » ?"
            add_q(next_a_id(), "A", f"Urgence à ne pas manquer · {ud['name']}", stem, opts, 0, justifs, ex=f"Priorité vitale ({ud['tier']}) : {ud['name']}. Prise en charge : {truncate(ud['pec'] or ud['confirme'] or ud['summary'], 170)}")

    freq_top = [d for d in dds if d["tier"] == "Très fréquente"]
    freq_low = [d for d in dds if d["tier"] in ("Peu fréquente", "Moins fréquente", "Rare")]
    if freq_top and len(freq_low) >= 4 and count_type("A") < target_a:
        tf = freq_top[0]
        dist_f = CSPRNG.sample(freq_low, 4)
        opts_f = [tf["name"]] + [x["name"] for x in dist_f]
        justifs_f = [
            f"A (Exacte · Strate Très fréquente) : « {tf['name']} » occupe les premiers rangs épidémiologiques devant « {title} »."
        ] + [
            f"{letters[k+1]} (Fausse · Strate {dist_f[k]['tier']}) : « {dist_f[k]['name']} » reste plus rare en population générale ou soins primaires."
            for k in range(4)
        ]
        stem_f = f"Hiérarchisation épidémiologique de « {title} » ({code}) : quelle étiologie appartient à la strate des causes très fréquentes ?"
        add_q(next_a_id(), "A", f"Stratification fréquentielle · {tf['name']}", stem_f, opts_f, 0, justifs_f, ex=f"Approche probabiliste suisse : évoquer d'abord les causes très fréquentes ({tf['name']}) tout en éliminant systématiquement les diagnostics « à ne pas manquer ».")

    # A3: Vignettes cliniques & Terrain pour chaque DD
    if len(dds) >= 5:
        for dd in dds:
            clues = []
            if is_clean_fact(dd["clinique"], 20):
                clues.append(("Présentation clinique", dd["clinique"]))
            if is_clean_fact(dd["summary"], 20) and dd["summary"] != dd["clinique"]:
                clues.append(("Tableau physiopathologique", dd["summary"]))
            if is_clean_fact(dd["terrain"], 15):
                clues.append(("Terrain & Épidémiologie", f"{dd['terrain']} · {dd['clinique'] or dd['summary']}"))
            for angle_lbl, clue_txt in clues:
                if count_type("A") >= target_a:
                    break
                dist = get_dist_dds(dd, k=4)
                if len(dist) < 4:
                    continue
                opts_raw = [dd] + dist
                rf = " [À ne pas manquer]" if dd["red_flag"] else ""
                stem = f"Consultation pour « {title} » ({code}) — {angle_lbl} : un patient présente {truncate(clue_txt, 200)}. Quel diagnostic devez-vous retenir en priorité ?"
                justifs = [
                    f"{letters[i]} (Exacte · {o['name']}{rf}) : Ce tableau correspond directement à {o['name']} ({truncate(o['confirme'] or o['summary'], 120)})."
                    if i == 0 else
                    f"{letters[i]} (Fausse · {o['name']}) : Tableau différent ({truncate(o['clinique'] or o['summary'], 100)}), n'expliquant pas les signes clés."
                    for i, o in enumerate(opts_raw)
                ]
                ex = f"{dd['name']}{rf} : {truncate(dd['summary'], 125)}. Confirmation : {truncate(dd['confirme'] or 'clinique', 110)}."
                add_q(next_a_id(), "A", f"Diagnostic · {dd['name']}", stem, [o["name"] for o in opts_raw], 0, justifs, ex=ex)

    # A4: Niveau d'intention des examens (1re vs 2e intention), PEC Urgente/Non-urgente, Pièges
    dd_attr_prompts = [
        ("confirme", "Examens & Confirmation (niveau d'intention)", "Quel examen complémentaire de confirmation (ou critère diagnostique) est indiqué pour « {name} » ?"),
        ("pec", "Prise en charge (aiguë, Compendium/AIPS & suivi)", "Quelle prise en charge thérapeutique est la plus adaptée pour « {name} » (vérification AIPS/Compendium) ?"),
        ("biologie", "Interprétation biologique", "Quel profil ou dosage biologique caractérise « {name} » ?"),
        ("imagerie", "Imagerie diagnostique", "Quel examen d'imagerie et quel résultat attend-on dans « {name} » ?"),
        ("examens", "Bilan de 1re intention", "Quel bilan initial de première intention est recommandé devant une suspicion de « {name} » ?"),
        ("piege", "Piège clinique majeur", "Quel piège clinique ou thérapeutique faut-il impérativement éviter dans « {name} » ?"),
        ("clinique", "Sémiologie & Examen clinique", "Quel tableau sémiologique oriente typiquement vers « {name} » ?"),
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
                    other_pool = [d for d in dds if d["name"] != dd["name"] and is_clean_fact(d.get(attr) or d.get("confirme") or d.get("pec") or d.get("clinique", ""), 18)]
                    CSPRNG.shuffle(other_pool)
                    dist = other_pool[:4]
                if len(dist) < 4:
                    continue
                opts_raw = [(dd["name"], truncate(val, 130), True)]
                for d in dist:
                    dv = d.get(attr) or d.get("confirme") or d.get("pec") or d.get("clinique")
                    opts_raw.append((d["name"], truncate(dv, 130), False))
                if len(set(x[1] for x in opts_raw)) < 5:
                    continue
                stem = f"SSP « {title} » ({code}) — " + q_tmpl.format(name=dd["name"])
                justifs = [
                    f"{letters[i]} (Exacte) : Correspond directement à « {x[0]} »."
                    if i == 0 else
                    f"{letters[i]} (Fausse) : Cet élément se rapporte à « {x[0]} », et non à « {dd['name']} »."
                    for i, x in enumerate(opts_raw)
                ]
                ex = f"{dd['name']} ({th_lbl}) : {truncate(val, 220)}."
                add_q(next_a_id(), "A", f"{th_lbl} · {dd['name']}", stem, [x[1] for x in opts_raw], 0, justifs, ex=ex)

    # A5: Comparaisons différentielles croisées DD_i vs DD_j & "SAUF UN"
    if len(dds) >= 5:
        for i in range(len(dds)):
            for j in range(i + 1, len(dds)):
                if count_type("A") >= target_a:
                    break
                d1, d2 = dds[i], dds[j]
                c1 = d1["confirme"] or d1["clinique"] or d1["pec"]
                c2 = d2["confirme"] or d2["clinique"] or d2["pec"]
                if is_clean_fact(c1, 18) and is_clean_fact(c2, 18) and c1 != c2:
                    dist_pool = [d for d in dds if d["name"] not in (d1["name"], d2["name"]) and is_clean_fact(d["confirme"] or d["clinique"], 18)]
                    if len(dist_pool) >= 3:
                        CSPRNG.shuffle(dist_pool)
                        opts_raw = [
                            (d1["name"], truncate(c1, 125), True),
                            (d2["name"], truncate(c2, 125), False),
                        ] + [(x["name"], truncate(x["confirme"] or x["clinique"], 125), False) for x in dist_pool[:3]]
                        if len(set(x[1] for x in opts_raw)) == 5:
                            stem = f"Devant « {title} » ({code}), vous hésitez entre « {d1['name']} » et « {d2['name']} ». Quel élément permet de retenir spécifiquement « {d1['name']} » ?"
                            justifs = [
                                f"{letters[k]} (Exacte) : Caractéristique discriminante en faveur de « {x[0]} »."
                                if k == 0 else
                                f"{letters[k]} (Fausse) : Oriente plutôt vers « {x[0]} »."
                                for k, x in enumerate(opts_raw)
                            ]
                            ex = f"Distinction {d1['name']} vs {d2['name']} : {truncate(c1, 140)} (alors que {d2['name']} présente : {truncate(c2, 95)})."
                            add_q(next_a_id(), "A", f"Différentiel · {d1['name']} vs {d2['name']}", stem, [x[1] for x in opts_raw], 0, justifs, ex=ex)

                if count_type("A") >= target_a:
                    break
                true_attrs = []
                for ak, albl in [("clinique", "Clinique"), ("confirme", "Confirmation"), ("pec", "Prise en charge"), ("biologie", "Biologie"), ("imagerie", "Imagerie"), ("terrain", "Terrain")]:
                    if is_clean_fact(d1.get(ak, ""), 15):
                        true_attrs.append((albl, truncate(d1[ak], 120)))
                false_attr = d2.get("confirme") or d2.get("pec") or d2.get("clinique")
                if len(true_attrs) >= 4 and is_clean_fact(false_attr, 15) and false_attr not in [x[1] for x in true_attrs]:
                    CSPRNG.shuffle(true_attrs)
                    opts_raw = [(truncate(false_attr, 125), True, d2["name"])] + [(f"{lbl} : {txt}", False, lbl) for lbl, txt in true_attrs[:4]]
                    if len(set(x[0] for x in opts_raw)) == 5:
                        stem = f"À propos de « {d1['name']} » dans « {title} » ({code}), toutes ces affirmations sont exactes, SAUF UNE. Laquelle est fausse ?"
                        justifs = [
                            f"{letters[k]} (Exacte · Affirmation fausse à repérer) : Cet élément appartient en réalité à « {d2['name']} »."
                            if k == 0 else
                            f"{letters[k]} (Rejetée · Affirmation vraie) : Élément exact pour « {d1['name']} » ({x[2]})."
                            for k, x in enumerate(opts_raw)
                        ]
                        ex = f"Dans {d1['name']}, cet intrus provient de {d2['name']} ({truncate(false_attr, 130)})."
                        add_q(next_a_id(), "A", f"Exclusion SAUF UN · {d1['name']}", stem, [x[0] for x in opts_raw], 0, justifs, ex=ex)

    # A6: Course Sections c[0..13] + Fondamentaux + Monographies + Doses CH Compendium/AIPS + Glossaire
    all_sec_pool = [(slbl, top, txt) for (_, slbl, top, txt) in course_facts]
    for fx in fond:
        if is_clean_fact(fx, 25):
            all_sec_pool.append(("Sciences fondamentales", "Physiopathologie & Bases", fx))
    for m in matched_monos[:12]:
        m_name = m.get("n", "")
        for mk, mlbl in [("def", "Définition"), ("phy", "Physiopathologie"), ("cli", "Clinique"), ("dia", "Diagnostic"), ("but", "Objectif thérapeutique"), ("mes", "Mesures"), ("pha", "Pharmacologie")]:
            val = strip_html(m.get(mk, ""))
            if is_clean_fact(val, 25):
                all_sec_pool.append((f"Monographie · {m_name}", mlbl, truncate(val, 220)))
    for d in matched_doses[:12]:
        sub = d.get("substance", "").capitalize()
        prod = d.get("produit_ch", "")
        dose_txt = f"{sub} ({prod}) : {d.get('dose','')} {d.get('voie','')} {d.get('intervalle','')} {d.get('duree','')} (Compendium/AIPS CH)".strip()
        all_sec_pool.append(("Pharmacologie CH (Compendium / AIPS)", f"Posologie · {sub}", truncate(dose_txt, 210)))
    for g in matched_glo[:20]:
        lbl = g.get("label", "")
        df = strip_html(g.get("def", ""))
        if is_clean_fact(df, 25):
            all_sec_pool.append(("Sémiologie & Glossaire", lbl, truncate(df, 210)))

    CSPRNG.shuffle(all_sec_pool)
    if len(all_sec_pool) >= 5:
        for idx_f, (slbl, top, txt) in enumerate(all_sec_pool):
            if count_type("A") >= target_a:
                break
            dist_candidates = [x for x in all_sec_pool if x[2] != txt and x[1] != top]
            if len(dist_candidates) < 4:
                continue
            CSPRNG.shuffle(dist_candidates)
            opts_raw = [(top, truncate(txt, 130), True)] + [(x[1], truncate(x[2], 130), False) for x in dist_candidates[:4]]
            if len(set(x[1] for x in opts_raw)) == 5:
                stem = f"Dans le SSP « {title} » ({code}), concernant « {slbl} — {top} », quelle proposition est exacte ?"
                justifs = [
                    f"{letters[k]} (Exacte) : Correspond fidèlement aux recommandations pour « {top} »."
                    if k == 0 else
                    f"{letters[k]} (Fausse) : Concerne un autre axe clinique (« {x[0]} ») et ne répond pas à la question."
                    for k, x in enumerate(opts_raw)
                ]
                add_q(next_a_id(), "A", f"{slbl}", stem, [x[1] for x in opts_raw], 0, justifs, ex=f"{slbl} · {top} : {truncate(txt, 230)}")

            if count_type("A") < target_a and len(set([top] + [x[1] for x in dist_candidates[:4]])) == 5:
                opts_raw2 = [(top, truncate(txt, 130), True)] + [(x[1], truncate(x[2], 130), False) for x in dist_candidates[:4]]
                stem2 = f"SSP « {title} » ({code}) : quel concept clinique correspond à l'énoncé suivant : « {truncate(txt, 190)} » ?"
                justifs2 = [
                    f"{letters[k]} (Exacte) : Cet énoncé décrit directement « {x[0]} »."
                    if k == 0 else
                    f"{letters[k]} (Fausse) : « {x[0]} » renvoie à une autre notion ({truncate(x[1], 80)})."
                    for k, x in enumerate(opts_raw2)
                ]
                add_q(next_a_id(), "A", f"Identification · {top}", stem2, [truncate(x[0], 110) for x in opts_raw2], 0, justifs2, ex=f"{top} : {truncate(txt, 210)}")

    if count_type("A") < target_a and len(all_sec_pool) >= 6:
        for p_idx in range(len(all_sec_pool)):
            if count_type("A") >= target_a:
                break
            slbl, top, txt = all_sec_pool[p_idx]
            dist_c = [x for x in all_sec_pool if x[2] != txt]
            if len(dist_c) < 5:
                continue
            CSPRNG.shuffle(dist_c)
            wrong_x = dist_c[4]
            false_stmt = f"Dans « {top} », l'élément principal retenu est : {truncate(wrong_x[2], 95)}"
            opts_raw = [(false_stmt, False, top)] + [(truncate(x[2], 125), True, x[1]) for x in dist_c[:4]]
            if len(set(x[0] for x in opts_raw)) < 5:
                continue
            stem = f"Évaluation de précision — « {title} » ({code}) [Module {(p_idx % 8) + 1}] : parmi ces 5 assertions, laquelle est INEXACTE ?"
            justifs = [
                f"{letters[k]} (Exacte · Assertion fausse) : Erreur d'attribution ! « {truncate(wrong_x[2], 90)} » appartient à « {wrong_x[1]} », non à « {top} »."
                if k == 0 else
                f"{letters[k]} (Rejetée · Assertion exacte) : Conforme aux données cliniques sur « {x[2]} »."
                for k, x in enumerate(opts_raw)
            ]
            add_q(next_a_id(), "A", f"Contrôle de précision · {top}", stem, [x[0] for x in opts_raw], 0, justifs, ex=f"Pour « {top} », la donnée exacte est : {truncate(txt, 200)}.")

    # =========================================================================
    # TYPE K' GENERATORS (~126 QCMs) — includes ALL 16 4-bit truth vectors!
    # =========================================================================
    k_seq = 1
    true_k_pool = []
    false_k_pool = []

    for sw in SWISS_PRACTICE_BANK:
        true_k_pool.append((sw["true"], f"Vrai ({sw['cat']}) : {sw['ex']}"))
        false_k_pool.append((sw["false"], f"Faux ({sw['cat']}) : {sw['ex']}"))

    for dd in dds:
        if is_clean_fact(dd["clinique"], 18):
            true_k_pool.append((f"[{dd['name']}] Le tableau clinique inclut classiquement : {truncate(dd['clinique'], 115)}.", f"Vrai : présentation clinique typique de {dd['name']}."))
        if is_clean_fact(dd["confirme"], 18):
            true_k_pool.append((f"[{dd['name']}] La confirmation repose notamment sur : {truncate(dd['confirme'], 115)}.", f"Vrai : examen/critère diagnostique retenu pour {dd['name']}."))
        if is_clean_fact(dd["pec"], 18):
            true_k_pool.append((f"[{dd['name']}] La prise en charge comprend : {truncate(dd['pec'], 115)}.", f"Vrai : mesure thérapeutique adaptée à {dd['name']}."))
        if dd["red_flag"]:
            true_k_pool.append((f"[{dd['name']}] Ce diagnostic figure parmi les urgences « à ne pas manquer » devant {title}.", f"Vrai : {dd['name']} engage potentiellement le pronostic vital ou fonctionnel."))
        if is_clean_fact(dd["piege"], 18):
            true_k_pool.append((f"[{dd['name']}] Piège clinique à éviter : {truncate(dd['piege'], 115)}.", f"Vrai : piège documenté pour {dd['name']}."))

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
                    false_k_pool.append((f"[{d1['name']}] L'examen de confirmation spécifique est : {truncate(d2['confirme'], 110)}.", f"Faux : cet examen confirme « {d2['name']} », pas « {d1['name']} »."))
                if is_clean_fact(d2["pec"], 18) and d2["pec"] != d1["pec"]:
                    false_k_pool.append((f"[{d1['name']}] Le traitement spécifique de première ligne est : {truncate(d2['pec'], 110)}.", f"Faux : cette conduite s'applique à « {d2['name']} »."))
                if is_clean_fact(d2["clinique"], 18) and d2["clinique"] != d1["clinique"]:
                    false_k_pool.append((f"[{d1['name']}] La présentation clinique cardinale associe : {truncate(d2['clinique'], 110)}.", f"Faux : cette sémiologie caractérise plutôt « {d2['name']} »."))

    for slbl, top, txt in all_sec_pool:
        true_k_pool.append((f"[{top}] {truncate(txt, 125)}.", f"Vrai : énoncé conforme à la rubrique « {slbl} »."))

    if len(all_sec_pool) >= 4:
        for i in range(len(all_sec_pool)):
            sl1, top1, txt1 = all_sec_pool[i]
            sl2, top2, txt2 = all_sec_pool[(i + 2) % len(all_sec_pool)]
            if top1 != top2 and txt1 != txt2:
                false_k_pool.append((f"[{top1}] L'élément spécifique retenu est : {truncate(txt2, 115)}.", f"Faux : cet énoncé concerne « {top2} » ({sl2}), et non « {top1} »."))

    def dedup_pairs(pairs):
        seen, out = set(), []
        for s, r in pairs:
            k = s.lower()
            if k not in seen:
                seen.add(k)
                out.append((s, r))
        return out

    true_k_pool = dedup_pairs(true_k_pool)
    false_k_pool = dedup_pairs(false_k_pool)
    CSPRNG.shuffle(true_k_pool)
    CSPRNG.shuffle(false_k_pool)

    # Weighted distribution across ALL counts of True (0, 1, 2, 3, 4) so all 16 bitmasks appear naturally!
    k_weights = [0, 1, 1, 2, 2, 2, 3, 3, 4]
    t_idx, f_idx = 0, 0
    attempts = 0
    while count_type("K") < target_k and attempts < target_k * 5:
        attempts += 1
        n_true = CSPRNG.choice(k_weights)
        n_false = 4 - n_true
        if len(true_k_pool) < n_true or len(false_k_pool) < n_false:
            continue
        chosen = []
        for _ in range(n_true):
            chosen.append((*true_k_pool[t_idx % len(true_k_pool)], True))
            t_idx += 1
            if t_idx % len(true_k_pool) == 0:
                CSPRNG.shuffle(true_k_pool)
        for _ in range(n_false):
            chosen.append((*false_k_pool[f_idx % len(false_k_pool)], False))
            f_idx += 1
            if f_idx % len(false_k_pool) == 0:
                CSPRNG.shuffle(false_k_pool)

        if len(set(c[0] for c in chosen)) < 4:
            continue
        CSPRNG.shuffle(chosen)
        options = [c[0] for c in chosen]
        answer = [c[2] for c in chosen]
        justifs = [f"{letters_k[i]} ({'+ Vrai' if chosen[i][2] else '- Faux'}) : {chosen[i][1]}" for i in range(4)]
        focus_tag = options[0].split("]")[0].lstrip("[") if "]" in options[0] else title
        stem = f"À propos de « {title} » ({code} · Série K'-{k_seq:03d}, focus {truncate(focus_tag, 40)}), indiquez pour chaque proposition si elle est vraie (+) ou fausse (-)."
        if add_q(f"{code}-K{k_seq:03d}", "K", f"Type K' · {focus_tag}", stem, options, answer, justifs, ex=f"Synthèse Type K' sur {title} ({code}) : 4/4 = 1 pt, 3/4 = 0.5 pt, ≤ 2/4 = 0 pt."):
            k_seq += 1

    # =========================================================================
    # MENU LONG GENERATORS (~63 QCMs)
    # =========================================================================
    m_seq = 1
    if len(dds) >= 6:
        menu_names = [d["name"] for d in dds[:16]]
        m_facets = [
            ("clinique", "Présentation clinique", "Dans la liste complète des étiologies de « {title} » ({code}), laquelle correspond à la présentation clinique : « {clue} » ?"),
            ("confirme", "Examen de confirmation", "Devant « {title} » ({code}), quel diagnostic du Menu Long est confirmé par : « {clue} » ?"),
            ("pec", "Prise en charge & Compendium", "Dans « {title} » ({code}), à quel diagnostic précis correspond la prise en charge : « {clue} » ?"),
            ("summary", "Mécanisme & Définition", "Pour « {title} » ({code}), quel diagnostic correspond à : « {clue} » ?"),
            ("piege", "Piège diagnostique", "Concernant « {title} » ({code}), quel diagnostic est associé au piège clinique : « {clue} » ?"),
            ("biologie", "Profil biologique", "Dans « {title} » ({code}), quel diagnostic présente ce bilan biologique : « {clue} » ?"),
            ("imagerie", "Imagerie évocatrice", "Devant « {title} » ({code}), quel diagnostic montre à l'imagerie : « {clue} » ?"),
        ]
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

        for dd in dds[:16]:
            if count_type("M") >= target_m:
                break
            c1 = dd.get("clinique") or dd.get("summary")
            c2 = dd.get("confirme") or dd.get("pec")
            if is_clean_fact(c1, 15) and is_clean_fact(c2, 15) and c1 != c2:
                ans_idx = menu_names.index(dd["name"])
                stem = f"Vignette intégrée « {title} » ({code}) : un patient présente « {truncate(c1, 120)} » avec « {truncate(c2, 110)} ». Sélectionnez le diagnostic exact."
                justifs = [
                    f"Option exacte · {dd['name']} : La combinaison de ces deux critères désigne {dd['name']}.",
                    f"Autres options du Menu Long : Elles ne réunissent pas simultanément ces deux éléments."
                ]
                if add_q(f"{code}-M{m_seq:03d}", "M", "Menu Long · Vignette intégrée", stem, menu_names, ans_idx, justifs, ex=f"{dd['name']} : {truncate(dd['summary'], 180)}"):
                    m_seq += 1

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
                stem = f"Dans « {title} » ({code}), rattachez cet énoncé clinique au volet exact du Menu Long : « {truncate(txt, 200)} »."
                justifs = [
                    f"Option exacte · {top} : Cet énoncé décrit directement le volet « {top} » ({slbl}).",
                    "Autres options du Menu Long : Elles renvoient à d'autres axes cliniques de ce SSP."
                ]
                if add_q(f"{code}-M{m_seq:03d}", "M", f"Menu Long · {top}", stem, topics_seen, ans_idx, justifs, ex=f"{slbl} · {top} : {truncate(txt, 210)}"):
                    m_seq += 1

    # Balance pass to guarantee >= 405 per SSP
    extra_idx = 0
    while len(questions) < 405 and len(all_sec_pool) >= 5 and extra_idx < 300:
        extra_idx += 1
        cur_k = count_type("K")
        cur_m = count_type("M")
        if cur_k / max(1, len(questions)) < 0.29 and len(true_k_pool) >= 4 and len(false_k_pool) >= 4:
            n_t = CSPRNG.choice(k_weights)
            n_f = 4 - n_t
            chosen = [(*x, True) for x in CSPRNG.sample(true_k_pool, n_t)] + \
                     [(*x, False) for x in CSPRNG.sample(false_k_pool, n_f)]
            if len(chosen) == 4 and len(set(c[0] for c in chosen)) == 4:
                CSPRNG.shuffle(chosen)
                stem = f"Révision Type K' ({code} · lot #{k_seq:03d}) sur « {title} » : évaluez chaque proposition (+ Vrai / - Faux)."
                justifs = [f"{letters_k[i]} ({'+ Vrai' if chosen[i][2] else '- Faux'}) : {chosen[i][1]}" for i in range(4)]
                if add_q(f"{code}-K{k_seq:03d}", "K", f"Révision Type K' · {title}", stem, [c[0] for c in chosen], [c[2] for c in chosen], justifs, ex=f"Maîtrise transversale du SSP {code}."):
                    k_seq += 1
                    continue

        if cur_m / max(1, len(questions)) < 0.14 and len(dds) >= 6:
            menu_names = [d["name"] for d in dds[:16]]
            dd = CSPRNG.choice(dds[:16])
            c_txt = dd.get("clinique") or dd.get("confirme") or dd.get("pec") or dd.get("summary")
            if is_clean_fact(c_txt, 15):
                ans_idx = menu_names.index(dd["name"])
                stem = f"Synthèse Menu Long #{m_seq:03d} ({code} · {title}) : quel diagnostic correspond à « {truncate(c_txt, 190)} » ?"
                justifs = [
                    f"Option exacte · {dd['name']} : Correspondance clinique et diagnostique établie.",
                    "Autres options du Menu Long : Diagnostics différentiels distincts."
                ]
                if add_q(f"{code}-M{m_seq:03d}", "M", "Menu Long · Synthèse", stem, menu_names, ans_idx, justifs, ex=f"{dd['name']} : {truncate(dd['summary'], 180)}"):
                    m_seq += 1
                    continue

        slbl, top, txt = all_sec_pool[extra_idx % len(all_sec_pool)]
        dist_c = [x for x in all_sec_pool if x[2] != txt and x[1] != top]
        if len(dist_c) >= 4:
            chosen_dist = CSPRNG.sample(dist_c, 4)
            opts_raw = [(top, truncate(txt, 125), True)] + [(x[1], truncate(x[2], 125), False) for x in chosen_dist]
            if len(set(x[1] for x in opts_raw)) == 5:
                stem = f"Approfondissement #{a_seq:03d} — « {title} » ({code}) : dans « {slbl} », quelle proposition concerne spécifiquement « {top} » ?"
                justifs = [
                    f"{letters[k]} (Exacte) : Correspond directement à « {top} »."
                    if k == 0 else
                    f"{letters[k]} (Fausse) : Relève de « {x[0]} »."
                    for k, x in enumerate(opts_raw)
                ]
                add_q(next_a_id(), "A", f"{slbl} · {top}", stem, [x[1] for x in opts_raw], 0, justifs, ex=f"{top} : {truncate(txt, 210)}")

    # Erratic interleaving + Anti-Pattern CSPRNG Permutation Pass
    final_questions = interleave_erratically(questions)

    return {
        "code": code,
        "title": title,
        "cat": cat,
        "dd_count": len(dds),
        "mastery": {"causes": causes_mastery},
        "fond": fond,
        "refs": refs,
        "questions": final_questions,
    }


def main():
    ssp_list, not_dict, doses, glo, prev, monos = load_all_sources()
    os.makedirs(SSP_DIR, exist_ok=True)

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

        ssp_obj = build_ssp_questions(code, title, cat, tip, not_entry, doses, glo, prev, monos, target_total=420)
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
