#!/usr/bin/env python3
"""PubMed (E-utilities NCBI) — compact, avec cache .cache/pubmed/.
  python3 harnais/pubmed.py chercher "<requête>" [n=8]     → PMID | année | revue | titre
  python3 harnais/pubmed.py verifier <PMID>               → titre, revue, année, DOI, URL ; échec si inconnu"""
import json, sys, urllib.parse, urllib.request, hashlib
from pathlib import Path
CA = Path(__file__).resolve().parent.parent / ".cache" / "pubmed"; CA.mkdir(parents=True, exist_ok=True)
B = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
def get(u):
    f = CA / (hashlib.sha256(u.encode()).hexdigest()[:24] + ".json")
    if f.exists(): return json.loads(f.read_text())
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=30)); f.write_text(json.dumps(d)); return d
def resume(ids):
    d = get(B + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(ids))["result"]
    for i in ids:
        r = d.get(i)
        if not r: print(i, "INCONNU"); continue
        doi = next((x["value"] for x in r.get("articleids", []) if x["idtype"] == "doi"), "")
        print(i, "|", r["pubdate"][:4], "|", r.get("source", ""), "|", r["title"][:140], "|", doi)
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["chercher"]:
        n = a[2] if len(a) > 2 else "8"
        ids = get(B + "esearch.fcgi?db=pubmed&retmode=json&retmax=%s&sort=relevance&term=%s" % (n, urllib.parse.quote(a[1])))["esearchresult"]["idlist"]
        resume(ids) if ids else print("AUCUN RÉSULTAT")
    elif a[:1] == ["verifier"]: resume([a[1]])
    else: print(__doc__)
