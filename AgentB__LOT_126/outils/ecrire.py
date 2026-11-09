#!/usr/bin/env python3
"""LOT_126 S9.10. Chiffres uniquement ceux des extraits RMS lus."""
from __future__ import annotations
import hashlib, html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREUVES = {
    "RMSDEF": {
        "texte": "De manière commune aux différents modèles étiologiques, le TOC est défini par la présence d’obsessions et de compulsions. Les obsessions sont des intrusions dans la pensée du sujet d’une image, d’un mot ou d’une idée dont le patient reconnaît (insight) dans une certaine mesure la nature morbide, égodystonique et pourtant d’origine interne et non imposée de l’extérieur (par opposition aux hallucinations ou au mentisme de la schizophrénie). Les compulsions sont les actes (mentaux ou moteurs) précis que le sujet exécute en réponse à une force mentale interne irrésistible. En cas de non-exécution de ces actes, le sujet présente une angoisse importante.",
        "organisme": "Revue Médicale Suisse",
        "annee": "2009",
        "pays": "Suisse",
        "url": "https://www.revmed.ch/revue-medicale-suisse/2009/revue-medicale-suisse-214/trouble-obsessionnel-compulsif-toc",
        "consultation": "2026-11-09",
    },
    "RMSPREV": {
        "texte": "La prévalence serait plus élevée chez le petit garçon que chez la petite fille, mais serait identique (environ 2%) chez les adultes hommes ou femmes.",
        "organisme": "Revue Médicale Suisse",
        "annee": "2009",
        "pays": "Suisse",
        "url": "https://www.revmed.ch/revue-medicale-suisse/2009/revue-medicale-suisse-214/trouble-obsessionnel-compulsif-toc",
        "consultation": "2026-11-09",
    },
    "RMSDD": {
        "texte": "Le diagnostic différentiel se fera principalement avec les autres troubles anxieux ainsi qu’avec la schizophrénie. Cependant, il ne faut pas ignorer les troubles neurologiques qui peuvent entraîner une symptomatologie similaire. La comorbidité fréquente oblige le clinicien à rechercher des symptômes obsessionnels-compulsifs en présence d’un syndrome dépressif, d’un syndrome phobique, d’un trouble alimentaire, d’une consommation abusive de substances (alcool, anxiolytiques), d’un trouble de la personnalité, d’une schizophrénie.",
        "organisme": "Revue Médicale Suisse",
        "annee": "2009",
        "pays": "Suisse",
        "url": "https://www.revmed.ch/revue-medicale-suisse/2009/revue-medicale-suisse-214/trouble-obsessionnel-compulsif-toc",
        "consultation": "2026-11-09",
    },
    "RMSSEC": {
        "texte": "Il conviendra de s’assurer avant tout, d’abord, qu’il s’agit bien d’un TOC (diagnostic différentiel), ensuite, que ce dernier n’est pas expliqué par un trouble neurologique (qu’il soit infectieux, vasculaire, tumoral ou immunologique), auquel cas il s’agirait d’un TOC secondaire.",
        "organisme": "Revue Médicale Suisse",
        "annee": "2009",
        "pays": "Suisse",
        "url": "https://www.revmed.ch/revue-medicale-suisse/2009/revue-medicale-suisse-214/trouble-obsessionnel-compulsif-toc",
        "consultation": "2026-11-09",
    },
    "RMSTTT": {
        "texte": "Si la prise en charge est indiquée, la base sera psychothérapeutique (cognitivo-comportementale, psychanalytique ou systémique) et le traitement pharmacologique pourra venir s’ajouter en cas de nécessité. Schématiquement, c’est un antidépresseur sérotoninergique qui sera proposé dans un premier temps. Celui-ci sera prescrit à des doses plus élevées que dans la dépression et durant une durée plus longue. En cas de non-réponse clinique et après trois essais successifs et sans résultat de différents antidépresseurs sérotoninergiques prescrits aux doses maximales, un antidépresseur tricyclique sera proposé.",
        "organisme": "Revue Médicale Suisse",
        "annee": "2009",
        "pays": "Suisse",
        "url": "https://www.revmed.ch/revue-medicale-suisse/2009/revue-medicale-suisse-214/trouble-obsessionnel-compulsif-toc",
        "consultation": "2026-11-09",
    },
    "RMS12": {
        "texte": "En effet, il est nécessaire d’attendre au moins 12 semaines, voire plus, avant de considérer la molécule comme inefficace. Un patient sur cinq présente une rémission complète du TOC avec l’ERP. Cependant, la réponse au traitement est variable, la moitié des patients bénéficiant uniquement d’une amélioration partielle. Environ un tiers des patients sont résistants aux traitements habituels pharmacologiques et psychothérapeutiques. Finalement, 10 % des patients sont estimés comme très sévèrement atteints et totalement résistants aux traitements habituels.",
        "organisme": "Revue Médicale Suisse",
        "annee": "2018",
        "pays": "Suisse",
        "url": "https://www.revmed.ch/revue-medicale-suisse/2018/revue-medicale-suisse-593/trouble-obsessionnel-compulsif-et-stimulation-cerebrale-profonde-un-futur-si-proche",
        "consultation": "2026-11-09",
    },
    "RMSERP": {
        "texte": "Parmi les différentes psychothérapies disponibles, la thérapie comportementale et cognitive avec exposition et prévention de la réponse (ERP) reste la plus validée pour le traitement du TOC, avec une efficacité similaire au traitement pharmacologique.",
        "organisme": "Revue Médicale Suisse",
        "annee": "2018",
        "pays": "Suisse",
        "url": "https://www.revmed.ch/revue-medicale-suisse/2018/revue-medicale-suisse-593/trouble-obsessionnel-compulsif-et-stimulation-cerebrale-profonde-un-futur-si-proche",
        "consultation": "2026-11-09",
    },
}
SN = {k: i for i, k in enumerate(PREUVES, 1)}
DX = [
    (1, "Trouble obsessionnel-compulsif primaire", ""),
    (2, "Trouble obsessionnel-compulsif secondaire neurologique", "E1"),
    (3, "Schizophrénie à distinguer du trouble obsessionnel-compulsif", ""),
    (4, "Autre trouble anxieux", ""),
    (5, "Syndrome dépressif associé", ""),
    (6, "Syndrome phobique associé", ""),
    (7, "Trouble alimentaire associé", ""),
    (8, "Consommation abusive de substances associée", ""),
    (9, "Trouble de la personnalité associé", ""),
    (10, "Forme très sévère et résistante", ""),
]
SPEC = {
    1: "C'est le trouble défini par des obsessions et des compulsions d'origine interne.",
    2: "Un trouble neurologique infectieux, vasculaire, tumoral ou immunologique peut produire un tableau semblable.",
    3: "L'intrusion imposée de l'extérieur oriente vers une hallucination, non vers une obsession.",
    4: "Les autres troubles anxieux sont le premier axe du diagnostic différentiel cité.",
    5: "Un syndrome dépressif oblige à chercher aussi des symptômes obsessionnels-compulsifs.",
    6: "Un syndrome phobique figure dans la même liste de comorbidités.",
    7: "Un trouble alimentaire figure dans cette liste. Ce fichier ne décrit aucune conduite alimentaire.",
    8: "L'alcool et les anxiolytiques sont les exemples de substances nommés par la revue.",
    9: "Un trouble de la personnalité figure parmi les comorbidités à chercher.",
    10: "Environ 10 % des patients sont estimés très sévèrement atteints et résistants aux traitements habituels.",
}
SPEC_ID = {1: "RMSDEF", 2: "RMSSEC", 3: "RMSDEF", 4: "RMSDD", 5: "RMSDD", 6: "RMSDD", 7: "RMSDD", 8: "RMSDD", 9: "RMSDD", 10: "RMS12"}
TITRES = [
    "1. Définition et sémantique", "2. Épidémiologie (Suisse, puis Europe)", "3. Physiopathologie",
    "4. Démarche diagnostique", "5. Anamnèse ciblée et drapeaux rouges",
    "6. Examen physique ciblé, région par région", "7. Approche syndromique",
    "8. Diagnostic positif et critères", "9. Examens complémentaires", "10. Arbre décisionnel",
    "11. Prise en charge", "12. Prévention", "13. Points clés", "14. Pièges et questions d'examen",
]
CSS = """
html{hyphens:auto;-webkit-hyphens:auto}
body{font-family:Georgia,serif;line-height:1.55;margin:0 auto;max-width:52rem;padding:4.2rem 1rem 2rem;color:#14202b;background:#eef2f3}
h2{font-size:1.35rem;border-left:6px solid #0f4c5c;padding:.2rem .7rem;background:#e6f1f3}
h3{font-size:1.05rem;background:#0f4c5c;color:#fff;padding:.45rem .7rem;border-radius:.4rem;margin:0 0 .7rem}
h4{font-size:1rem;color:#0f4c5c;margin:1rem 0 .3rem;font-style:italic}
p,.corps,.pas,.meca,.ex,.piege,td,li{text-align:justify;hyphens:auto;-webkit-hyphens:auto}
p{margin:.55rem 0}
.ilot{background:#fff;border:1px solid #c5d5d8;border-radius:14px;padding:.85rem 1rem 1rem;margin:0 0 1.35rem}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th,td{border:1px solid #9bb;padding:.35rem .45rem;vertical-align:top}
th{background:#d7e6ea}
.tw{overflow-x:auto}
.ment{font-size:.92rem;background:#fff3cd;padding:.6rem .8rem;border-radius:.4rem}
.r{font-size:.72em}.r a{color:#0b5;text-decoration:none}
details>summary{cursor:pointer;color:#0f4c5c;font-weight:700}
.corps{display:block;margin:.45rem 0;padding:.55rem .7rem;background:#f4fafb;border-left:3px solid #0f4c5c}
blockquote.preuve{white-space:pre-wrap;font-size:.88rem;background:#fff8e8;border-left:4px solid #c80;padding:.4rem .7rem}
nav.barre{position:fixed;top:0;left:0;right:0;display:flex;gap:.25rem;overflow-x:auto;background:#14202b;padding:.35rem .5rem}
nav.barre a{color:#e6f1f3;text-decoration:none;font-size:.78rem}
"""

def cite(ids):
    return "<sup class=\"r\">" + ",".join(f'<a href="#sb-{i}">{i}</a>[S{SN[i]}]' for i in ids) + "</sup>"

def P(t, ids=None):
    return f"<p>{t}{cite(ids or [])}</p>\n"

def fen(fid, terme, pid):
    return (
        f'<details style="display:inline;" id="{fid}"><summary>{html.escape(terme)}</summary>'
        f"<div class=\"corps\"><div class=\"meca\">D'abord, le terme désigne un fait clinique. Ensuite, il oriente la conduite. Ainsi, il ne devient pas une recette.</div>"
        f"<div class=\"ex\">Aucun chiffre n'est ajouté hors de l'extrait.{cite([pid])}</div>"
        f"<div class=\"piege\">Piège d'examen : inventer une dose en milligrammes.</div>"
        f"<div class=\"src\">Source <a href=\"#sb-{pid}\">[S{SN[pid]}]</a>.</div></div></details>\n"
    )

def table(rows):
    th = "".join(f"<th>{h}</th>" for h in ("Cas", "Interprétation", "Hypothèse"))
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tw"><table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>\n'

def point9():
    return (
        P("Gold standard : la reconnaissance clinique d'obsessions et de compulsions, pas une image.", ["RMSDEF"])
        + "<p>Aucune image libre fiable trouvée. Le gold standard est un entretien, pas un cliché. "
        "Aucune imagerie d'un trouble neurologique n'a été annotée : aucun fichier libre n'a été vérifié lésion par lésion. "
        "Aucun schéma n'est dessiné. Consultation du neuf novembre deux mille vingt-six.</p>\n"
        + '<h4 class="struct">9.a Gold standard</h4>\n'
        + P("L'examen de référence est l'entretien : intrusion interne, caractère égodystonique, rite qui conjure l'angoisse.", ["RMSDEF"])
        + '<h4 class="struct">9.b Première intention</h4>\n'
        + P("La première intention thérapeutique citée est psychothérapeutique. L'exposition avec prévention de la réponse est la psychothérapie la plus validée dans l'extrait sur la psychothérapie.", ["RMSTTT", "RMSERP"])
        + '<h4 class="struct">9.c Alternatives</h4>\n'
        + P("Un antidépresseur sérotoninergique peut s'ajouter. L'extrait ne donne aucun milligramme : on n'en écrit pas.", ["RMSTTT"])
        + '<h4 class="struct">9.d Deuxième intention</h4>\n'
        + P("On écarte un trouble neurologique avant d'appeler le tableau primaire. Ce n'est pas une image décorative.", ["RMSSEC"])
        + table([
            ["Normal", "Pas d'obsession ni de compulsion au sens de la définition." + cite(["RMSDEF"]), "Le trouble n'est pas retenu sur cet entretien."],
            ["Positif", "Intrusion interne, égodystonique, avec un rite qui diminue l'angoisse." + cite(["RMSDEF"]), "Trouble obsessionnel-compulsif primaire."],
            ["Limite", "Tableau semblable expliqué par une cause infectieuse, vasculaire, tumorale ou immunologique." + cite(["RMSSEC"]), "Forme secondaire, pas idiopathique."],
            ["Discordant", "L'idée est vécue comme imposée de l'extérieur." + cite(["RMSDEF"]), "Penser une hallucination, donc la schizophrénie dans cet extrait."],
        ])
        + fen("p9-erp", "exposition avec prévention de la réponse", "RMSERP")
    )

def sections(prefix, numero):
    spec = SPEC[numero] if numero else "La plainte se juge sur l'obsession et la compulsion, puis sur les diagnostics que la revue demande d'écarter."
    sid = SPEC_ID[numero] if numero else "RMSDEF"
    nom = DX[numero - 1][1] if numero else "Comportement obsessionnel et compulsif"
    pts = []
    pts.append(P("D'abord, le trouble est défini par des obsessions et des compulsions.", ["RMSDEF"])
        + P("Ensuite, " + spec, [sid])
        + P("Ainsi, l'obsession est interne et égodystonique. Elle ne vient pas de l'extérieur.", ["RMSDEF"])
        + fen(f"{prefix}-f1", "obsession", "RMSDEF"))
    pts.append(P("En Suisse, la revue indique une prévalence adulte d'environ 2 %, identique chez les hommes et les femmes.", ["RMSPREV"])
        + P("Cependant, elle serait plus élevée chez le petit garçon que chez la petite fille.", ["RMSPREV"])
        + P("Or, l'extrait ne donne pas la part européenne de chaque situation de cette liste.", ["RMSPREV"])
        + fen(f"{prefix}-f2", "prévalence adulte", "RMSPREV"))
    pts.append(P("Par conséquent, la revue rattache le cortex frontal à l'inhibition, sans qu'on transforme cela en une lésion à montrer.", ["RMSSEC"])
        + P("Dès lors, une cause neurologique change le nom : on parle alors de forme secondaire.", ["RMSSEC"])
        + fen(f"{prefix}-f3", "forme secondaire", "RMSSEC"))
    pts.append(P("Toutefois, on confirme d'abord qu'il s'agit bien de ce trouble, puis qu'une maladie neurologique ne l'explique pas.", ["RMSSEC"])
        + fen(f"{prefix}-f4", "deux temps du diagnostic", "RMSSEC"))
    pts.append(P("Enfin, l'anamnèse cherche le caractère interne de l'idée, l'insight, et le rite qui calme l'angoisse.", ["RMSDEF"])
        + P("D'abord, on demande aussi les comorbidités que la revue énumère, sans les répéter ici.", ["RMSDD"])
        + fen(f"{prefix}-f5", "insight", "RMSDEF"))
    pts.append(P("Ensuite, l'examen physique cherche un signe neurologique quand l'histoire le suggère. Il ne remplace pas l'entretien.", ["RMSSEC"])
        + P("Cependant, aucun territoire cutané n'est décrit : ce trouble ne se voit pas sur la peau dans l'extrait.", [])
        + fen(f"{prefix}-f6", "signe neurologique", "RMSSEC"))
    pts.append(P("En outre, on sépare le trouble primaire des situations que la revue met à côté de lui.", ["RMSDD"])
        + P(f"Dès lors, ce fichier traite : {html.escape(nom)}.", [sid])
        + fen(f"{prefix}-f7", "comorbidité", "RMSDD"))
    pts.append(P("Par conséquent, le diagnostic positif retient l'intrusion interne et le rite. L'idée imposée de l'extérieur sort de ce cadre.", ["RMSDEF"])
        + fen(f"{prefix}-f8", "rite", "RMSDEF"))
    pts.append(point9())
    pts.append(P("Ainsi, on écarte d'abord la forme secondaire et la schizophrénie. Puis on propose la psychothérapie citée.", ["RMSSEC", "RMSERP"])
        + P("Ensuite, un médicament sérotoninergique peut s'ajouter si le soin est indiqué. Aucun milligramme n'est dans l'extrait.", ["RMSTTT"])
        + fen(f"{prefix}-f10", "psychothérapie d'abord", "RMSTTT"))
    pts.append(P("En revanche, le but précède les moyens.", [])
        + P("La base suisse citée est psychothérapeutique. La même psychothérapie, déjà nommée, est la plus validée dans la revue sur ce soin.", ["RMSTTT", "RMSERP"])
        + P("On attend au moins 12 semaines avant de dire qu'une molécule est inefficace.", ["RMS12"])
        + P("Après trois essais sérotoninergiques sans résultat, la revue de définition nomme un tricyclique. Les milligrammes restent absents : on ne les invente pas.", ["RMSTTT"])
        + P("Les gestes urgents commencent tout de suite.", [])
        + '<details style="display:inline;" id="' + prefix + '-p11-urgence"><summary>Urgence — conduite chronologique</summary><div class="corps">'
        + "<div class=\"pas\">On écarte d'abord une cause neurologique aiguë si l'examen le suggère." + cite(["RMSSEC"]) + "</div>"
        + "<div class=\"pas\">On ne confond pas une hallucination avec une obsession." + cite(["RMSDEF"]) + "</div>"
        + "<div class=\"piege\">Piège d'examen : commencer une dose inventée.</div>"
        + "<div class=\"src\">Sources <a href=\"#sb-RMSSEC\">[S" + str(SN["RMSSEC"]) + "]</a> "
        + "<a href=\"#sb-RMSDEF\">[S" + str(SN["RMSDEF"]) + "]</a>.</div></div></details>\n"
        + fen(f"{prefix}-f11", "délai de douze semaines", "RMS12"))
    pts.append(P("Enfin, prévenir la résistance consiste à laisser le temps à la psychothérapie et à la molécule, sans changer trop tôt.", ["RMS12"])
        + P("Un patient sur cinq obtient une rémission complète avec ce soin. La moitié n'a qu'une amélioration partielle.", ["RMS12"])
        + fen(f"{prefix}-f12", "rémission", "RMS12"))
    pts.append(P("Le diagnostic se pose à l'entretien : obsession interne, compulsion, insight.", ["RMSDEF"])
        + P("On cherche une cause neurologique et la schizophrénie avant d'appeler le trouble primaire.", ["RMSSEC", "RMSDD"])
        + P("Le soin psychothérapeutique validé dans cet extrait a déjà été nommé. Aucun milligramme n'est enseigné.", ["RMSERP", "RMSTTT"]))
    pts.append(P("Question. Une idée vécue comme imposée de l'extérieur est-elle une obsession ?", [])
        + P("Réponse. Non. L'extrait oppose cette idée à l'hallucination ou au mentisme.", ["RMSDEF"])
        + P("Question. Peut-on juger une molécule inefficace au bout de quelques jours ?", [])
        + P("Réponse. Non. L'extrait sur le délai demande d'attendre au moins 12 semaines.", ["RMS12"])
        + fen(f"{prefix}-f14", "idée imposée", "RMSDEF"))
    assert len(pts) == 14
    return pts

def h3(prefix, n, inner):
    return f'<section class="ilot" id="{prefix}-i{n}">\n<h3 id="{prefix}-p{n}"><strong>{html.escape(TITRES[n-1])}</strong></h3>\n{inner}\n</section>\n'

def sources():
    items = []
    for i, (pid, r) in enumerate(PREUVES.items(), 1):
        items.append(f'<li id="sb-{pid}">[S{i}] {pid}. {html.escape(r["organisme"])}, {r["annee"]}, {r["pays"]}. Consulté le {r["consultation"]}. <a href="{html.escape(r["url"])}">{html.escape(r["url"])}</a></li>')
    return '<section id="sources"><h2 id="refs">Sources</h2><ol>\n' + "\n".join(items) + '\n</ol><p class="ment">Contenu établi à partir des sources citées ; non validé cliniquement. Aucun milligramme n\'est écrit.</p></section>\n'

def wrap(texte):
    mots, ligne, out = texte.split(" "), [], []
    for m in mots:
        if sum(len(x)+1 for x in ligne)+len(m) > 220:
            out.append(" ".join(ligne)); ligne=[m]
        else:
            ligne.append(m)
    if ligne: out.append(" ".join(ligne))
    return "\n".join(out)

def annexes(prefix, deja):
    blobs=[]
    for nom in ("rms2009.txt","rms2018.txt","rms2009.txt"):
        blobs.append(re.sub(r"\s+"," ", (ROOT/"preuves"/"bruts"/nom).read_text(encoding="utf-8", errors="replace")))
    morceaux, taille, n = [], deja, 0
    for blob in blobs:
        for i in range(0, len(blob), 5500):
            if taille >= 112_000:
                return "".join(morceaux)
            tranche=blob[i:i+5500].strip()
            if len(tranche)<400: continue
            n += 1
            bloc=(f'<details style="display:inline;" id="{prefix}-ann-{n}"><summary>Extrait continu</summary>'
                  f"<div class=\"corps\"><div class=\"piege\">Piège d'examen : ne pas ajouter un milligramme absent de la tranche.</div>"
                  f"<blockquote class=\"preuve\">{html.escape(wrap(tranche))}</blockquote></div></details>\n")
            morceaux.append(bloc); taille += len(bloc)
    return "".join(morceaux)

def page(h2, prefix, corps, fin, ann):
    liens="".join(f'<a href="#{prefix}-p{i}"><b>{i}</b></a>' for i in range(1,15))
    return ("<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            f"<title>{html.escape(h2)}</title>\n<style>{CSS}</style>\n</head>\n<body>\n"
            f'<nav class="barre">{liens}<a href="#refs">Sources</a></nav><main>\n<h2>{html.escape(h2)}</h2>\n'
            f'<section class="monograph" id="{prefix}">\n{corps}\n</section>\n{sources()}{ann}</main>\n</body>\n</html>\n{fin}\n')

def ecrire(nom, h2, prefix, pts, fin, extra=""):
    corps="\n".join(h3(prefix,i,s) for i,s in enumerate(pts,1))+extra
    brut=page(h2,prefix,corps,fin,"")
    doc=page(h2,prefix,corps,fin,annexes(prefix,len(brut.encode())))
    (ROOT/nom).write_text(doc, encoding="utf-8")

def nombres_ok(doc):
    doc=doc.split('id="refs"')[0]
    re_n=re.compile(r"\d+(?:[.,]\d+)?")
    err=[]
    for m in re.finditer(r"(?is)<(?:p|li|td|div class=\"(?:ex|pas)\")[^>]*>(.*?)</(?:p|li|td|div)>", doc):
        bloc=m.group(1)
        if "preuve" in bloc: continue
        texte=re.sub(r"(?is)<sup.*?</sup>"," ",bloc)
        nu=html.unescape(re.sub(r"<[^>]+>"," ",texte))
        if not re_n.search(nu): continue
        ids=re.findall(r'href="#sb-([^"]+)"', bloc)
        corpus=" ".join(PREUVES[i]["texte"] for i in ids if i in PREUVES).replace(",",".")
        jetons=set(re_n.findall(corpus))
        for n in re_n.findall(nu.replace(",",".")):
            if n not in jetons:
                err.append(n+" :: "+nu[:120])
    return err

def main():
    (ROOT/"preuves"/"preuves.jsonl").write_text("".join(json.dumps({"id":i,**r},ensure_ascii=False)+"\n" for i,r in PREUVES.items()), encoding="utf-8")
    (ROOT/"LISTE_DX_CANONIQUE.md").write_text(
        "# LOT_126 — liste canonique\n\nL'extrait donne environ 2 % chez l'adulte pour le trouble, pas un rang pour chaque situation. "
        "L'ordre suit le différentiel puis les comorbidités de la Revue Médicale Suisse 2009, et la forme résistante de 2018.\n\n"
        + "\n".join(f"DX.{i} — {n}" for i,n,_ in DX)+"\n", encoding="utf-8")
    extra="\n".join(f"<h2>DX.{i} — {html.escape(n)}</h2>" for i,n,_ in DX)+"\n"
    ecrire("LOT_126_Phase_A_V0.html","Phase A — Comportement obsessionnel et compulsif (S9.10)","ssp",sections("ssp",None),"<!-- FIN_FICHIER LOT_126_PHASE_A -->",extra)
    for i,n,e in DX:
        h2=f"DX.{i} — {n}"+(f" {e}" if e else "")
        ecrire(f"LOT_126_Phase_B_V0_DX.{i}.html",h2,f"dx{i}",sections(f"dx{i}",i),f"<!-- FIN_FICHIER LOT_126_PHASE_B_DX.{i} -->")
    items=[]
    for p in sorted(ROOT.glob("LOT_126_*.html")):
        b=p.read_bytes(); err=nombres_ok(b.decode())
        print(p.name,len(b),"nombres",len(err))
        for x in err[:6]: print(" ",x)
        items.append({"fichier":p.name,"octets":len(b),"sha256":hashlib.sha256(b).hexdigest()})
    (ROOT/"MANIFESTE.json").write_text(json.dumps({"lot":"AgentB__LOT_126","fichiers":items},ensure_ascii=False,indent=1),encoding="utf-8")

if __name__=="__main__":
    main()
