"""Taille et tranche d'âge. Ne promeut jamais un manifeste au statut complet."""
import os
import attestations as A
import socle


def normaliser_fichier(path):
    from normalize import normalize
    w, h = normalize(path, path)
    return w, h


def _ratio(a, b):
    if min(a, b) <= 0:
        return 99
    return max(a, b) / float(min(a, b))


def taille_comparable(s1, s2):
    if _ratio(max(s1), max(s2)) > 1.5:
        return False
    a1, a2 = s1[0] / float(s1[1]), s2[0] / float(s2[1])
    return _ratio(a1, a2) <= 1.35


def preparer(mid, force=False):
    etat = socle.charger(mid)
    cle = socle.cle("norm", socle.VERSION, [c.get("cle_dl") for c in etat.get("acceptes") or []])
    if not force and etat.get("cle_norm") == cle and etat.get("acceptes") is not None:
        return etat
    for c in etat.get("acceptes") or []:
        p = c.get("fichier")
        if not p or not os.path.isfile(p):
            c["taille"] = None
            continue
        w, h = normaliser_fichier(p)
        c["taille"] = [w, h]
    etat["cle_norm"] = cle
    socle.sauver(etat)
    socle.journal("normalize", id=mid, n=len(etat.get("acceptes") or []))
    return etat


def apparier(mid, cfg=None, force=False):
    etat = preparer(mid, force=force) if force else socle.charger(mid)
    if "cle_norm" not in etat:
        etat = preparer(mid, force=False)
    acceptes = etat.get("acceptes") or []
    adultes = [c for c in acceptes if c.get("adulte") == "oui"]
    pool = adultes if adultes else acceptes
    if adultes and len(adultes) < len(acceptes):
        etat["priorite_adulte"] = "des mineurs attestés ont été écartés : un adulte est disponible"
    else:
        etat["priorite_adulte"] = ""
    normals = [c for c in pool if c.get("cote") == "normal" and c.get("taille")]
    pathos = [c for c in pool if c.get("cote") == "patho" and c.get("taille")]
    raison = ""
    choix = None
    if not normals or not pathos:
        raison = "pas de vis-à-vis normal et pathologique après les quatre portes"
    else:
        dx = {"region": etat.get("region"), "dx": etat.get("dx"), "cliche": etat.get("cliche")}
        requis = A.sexe_region({}, dx)
        meilleur = None
        for n in normals:
            for p in pathos:
                if not A.ages_comparables(n.get("age_ans"), p.get("age_ans"), cfg):
                    continue
                if requis and n.get("sex") != p.get("sex"):
                    continue
                if not taille_comparable(tuple(n["taille"]), tuple(p["taille"])):
                    continue
                ecart = abs(n["age_ans"] - p["age_ans"])
                if meilleur is None or ecart < meilleur[0]:
                    meilleur = (ecart, n, p)
        if meilleur:
            _, n, p = meilleur
            choix = {"normal": n.get("cle_dl"), "patho": p.get("cle_dl"), "ecart_ans": meilleur[0]}
            raison = "taille et tranche d'âge comparables"
        else:
            raison = "aucun couple de taille et de tranche d'âge comparables"
    etat["paire"] = choix
    etat["raison_paire"] = raison
    if choix and etat.get("statut_pose") != "partiel":
        _inserer(mid, etat, choix)
    socle.sauver(etat)
    socle.journal("pair", id=mid, paire=bool(choix), raison=raison)
    return etat


def _bloc(c, fichier):
    return {
        "file": fichier,
        "source_url": c.get("source_url") or "",
        "license": c.get("license") or "",
        "license_url": c.get("license_url") or "",
        "author": c.get("author") or "",
        "sex": c.get("sex") or "À vérifier",
        "adulte": c.get("adulte") or "À vérifier",
        "adulte_preuve": ("Légende : « " + c["preuve_age"] + " », sexe " + c.get("sex", "") + ".")
        if c.get("preuve_age") else "À vérifier",
        "age_ans": c.get("age_ans"),
        "anonymisation_verifiee": "oui" if c.get("anonymisation_verifiee") == "oui" else "non",
        "caption_source": ("Âge attesté (" + c.get("preuve_age", "") + "). Légende intégrale non recopiée."),
        "note": "Retenue par la légion après les quatre portes. Contour non relu : statut partiel.",
    }


def _inserer(mid, etat, choix):
    """Copie les JPEG et pose un partiel. Refus net si le manifeste est déjà complet."""
    m, path = socle.manifeste(mid)
    if not m:
        return
    if m.get("statut") == "complet":
        etat["insertion"] = "refusée : le manifeste est déjà complet, la légion n'y touche pas"
        return
    by = {c.get("cle_dl"): c for c in etat.get("acceptes") or []}
    n, p = by.get(choix["normal"]), by.get(choix["patho"])
    if not n or not p:
        return
    dest_n = os.path.join("images", "normal", f"{mid}_normal.jpg")
    dest_p = os.path.join("images", "patho", f"{mid}_patho.jpg")
    for src, rel in ((n["fichier"], dest_n), (p["fichier"], dest_p)):
        abs_dest = os.path.join(socle.ROOT, rel)
        os.makedirs(os.path.dirname(abs_dest), exist_ok=True)
        with open(src, "rb") as i, open(abs_dest, "wb") as o:
            o.write(i.read())
    m["normal"] = _bloc(n, dest_n)
    m["patho"] = _bloc(p, dest_p)
    m["statut"] = "partiel"
    m["pair_match"] = (
        "Paire retenue par la légion : licence, âge, sexe, anonymisation, taille et tranche d'âge. "
        "Pas de flèche relue ni de définition sourcée : le statut reste partiel."
    )
    note = "Contour et signe non relus à l'œil."
    av = m.setdefault("a_verifier", [])
    if note not in av:
        av.append(note)
    socle.ecrire_json(path, m)
    etat["insertion"] = "partiel"
    etat["statut_pose"] = "partiel"
