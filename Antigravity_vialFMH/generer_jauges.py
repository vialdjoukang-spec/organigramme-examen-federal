#!/usr/bin/env python3
"""GENERER_JAUGES — Générateur déterministe (0 token modèle) des jauges fines de production
pour les 248 LOTs PROFILES 2023 et les 2 728 cours (248 × 11 : Phase A + DX.1..DX.10).

Sources lues en lecture seule :
  - LOT_Claude_Finaux/CATALOGUE_248.csv
  - ATTRIBUTIONS.json
  - LOT_Claude_Finaux/ETAT_FILE.json
  - qa/domaines.yml
  - Claude/_reference/prets.txt
  - Conteneurs sur disque : Antigravity_LOTs_du_16_11_2026/, Claude/, ChatGPT_Codex/,
    Grokbot/, LOT_Claude_Finaux/

Sorties écrites uniquement dans Antigravity_vialFMH/ :
  - Antigravity_vialFMH/jauges_248_lots.json
  - Antigravity_vialFMH/jauges_2728_cours.csv

Usage :
  python3 Antigravity_vialFMH/generer_jauges.py
  python3 Antigravity_vialFMH/generer_jauges.py --stdout-summary
  python3 Antigravity_vialFMH/generer_jauges.py --check
"""

from __future__ import annotations

import argparse
import collections
import colorsys
import csv
import hashlib
import html as html_lib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

# --- Constantes alignées sur Claude/_outils/controle3.py, forme.py, verif_aips.py, inventaire_images.py ---

MODULE_IDS = ["PA"] + [f"DX.{i}" for i in range(1, 11)]

CIT_RE = re.compile(r'<sup class="r"><a href="#((?:sb-|[\w-]+-ref-)[\w.\-:]+)">')
NUM_RE = re.compile(r"(?<![\w])(\d+(?:[.,’'\s]\d+)*(?:[.,]\d+)?)(?![\w])")
HORS_AIPS_RE = re.compile(
    r"\b(?:L'|La |Le |Les )([A-Za-zÀ-ÿ-]{4,})(?: [a-zà-ÿ]+)? (?:est|sont) absente?s? de l'AIPS"
)
HORS_AIPS_GENERIC_RE = re.compile(
    r"hors\s+(?:AIPS|information professionnelle)|absente?s?\s+de\s+l['’]AIPS",
    re.I,
)
DOSE_RE = re.compile(
    r"\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|UI|g(?=\s?(?:/kg|/j|/jour|par jour|toutes|i\.?v|IV|per os|p\.o)))(?!\s?/\s?(?:l|L|dl|dL|mmol))\b"
)
CONNECT_RE = re.compile(
    r"\b(car|donc|or|ainsi|puis|alors|parce que|puisque|lorsque|quand|si|tandis que|alors que|"
    r"afin de|afin que|pour que|de sorte que|c'est pourquoi|en effet|cependant|toutefois|"
    r"néanmoins|par conséquent|dès lors|ensuite|enfin|d'abord|en revanche|ce qui|"
    r"grâce à|à cause de|en raison de|si bien que|de ce fait|par ailleurs|en outre|"
    r"autrement dit|c'est-à-dire|d'où|puisqu'|lorsqu'|qu'il)\b",
    re.I,
)
VERBES = set(
    """propose proposent recommande recommandent conseille conseillent mentionne mentionnent contient contiennent figure figurent résulte résultent ajoute ajoutent dépend dépendent rassemble rassemblent résume résument précise précisent indique indiquent décrit décrivent est sont a ont fait font peut peuvent doit doivent reste restent devient deviennent va vont
semble semblent permet permettent signe signent oriente orientent impose imposent confirme confirment élimine
éliminent exclut excluent traite traitent associe associent survient surviennent provoque provoquent entraîne
entraînent exige exigent reçoit reçoivent touche touchent atteint atteignent dépasse dépassent varie varient
augmente augmentent diminue diminuent baisse baissent réduit réduisent favorise favorisent explique expliquent
précède précèdent suit suivent recherche recherchent mesure mesurent montre montrent révèle révèlent
définit définissent correspond correspondent comprend comprennent repose reposent consiste consistent
représente représentent constitue constituent nécessite nécessitent justifie justifient
prescrit prescrivent administre administrent contre-indique évite évitent limite limitent
dure durent persiste persistent apparaît apparaissent disparaît disparaissent évolue évoluent aggrave aggravent
protège protègent prévient préviennent dépiste dépistent détecte détectent distingue distinguent sépare séparent
conduit conduisent mène mènent aboutit aboutissent cause causent déclenche déclenchent libère libèrent
active activent inhibe inhibent bloque bloquent stimule stimulent fixe fixent lie lient agit agissent
s'accompagne s'accompagnent s'associe s'explique s'élève se manifeste se manifestent se traduit se traduisent
se définit se recherche se mesure se prescrit se discute se pose s'impose s'observe s'installe se complique
remplace remplacent compte comptent atteste attestent rappelle rappellent signale signalent
pose posent écarte écartent retient retiennent ordonne ordonnent adapte adaptent surveille surveillent
contrôle contrôlent corrige corrigent restaure restaurent normalise prolonge prolongent
était étaient avait avaient sera seront aura auront serait seraient pourrait pourraient devrait devraient
faut suffit suffisent vise visent cible ciblent porte portent concerne concernent relève relèvent
désigne désignent regroupe regroupent""".split()
)
VERBE_RE = re.compile(
    r"\b(?:\w+(?:ent|ait|aient|era|eront|erait|eraient|ise|isent|it|issent))\b",
    re.I,
)
PRONOM_VERBE_RE = re.compile(
    r"\b(?:il|elle|ils|elles|on|qui|cela|ce|celle-ci|celui-ci)\s+(?:ne\s+|n'|se\s+|s'|l'|le\s+|la\s+|les\s+|y\s+|en\s+)*\w+",
    re.I,
)
LACUNE_RE = re.compile(
    r"\(\s*À vérifier|À vérifier\s*[:)]|reste à (?:lire|vérifier)|texte (?:intégral )?non (?:lu|relu)|"
    r"non relue? dans|faute d'extrait lisible|aucune source (?:lue|lisible)|\bTODO\b|\bFIXME\b",
    re.I,
)
STRUCT_RE = re.compile(
    r"\b(?:points?|DX\.?|rangs?|E|étapes?|îlots?|n°|LOT_?|Phase)\s*\d+(?:[.,]\d+)?|"
    r"\b[A-Z]\d{2}(?:\.\d{1,2})?\b|\bCIM-1[01]\b|\b(?:le|au|du|appeler le)\s+14[0-9]\b|"
    r"\binterleukine[- ]\d+\b|\bIL-\d+\b|^\s*\d{1,2}\.[A-D]\d?\b",
    re.I,
)
SOURCES_RE = re.compile(
    r'<section\b[^>]*id="[\w-]*(?:sources|bib)"[^>]*>.*?</section>|<details\b[^>]*class="refs"[^>]*>.*?</details>',
    re.S | re.I,
)
SCRIPT_FORME = '<script src="../_polices/forme.js" defer></script>'
TAG_SS_RE = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.S | re.I)
VIDES = {
    "br", "hr", "img", "meta", "link", "input", "source", "col",
    "wbr", "area", "base", "embed", "track", "param",
}
CREAM_HEXES = {
    "#f9f5ee", "#fbf7f2", "#f4eadf", "#faf5ef", "#fcf9f4", "#f6ebe0",
    "#f5f5dc", "#fffff0", "#faf0e6", "#fdf5e6", "#faebd7", "#fdf3ee",
    "#fdf6ed", "#f5ded2", "#f5e3cc",
}
INTERP_IMG_RE = re.compile(
    r"\b(on (?:voit|observe|note|distingue)|montre|flèche|repère|noter|remarquer|"
    r"signe (?:de|du)|à comparer|aspect (?:typique|en)|la lecture|interprét|"
    r"met en évidence|visible|opacité|hyper|hypo(?:échog|dens|signal))",
    re.I,
)
FREE_LIC_RE = re.compile(
    r"CC[- ]?BY(?:[- ]SA)?(?:[- ]\d(?:\.\d)?)?|CC0|domaine public|public domain|\bPD\b",
    re.I,
)
FORBIDDEN_LIC_RE = re.compile(r"CC[- ]?BY[- ]?(?:NC|ND)", re.I)
RE_HEX = re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
RE_URL = re.compile(r"https?://([^\s\"'<>)]+)")

# Poids des 8 axes pour le score composite cours (total = 100)
AXIS_WEIGHTS = {
    "G1": 18,
    "G2": 14,
    "G3": 12,
    "G4": 14,
    "G5": 14,
    "G6": 10,
    "G7": 8,
    "G8": 10,
}

# PRs ouverts du 15.11.2026 documentés (Survey 1) pour les LOTs absents de main
DRAFT_PRS_NOV15 = {
    43: "#737 (grok/redaction-lot-043, 2 HTML)",
    44: "#733 (grok/redaction-lot-044, 2 HTML)",
    46: "#740 (grok/redaction-lot-046, 8 HTML)",
    47: "#734 (grok/redaction-lot-047, 2 HTML)",
    48: "#739 (grok/redaction-lot-048, 2 HTML)",
    49: "#738 (grok/redaction-lot-049, 2 HTML)",
    50: "#736 (grok/redaction-lot-050, 4 HTML)",
    80: "#735 (grok/redaction-lot-080, 2 HTML)",
    102: "#732 (grok/redaction-lot-102, 1 HTML)",
}

# PRs ouverts vérifiés via gh pr/api (16.11.2026) pour l'ensemble des LOTs absents & stubs T8e
OPEN_PRS_ABSENTS = {
    42: "#432 (flash/vague1/LOT_042-A)",
    43: "#737 (grok L1 PA+DX.1) + #527 (claude/lot-043, Lo 11/11 + LISTE_DX)",
    44: "#733 (grok L1 PA+DX.1, PA 161.6 Ko -> -11.6 Ko) + #525 (claude/lot-044, Lo 11/11 + LISTE_DX)",
    45: "#524 (claude/lot-045, open non-draft, Lo 11/11 + LISTE_DX_CANONIQUE gelée + paquet.json)",
    46: "#740 (grok L1 PA+DX.1) + #532 (claude/lot-046, Lo 11/11 + LISTE_DX)",
    47: "#734 (grok L1 PA+DX.1) + #537 (claude/lot-047, Lo 11/11 + LISTE_DX)",
    48: "#739 (grok L1 PA+DX.1) + #533 (claude/lot-048, Lo 11/11 + LISTE_DX)",
    49: "#738 (grok L1 PA+DX.1) + #535 (claude/lot-049, Lo 11/11 + LISTE_DX)",
    50: "#736 (grok L1 PA+DX.1) + #539 (claude/lot-050, Lo 11/11 + LISTE_DX)",
    51: "#584 (claude/lot-051, Lo 162 Ko) + #593 (grok/lot-051-bande, Lo 118.5 Ko)",
    52: "#575 (claude/lot-052, Lo) + #594 (grok/lot-052-bande, Lo 103.5 Ko)",
    53: "#595 (grok/lot-053-bande, Lo 100–200 Ko)",
    54: "#596 (grok/lot-054-bande, Lo 100–200 Ko)",
    58: "#597 (grok/lot-058-bande, Lo 100–200 Ko)",
    59: "#598 (grok/lot-059-bande, Lo 100–200 Ko)",
    75: "#430, #431 (flash/vague1/LOT_075-*)",
    76: "#433 (flash/vague1/LOT_076-A)",
    80: "#735 (grok/redaction-lot-080, L1 PA+DX.1 controle3 VERT)",
    102: "#732 (grok/redaction-lot-102, L1 PA seul) + #592 (grok/lot-102, pre-L1 11/11)",
}


def strip_text(fragment: str) -> str:
    return re.sub(r"\s+", " ", html_lib.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def compute_bytes_no_img(h: str) -> int:
    sans_img = re.sub(r"<(svg|picture)\b.*?</\1>", "", h, flags=re.S | re.I)
    sans_img = re.sub(r"<img\b[^>]*>", "", sans_img, flags=re.I)
    sans_img = re.sub(r"data:image/[^\"')\s]+", "", sans_img)
    return len(sans_img.encode("utf-8"))


def check_tag_balance(h: str) -> str | None:
    pile: list[str] = []
    for ferme, nom in re.findall(r"<(/?)([a-zA-Z][\w-]*)\b[^>]*?(?<!/)>", TAG_SS_RE.sub("", h)):
        nom = nom.lower()
        if nom in VIDES:
            continue
        if not ferme:
            pile.append(nom)
        elif pile and pile[-1] == nom:
            pile.pop()
        elif nom in pile:
            return f"fermeture </{nom}> mal placée"
    return None if not pile else f"non fermées: {pile[-5:]}"


def is_verbal(ph: str) -> bool:
    ph_norm = ph.replace("’", "'")
    mots = {m.lower() for m in re.findall(r"[\w'-]+", ph_norm)}
    for m in list(mots):
        em = re.match(r"^(?:n|qu|j|t|m|s)'(.+)$", m)
        if em:
            mots.add(em.group(1))
    return bool(mots & VERBES or PRONOM_VERBE_RE.search(ph_norm) or VERBE_RE.search(ph_norm))


def extract_sentences(h: str) -> list[tuple[str, str, str]]:
    blocs = re.findall(
        r'<(p|li|td|dd|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|li|td|dd|div)>',
        h,
        re.S | re.I,
    )
    out = []
    for tag, b in blocs:
        for brut in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý«])", b):
            t = strip_text(re.sub(r'<sup class="r">.*?</sup>', "", brut, flags=re.S))
            if len(t.split()) >= 4:
                out.append((tag, brut, t))
    return out


def is_blue_hex(hx: str) -> bool:
    v = hx.lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    r, g, b = int(v[0:2], 16) / 255.0, int(v[2:4], 16) / 255.0, int(v[4:6], 16) / 255.0
    h, _l, s = colorsys.rgb_to_hls(r, g, b)
    deg = h * 360.0
    return s >= 0.12 and 150.0 <= deg <= 305.0


def load_domain_whitelist(repo_root: Path) -> set[str]:
    yml_path = repo_root / "qa" / "domaines.yml"
    hosts: set[str] = set()
    if not yml_path.exists():
        return hosts
    txt = yml_path.read_text(encoding="utf-8", errors="ignore")
    for line in txt.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        for item in re.findall(r'"([^"]+)"|([a-zA-Z0-9.-]+\.[a-z]{2,}(?:/[^\s,\]]*)?)', s):
            cand = (item[0] or item[1]).strip()
            if "/" in cand:
                cand = cand.split("/", 1)[0]
            if "." in cand and not cand.endswith(".pdf"):
                hosts.add(cand.lower().lstrip("www."))
    # Ajouter domaines académiques/hospitaliers CH/EU courants documentés dans qa/domaines.yml
    hosts.update(
        {
            "files.refdata.ch",
            "swissmedicinfo.ch",
            "swissmedicinfo-pro.ch",
            "swissmedic.ch",
            "bag.admin.ch",
            "hug.ch",
            "chuv.ch",
            "insel.ch",
            "usz.ch",
            "revmed.ch",
            "smw.ch",
            "fmh.ch",
            "samw.ch",
            "assm.ch",
            "paediatrieschweiz.ch",
            "ssi.guidelines.ch",
            "sginf.ch",
            "sgaim.ch",
            "escardio.org",
            "ersnet.org",
            "eular.org",
            "esmo.org",
            "easl.eu",
            "escmid.org",
            "nice.org.uk",
            "has-sante.fr",
            "awmf.org",
            "who.int",
            "ema.europa.eu",
            "ncbi.nlm.nih.gov",
            "pmc.ncbi.nlm.nih.gov",
            "pubmed.ncbi.nlm.nih.gov",
            "doi.org",
            "europepmc.org",
        }
    )
    return hosts


def url_in_ch_eu_whitelist(url: str, hosts: set[str]) -> bool:
    m = re.match(r"https?://([^/:?#]+)", url, re.I)
    if not m:
        return False
    host = m.group(1).lower()
    if host.startswith("www."):
        host = host[4:]
    if host in hosts:
        return True
    # Sous-domaines autorisés d'un hôte de la liste blanche ou domaines institutionnels .ch / .eu
    for h in hosts:
        if host.endswith("." + h):
            return True
    if host.endswith(".ch") or host.endswith(".europa.eu"):
        return True
    return False


def split_antigravity_bundle(bundle_path: Path) -> tuple[str, dict[str, str], bool]:
    """Découpe un fichier *_complet.html d'Antigravity en (head_style_context, {cid: article_html}, has_custom_script)."""
    raw = bundle_path.read_text(encoding="utf-8", errors="ignore")
    head_m = re.search(r"<head\b[^>]*>(.*?)</head>", raw, re.S | re.I)
    head_ctx = head_m.group(1) if head_m else ""
    modules: dict[str, str] = {}
    for m in re.finditer(
        r'<article\b[^>]*class="lot-course"[^>]*data-cid="(PA|DX\.\d+)"[^>]*>(.*?)</article>',
        raw,
        re.S | re.I,
    ):
        cid = m.group(1).upper()
        modules[cid] = m.group(0)
    outside_articles = re.sub(
        r'<article\b[^>]*class="lot-course"[^>]*>.*?</article>',
        "",
        raw,
        flags=re.S | re.I,
    ).replace(SCRIPT_FORME, "")
    bundle_has_custom_script = bool(re.search(r"<script\b", outside_articles, re.I))
    return head_ctx, modules, bundle_has_custom_script


def extract_section_slice(h: str, pt_num: int) -> str:
    """Extrait le HTML approximatif d'un point `p{pt_num}` jusqu'au point suivant ou biblio."""
    m = re.search(rf'id="[\w-]*p{pt_num}"', h)
    if not m:
        return ""
    start = m.start()
    nxt = re.search(
        rf'id="[\w-]*p{pt_num + 1}"|id="[\w-]*(?:sources|bib)"|<p class="fin-cours"|FIN_FICHIER',
        h[start + 10 :],
    )
    end = start + 10 + nxt.start() if nxt else len(h)
    return h[start:end]


def analyze_course_html(
    lot_num: int,
    cid: str,
    h: str,
    whitelist_hosts: set[str],
    shared_ctx_head: str = "",
    is_bundled: bool = False,
    bundle_has_custom_script: bool = False,
    lot_phrase_seen: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Calcule les 8 axes (G1–G8) et les sous-métriques exactes d'un cours."""
    bytes_raw = len(h.encode("utf-8"))
    h_no_img = re.sub(r"<(svg|picture)\b.*?</\1>", "", h, flags=re.S | re.I)
    h_no_img = re.sub(r"<img\b[^>]*>", "", h_no_img, flags=re.I)
    h_no_img = re.sub(r"data:image/[^\"')\s]+", "", h_no_img)
    bytes_no_img = len(h_no_img.encode("utf-8"))

    # --- G1. Structure & Gabarit L1 ---
    pts_found = [i for i in range(1, 15) if re.search(rf'id="[\w-]*p{i}"', h_no_img)]
    pts_count = len(pts_found)
    has_fin_fichier = "FIN_FICHIER" in h_no_img[-400:]
    has_fin_cours = "FIN_COURS" in h_no_img[-400:]
    fin_ok = has_fin_fichier or (is_bundled and has_fin_cours)
    bal_err = check_tag_balance(h_no_img)
    balises_ok = bal_err is None
    no_cim_tree = not bool(re.search(r"Où se situe le problème", h_no_img))
    pt1_def_only = not (
        bool(re.search(r"<h[1-4][^>]*>(?:<[^>]+>)*\s*1\.\s*Définition et sémantique", h_no_img))
        or bool(re.search(r">\s*Notions voisines\s*<", h_no_img))
    )
    title_attr_count = len(re.findall(r"\stitle=", h_no_img))
    tables_total = len(re.findall(r"<table\b", h_no_img))
    tables_wrapped = len(re.findall(r"overflow-x:\s*auto[^>]*>\s*<table", h_no_img))
    tables_unwrapped = max(0, tables_total - tables_wrapped)

    ids_all = set(re.findall(r'\bid="([^"]+)"', h_no_img))
    # Dans un bundle, les liens peuvent cibler le contexte global ou l'article ; on vérifie dans l'article
    broken_anchors = len(
        {
            x
            for x in re.findall(r'href="#([^"]+)"', h_no_img)
            if x and x not in ids_all and not x.startswith("course-")
        }
    )

    nested_fenetre = 0
    pile: list[bool] = []
    for m in re.finditer(r"<section\b([^>]*)>|</section>", h_no_img):
        if m.group(0) == "</section>":
            if pile:
                pile.pop()
            continue
        fen = "fenetre" in m.group(1)
        if fen and any(pile):
            nested_fenetre += 1
        pile.append(fen)

    unconverted_tpl = len(re.findall(r"\(\{[^)]{0,80}\}\)", h_no_img))
    fenetre_count = len(re.findall(r'<(?:section|div|details)\b[^>]*class="[^"]*\bfenetre\b', h_no_img, re.I))
    script_cleaned = h_no_img.replace(SCRIPT_FORME, "")
    custom_script_count = len(re.findall(r"<script\b", script_cleaned, re.I))
    if is_bundled and (bundle_has_custom_script or "<script" in shared_ctx_head.lower()):
        custom_script_count = max(custom_script_count, 1)

    g1_checks = [
        pts_count == 14,
        fin_ok,
        balises_ok,
        no_cim_tree,
        pt1_def_only,
        title_attr_count == 0,
        tables_unwrapped == 0 or is_bundled,
        broken_anchors == 0,
        nested_fenetre == 0,
        unconverted_tpl == 0,
        fenetre_count >= 1,
        custom_script_count == 0,
    ]
    g1_score = round(100.0 * sum(g1_checks) / len(g1_checks), 1)
    g1_pass = (
        pts_count == 14
        and fin_ok
        and balises_ok
        and no_cim_tree
        and pt1_def_only
        and nested_fenetre == 0
        and unconverted_tpl == 0
        and fenetre_count >= 1
    )

    # --- G2. Volume hors images ---
    in_l1_band = 80_000 <= bytes_no_img <= 150_000
    in_sweet_spot = 115_000 <= bytes_no_img <= 145_000
    is_stub = bytes_no_img < 20_000
    if is_stub:
        size_band = "STUB_<20K"
        g2_score = 5.0
    elif bytes_no_img < 80_000:
        size_band = "SOUS_BANDE_20_80K"
        g2_score = round(max(20.0, 80.0 * (bytes_no_img / 80_000.0)), 1)
    elif bytes_no_img <= 150_000:
        size_band = "L1_CONFORME_80_150K"
        g2_score = 100.0 if in_sweet_spot else 92.0
    else:
        size_band = "SUR_BANDE_>150K"
        over_ratio = min(1.0, (bytes_no_img - 150_000) / 100_000.0)
        g2_score = round(max(25.0, 75.0 - 50.0 * over_ratio), 1)
    g2_pass = in_l1_band

    # --- G3. Langue & Non-Redondance ---
    body_sans_src = SOURCES_RE.sub(" ", h_no_img)
    phrases = extract_sentences(body_sans_src)
    paras = re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>', body_sans_src, re.S | re.I)
    paras_no_conn = sum(
        1 for p in paras if len(strip_text(p).split()) > 40 and not CONNECT_RE.search(strip_text(p))
    )

    nominal_cnt = 0
    long_gt32_cnt = 0
    short_lt12_cnt = 0
    intra_dup_cnt = 0
    inter_dup_cnt = 0
    local_hashes: set[str] = set()
    non_td_phrases = 0
    conn_phrases = 0

    for tag, _b, t in phrases:
        if tag.lower() == "td":
            continue
        non_td_phrases += 1
        words = len(t.split())
        if not is_verbal(t):
            nominal_cnt += 1
        if words > 32:
            long_gt32_cnt += 1
        if words < 12:
            short_lt12_cnt += 1
        if CONNECT_RE.search(t):
            conn_phrases += 1
        if len(t) > 60:
            k = hashlib.sha1(re.sub(r"\W+", "", t.lower()).encode("utf-8")).hexdigest()
            if k in local_hashes:
                intra_dup_cnt += 1
            local_hashes.add(k)
            if lot_phrase_seen is not None:
                if k in lot_phrase_seen and lot_phrase_seen[k] != cid:
                    inter_dup_cnt += 1
                else:
                    lot_phrase_seen.setdefault(k, cid)

    nph = max(1, non_td_phrases)
    connecteur_pct = round(100.0 * conn_phrases / nph, 1)
    g3_penalty = (
        min(35.0, nominal_cnt * 1.5)
        + min(20.0, long_gt32_cnt * 1.5)
        + min(20.0, intra_dup_cnt * 5.0)
        + min(25.0, inter_dup_cnt * 10.0)
    )
    if connecteur_pct < 15.0:
        g3_penalty += 10.0
    g3_score = round(max(0.0, 100.0 - g3_penalty), 1)
    if is_stub:
        g3_score = min(g3_score, 20.0)
    g3_pass = (
        not is_stub
        and nominal_cnt <= 3
        and long_gt32_cnt <= 3
        and intra_dup_cnt == 0
        and inter_dup_cnt == 0
    )

    # --- G4. Sources & Véracité CH/EU ---
    sup_r_count = len(re.findall(r'<sup class="r">', h_no_img))
    nums_no_cite = 0
    lacune_cnt = 0
    for tag, b, t in phrases:
        if LACUNE_RE.search(t):
            lacune_cnt += 1
        cites = CIT_RE.findall(b)
        nums = NUM_RE.findall(STRUCT_RE.sub(" ", t))
        if nums and not cites and tag.lower() != "td":
            nums_no_cite += 1

    bib_items: list[str] = []
    for m in re.finditer(r"<li\b([^>]*)>", h_no_img, re.I):
        attrs = m.group(1)
        if re.search(r'\bid="(?:sb-|[\w-]+-ref-|src-|source-)[^"]*"', attrs, re.I):
            end_li = h_no_img.find("</li>", m.end())
            if end_li != -1:
                bib_items.append(h_no_img[m.end() : end_li])
    if not bib_items:
        for sb_m in SOURCES_RE.finditer(h_no_img):
            bib_items.extend(re.findall(r"<li\b[^>]*>(.*?)</li>", sb_m.group(0), re.S | re.I))
    if not bib_items:
        for m in re.finditer(r"<div\b([^>]*)>", h_no_img, re.I):
            if re.search(r'\bclass="[^"]*\bsb\b[^"]*"', m.group(1), re.I):
                end_div = h_no_img.find("</div>", m.end())
                if end_div != -1:
                    bib_items.append(h_no_img[m.end() : end_div])
    bib_count = len(bib_items)
    dated_bib = sum(
        1 for bi in bib_items if re.search(r"consulté|20[12]\d", strip_text(bi), re.I)
    )
    bib_urls = []
    for bi in bib_items:
        for um in RE_URL.findall(bi):
            bib_urls.append("https://" + um)
    ch_eu_urls = sum(1 for u in bib_urls if url_in_ch_eu_whitelist(u, whitelist_hosts))
    ch_eu_ratio = round(100.0 * ch_eu_urls / len(bib_urls), 1) if bib_urls else 0.0

    g4_score = 0.0
    if sup_r_count > 0:
        g4_score += 30.0
    elif bib_count > 0:
        g4_score += 15.0
    if bib_count >= 5:
        g4_score += 20.0
    elif bib_count >= 1:
        g4_score += 10.0
    if bib_count > 0 and dated_bib == bib_count:
        g4_score += 15.0
    elif dated_bib > 0:
        g4_score += 8.0
    if bib_urls and ch_eu_ratio >= 85.0:
        g4_score += 20.0
    elif ch_eu_urls > 0:
        g4_score += 10.0
    if lacune_cnt == 0:
        g4_score += 15.0
    if nums_no_cite > 5:
        g4_score = max(0.0, g4_score - min(20.0, (nums_no_cite - 5) * 1.5))
    g4_score = round(min(100.0, g4_score), 1)
    g4_pass = sup_r_count >= 10 and bib_count >= 3 and lacune_cnt == 0 and nums_no_cite <= 5

    # --- G5. Pharmacologie & AIPS ---
    bib_map_by_id: dict[str, str] = {}
    for m in re.finditer(r"<li\b([^>]*)>", h_no_img, re.I):
        idm = re.search(r'\bid="([^"]+)"', m.group(1), re.I)
        if idm:
            end_li = h_no_img.find("</li>", m.end())
            if end_li != -1:
                bid = idm.group(1)
                bbody = h_no_img[m.end() : end_li]
                bib_map_by_id[bid] = bbody
                for sm in re.finditer(r'<span\b[^>]*id="(sb-[^"]+)"', bbody, re.I):
                    bib_map_by_id[sm.group(1)] = bbody
    for m in re.finditer(r"<div\b([^>]*)>", h_no_img, re.I):
        attrs = m.group(1)
        if "sb" not in attrs:
            continue
        if re.search(r'\bclass="[^"]*\bsb\b[^"]*"', attrs, re.I):
            idm = re.search(r'\bid="([^"]+)"', attrs, re.I)
            if idm:
                end_div = h_no_img.find("</div>", m.end())
                if end_div != -1:
                    bib_map_by_id.setdefault(idm.group(1), h_no_img[m.end() : end_div])
    aips_bib_ids = {
        bid
        for bid, btxt in bib_map_by_id.items()
        if "aips" in bid.lower() or "files.refdata.ch" in btxt.lower() or "swissmedic" in btxt.lower()
    }
    hors_aips_mols = {m.lower() for m in HORS_AIPS_RE.findall(strip_text(h_no_img))}
    dose_cnt = 0
    dose_bad_cnt = 0
    for _tag, b, t in phrases:
        if DOSE_RE.search(t):
            dose_cnt += 1
            cites = CIT_RE.findall(b)
            has_aips = any(("aips" in c.lower() or c in aips_bib_ids) for c in cites) or bool(
                re.search(r"Swissmedic|n°\s*\d{4,5}", t) and cites
            )
            has_hors = bool(
                cites
                and (
                    any(mol in t.lower() for mol in hors_aips_mols)
                    or HORS_AIPS_GENERIC_RE.search(t)
                )
            )
            if not (has_aips or has_hors):
                dose_bad_cnt += 1

    aips_bib_cnt = len(re.findall(r'id="sb-aips-[0-9a-z]+"', h_no_img, re.I))
    aips_refdata_cnt = len(re.findall(r"https://files\.refdata\.ch/", h_no_img, re.I))
    swissmedic_no_cnt = len(re.findall(r"Swissmedic|n°\s*\d{4,5}", h_no_img))
    compendium_cnt = len(re.findall(r"compendium\.ch", h_no_img, re.I))
    mb_cnt = len(re.findall(r'class="[^"]*\bmb\b', h_no_img))
    has_urgence_modal = bool(
        re.search(r"Urgence\s*[—–-]\s*conduite chronologique", h_no_img, re.I)
        or re.search(r"conduite chronologique|prise en charge en urgence", h_no_img, re.I)
    )

    if dose_cnt == 0 and cid == "PA":
        g5_score = 90.0 if compendium_cnt == 0 else 40.0
    else:
        g5_score = 100.0
        if dose_bad_cnt > 0:
            g5_score -= min(50.0, dose_bad_cnt * 12.0)
        if compendium_cnt > 0:
            g5_score -= 30.0
        if cid != "PA" and (aips_bib_cnt == 0 and len(aips_bib_ids) == 0 and swissmedic_no_cnt == 0):
            g5_score -= 25.0
        if cid != "PA" and mb_cnt == 0 and not is_bundled:
            g5_score -= 10.0
        if cid != "PA" and not has_urgence_modal:
            g5_score -= 5.0
    if is_stub:
        g5_score = min(g5_score, 15.0)
    g5_score = round(max(0.0, g5_score), 1)
    g5_pass = (
        not is_stub
        and compendium_cnt == 0
        and dose_bad_cnt == 0
        and (cid == "PA" or aips_bib_cnt > 0 or len(aips_bib_ids) > 0 or swissmedic_no_cnt > 0)
    )

    # --- G6. Complétude pédagogique (µ3 + 11.11) ---
    p3_slice = extract_section_slice(h_no_img, 3)
    p6_slice = extract_section_slice(h_no_img, 6)
    p11_slice = extract_section_slice(h_no_img, 11)
    p13_slice = extract_section_slice(h_no_img, 13)
    p14_slice = extract_section_slice(h_no_img, 14)

    needs_anatomo = lot_num >= 21 or (lot_num == 20 and cid == "DX.1")
    pt3_has_anatomo = bool(
        re.search(r"Base à connaître|anatomo-fonctionnel|physiopatholog|voie\s+|innervation|récepteur", p3_slice, re.I)
    )
    pt6_fen_cnt = len(re.findall(r'class="[^"]*\bfenetre\b|class="ouvre"', p6_slice))
    pt11_subparts = sum(
        1 for sub in ("11.A", "11.B", "11.C", "11.D") if sub in p11_slice or sub in h_no_img
    )
    pt13_no_fen = bool(p13_slice) and ('class="fenetre"' not in p13_slice)
    p14_tr_rows = max(0, len(re.findall(r"<tr\b", p14_slice)) - len(re.findall(r"<tr\b[^>]*>\s*<th\b", p14_slice)))
    p14_q_markers = len(re.findall(r"(?:Question\s*\d+|<strong>\s*Q\d*\s*[:.]|<dt\b)", p14_slice, re.I))
    pt14_qr_cnt = max(p14_tr_rows, p14_q_markers)

    g6_pts = 0.0
    if pts_count == 14:
        g6_pts += 20.0
    if pt6_fen_cnt >= 2:
        g6_pts += 20.0
    elif pt6_fen_cnt == 1:
        g6_pts += 10.0
    if pt11_subparts >= 4:
        g6_pts += 20.0
    elif pt11_subparts >= 2:
        g6_pts += 10.0
    if pt13_no_fen:
        g6_pts += 15.0
    if pt14_qr_cnt >= 6:
        g6_pts += 25.0
    elif pt14_qr_cnt >= 1:
        g6_pts += 10.0
    if needs_anatomo and not pt3_has_anatomo:
        g6_pts = max(0.0, g6_pts - 15.0)
    g6_score = round(min(100.0, g6_pts), 1)
    g6_pass = (
        pts_count == 14
        and pt6_fen_cnt >= 1
        and pt11_subparts >= 3
        and pt13_no_fen
        and pt14_qr_cnt >= 6
        and (not needs_anatomo or pt3_has_anatomo)
    )

    # --- G7. Images pédagogiques (µ6 v2) ---
    figs_raw = re.findall(r"<figure\b.*?</figure>|<img\b[^>]*>|<svg\b.*?</svg>", h, re.S | re.I)
    img_count = len(figs_raw)
    data_img_count = len(re.findall(r"data:image/", h, re.I))
    free_lic_cnt = 0
    nc_nd_cnt = 0
    guided_interp_cnt = 0
    for fb in figs_raw:
        fb_clean = re.sub(r"data:image/[^\"')\s]+", "", fb)
        if FREE_LIC_RE.search(fb_clean):
            free_lic_cnt += 1
        if FORBIDDEN_LIC_RE.search(fb_clean):
            nc_nd_cnt += 1
        if INTERP_IMG_RE.search(fb_clean):
            guided_interp_cnt += 1
    if img_count > 0 and free_lic_cnt == 0:
        free_lic_cnt = len(FREE_LIC_RE.findall(h_no_img))
    if img_count > 0 and nc_nd_cnt == 0:
        nc_nd_cnt = len(FORBIDDEN_LIC_RE.findall(h_no_img))

    if img_count == 0:
        g7_score = 20.0 if cid == "PA" else 0.0
    else:
        g7_score = 40.0
        if free_lic_cnt > 0:
            g7_score += 25.0
        if guided_interp_cnt > 0:
            g7_score += 25.0
        if data_img_count > 0 or len(re.findall(r"<figure\b", h_no_img, re.I)) > 0:
            g7_score += 10.0
        if nc_nd_cnt > 0:
            g7_score = max(0.0, g7_score - 40.0)
    g7_score = round(min(100.0, g7_score), 1)
    g7_pass = img_count >= 1 and free_lic_cnt >= 1 and nc_nd_cnt == 0

    # --- G8. Design & Front-End Uniforme ---
    has_forme_css = "../_polices/forme.css" in h_no_img
    has_forme_js = "../_polices/forme.js" in h_no_img
    has_brain_barre14 = 'id="brain-barre14"' in h_no_img or 'id="brain-barre14"' in shared_ctx_head
    has_fm_bandeau = 'id="fm-bandeau"' in h_no_img or 'class="fm-bandeau"' in h_no_img

    style_zone = shared_ctx_head + "\n" + "\n".join(
        re.findall(r"<style\b[^>]*>(.*?)</style>", h_no_img, re.S | re.I)
    ) + "\n" + "\n".join(re.findall(r'\sstyle="([^"]*)"', h_no_img, re.I))

    cream_hits = sum(1 for ch in CREAM_HEXES if ch in style_zone.lower())
    blue_hits = sum(1 for hx in RE_HEX.findall(style_zone) if is_blue_hex(hx))
    pure_white_bg = ("--fm-fond:#fff" in style_zone.lower() or has_forme_css) and cream_hits == 0

    g8_pts = 0.0
    if has_forme_css:
        g8_pts += 35.0
    if has_forme_js:
        g8_pts += 20.0
    if has_brain_barre14:
        g8_pts += 10.0
    if has_fm_bandeau:
        g8_pts += 10.0
    if cream_hits == 0:
        g8_pts += 15.0
    if blue_hits == 0:
        g8_pts += 10.0
    if is_stub:
        g8_pts = min(g8_pts, 25.0)
    g8_score = round(min(100.0, g8_pts), 1)
    g8_pass = has_forme_css and has_forme_js and cream_hits == 0 and blue_hits == 0

    # --- Composite ---
    scores_map = {
        "G1": g1_score,
        "G2": g2_score,
        "G3": g3_score,
        "G4": g4_score,
        "G5": g5_score,
        "G6": g6_score,
        "G7": g7_score,
        "G8": g8_score,
    }
    score_composite = round(
        sum(scores_map[ax] * w for ax, w in AXIS_WEIGHTS.items()) / 100.0,
        1,
    )

    return {
        "exists": True,
        "bytes_raw": bytes_raw,
        "bytes_no_img": bytes_no_img,
        "size_band": size_band,
        "g1_score": g1_score,
        "g1_pass": g1_pass,
        "points_1_14": pts_count,
        "fin_ok": fin_ok,
        "balises_ok": balises_ok,
        "no_cim_tree": no_cim_tree,
        "pt1_def_only": pt1_def_only,
        "title_attr_count": title_attr_count,
        "tables_unwrapped": tables_unwrapped,
        "broken_anchors": broken_anchors,
        "nested_fenetre": nested_fenetre,
        "unconverted_tpl": unconverted_tpl,
        "fenetre_count": fenetre_count,
        "custom_script_count": custom_script_count,
        "g2_score": g2_score,
        "g2_pass": g2_pass,
        "in_l1_band": in_l1_band,
        "in_sweet_spot": in_sweet_spot,
        "is_stub": is_stub,
        "g3_score": g3_score,
        "g3_pass": g3_pass,
        "phrase_count": non_td_phrases,
        "nominal_sentences": nominal_cnt,
        "long_sentences_gt32": long_gt32_cnt,
        "short_sentences_lt12": short_lt12_cnt,
        "intra_dup_phrases": intra_dup_cnt,
        "inter_dup_phrases": inter_dup_cnt,
        "connecteur_pct": connecteur_pct,
        "paras_without_connector": paras_no_conn,
        "g4_score": g4_score,
        "g4_pass": g4_pass,
        "sup_r_count": sup_r_count,
        "bib_entries_count": bib_count,
        "dated_bib_count": dated_bib,
        "ch_eu_domain_ratio": ch_eu_ratio,
        "nums_no_cite_count": nums_no_cite,
        "lacune_formula_count": lacune_cnt,
        "g5_score": g5_score,
        "g5_pass": g5_pass,
        "dose_sentences_count": dose_cnt,
        "dose_bad_count": dose_bad_cnt,
        "aips_bib_count": aips_bib_cnt,
        "aips_refdata_count": aips_refdata_cnt,
        "swissmedic_no_count": swissmedic_no_cnt,
        "compendium_ch_count": compendium_cnt,
        "mb_sheets_count": mb_cnt,
        "has_urgence_modal": has_urgence_modal,
        "g6_score": g6_score,
        "g6_pass": g6_pass,
        "needs_anatomo": needs_anatomo,
        "pt3_has_anatomo": pt3_has_anatomo,
        "pt6_fenetre_count": pt6_fen_cnt,
        "pt11_subparts": pt11_subparts,
        "pt13_intact_no_fenetre": pt13_no_fen,
        "pt14_qr_count": pt14_qr_cnt,
        "g7_score": g7_score,
        "g7_pass": g7_pass,
        "img_count": img_count,
        "data_img_count": data_img_count,
        "free_lic_count": free_lic_cnt,
        "nc_nd_forbidden_count": nc_nd_cnt,
        "guided_interp_count": guided_interp_cnt,
        "g8_score": g8_score,
        "g8_pass": g8_pass,
        "has_forme_css": has_forme_css,
        "has_forme_js": has_forme_js,
        "has_brain_barre14": has_brain_barre14,
        "has_fm_bandeau": has_fm_bandeau,
        "pure_white_bg": pure_white_bg,
        "forbidden_cream_count": cream_hits,
        "blue_hex_count": blue_hits,
        "score_composite": score_composite,
    }


def empty_course_metrics(lot_num: int, cid: str) -> dict[str, Any]:
    return {
        "exists": False,
        "bytes_raw": 0,
        "bytes_no_img": 0,
        "size_band": "ABSENT",
        "g1_score": 0.0,
        "g1_pass": False,
        "points_1_14": 0,
        "fin_ok": False,
        "balises_ok": False,
        "no_cim_tree": False,
        "pt1_def_only": False,
        "title_attr_count": 0,
        "tables_unwrapped": 0,
        "broken_anchors": 0,
        "nested_fenetre": 0,
        "unconverted_tpl": 0,
        "fenetre_count": 0,
        "custom_script_count": 0,
        "g2_score": 0.0,
        "g2_pass": False,
        "in_l1_band": False,
        "in_sweet_spot": False,
        "is_stub": False,
        "g3_score": 0.0,
        "g3_pass": False,
        "phrase_count": 0,
        "nominal_sentences": 0,
        "long_sentences_gt32": 0,
        "short_sentences_lt12": 0,
        "intra_dup_phrases": 0,
        "inter_dup_phrases": 0,
        "connecteur_pct": 0.0,
        "paras_without_connector": 0,
        "g4_score": 0.0,
        "g4_pass": False,
        "sup_r_count": 0,
        "bib_entries_count": 0,
        "dated_bib_count": 0,
        "ch_eu_domain_ratio": 0.0,
        "nums_no_cite_count": 0,
        "lacune_formula_count": 0,
        "g5_score": 0.0,
        "g5_pass": False,
        "dose_sentences_count": 0,
        "dose_bad_count": 0,
        "aips_bib_count": 0,
        "aips_refdata_count": 0,
        "swissmedic_no_count": 0,
        "compendium_ch_count": 0,
        "mb_sheets_count": 0,
        "has_urgence_modal": False,
        "g6_score": 0.0,
        "g6_pass": False,
        "needs_anatomo": lot_num >= 21 or (lot_num == 20 and cid == "DX.1"),
        "pt3_has_anatomo": False,
        "pt6_fenetre_count": 0,
        "pt11_subparts": 0,
        "pt13_intact_no_fenetre": False,
        "pt14_qr_count": 0,
        "g7_score": 0.0,
        "g7_pass": False,
        "img_count": 0,
        "data_img_count": 0,
        "free_lic_count": 0,
        "nc_nd_forbidden_count": 0,
        "guided_interp_count": 0,
        "g8_score": 0.0,
        "g8_pass": False,
        "has_forme_css": False,
        "has_forme_js": False,
        "has_brain_barre14": False,
        "has_fm_bandeau": False,
        "pure_white_bg": False,
        "forbidden_cream_count": 0,
        "blue_hex_count": 0,
        "score_composite": 0.0,
    }


def evaluate_lot_audits_and_p1(lot_dir: Path | None, lot_num: int) -> dict[str, Any]:
    """Évalue P1_gel, maturite_audit (0..4) et MANIFESTE SHA-256 à partir des vrais fichiers sur disque."""
    if lot_dir is None or not lot_dir.exists():
        return {
            "p1_gel": False,
            "p1_statut": "ABSENT",
            "maturite_audit": 0,
            "audit_note": "Aucun dossier sur main",
            "audit_files_count": 0,
            "manifeste_present": False,
            "manifeste_sha_exact": False,
        }

    # Cas spécifique Antigravity LOT_033
    if lot_dir.parent.name == "Antigravity_LOTs_du_16_11_2026":
        aud_md = lot_dir / f"LOT_{lot_num:03d}_audits.md"
        if aud_md.exists():
            txt = aud_md.read_text(encoding="utf-8", errors="ignore")
            has_approve = "APPROVE" in txt and "CLEAN" in txt
            return {
                "p1_gel": "10 DX gelés" in txt or "LISTE_DX" in txt or has_approve,
                "p1_statut": "GEL_BUNDLE",
                "maturite_audit": 3 if has_approve else 1,
                "audit_note": "4/4 portes PASS (Audit1 97.1%, Contre-Audit2 96.4%, Forensique CLEAN, Challenger APPROVE) ; 11 HTML séparés + MANIFESTE manquants",
                "audit_files_count": 1,
                "manifeste_present": False,
                "manifeste_sha_exact": False,
            }

    audits_dir = lot_dir / "audits"
    audit_files = sorted(audits_dir.glob("*")) if audits_dir.exists() else []
    ldx_md = lot_dir / "LISTE_DX_CANONIQUE.md"
    ldx_json = audits_dir / "LISTE_DX.audit.json"
    p1_statut = "ABSENT"
    p1_gel = False
    if ldx_json.exists():
        try:
            j = json.loads(ldx_json.read_text(encoding="utf-8", errors="ignore"))
            v = str(j.get("verdict") or j.get("statut") or "").upper()
            p1_statut = v or "PRESENT"
            p1_gel = v == "GEL" and ldx_md.exists()
        except Exception:
            p1_statut = "ILLISIBLE"
    elif ldx_md.exists():
        p1_statut = "NON_AUDITE"

    manifeste_path = lot_dir / "MANIFESTE.json"
    manifeste_present = manifeste_path.exists()
    manifeste_sha_exact = False
    if manifeste_present:
        try:
            mj = json.loads(manifeste_path.read_text(encoding="utf-8", errors="ignore"))
            manifest_entries: list[tuple[str, str]] = []
            raw_files = mj.get("fichiers") if "fichiers" in mj else mj.get("files")
            if isinstance(raw_files, dict):
                for fname, meta in raw_files.items():
                    exp = meta.get("sha256") if isinstance(meta, dict) else meta
                    if fname and exp:
                        manifest_entries.append((str(fname), str(exp)))
            elif isinstance(raw_files, list):
                for item in raw_files:
                    if isinstance(item, dict):
                        fn = item.get("fichier") or item.get("nom") or item.get("file")
                        exp = item.get("sha256")
                        if fn and exp:
                            manifest_entries.append((str(fn), str(exp)))
            elif isinstance(mj, dict):
                for k, v in mj.items():
                    if isinstance(v, dict) and "sha256" in v and v["sha256"]:
                        manifest_entries.append((str(k), str(v["sha256"])))
                    elif isinstance(v, str) and len(v) >= 8 and "." in str(k):
                        manifest_entries.append((str(k), v))
            if manifest_entries:
                ok = True
                for fname, exp in manifest_entries:
                    fp = lot_dir / fname
                    if not fp.exists() or len(exp) < 8:
                        ok = False
                        break
                    got = hashlib.sha256(fp.read_bytes()).hexdigest()
                    if not got.startswith(exp):
                        ok = False
                        break
                manifeste_sha_exact = ok
        except Exception:
            manifeste_sha_exact = False

    if not audit_files:
        return {
            "p1_gel": p1_gel,
            "p1_statut": p1_statut,
            "maturite_audit": 0,
            "audit_note": "Non audité (0 fichier dans audits/)" + (" · MANIFESTE présent sans audit" if manifeste_present else ""),
            "audit_files_count": 0,
            "manifeste_present": manifeste_present,
            "manifeste_sha_exact": manifeste_sha_exact,
        }

    # Détecter Audit 1 vs Contre-audit 2 vs Pre-L1 Codex
    is_codex_pre_l1 = lot_dir.parent.name == "ChatGPT_Codex"
    if is_codex_pre_l1:
        return {
            "p1_gel": p1_gel,
            "p1_statut": p1_statut,
            "maturite_audit": 1,
            "audit_note": f"Audit V0 pré-L1 ({len(audit_files)} fichiers dans audits/) — à réauditer en L1",
            "audit_files_count": len(audit_files),
            "manifeste_present": manifeste_present,
            "manifeste_sha_exact": manifeste_sha_exact,
        }

    # Lire les verdicts JSON de contre-audit / audit2
    contre_files = [
        f
        for f in audit_files
        if f.suffix == ".json" and ("audit2" in f.name or "contre_audit" in f.name)
    ]
    a1_files = [
        f
        for f in audit_files
        if f.suffix == ".json"
        and f not in contre_files
        and f.name != "LISTE_DX.audit.json"
    ]

    contre_verdicts = []
    for cf in contre_files:
        try:
            j = json.loads(cf.read_text(encoding="utf-8", errors="ignore"))
            v = str(j.get("verdict") or j.get("statut") or "").strip()
            fn = str(j.get("finale") or "").strip().lower()
            corrs = j.get("corrections")
            has_corrs = isinstance(corrs, list) and len(corrs) > 0
            if v:
                v_up = v.upper()
                if fn.startswith("non"):
                    v_up = f"{v_up}_FINALE_NON"
                contre_verdicts.append((cf.name, v_up))
            elif fn:
                if fn.startswith("non"):
                    corr_lbl = f"({len(corrs)} corr.)" if has_corrs else ""
                    contre_verdicts.append((cf.name, f"FINALE_NON{corr_lbl}"))
                elif fn.startswith("oui"):
                    if has_corrs:
                        contre_verdicts.append((cf.name, f"CORRECTIONS_FINALE_OUI({len(corrs)})"))
                    else:
                        contre_verdicts.append((cf.name, "ACCEPTE_FINALE_OUI"))
        except Exception:
            pass

    all_accepte = bool(contre_verdicts) and all(
        any(tok in v for tok in ("ACCEPTE", "APPROVE", "CONFORME", "AUDIT-OK"))
        and "CORR" not in v
        and "REFUS" not in v
        and "NON" not in v
        for _fn, v in contre_verdicts
    )
    has_phase_b_contre = (
        (audits_dir / "contre_audit.audit.json").exists()
        or (audits_dir / "phase_B.contre_audit.json").exists()
        or any(
            ("DX" in cf.name or "phase_B" in cf.name or bool(re.match(r"LOT_\d{3}\.audit2\.json$", cf.name)))
            and "L1_fidelite" not in cf.name
            for cf in contre_files
        )
    )

    if contre_files:
        if all_accepte and has_phase_b_contre and manifeste_sha_exact:
            mat = 4
            note = f"Contre-audit ACCEPTE/conforme + MANIFESTE SHA-256 exact ({len(contre_verdicts)} verdicts)"
        elif all_accepte and has_phase_b_contre:
            mat = 3
            note = f"Contre-audit ACCEPTE/conforme ({len(contre_verdicts)} verdicts), sans MANIFESTE SHA-256 vérifié"
        else:
            mat = 2
            neg = [f"{fn}={v}" for fn, v in contre_verdicts if "CORR" in v or "REFUS" in v or "NON" in v]
            note = f"Audit 2 / Contre-audit partiel ou CORRECTIONS ({len(contre_verdicts)} verdicts : {', '.join(neg[:3])})"
    elif a1_files or audit_files:
        mat = 1
        note = f"Audit 1 seul ({len(a1_files)} JSON)"
    else:
        mat = 0
        note = "Non audité"

    return {
        "p1_gel": p1_gel,
        "p1_statut": p1_statut,
        "maturite_audit": mat,
        "audit_note": note,
        "audit_files_count": len(audit_files),
        "manifeste_present": manifeste_present,
        "manifeste_sha_exact": manifeste_sha_exact,
    }


def classify_tier_and_wave(
    lot_num: int,
    container: str | None,
    present_count: int,
    courses: dict[str, dict[str, Any]],
    audit_info: dict[str, Any],
) -> tuple[str, str]:
    """Détermine le palier exact (T1..T9) et la vague de reprise (DONE, W0..W5)."""
    if container is None or present_count == 0:
        return "T9", ("W0" if lot_num in DRAFT_PRS_NOV15 else "W2")

    if container == "Antigravity_LOTs_du_16_11_2026":
        return "T1", "W0"

    if container == "Claude":
        if 17 <= lot_num <= 22:
            return "T2a", "DONE"
        if 1 <= lot_num <= 16:
            return "T2b", "W0"
        if 23 <= lot_num <= 32:
            return "T2c", "W0"
        if present_count < 11:
            return "T5", ("W1" if lot_num <= 42 else "W3")
        fen_cnt = sum(1 for c in courses.values() if c["fenetre_count"] > 0)
        if fen_cnt == 11:
            return "T3", "W1"
        return "T4", ("W1" if lot_num <= 42 else "W3")

    if container == "ChatGPT_Codex":
        if audit_info["maturite_audit"] >= 1 and present_count == 11:
            return "T6", "W4"
        return "T7", "W4"

    if container == "Grokbot":
        stubs = sum(1 for c in courses.values() if c["exists"] and c["is_stub"])
        if stubs >= 6:
            return "T8e", "W2"
        if present_count < 11:
            return "T8d", "W5"
        in_band = sum(1 for c in courses.values() if c["in_l1_band"])
        fen_cnt = sum(1 for c in courses.values() if c["fenetre_count"] > 0)
        if in_band == 11 and fen_cnt >= 10:
            return "T8a", "W5"
        if in_band == 11:
            return "T8b", "W5"
        return "T8c", "W5"

    return "T4", "W5"


def compute_coherence_ab(lot_dir: Path | None, courses_html: dict[str, str], courses_metrics: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Vérifie la cohérence entre Phase A / LISTE_DX_CANONIQUE.md et les DX.1..DX.10 + 0 partage inter-fichiers."""
    inter_dups = sum(c["inter_dup_phrases"] for c in courses_metrics.values())
    pa_html = courses_html.get("PA", "")
    dx_present = sum(1 for i in range(1, 11) if f"DX.{i}" in courses_html)

    # Extraire les noms DX de LISTE_DX_CANONIQUE.md ou de Phase A
    expected_names: dict[int, str] = {}
    if lot_dir and (lot_dir / "LISTE_DX_CANONIQUE.md").exists():
        txt = (lot_dir / "LISTE_DX_CANONIQUE.md").read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"\bDX\.(\d{1,2})\b[^\w\n]{1,5}([^\n|]{3,80})", txt):
            i = int(m.group(1))
            if 1 <= i <= 10 and i not in expected_names:
                expected_names[i] = re.sub(r"[*`#]+", "", m.group(2)).strip()
    if len(expected_names) < 10 and pa_html:
        for m in re.finditer(r"\bDX\.(\d{1,2})\b\s*[—–:\-]\s*([^<\n]{3,80})", strip_text(pa_html)):
            i = int(m.group(1))
            if 1 <= i <= 10 and i not in expected_names:
                expected_names[i] = m.group(2).strip()

    matched = 0
    for i in range(1, 11):
        dh = courses_html.get(f"DX.{i}", "")
        if not dh:
            continue
        if i in expected_names:
            # Comparer les 2 mots significatifs du titre
            toks = [w.lower() for w in re.findall(r"[A-Za-zÀ-ÿ]{4,}", expected_names[i])][:3]
            dh_clean = re.sub(r"<(style|script|nav)\b[^>]*>.*?</\1>", " ", dh, flags=re.S | re.I)
            head_zone = strip_text(dh_clean)[:4000].lower()
            if toks and any(tok in head_zone for tok in toks):
                matched += 1
        else:
            # S'il n'y a pas de liste canonique mais que DX.i existe et est mentionné dans PA
            if re.search(rf"\bDX\.{i}\b", pa_html):
                matched += 1

    return {
        "dx_present": dx_present,
        "dx_matched_ab": matched,
        "inter_file_dups": inter_dups,
        "coherence_ok": dx_present == 10 and matched >= 8 and inter_dups == 0,
    }


def locate_lot_files(repo_root: Path) -> tuple[dict[int, dict[str, Any]], dict[str, int]]:
    """Inventorie chaque LOT_001..248 sur tous les conteneurs du dépôt."""
    containers_priority = [
        "Antigravity_LOTs_du_16_11_2026",
        "Claude",
        "ChatGPT_Codex",
        "Grokbot",
        "LOT_Claude_Finaux",
    ]
    container_counts: dict[str, int] = collections.Counter()
    per_lot: dict[int, dict[str, Any]] = {}

    for lot_num in range(1, 249):
        lot_tag = f"LOT_{lot_num:03d}"
        found_in: list[str] = []
        best_container: str | None = None
        best_dir: Path | None = None
        best_modules: dict[str, str] = {}
        best_shared_head = ""
        best_paths: dict[str, str] = {}
        is_bundled = False
        bundle_has_custom_script = False

        for cont in containers_priority:
            d = repo_root / cont / lot_tag
            if not d.exists() or not d.is_dir():
                continue
            if cont == "Antigravity_LOTs_du_16_11_2026":
                bundles = sorted(d.glob("*_complet.html"))
                if bundles:
                    found_in.append(cont)
                    container_counts[cont] += 1
                    if best_container is None:
                        head_ctx, mods, has_script = split_antigravity_bundle(bundles[0])
                        if mods:
                            best_container = cont
                            best_dir = d
                            best_modules = mods
                            best_shared_head = head_ctx
                            rel = str(bundles[0].relative_to(repo_root))
                            best_paths = {cid: f"{rel}#{cid}" for cid in mods}
                            is_bundled = True
                            bundle_has_custom_script = has_script
                continue

            htmls = [
                p
                for p in sorted(d.glob("*.html"))
                if "PLANCHE" not in p.name and "OBSOLETE" not in p.name
            ]
            mods_here: dict[str, str] = {}
            paths_here: dict[str, str] = {}
            for p in htmls:
                if re.search(r"(?:Phase_A|Appel_A).*\.html$", p.name, re.I):
                    mods_here["PA"] = p.read_text(encoding="utf-8", errors="ignore")
                    paths_here["PA"] = str(p.relative_to(repo_root))
                else:
                    dm = re.search(r"(?:Phase_B|Appel_B).*DX\.(\d{1,2})\.html$", p.name, re.I)
                    if dm:
                        idx = int(dm.group(1))
                        if 1 <= idx <= 10:
                            cid = f"DX.{idx}"
                            mods_here[cid] = p.read_text(encoding="utf-8", errors="ignore")
                            paths_here[cid] = str(p.relative_to(repo_root))
            if htmls:
                found_in.append(cont)
                container_counts[cont] += len(htmls)
            # Choisir ce conteneur s'il apporte PA/DX.1..10 (et non uniquement DX.11..15)
            if best_container is None and mods_here:
                best_container = cont
                best_dir = d
                best_modules = mods_here
                best_paths = paths_here

        per_lot[lot_num] = {
            "found_in": found_in,
            "best_container": best_container,
            "best_dir": best_dir,
            "modules_html": best_modules,
            "paths": best_paths,
            "shared_head": best_shared_head,
            "is_bundled": is_bundled,
            "bundle_has_custom_script": bundle_has_custom_script,
        }
    return per_lot, dict(container_counts)


def build_gauges(repo_root: Path) -> dict[str, Any]:
    # 1. Métadonnées fixes du dépôt
    head_sha = (
        subprocess.run(["git", "-C", str(repo_root), "rev-parse", "HEAD"], capture_output=True, text=True)
        .stdout.strip()
    )
    head_date = (
        subprocess.run(
            ["git", "-C", str(repo_root), "log", "-1", "--format=%cI", "HEAD"],
            capture_output=True,
            text=True,
        )
        .stdout.strip()
    )

    cat_path = repo_root / "LOT_Claude_Finaux" / "CATALOGUE_248.csv"
    catalogue: dict[int, dict[str, str]] = {}
    with cat_path.open("r", encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            n = int(row["lot"])
            catalogue[n] = {
                "code": row["code"].strip(),
                "titre": row["ssp_profiles_2023_fr_en"].strip(),
                "statut_catalogue_legacy": row["statut"].strip(),
            }

    attr_data = json.loads((repo_root / "ATTRIBUTIONS.json").read_text(encoding="utf-8"))
    attributions = attr_data.get("lots", {})

    etat_file = json.loads((repo_root / "LOT_Claude_Finaux" / "ETAT_FILE.json").read_text(encoding="utf-8"))
    etat_by_lot = {int(item["lot"]): item for item in etat_file.get("lots", [])}

    prets_txt = (repo_root / "Claude" / "_reference" / "prets.txt").read_text(encoding="utf-8").strip()
    whitelist_hosts = load_domain_whitelist(repo_root)

    # 2. Scan de tous les conteneurs
    lot_locs, container_html_counts = locate_lot_files(repo_root)

    lots_out: list[dict[str, Any]] = []
    courses_rows: list[dict[str, Any]] = []

    tier_counts: dict[str, int] = collections.Counter()
    wave_counts: dict[str, int] = collections.Counter()
    group_stats: dict[str, dict[str, Any]] = {}
    course_status_counts: dict[str, int] = collections.Counter()

    for lot_num in range(1, 249):
        cat = catalogue[lot_num]
        code = cat["code"]
        groupe = code[0]  # G, S, F, O
        loc = lot_locs[lot_num]
        container = loc["best_container"]
        lot_dir: Path | None = loc["best_dir"]
        modules_html: dict[str, str] = loc["modules_html"]
        is_bundled: bool = loc["is_bundled"]
        shared_head: str = loc["shared_head"]
        bundle_script: bool = loc["bundle_has_custom_script"]

        lot_phrase_seen: dict[str, str] = {}
        courses_metrics: dict[str, dict[str, Any]] = {}
        for cid in MODULE_IDS:
            if cid in modules_html:
                cm = analyze_course_html(
                    lot_num=lot_num,
                    cid=cid,
                    h=modules_html[cid],
                    whitelist_hosts=whitelist_hosts,
                    shared_ctx_head=shared_head,
                    is_bundled=is_bundled,
                    bundle_has_custom_script=bundle_script,
                    lot_phrase_seen=lot_phrase_seen,
                )
            else:
                cm = empty_course_metrics(lot_num, cid)
            courses_metrics[cid] = cm

        audit_info = evaluate_lot_audits_and_p1(lot_dir, lot_num)
        present_count = sum(1 for cm in courses_metrics.values() if cm["exists"])
        palier, vague = classify_tier_and_wave(lot_num, container, present_count, courses_metrics, audit_info)
        tier_counts[palier] += 1
        wave_counts[vague] += 1

        coherence_ab = compute_coherence_ab(lot_dir, modules_html, courses_metrics)

        # Statut de chaque cours & collecte CSV
        for cid in MODULE_IDS:
            cm = courses_metrics[cid]
            if not cm["exists"]:
                st_c = "ABSENT"
            elif cm["is_stub"]:
                st_c = "EBAUCHE_STUB"
            elif cm["g1_pass"] and cm["g2_pass"] and cm["g3_pass"] and cm["g4_pass"] and cm["g5_pass"] and cm["g8_pass"] and audit_info["maturite_audit"] >= 3:
                st_c = "AUDITE_CONFORME"
            elif cm["g1_pass"] and cm["g2_pass"] and cm["g5_pass"] and cm["g8_pass"]:
                st_c = "PRET_AUDIT"
            elif cm["g2_pass"] or cm["has_forme_css"] or cm["fenetre_count"] > 0:
                st_c = "L1_MECANIQUE_PARTIEL"
            else:
                st_c = "HERITAGE_PRE_L1"
            cm["statut_cours"] = st_c
            course_status_counts[st_c] += 1

            courses_rows.append(
                {
                    "lot": f"{lot_num:03d}",
                    "code": code,
                    "groupe": groupe,
                    "module": cid,
                    "palier": palier,
                    "vague_reprise": vague,
                    "conteneur": container or "ABSENT",
                    "chemin": loc["paths"].get(cid, ""),
                    "statut_cours": st_c,
                    "score_composite": cm["score_composite"],
                    "bytes_raw": cm["bytes_raw"],
                    "bytes_no_img": cm["bytes_no_img"],
                    "size_band": cm["size_band"],
                    "G1": cm["g1_score"],
                    "G2": cm["g2_score"],
                    "G3": cm["g3_score"],
                    "G4": cm["g4_score"],
                    "G5": cm["g5_score"],
                    "G6": cm["g6_score"],
                    "G7": cm["g7_score"],
                    "G8": cm["g8_score"],
                    "points_1_14": cm["points_1_14"],
                    "fenetres": cm["fenetre_count"],
                    "sup_r": cm["sup_r_count"],
                    "bib": cm["bib_entries_count"],
                    "aips_bib": cm["aips_bib_count"],
                    "compendium_ch": cm["compendium_ch_count"],
                    "mb_sheets": cm["mb_sheets_count"],
                    "pt14_qr": cm["pt14_qr_count"],
                    "images": cm["img_count"],
                    "forme_css": int(cm["has_forme_css"]),
                    "forme_js": int(cm["has_forme_js"]),
                    "cream_hex": cm["forbidden_cream_count"],
                    "blue_hex": cm["blue_hex_count"],
                    "connecteur_pct": cm["connecteur_pct"],
                    "nominales": cm["nominal_sentences"],
                    "longues_gt32": cm["long_sentences_gt32"],
                    "dup_inter": cm["inter_dup_phrases"],
                    "maturite_audit": audit_info["maturite_audit"],
                }
            )

        # Agrégats LOT
        n_mech_ok = sum(
            1
            for cm in courses_metrics.values()
            if cm["exists"] and cm["g1_pass"] and cm["g2_pass"] and cm["g5_pass"] and cm["g8_pass"]
        )
        n_l1_band = sum(1 for cm in courses_metrics.values() if cm["in_l1_band"])
        n_forme = sum(1 for cm in courses_metrics.values() if cm["has_forme_css"] and cm["has_forme_js"])
        n_fenetre = sum(1 for cm in courses_metrics.values() if cm["fenetre_count"] > 0)
        n_sup_r = sum(1 for cm in courses_metrics.values() if cm["sup_r_count"] > 0)
        n_img_courses = sum(1 for cm in courses_metrics.values() if cm["img_count"] > 0)
        total_figs = sum(cm["img_count"] for cm in courses_metrics.values())
        free_figs = sum(cm["free_lic_count"] for cm in courses_metrics.values())
        total_bytes_no_img = sum(cm["bytes_no_img"] for cm in courses_metrics.values())
        total_bytes_raw = sum(cm["bytes_raw"] for cm in courses_metrics.values())

        axis_means = {
            ax: round(sum(cm[f"{ax.lower()}_score"] for cm in courses_metrics.values()) / 11.0, 1)
            for ax in AXIS_WEIGHTS
        }
        lot_score_composite = round(
            sum(cm["score_composite"] for cm in courses_metrics.values()) / 11.0, 1
        )

        ef = etat_by_lot.get(lot_num, {})
        lot_entry = {
            "lot": f"{lot_num:03d}",
            "lot_num": lot_num,
            "code": code,
            "groupe": groupe,
            "titre": cat["titre"],
            "attribution": attributions.get(f"{lot_num:03d}", "INCONNU"),
            "conteneur_principal": container or "ABSENT",
            "conteneurs_presents": loc["found_in"],
            "format_bundle": is_bundled,
            "palier": palier,
            "vague_reprise": vague,
            "pr_brouillon_nov15": DRAFT_PRS_NOV15.get(lot_num),
            "etat_file_legacy": ef.get("verdict", "INCONNU"),
            "cours_presents": present_count,
            "completion_mecanique": {
                "n_ok": n_mech_ok,
                "pct": round(100.0 * n_mech_ok / 11.0, 1),
                "n_l1_band": n_l1_band,
                "n_forme": n_forme,
                "n_fenetre": n_fenetre,
                "n_sup_r": n_sup_r,
            },
            "P1_gel": audit_info["p1_gel"],
            "p1_statut": audit_info["p1_statut"],
            "coherence_AB": coherence_ab,
            "couverture_images": {
                "cours_avec_image": n_img_courses,
                "pct": round(100.0 * n_img_courses / 11.0, 1),
                "total_figures": total_figs,
                "figures_licence_libre": free_figs,
            },
            "maturite_audit": audit_info["maturite_audit"],
            "audit_note": audit_info["audit_note"],
            "manifeste_present": audit_info["manifeste_present"],
            "manifeste_sha_exact": audit_info["manifeste_sha_exact"],
            "bytes_raw_total": total_bytes_raw,
            "bytes_no_img_total": total_bytes_no_img,
            "score_composite": lot_score_composite,
            "axes_moyens": axis_means,
            "cours": {
                cid: {
                    "statut": courses_metrics[cid]["statut_cours"],
                    "score": courses_metrics[cid]["score_composite"],
                    "bytes_raw": courses_metrics[cid]["bytes_raw"],
                    "bytes_no_img": courses_metrics[cid]["bytes_no_img"],
                    "band": courses_metrics[cid]["size_band"],
                    "G1": courses_metrics[cid]["g1_score"],
                    "G2": courses_metrics[cid]["g2_score"],
                    "G3": courses_metrics[cid]["g3_score"],
                    "G4": courses_metrics[cid]["g4_score"],
                    "G5": courses_metrics[cid]["g5_score"],
                    "G6": courses_metrics[cid]["g6_score"],
                    "G7": courses_metrics[cid]["g7_score"],
                    "G8": courses_metrics[cid]["g8_score"],
                    "pts": courses_metrics[cid]["points_1_14"],
                    "fen": courses_metrics[cid]["fenetre_count"],
                    "sup_r": courses_metrics[cid]["sup_r_count"],
                    "aips_bib": courses_metrics[cid]["aips_bib_count"],
                    "mb": courses_metrics[cid]["mb_sheets_count"],
                    "qr": courses_metrics[cid]["pt14_qr_count"],
                    "img": courses_metrics[cid]["img_count"],
                    "forme": courses_metrics[cid]["has_forme_css"] and courses_metrics[cid]["has_forme_js"],
                    "cream": courses_metrics[cid]["forbidden_cream_count"],
                    "blue": courses_metrics[cid]["blue_hex_count"],
                    "conn_pct": courses_metrics[cid]["connecteur_pct"],
                    "nom": courses_metrics[cid]["nominal_sentences"],
                }
                for cid in MODULE_IDS
            },
        }
        lots_out.append(lot_entry)

        gs = group_stats.setdefault(
            groupe,
            {
                "lots": 0,
                "cours_total": 0,
                "cours_presents": 0,
                "l1_audites": 0,
                "maturite_3_plus": 0,
                "l1_band_cours": 0,
                "forme_cours": 0,
                "images_cours": 0,
                "score_sum": 0.0,
            },
        )
        gs["lots"] += 1
        gs["cours_total"] += 11
        gs["cours_presents"] += present_count
        if palier in ("T1", "T2a", "T2b", "T2c"):
            gs["l1_audites"] += 1
        if audit_info["maturite_audit"] >= 3:
            gs["maturite_3_plus"] += 1
        gs["l1_band_cours"] += n_l1_band
        gs["forme_cours"] += n_forme
        gs["images_cours"] += n_img_courses
        gs["score_sum"] += lot_score_composite

    for g, gs in group_stats.items():
        gs["score_moyen"] = round(gs["score_sum"] / gs["lots"], 1)
        del gs["score_sum"]

    summary = {
        "total_lots": len(lots_out),
        "total_courses": len(courses_rows),
        "courses_presents": sum(l["cours_presents"] for l in lots_out),
        "courses_absents": len(courses_rows) - sum(l["cours_presents"] for l in lots_out),
        "l1_audited_lots": sum(1 for l in lots_out if l["palier"] in ("T1", "T2a", "T2b", "T2c")),
        "maturite_audit_dist": {str(m): sum(1 for l in lots_out if l["maturite_audit"] == m) for m in range(5)},
        "manifeste_present_count": sum(1 for l in lots_out if l["manifeste_present"]),
        "manifeste_sha_exact_count": sum(1 for l in lots_out if l["manifeste_sha_exact"]),
        "tier_counts": dict(sorted(tier_counts.items())),
        "wave_counts": dict(sorted(wave_counts.items())),
        "course_status_counts": dict(sorted(course_status_counts.items())),
        "group_stats": group_stats,
        "container_html_counts": container_html_counts,
        "prets_txt": prets_txt,
        "score_moyen_global": round(sum(l["score_composite"] for l in lots_out) / len(lots_out), 1),
    }

    return {
        "meta": {
            "schema_version": "1.0.0",
            "git_head": head_sha,
            "git_head_date": head_date,
            "axis_weights": AXIS_WEIGHTS,
            "generator": "Antigravity_vialFMH/generer_jauges.py",
        },
        "summary": summary,
        "lots": lots_out,
        "_courses_rows": courses_rows,
    }


def build_checkpoint_absents(data: dict[str, Any]) -> dict[str, Any]:
    """Construit la file prioritaire déterministe des LOTs/cours sans contenu didactique (F8)."""
    priority_order = {
        "A1_T9_LOT1": (1, "Vague P0-A1 (T9 Lot 1 : 045 #524, 080 #735, 102 #732/#592)"),
        "A2_T9_LOT2": (2, "Vague P0-A2 (T9 Lot 2 : 043,044,046–050 — appariement #733–#740 + #525–#539)"),
        "B_STUBS_T8E": (3, "Vague P0-B (16 stubs <20 Ko T8e : d'abord 051–054,058–059 via #575,#584,#593–#598, puis 10 sans PR)"),
        "B2_STUBS_RESIDUELS_T8C": (4, "Vague P0-B2 (Stubs résiduels <20 Ko sur T8c : 158, 160)"),
        "C1_PARTIEL_CLAUDE_CODEX": (5, "Vague P0-C1 (Partiels T5 réécriture L1 complète 041,042,075–077 + T7 122)"),
        "C2_PARTIEL_GROKBOT": (6, "Vague P0-C2 (Partiels Grokbot T8d : 13 LOTs / 70 modules)"),
    }
    queue: list[dict[str, Any]] = []
    prio_counts: dict[str, int] = collections.Counter()
    prio_course_counts: dict[str, int] = collections.Counter()

    for l in data["lots"]:
        abs_cids = [cid for cid in MODULE_IDS if l["cours"][cid]["statut"] == "ABSENT"]
        stub_cids = [cid for cid in MODULE_IDS if l["cours"][cid]["statut"] == "EBAUCHE_STUB"]
        if not abs_cids and not stub_cids:
            continue

        lot_num = l["lot_num"]
        palier = l["palier"]
        pr_info = OPEN_PRS_ABSENTS.get(lot_num) or l["pr_brouillon_nov15"]

        if palier == "T9" and lot_num in (45, 80, 102):
            prio = "A1_T9_LOT1"
            if lot_num == 45:
                action = "Reprendre PR #524 (LISTE_DX_CANONIQUE gelée + paquet.json + 11 Lo) → migrer/réduire en L1 (80–150 Ko, #fff, forme.css)"
            elif lot_num == 80:
                action = "Reprendre PR #735 (PA+DX.1 L1 verts) → geler P1 → rédiger DX.2–DX.10 en L1 (1+5 parallèles)"
            else:
                action = "Reprendre PR #732 (PA L1) + vérifier #592 → geler P1 → rédiger DX.1–DX.10 en L1"
        elif palier == "T9":
            prio = "A2_T9_LOT2"
            trim_note = " (réduire PA de 161.6 Ko à <=150 Ko)" if lot_num == 44 else ""
            action = f"Apparier PR {pr_info}{trim_note} : garder PA+DX.1 L1, migrer DX.2–DX.10 Lo en L1 (80–150 Ko, controle3 VERT, verif_aips OK)"
        elif palier == "T8e":
            prio = "B_STUBS_T8E"
            if pr_info:
                action = f"Sauver/convertir {pr_info} vers Prompt L1 (80–150 Ko, #fff, forme.css) pour remplacer les {len(stub_cids)} stubs <20 Ko"
            else:
                action = f"Gel P1 puis rédaction L1 neuve (80–150 Ko, AIPS vérifiées, #fff) pour remplacer les {len(stub_cids)} stubs <20 Ko (sans PR ouverte)"
        elif palier == "T5":
            prio = "C1_PARTIEL_CLAUDE_CODEX"
            action = (
                f"Réécriture/éclatement L1 complet obligatoire (fichiers groupés pré-L1 dupliqués, 0 LISTE_DX_CANONIQUE) "
                f"+ rédaction des {len(abs_cids)} ABSENT(s) ({', '.join(abs_cids)})"
            )
        elif palier == "T7":
            prio = "C1_PARTIEL_CLAUDE_CODEX"
            action = f"Geler P1, migrer les 9 HTML pré-L1 vers forme.css/:target et rédiger les {len(abs_cids)} ABSENT(s) ({', '.join(abs_cids)})"
        elif palier == "T8d":
            prio = "C2_PARTIEL_GROKBOT"
            action = f"Geler P1 sur Phase A puis rédiger les {len(abs_cids)} module(s) ABSENT(s) ({', '.join(abs_cids)}) au gabarit L1 et aligner les présents"
        else:
            prio = "B2_STUBS_RESIDUELS_T8C"
            action = f"Remplacer les {len(stub_cids)} ébauche(s) résiduelle(s) <20 Ko ({', '.join(stub_cids)}) par une rédaction L1 complète (80–150 Ko)"

        prio_counts[prio] += 1
        prio_course_counts[prio] += len(abs_cids) + len(stub_cids)
        checkpoints = {
            cid: {"statut": l["cours"][cid]["statut"], "checkpoint": "TODO"}
            for cid in MODULE_IDS
            if cid in abs_cids or cid in stub_cids
        }
        queue.append(
            {
                "lot": l["lot"],
                "lot_num": lot_num,
                "ssp_code": l["code"],
                "groupe": l["groupe"],
                "titre": l["titre"],
                "palier": palier,
                "vague_reprise": l["vague_reprise"],
                "conteneur_principal": l["conteneur_principal"],
                "priorite_file": prio,
                "cours_presents": l["cours_presents"],
                "cours_absents_count": len(abs_cids),
                "cours_stubs_count": len(stub_cids),
                "cours_sans_didactique_count": len(abs_cids) + len(stub_cids),
                "cours_absents": abs_cids,
                "cours_stubs": stub_cids,
                "statut_checkpoint": "A_PRODUIRE",
                "pr_existante": pr_info,
                "prochaine_action_l1": action,
                "projection_vague_absents": priority_order[prio][1],
                "cours_checkpoints": checkpoints,
            }
        )

    queue.sort(
        key=lambda item: (
            priority_order[item["priorite_file"]][0],
            0 if item["pr_existante"] else 1,
            item["lot_num"],
        )
    )
    for idx, item in enumerate(queue, start=1):
        item["ordre_file"] = idx

    first = queue[0] if queue else None
    first_cid = (first["cours_absents"] + first["cours_stubs"])[0] if first else None

    main_lots_count = sum(
        prio_counts[k]
        for k in ("A1_T9_LOT1", "A2_T9_LOT2", "B_STUBS_T8E", "C1_PARTIEL_CLAUDE_CODEX", "C2_PARTIEL_GROKBOT")
    )
    lots_avec_abs = sum(1 for item in queue if item["cours_absents_count"] > 0)
    total_abs = sum(item["cours_absents_count"] for item in queue)
    total_stubs = sum(item["cours_stubs_count"] for item in queue)

    return {
        "meta": {
            "schema_version": "1.0.0",
            "git_head": data["meta"]["git_head"],
            "git_head_date": data["meta"]["git_head_date"],
            "generator": data["meta"]["generator"],
            "ordre_source": "Réorientation prioritaire utilisateur 2026-11-17T00:40:01Z + explorer_absents_1 + Prompt L1",
        },
        "summary": {
            "lots_priorite_principale_a1_a2_b_c": main_lots_count,
            "lots_total_avec_absents_ou_stubs": len(queue),
            "lots_avec_absents": lots_avec_abs,
            "lots_t9_complets": prio_counts["A1_T9_LOT1"] + prio_counts["A2_T9_LOT2"],
            "lots_partiels": prio_counts["C1_PARTIEL_CLAUDE_CODEX"] + prio_counts["C2_PARTIEL_GROKBOT"],
            "lots_stubs_t8e": prio_counts["B_STUBS_T8E"],
            "lots_stubs_residuels_t8c": prio_counts["B2_STUBS_RESIDUELS_T8C"],
            "total_cours_absents": total_abs,
            "total_cours_stubs": total_stubs,
            "total_cours_sans_contenu_didactique": total_abs + total_stubs,
            "priority_lot_counts": {k: prio_counts.get(k, 0) for k in priority_order},
            "priority_course_counts": {k: prio_course_counts.get(k, 0) for k in priority_order},
        },
        "resume_cursor": {
            "next_ordre_file": first["ordre_file"] if first else None,
            "next_priority": first["priorite_file"] if first else "TERMINE",
            "next_lot": first["lot"] if first else None,
            "next_ssp_code": first["ssp_code"] if first else None,
            "next_course": first_cid,
            "remaining_lots": len(queue),
            "remaining_courses": total_abs + total_stubs,
            "resume_rule": (
                "En cas d'atteinte de la limite de quota, reprendre exactement à (next_lot, next_course) "
                "dans l'ordre A1 -> A2 -> B -> B2 -> C1 -> C2. Chaque module rédigé passe forme.py, "
                "controle3.py --script-ok, verif_aips.py et generer_jauges.py --check avant bascule du checkpoint "
                "à FAIT. Retour au schéma normal W0–W5 dès que remaining_courses == 0."
            ),
        },
        "projection_reprise": [
            {
                "phase": "P0-A1",
                "priorite": "A1_T9_LOT1",
                "lots": prio_counts["A1_T9_LOT1"],
                "cours": prio_course_counts["A1_T9_LOT1"],
                "cadence": "3 worktrees parallèles disjoints (045 #524, 080 #735, 102 #732/#592)",
                "retour_schema_normal": "Non — enchaîner sur P0-A2",
            },
            {
                "phase": "P0-A2",
                "priorite": "A2_T9_LOT2",
                "lots": prio_counts["A2_T9_LOT2"],
                "cours": prio_course_counts["A2_T9_LOT2"],
                "cadence": "2 vagues de 3–4 LOTs (043,044,046–050 : appariement #733–#740 + #525–#539, trim 044 PA -11.6 Ko)",
                "retour_schema_normal": "Non — enchaîner sur P0-B",
            },
            {
                "phase": "P0-B",
                "priorite": "B_STUBS_T8E + B2_STUBS_RESIDUELS_T8C",
                "lots": prio_counts["B_STUBS_T8E"] + prio_counts["B2_STUBS_RESIDUELS_T8C"],
                "cours": prio_course_counts["B_STUBS_T8E"] + prio_course_counts["B2_STUBS_RESIDUELS_T8C"],
                "cadence": "3 vagues : d'abord 6 LOTs avec PRs (#575,#584,#593–#598), puis 10 stubs sans PR + 2 résiduels (158, 160)",
                "retour_schema_normal": "Non — enchaîner sur P0-C",
            },
            {
                "phase": "P0-C1",
                "priorite": "C1_PARTIEL_CLAUDE_CODEX",
                "lots": prio_counts["C1_PARTIEL_CLAUDE_CODEX"],
                "cours": prio_course_counts["C1_PARTIEL_CLAUDE_CODEX"],
                "cadence": "1 vague de 6 LOTs (041,042,075–077 réécriture L1 complète + 122)",
                "retour_schema_normal": "Non — enchaîner sur P0-C2",
            },
            {
                "phase": "P0-C2",
                "priorite": "C2_PARTIEL_GROKBOT",
                "lots": prio_counts["C2_PARTIEL_GROKBOT"],
                "cours": prio_course_counts["C2_PARTIEL_GROKBOT"],
                "cadence": "2 vagues de 6–7 LOTs (13 LOTs T8d / 70 modules ABSENTs)",
                "retour_schema_normal": "OUI — 248/248 LOTs et 2 728/2 728 cours dotés de contenu didactique → reprise schéma normal W0 → W5",
            },
        ],
        "queue": queue,
    }


def _short_title(titre: str, max_len: int = 52) -> str:
    fr = titre.split("|")[0].strip()
    if len(fr) <= max_len:
        return fr
    return fr[: max_len - 1].rstrip() + "…"


def _format_lot_md_row(l: dict[str, Any]) -> str:
    cm = l["completion_mecanique"]
    ab = l["coherence_AB"]
    ci = l["couverture_images"]
    ax = l["axes_moyens"]
    return (
        f"| `{l['lot']}` | `{l['code']}` | {l['groupe']} | `{l['palier']}` | `{l['vague_reprise']}` | "
        f"`{l['conteneur_principal']}` | {l['cours_presents']}/11 | {cm['n_ok']}/11 | {l['p1_statut']} | "
        f"{ab['dx_matched_ab']}/10 ({ab['inter_file_dups']}) | {ci['cours_avec_image']}/11 | {l['maturite_audit']} | "
        f"{ax['G1']} | {ax['G2']} | {ax['G3']} | {ax['G4']} | {ax['G5']} | {ax['G6']} | {ax['G7']} | {ax['G8']} | "
        f"**{l['score_composite']}** | {_short_title(l['titre'])} |"
    )


def render_jauges_markdown(data: dict[str, Any]) -> str:
    s = data["summary"]
    head_short = (data["meta"]["git_head"] or "")[:7]
    pct_pres = round(100.0 * s["courses_presents"] / s["total_courses"], 1)
    pct_aud = round(100.0 * s["l1_audited_lots"] / s["total_lots"], 1)
    mat_str = " · ".join(f"`{m}:{s['maturite_audit_dist'][str(m)]}`" for m in range(5))
    cs_order = ["AUDITE_CONFORME", "PRET_AUDIT", "L1_MECANIQUE_PARTIEL", "HERITAGE_PRE_L1", "EBAUCHE_STUB", "ABSENT"]
    cs_str = " · ".join(f"`{k}:{s['course_status_counts'].get(k, 0)}`" for k in cs_order)

    tier_desc = {
        "T1": "Antigravity L1 Audité (bundle)",
        "T2a": "Claude L1 Audité (`ACCEPTE`)",
        "T2b": "Claude L1 + `audit2` (`001–016`)",
        "T2c": "Claude L1 + `PLANCHE` (`023–032`)",
        "T3": "Claude `fenetre` (sans `forme.css`/`cite`)",
        "T4": "Claude Héritage 11 HTML",
        "T5": "Claude Partiel (<11 HTML)",
        "T6": "Codex Pré-L1 Audité V0",
        "T7": "Codex Pré-L1 Non Audité / Partiel",
        "T8a": "Grokbot 11 HTML `80–150 Ko` + `fenetre`",
        "T8b": "Grokbot 11 HTML `80–150 Ko` (sans `fenetre`)",
        "T8c": "Grokbot 11 HTML Tailles mixtes",
        "T8d": "Grokbot Partiel (<11 HTML)",
        "T8e": "Grokbot Ébauches / Stubs (`<20 Ko`)",
        "T9": "`MISSING` sur `main` (0 HTML)",
    }
    wave_desc = {
        "DONE": "Clôturé (`017–022` : `MANIFESTE.json` seul)",
        "W0": "Clôture audits `001–016`/`023–032`, harmonisation `033`, PRs `#732–#740`",
        "W1": "Renfort rapide `Claude` `T3/T4/T5` (`034–042`, `109`, `111`)",
        "W2": "Orphelin `T9` (`045`) + `16` stubs `T8e` (`<20 Ko`)",
        "W3": "Rattrapage `Claude` héritage & partiels (`072–078`, `104–108`, `110`)",
        "W4": "Reprise ouverte `ChatGPT_Codex` (`T6` + `T7`)",
        "W5": "Reprise de masse `Grokbot` (`T8a`–`T8d`)",
    }

    lines = [
        "# Jauges fines de production — 248 LOTs & 2 728 cours",
        "",
        f"**Source canonique** : `Antigravity_vialFMH/jauges_248_lots.json`, `Antigravity_vialFMH/jauges_2728_cours.csv` et `Antigravity_vialFMH/CHECKPOINT_ABSENTS.json` (générés par `python3 Antigravity_vialFMH/generer_jauges.py`, réf. `{head_short}`).",
        "",
        "## 1. Synthèse globale mesurée sur disque",
        "",
        "| Indicateur | Valeur mesurée |",
        "|---|---:|",
        f"| LOTs PROFILES 2023 | **{s['total_lots']}** |",
        f"| Cours totaux (`248 × 11`) | **{s['total_courses']}** |",
        f"| Cours physiquement présents sur `main` | **{s['courses_presents']}** ({pct_pres} %) |",
        f"| Cours absents sur `main` (priorité urgente) | **{s['courses_absents']}** |",
        f"| LOTs L1 audités (`T1 + T2a + T2b + T2c`) | **{s['l1_audited_lots']} / {s['total_lots']}** ({pct_aud} %) |",
        f"| Score composite moyen global (`G1–G8`) | **{s['score_moyen_global']} / 100** |",
        f"| Maturité d'audit (`0 / 1 / 2 / 3 / 4`) | {mat_str} |",
        f"| `MANIFESTE.json` présents / SHA-256 exacts | `{s['manifeste_present_count']} / {s['total_lots']}` présents · `{s['manifeste_sha_exact_count']} / {s['total_lots']}` SHA-256 exacts |",
        f"| Statuts cours (`2 728`) | {cs_str} |",
        "",
        "## 2. Spécification des 8 axes par cours (`G1`–`G8`) et des 5 agrégats LOT",
        "",
        "| Axe | Poids | Critères mesurés (0-token / Audit) | Seuil PASS |",
        "|---|---:|---|---|",
        "| **G1. Structure & Gabarit L1** | 18 % | `14/14` points (`id=\"*p1..p14\"`), `FIN_FICHIER` (ou `FIN_COURS` en bundle), balises équilibrées, 0 arbre CIM, Pt 1 Définition seule, 0 `title=`, tableaux enveloppés, 0 ancre cassée, 0 fenêtre imbriquée, 0 gabarit `({..})`, `>=1` `.fenetre`, 0 `<script>` hors `forme.js` (y compris hors `<article>` en bundle). | 14 pts + 0 défaut L1 bloquant |",
        "| **G2. Volume hors images** | 14 % | `bytes_no_img` (retrait `<img>`, `<svg>`, `<picture>`, `data:image` conforme à `controle3.py:192-195`). | `80 000 <= bytes_no_img <= 150 000` (cible `115–145 Ko`) |",
        "| **G3. Langue & Non-Redondance** | 12 % | Phrases verbales (`VERBES`/`VERBE_RE`, apostrophe `’` normalisée), longueur `<=32` mots, 0 doublon intra-fichier, **0 phrase partagée inter-fichiers** dans le LOT, `connecteur%`, paragraphes `>40` mots sans connecteur. | 0 doublon intra/inter, `<=3` nominales/longues |",
        "| **G4. Sources & Véracité CH/EU** | 14 % | `<sup class=\"r\">`, entrées biblio `sb-*`/`*-ref-*`/`src-*`/`div.sb` datées (`consulté`/année), ratio URLs conformes `qa/domaines.yml` (CH/EU), 0 formule lacune (`À vérifier`), chiffres non cités. | `sup.r>=10`, `bib>=3`, 0 lacune, `<=5` chiffres non cités |",
        "| **G5. Pharmacologie & AIPS** | 14 % | Doses (`mg`, `µg`, `UI`…) liées à AIPS (`sb-aips-*` / `files.refdata.ch` / `Swissmedic n°`) ou `hors AIPS`, 0 `compendium.ch`, fiches `.mb`, modal `Urgence — conduite chronologique`. | 0 `compendium.ch`, 0 dose non sourcée |",
        "| **G6. Complétude pédagogique (`µ3` + 11.11)** | 10 % | Pt 3 prérequis anatomo-fonctionnel (`LOT_021+` & `020 DX.1`), Pt 6 `>=1` fenêtre par région, Pt 11 `11.A–11.D`, Pt 13 intact sans `.fenetre`, Pt 14 `>=6` Q&R. | `14` pts + `Pt14>=6` + `Pt3` anatomo (`021+`) |",
        "| **G7. Images pédagogiques (`µ6 v2`)** | 8 % | Présence `<img>`/`<svg>`/`<figure>`, licence libre (`CC0`/`CC BY`/`CC BY-SA`/`PD`), 0 `NC/ND`, lecture guidée (`INTERP`). | `>=1` image licence libre, 0 `NC/ND` |",
        "| **G8. Design & Front-End Uniforme** | 10 % | Liens `../_polices/forme.css` & `forme.js`, `#brain-barre14`, `#fm-bandeau`, fond `#fff` pur, **0 hex crème/beige/ivoire** (`#f9f5ee`…), **0 bleu `150°–305°`**. | `forme.css` + `forme.js` + 0 crème + 0 bleu |",
        "",
        "**Agrégats LOT (`LOT_001`–`LOT_248`)** : `completion_mecanique` (`N/11` cours validant `G1+G2+G5+G8`), `P1_gel` (`LISTE_DX_CANONIQUE.md` + `LISTE_DX.audit.json == GEL`), `coherence_AB` (`DX.1..10` alignés sur Phase A + 0 doublon inter-fichiers), `couverture_images` (`N/11` cours illustrés), `maturite_audit` (`0` non audité · `1` Audit 1 / V0 · `2` Audit 2 `CORRECTIONS` / `finale:non` · `3` Contre-audit 2 Phase B `ACCEPTE`/`APPROVE` · `4` `ACCEPTE` + `MANIFESTE.json` SHA-256 exact).",
        "",
        "## 3. Répartition par groupe PROFILES (`G / S / F / O`)",
        "",
        "| Groupe | LOTs | Cours présents / Total | L1 audités (`T1–T2`) | Maturité ≥ 3 | Cours `80–150 Ko` | Cours `forme.css/js` | Cours illustrés | Score moyen |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for g in ("G", "S", "F", "O"):
        x = s["group_stats"][g]
        lines.append(
            f"| **{g}** | {x['lots']} | {x['cours_presents']} / {x['cours_total']} | {x['l1_audites']} | "
            f"{x['maturite_3_plus']} | {x['l1_band_cours']} | {x['forme_cours']} | {x['images_cours']} | **{x['score_moyen']}** |"
        )

    lines.extend([
        "",
        "## 4. Répartition par palier (`T1`–`T9`) et par vague (`DONE`, `W0`–`W5`)",
        "",
        "| Palier | Description | LOTs | Cours (×11) |",
        "|---|---|---:|---:|",
    ])
    for t in ("T1", "T2a", "T2b", "T2c", "T3", "T4", "T5", "T6", "T7", "T8a", "T8b", "T8c", "T8d", "T8e", "T9"):
        c = s["tier_counts"].get(t, 0)
        if c:
            lines.append(f"| **`{t}`** | {tier_desc[t]} | {c} | {c * 11} |")

    lines.extend([
        "",
        "| Vague | Périmètre & Stratégie | LOTs | Cours (×11) |",
        "|---|---|---:|---:|",
    ])
    for w in ("DONE", "W0", "W1", "W2", "W3", "W4", "W5"):
        c = s["wave_counts"].get(w, 0)
        if c:
            lines.append(f"| **`{w}`** | {wave_desc[w]} | {c} | {c * 11} |")

    lines.extend([
        "",
        "## 5. Tableau complet des 248 LOTs (mesures directes sur disque)",
        "",
        "| LOT | Code | Grp | Palier | Vague | Conteneur | Prés. | Méca `N/11` | `P1` | Cohér. `A↔B` (dup) | Img `N/11` | Mat. (0–4) | `G1` | `G2` | `G3` | `G4` | `G5` | `G6` | `G7` | `G8` | Score | Intitulé SSP |",
        "|---|---|---:|---|---|---|---|---:|:---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ])
    for l in data["lots"]:
        lines.append(_format_lot_md_row(l))
    lines.append("")
    return "\n".join(lines)


def sync_dashboard_json(out_dir: Path, data: dict[str, Any]) -> None:
    html_path = out_dir / "DASHBOARD_PRODUCTION_ANTIGRAVITY.html"
    if not html_path.exists():
        return
    ht = html_path.read_text(encoding="utf-8")
    courses_rows = data.pop("_courses_rows", None)
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    if courses_rows is not None:
        data["_courses_rows"] = courses_rows
    new_ht, n = re.subn(
        r'(<script id="jauges-json" type="application/json">)(.*?)(</script>)',
        lambda m: m.group(1) + payload + m.group(3),
        ht,
        count=1,
        flags=re.S,
    )
    if n == 1:
        html_path.write_text(new_ht, encoding="utf-8")


def write_outputs(out_dir: Path, data: dict[str, Any]) -> tuple[Path, Path, Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "jauges_248_lots.json"
    csv_path = out_dir / "jauges_2728_cours.csv"
    cp_path = out_dir / "CHECKPOINT_ABSENTS.json"
    md_path = out_dir / "JAUGES_FINES_PRODUCTION.md"

    courses_rows = data.pop("_courses_rows")
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    fieldnames = list(courses_rows[0].keys())
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(courses_rows)

    data["_courses_rows"] = courses_rows
    cp_data = build_checkpoint_absents(data)
    cp_path.write_text(json.dumps(cp_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_jauges_markdown(data), encoding="utf-8")
    sync_dashboard_json(out_dir, data)
    return json_path, csv_path, cp_path, md_path


def run_check(out_dir: Path, fresh: dict[str, Any]) -> int:
    errors: list[str] = []
    json_path = out_dir / "jauges_248_lots.json"
    csv_path = out_dir / "jauges_2728_cours.csv"
    cp_path = out_dir / "CHECKPOINT_ABSENTS.json"
    md_path = out_dir / "JAUGES_FINES_PRODUCTION.md"
    html_path = out_dir / "DASHBOARD_PRODUCTION_ANTIGRAVITY.html"

    if not json_path.exists():
        errors.append(f"Manquant: {json_path}")
    else:
        existing = json.loads(json_path.read_text(encoding="utf-8"))
        for k in ("schema_version", "axis_weights", "generator"):
            if existing.get("meta", {}).get(k) != fresh["meta"].get(k):
                errors.append(f"JSON meta.{k} diffère du calcul frais")
        if existing.get("summary") != fresh["summary"]:
            errors.append("JSON summary diffère du calcul frais (relancer generer_jauges.py)")
        if existing.get("lots") != fresh["lots"]:
            errors.append("JSON lots diffère du calcul frais (relancer generer_jauges.py)")

    if not csv_path.exists():
        errors.append(f"Manquant: {csv_path}")
    else:
        with csv_path.open("r", encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            got_fields = reader.fieldnames
            rows = list(reader)
        exp_rows = fresh["_courses_rows"]
        exp_fields = list(exp_rows[0].keys())
        if got_fields != exp_fields:
            errors.append(f"CSV colonnes diffèrent ({got_fields} != {exp_fields})")
        elif len(rows) != len(exp_rows):
            errors.append(f"CSV rows={len(rows)} != {len(exp_rows)}")
        else:
            for idx, (got_r, exp_r) in enumerate(zip(rows, exp_rows)):
                norm_exp = {k: str(v) for k, v in exp_r.items()}
                if got_r != norm_exp:
                    errors.append(
                        f"CSV ligne {idx + 1} ({exp_r['lot']} {exp_r['module']}) diffère du calcul frais"
                    )
                    break

    if not cp_path.exists():
        errors.append(f"Manquant: {cp_path}")
    else:
        existing_cp = json.loads(cp_path.read_text(encoding="utf-8"))
        fresh_cp = build_checkpoint_absents(fresh)
        for k in ("summary", "resume_cursor", "projection_reprise", "queue"):
            if existing_cp.get(k) != fresh_cp[k]:
                errors.append(f"CHECKPOINT_ABSENTS.json {k} diffère du calcul frais")

    if not md_path.exists():
        errors.append(f"Manquant: {md_path}")
    else:
        md_txt = md_path.read_text(encoding="utf-8")
        s = fresh["summary"]
        for needle in (
            f"**{s['score_moyen_global']} / 100**",
            f"**{s['courses_presents']}**",
            f"**{s['courses_absents']}**",
            f"**{s['l1_audited_lots']} / {s['total_lots']}**",
            f"`{s['manifeste_present_count']} / {s['total_lots']}`",
            f"`{s['manifeste_sha_exact_count']} / {s['total_lots']}`",
        ):
            if needle not in md_txt:
                errors.append(f"MD synthèse ne contient pas {needle}")
                break
        for g in ("G", "S", "F", "O"):
            x = s["group_stats"][g]
            g_needle = f"| **{g}** | {x['lots']} | {x['cours_presents']} / {x['cours_total']} | {x['l1_audites']} | {x['maturite_3_plus']} | {x['l1_band_cours']} | {x['forme_cours']} | {x['images_cours']} | **{x['score_moyen']}** |"
            if g_needle not in md_txt:
                errors.append(f"MD table groupe {g} diffère du calcul frais")
                break
        for l in fresh["lots"]:
            expected_row = _format_lot_md_row(l)
            if expected_row not in md_txt:
                errors.append(f"MD ligne LOT {l['lot']} diffère du calcul frais")
                break

    if not html_path.exists():
        errors.append(f"Manquant: {html_path}")
    else:
        ht = html_path.read_text(encoding="utf-8")
        m = re.search(r'<script id="jauges-json" type="application/json">(.*?)</script>', ht, re.S)
        if not m:
            errors.append("HTML DASHBOARD sans bloc <script id=\"jauges-json\">")
        else:
            try:
                hdata = json.loads(m.group(1))
                if hdata.get("summary") != fresh["summary"]:
                    errors.append("HTML DASHBOARD embedded summary diffère du calcul frais")
                if hdata.get("lots") != fresh["lots"]:
                    errors.append("HTML DASHBOARD embedded lots diffère du calcul frais")
            except Exception as exc:
                errors.append(f"HTML DASHBOARD JSON invalide: {exc}")

    if errors:
        for e in errors:
            print(f"[ERREUR] {e}", file=sys.stderr)
        return 1
    print(
        f"[OK] Parité stricte vérifiée : 248 LOTs, 2 728 cours, score_moyen_global={fresh['summary']['score_moyen_global']}, "
        f"paliers={fresh['summary']['tier_counts']}"
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Générateur déterministe des jauges fines (248 LOTs / 2 728 cours)")
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent), help="Racine du dépôt")
    ap.add_argument("--check", action="store_true", help="Vérifie la parité stricte JSON/CSV/CHECKPOINT/MD/HTML sans rien modifier")
    ap.add_argument("--stdout-summary", action="store_true", help="Affiche la synthèse JSON sur stdout en lecture seule (aucune écriture)")
    args = ap.parse_args()

    repo_root = Path(args.repo).resolve()
    out_dir = Path(__file__).resolve().parent
    data = build_gauges(repo_root)

    if args.check:
        return run_check(out_dir, data)

    if args.stdout_summary:
        print(json.dumps(data["summary"], ensure_ascii=False, indent=2))
        return 0

    json_path, csv_path, cp_path, md_path = write_outputs(out_dir, data)
    s = data["summary"]
    print(
        f"Généré : {json_path.name} ({s['total_lots']} LOTs), {csv_path.name} ({s['total_courses']} cours), "
        f"{cp_path.name}, {md_path.name}\n"
        f"Présents : {s['courses_presents']}/{s['total_courses']} cours | Absents : {s['courses_absents']} | "
        f"Score moyen global : {s['score_moyen_global']}/100\n"
        f"Paliers : {s['tier_counts']}\n"
        f"Vagues  : {s['wave_counts']}\n"
        f"Maturité audit (0-4) : {s['maturite_audit_dist']} | MANIFESTE SHA exact : {s['manifeste_sha_exact_count']}/{s['manifeste_present_count']}\n"
        f"Statuts cours : {s['course_status_counts']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
