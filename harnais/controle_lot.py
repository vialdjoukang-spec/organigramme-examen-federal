#!/usr/bin/env python3
"""Contrôle mécanique d'un LOT (zéro jeton) — harnais V0, 26.10.2026.

Usage
  python3 harnais/controle_lot.py verifier  <dossier_LOT_XXX> [--json] [--sans-nom]
  python3 harnais/controle_lot.py extraire  <fichier.html> --points 2,3,4 [--html]
  python3 harnais/controle_lot.py manifeste <dossier_LOT_XXX>

verifier  : contrôle la forme d'un LOT final (1 Phase A + 10 Phase B = 11 HTML).
            Sortie : une ligne ; --json : détail. Code 0 = conforme, 1 = non conforme.
            --sans-nom : diagnostic de dossiers anciens (nommage non contrôlé).
extraire  : sort uniquement les points demandés (texte brut par défaut) pour
            qu'un auditeur ne lise pas tout le fichier.
manifeste : écrit MANIFESTE.json (nom, octets, SHA-256) dans le dossier.

Ce script NE juge PAS le fond médical ; il évite seulement de payer un modèle
pour des contrôles déterministes. Ko = 1 000 octets.
"""
from __future__ import annotations
import argparse, hashlib, html, json, re, sys
from pathlib import Path

VERSION = "1.0"
try:  # BANDE.json est absent de main : repli sur 100–200 Ko, jamais d'échec à l'import
    _B = json.loads((Path(__file__).resolve().parent / "BANDE.json").read_text(encoding="utf-8"))
    BANDE_MIN, BANDE_MAX = int(_B["min_ko"]) * 1000, int(_B["max_ko"]) * 1000
except (OSError, ValueError, KeyError, TypeError):
    BANDE_MIN, BANDE_MAX = 100_000, 200_000  # Ko = 1 000 octets ; bande indicative : avertissement, jamais critique
RE_A = re.compile(r"^LOT_(\d{3})_Phase_A_V0\.html$")
RE_B = re.compile(r"^LOT_(\d{3})_Phase_B_V0_DX\.(\d{1,2})\.html$")
RE_H3 = re.compile(r"<h3[^>]*\bid\s*=\s*[\"']([A-Za-z0-9_-]+?)-p(\d{1,2})[\"']", re.I)
RE_STRONG = re.compile(r"<strong>\s*(\d{1,2})\.\s", re.I)
RE_DX_H2 = re.compile(r"<h2[^>]*>\s*(DX\.(\d{1,2})\s*[—–-]\s*[^<]+)", re.I)
RE_LISTE = re.compile(r"DX\.(\d{1,2})\s*[—–:\-]\s*(.+)")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def norm(s: str) -> str:
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    s = s.replace(" ", " ").replace(" ", " ").replace("🚩", "")
    s = re.sub(r"\(?\bE\d{1,2}\b\)?\s*$", "", s.strip())
    return re.sub(r"\s+", " ", s).strip(" .*|")


def compte(t: str, tag: str) -> tuple[int, int]:
    o = len(re.findall(rf"<{tag}[\s>]", t, re.I))
    f = len(re.findall(rf"</{tag}\s*>", t, re.I))
    return o, f


def monographies(t: str) -> dict[str, set[int]]:
    g: dict[str, set[int]] = {}
    for pre, n in RE_H3.findall(t):
        g.setdefault(pre, set()).add(int(n))
    if not g:  # repli : titres <strong>N. …</strong>
        nums = [int(n) for n in RE_STRONG.findall(t)]
        k, cur = 0, set()
        for n in nums:
            if n == 1 and cur:
                g[f"m{k}"] = cur; k += 1; cur = set()
            cur.add(n)
        if cur:
            g[f"m{k}"] = cur
    return g


def analyse_fichier(p: Path) -> dict:
    b = p.read_bytes()
    t = b.decode("utf-8", errors="replace")
    crit, av, info = [], [], {}
    info["octets"] = len(b); info["sha256"] = sha(b)
    if not t.lstrip()[:15].lower().startswith("<!doctype html"):
        crit.append("début ≠ <!DOCTYPE html>")
    if not re.search(r"<!--\s*FIN_FICHIER\s+[^>]*-->\s*$", t):
        crit.append("FIN_FICHIER absent en fin de fichier (troncature présumée)")
    if re.search(r"\stitle\s*=", t, re.I):
        crit.append("attribut title= présent (infobulle interdite)")
    for tag in ("details", "table", "section", "div", "main"):
        o, f = compte(t, tag)
        if o != f:
            crit.append(f"balises <{tag}> déséquilibrées ({o} ouvertes / {f} fermées)")
    classes_defil = set(re.findall(r"\.([A-Za-z][\w-]*)\s*\{[^}]*overflow-x\s*:\s*auto", t))
    for pos in (m.start() for m in re.finditer(r"<table[\s>]", t, re.I)):
        avant = t[max(0, pos - 300):pos]
        inline = "overflow-x:auto" in avant.replace(" ", "")
        par_classe = any(re.search(rf"class\s*=\s*[\"'][^\"']*\b{re.escape(c)}\b", avant) for c in classes_defil)
        if not (inline or par_classe):
            crit.append("tableau non enveloppé (ni style overflow-x:auto, ni classe CSS interne équivalente)"); break
    longues = [i + 1 for i, l in enumerate(t.splitlines()) if len(l) > 3000 and "data:font" not in l and "font/woff" not in l and "data-brain=" not in l]
    if longues:
        crit.append(f"{len(longues)} ligne(s) > 3 000 caractères (ex. l.{longues[0]})")
    if re.search(r"<script[\s>]|<img[\s>]|<link[^>]+stylesheet", t, re.I):
        crit.append("script, image ou feuille de style externe présent")
    if not re.search(r"\[S1\]", t):
        crit.append("section Sources [S1]… absente")
    if "non validé cliniquement" not in t:
        av.append("mention « non validé cliniquement » absente")
    info["a_verifier_aips"] = t.count("À vérifier (AIPS)")
    mono = monographies(t)
    info["monographies"] = {k: sorted(v) for k, v in mono.items()}
    for k, v in mono.items():
        manque = sorted(set(range(1, 15)) - v)
        if manque:
            crit.append(f"monographie {k} : point(s) manquant(s) {manque}")
    info["dx_titres"] = [norm(m[0]) for m in RE_DX_H2.findall(t)]
    return {"fichier": p.name, "critiques": crit, "avertissements": av, **info}


def lire_liste(d: Path) -> dict[int, str]:
    for cand in (d / "LISTE_DX_CANONIQUE.md",):
        if cand.exists():
            out = {}
            for l in cand.read_text(encoding="utf-8").splitlines():
                m = RE_LISTE.search(l)
                if m and 1 <= int(m.group(1)) <= 15 and int(m.group(1)) not in out:
                    out[int(m.group(1))] = norm(m.group(2))
            return out
    return {}


def cache_lire(key: str):
    p = Path(".cache/harnais") / f"{key}.json"
    try:
        return json.loads(p.read_text())
    except Exception:
        return None


def cache_ecrire(key: str, val: dict):
    try:
        p = Path(".cache/harnais"); p.mkdir(parents=True, exist_ok=True)
        (p / f"{key}.json").write_text(json.dumps(val, ensure_ascii=False))
    except Exception:
        pass


def verifier(d: Path, sans_nom: bool) -> dict:
    fichiers = sorted(p for p in d.glob("*.html"))
    rapport = {"lot": d.name, "version_script": VERSION, "fichiers": [], "critiques_lot": [], "avertissements_lot": []}
    for p in fichiers:
        key = f"v{VERSION}_{sha(p.read_bytes())}"
        r = cache_lire(key) or analyse_fichier(p)
        r["fichier"] = p.name
        cache_ecrire(key, r)
        rapport["fichiers"].append(r)
    if sans_nom:
        return rapport
    m = re.match(r"LOT_(\d{3})", d.name)
    lot = m.group(1) if m else None
    A = [r for r in rapport["fichiers"] if RE_A.match(r["fichier"])]
    B = {int(RE_B.match(r["fichier"]).group(2)): r for r in rapport["fichiers"] if RE_B.match(r["fichier"])}
    autres = [r["fichier"] for r in rapport["fichiers"] if not (RE_A.match(r["fichier"]) or RE_B.match(r["fichier"]))]
    C = rapport["critiques_lot"]
    if len(A) != 1:
        C.append(f"Phase A : {len(A)} fichier(s) au lieu de 1")
    liste = lire_liste(d)
    N = len(liste) if 10 <= len(liste) <= 15 else 10  # 10 DD, jusqu'à 15 si lignes vertes retenues
    if sorted(B) != list(range(1, N + 1)):
        C.append(f"Phase B : DX présents {sorted(B)} ; attendus 1 à {N}, un fichier chacun")
    if autres:
        C.append(f"HTML hors nommage 1 + N : {autres}")
    for r in rapport["fichiers"]:
        ml = RE_A.match(r["fichier"]) or RE_B.match(r["fichier"])
        if ml and lot and ml.group(1) != lot:
            C.append(f"{r['fichier']} : numéro de LOT ≠ dossier {d.name}")
    AV = rapport["avertissements_lot"]   # taille : indicative, jamais bloquante (Vial 27.10.2026)
    for i, r in B.items():
        if not BANDE_MIN <= r["octets"] <= BANDE_MAX:
            AV.append(f"DX.{i} : {r['octets']} octets hors bande {BANDE_MIN // 1000}–{BANDE_MAX // 1000} Ko (indicative, non bloquante)")
        if len(r["monographies"]) != 1:
            C.append(f"DX.{i} : {len(r['monographies'])} monographie(s) dans le fichier au lieu de 1")
    for r in A:
        if not BANDE_MIN <= r["octets"] <= BANDE_MAX:
            AV.append(f"Phase A : {r['octets']} octets hors bande {BANDE_MIN // 1000}–{BANDE_MAX // 1000} Ko (indicative, non bloquante)")
    if not liste:
        C.append("LISTE_DX_CANONIQUE.md absente ou illisible (contrôle A↔B impossible)")
    else:
        if sorted(liste) != list(range(1, N + 1)):
            C.append(f"liste canonique incomplète : {sorted(liste)}")
        for i, r in B.items():
            titres = r.get("dx_titres") or []
            attendu = f"DX.{i} — {liste.get(i, '?')}"
            if not titres or norm(titres[0].replace("–", "—").replace(" - ", " — ").replace("’", "'")) != norm(attendu.replace("–", "—").replace(" - ", " — ").replace("’", "'")):
                C.append(f"DX.{i} : titre {titres[:1]} ≠ liste canonique « {attendu} » (CRITIQUE A↔B)")
        if A:
            ta = norm(Path(d / A[0]["fichier"]).read_text(encoding="utf-8", errors="replace"))
            for i, nom in liste.items():
                if nom and nom not in ta:
                    C.append(f"Phase A : DX.{i} « {nom} » introuvable mot pour mot (CRITIQUE A↔B)")
    return rapport


def cerveau_lot(d: Path, rapport: dict) -> None:
    """BRAIN-HARNESS en avertissements de lot (conseil) : sans effet si harnais/brain n'existe pas (ex. main)."""
    b = Path(__file__).resolve().parent / "brain"
    if not (b / "cerveau.py").exists():
        rapport["avertissements_lot"].append("cerveau : harnais/brain absent, contrôle sauté"); return
    sys.path.insert(0, str(b))
    try:
        import cerveau as CV
        for p in sorted(d.glob("*.html")):
            dl, _ = CV.analyser(p.read_text(encoding="utf-8", errors="replace"), p.name, ecrire=False)
            if dl: rapport["avertissements_lot"].append(f"cerveau {p.name} : {len(dl)} doléance(s) {CV.compte(dl)}")
    except BaseException as e:
        rapport["avertissements_lot"].append(f"cerveau en panne : {type(e).__name__} {str(e)[:120]}")


def extraire(p: Path, points: list[int], brut_html: bool) -> str:
    t = p.read_text(encoding="utf-8", errors="replace")
    heads = [(m.start(), int(m.group(2))) for m in RE_H3.finditer(t)]
    if not heads:
        heads = [(m.start(), int(m.group(1))) for m in RE_STRONG.finditer(t)]
    out = []
    for k, (pos, n) in enumerate(heads):
        if n in points:
            fin = heads[k + 1][0] if k + 1 < len(heads) else len(t)
            seg = t[pos:fin]
            if not brut_html:
                seg = re.sub(r"<(br|/p|/li|/tr|/h\d|/summary)[^>]*>", "\n", seg, flags=re.I)
                seg = html.unescape(re.sub(r"<[^>]+>", " ", seg))
                seg = re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", seg))
            out.append(f"=== point {n} @ {pos} ===\n{seg.strip()}")
    return "\n".join(out)


def manifeste(d: Path) -> Path:
    items = [{"fichier": p.name, "octets": p.stat().st_size, "sha256": sha(p.read_bytes())}
             for p in sorted(d.glob("*.html"))]
    out = d / "MANIFESTE.json"
    out.write_text(json.dumps({"lot": d.name, "fichiers": items}, ensure_ascii=False, indent=1), encoding="utf-8")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    v = sp.add_parser("verifier"); v.add_argument("dossier"); v.add_argument("--json", action="store_true"); v.add_argument("--sans-nom", action="store_true")
    v.add_argument("--cerveau", action="store_true", help="ajoute les doléances du BRAIN-HARNESS en avertissements (jamais bloquant ; ignoré si harnais/brain est absent)")
    e = sp.add_parser("extraire"); e.add_argument("fichier"); e.add_argument("--points", required=True); e.add_argument("--html", action="store_true")
    m = sp.add_parser("manifeste"); m.add_argument("dossier")
    a = ap.parse_args()
    if a.cmd == "verifier":
        r = verifier(Path(a.dossier), a.sans_nom)
        if a.cerveau: cerveau_lot(Path(a.dossier), r)
        nc = len(r["critiques_lot"]) + sum(len(f["critiques"]) for f in r["fichiers"])
        na = len(r["avertissements_lot"]) + sum(len(f["avertissements"]) for f in r["fichiers"])
        if a.json:
            print(json.dumps(r, ensure_ascii=False, indent=1))
        else:
            print(f"{r['lot']}: {'CONFORME' if nc == 0 else 'NON CONFORME'} — {len(r['fichiers'])} HTML, {nc} critique(s), {na} avertissement(s)")
        return 0 if nc == 0 else 1
    if a.cmd == "extraire":
        print(extraire(Path(a.fichier), [int(x) for x in a.points.split(",")], a.html))
        return 0
    print(manifeste(Path(a.dossier)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
