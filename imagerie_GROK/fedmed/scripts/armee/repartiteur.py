#!/usr/bin/env python3
"""Envoie chaque introuvable aux éclaireurs de sa modalité. MIN avant CIBLE. Reprise par cache."""
import importlib.util
import json
import sys
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parents[2] / "harnais" / "scripts"))
sys.path.insert(0, str(ICI.parents[2] / "harnais" / "scripts" / "legion"))
sys.path.insert(0, str(ICI))

import besoins as B
import portes
from base import ETAT, get

NOMS = (
    "commons", "europepmc", "pmc_oa", "openi", "medpix2", "idc", "tcia", "vindr",
    "nih_cxr14", "isic", "odir", "ptbxl", "sleep_edf", "ctu_uhb", "openneuro",
    "kvasir", "zenodo_figshare",
)
def _scout(nom):
    spec = importlib.util.spec_from_file_location(f"armee_{nom}", ICI / f"{nom}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SCOUTS = {nom: _scout(nom) for nom in NOMS}
ENTRANT = ICI.parents[2] / "harnais" / "entrant"
COTE_FORCE = {"IMG-226": "patho", "IMG-293": "normal", "EXP-027": "patho", "EXP-090": "normal"}


def _octets(cand):
    if cand.get("octets"):
        return cand["octets"], ""
    if cand.get("pipeline") == "A" and cand.get("img_url"):
        try:
            return get(cand["img_url"], binaire=True, timeout=25), ""
        except Exception as exc:
            return None, f"téléchargement impossible ({type(exc).__name__})"
    if cand.get("pipeline") in ("B", "D") and cand.get("viewer_url"):
        from capture import capturer
        dest = ETAT / "_captures" / f"{cand.get('titre','vue')}.png"
        ok, msg = capturer(cand["viewer_url"], dest)
        if not ok:
            return None, msg
        return dest.read_bytes(), ""
    return None, "pas de fichier direct et pas de capture utile"


def _deposer(besoin, jpeg, cand, mention):
    ENTRANT.mkdir(parents=True, exist_ok=True)
    nom = f"{besoin['id']}_{besoin['cote']}.jpg"
    (ENTRANT / nom).write_bytes(jpeg)
    meta = {
        "id": besoin["id"],
        "cote": besoin["cote"],
        "source": cand.get("url") or "",
        "licence": cand.get("license") or "",
        "auteur": (cand.get("author") or "auteur de la notice")[:160],
        "age": cand.get("age_ans") if isinstance(cand.get("age_ans"), int) else "",
        "sexe": cand.get("sex") if cand.get("sex") in ("M", "F") else "",
        "note": mention,
    }
    (ENTRANT / f"{besoin['id']}_{besoin['cote']}.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")


def traiter(besoin):
    dest = ETAT / f"{besoin['id']}.json"
    if dest.is_file():
        ancien = json.loads(dest.read_text(encoding="utf-8"))
        if ancien.get("clos"):
            return ancien
    rapport = {"id": besoin["id"], "niveau": besoin["niveau"], "cote": besoin["cote"],
               "modalite": besoin["modalite"], "sources": {}, "retenu": None, "clos": False}
    for source in besoin["sources"]:
        try:
            res = SCOUTS[source].chercher(besoin)
        except Exception as exc:
            rapport["sources"][source] = {"n": 0, "raison": type(exc).__name__}
            continue
        rapport["sources"][source] = {"n": len(res.get("candidats") or []), "raison": res.get("raison") or ""}
        for cand in res.get("candidats") or []:
            octets, err = _octets(cand)
            if not octets:
                rapport["sources"][source]["raison"] = err or rapport["sources"][source]["raison"]
                continue
            try:
                ok, mention, jpeg = portes.evaluer(cand, besoin, octets)
            except Exception as exc:
                rapport["sources"][source]["raison"] = f"image illisible ({type(exc).__name__})"
                continue
            if not ok:
                rapport["sources"][source]["raison"] = mention
                continue
            portes.ecrire_provenance(besoin["id"], besoin["cote"], cand, mention)
            _deposer(besoin, jpeg, cand, mention)
            rapport["retenu"] = {"source": source, "mention": mention, "url": cand.get("url")}
            break
        if rapport["retenu"]:
            break
    rapport["clos"] = True
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(rapport, ensure_ascii=False, indent=1), encoding="utf-8")
    print(besoin["id"], rapport["retenu"]["source"] if rapport["retenu"] else "rien", flush=True)
    return rapport


def main():
    tout = B.charger()
    for besoin in tout:
        if besoin["id"] in COTE_FORCE:
            besoin["cote"] = COTE_FORCE[besoin["id"]]
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg.isdigit():
        tout = tout[: int(arg)]
    elif arg:
        voulus = set(arg.split(","))
        tout = [b for b in tout if b["id"] in voulus]
    faits = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futurs = [pool.submit(traiter, b) for b in tout]
        for fut in as_completed(futurs):
            try:
                faits.append(fut.result())
            except Exception:
                traceback.print_exc()
    retenus = [f for f in faits if f.get("retenu")]
    print(f"besoins {len(tout)} retenus {len(retenus)}")
    if retenus:
        legion_dir = str(ICI.parents[2] / "harnais" / "scripts" / "legion")
        sys.path.insert(0, legion_dir)
        for nom in ("portes", "injecter"):
            sys.modules.pop(nom, None)
        import injecter
        res = injecter.traiter()
        print(res.get("resultats"))
        _vers_page(res.get("resultats") or [])
    _bilan()


def _bilan():
    """Comptes par source et par entrée, pour CONTROLE.md et PROGRESSION.md."""
    lignes = []
    if not ETAT.is_dir():
        return
    par_source = {}
    retenus = []
    restes = []
    for path in sorted(ETAT.glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        if doc.get("retenu"):
            retenus.append(doc)
            src = doc["retenu"]["source"]
            par_source[src] = par_source.get(src, 0) + 1
        else:
            raisons = []
            for nom, info in (doc.get("sources") or {}).items():
                if info.get("raison"):
                    raisons.append(f"{nom}: {info['raison']}")
                    par_source.setdefault(nom, 0)
            restes.append((doc["id"], " ; ".join(raisons)[:240] or "aucun candidat"))
    fed = ICI.parents[1]
    controle = [
        "# Contrôle — armée des sources",
        "",
        f"Introuvables examinés : {len(retenus) + len(restes)}.",
        f"Récupérés : {len(retenus)}. Restés introuvables : {len(restes)}.",
        "",
        "## Comptes par source",
        "",
    ]
    for nom in NOMS:
        controle.append(f"- {nom} : {par_source.get(nom, 0)} retenu(s)")
    controle += ["", "## Récupérés", ""]
    for doc in retenus:
        controle.append(f"- {doc['id']} ({doc.get('cote')}) via {doc['retenu']['source']} — {doc['retenu'].get('mention')}")
    controle += ["", "## Restés introuvables", ""]
    for ident, raison in restes:
        controle.append(f"- {ident} — {raison}")
    path = fed / "CONTROLE.md"
    ancien = path.read_text(encoding="utf-8") if path.is_file() else ""
    if "## Armée des sources" in ancien:
        ancien = ancien.split("## Armée des sources")[0].rstrip() + "\n"
    path.write_text(ancien + "\n" + "\n".join(controle).replace("# Contrôle — armée des sources", "## Armée des sources") + "\n", encoding="utf-8")
    prog = fed / "PROGRESSION.md"
    bloc = [
        "",
        "## Armée des sources",
        "",
        f"- Examinés : {len(retenus) + len(restes)}",
        f"- Récupérés : {len(retenus)}",
        f"- Restés introuvables : {len(restes)}",
        "",
    ]
    for nom in NOMS:
        bloc.append(f"- {nom} : {par_source.get(nom, 0)}")
    if prog.is_file():
        texte = prog.read_text(encoding="utf-8")
        if "## Armée des sources" in texte:
            texte = texte.split("## Armée des sources")[0].rstrip() + "\n"
        prog.write_text(texte + "\n".join(bloc) + "\n", encoding="utf-8")


def _vers_page(resultats):
    """Pose l'image acceptée par la légion sur la fenêtre FedMed du même identifiant."""
    fed = ICI.parents[2] / "fedmed"
    sys.path.insert(0, str(ICI.parents[0]))
    import commun as C
    for rec in resultats:
        if not rec.get("ok") or not rec.get("id"):
            continue
        ident = rec["id"]
        fusion_path = fed / "fusion" / f"{ident}.json"
        fiche_path = fed / "fenetres" / f"{ident}.json"
        if not fusion_path.is_file():
            continue
        cote = COTE_FORCE.get(ident, "patho")
        src = ENTRANT / f"{ident}_{cote}.jpg"
        if not src.is_file():
            continue
        dest = fed / "fenetres" / "images" / f"{ident}_{cote}.jpg"
        dest.write_bytes(src.read_bytes())
        fusion = C.lire_json(fusion_path)
        fiche = C.lire_json(fiche_path)
        g = fusion["gabarit"].setdefault(cote, {})
        g["refus"] = ""
        g["aspect_adulte"] = True
        g["age"] = ""
        g["source"] = {"auteur": "", "licence": "", "url": "", "credit": "déposé par la légion"}
        prov = fed / "sources" / "provenance" / f"{ident}_{cote}.json"
        if prov.is_file():
            meta = json.loads(prov.read_text(encoding="utf-8"))
            g["source"] = {
                "auteur": meta.get("auteur") or "",
                "licence": meta.get("licence") or "",
                "url": meta.get("url") or "",
                "credit": meta.get("mention") or "",
            }
            if isinstance(meta.get("age"), int):
                g["age"] = f"{meta['age']} ans"
                g["aspect_adulte"] = False
            if meta.get("sexe") == "M":
                g["sexe"] = "homme"
            elif meta.get("sexe") == "F":
                g["sexe"] = "femme"
        im = fiche.setdefault("enr", {}).setdefault("images", {})
        im[cote] = {
            "fichier": f"images/{ident}_{cote}.jpg",
            "technique": (fiche.get("contexte") or {}).get("cliche") or "",
            "credit": g["source"].get("auteur") or "",
            "licence": g["source"].get("licence") or "",
            "url": g["source"].get("url") or "",
        }
        fiche.setdefault("mime", {})[cote] = "image/jpeg"
        if cote == "normal":
            fusion.pop("normal_ajoute", None)
            retraits = fusion.get("retraits") or {}
            retraits.pop("normal", None)
            if retraits:
                fusion["retraits"] = retraits
            elif "retraits" in fusion:
                fusion.pop("retraits")
        C.ecrire_json(fusion_path, fusion)
        C.ecrire_json(fiche_path, fiche)


if __name__ == "__main__":
    main()
