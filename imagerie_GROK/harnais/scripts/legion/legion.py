#!/usr/bin/env python3
"""Orchestrateur unique. Sous-commandes idempotentes. Ne pose jamais « complet »."""
import argparse, os, shutil, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(ICI)
sys.path.insert(0, ICI)
sys.path.insert(0, SCRIPTS)

import apparier
import chercher
import injecter
import rapport
import recepteur
import segmenter
import socle


def _ids(args):
    if getattr(args, "ids", ""):
        return [x.strip() for x in args.ids.split(",") if x.strip()]
    return socle.choisir(getattr(args, "limit", 10) or 10)


def _sous(script, *plus):
    return subprocess.run([sys.executable, os.path.join(SCRIPTS, script), *plus], cwd=socle.ROOT).returncode


def cmd_inventaire(args):
    ids = _ids(args)
    for i in ids:
        m, _ = socle.manifeste(i)
        print(f"{i}\t{m.get('cliche', '')}\t{m.get('dx', '')}")
    print(f"{len(ids)} introuvable(s)")
    return 0


def cmd_fetch(args):
    code = 0
    for mid in _ids(args):
        try:
            etat = chercher.chercher(mid, force=args.force)
            print(f"{mid}\tcandidats {len(etat.get('candidats') or [])}\trefus {len(etat.get('refus_fetch') or [])}")
        except Exception as e:
            socle.journal("erreur", id=mid, etape="fetch", erreur=type(e).__name__)
            print(mid, "ERREUR", type(e).__name__)
            code = 1
    return code


def cmd_gate(args):
    code = 0
    for mid in _ids(args):
        try:
            etat = chercher.filtrer(mid, force=args.force)
            print(f"{mid}\tacceptées {len(etat.get('acceptes') or [])}\trefus {len(etat.get('refus_gate') or [])}")
        except Exception as e:
            socle.journal("erreur", id=mid, etape="gate", erreur=type(e).__name__)
            print(mid, "ERREUR", type(e).__name__)
            code = 1
    return code


def cmd_normalize(args):
    for mid in _ids(args):
        etat = apparier.preparer(mid, force=args.force)
        print(mid, "normalisées", len(etat.get("acceptes") or []))
    return 0


def cmd_pair(args):
    cfg = socle.lire_json(socle.CONFIG, {}) or {}
    for mid in _ids(args):
        etat = apparier.apparier(mid, cfg=cfg, force=args.force)
        print(mid, etat.get("raison_paire") or "")
    return 0


def cmd_segment(args):
    for mid in _ids(args):
        etat = segmenter.executer(mid, force=args.force)
        seg = etat.get("segment") or {}
        print(mid, seg.get("raison") or seg.get("methode") or "")
    return 0


def cmd_build(args):
    plus = []
    if args.external or not args.out:
        plus.append("--external")
    if args.include_test:
        plus.append("--include-test")
    if args.only:
        plus += ["--only", args.only]
    out = args.out or os.path.join(socle.DEMO, "Radio_Paires.html")
    if not args.out:
        print("Page de démonstration. Le fichier publié app/Radio_Paires.html (53 Mo) n'est pas réécrit.")
    plus += ["--out", out]
    return _sous("build_app.py", *plus)


def cmd_capture(args):
    html = args.html or os.path.join(socle.DEMO, "Radio_Paires.html")
    if not os.path.isfile(html):
        print("page absente :", html)
        return 1
    tag = args.tag or "legion"
    plus = ["--html", html, "--tag", tag]
    if args.ids:
        plus += ["--ids", args.ids]
    code = _sous("screenshot.py", *plus)
    dest = os.path.join(socle.DEMO, "captures")
    os.makedirs(dest, exist_ok=True)
    src = os.path.join(socle.ROOT, "shots")
    if os.path.isdir(src):
        for nom in os.listdir(src):
            if nom.startswith(tag + "_") and nom.endswith(".png"):
                shutil.copy2(os.path.join(src, nom), os.path.join(dest, nom))
    return code


def cmd_validate(args):
    plus = ["--quiet"]
    if args.ids:
        plus += ["--only", args.ids]
    if getattr(args, "include_test", False):
        plus.append("--include-test")
    return _sous("validate.py", *plus)


def cmd_report(args):
    ids = _ids(args) if args.ids else None
    res = rapport.bilan(ids)
    print(f"acceptées {res['acceptes']} · refusées {res['refusees']} · insérées {res['inserees']}")
    print(os.path.join(socle.RAPPORTS, "BILAN.md"))
    return 0


def cmd_run(args):
    ids = _ids(args)
    print("Introuvables :", ", ".join(ids))
    socle.ecrire_json(os.path.join(socle.RAPPORTS, "SELECTION.json"), {"ids": ids})
    args.ids = ",".join(ids)
    cmd_fetch(args)
    cmd_gate(args)
    cmd_normalize(args)
    cmd_pair(args)
    cmd_segment(args)
    cmd_report(args)
    return cmd_validate(args)


def cmd_entrant(args):
    res = injecter.traiter(construire_page=args.build)
    for r in res["resultats"]:
        print(("OK " if r.get("ok") else "REFUS ") + r.get("fichier", ""))
    if res.get("page"):
        print("page", res["page"])
    return 0 if any(r.get("ok") for r in res["resultats"]) or res["resultats"] else 0


def cmd_consigne(args):
    res = recepteur.appliquer(relancer=not args.sans_relance, out=args.out or None, only=args.only)
    print(f"file {len(res['file'])}")
    if res["page"]:
        print(res["page"], "build", res["build"], "validate", res["validate"])
    return 0 if res["build"] == 0 and res["validate"] == 0 else 1


def main(argv=None):
    p = argparse.ArgumentParser(prog="legion", description="Légion du harnais Radio-Paires")
    sub = p.add_subparsers(dest="cmd", required=True)

    def commun(sp):
        sp.add_argument("--ids", default="")
        sp.add_argument("--limit", type=int, default=10)
        sp.add_argument("--force", action="store_true")

    for nom, fn, aide in (
        ("inventaire", cmd_inventaire, "Lister des introuvables"),
        ("fetch", cmd_fetch, "Commons, Open-i, Europe PMC"),
        ("gate", cmd_gate, "Quatre portes"),
        ("normalize", cmd_normalize, "JPEG ≤ 1024"),
        ("pair", cmd_pair, "Taille et tranche d'âge"),
        ("segment", cmd_segment, "Contour scikit-image, sans promotion"),
        ("report", cmd_report, "JSON et Markdown par paire"),
        ("run", cmd_run, "fetch, gate, normalize, pair, segment, report, validate"),
    ):
        sp = sub.add_parser(nom, help=aide)
        commun(sp)
        sp.set_defaults(fn=fn)
    sp = sub.add_parser("build", help="build_app.py")
    sp.add_argument("--out", default="")
    sp.add_argument("--only", default="")
    sp.add_argument("--external", action="store_true")
    sp.add_argument("--include-test", action="store_true")
    sp.set_defaults(fn=cmd_build)
    sp = sub.add_parser("capture", help="screenshot.py (Playwright)")
    sp.add_argument("--html", default="")
    sp.add_argument("--ids", default="")
    sp.add_argument("--tag", default="legion")
    sp.set_defaults(fn=cmd_capture)
    sp = sub.add_parser("validate", help="validate.py")
    sp.add_argument("--ids", default="")
    sp.add_argument("--include-test", action="store_true")
    sp.set_defaults(fn=cmd_validate)
    sp = sub.add_parser("entrant", help="Dossier entrant/")
    sp.add_argument("--build", action="store_true")
    sp.set_defaults(fn=cmd_entrant)
    sp = sub.add_parser("consigne", help="CONSIGNES_VIAL.md → interface.json")
    sp.add_argument("--sans-relance", action="store_true")
    sp.add_argument("--out", default="")
    sp.add_argument("--only", default="IMG-001")
    sp.set_defaults(fn=cmd_consigne)
    args = p.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
