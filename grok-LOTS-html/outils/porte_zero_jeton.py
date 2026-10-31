#!/usr/bin/env python3
"""PORTE ZÉRO JETON — contrôles mécaniques gratuits AVANT toute passe de modèle (Python standard, aucun appel à un modèle).

  python3 grok-LOTS-html/outils/porte_zero_jeton.py avant <poste> <fichier.html> [--lot LOT_XXX] [--sha-attendu SHA] [--preuves DOSSIER]
                                                       [--strict] [--json] [--racine DEPOT]
  python3 grok-LOTS-html/outils/porte_zero_jeton.py precommit [--strict] [--json] [--racine DEPOT]   (fichiers indexés par git add)
  python3 grok-LOTS-html/outils/porte_zero_jeton.py reference [--racine DEPOT]                        codes tolérés (mesurés sur MODELE_DD_V8.html)

Verdict : VERT (rien à dire) · ORANGE (à lire, ne bloque pas ; bloque avec --strict) · ROUGE (ne lancez PAS la passe de modèle).
Code de sortie : 0 VERT/ORANGE · 1 ROUGE · 2 usage. LECTURE SEULE : n'écrit rien dans le dépôt (tampons dans le dossier temporaire).

Pourquoi « différentiel » : le harnais audit_langue.py garde des règles de l'époque V0 (title=, feuille externe, bande 80–150 Ko,
h2, h3_14) que le MODÈLE V8 lui-même déclenche. Un contrôle absolu donnerait de faux ROUGE sur un fichier V8 valide. La porte ne
bloque donc que les critiques NOUVEAUX par rapport à MODELE_DD_V8.html. Elle ne prouve JAMAIS l'exactitude médicale : elle retire
seulement, gratuitement, les défauts de forme que le modèle ferait payer à l'audit.
"""
from __future__ import annotations
import argparse, glob, hashlib, html, json, re, subprocess, sys, tempfile, time, unicodedata
from html.parser import HTMLParser
from pathlib import Path

POSTES = ("redacteur-phase-a", "redacteur", "auditeur-medical", "auditeur-conformite", "transversale", "mecanique")
X_MAX_DD, X_MAX_A = 9_000, 100_000                      # règle de Vial : fiche x ≤ 9 Ko (DD), ≤ 100 Ko (Phase A)
IDS = ["ess", "som"] + [f"p{i}" for i in range(1, 15)] + ["sources"]
PRECEDENT = {"auditeur-medical": ("redacteur", "redacteur-phase-a"), "auditeur-conformite": ("auditeur-medical",),
             "transversale": ("auditeur-conformite",)}
FIN = re.compile(r"^<!--\s*FIN_FICHIER\b.*-->\s*$")
MARQUEURS_ETRANGERS = re.compile(r"\b(FDA|EMA|BNF|UpToDate|Vidal|Micromedex|Lexicomp)\b")
DOSE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|UI|IU|ml|mL)\b")


def racine_depot(arg):
    if arg:
        return Path(arg).resolve()
    try:
        o = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, cwd=Path(__file__).resolve().parent)
        if o.returncode == 0 and o.stdout.strip():
            return Path(o.stdout.strip())
    except Exception:
        pass
    return Path(__file__).resolve().parents[2]


def lancer(R, args):
    o = subprocess.run([sys.executable, *args], capture_output=True, text=True, cwd=R)
    return o.returncode, o.stdout, o.stderr


def audit_langue(R, fichier):
    code, out, err = lancer(R, [str(R / "harnais/audit_langue.py"), str(fichier), "--json"])
    try:
        return json.loads(out)
    except Exception:
        return {"critiques": [{"code": "audit_illisible", "message": (err or out)[:200], "n": 1}], "avertissements": []}


def mesure_x(R, fichier):
    sys.path.insert(0, str(R / "harnais"))
    try:
        import taille_xy
    finally:
        sys.path.pop(0)
    m = taille_xy.mesurer(Path(fichier).read_text(encoding="utf-8"))
    return m.x[1], m.y[1]


class Balises(HTMLParser):
    VIDES = {"meta", "link", "br", "hr", "img", "input", "col", "area", "base", "source", "wbr"}

    def __init__(s):
        super().__init__(convert_charrefs=True)
        s.pile, s.err, s.ids, s.scripts, s.pop_cibles, s.pop_ids, s.fermetures = [], [], set(), 0, set(), set(), 0

    def handle_starttag(s, t, a):
        a = dict(a)
        if t == "script": s.scripts += 1
        if "id" in a: s.ids.add(a["id"])
        if "popover" in a and "id" in a: s.pop_ids.add(a["id"])
        if "popovertarget" in a: s.pop_cibles.add(a["popovertarget"])
        if a.get("popovertargetaction") == "hide": s.fermetures += 1
        if t not in s.VIDES: s.pile.append(t)

    def handle_endtag(s, t):
        if t in s.VIDES: return
        if t in s.pile:
            while s.pile:
                x = s.pile.pop()
                if x == t: break
                if x not in ("p", "li", "td", "th", "tr", "dd", "dt"): s.err.append(f"<{x}> non fermée avant </{t}>")
        else:
            s.err.append(f"</{t}> sans ouverture")


def norm(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s)); s = unicodedata.normalize("NFKC", s).lower()
    return re.sub(r"[^a-z0-9àâçéèêëîïôûùüœ]+", " ", s).strip()


def citations(R, texte, lot, preuves=None):
    """Part des « citations » de 40–400 car. retrouvées mot pour mot dans les preuves du LOT et les extraits AIPS locaux."""
    cites = re.findall(r"«([^»]{40,400})»", html.unescape(re.sub(r"<[^>]+>", "", texte)))
    if not cites:
        return None, 0, 0, "aucune citation"
    dossier = Path(preuves) if preuves else R / f"lot en cours de production/{lot}/evidence"
    ev = glob.glob(str(dossier / "*"))
    if not ev:
        return None, len(cites), 0, f"dossier de preuves absent ({dossier.name}/) ; passez --preuves DOSSIER"
    fichiers = ev + glob.glob(str(R / "ressources_ia/aips/extraits/*.txt"))
    corp = " ".join(norm(Path(f).read_text(encoding="utf-8", errors="ignore")) for f in fichiers)
    hit = sum(norm(c) in corp for c in cites)
    return hit / len(cites), len(cites), hit, f"{len(fichiers)} fichiers de preuves"


def journal(R):
    p = R / "grok-LOTS-html/ROUTAGE_GROK.jsonl"
    out = []
    if p.exists():
        for l in p.read_text(encoding="utf-8").splitlines():
            try: out.append(json.loads(l))
            except Exception: pass
    return out


def verifier(R, poste, fichier, lot=None, sha_attendu=None, base=None, preuves=None):
    t0 = time.time()
    f = Path(fichier)
    rouge, orange, info = [], [], {}
    if poste not in POSTES:
        return {"verdict": "ROUGE", "rouge": [f"poste inconnu : {poste}"], "orange": [], "info": {}}
    if not f.exists():
        return {"verdict": "ROUGE", "rouge": [f"fichier absent : {f}"], "orange": [], "info": {}}
    brut = f.read_bytes()
    texte = brut.decode("utf-8", errors="replace")
    phase_a = "Phase_A" in f.name
    m = re.search(r"LOT_(\d+)", f.name)
    lot = lot or (f"LOT_{m.group(1)}" if m else None)
    info.update({"fichier": str(f), "poste": poste, "type": "Phase A" if phase_a else "DD", "lot": lot,
                 "octets": len(brut), "sha256": hashlib.sha256(brut).hexdigest()[:16]})
    if sha_attendu and not info["sha256"].startswith(sha_attendu.lower()):
        rouge.append(f"sceau SHA différent : attendu {sha_attendu}, trouvé {info['sha256']} (le fichier a changé depuis la passe précédente)")
    # 1. FIN_FICHIER = dernière ligne non vide
    lignes = [l for l in texte.splitlines() if l.strip()]
    if not lignes or not FIN.match(lignes[-1].strip()):
        rouge.append("FIN_FICHIER absent ou n'est pas la dernière ligne non vide (fichier tronqué ?)")
    # 2. taille x/y
    x, y = mesure_x(R, f)
    xmax = X_MAX_A if phase_a else X_MAX_DD
    info.update({"x_octets": x, "y_octets": y, "x_max": xmax})
    if x > xmax: rouge.append(f"fiche x = {x/1000:.1f} Ko > {xmax/1000:.0f} Ko")
    elif x > 0.95 * xmax: orange.append(f"fiche x = {x/1000:.1f} Ko (> 95 % du plafond {xmax/1000:.0f} Ko)")
    # 3. structure
    b = Balises(); b.feed(texte)
    if b.scripts: rouge.append(f"{b.scripts} balise(s) <script> (interdit)")
    manque = [i for i in IDS if i not in b.ids]
    if manque: rouge.append("ids absents : " + ", ".join(manque))
    if b.err: rouge.append(f"{len(b.err)} balise(s) mal appariée(s), p. ex. {b.err[0]}")
    orphelins = sorted(b.pop_cibles - b.pop_ids)
    if orphelins: rouge.append(f"popovertarget orphelin(s) : {', '.join(orphelins[:5])}")
    if b.pop_ids and b.fermetures < len(b.pop_ids): rouge.append(f"{len(b.pop_ids) - b.fermetures} fenêtre(s) sans bouton de fermeture (popovertargetaction=\"hide\")")
    if "non validé cliniquement" not in texte: rouge.append("mention « non validé cliniquement » absente")
    # 4. audit_langue : critiques NOUVEAUX par rapport au modèle V8
    a = audit_langue(R, f)
    tol = base if base is not None else codes_tolerees(R)
    nouveaux = [c for c in a.get("critiques", []) if c["code"] not in tol]
    for c in nouveaux: rouge.append(f"audit_langue [{c['code']}] {c.get('message','')} (n = {c.get('n')})")
    info["critiques_toleres_V8"] = sorted(c["code"] for c in a.get("critiques", []) if c["code"] in tol)
    av = {c["code"]: c["n"] for c in a.get("avertissements", [])}
    info["avertissements"] = av
    gros = {k: v for k, v in av.items() if k in ("phrase_longue", "phrase_double", "abreviation", "sigle_non_developpe") and v}
    if gros: orange.append("langue : " + ", ".join(f"{k} × {v}" for k, v in gros.items()))
    # 5. AIPS / doses (indice, pas preuve)
    txt = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?s)<(style|script)[^>]*>.*?</\1>", " ", texte)))
    doses = len(DOSE.findall(txt)); etr = sorted(set(MARQUEURS_ETRANGERS.findall(txt)))
    info["doses_reperees"] = doses
    if doses and "AIPS" not in txt: orange.append(f"{doses} dose(s) repérée(s) sans la moindre mention AIPS")
    if etr: orange.append("source(s) étrangère(s) citée(s) : " + ", ".join(etr) + " (doses : AIPS suisse seulement)")
    # 6. citations « » mot pour mot
    if lot:
        taux, n, hit, note = citations(R, texte, lot, preuves)
        info["citations"] = {"n": n, "retrouvees": hit, "taux": None if taux is None else round(taux, 3), "note": note}
        if taux is not None and taux < 0.85: orange.append(f"citations « » retrouvées mot pour mot : {hit}/{n} ({taux:.0%}) — mesure de référence LOT_016 : 94 %")
        if taux is None and n: orange.append(f"{n} citation(s) non vérifiable(s) : {note}")
    # 7. ordre des postes : la passe précédente est-elle consignée ?
    if poste in PRECEDENT and lot:
        J = journal(R)
        vu = any(j.get("lot") == lot and j.get("poste") in PRECEDENT[poste] and Path(str(j.get("fichier", ""))).name == f.name for j in J)
        if not vu: orange.append(f"passe précédente ({'/'.join(PRECEDENT[poste])}) non consignée pour {f.name} dans ROUTAGE_GROK.jsonl")
    info["duree_s"] = round(time.time() - t0, 2)
    return {"verdict": "ROUGE" if rouge else ("ORANGE" if orange else "VERT"), "rouge": rouge, "orange": orange, "info": info}


_BASE = None


def codes_tolerees(R):
    global _BASE
    if _BASE is None:
        mod = R / "harnais/modele_lecon/MODELE_DD_V8.html"
        _BASE = {c["code"] for c in audit_langue(R, mod).get("critiques", [])} if mod.exists() else set()
    return _BASE


def afficher(r, as_json):
    if as_json:
        print(json.dumps(r, ensure_ascii=False, indent=1)); return
    i = r["info"]
    print(f"{r['verdict']}  {i.get('poste','')}  {Path(i.get('fichier','')).name}  [{i.get('type','')}, x = {i.get('x_octets','?')} o, sha {i.get('sha256','?')}, {i.get('duree_s','?')} s]")
    for m in r["rouge"]: print("  ROUGE  ", m)
    for m in r["orange"]: print("  ORANGE ", m)
    if r["verdict"] == "ROUGE": print("  → ne lancez pas la passe de modèle : corrigez d'abord (gratuit), puis relancez la porte.")


def precommit(R, strict, as_json):
    o = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"], capture_output=True, text=True, cwd=R)
    fichiers = [l for l in o.stdout.splitlines() if l.strip()]
    branche = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True, cwd=R).stdout.strip()
    res, rouge_global = [], False
    if branche.startswith("grok/"):
        hors = [f for f in fichiers if not f.startswith("grok-LOTS-html/")]
        if hors:
            res.append({"verdict": "ROUGE", "rouge": [f"hors périmètre grok-LOTS-html/ : {', '.join(hors[:5])}"], "orange": [], "info": {"fichier": "(périmètre)", "poste": "mecanique"}}); rouge_global = True
    with tempfile.TemporaryDirectory() as tmp:
        for f in fichiers:
            if not (f.startswith("grok-LOTS-html/") and f.endswith(".html") and re.search(r"LOT_\d+", f)): continue
            blob = subprocess.run(["git", "show", f":{f}"], capture_output=True, cwd=R).stdout
            cp = Path(tmp) / Path(f).name; cp.write_bytes(blob)
            r = verifier(R, "mecanique", cp)
            r["info"]["fichier"] = f
            res.append(r); rouge_global |= r["verdict"] == "ROUGE" or (strict and r["verdict"] == "ORANGE")
    if as_json: print(json.dumps(res, ensure_ascii=False, indent=1))
    else:
        for r in res: afficher(r, False)
        if not res: print("VERT  rien d'indexé à contrôler")
    return 1 if rouge_global else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=("avant", "precommit", "reference"))
    ap.add_argument("poste", nargs="?"); ap.add_argument("fichier", nargs="?")
    ap.add_argument("--lot"); ap.add_argument("--sha-attendu"); ap.add_argument("--preuves", help="dossier des preuves (défaut : lot en cours de production/<LOT>/evidence)"); ap.add_argument("--racine")
    ap.add_argument("--strict", action="store_true"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    R = racine_depot(a.racine)
    if a.cmd == "reference":
        print(json.dumps({"codes_toleres_V8": sorted(codes_tolerees(R)), "x_max_dd": X_MAX_DD, "x_max_phase_a": X_MAX_A, "ids": IDS}, ensure_ascii=False, indent=1)); return 0
    if a.cmd == "precommit":
        return precommit(R, a.strict, a.json)
    if not a.poste or not a.fichier:
        ap.print_usage(sys.stderr); return 2
    r = verifier(R, a.poste, a.fichier, a.lot, a.sha_attendu, preuves=a.preuves)
    afficher(r, a.json)
    return 1 if r["verdict"] == "ROUGE" or (a.strict and r["verdict"] == "ORANGE") else 0


if __name__ == "__main__":
    sys.exit(main())
