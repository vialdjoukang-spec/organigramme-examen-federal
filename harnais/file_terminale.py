#!/usr/bin/env python3
"""File terminale : tout ce qui reste, dans l'ordre, avec dépendances et prompts prêts (zéro jeton).

  python3 harnais/file_terminale.py init            construit journal/FILE_TERMINALE.json (n'écrase pas les statuts existants)
  python3 harnais/file_terminale.py prochaines [N]  N tâches lançables (dépendances faites), JSON {id, description, subagent_type, prompt}
  python3 harnais/file_terminale.py lance <id>      statut « lancé »
  python3 harnais/file_terminale.py fait <id>       statut « fait »
  python3 harnais/file_terminale.py etat            décompte par statut et par LOT

Ordre : LOT_011 (fin + audit), LOT_010 → LOT_001 (Phase A, DX, audit croisé), puis LOT_017 (achèvement V0, audits, refonte V8, audit croisé).
Le nombre de lancements simultanés est fixé par harnais/gouverneur.py --lancer ; l'effort est toujours celui du contrat (xhigh pour Opus).
"""
import json, re, sys
from pathlib import Path

R = Path(__file__).resolve().parents[1]
F = R / "journal" / "FILE_TERMINALE.json"
FIN = R / "LOT_Claude_Finaux"
PROD = R / "lot en cours de production"
V8 = R / "LOTS_V8"

REGLES = ("AIPS = information professionnelle suisse du médicament (Swissmedic), jamais « Compendium ». Pièges : garde ceux de la source, n'ajoute aucun fait. "
          "N'ajoute aucun lien que tu n'as pas lu (doi/PMID de la source → doi.org / pubmed). Doses AIPS suisse seulement ; une dose « hors AIPS » se signale sans valeur de consigne ; toute dose attribuée à l'AIPS se vérifie dans l'AIPS locale (`.cache/aips`, `ressources_ia/aips/fi_fr`). "
          "N'attribue jamais une source à un fait que la source n'y rattache pas. Si la source contient une erreur médicale manifeste, ne la recopie pas comme vraie : signale-la et marque-la « À vérifier ». "
          "Tableaux lisibles sur téléphone (390 px). Contrôle du rendu avec Playwright. Fichiers de travail dans un sous-dossier propre du scratchpad. Aucun commit ; rapport bref.")


def p_refonte(lot, nom, src):
    brief = "/home/user/organigramme-examen-federal/harnais/briefs/REFONTE_V8.md"
    sortie = f"LOTS_V8/{lot}/{Path(src).name}"
    if nom == "Phase_A":
        return (f"Applique `{brief}` (lis-la en entier, règles récentes comprises) pour LOT={lot}, source `{src}`, sortie `{sortie}` "
                f"(Phase A : fiche x ≤ 100 Ko, vérification avec `--phase-a`). Vérifie d'abord le format de la source et le nombre de DX (LISTE_DX_CANONIQUE.md) et signale tout écart ; "
                f"format ancien (`abbr[data-k]`, infobulles `.tm/.df`, fiches `:target`, tableaux non fermés) : convertis tout en `abbr title` et fenêtres popover. {REGLES}")
    return (f"Applique `{brief}` (lis-la en entier, règles récentes comprises) pour LOT={lot}, source `{src}`, sortie `{sortie}`, "
            f"`--ref LOTS_V8/{lot}/{lot}_Phase_A_V0.html` (Phase A V8 terminée : tout retrait pour redondance doit y figurer mot pour mot, doses comprises, sinon garde-le en fenêtre). "
            f"Titre en `<h1>` comme le modèle. Format ancien éventuel : convertis `abbr[data-k]` en `abbr title`, infobulles `.tm/.df` et fiches `:target` en fenêtres popover. {REGLES}")


def p_audit(lot, n):
    return (f"Audit croisé V8 de {lot} ({n} fichiers dans `/home/user/organigramme-examen-federal/LOTS_V8/{lot}/`), avec correction en place. Sources d'origine : "
            f"`LOT_Claude_Finaux/{lot}/` (ou `lot en cours de production/{lot}/`). Normes : `harnais/briefs/REFONTE_V8.md` (en entier), `harnais/briefs/AUDIT_MEDICAL.md`, "
            f"modèle `harnais/modele_lecon/MODELE_DD_V8.html`. Doses : AIPS suisse seulement (`.cache/aips`, `ressources_ia/aips/fi_fr`), jamais le Compendium. "
            f"Points : (1) liens de cause inventés entre faits que la source juxtapose (neutraliser ; garder ceux que la source donne) ; (2) « → » restants ; "
            f"(3) retraits pour redondance absents mot pour mot de la Phase A V8 → réintégrer ; (4) perte de texte (comparaison section par section), colonnes, "
            f"titres `<h1 id=\"titre\">` = LISTE_DX_CANONIQUE.md, élisions séparées de leur lien, `abbr` imbriquées, sources rattachées à tort, figures contrôlées à l'image (Playwright) ; "
            f"(5) doses hors AIPS signalées sans valeur de consigne, cohérence des doses entre fichiers, citations AIPS mot pour mot, erreurs médicales et contradictions entre fichiers "
            f"(trancher sur la source lue la plus fiable ; sinon « À vérifier » et liste pour Vial). Après correction : `verif_refonte.py` VERT pour tous "
            f"(`--ref LOTS_V8/{lot}/{lot}_Phase_A_V0.html` pour les DX, `--phase-a` pour la Phase A), `taille_xy.py --inscrire` sur les fichiers modifiés, "
            f"journal dans `LOT_Claude_Finaux/{lot}/audits/corrections.jsonl` (ou celui du dossier de production). Fichiers de travail dans `scratchpad/A{lot[-3:]}_xhigh/`. "
            f"Aucun commit. Rapport bref ; liste ce qui reste à décider par Vial.")


def construire():
    t = []
    def ajoute(id_, lot, desc, typ, prompt, dep):
        t.append(dict(id=id_, lot=lot, description=desc, subagent_type=typ, prompt=prompt, dep=dep, statut="attente"))
    # LOT_011 : reste des DX + audit
    lot = "LOT_011"; dx = sorted(FIN.glob(f"{lot}_*") if False else (FIN / lot).glob(f"{lot}_Phase_B_V0_DX.*.html"), key=lambda p: int(re.search(r"DX\.(\d+)", p.name)[1]))
    ajoute(f"{lot}_Phase_A", lot, f"Refonte V8 {lot} Phase A (xhigh)", "general-purpose", p_refonte(lot, "Phase_A", f"LOT_Claude_Finaux/{lot}/{lot}_Phase_A_V0.html"), [])
    ids = []
    for p in dx:
        n = re.search(r"DX\.(\d+)", p.name)[1]; i = f"{lot}_DX.{n}"; ids.append(i)
        ajoute(i, lot, f"Refonte V8 {lot} DX.{n} (xhigh)", "general-purpose", p_refonte(lot, f"DX.{n}", f"LOT_Claude_Finaux/{lot}/{p.name}"), [f"{lot}_Phase_A"])
    ajoute(f"{lot}_audit", lot, f"Audit croisé V8 {lot} (xhigh)", "general-purpose", p_audit(lot, 1 + len(dx)), [f"{lot}_Phase_A"] + ids)
    # LOT_010 → LOT_001
    for k in range(10, 0, -1):
        lot = f"LOT_{k:03d}"; d = FIN / lot
        ajoute(f"{lot}_Phase_A", lot, f"Refonte V8 {lot} Phase A (xhigh)", "general-purpose", p_refonte(lot, "Phase_A", f"LOT_Claude_Finaux/{lot}/{lot}_Phase_A_V0.html"), [])
        ids = []
        for p in sorted(d.glob(f"{lot}_Phase_B_V0_DX.*.html"), key=lambda p: int(re.search(r"DX\.(\d+)", p.name)[1])):
            n = re.search(r"DX\.(\d+)", p.name)[1]; i = f"{lot}_DX.{n}"; ids.append(i)
            ajoute(i, lot, f"Refonte V8 {lot} DX.{n} (xhigh)", "general-purpose", p_refonte(lot, f"DX.{n}", f"LOT_Claude_Finaux/{lot}/{p.name}"), [f"{lot}_Phase_A"])
        ajoute(f"{lot}_audit", lot, f"Audit croisé V8 {lot} (xhigh)", "general-purpose", p_audit(lot, 1 + len(ids)), [f"{lot}_Phase_A"] + ids)
    # LOT_017 : achèvement V0 (DX.6, 8, 9, 10), audits V0, refonte V8, audit croisé
    lot = "LOT_017"; pd = "lot en cours de production/LOT_017"
    red = []
    for n in (6, 8, 9, 10):
        i = f"{lot}_V0_DX.{n}"; red.append(i)
        ajoute(i, lot, f"Rédaction V0 {lot} DX.{n} (redacteur xhigh)", "redacteur",
               f"Lis `{pd}/BRIEF_PHASE_B.md` ; LOT={lot} ; DX.{n}. Le fichier `{pd}/{lot}_Phase_B_V0_DX.{n}.html` est inachevé ou absent : termine-le jusqu'à FIN_FICHIER "
               f"selon LISTE_DX_CANONIQUE.md (gelée) et CORRECTIONS_AUDIT.md, sans réécrire ce qui est juste. Aucun commit.", [])
    aud = []
    for n in (6, 8, 9, 10):
        i = f"{lot}_V0_audit_DX.{n}"; aud.append(i)
        ajoute(i, lot, f"Audit médical V0 {lot} DX.{n} (xhigh)", "auditeur-medical",
               f"Lis `{pd}/BRIEF_AUDIT_B.md` (ou `harnais/briefs/AUDIT_MEDICAL.md`) ; LOT={lot} ; DX.{n} ; fichier `{pd}/{lot}_Phase_B_V0_DX.{n}.html`. Aucun commit.", [f"{lot}_V0_DX.{n}"])
    ajoute(f"{lot}_Phase_A", lot, f"Refonte V8 {lot} Phase A (xhigh)", "general-purpose", p_refonte(lot, "Phase_A", f"{pd}/{lot}_Phase_A_V0.html"), [])
    ids = []
    for n in range(1, 11):
        i = f"{lot}_DX.{n}"; ids.append(i)
        dep = [f"{lot}_Phase_A"] + ([f"{lot}_V0_audit_DX.{n}"] if n in (6, 8, 9, 10) else [])
        ajoute(i, lot, f"Refonte V8 {lot} DX.{n} (xhigh)", "general-purpose", p_refonte(lot, f"DX.{n}", f"{pd}/{lot}_Phase_B_V0_DX.{n}.html"), dep)
    ajoute(f"{lot}_audit", lot, f"Audit croisé V8 {lot} (xhigh)", "general-purpose", p_audit(lot, 11), [f"{lot}_Phase_A"] + ids)
    return t


def charger():
    return json.loads(F.read_text(encoding="utf-8")) if F.exists() else []


def sauver(t):
    F.write_text(json.dumps(t, ensure_ascii=False, indent=1), encoding="utf-8")


def main(a):
    cmd = a[0] if a else "etat"
    if cmd == "init":
        anc = {x["id"]: x["statut"] for x in charger()}
        t = construire()
        for x in t:
            x["statut"] = anc.get(x["id"], x["statut"])
        sauver(t); print(len(t), "tâches")
    elif cmd == "prochaines":
        n = int(a[1]) if len(a) > 1 else 1; t = charger(); fait = {x["id"] for x in t if x["statut"] == "fait"}
        ok = [x for x in t if x["statut"] == "attente" and all(d in fait for d in x["dep"])][:n]
        print(json.dumps([{k: x[k] for k in ("id", "description", "subagent_type", "prompt")} for x in ok], ensure_ascii=False))
    elif cmd in ("lance", "fait", "attente"):
        t = charger(); st = {"lance": "lancé", "fait": "fait", "attente": "attente"}[cmd]
        for x in t:
            if x["id"] in a[1:]:
                x["statut"] = st
        sauver(t); print(cmd, " ".join(a[1:]))
    elif cmd == "etat":
        import collections
        t = charger(); c = collections.Counter(x["statut"] for x in t)
        print(f"{len(t)} tâches · " + " · ".join(f"{k} {v}" for k, v in c.items()))
        par = collections.defaultdict(collections.Counter)
        for x in t:
            par[x["lot"]][x["statut"]] += 1
        for lot, cc in par.items():
            print(f"  {lot} : " + ", ".join(f"{k} {v}" for k, v in cc.items()))
    else:
        print(__doc__); return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
