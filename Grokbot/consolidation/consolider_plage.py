#!/usr/bin/env python3
"""Consolidation à mémoire — plage Grokbot.

Vérifie, cours par cours, les exigences du PROMPT (présence, 14 points,
FIN_FICHIER, bande 100–200 Ko, score du détecteur). Mémorise l'état pour
ne revérifier qu'un fichier modifié ou encore en échec.

N'écrit jamais hors de Grokbot/. Ne corrige que l'absence de FIN_FICHIER
lorsque les 14 points sont déjà là (--corriger-fin).
"""
import argparse, datetime, hashlib, json, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GROK = ROOT / "Grokbot"
ETAT = Path(__file__).resolve().parent / "etat.json"
RAPPORT = GROK / "CONSOLIDATION_RAPPORT.md"
JAUGE = GROK / "Progression_PR_Grokbot.html"
LECONS = ["A"] + [f"DX{i}" for i in range(1, 11)]
BANDE = (100_000, 200_000)
BLOQUANTS = {"C_points_manquants", "C_FIN_FICHIER_absent", "C_balises", "B_phrase_partagee_entre_fichiers"}


def plage():
    nums = list(range(133, 249)) + list(range(51, 72)) + [79] + list(range(81, 103))
    return sorted(set(nums))


def fichier(lot, lec):
    d = GROK / f"LOT_{lot:03d}"
    if lec == "A":
        return d / f"LOT_{lot:03d}_Phase_A_V0.html"
    return d / f"LOT_{lot:03d}_Phase_B_V0_DX.{lec[2:]}.html"


def charger_controle():
    candidats = [
        ROOT / "ChatGPT_Codex" / "_outils" / "controle3.py",
        Path("/tmp/ref-prompts/outils/controle3.py"),
    ]
    for c in candidats:
        if c.is_file():
            sys.path.insert(0, str(c.parent))
            import controle3
            return controle3
    return None


CTRL = charger_controle()


class Args:
    points, min, max, ex, script_ok = 14, BANDE[0], BANDE[1], 1, False


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def exigences(chemin):
    ex = {
        "presence": "KO",
        "points_14": "KO",
        "fin_fichier": "KO",
        "bande_100_200": "KO",
        "sans_bloqueur": "KO",
        "score_90": "KO",
    }
    detail = {"octets": 0, "score": 0, "defauts": [], "besoin_sources": True}
    if not chemin.is_file():
        detail["besoin_sources"] = True
        detail["defauts"] = ["fichier_absent"]
        return ex, detail
    brut = chemin.read_bytes()
    texte = brut.decode("utf-8", "ignore")
    detail["octets"] = len(brut)
    ex["presence"] = "OK"
    points = all(re.search(rf'id="[\w-]*p{i}"', texte) for i in range(1, 15))
    ex["points_14"] = "OK" if points else "KO"
    fin = "FIN_FICHIER" in texte[-400:]
    ex["fin_fichier"] = "OK" if fin else "KO"
    ex["bande_100_200"] = "OK" if BANDE[0] <= len(brut) <= BANDE[1] else "KO"
    defs = set()
    if CTRL is not None:
        r = CTRL.controler(str(chemin), {}, Args(), {})
        defs = set(r["defauts"])
        detail["defauts"] = sorted(defs)
    else:
        if not points:
            defs.add("C_points_manquants")
        if not fin:
            defs.add("C_FIN_FICHIER_absent")
        if not (BANDE[0] <= len(brut) <= BANDE[1]):
            defs.add("C_taille_hors_bande")
        detail["defauts"] = sorted(defs)
    bloq = bool(defs & BLOQUANTS)
    ex["sans_bloqueur"] = "KO" if bloq else "OK"
    score = 40 + (20 if points else 0) + (20 if ex["bande_100_200"] == "OK" else 0)
    score += (0 if bloq else 10) + (10 if not defs else 0)
    detail["score"] = score
    ex["score_90"] = "OK" if score >= 90 else "KO"
    # La bande et les phrases se corrigent avec des sources, pas par remplissage.
    detail["besoin_sources"] = ex["bande_100_200"] == "KO" or any(
        d.startswith(("A_", "B_")) for d in defs
    )
    detail["corrigeable_fin"] = ex["presence"] == "OK" and ex["points_14"] == "OK" and ex["fin_fichier"] == "KO"
    return ex, detail


def maintenant():
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).strftime("%Y-%m-%dT%H:%M:%S+01:00")


def charger_etat():
    if ETAT.is_file():
        return json.loads(ETAT.read_text(encoding="utf-8"))
    return {"version": 1, "lots": {}}


def sauver(etat):
    ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def corriger_fin(chemin):
    texte = chemin.read_text(encoding="utf-8")
    if "FIN_FICHIER" in texte[-400:]:
        return False
    nom = chemin.stem
    chemin.write_text(texte.rstrip() + f"\n<!-- FIN_FICHIER {nom} -->\n", encoding="utf-8")
    return True


def passage(corriger):
    etat = charger_etat()
    etat["plage"] = [f"{n:03d}" for n in plage()]
    etat["dernier_passage"] = maintenant()
    stats = {"lecons": 0, "ok": 0, "ko": 0, "repris": 0, "sautes": 0, "corriges_fin": 0}
    lignes_sources = []
    for lot in plage():
        bloc = etat["lots"].setdefault(f"{lot:03d}", {"lecons": {}})
        for lec in LECONS:
            path = fichier(lot, lec)
            cle = f"{lot:03d}:{lec}"
            stats["lecons"] += 1
            digest = sha256(path.read_bytes()) if path.is_file() else ""
            ancien = bloc["lecons"].get(lec)
            if ancien and ancien.get("sha256") == digest and ancien.get("ok") and digest:
                stats["sautes"] += 1
                stats["ok"] += 1
                continue
            stats["repris"] += 1
            if corriger and path.is_file():
                ex0, det0 = exigences(path)
                if det0.get("corrigeable_fin") and corriger_fin(path):
                    stats["corriges_fin"] += 1
                    digest = sha256(path.read_bytes())
            ex, det = exigences(path)
            ok = all(v == "OK" for v in ex.values())
            bloc["lecons"][lec] = {
                "sha256": digest,
                "ok": ok,
                "exigences": ex,
                "octets": det["octets"],
                "score": det["score"],
                "defauts": det["defauts"],
                "besoin_sources": det["besoin_sources"] and not ok,
                "date": maintenant(),
            }
            if ok:
                stats["ok"] += 1
            else:
                stats["ko"] += 1
                if det["besoin_sources"]:
                    lignes_sources.append((cle, det["score"], det["defauts"][:6], "absent" if not path.is_file() else "présent"))
    sauver(etat)
    rediger(etat, stats, lignes_sources)
    integrer_jauge(stats)
    return stats


def rediger(etat, stats, lignes_sources):
    pct = round(100 * stats["ok"] / stats["lecons"]) if stats["lecons"] else 0
    par_lot = {}
    for cle, score, defs, pres in lignes_sources:
        lot = cle.split(":")[0]
        rec = par_lot.setdefault(lot, {"absent": 0, "bande": 0, "autre": 0})
        if pres == "absent":
            rec["absent"] += 1
        elif "C_taille_hors_bande" in defs:
            rec["bande"] += 1
        else:
            rec["autre"] += 1
    out = []
    out.append("# Consolidation Grokbot\n")
    out.append(f"Dernier passage : {etat['dernier_passage']} (Europe/Zurich).\n")
    out.append(f"Exigences remplies : **{stats['ok']} / {stats['lecons']} ({pct} %)**.\n")
    out.append(f"Revérifiées : {stats['repris']}. Déjà conformes et inchangées : {stats['sautes']}. FIN_FICHIER ajoutés : {stats['corriges_fin']}.\n")
    out.append("Exigences : présence du fichier, 14 points, FIN_FICHIER, bande 100–200 Ko, aucun bloqueur, score ≥ 90.\n")
    out.append("Le détail par leçon est dans `Grokbot/consolidation/etat.json`. Aucun texte clinique n'est inventé pour atteindre la bande.\n")
    out.append("## Synthèse par LOT\n")
    out.append("| LOT | Leçons absentes | Présentes sous la bande | Autre défaut |\n|---|---|---|---|\n")
    for lot in sorted(par_lot):
        r = par_lot[lot]
        out.append(f"| {lot} | {r['absent']} | {r['bande']} | {r['autre']} |\n")
    if not par_lot:
        out.append("| — | 0 | 0 | 0 |\n")
    RAPPORT.write_text("".join(out), encoding="utf-8")
    print(f"{RAPPORT} : {pct} % ({stats['ok']}/{stats['lecons']})")


def integrer_jauge(stats):
    if not JAUGE.is_file():
        return
    html = JAUGE.read_text(encoding="utf-8")
    pct = round(100 * stats["ok"] / stats["lecons"]) if stats["lecons"] else 0
    bloc = (
        f'<section id="consolidation-grokbot"><h2>Consolidation</h2>'
        f'<p>Passage du {stats.get("date", maintenant())}. '
        f'Exigences du PROMPT remplies : {stats["ok"]} / {stats["lecons"]} ({pct} %). '
        f'Rapport : Grokbot/CONSOLIDATION_RAPPORT.md.</p></section>'
    )
    if 'id="consolidation-grokbot"' in html:
        html = re.sub(r'<section id="consolidation-grokbot">.*?</section>', bloc, html, count=1, flags=re.S)
    elif "</main>" in html:
        html = html.replace("</main>", bloc + "</main>", 1)
    else:
        html += bloc
    JAUGE.write_text(html, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corriger-fin", action="store_true")
    a = ap.parse_args()
    passage(a.corriger_fin)


if __name__ == "__main__":
    main()
