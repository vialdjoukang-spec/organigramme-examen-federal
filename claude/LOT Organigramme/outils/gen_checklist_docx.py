#!/usr/bin/env python3
"""Génère la liste de corrections d'un lot PROFILES au format Word (.docx minimal).

Usage : gen_checklist_docx.py audit.json sortie.docx

audit.json :
{
  "lot": 8, "titre": "Hypothermie", "ssp": "G8", "date": "2026-10-22",
  "auditeur": "Claude (audit médical et linguistique)",
  "fichiers": [{"nom": "...", "drive_id": "...", "taille": 16199, "statut": "actif|doublon|vide|obsolète"}],
  "synthese": ["phrase", ...],
  "constats": [{
     "id": "L8-C01", "gravite": "Critique|Grave|Moyen|Léger",
     "domaine": "Médical|Linguistique|Prompt de base|Structure",
     "fichier": "nom exact", "emplacement": "Bloc 1 › point 11 › fenêtre « Médicaments de réanimation »",
     "extrait": "citation exacte, 25 mots au plus",
     "probleme": "phrase verbale", "correction": "texte de remplacement ou action précise",
     "source": "référence vérifiable ou « donnée non trouvée dans les sources consultées »"}],
  "rapport_medical": ["paragraphe", ...],
  "rapport_linguistique": ["paragraphe", ...]
}
Les cases à cocher sont des contrôles de contenu Word : cliquer dessus les coche.
Une case cochée affiche un ☒ rouge.
"""
import json, sys, zipfile
from xml.sax.saxutils import escape

GRAV = [("Critique", "8B0000", "FADBD8"), ("Grave", "C0392B", "FDEBD0"),
        ("Moyen", "B9770E", "FEF9E7"), ("Léger", "1F618D", "EBF5FB")]
NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
      'xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" '
      'xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="w14"')


def run(t, b=False, i=False, color=None, sz=None, font=None):
    rp = ""
    if font: rp += f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:eastAsia="{font}"/>'
    if b: rp += "<w:b/>"
    if i: rp += "<w:i/>"
    if color: rp += f'<w:color w:val="{color}"/>'
    if sz: rp += f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
    return f'<w:r><w:rPr>{rp}</w:rPr><w:t xml:space="preserve">{escape(str(t))}</w:t></w:r>'


def para(content, style=None, jc=None, after=None, keep=False):
    pp = ""
    if style: pp += f'<w:pStyle w:val="{style}"/>'
    if keep: pp += "<w:keepNext/>"
    if after is not None: pp += f'<w:spacing w:after="{after}"/>'
    if jc: pp += f'<w:jc w:val="{jc}"/>'
    return f"<w:p><w:pPr>{pp}</w:pPr>{content}</w:p>"


def checkbox():
    # Contrôle de contenu case à cocher (Word 2010+) ; le glyphe est rouge.
    return ('<w:sdt><w:sdtPr><w:rPr><w:rFonts w:ascii="MS Gothic" w:hAnsi="MS Gothic" w:eastAsia="MS Gothic"/>'
            '<w:color w:val="FF0000"/><w:sz w:val="32"/></w:rPr><w:alias w:val="Corrigé"/>'
            '<w14:checkbox><w14:checked w14:val="0"/>'
            '<w14:checkedState w14:val="2612" w14:font="MS Gothic"/>'
            '<w14:uncheckedState w14:val="2610" w14:font="MS Gothic"/></w14:checkbox></w:sdtPr>'
            '<w:sdtContent><w:r><w:rPr><w:rFonts w:ascii="MS Gothic" w:hAnsi="MS Gothic" w:eastAsia="MS Gothic"/>'
            '<w:color w:val="FF0000"/><w:sz w:val="32"/></w:rPr><w:t>☐</w:t></w:r></w:sdtContent></w:sdt>')


def cell(content, w, fill=None, header=False):
    tc = f'<w:tcW w:w="{w}" w:type="dxa"/>'
    if fill: tc += f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>'
    tc += '<w:vAlign w:val="top"/>'
    if not content.startswith("<w:"):
        content = para(run(content, b=header, sz=17 if not header else 17,
                           color="FFFFFF" if header else None), after=0)
    return f"<w:tc><w:tcPr>{tc}</w:tcPr>{content}</w:tc>"


def table(rows, widths, header_fill="1A5276"):
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    out = (f'<w:tbl><w:tblPr><w:tblW w:w="{sum(widths)}" w:type="dxa"/><w:tblLayout w:type="fixed"/>'
           '<w:tblBorders>' + "".join(f'<w:{s} w:val="single" w:sz="4" w:color="AEB6BF"/>'
                                      for s in ("top", "left", "bottom", "right", "insideH", "insideV")) +
           '</w:tblBorders><w:tblCellMar><w:top w:w="40" w:type="dxa"/><w:left w:w="70" w:type="dxa"/>'
           '<w:bottom w:w="40" w:type="dxa"/><w:right w:w="70" w:type="dxa"/></w:tblCellMar></w:tblPr>'
           f'<w:tblGrid>{grid}</w:tblGrid>')
    for k, r in enumerate(rows):
        hdr = k == 0
        trpr = '<w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>' if hdr else '<w:trPr><w:cantSplit/></w:trPr>'
        cells = "".join(cell(c if not isinstance(c, tuple) else c[0], widths[j],
                             fill=header_fill if hdr else (c[1] if isinstance(c, tuple) else None), header=hdr)
                        for j, c in enumerate(r))
        out += f"<w:tr>{trpr}{cells}</w:tr>"
    return out + "</w:tbl>" + para("", after=120)


def multi(lines):
    return "".join(para(run(l, sz=17), after=40) for l in lines)


def build(a):
    b = []
    b.append(para(run(f"LOT {a['lot']} — {a['titre']} (SSP {a['ssp']})", b=True, sz=40, color="1A5276"), after=60))
    b.append(para(run("Liste des problèmes à corriger — audit médical, linguistique et conformité au prompt de base",
                      i=True, sz=24, color="5D6D7E"), after=60))
    b.append(para(run(f"Audit du {a['date']} · {a['auditeur']}", sz=18, color="5D6D7E"), after=200))

    b.append(para(run("Mode d'emploi", b=True, sz=26, color="1A5276"), style="Titre1", keep=True))
    for t in ["Chaque ligne décrit un problème et son emplacement exact. Le correcteur n'a pas besoin de relire le lot entier.",
              "L'emplacement suit le chemin Fichier › Bloc › point › fenêtre. L'extrait cite le texte fautif mot pour mot : une recherche Ctrl+F le retrouve.",
              "Le correcteur applique la correction, puis il clique sur la case : elle se coche en rouge (☒).",
              "L'auditeur suivant contrôle chaque case cochée avant de valider le lot."]:
        b.append(para(run("• " + t, sz=19), after=40))

    b.append(para(run("Synthèse", b=True, sz=26, color="1A5276"), style="Titre1", keep=True))
    counts = {g: sum(1 for c in a["constats"] if c["gravite"] == g) for g, _, _ in GRAV}
    rows = [["Gravité", "Nombre", "Définition"]]
    defs = {"Critique": "L'erreur peut nuire à un patient (dose, contre-indication, conduite dangereuse). Correction immédiate.",
            "Grave": "Le contenu est faux, non sourcé ou viole une règle absolue du prompt de base.",
            "Moyen": "Le contenu est incomplet, imprécis ou mal structuré ; la pédagogie en souffre.",
            "Léger": "Faute de langue, de typographie ou de mise en forme sans conséquence sur le fond."}
    for g, col, fill in GRAV:
        rows.append([(g, fill), (str(counts[g]), fill), (defs[g], fill)])
    rows.append([("Total", "EAECEE"), (str(len(a["constats"])), "EAECEE"), ("", "EAECEE")])
    b.append(table(rows, [1800, 1100, 11500]))
    b.append(multi(a.get("synthese", [])))

    b.append(para(run("Fichiers audités", b=True, sz=26, color="1A5276"), style="Titre1", keep=True))
    rows = [["Fichier", "Identifiant Drive", "Taille (octets)", "Statut"]]
    for f in a["fichiers"]:
        rows.append([f["nom"], f.get("drive_id", ""), str(f.get("taille", "")), f.get("statut", "")])
    b.append(table(rows, [6400, 4600, 1500, 1900]))

    widths = [600, 900, 1250, 1900, 2350, 2600, 3000, 1800]
    for g, col, fill in GRAV:
        items = [c for c in a["constats"] if c["gravite"] == g]
        b.append(para(run(f"{g} — {len(items)} problème(s)", b=True, sz=26, color=col), style="Titre1", keep=True))
        if not items:
            b.append(para(run("Aucun problème de ce niveau.", i=True, sz=18), after=120))
            continue
        rows = [["Fait", "N°", "Domaine", "Fichier", "Emplacement", "Extrait exact", "Problème → correction", "Source"]]
        for c in items:
            fix = para(run(c["probleme"], sz=17), after=40) + para(run("→ " + c["correction"], b=True, sz=17, color="145A32"), after=0)
            rows.append([para(checkbox(), jc="center", after=0), (c["id"], fill), c["domaine"], c["fichier"],
                         c["emplacement"], para(run("« " + c["extrait"] + " »", i=True, sz=17), after=0), fix, c["source"]])
        b.append(table(rows, widths, header_fill=col))

    for key, title in (("rapport_medical", "Rapport d'audit médical"), ("rapport_linguistique", "Rapport d'audit linguistique")):
        b.append(para(run(title, b=True, sz=26, color="1A5276"), style="Titre1", keep=True))
        for p in a.get(key, []):
            b.append(para(run(p, sz=19), jc="both", after=100))
    b.append(para(run("Audit produit par IA à partir des sources citées ; il ne remplace pas une validation clinique par un médecin.",
                      i=True, sz=16, color="5D6D7E")))
    sect = ('<w:sectPr><w:pgSz w:w="16838" w:h="11906" w:orient="landscape"/>'
            '<w:pgMar w:top="850" w:right="850" w:bottom="850" w:left="850" w:header="400" w:footer="400" w:gutter="0"/></w:sectPr>')
    return f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document {NS}><w:body>{"".join(b)}{sect}</w:body></w:document>'


STYLES = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
          '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Calibri" w:cs="Calibri"/>'
          '<w:sz w:val="20"/><w:lang w:val="fr-CH"/></w:rPr></w:rPrDefault>'
          '<w:pPrDefault><w:pPr><w:spacing w:after="80" w:line="264" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>'
          '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>'
          '<w:style w:type="paragraph" w:styleId="Titre1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/>'
          '<w:pPr><w:keepNext/><w:spacing w:before="240" w:after="100"/><w:pBdr><w:bottom w:val="single" w:sz="8" w:space="2" w:color="2980B9"/></w:pBdr>'
          '<w:outlineLvl w:val="0"/></w:pPr></w:style></w:styles>')
CT = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
      '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
      '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
      '<Default Extension="xml" ContentType="application/xml"/>'
      '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
      '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>')
RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>')
DRELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
         '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
         '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>')

if __name__ == "__main__":
    a = json.load(open(sys.argv[1], encoding="utf-8"))
    with zipfile.ZipFile(sys.argv[2], "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.writestr("[Content_Types].xml", CT)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/_rels/document.xml.rels", DRELS)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/document.xml", build(a))
    print(sys.argv[2])
