"""Quatre portes. Une image n'est acceptée que si les quatre sont ouvertes."""
import os
import attestations as A
import anonymiser
import licences as L
import validate as V


NOMS = ("licence", "age_sexe", "sexe_region", "anonymisation")


def porte_licence(c):
    raison = L.raison_licence(c.get("license"), c.get("author"), c.get("source_url"))
    if raison:
        return False, raison
    c["license"] = L.normaliser(c.get("license"))
    return True, "liste blanche, auteur et URL"


def porte_age_sexe(c):
    if c.get("age_ans") is None or c.get("sex") not in ("M", "F"):
        return False, "âge ou sexe non attesté"
    if c.get("adulte") == "oui":
        return True, f"adulte {c['age_ans']} ans, sexe {c['sex']}"
    return True, f"mineur {c['age_ans']} ans, sexe {c['sex']} (adulte prioritaire s'il existe)"


def porte_sexe_region(c, dx, vis_a_vis=None):
    requis = A.sexe_region({"dx": c.get("dx", ""), "cliche": c.get("cliche", ""),
                            "normal": {}, "patho": {}}, dx)
    if not requis:
        return True, "région sans exigence de sexe concordant"
    if c.get("sex") not in ("M", "F"):
        return False, "bassin, sein ou organes génitaux : sexe non attesté"
    if vis_a_vis and vis_a_vis.get("sex") in ("M", "F") and vis_a_vis["sex"] != c["sex"]:
        return False, "sexe discordant sur le bassin, le sein ou les organes génitaux"
    return True, "sexe attesté pour la région concernée"


def porte_anonymisation(c, dest):
    src = c.get("fichier")
    if not src or not os.path.isfile(src):
        return False, "fichier absent, anonymisation non vérifiée"
    res = anonymiser.anonymiser(src, dest)
    c["anonymisation_verifiee"] = "oui" if res["ok"] else "non"
    c["masques"] = res["masques"]
    if res["ok"]:
        c["fichier"] = dest
    return res["ok"], res["raison"] + (f" ({res['masques']} zone(s))" if res["masques"] else "")


def evaluer(c, dx, dest, vis_a_vis=None):
    """Renseigne c['portes']. ok seulement si les quatre passent."""
    portes = []
    ok, raison = porte_licence(c)
    portes.append({"nom": "licence", "ok": ok, "raison": raison})
    if ok:
        ok, raison = porte_age_sexe(c)
        portes.append({"nom": "age_sexe", "ok": ok, "raison": raison})
    else:
        portes.append({"nom": "age_sexe", "ok": False, "raison": "non exécutée : licence fermée"})
    if portes[-1]["ok"]:
        ok, raison = porte_sexe_region(c, dx, vis_a_vis)
        portes.append({"nom": "sexe_region", "ok": ok, "raison": raison})
    else:
        portes.append({"nom": "sexe_region", "ok": False, "raison": "non exécutée : porte précédente fermée"})
    if portes[-1]["ok"]:
        ok, raison = porte_anonymisation(c, dest)
        portes.append({"nom": "anonymisation", "ok": ok, "raison": raison})
    else:
        portes.append({"nom": "anonymisation", "ok": False, "raison": "non exécutée : porte précédente fermée"})
    c["portes"] = portes
    c["portes_ok"] = all(p["ok"] for p in portes)
    if not c["portes_ok"]:
        fermee = next(p for p in portes if not p["ok"])
        c["refus"] = {"porte": fermee["nom"], "raison": fermee["raison"]}
    return c["portes_ok"]


def sexe_code(v):
    return V.sex_code(v)
