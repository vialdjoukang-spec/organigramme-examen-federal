#!/usr/bin/env python3
"""Texte AIPS (information professionnelle SmPC) par n° Swissmedic ou nom — cache .cache/aips/.

  python3 harnais/aips_texte.py 69243            # texte FR complet (cache)
  python3 harnais/aips_texte.py 69243 --section grossesse
  python3 harnais/aips_texte.py --nom Axhidrox   # cherche dans l'index (descriptions)
Le XML local ne contient que l'index (n°, titulaire, URL) ; le texte vient de files.refdata.ch.
"""
import argparse, re, sys, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from aips_verbatim import decode  # police Symbol : µ, ≥
RAC = Path(__file__).resolve().parent.parent / ".cache" / "aips"
XML = RAC / "AipsDownload_20261008.xml"
B = re.compile(r"<MedicinalDocumentsBundle>.*?</MedicinalDocumentsBundle>", re.S)

def bundles():
    t = XML.read_text(encoding="utf-8-sig")
    for m in B.finditer(t):
        b = m.group(0)
        yield b

def trouve(num=None, nom=None):
    for b in bundles():
        if "<Type>SmPC</Type>" not in b: continue
        ids = re.findall(r"<Identifier>(\d+)</Identifier>", b.split("<Holder>")[0])
        if not ids: continue
        n = num if num in ids else ids[0]
        if num and num not in ids: continue
        if nom and not re.search(nom, b, re.I): continue
        yield n, b

def url_html(b, lang="fr"):
    for d in re.finditer(r"<AttachedDocument>.*?</AttachedDocument>", b, re.S):
        if f"<Language>{lang}</Language>" in d.group(0):
            u = re.search(r"<Url>([^<]+\.html)</Url>", d.group(0))
            if u: return u.group(1)

def texte(num, lang="fr"):
    c = RAC / f"{num}_{lang}.txt"
    if c.exists(): return c.read_text(encoding="utf-8")
    for n, b in trouve(num):
        u = url_html(b, lang)
        if not u: continue
        h = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode("utf-8", "replace")
        t = "\n".join(re.sub(r"\s+", " ", l).strip() for l in decode(h).splitlines() if l.strip())
        c.write_text(f"SOURCE {u}\nN° Swissmedic {n}\n{t}\n", encoding="utf-8")
        return c.read_text(encoding="utf-8")
    sys.exit(f"SmPC {lang} introuvable pour {num}")

if __name__ == "__main__":
    a = argparse.ArgumentParser(); a.add_argument("num", nargs="?"); a.add_argument("--nom"); a.add_argument("--section"); a.add_argument("--lang", default="fr")
    x = a.parse_args()
    if x.nom and not x.num:
        for n, b in trouve(nom=x.nom):
            print(n, re.findall(r"<Description>([^<]+)", b)[:1])
        sys.exit()
    t = texte(x.num, x.lang)
    if x.section:
        i = [m.start() for m in re.finditer(x.section, t, re.I)]
        for p in i[:5]: print("…", t[max(0, p - 200):p + 1200], "\n---")
    else: print(t)
