#!/usr/bin/env python3
"""Construit HELP_Organi.docx (questions de recherche pour Google Gemini) et sa version HTML.

Usage : gen_help_organi.py DOSSIER_QUESTIONS sortie.docx sortie.html
Entrées : QUESTIONS_A.json … QUESTIONS_F.json produits par les agents de synthèse.
"""
import html as H, json, os, sys, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_checklist_docx import run, para, checkbox, table, STYLES, CT, RELS, DRELS, NS

SRC, OUT_DOCX, OUT_HTML = sys.argv[1], sys.argv[2], sys.argv[3]
GROUPES = {"A": "Audits des LOT 1 à 8 (Gemini, SSP G1–G8)", "B": "Lots Claude 227 à 231",
           "C": "Lots Claude 232 à 236", "D": "Lots Claude 237 à 241", "E": "Lots Claude 242 à 246",
           "F": "Lots Claude 247, 248 et dizaine 02 (217 à 226)"}
PRIO = [("Critique", "8B0000", "FADBD8"), ("Haute", "C0392B", "FDEBD0"), ("Moyenne", "1F618D", "EBF5FB")]
PCOL = {p: (c, f) for p, c, f in PRIO}
A_FOURNIR = ("Pour cette question, fournis : (1) la recommandation suisse en vigueur — société ou autorité, titre exact, "
             "année, URL ; (2) la version la plus récente comparée à la version citée dans le cours, avec les différences ; "
             "(3) les informations cliniques, doses, posologies, voies et adaptations (rein, foie, enfant, grossesse) selon "
             "l'information professionnelle suisse AIPS (swissmedicinfo.ch) ; (4) à défaut de source suisse, la "
             "recommandation européenne la plus récente ; (5) un extrait mot pour mot de la source et sa date de consultation.")
REPONSE = ["Recommandation suisse la plus récente (société/autorité, titre, année, URL) :",
           "Version citée dans le cours et différences avec la plus récente :",
           "Informations, doses, posologies (AIPS Swissmedic, avec n° d'autorisation) :",
           "Source européenne (seulement si aucune source suisse) :",
           "Extrait mot pour mot + date de consultation :",
           "Certitude (élevée / moyenne / faible) et réserves :"]
CONSIGNES = [
    "Tu agis comme documentaliste médical suisse. Tu réponds à chaque question de ce document, dans l'ordre, sans en sauter.",
    "Tu cherches d'abord les sources suisses : OFSP, Swissmedic et l'information professionnelle AIPS (swissmedicinfo.ch), Tox Info Suisse, Fedlex, ASSM, FMH, sociétés suisses (SSMIG, SSI, SSED, SSC, SGNOR, SSGO, SSP, SGN…), Obsan et OFS.",
    "Si aucune source suisse n'existe, tu donnes la recommandation européenne la plus récente : ESC, ERS, ERC, EASL, ESCMID, ESE, EULAR, EAACI, KDIGO, EMA. Tu n'utilises jamais une recommandation exclusivement américaine.",
    "Tu compares toujours la version la plus récente avec la version que le cours utilise (indiquée dans « Contexte »). Tu nommes chaque différence de seuil, de dose ou de conduite.",
    "Pour tout médicament, tu donnes la DCI, la spécialité suisse ® réellement autorisée, la dose, la voie, le rythme et les adaptations, d'après l'AIPS. Tu signales un produit non autorisé ou retiré en Suisse.",
    "Tu ne réponds jamais de mémoire. Chaque chiffre porte sa source : titre, organisme, année, URL et date de consultation. Tu cites un extrait mot pour mot.",
    "Si tu ne trouves rien de fiable, tu écris « donnée non trouvée dans les sources consultées » et tu listes les sources consultées. Tu n'inventes jamais.",
    "Tu conserves le numéro de chaque question (ex. B-014). Tu remplis les six lignes du cadre « Réponse » sous chaque question.",
    "Tu écris en français, en phrases verbales courtes et complètes. Tu renvoies le document complété."]


def qblock(q):
    col, fill = PCOL.get(q.get("priorite", "Moyenne"), PCOL["Moyenne"])
    W = [3400, 11200]
    head = para(checkbox() + run(f"  {q['id']}  ·  priorité {q.get('priorite','')}  ·  {q.get('type','')}", b=True, sz=20, color=col), after=0)
    rows = [[head, para(run(f"LOT {q.get('lot','')} · SSP {q.get('ssp','')} · {q.get('fichier','')}", sz=17), after=0)],
            ["Emplacement", q.get("emplacement", "")],
            ["Contexte (cours actuel)", q.get("contexte", "")],
            [para(run("Question", b=True, sz=18), after=0), para(run(q["question"], b=True, sz=18, color="1A5276"), after=0)],
            ["À fournir", A_FOURNIR]]
    rows += [[(para(run("Réponse Gemini", b=True, sz=17, color="145A32"), after=0), "EAFAF1"), (para(run(r, sz=17, color="145A32"), after=0) + para(run(" ", sz=17), after=60), "FFFFFF")] for r in REPONSE]
    return table(rows, W, header_fill=fill).replace("<w:tr><w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>", "<w:tr><w:trPr><w:cantSplit/></w:trPr>", 1)


def main():
    groups = []
    for g in "ABCDEF":
        p = os.path.join(SRC, f"QUESTIONS_{g}.json")
        if os.path.exists(p):
            groups.append((g, json.load(open(p, encoding="utf-8"))))
    b, h = [], []
    b.append(para(run("HELP_Organi", b=True, sz=44, color="1A5276"), after=40))
    b.append(para(run("Questions de recherche pour Google Gemini — encyclopédie PROFILES 2023 (examen fédéral suisse)", i=True, sz=24, color="5D6D7E"), after=40))
    b.append(para(run("Version V1 du 22 octobre 2026 · rédigée par Claude à partir des lacunes de sources de ses lots (217 à 248) et des audits des LOT 1 à 8", sz=18, color="5D6D7E"), after=200))
    b.append(para(run("1. Consignes pour Gemini", b=True, sz=28, color="1A5276"), style="Titre1"))
    for i, c in enumerate(CONSIGNES, 1):
        b.append(para(run(f"{i}. {c}", sz=19), jc="both", after=60))
    b.append(para(run("2. Mode d'emploi pour Vial", b=True, sz=28, color="1A5276"), style="Titre1"))
    for t in ["Soumets ce document à Gemini et demande-lui de remplir le cadre « Réponse » de chaque question.",
              "Rends-moi le document complété : j'audite chaque réponse (source réelle, version, dose AIPS) avant de corriger les cours.",
              "Quand une réponse est auditée et intégrée au cours, je coche la case de la question : elle devient un ☒ rouge.",
              "L'emplacement de chaque question renvoie au fichier et au point exacts du cours : la correction se fait sans relire le lot."]:
        b.append(para(run("• " + t, sz=19), after=40))
    b.append(para(run("3. Synthèse", b=True, sz=28, color="1A5276"), style="Titre1"))
    rows = [["Groupe", "Périmètre", "Critique", "Haute", "Moyenne", "Total"]]
    tot = [0, 0, 0]
    for g, d in groups:
        c = [sum(q.get("priorite") == p for q in d["questions"]) for p, _, _ in PRIO]
        tot = [x + y for x, y in zip(tot, c)]
        rows.append([g, GROUPES[g]] + [str(x) for x in c] + [str(sum(c))])
    rows.append([("Total", "EAECEE"), ("", "EAECEE")] + [(str(x), "EAECEE") for x in tot] + [(str(sum(tot)), "EAECEE")])
    b.append(table(rows, [1000, 7400, 1500, 1500, 1500, 1500]))
    n = 4
    for g, d in groups:
        b.append(para(run(f"{n}. Groupe {g} — {GROUPES[g]}", b=True, sz=28, color="1A5276"), style="Titre1"))
        h.append(f"<h2>{n}. Groupe {g} — {H.escape(GROUPES[g])}</h2>")
        n += 1
        qs = sorted(d["questions"], key=lambda q: (str(q.get("lot")), {"Critique": 0, "Haute": 1}.get(q.get("priorite"), 2), q["id"]))
        for q in qs:
            b.append(qblock(q))
            h.append(f"<h3>☐ {H.escape(q['id'])} — priorité {H.escape(q.get('priorite',''))} — LOT {H.escape(str(q.get('lot','')))} · SSP {H.escape(str(q.get('ssp','')))}</h3>"
                     f"<p><b>Fichier › emplacement :</b> {H.escape(q.get('fichier',''))} › {H.escape(q.get('emplacement',''))}</p>"
                     f"<p><b>Contexte :</b> {H.escape(q.get('contexte',''))}</p><p><b>Question :</b> {H.escape(q['question'])}</p>"
                     f"<p><i>{H.escape(A_FOURNIR)}</i></p><p><b>Réponse Gemini :</b></p><ul>" +
                     "".join(f"<li>{H.escape(r)} </li>" for r in REPONSE) + "</ul>")
    sect = ('<w:sectPr><w:pgSz w:w="16838" w:h="11906" w:orient="landscape"/>'
            '<w:pgMar w:top="850" w:right="850" w:bottom="850" w:left="850" w:header="400" w:footer="400" w:gutter="0"/></w:sectPr>')
    doc = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document {NS}><w:body>{"".join(b)}{sect}</w:body></w:document>'
    with zipfile.ZipFile(OUT_DOCX, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.writestr("[Content_Types].xml", CT); z.writestr("_rels/.rels", RELS)
        z.writestr("word/_rels/document.xml.rels", DRELS); z.writestr("word/styles.xml", STYLES)
        z.writestr("word/document.xml", doc)
    head = "<h1>HELP_Organi — Questions de recherche pour Google Gemini</h1><h2>1. Consignes pour Gemini</h2><ol>" + "".join(f"<li>{H.escape(c)}</li>" for c in CONSIGNES) + "</ol>"
    open(OUT_HTML, "w", encoding="utf-8").write("<!DOCTYPE html><html lang='fr'><head><meta charset='UTF-8'><title>HELP_Organi</title></head><body>" + head + "".join(h) + "</body></html>\n")
    print(json.dumps({"questions": sum(tot), "par_priorite": tot, "docx": os.path.getsize(OUT_DOCX), "html": os.path.getsize(OUT_HTML)}))


main()
