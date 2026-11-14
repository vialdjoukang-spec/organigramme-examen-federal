"""État JSON et Markdown par paire. Aucun identifiant patient."""
import os
import socle


def _refus(etat):
    return list(etat.get("refus_fetch") or []) + list(etat.get("refus_gate") or [])


def rediger(mid):
    etat = socle.charger(mid)
    if not etat.get("cle_fetch") and not etat.get("insertion"):
        return None
    refus = _refus(etat)
    acceptes = etat.get("acceptes") or []
    doc = {
        "id": mid,
        "dx": etat.get("dx") or "",
        "cliche": etat.get("cliche") or "",
        "acceptes": len(acceptes),
        "refusees": len(refus),
        "paire": bool(etat.get("paire")),
        "insertion": etat.get("insertion") or "aucune",
        "complet_force": False,
        "raison_paire": etat.get("raison_paire") or "",
        "priorite_adulte": etat.get("priorite_adulte") or "",
        "segment": etat.get("segment") or {},
        "refus": refus,
        "acceptes_detail": [
            {k: c.get(k) for k in ("origine", "titre", "source_url", "license", "age_ans", "sex", "adulte", "masques", "cote")}
            for c in acceptes
        ],
    }
    socle.ecrire_json(os.path.join(socle.RAPPORTS, mid + ".json"), doc)
    lignes = [
        f"# {mid}",
        "",
        f"- Diagnostic : {doc['dx']}",
        f"- Cliché : {doc['cliche']}",
        f"- Acceptées (quatre portes) : {doc['acceptes']}",
        f"- Refusées : {doc['refusees']}",
        f"- Paire : {'oui' if doc['paire'] else 'non'} — {doc['raison_paire']}",
        f"- Insertion : {doc['insertion']}",
        "- Complet forcé : non",
        "",
    ]
    if doc["priorite_adulte"]:
        lignes += [doc["priorite_adulte"], ""]
    if doc["segment"]:
        lignes += [f"- Segmentation : {doc['segment'].get('raison') or doc['segment'].get('methode') or doc['segment']}", ""]
    if refus:
        lignes += ["## Refus", ""]
        for r in refus:
            lignes.append(f"- {r.get('origine') or '—'} | {r.get('porte')} | {r.get('raison')}")
        lignes.append("")
    if acceptes:
        lignes += ["## Acceptées", ""]
        for c in doc["acceptes_detail"]:
            lignes.append(
                f"- {c.get('origine')} | {c.get('titre') or '—'} | {c.get('license')} | {c.get('age_ans')} ans {c.get('sex')} | {c.get('source_url')}"
            )
        lignes.append("")
    with open(os.path.join(socle.RAPPORTS, mid + ".md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lignes))
    return doc


def bilan(ids=None):
    if ids is None:
        ids = []
        for nom in sorted(os.listdir(socle.ETAT)):
            if nom.endswith(".json"):
                ids.append(nom[:-5])
    docs = [d for d in (rediger(i) for i in ids) if d]
    total_a = sum(d["acceptes"] for d in docs)
    total_r = sum(d["refusees"] for d in docs)
    raisons = {}
    for d in docs:
        for r in d["refus"]:
            cle = f"{r.get('porte')} — {r.get('raison')}"
            raisons[cle] = raisons.get(cle, 0) + 1
    resume = {
        "paires": len(docs),
        "acceptes": total_a,
        "refusees": total_r,
        "inserees": sum(1 for d in docs if d["insertion"] not in ("", "aucune")),
        "complets_forces": 0,
        "raisons": raisons,
        "ids": [d["id"] for d in docs],
    }
    socle.ecrire_json(os.path.join(socle.RAPPORTS, "BILAN.json"), resume)
    lignes = [
        "# Bilan de la légion",
        "",
        f"- Paires traitées : {resume['paires']}",
        f"- Images acceptées (quatre portes) : {resume['acceptes']}",
        f"- Images refusées : {resume['refusees']}",
        f"- Manifestes touchés (partiel, jamais complet) : {resume['inserees']}",
        "",
        "## Raisons de refus",
        "",
    ]
    for cle, n in sorted(raisons.items(), key=lambda kv: (-kv[1], kv[0])):
        lignes.append(f"- {n} × {cle}")
    if not raisons:
        lignes.append("- aucun refus enregistré")
    lignes.append("")
    entree = socle.lire_json(os.path.join(socle.RAPPORTS, "ENTRANT.json"), None)
    if entree:
        lignes += ["## Dépôt entrant", ""]
        for r in entree.get("resultats") or []:
            lignes.append(f"- {'accepté' if r.get('ok') else 'refusé'} : {r.get('fichier')} ({r.get('id') or 'sans id'})")
        if entree.get("page"):
            lignes.append(f"- Page : {entree['page']}")
        lignes.append("")
    with open(os.path.join(socle.RAPPORTS, "BILAN.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lignes))
    return resume
