#!/usr/bin/env python3
"""fetch_openi.py — Open-i (NIH/NLM) figure search + download, with article licence.
CLI:
  python3 scripts/fetch_openi.py search "query" [-n 15] [--it x|c|m|u|ph|g] [--lic by|bysa|bync...] [--json]
      it: x=X-ray, c=CT, m=MRI, u=ultrasound (Open-i image-type filter; optional)
      -> uid#fig | licence | journal year | caption (short) | uid key for get
      '!' prefix = licence not in whitelist (only by / by-sa / cc0 / pd are acceptable; NC/ND rejected)
  python3 scripts/fetch_openi.py get <UID_KEY> dest.jpg
      UID_KEY = the 'key' printed by search (e.g. PMC8219779_41598_2021_92523_Fig3_HTML); the query
      used must still be in cache: pass --q "query" if not the last search (default: last search).
      -> downloads the 512 px image (Open-i max), normalizes, writes dest.jpg.meta.json
         {source_url (PMC article), license, license_url, author, description(caption), citation, pmcid}
Note: Open-i serves at most 512 px; for a sharper figure use the PMC article figure (source_url).
"""
import sys, os, re, json, html, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import get, get_json, CACHE
from normalize import normalize
BASE = "https://openi.nlm.nih.gov"
LAST = os.path.join(CACHE, "openi_last_query.txt")
LIC = {"by": "CC BY", "by-sa": "CC BY-SA", "cc0": "CC0", "pd": "Public domain",
       "by-nc": "CC BY-NC", "by-nc-sa": "CC BY-NC-SA", "by-nd": "CC BY-ND", "by-nc-nd": "CC BY-NC-ND"}

def strip(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s or ""))).strip()

def lic_of(it):
    cc = (it.get("ccLicense") or "").strip().lower()
    url = it.get("licenseURL") or ""
    m = re.search(r"licenses/([a-z\-]+)/(\d\.\d)", url)
    if m:
        return LIC.get(m.group(1), m.group(1)) + " " + m.group(2), url
    if "publicdomain/zero" in url:
        return "CC0", url
    return (LIC.get(cc, cc or "?")), url

def free(lic):
    l = lic.lower()
    return l.startswith(("cc by ", "cc by-sa", "cc0", "public domain")) or l in ("cc by", "cc by-sa")

def _rec(it):
    lic, url = lic_of(it)
    img = it.get("image", {}) or {}
    key = os.path.basename(it.get("imgLarge", "")).rsplit(".", 1)[0]
    jd = it.get("journal_date") or {}
    return {"key": key, "uid": it.get("uid"), "fig": img.get("id"),
            "license": lic, "license_url": url, "author": it.get("authors", ""),
            "title": strip(it.get("title")), "journal": it.get("journal_title", ""), "year": jd.get("year", ""),
            "description": strip(img.get("caption")), "modality": img.get("modalityMajor"),
            "img_url": BASE + it.get("imgLarge", ""),
            "source_url": f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{it.get('pmcid')}/" if it.get("pmcid") else BASE + it.get("detailedQueryURL", ""),
            "pmcid": it.get("pmcid"), "pmid": it.get("pmid")}

def search(q, n=15, it=None, lic=None):
    p = {"query": q, "m": "1", "n": str(n)}
    if it:
        p["it"] = it
    if lic:
        p["lic"] = lic
    d = get_json(BASE + "/api/search?" + urllib.parse.urlencode(p))
    open(LAST, "w").write(json.dumps(p))
    return [_rec(x) for x in d.get("list", [])]

def download(key, dest, q=None):
    p = json.loads(open(LAST).read()) if q is None else {"query": q, "m": "1", "n": "30"}
    d = get_json(BASE + "/api/search?" + urllib.parse.urlencode(p))
    recs = [_rec(x) for x in d.get("list", [])]
    r = next((x for x in recs if x["key"] == key), None)
    if not r:
        raise SystemExit("key not in that search result; pass --q 'query'")
    tmp = dest + ".src"
    open(tmp, "wb").write(get(r["img_url"], binary=True))
    w, h = normalize(tmp, dest)
    os.remove(tmp)
    r.update({"file_width": w, "file_height": h,
              "citation": f"{r['author']}. {r['title']}. {r['journal']} {r['year']}. PMC{r['pmcid']}, figure {r['fig']}."})
    json.dump(r, open(dest + ".meta.json", "w"), ensure_ascii=False, indent=1)
    return r

if __name__ == "__main__":
    a = sys.argv[1:]
    def opt(name, default=None):
        if name in a:
            i = a.index(name); v = a[i + 1]; del a[i:i + 2]; return v
        return default
    n = int(opt("-n", 15)); it = opt("--it"); q = opt("--q"); lic = opt("--lic")
    js = "--json" in a; a = [x for x in a if x != "--json"]
    if len(a) >= 2 and a[0] == "search":
        res = search(a[1], n, it, lic)
        if js:
            print(json.dumps(res, ensure_ascii=False, indent=1)); sys.exit(0)
        for r in res:
            print(f"{' ' if free(r['license']) else '!'} {r['key']} | {r['license']} | {r['journal'][:30]} {r['year']} | {r['modality']} | {r['description'][:180]}")
    elif len(a) >= 3 and a[0] == "get":
        r = download(a[1], a[2], q)
        print(f"OK {a[2]} {r['file_width']}x{r['file_height']} | {r['license']} | {r['source_url']}")
        if not free(r["license"]):
            print("WARNING: licence not in whitelist:", r["license"])
    else:
        print(__doc__); sys.exit(1)
