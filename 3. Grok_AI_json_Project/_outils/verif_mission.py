#!/usr/bin/env python3
"""VERIF_MISSION.PY — Contrôle déterministe (0 token) spécifique au cahier des charges 248 SSP.

Vérifie sur un SSP entier (ex: `python _outils/verif_mission.py 248`) ou sur des fichiers HTML donnés :
  1. Calibre texte pur UTF-8 entre 60,0 Ko (61 440 o) et 90,0 Ko (92 160 o), images/balises/CSS/JS exclus.
  2. Présence exacte du bloc <div id="signature-ia"...> juste avant </body>.
  3. Zéro terme de chantier visible dans <title> et le corps visible (LOT, V0, Phase A/B, DX.n, Appel A/B, Partie n).
  4. Zéro image (<img>, <svg>, <picture>, <figure>) en dehors d'une <section class="fenetre">.
  5. Zéro phrase gabarit issue de cartographie_DATA.json (>= 20 occurrences).
  6. Phrases verbales exclusives dans les paragraphes, listes, fenêtres, légendes <figcaption> et cellules <td> narratives (>= 6 mots).
  7. Front-end L1 : forme.css / forme.js, zéro <script> local, zéro title=, zéro popover, fond blanc #ffffff,
     teintes --fm-a hors bleu (150°-305°), ancres résolues, zéro fenêtre imbriquée, FIN_FICHIER présent.
  8. Pour un SSP complet : présence de 1 + N entités dans l'ordre exact de NOTIONS.json, zéro phrase dupliquée entre fichiers,
     couverture des notions réelles (hors phrases gabarit de la cartographie).
"""
from __future__ import annotations

import argparse
import colorsys
import hashlib
import html as H
import json
import os
import re
import sys
import unicodedata

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTO_PATH = os.path.join(BASE, "_outils", "cartographie_DATA.json")
CAT_PATH = os.path.join(BASE, "_outils", "catalogue_248.json")

MIN_PURE = 81_920  # 80.0 Ko — calibre du Prompt Alpha, confirmé par Vial le 2026-11-20 21:20 (30-50 Ko abandonné : cours pauvres)
MAX_PURE = 102_400  # 100.0 Ko

# Signature : validation de FORMAT (toute signature DÉBUT · MODÈLE · PLATEFORME, une ou plusieurs lignes successives)
SIG_LIGNE = r"DÉBUT\s*:\s*\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}\s*\([^)]+\)\s*·\s*MODÈLE\s*:\s*[^·<\r\n]+?\s*·\s*PLATEFORME\s*:\s*[^·<\r\n]+?"
SIG_RE = re.compile(
    r'<div\s+id="signature-ia"[^>]*>\s*(?:<div[^>]*>\s*)?'
    + SIG_LIGNE
    + r'(?:\s*(?:<br\s*/?>|\r?\n|</div>\s*<div[^>]*>)\s*'
    + SIG_LIGNE
    + r')*\s*(?:</div>\s*)?</div>',
    re.I | re.S,
)


def find_signature(h: str):
    """Retourne le dernier match de signature valide, ou None."""
    ms = list(SIG_RE.finditer(h))
    return ms[-1] if ms else None

CHANTIER_RE = re.compile(
    r'\bLOT(?:_\d+|\s+\d+)?\b'
    r'|\bV0\b'
    r'|\bPhase\s+[AB]\b'
    r'|\bDX\.?\s*\d+\b'
    r'|\bAppel(?:\s+[AB])?\b'
    r'|\bPartie\s+\d+\b'
)

VERBES = set("""
propose proposent recommande recommandent conseille conseillent mentionne mentionnent contient contiennent figure figurent
résulte résultent ajoute ajoutent dépend dépendent rassemble rassemblent résume résument précise précisent indique indiquent
décrit décrivent est sont a ont fait font peut peuvent doit doivent reste restent devient deviennent va vont
semble semblent permet permettent signe signent oriente orientent impose imposent confirme confirment élimine éliminent
exclut excluent traite traitent associe associent survient surviennent provoque provoquent entraîne entraînent exige exigent
reçoit reçoivent touche touchent atteint atteignent dépasse dépassent varie varient augmente augmentent diminue diminuent
baisse baissent réduit réduisent favorise favorisent explique expliquent précède précèdent suit suivent recherche recherchent
mesure mesurent montre montrent révèle révèlent définit définissent correspond correspondent comprend comprennent
repose reposent consiste consistent représente représentent constitue constituent nécessite nécessitent justifie justifient
prescrit prescrivent administre administrent contre-indique contre-indiquent évite évitent limite limitent dure durent
persiste persistent apparaît apparaissent disparaît disparaissent évolue évoluent aggrave aggravent protège protègent
prévient préviennent dépiste dépistent détecte détectent distingue distinguent sépare séparent conduit conduisent mène mènent
aboutit aboutissent cause causent déclenche déclenchent libère libèrent active activent inhibe inhibent bloque bloquent
stimule stimulent fixe fixent lie lient agit agissent s'accompagne s'accompagnent s'associe s'associent s'explique s'expliquent
s'élève s'élèvent se manifeste se manifestent se traduit se traduisent se définit se définissent se recherche se recherchent
se mesure se mesurent se prescrit se prescrivent se discute se discutent se pose se posent s'impose s'imposent s'observe s'observent
s'installe s'installent se complique se compliquent remplace remplacent compte comptent atteste attestent rappelle rappellent
signale signalent pose posent écarte écartent retient retiennent ordonne ordonnent adapte adaptent surveille surveillent
contrôle contrôlent corrige corrigent restaure restaurent normalise normalisent prolonge prolongent était étaient avait avaient
sera seront aura auront serait seraient pourrait pourraient devrait devraient faut suffit suffisent vise visent cible ciblent
porte portent concerne concernent relève relèvent interdit interdisent autorise autorisent exige exigent oblige obligent
protège protègent garanit garantit garantissent informe informent consent consentent refuse refusent communique communiquent
transmet transmettent consulte consultent adresse adressent oriente orientent évalue évaluent vérifie vérifient documente documentent
consigne consignent archive archivent protègent prouve prouvent établit établissent distingue distinguent classe classent
reclasse reclassent confirme confirment infirme infirment déclare déclarent notifie notifient réalise réalisent effectue effectuent
prélève prélèvent analyse analysent interprète interprètent confirme confirment compare comparent calcule calculent estime estiment
démontre démontrent prouve prouvent prévaut prévalent dispose disposent existe existent figure figurent provient proviennent
émane émanent constitue constituent recouvre recouvrent réunit réunissent forme forment explique expliquent répond répondent
applique appliquent s'applique s'appliquent utilise utilisent emploie emploient recourt recourent privilégie privilégient
bénéficie bénéficient requiert requièrent assure assurent couvre couvrent rembourse remboursent prend prennent donne donnent
remet remettent garde gardent maintient maintiennent améliore améliorent ralentit ralentissent accélère accélèrent
bloque bloquent dissocie dissocient restaure restaurent prévient préviennent survit survivent décède décèdent meurt meurent
présente présentent abaisse abaissent guide guident demeure demeurent consomme consomment amplifie amplifient abolit abolissent
complète complètent lève lèvent débute débutent illustre illustrent congèle congèlent diffuse diffusent perfore perforent
tue tuent chute chutent menace menacent précipite précipitent décompense décompensent lèse lèsent initie initient apporte apportent
titre titrent proscrit proscrivent maintient maintiennent guette guettent injecte injectent délivre délivrent
adsorbe adsorbent souffre souffrent dévie dévient effondre effondrent élève élèvent note notent palpe palpent constate constatent
rapporte rapportent observe observent tranche tranchent cherche cherchent perfuse perfusent culmine culminent descend descendent
""".split())

VERBE_SUFFIX_RE = re.compile(
    r"\b(?:\w+(?:ent|ait|aient|era|eront|erait|eraient|ise|isent|it|issent))\b",
    re.I,
)
PRONOM_VERBE_RE = re.compile(
    r"\b(?:il|elle|ils|elles|on|qui|cela|ce|celle-ci|celui-ci)\s+(?:ne\s+|n'|se\s+|s'|l'|le\s+|la\s+|les\s+|y\s+|en\s+)*\w+",
    re.I,
)
AUX_PP_RE = re.compile(
    r"\b(?:est|sont|a|ont|fut|furent|été|sera|seront|serait|seraient|doit|doivent|devrait|devraient|peut|peuvent|pourrait|pourraient|faut|suffit|suffisent|vaut|valent|"
    r"permet|permettent|entraîne|entraînent|provoque|provoquent|indique|indiquent|impose|imposent|confirme|confirment|exclut|excluent|élimine|éliminent|"
    r"nécessite|nécessitent|justifie|justifient|prescrit|prescrivent|administre|administrent|recommande|recommandent|interdit|interdisent|exige|exigent|"
    r"protège|protègent|informe|informent|consent|consentent|refuse|refusent|communique|communiquent|évalue|évaluent|vérifie|vérifient|documente|documentent|"
    r"consigne|consignent|distingue|distinguent|constitue|constituent|représente|représentent|comprend|comprennent|repose|reposent|résulte|résultent|"
    r"correspond|correspondent|dépend|dépendent|survient|surviennent|touche|touchent|atteint|atteignent|dépasse|dépassent|varie|varient|augmente|augmentent|"
    r"diminue|diminuent|baisse|baissent|réduit|réduisent|favorise|favorisent|explique|expliquent|précède|précèdent|suit|suivent|recherche|recherchent|"
    r"mesure|mesurent|montre|montrent|révèle|révèlent|définit|définissent|associe|associent|signe|signent|oriente|orientent|évite|évitent|limite|limitent|"
    r"dure|durent|persiste|persistent|apparaît|apparaissent|disparaît|disparaissent|évolue|évoluent|aggrave|aggravent|prévient|préviennent|dépiste|dépistent|"
    r"détecte|détectent|sépare|séparent|conduit|conduisent|mène|mènent|aboutit|aboutissent|cause|causent|déclenche|déclenchent|libère|libèrent|active|activent|"
    r"inhibe|inhibent|bloque|bloquent|stimule|stimulent|fixe|fixent|lie|lient|agit|agissent|remplace|remplacent|compte|comptent|atteste|attestent|rappelle|rappellent|"
    r"signale|signalent|pose|posent|écarte|écartent|retient|retiennent|ordonne|ordonnent|adapte|adaptent|surveille|surveillent|contrôle|contrôlent|corrige|corrigent|"
    r"restaure|restaurent|normalise|normalisent|prolonge|prolongent|vise|visent|cible|ciblent|porte|portent|concerne|concernent|relève|relèvent|autorise|autorisent|"
    r"oblige|obligent|garantit|garantissent|transmet|transmettent|consulte|consultent|adresse|adressent|classe|classent|reclasse|reclassent|déclare|déclarent|"
    r"notifie|notifient|réalise|réalisent|effectue|effectuent|prélève|prélèvent|analyse|analysent|interprète|interprètent|compare|comparent|calcule|calculent|"
    r"estime|estiment|démontre|démontrent|prouve|prouvent|prévaut|prévalent|dispose|disposent|existe|existent|figure|figurent|provient|proviennent|émane|émanent|"
    r"recouvre|recouvrent|réunit|réunissent|forme|forment|répond|répondent|applique|appliquent|utilise|utilisent|emploie|emploient|recourt|recourent|privilégie|privilégient|"
    r"bénéficie|bénéficient|requiert|requièrent|assure|assurent|couvre|couvrent|rembourse|remboursent|prend|prennent|donne|donnent|remet|remettent|garde|gardent|"
    r"maintient|maintiennent|améliore|améliorent|ralentit|ralentissent|accélère|accélèrent|dissocie|dissocient|survit|survivent|décède|décèdent|meurt|meurent|"
    r"contient|contiennent|ajoute|ajoutent|mentionne|mentionnent|conseille|conseillent|précise|précisent|décrit|décrivent|semble|semblent|reste|restent|devient|deviennent|"
    r"va|vont|fait|font|traite|traitent|fournit|fournissent|offre|offrent|crée|créent|génère|génèrent|empêche|empêchent|engage|engagent|suspend|suspendent|reporte|reportent|"
    r"annule|annulent|confie|confient|sollicite|sollicitent|lève|lèvent|archive|archivent|suppose|supposent|implique|impliquent|caractérise|caractérisent|traduit|traduisent|"
    r"manifeste|manifestent|accompagne|accompagnent|installe|installent|complique|compliquent|"
    r"conjugue|conjuguent|débute|débutent|traverse|traversent|exerce|exercent|absorbe|absorbent|métabolise|métabolisent|transforme|transforment|excrète|excrètent|"
    r"concentre|concentrent|accumule|accumulent|dégrade|dégradent|altère|altèrent|induit|induisent|reflète|reflètent|évoque|évoquent|comporte|comportent|inclut|incluent|"
    r"souligne|soulignent|illustre|illustrent|valide|valident|stratifie|stratifient|quantifie|quantifient|identifie|identifient|situe|situent|relie|relient|expose|exposent|"
    r"menace|menacent|modifie|modifient|ajuste|ajustent|interrompt|interrompent|met|mettent|tient|tiennent|vient|viennent|passe|passent|attend|attendent|évacue|évacuent|"
    r"corrèle|corrèlent|discrimine|discriminent|confond|confondent|masque|masquent|retarde|retardent|précipite|précipitent|agisse|agissent|exprime|expriment|déplie|déplient|"
    r"prévoit|prévoient|stipule|stipulent|sanctionne|sanctionnent|encadre|encadrent|délivre|délivrent|reconnaît|reconnaissent|admet|admettent|oppose|opposent|opère|opèrent)\b",
    re.I,
)


def norm(t: str) -> str:
    t = unicodedata.normalize("NFD", (t or "").lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def toks(t: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]{5,}|\d+(?:[.,]\d+)?", norm(t))}


def load_catalogue() -> dict[int, dict]:
    if not os.path.exists(CAT_PATH):
        return {}
    return {x["lot"]: x for x in json.load(open(CAT_PATH, encoding="utf-8"))}


def load_boilerplate() -> set[str]:
    if not os.path.exists(CARTO_PATH):
        return set()
    data = json.load(open(CARTO_PATH, encoding="utf-8"))
    freq: dict[str, int] = {}
    for c in data.get("cartographies", {}).values():
        for x in c.get("prevalenceTable", []) + c.get("urgencyTable", []):
            for v in (x.get("monograph") or {}).values():
                s = v.get("summary") if isinstance(v, dict) else v
                if not s:
                    continue
                for part in re.split(r"(?<=[.!?])\s+", s):
                    p = part.strip()
                    if len(p) > 40:
                        freq[p] = freq.get(p, 0) + 1
    return {p for p, cnt in freq.items() if cnt >= 20}


def strip_fenetres(h: str) -> str:
    """Retire toutes les <section class="fenetre...">...</section> en gérant les sections imbriquées éventuelles."""
    out = []
    i = 0
    for m in re.finditer(r'<section\b[^>]*class="[^"]*\bfenetre\b[^"]*"[^>]*>', h, re.I):
        if m.start() < i:
            continue
        out.append(h[i:m.start()])
        depth = 1
        pos = m.end()
        for t in re.finditer(r"<(/?)section\b", h[m.end():], re.I):
            if t.group(1):
                depth -= 1
                if depth == 0:
                    pos = m.end() + t.end()
                    close_gt = h.find(">", pos)
                    i = (close_gt + 1) if close_gt >= 0 else pos
                    break
            else:
                depth += 1
        else:
            i = len(h)
    out.append(h[i:])
    return "".join(out)


def pure_text(h: str) -> str:
    s = re.sub(r"<!--.*?-->", " ", h, flags=re.S)
    s = re.sub(r"<(script|style|svg|picture)\b[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<img\b[^>]*>", " ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = H.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def html_no_images_bytes(h: str) -> int:
    s = re.sub(r"<(svg|picture)\b.*?</\1>", "", h, flags=re.S | re.I)
    s = re.sub(r"<img\b[^>]*>", "", s, flags=re.I)
    s = re.sub(r'data:image/[^"\')\s]+', "", s)
    return len(s.encode("utf-8"))


def color_hue(val: str) -> float | None:
    val = val.strip()
    m = re.match(r"hsl\(\s*(\d+(?:\.\d+)?)", val, re.I)
    if m:
        return float(m.group(1)) % 360.0
    m = re.match(r"#([0-9a-f]{6}|[0-9a-f]{3})$", val, re.I)
    if m:
        hx = m.group(1)
        if len(hx) == 3:
            hx = "".join(c * 2 for c in hx)
        r, g, b = (int(hx[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return (h * 360.0) % 360.0
    return None


def is_verbal(sent: str) -> bool:
    words = {w.lower() for w in re.findall(r"[\w'’-]+", sent)}
    if words & VERBES or PRONOM_VERBE_RE.search(sent) or AUX_PP_RE.search(sent) or VERBE_SUFFIX_RE.search(sent):
        return True
    return False


def check_file(path: str, boiler: set[str], seen_lot: dict[str, str], cat: dict[int, dict] | None = None) -> dict:
    raw = open(path, encoding="utf-8", errors="ignore").read()
    errors: list[str] = []
    warnings: list[str] = []

    # 0. Circuit validation against catalogue_248.json & NON_MONOGRAPHIQUE guard
    m_lot = re.search(r"LOT_(\d{3})_", os.path.basename(path))
    m_circ = re.search(r'<meta\s+[^>]*name=["\']ssp-circuit["\'][^>]*content=["\']([^"\']+)["\']', raw, re.I)
    circ = m_circ.group(1).upper() if m_circ else ""
    if not circ:
        errors.append("META_SSP_CIRCUIT_MANQUANT")
    elif cat and m_lot:
        lot_n = int(m_lot.group(1))
        exp_circ = (cat.get(lot_n) or {}).get("circuit", "")
        if exp_circ and circ != exp_circ:
            errors.append(f"CIRCUIT_INCOHERENT: {circ} != {exp_circ}")
    if circ == "NON_MONOGRAPHIQUE":
        h3s = [H.unescape(re.sub(r"<[^>]+>", "", x)).strip() for x in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", raw, re.S | re.I)]
        bad_h = [h for h in h3s if re.search(r"\b(Physiopathologie|Approche syndromique|Diagnostic positif|Examen physique cibl)\b", h, re.I)]
        if bad_h:
            errors.append(f"PLAN_MALADIE_SUR_NON_MONOGRAPHIQUE: {bad_h[:4]}")

    # 1. Pure text & HTML no-image bytes
    pt = pure_text(raw)
    pt_bytes = len(pt.encode("utf-8"))
    no_img = html_no_images_bytes(raw)
    if not (MIN_PURE <= pt_bytes <= MAX_PURE):
        errors.append(f"CALIBRE_TEXTE_PUR: {pt_bytes} o ({pt_bytes/1024:.1f} Ko) hors [80.0–100.0 Ko]")
    if not (40_000 <= no_img <= 100_000):
        warnings.append(f"HTML_HORS_IMG: {no_img} o hors [40 000–100 000]")

    # 2. Signature (format DÉBUT · MODÈLE · PLATEFORME, 1..n lignes) juste avant </body>
    body_idx = raw.rfind("</body>")
    sig_m = find_signature(raw)
    if body_idx < 0:
        errors.append("BODY_MANQUANT: </body> introuvable")
    elif not sig_m or sig_m.end() > body_idx or not re.fullmatch(r"(?:\s|<script\b.*?</script>|<!--.*?-->)*", raw[sig_m.end():body_idx], re.S | re.I):
        errors.append("SIGNATURE_ABSENTE_OU_MAL_FORMEE avant </body>")
    if "FIN_FICHIER" not in raw[-400:]:
        errors.append("FIN_FICHIER_ABSENT dans les 400 derniers octets")

    # 3. Zero chantier terms in <title> and visible body (excluding signature)
    m_title = re.search(r"<title>(.*?)</title>", raw, re.S | re.I)
    title_txt = H.unescape(re.sub(r"<[^>]+>", "", m_title.group(1))) if m_title else ""
    body_only = raw[raw.find("<body"):] if "<body" in raw else raw
    body_no_sig = SIG_RE.sub("", body_only)
    vis_txt = pure_text(body_no_sig)
    for label, txt in (("TITLE", title_txt), ("VISIBLE", vis_txt)):
        hits = CHANTIER_RE.findall(txt)
        if hits:
            errors.append(f"TERME_CHANTIER_{label}: {sorted(set(hits))[:8]}")

    # 4. Zero images outside <section class="fenetre">
    outside = strip_fenetres(raw)
    imgs_out = re.findall(r"<(?:img|svg|picture|figure)\b", outside, re.I)
    if imgs_out:
        errors.append(f"IMAGE_HORS_FENETRE: {len(imgs_out)} balise(s) {imgs_out[:5]}")

    # Check image files exist
    lot_dir = os.path.dirname(path)
    for img_rel in re.findall(r'(?:src|href)="(images/[^"]+)"', raw):
        if not os.path.exists(os.path.join(lot_dir, img_rel)):
            errors.append(f"IMAGE_MANQUANTE: {img_rel}")

    # 5. Zero boilerplate from cartographie_DATA.json
    pt_norm = norm(pt)
    for b in boiler:
        if norm(b) in pt_norm:
            errors.append(f"GABARIT_CARTOGRAPHIE: {b[:80]}")

    # 6. Verbal sentences (prose, fenêtres, figcaptions, descriptive td)
    body_no_src = re.sub(r'<section\b[^>]*id="[\w-]*sources"[^>]*>.*?</section>', " ", body_no_sig, flags=re.S | re.I)
    body_no_src = re.sub(r"<nav\b[^>]*>.*?</nav>", " ", body_no_src, flags=re.S | re.I)
    body_no_src = re.sub(r"<header\b[^>]*>.*?</header>", " ", body_no_src, flags=re.S | re.I)
    body_no_src = re.sub(r"<footer\b[^>]*>.*?</footer>", " ", body_no_src, flags=re.S | re.I)

    nominal_hits = []
    for tag, inner in re.findall(r'<(p|li|dd|figcaption|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|li|dd|figcaption|div)>', body_no_src, re.S | re.I):
        for brut in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý«])", inner):
            t = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", re.sub(r'<sup class="r">.*?</sup>', "", brut, flags=re.S)))).strip()
            if len(t.split()) >= 4 and not is_verbal(t):
                nominal_hits.append(f"<{tag}> {t[:100]}")
            if len(t) > 60:
                k = hashlib.sha1(re.sub(r"\W+", "", t.lower()).encode()).hexdigest()
                if k in seen_lot and seen_lot[k] != path:
                    errors.append(f"PHRASE_PARTAGEE_AVEC_{os.path.basename(seen_lot[k])}: {t[:90]}")
                seen_lot.setdefault(k, path)

    if nominal_hits:
        errors.append(f"PHRASE_NOMINALE ({len(nominal_hits)}): {nominal_hits[:4]}")

    # 7. Front-end L1 & design constraints
    has_css = ("../_polices/forme.css" in raw) or ("../../_polices/forme.css" in raw)
    has_js = ("../_polices/forme.js" in raw) or ("../../_polices/forme.js" in raw)
    if not has_css or not has_js:
        errors.append("FORME_CSS_OU_JS_MANQUANT")
    raw_no_forme_js = re.sub(r'<script\b[^>]*src=["\'](?:\.\./)+_polices/forme\.js["\'][^>]*>\s*</script>', "", raw, flags=re.I)
    if re.search(r"<script\b", raw_no_forme_js, re.I):
        errors.append("SCRIPT_LOCAL_INTERDIT")
    if re.search(r"\stitle=", raw, re.I):
        errors.append("ATTRIBUT_TITLE_INTERDIT")
    if re.search(r"\bpopover(?:target)?=", raw, re.I):
        errors.append("ATTRIBUT_POPOVER_INTERDIT")
    for m_col in re.finditer(r"--fm-a\s*:\s*([^;\"]+)", raw):
        hue = color_hue(m_col.group(1))
        if hue is not None and 150.0 <= hue <= 305.0:
            errors.append(f"COULEUR_BLEUE_INTERDITE: {m_col.group(1)} (H={hue:.1f}°)")

    # Anchors check
    ids = set(re.findall(r'\bid="([^"]+)"', raw))
    missing_anc = sorted({a for a in re.findall(r'href="#([^"]+)"', raw) if a not in ids})
    if missing_anc:
        errors.append(f"ANCRES_ABSENTES ({len(missing_anc)}): {missing_anc[:6]}")

    return {
        "fichier": os.path.basename(path),
        "texte_pur_ko": round(pt_bytes / 1024, 2),
        "texte_pur_octets": pt_bytes,
        "html_hors_img_octets": no_img,
        "verdict": "PASS" if not errors else "FAIL",
        "errors": errors,
        "warnings": warnings,
    }


def resolve_src_dir(d: str) -> str:
    sub = os.path.join(d, "_sources")
    if os.path.isdir(sub) and (
        os.path.exists(os.path.join(sub, "NOTIONS.json"))
        or any(x.startswith("LOT_") and x.endswith(".html") for x in os.listdir(sub))
    ):
        return sub
    return d


def check_ssp(ssp_num: int, boiler: set[str], cat: dict[int, dict]) -> int:
    d = resolve_src_dir(os.path.join(BASE, f"SSP_{ssp_num:03d}"))
    nj = json.load(open(os.path.join(d, "NOTIONS.json"), encoding="utf-8"))
    entites = nj["entites"]
    expected = [os.path.join(d, f"LOT_{ssp_num:03d}_Phase_A_V0.html")] + [
        os.path.join(d, f"LOT_{ssp_num:03d}_Phase_B_V0_DX.{i}.html") for i in range(1, len(entites) + 1)
    ]
    missing = [os.path.basename(p) for p in expected if not os.path.exists(p)]
    results = []
    seen_lot: dict[str, str] = {}
    for p in expected:
        if os.path.exists(p):
            results.append(check_file(p, boiler, seen_lot, cat))

    # Real-notion coverage check (ignoring boilerplate sentences in NOTIONS.json)
    real_misses = []
    for i, e in enumerate(entites, 1):
        fp = expected[i]
        if not os.path.exists(fp):
            real_misses.append((i, e["nom"], "FICHIER_ABSENT"))
            continue
        pt_norm = norm(pure_text(open(fp, encoding="utf-8", errors="ignore").read()))
        for n in e["notions"]:
            parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+", n["texte"]) if p.strip()]
            clean_txt = " ".join(p for p in parts if p not in boiler and "Ce mécanisme physiopathologique (" not in p)
            k = toks(clean_txt)
            if not k:
                continue
            cov = sum(1 for w in k if w in pt_norm) / len(k)
            if cov < 0.60:
                real_misses.append((i, e["nom"][:35], n["point"], round(cov * 100), clean_txt[:90]))

    fail_count = sum(1 for r in results if r["verdict"] == "FAIL") + len(missing)
    out = {
        "ssp": f"SSP_{ssp_num:03d}",
        "code": nj["code"],
        "circuit": nj["circuit"],
        "entites_attendues": len(entites),
        "fichiers_manquants": missing,
        "fichiers": results,
        "notions_reelles_sous_60pct": real_misses[:25],
        "nb_notions_reelles_sous_60pct": len(real_misses),
        "verdict_global": "PASS" if (fail_count == 0 and len(real_misses) == 0) else "FAIL",
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0 if out["verdict_global"] == "PASS" else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cibles", nargs="+", help="Numéro SSP (ex: 248) ou chemins vers des fichiers HTML")
    args = ap.parse_args()
    boiler = load_boilerplate()
    cat = load_catalogue()
    if len(args.cibles) == 1 and re.fullmatch(r"\d{1,3}", args.cibles[0]):
        sys.exit(check_ssp(int(args.cibles[0]), boiler, cat))
    seen: dict[str, str] = {}
    res = [check_file(os.path.abspath(p), boiler, seen, cat) for p in args.cibles]
    print(json.dumps(res, ensure_ascii=False, indent=1))
    sys.exit(1 if any(r["verdict"] == "FAIL" for r in res) else 0)
