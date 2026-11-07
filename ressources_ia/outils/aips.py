#!/usr/bin/env python3
"""AIPS suisse hors ligne (zéro jeton). Corpus : ressources_ia/aips/.

  python3 ressources_ia/outils/aips.py chercher <texte>        spécialités (FI = SmPC) dont le nom ou le numéro contient <texte>
  python3 ressources_ia/outils/aips.py lire <numéro> [motif]   texte français de l'information professionnelle ; avec motif : lignes contenant le motif
  python3 ressources_ia/outils/aips.py telecharger-tout [-j 16]   (re)construit ressources_ia/aips/fi_fr/<numéro>.txt.gz depuis refdata
Le texte vient des documents officiels Swissmedic/refdata (files.refdata.ch) listés dans AipsDownload_*.xml.
"""
import concurrent.futures as cf, gzip, html, re, sys, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path

D = Path(__file__).resolve().parent.parent / "aips"
NS = {"m": "https://simisinfo.refdata.ch/MedicinalDocuments/1.0/"}


def index():
    xmlf = sorted(D.glob("AipsDownload_*.xml"))[-1]
    out = []
    for b in ET.parse(xmlf).getroot().findall("m:MedicinalDocumentsBundle", NS):
        if b.findtext("m:Type", "", NS) != "SmPC" or b.findtext("m:Domain", "", NS) != "Human":
            continue
        num = b.findtext("m:RegulatedAuthorization/m:Identifier", "", NS)
        titulaire = b.findtext("m:Holder/m:Name", "", NS)
        for a in b.findall("m:AttachedDocument", NS):
            if a.findtext("m:Language", "", NS) != "fr":
                continue
            nom = a.findtext("m:Description", "", NS)
            url = next((r.findtext("m:Url", "", NS) for r in a.findall("m:DocumentReference", NS)
                        if r.findtext("m:ContentType", "", NS) == "text/html"), "")
            out.append((num, nom, titulaire, url))
    return out


def texte(h):
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>|</(p|div|h\d|li|tr)>", "\n", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h)
    return "\n".join(re.sub(r"[ \t ]+", " ", l).strip() for l in h.splitlines() if l.strip())


def telecharger(item):
    num, nom, tit, url = item
    f = D / "fi_fr" / f"{num}.txt.gz"
    if f.exists() or not url:
        return 0
    try:
        h = urllib.request.urlopen(url, timeout=60).read().decode("utf-8", "replace")
    except Exception as e:
        return f"{num} : {e}"
    with gzip.open(f, "wt", encoding="utf-8") as g:
        g.write(f"# {nom} — n° Swissmedic {num} — {tit}\n# Source : {url}\n\n{texte(h)}\n")
    return 1


def main(a):
    if not a:
        print(__doc__); return 2
    if a[0] == "chercher" and len(a) > 1:
        q = " ".join(a[1:]).lower()
        for num, nom, tit, url in index():
            if q in nom.lower() or q == num:
                print(f"{num}\t{nom}\t{tit}\t{'hors ligne' if (D/'fi_fr'/f'{num}.txt.gz').exists() else url}")
    elif a[0] == "lire" and len(a) > 1:
        f = D / "fi_fr" / f"{a[1]}.txt.gz"
        if not f.exists():
            print("Absent hors ligne : lancer telecharger-tout ou lire l'URL donnée par `chercher`."); return 1
        t = gzip.open(f, "rt", encoding="utf-8").read()
        if len(a) > 2:
            m = " ".join(a[2:]).lower()
            print("\n".join(l for l in t.splitlines() if m in l.lower()))
        else:
            print(t)
    elif a[0] == "telecharger-tout":
        j = int(a[a.index("-j") + 1]) if "-j" in a else 16
        (D / "fi_fr").mkdir(exist_ok=True)
        items = index(); ok = err = 0
        with cf.ThreadPoolExecutor(j) as ex:
            for r in ex.map(telecharger, items):
                if r == 1: ok += 1
                elif r: err += 1; print(r, file=sys.stderr)
        print(f"{len(items)} FI françaises ; {ok} téléchargées ; {err} erreurs ; dossier {D/'fi_fr'}")
    else:
        print(__doc__); return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
