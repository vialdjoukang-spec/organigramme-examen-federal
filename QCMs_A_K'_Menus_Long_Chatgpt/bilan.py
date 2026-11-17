"""Bilan à 08 h 30 Europe/Zurich, établi sur l'historique Git de main.
Depuis un clone actualisé : python bilan.py 2026-11-17 rapport.pdf --ref origin/main
Dépendance : reportlab. Les heures antérieures à l'échéance sont refusées.
"""
import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from datetime import date, datetime, time, timedelta
from pathlib import Path
from xml.sax.saxutils import escape
from zoneinfo import ZoneInfo

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

HERE = Path(__file__).resolve().parent
TZ = ZoneInfo("Europe/Zurich")
INK = "#18334A"
TEAL = "#096763"
SLATE = "#486277"
BASE = "https://github.com/vialdjoukang-spec/organigramme-examen-federal/commit/"
def git(*args):
    return subprocess.check_output(["git", "-C", str(HERE), *args])

def snapshot(ref, cutoff):
    relative = git("rev-parse", "--show-prefix").decode().strip() + "index.html"
    sha = git("rev-list", "-1", "--first-parent", "--before=" + cutoff.isoformat(), ref).decode().strip()
    if not sha:
        return None
    name = sha + ":" + relative
    if subprocess.run(["git", "-C", str(HERE), "cat-file", "-e", name], stderr=subprocess.DEVNULL).returncode:
        return None
    raw = git("show", name)
    blob = git("rev-parse", name).decode().strip()
    if hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest() != blob:
        raise ValueError("Empreinte du fichier HTML discordante")
    data = json.loads(re.search(rb'<script[^>]+id="donnees"[^>]*>(.*?)</script>', raw, re.S)[1])
    return sha, blob, data

def make_report(path, cutoff, current, prior, hour_prior=None):
    sha, blob, bank = current
    catalogue = bank["catalogue"]
    items = bank["items"]
    seen = {q["id"] for q in items}
    codes = [code for code, _ in catalogue]
    count = Counter(q["code"] for q in items)
    if len(seen) != len(items) or set(count) - set(codes) or len(set(codes)) != len(catalogue):
        raise ValueError("Identifiants en double ou code inconnu")
    status = bank["production"]["statuts"]
    target = bank["production"]["minimumParSSP"]
    def closed(code):
        s = status.get(code, {})
        return bool(s.get("clos") and s.get("auditComplet") and s.get("couvertureComplete") and count[code] >= target)
    for code, state in status.items():
        if state.get("integrees", count[code]) != count[code] or bool(state.get("clos")) != closed(code):
            raise ValueError("État publié discordant pour " + code)
    audits = bank["audits"]
    audited = sum(a["items"] for a in audits)
    deficit = lambda c: max(0, target - count[c])
    def fmt(n):
        return f"{n:,}".replace(",", " ")
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=20*mm, bottomMargin=20*mm)
    story = []
    def p(s, size=10, color=INK, bold=False):
        style = ParagraphStyle("ligne", fontName="Helvetica-Bold" if bold else "Helvetica", fontSize=size, leading=size*1.32, textColor=colors.HexColor(color), spaceAfter=4)
        return Paragraph(s, style)
    def table(rows, widths, last_bold=False):
        t = Table(rows, colWidths=[n*mm for n in widths], repeatRows=1, hAlign="LEFT")
        rules = [("BACKGROUND",(0,0),(-1,0),colors.HexColor(TEAL)),("TEXTCOLOR",(0,0),(-1,0),colors.white),("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,colors.HexColor("#EFF5F5")]),("FONTSIZE",(0,0),(-1,-1),9),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)]
        if last_bold:
            rules.append(("FONTNAME",(0,-1),(-1,-1),"Helvetica-Bold"))
        t.setStyle(TableStyle(rules))
        return t
    story.extend([p("EXAMEN FÉDÉRAL DE MÉDECINE HUMAINE",9,TEAL,True),p("Banque suisse de QCM",23,INK,True),p("État publié au " + cutoff.strftime("%d.%m.%Y à %H h %M") + " (Europe/Zurich)",13,SLATE),Spacer(1,3*mm)])
    rows=[["Branche","SSP clos","Intégrées","Seuil cumulé","Manquantes"]]
    for branch in "GSFO":
        group=[c for c in codes if c.startswith(branch)]
        rows.append([branch,f"{sum(closed(c) for c in group)} / {len(group)}",fmt(sum(count[c] for c in group)),fmt(len(group)*target),fmt(sum(deficit(c) for c in group))])
    rows.append(["Ensemble",f"{sum(map(closed,codes))} / {len(codes)}",fmt(len(items)),fmt(target*len(codes)),fmt(sum(map(deficit,codes)))])
    story.extend([table(rows,[30,28,35,36,45],True),Spacer(1,4*mm)])
    complete = all(closed(c) for c in codes)
    verdict = "atteint" if complete else "non atteint"
    story.append(p("Objectif global " + verdict, 15, TEAL if complete else "#8F412F", True))
    story.append(p(f"{fmt(audited)} questions consignées dans {len(audits)} lots d’audit. Chaque SSP requiert au moins {target} questions. Le déficit additionne les écarts locaux. Les questions excédentaires d’un SSP ne couvrent pas un autre SSP."))
    if hour_prior:
        delta = len(items) - len(hour_prior[2]["items"])
        story.append(p(f"Débit net observé entre {(cutoff-timedelta(hours=1)):%H h %M} et {cutoff:%H h %M} : {delta:+d} questions intégrées en une heure."))
    if prior:
        delta=len(items)-len(prior[2]["items"])
        story.append(p(f"Depuis la veille à 08 h 30 : {delta:+d} questions intégrées."))
    else:
        story.append(p("Évolution sur 24 heures indisponible : aucune banque comparable trouvée la veille à 08 h 30."))
    first=next((c for c in codes if not closed(c)),None)
    if first:
        title=dict(catalogue)[first]
        last=max((int(q["id"].rsplit("-",1)[1]) for q in items if q["code"]==first),default=0)
        story.append(p(f"File ouverte : {escape(first)} · {escape(title)}. Examiner les réservations à partir de Q{last+1:03d} et la couverture clinique avant clôture."))
    story.append(p("Contrôle documentaire par agents indépendants. La validation par un médecin suisse n’est pas attestée par les compteurs. Les manuscrits en cours sont exclus des totaux."))
    story.extend([p(f'<link href="{BASE}{sha}" color="{TEAL}">Version de main : {sha}</link>',9),p("Empreinte du HTML : "+blob,9),Spacer(1,4*mm),p("Formats et reprise par branche",15,INK,True)])
    rows = [["Branche", "Type A", "K-prime", "Menu long", "Premier SSP ouvert"]]
    for branch in "GSFO":
        formats = Counter(q["type"] for q in items if q["code"].startswith(branch))
        active = next((c for c in codes if c.startswith(branch) and not closed(c)), None)
        following = f"{active} · Q{count[active]+1:03d}" if active else "Branche close"
        rows.append([branch, formats["A"], formats["K"], formats["M"], following])
    story.append(table(rows, [27, 26, 26, 35, 60]))
    story.append(p("Le premier SSP ouvert de la branche G, puis S, F et O détermine la priorité de rédaction.",9))
    story.extend([PageBreak(),p("Couverture pédagogique",17,INK,True)])
    threshold = [c for c in codes if count[c] >= target]
    story.append(p("SSP ayant atteint le seuil individuel : " + (", ".join(threshold) if threshold else "aucun") + "."))
    classified = [q for q in items if q.get("objectifFacultaire") in bank["production"].get("objectifsFacultaires", {})]
    direct = sum(q.get("rattachement") == "directe" for q in classified)
    inferred = sum(any(mot in q.get("rattachement", "").lower() for mot in ("déduite", "inférée")) for q in classified)
    story.append(p(f"{fmt(len(items))} décisions cliniques portent un objectif explicite dans la banque. {fmt(len(classified))} renvoient au registre facultaire embarqué, dont {fmt(direct)} correspondances directes et {fmt(inferred)} déduites. Le rattachement documentaire détaillé reste à intégrer pour {fmt(len(items)-len(classified))} questions."))
    themes = sum(len(bank.get("agenda", {}).get(c, [])) for c in codes if not closed(c))
    story.append(p(f"Le catalogue recense {fmt(themes)} thèmes de départ dans les SSP encore ouverts. Un thème peut déjà avoir donné lieu à plusieurs questions. Les décisions restant à spécifier et la couverture au-delà de {target} sont examinées dans la matrice clinique de chaque SSP."))
    story.extend([Spacer(1,4*mm),p("Derniers lots consignés",15,INK,True)])
    rows = [["Lot","Date","Questions","Première question","Dernière question"]]
    index = 0
    for audit in audits:
        batch = items[index:index + audit["items"]]
        index += audit["items"]
        if batch:
            rows.append([f'{audit["lot"]:03d}',audit["date"],len(batch),batch[0]["id"],batch[-1]["id"]])
    story.append(table([rows[0], *rows[-min(len(rows)-1,5):]] if len(rows)>1 else rows, [22,32,28,46,46]))
    if hour_prior:
        story.append(p(f'<link href="{BASE}{hour_prior[0]}" color="{TEAL}">Révision de référence pour le débit horaire : {hour_prior[0]}</link>',9))
    story.extend([Spacer(1,4*mm),p("Progression par SSP",15,INK,True)])
    rows=[["Code","Titre du catalogue","Intégrées","Déficit","État"]]
    for code,title in catalogue:
        rows.append([code,p(escape(title),9),count[code],deficit(code),"Clos" if closed(code) else ("Ouvert" if count[code] else "À traiter")])
    story.append(table(rows,[17,95,20,17,25]))
    def frame(canvas,doc):
        w,h=A4
        canvas.setFillColor(colors.HexColor(TEAL))
        canvas.rect(0,h-3*mm,w,3*mm,stroke=0,fill=1)
        canvas.setFont("Helvetica",8)
        canvas.drawString(18*mm,10*mm,"Suivi de production  /  "+cutoff.strftime("%d.%m.%Y"))
        canvas.drawRightString(w-18*mm,10*mm,f"Page {doc.page}")
    doc.build(story,onFirstPage=frame,onLaterPages=frame)

def main():
    arg=argparse.ArgumentParser(description=__doc__)
    arg.add_argument("jour",type=date.fromisoformat)
    arg.add_argument("sortie",type=Path)
    arg.add_argument("--ref",default="origin/main")
    args=arg.parse_args()
    cutoff=datetime.combine(args.jour,time(8,30),tzinfo=TZ)
    if datetime.now(TZ) < cutoff:
        arg.error("Le relevé de cette échéance sera disponible à 08 h 30.")
    current=snapshot(args.ref,cutoff)
    if current is None:
        arg.error("Aucune banque sur la référence à cette échéance.")
    make_report(args.sortie,cutoff,current,snapshot(args.ref,cutoff-timedelta(days=1)),
                snapshot(args.ref,cutoff-timedelta(hours=1)))

if __name__ == "__main__":
    main()
