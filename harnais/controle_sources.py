#!/usr/bin/env python3
"""Ancrage des chiffres dans leurs sources (anti-invention), gratuit : chaque chiffre suivi de [Sn] est cherché dans le texte réel de la source Sn
(résumé PubMed via PMID, page HTML ou PDF via pdftotext). Module + CLI : python3 harnais/controle_sources.py <fichier.html>"""
import hashlib, html, re, subprocess, sys, urllib.request
from pathlib import Path
R = Path(__file__).resolve().parent.parent; CA = R / ".cache/script_audit"; CA.mkdir(parents=True, exist_ok=True)
def _get(u):
    k = CA / ("src_" + hashlib.sha256(u.encode()).hexdigest()[:24])
    if k.exists(): return k.read_bytes()
    for _ in range(3):
        try:
            b = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=40).read(); k.write_bytes(b); return b
        except Exception: pass
    return b""
def texte_source(pmid=None, url=None):
    if pmid:
        b = _get(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml")
        return html.unescape(re.sub(r"<[^>]+>", " ", b.decode("utf-8", "replace")))
    if url:
        b = _get(url)
        if b[:4] == b"%PDF":
            f = CA / ("pdf_" + hashlib.sha256(url.encode()).hexdigest()[:16] + ".pdf"); f.write_bytes(b)
            return subprocess.run(["pdftotext", "-q", str(f), "-"], capture_output=True, text=True).stdout
        return html.unescape(re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>|<[^>]+>", " ", b.decode("utf-8", "replace")))
    return ""
def sources(txt):
    S = {}
    for m in re.finditer(r"\[S(\d+)\]\s*([^\[]{20,600}?)(?=\s\[S\d+\]|$)", txt):
        c = m.group(2); p = re.search(r"PMID\D{0,3}(\d{6,9})", c); u = re.search(r"https?://\S+", c)
        if p or u: S[m.group(1)] = (p.group(1) if p else None, u.group(0).rstrip(".,;)") if u else None)
    return S
norm = lambda s: re.sub(r"[\s  ]+", "", s).replace(",", ".")
def ancrage(txt, limite=60):
    S = sources(txt); cache = {}; ok = ko = 0; manq = []
    for m in re.finditer(r"(\d+(?:[.,]\d+)?)\s?%", txt):
        tags = [t for t in re.findall(r"\[S(\d+)\]", txt[m.end():m.end() + 90]) if t in S]
        if not tags: continue
        if ok + ko >= limite: break
        v = m.group(1).replace(",", "."); ctx = txt[max(0, m.start() - 60):m.end() + 25]
        fr = re.findall(r"(\d+)\s*(?:sur|/)\s*(\d+)", ctx); need = [v] + (list(fr[-1]) if fr else [])
        found = False
        for t in tags:
            if t not in cache: cache[t] = norm(texte_source(*S[t]))
            if any(norm(x) in cache[t] for x in need): found = True; break
        if found: ok += 1
        else: ko += 1; manq.append(f"{m.group(0)} [S{','.join(tags)}]")
    return ok, ko, manq
if __name__ == "__main__":
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace"))))
    o, k, m = ancrage(t); print(f"{o} chiffres retrouvés dans leur source / {o+k} contrôlés ; non retrouvés : {m[:10]}")
