#!/usr/bin/env python3
"""Audit linguistique et de forme d'un fichier HTML de LOT — zéro jeton (Python standard).

Reprend ce que l'auditeur de conformité fait de façon déterministe ; ne juge PAS le fond médical.

Usage
  python3 harnais/audit_langue.py <fichier.html> [--json] [--liste LISTE_DX_CANONIQUE.md]
                                  [--sigles-ok fichier.txt] [--max-mots 35]
  python3 harnais/audit_langue.py <fichier.html> --corriger [--sortie copie.html]
  python3 harnais/audit_langue.py <fichier.html> --corriger --en-place   (explicite, jamais par défaut)

Contrôles
  structure : DOCTYPE, FIN_FICHIER, bande 80-150 Ko, mention « non validé cliniquement »
  balises   : table/thead/tbody/tr/th/td/ul/ol/li/details/section équilibrées
  interdits : attribut title=, <script>, <img>, feuille externe
  fenêtres  : chaque popover porte un bouton popovertargetaction="hide" ; popovertarget orphelin
  titres    : <h2> = ligne de LISTE_DX_CANONIQUE.md ; 14 <h3 id="dxN-pM"> uniques
  langue    : sigles non développés à la première occurrence, abréviations interdites,
              phrases > 35 mots (hors « citations »), chaînes de points-virgules,
              phrases en double, espaces insécables manquantes, espace avant . ou ,
Corrections sûres (--corriger, sur copie) : espaces insécables, espace avant . et ,,
  popovertargetaction="hide" manquant sur le bouton de fermeture, attribut title= retiré.
Tout le reste est signalé, jamais réécrit. Code de sortie : 0 sans critique, 1 sinon.
"""
from __future__ import annotations
import argparse, html, json, re, sys
from html.parser import HTMLParser
from pathlib import Path

VERSION = "1.0"
BANDE_MIN, BANDE_MAX = 80_000, 150_000
NBSP = " "

# Sigles connus sans développement requis (extensible : --sigles-ok ou harnais/audit_langue_sigles.txt).
SIGLES_OK = {
    "SI", "OK", "LOT", "DX", "HTML", "PDF", "URL", "ATC", "UI", "ABCDE", "CH", "UE", "EU", "USA",
    "ISBN", "DOI", "PMID", "PMC", "ID",
}
ROMAIN = re.compile(r"^(?=[IVXLCDM]+$)M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
RE_SIGLE = re.compile(r"(?<![\w\[/.-])([A-ZÀ-Ý][A-ZÀ-Ý0-9]{1,7})(?![\w\]/-])")
ABREV_INTERDITES = [
    (r"\bp\.\s?ex\.", "p. ex."), (r"\bcf\.", "cf."), (r"\bvs\.?(?=\s)", "vs"), (r"\betc\.", "etc."),
    (r"\bi\.\s?v\.(?![\w])", "i.v."), (r"\bs\.\s?c\.(?![\w])", "s.c."), (r"\bi\.\s?m\.(?![\w])", "i.m."),
    (r"\benv\.", "env."), (r"\bqqch\b", "qqch"), (r"\bpdt\b", "pdt"), (r"\bs/p\b", "s/p"), (r"\bc/o\b", "c/o"),
    (r"\bnb\.", "nb."),
]
UNITES = r"(?:mg|g|kg|µg|mcg|ng|mL|ml|L|dL|mmol|µmol|nmol|mol|UI|mm|cm|mmHg|kPa|°C|%|bpm|mEq)"
RE_NBSP_UNITE = re.compile(rf"(\d) (?={UNITES}(?![\wÀ-ÿ]))")
RE_NBSP_PONCT = re.compile(r" (?=[:;?!»%])")
RE_NBSP_GUIL = re.compile(r"(«) ")
RE_ESPACE_AVANT_POINT = re.compile(r" +(?=[.,](?:\s|$))")
BLOCS = {"p", "li", "td", "th", "caption", "h1", "h2", "h3", "h4", "h5", "div", "section", "tr", "ul", "ol",
         "table", "details", "summary", "nav", "header", "main", "button", "br", "dd", "dt", "figcaption"}
APPARIES = ["table", "thead", "tbody", "tr", "th", "td", "ul", "ol", "li", "details", "section"]


# ---------------------------------------------------------------- extraction du texte
class Extracteur(HTMLParser):
    """Blocs de texte visibles avec contexte : point courant (h3), zone (sources, titre)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocs: list[dict] = []
        self._buf: list[str] = []
        self._skip = 0
        self._point = ""
        self._tag_h = None
        self._in_sources = False

    def flush(self):
        t = re.sub(r"\s+", " ", "".join(self._buf)).strip()
        self._buf = []
        if t:
            self.blocs.append({"texte": t, "point": self._point, "sources": self._in_sources,
                               "tete": self._tag_h in ("h1", "h2")})

    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script", "head", "title"):
            self._skip += 1
        if tag in BLOCS:
            self.flush()
        if tag == "h3":
            self._point = dict(attrs).get("id", "") or ""
        if tag in ("h1", "h2", "h3"):
            self._tag_h = tag

    def handle_endtag(self, tag):
        if tag in ("style", "script", "head", "title"):
            self._skip = max(0, self._skip - 1)
        if tag in BLOCS:
            if tag == "h2":
                t = re.sub(r"\s+", " ", "".join(self._buf)).strip()
                self._in_sources = t.lower().startswith("sources")
            self.flush()
            if tag in ("h1", "h2", "h3"):
                self._tag_h = None

    def handle_data(self, data):
        if not self._skip:
            self._buf.append(data)


def blocs_de(src: str) -> list[dict]:
    e = Extracteur()
    e.feed(src)
    e.flush()
    return e.blocs


RE_CITATION = re.compile(r"«[^»]*»")
RE_REF = re.compile(r"\[S\d+(?:[–,\-\s]+S?\d+)*\]")
RE_MOT = re.compile(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*")
RE_FIN_PHRASE = re.compile(r"(?<=[.!?…])(?:\s*\[S[^\]]*\])?\s+(?=[A-ZÀ-Ý«(\[\"“])")


def phrases(texte: str) -> list[str]:
    t = re.sub(r"\b(p|env|cf|etc|art|al|no|Dr|Prof|ss|vs|fig|tab|réf)\.\s",
               lambda m: m.group(0).replace(". ", ".\x00"), texte)
    return [p.replace("\x00", " ").strip() for p in RE_FIN_PHRASE.split(t) if p.strip()]


def nb_mots(phrase: str) -> int:
    return len(RE_MOT.findall(RE_REF.sub(" ", RE_CITATION.sub(" ", phrase))))


def norm_cle(s: str) -> str:
    return re.sub(r"[^a-z0-9àâäçéèêëîïôöùûüœ]+", " ", s.lower()).strip()


# ---------------------------------------------------------------- contrôles
def charger_liste(p: Path | None) -> dict[int, str]:
    out: dict[int, str] = {}
    if not p or not p.is_file():
        return out
    for l in p.read_text(encoding="utf8").splitlines():
        m = re.match(r"\s*DX\.(\d{1,2})\s*[—–:\-]\s*(.+?)\s*$", l)
        if m:
            out[int(m.group(1))] = m.group(2).strip()
    return out


def trouver_liste(f: Path, explicite: str | None) -> Path | None:
    if explicite:
        return Path(explicite)
    cands = [f.parent / "LISTE_DX_CANONIQUE.md"]
    m = re.search(r"LOT_(\d{3})", f.name)
    racine = next((a for a in f.resolve().parents if (a / "harnais").is_dir()), None)
    if m and racine:
        for d in ("LOT_Claude_Finaux", "lot en cours de production"):
            cands.append(racine / d / f"LOT_{m.group(1)}" / "LISTE_DX_CANONIQUE.md")
    return next((c for c in cands if c.is_file()), None)


def norm_titre(s: str) -> str:
    s = html.unescape(re.sub(r"<[^>]+>", "", s)).replace(NBSP, " ").replace("🚩", "")
    s = re.sub(r"\(?\bE\d{1,2}\b\)?\s*$", "", s.strip())
    return re.sub(r"\s+", " ", s).strip(" .*|")


def charger_sigles_ok(extra: str | None) -> set[str]:
    ok = set(SIGLES_OK)
    cands = [Path(__file__).with_name("audit_langue_sigles.txt")]
    if extra:
        cands.append(Path(extra))
    for c in cands:
        if c.is_file():
            for l in c.read_text(encoding="utf8").splitlines():
                l = l.split("#")[0].strip()
                if l:
                    ok.add(l)
    return ok


def audit(f: Path, liste: str | None = None, sigles_ok: str | None = None, max_mots: int = 35,
          src: str | None = None, nom: str | None = None) -> dict:
    """`src`/`nom` permettent d'auditer un texte venu de git (banc d'essai)."""
    nom = nom or f.name
    if src is None:
        brut = f.read_bytes()
        src = brut.decode("utf8", errors="replace")
    else:
        brut = src.encode("utf8")
    crit: list[dict] = []
    avert: list[dict] = []
    stats: dict = {"octets": len(brut), "version_script": VERSION}

    def C(code, msg, n=1, ex=None):
        crit.append({"code": code, "message": msg, "n": n, "exemples": (ex or [])[:6]})

    def A(code, msg, n=1, ex=None):
        avert.append({"code": code, "message": msg, "n": n, "exemples": (ex or [])[:6]})

    est_a = "Phase_A" in nom
    mdx = re.search(r"DX\.(\d{1,2})\.html$", nom)
    numdx = int(mdx.group(1)) if mdx else None

    if not re.match(r"\s*<!DOCTYPE html>", src, re.I):
        C("doctype", "DOCTYPE html absent")
    if not re.search(r"<!--\s*FIN_FICHIER\s+[^>]*-->\s*$", src):
        C("fin_fichier", "balise FIN_FICHIER absente en fin de fichier (troncature présumée)")
    if not (BANDE_MIN <= len(brut) <= BANDE_MAX):
        C("bande", f"{len(brut)} octets hors bande {BANDE_MIN // 1000}–{BANDE_MAX // 1000} Ko")
    if "non validé cliniquement" not in src:
        C("non_valide", "mention « non validé cliniquement » absente")

    for tag in APPARIES:
        o = len(re.findall(rf"<{tag}[\s>/]", src, re.I))
        c = len(re.findall(rf"</{tag}\s*>", src, re.I))
        if o != c:
            C("balise_" + tag, f"<{tag}> ouvertes {o} ≠ fermées {c}")

    tt = re.findall(r"<(?!title\b)[a-z][^>]*\stitle\s*=[^>]*>", src, re.I)
    if tt:
        C("title", "attribut title= présent (infobulle interdite)", len(tt), [x[:90] for x in tt])
    sc = re.findall(r"<script[\s>]", src, re.I)
    if sc:
        C("script", "<script> présent", len(sc))
    ex_ext = re.findall(r"<img[\s>]|<link[^>]+stylesheet", src, re.I)
    if ex_ext:
        C("externe", "image ou feuille de style externe", len(ex_ext))

    pop_ids = [m.group(1) for m in re.finditer(r"<[a-z]+(?=[^>]*\spopover(?:\s|>|=))[^>]*\sid\s*=\s*[\"']([^\"']+)[\"']", src, re.I)]
    pop_ids += [m.group(1) for m in re.finditer(r"<[a-z]+[^>]*\sid\s*=\s*[\"']([^\"']+)[\"'][^>]*\spopover(?:\s|>|=)", src, re.I)]
    pop_ids = list(dict.fromkeys(pop_ids))
    cibles = set(re.findall(r"\spopovertarget\s*=\s*[\"']([^\"']+)[\"']", src, re.I))
    hide = set()
    for m in re.finditer(r"<button[^>]*>", src, re.I):
        b = m.group(0)
        t = re.search(r"popovertarget\s*=\s*[\"']([^\"']+)[\"']", b, re.I)
        if t and re.search(r"popovertargetaction\s*=\s*[\"']hide[\"']", b, re.I):
            hide.add(t.group(1))
    sans_hide = [i for i in pop_ids if i not in hide]
    if sans_hide:
        C("popover_hide", f"{len(sans_hide)} popover sans bouton popovertargetaction=\"hide\"", len(sans_hide), sans_hide)
    orph = sorted(cibles - set(pop_ids))
    if orph:
        C("popover_orphelin", f"{len(orph)} popovertarget sans fenêtre popover", len(orph), orph)
    stats["popover"] = len(pop_ids)

    if not est_a:
        h2 = [norm_titre(x) for x in re.findall(r"<h2[^>]*>(.*?)</h2>", src, re.I | re.S)]
        h2dx = [x for x in h2 if re.match(r"DX\.\d", x)]
        lp = trouver_liste(f, liste)
        canon = charger_liste(lp)
        stats["liste_canonique"] = str(lp) if lp else None
        if not h2dx:
            C("h2", "aucun <h2> « DX.n — nom »")
        elif canon and numdx in canon:
            attendu = f"DX.{numdx} — {canon[numdx]}"
            if norm_titre(h2dx[0]) != norm_titre(attendu):
                C("h2_canon", "<h2> différent de LISTE_DX_CANONIQUE.md", 1, [f"fichier : {h2dx[0]}", f"liste   : {attendu}"])
        elif not canon:
            A("h2_canon", "liste canonique introuvable : <h2> non comparé")
        ids = re.findall(r"<h3[^>]*\bid\s*=\s*[\"']([A-Za-z0-9_-]+?)-p(\d{1,2})[\"']", src, re.I)
        pref = {p for p, _ in ids}
        nums = [int(n) for _, n in ids]
        if sorted(nums) != list(range(1, 15)) or len(pref) != 1:
            C("h3_14", f"les <h3 id=\"dxN-pM\"> ne forment pas 1..14 uniques ({len(nums)} trouvés, préfixes {sorted(pref)})")
        elif numdx and pref != {f"dx{numdx}"}:
            C("h3_prefixe", f"préfixe des h3 {sorted(pref)} ≠ dx{numdx}")
        stats["h3"] = len(nums)

    blocs = blocs_de(src)
    corps = [b for b in blocs if not b["tete"] and not b["sources"]]
    stats["blocs"] = len(blocs)
    stats["mots"] = sum(len(RE_MOT.findall(b["texte"])) for b in corps)

    longues, chaines, vus, doubles = [], [], {}, []
    for b in corps:
        for ph in phrases(b["texte"]):
            n = nb_mots(ph)
            if n > max_mots:
                longues.append({"mots": n, "point": b["point"], "texte": ph[:220]})
            if ph.count(";") >= 2 and n > 20:
                chaines.append({"mots": n, "point": b["point"], "texte": ph[:220]})
            if n >= 8:
                k = norm_cle(RE_REF.sub("", ph))
                if k in vus:
                    doubles.append({"point": b["point"], "texte": ph[:160]})
                else:
                    vus[k] = b["point"]
    if longues:
        A("phrase_longue", f"{len(longues)} phrases > {max_mots} mots (hors citations)", len(longues),
          [f"{x['mots']} mots [{x['point']}] {x['texte']}" for x in sorted(longues, key=lambda y: -y["mots"])])
    if chaines:
        A("chaine_pv", f"{len(chaines)} phrases à ≥ 2 points-virgules et > 20 mots (à scinder)", len(chaines),
          [f"[{x['point']}] {x['texte']}" for x in chaines])
    if doubles:
        A("phrase_double", f"{len(doubles)} phrases (≥ 8 mots) répétées à l'identique", len(doubles),
          [f"[{x['point']}] {x['texte']}" for x in doubles])

    pleine = " \n".join(b["texte"] for b in corps)
    ab = []
    for rx, nom_ab in ABREV_INTERDITES:
        n = len(re.findall(rx, pleine))
        if n:
            ab.append(f"{nom_ab} ×{n}")
    if ab:
        A("abreviation", "abréviations non développées : " + ", ".join(ab), len(ab), ab)

    ok = charger_sigles_ok(sigles_ok)
    premiers: dict[str, dict] = {}
    for i, b in enumerate(corps):
        for m in RE_SIGLE.finditer(b["texte"]):
            s = m.group(1)
            if s in premiers:
                premiers[s]["n"] += 1
            else:
                premiers[s] = {"n": 1, "bloc": i, "pos": m.start(), "point": b["point"]}
    non_dev = []
    for s, d in premiers.items():
        if s in ok or ROMAIN.match(s) or re.match(r"^[A-Z]\d{1,2}$", s) or s.startswith("DX"):
            continue
        t, p = corps[d["bloc"]]["texte"], d["pos"]
        reste = t[p + len(s):]
        dev = (t[:p].rstrip().endswith("(") and re.match(r"\s*[),;]", reste)) \
            or re.match(r"\s*\(\s*[a-zà-ÿ]", reste) or re.match(r"\s*:\s*[a-zà-ÿ]{3,}", reste)
        if not dev:
            non_dev.append((s, d))
    if non_dev:
        non_dev.sort(key=lambda x: (x[1]["bloc"], x[1]["pos"]))
        A("sigle_non_developpe", f"{len(non_dev)} sigles dont la 1re occurrence n'est pas développée", len(non_dev),
          [f"{s} (×{d['n']}) [{d['point']}] …{corps[d['bloc']]['texte'][max(0, d['pos'] - 40):d['pos'] + 30]}…" for s, d in non_dev])
    stats["sigles_distincts"] = len(premiers)

    n_ponct = n_unite = n_guil = n_pt = zone = 0
    exs = []
    for seg in re.split(r"(<[^>]*>)", src):
        if seg.startswith("<"):
            low = seg.lower()
            if re.match(r"<(style|script|head)\b", low):
                zone += 1
            elif re.match(r"</(style|script|head)\b", low):
                zone = max(0, zone - 1)
            continue
        if zone:
            continue
        a = len(RE_NBSP_PONCT.findall(seg))
        n_ponct += a
        n_unite += len(RE_NBSP_UNITE.findall(seg))
        n_guil += len(RE_NBSP_GUIL.findall(seg))
        n_pt += len(RE_ESPACE_AVANT_POINT.findall(seg))
        if a and len(exs) < 4:
            m = RE_NBSP_PONCT.search(seg)
            exs.append(seg[max(0, m.start() - 25):m.end() + 15])
    tot_nb = n_ponct + n_unite + n_guil
    if tot_nb:
        A("insecable", f"{tot_nb} espaces insécables manquantes (ponctuation haute {n_ponct}, nombre-unité {n_unite}, guillemets {n_guil})",
          tot_nb, exs)
    if n_pt:
        A("espace_avant_point", f"{n_pt} espaces avant . ou ,", n_pt)
    stats["nbsp_presentes"] = src.count(NBSP) + src.count(" ") + src.count("&nbsp;")

    for l in (crit, avert):
        for x in l:
            x["exemples"] = [re.sub(r"\s+", " ", e) for e in x["exemples"]]
    return {"fichier": str(f), "octets": len(brut), "critiques": crit, "avertissements": avert, "stats": stats,
            "conforme": not crit}


# ---------------------------------------------------------------- corrections sûres
def corriger(src: str) -> tuple[str, dict]:
    n = {"insecable": 0, "espace_avant_point": 0, "popover_hide": 0, "title": 0}
    ids_pop = set(m.group(1) for m in re.finditer(r"<[a-z]+(?=[^>]*\spopover(?:\s|>|=))[^>]*\sid\s*=\s*[\"']([^\"']+)[\"']", src, re.I))
    ids_pop |= set(m.group(1) for m in re.finditer(r"<[a-z]+[^>]*\sid\s*=\s*[\"']([^\"']+)[\"'][^>]*\spopover(?:\s|>|=)", src, re.I))

    def hide(m):
        b = m.group(0)
        tid = re.search(r"popovertarget\s*=\s*[\"']([^\"']+)[\"']", b, re.I)
        if tid and tid.group(1) in ids_pop and not re.search(r"popovertargetaction", b, re.I) \
                and re.search(r"Fermer|✕|×", src[m.end():m.end() + 40]):
            n["popover_hide"] += 1
            return b[:-1].rstrip("/ ") + ' popovertargetaction="hide">'
        return b
    src = re.sub(r"<button[^>]*>", hide, src, flags=re.I)

    def t_title(m):
        n["title"] += 1
        return re.sub(r"\s+title\s*=\s*(\"[^\"]*\"|'[^']*')", "", m.group(0), flags=re.I)
    src = re.sub(r"<(?!title\b)[a-z][^>]*\stitle\s*=[^>]*>", t_title, src, flags=re.I)

    out, skip = [], 0
    for seg in re.split(r"(<[^>]*>)", src):
        if seg.startswith("<"):
            low = seg.lower()
            if re.match(r"<(style|script|head|pre)\b", low):
                skip += 1
            elif re.match(r"</(style|script|head|pre)\b", low):
                skip = max(0, skip - 1)
            out.append(seg)
            continue
        if skip:
            out.append(seg)
            continue
        s, a = RE_NBSP_PONCT.subn(NBSP, seg); n["insecable"] += a
        s, a = RE_NBSP_UNITE.subn(lambda m: m.group(1) + NBSP, s); n["insecable"] += a
        s, a = RE_NBSP_GUIL.subn("«" + NBSP, s); n["insecable"] += a
        s, a = RE_ESPACE_AVANT_POINT.subn("", s); n["espace_avant_point"] += a
        out.append(s)
    return "".join(out), n


def texte(r: dict) -> str:
    L = [f"AUDIT LANGUE — {r['fichier']} ({r['octets']} octets) : "
         + ("CONFORME (aucune critique)" if r["conforme"] else f"{len(r['critiques'])} CRITIQUE(S)")]
    for titre, k in (("CRITIQUES", "critiques"), ("AVERTISSEMENTS", "avertissements")):
        if r[k]:
            L.append(f"-- {titre}")
            for x in r[k]:
                L.append(f"  [{x['code']}] {x['message']}")
                for e in x["exemples"][:3]:
                    L.append(f"      · {e[:200]}")
    s = r["stats"]
    L.append(f"-- stats : {s.get('mots', 0)} mots, {s.get('sigles_distincts', 0)} sigles distincts, "
             f"{s.get('popover', 0)} fenêtres, {s.get('nbsp_presentes', 0)} insécables présentes")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fichier")
    ap.add_argument("--json", action="store_true", help="sortie JSON seule")
    ap.add_argument("--liste")
    ap.add_argument("--sigles-ok")
    ap.add_argument("--max-mots", type=int, default=35)
    ap.add_argument("--corriger", action="store_true", help="corrections sûres sur une copie")
    ap.add_argument("--sortie", help="copie corrigée (défaut : ./<nom>.corrige.html)")
    ap.add_argument("--en-place", action="store_true", help="écrase le fichier (explicite)")
    a = ap.parse_args()
    f = Path(a.fichier)
    if not f.is_file():
        print(f"introuvable : {f}", file=sys.stderr)
        return 2
    if a.corriger:
        liste = a.liste or (str(trouver_liste(f, None)) if trouver_liste(f, None) else None)
        neuf, n = corriger(f.read_bytes().decode("utf8"))
        dest = f if a.en_place else Path(a.sortie or f"{f.stem}.corrige.html")
        if dest.resolve() == f.resolve() and not a.en_place:
            print("refus : la copie ne peut pas écraser l'original sans --en-place", file=sys.stderr)
            return 2
        dest.write_bytes(neuf.encode("utf8"))
        r = audit(dest, liste, a.sigles_ok, a.max_mots, nom=f.name)
        r["corrections_appliquees"] = n
        r["copie"] = str(dest)
    else:
        r = audit(f, a.liste, a.sigles_ok, a.max_mots)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        print(texte(r))
        if a.corriger:
            print(f"-- corrections sûres appliquées dans {r['copie']} : {r['corrections_appliquees']}")
    return 0 if r["conforme"] else 1


if __name__ == "__main__":
    sys.exit(main())
