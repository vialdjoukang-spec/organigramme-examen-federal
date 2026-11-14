#!/usr/bin/env python3
"""fetch_commons.py — Wikimedia Commons search + download (licence/author/description from extmetadata).
CLI:
  python3 scripts/fetch_commons.py search "query" [-n 15] [--json]
      -> title | licence | WxH | short description | url  (! = licence hors liste blanche, ~ = pas une image)
      Astuce : ajouter "filetype:bitmap" à la requête pour exclure PDF/SVG.
  python3 scripts/fetch_commons.py findcat "pneumothorax"      -> category names (much more precise than full-text)
  python3 scripts/fetch_commons.py cat "X-rays of pneumothorax" [-n 50]  -> same columns as search
  python3 scripts/fetch_commons.py info "File:Title.jpg"
  python3 scripts/fetch_commons.py get "File:Title.jpg" dest.jpg
      -> downloads the 1024 px thumb (cached in cache/), normalizes (JPEG<=1024 q85, no EXIF)
         and writes dest.jpg.meta.json {title, source_url, license, license_url, author, description, credit, width, height, orig_url}
"""
import sys, os, re, json, html, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import get, get_json
from normalize import normalize
API = "https://commons.wikimedia.org/w/api.php"
FREE = re.compile(r"^(cc0|public domain|pd\b|pd-|cc[- ]by(-sa)?[- ]?\d|cc by(-sa)? \d|attribution)", re.I)

def strip(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()

def _meta(page):
    ii = (page.get("imageinfo") or [{}])[0]
    em = ii.get("extmetadata", {})
    g = lambda k: strip(em.get(k, {}).get("value", ""))
    return {
        "title": page.get("title"),
        "source_url": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(page.get("title", "").replace(" ", "_")),
        "license": g("LicenseShortName"),
        "license_url": g("LicenseUrl"),
        "author": g("Artist"),
        "credit": g("Credit"),
        "description": g("ImageDescription"),
        "categories": g("Categories"),
        "width": ii.get("width"), "height": ii.get("height"),
        "mime": ii.get("mime"),
        "orig_url": ii.get("url"),
        "thumb_url": ii.get("thumburl") or ii.get("url"),
    }

def _q(params):
    params.update({"format": "json", "prop": "imageinfo",
                   "iiprop": "url|extmetadata|size|mime", "iiurlwidth": "1024"})
    return get_json(API + "?" + urllib.parse.urlencode(params))

def search(query, n=15):
    d = _q({"action": "query", "generator": "search", "gsrnamespace": "6",
            "gsrsearch": query, "gsrlimit": str(n)})
    pages = sorted((d.get("query", {}).get("pages", {}) or {}).values(), key=lambda p: p.get("index", 0))
    return [_meta(p) for p in pages]

def info(title):
    if not title.startswith("File:"):
        title = "File:" + title
    d = _q({"action": "query", "titles": title})
    pages = list((d.get("query", {}).get("pages", {}) or {}).values())
    if not pages or "missing" in pages[0]:
        raise SystemExit("not found: " + title)
    return _meta(pages[0])

def category(cat, n=50):
    """Files in a Commons category (e.g. 'X-rays of pneumothorax')."""
    if not cat.startswith("Category:"):
        cat = "Category:" + cat
    d = _q({"action": "query", "generator": "categorymembers", "gcmtitle": cat,
            "gcmtype": "file", "gcmlimit": str(n)})
    return [_meta(p) for p in (d.get("query", {}).get("pages", {}) or {}).values()]

def findcat(q, n=15):
    """Search Commons category names (namespace 14)."""
    d = get_json(API + "?" + urllib.parse.urlencode({"action": "query", "list": "search", "srnamespace": "14",
                 "srsearch": q, "srlimit": str(n), "format": "json"}))
    return [x["title"] for x in d.get("query", {}).get("search", [])]

def is_free(lic):
    return bool(FREE.search((lic or "").strip()))

def download(title, dest):
    m = info(title)
    if m["mime"] and not m["mime"].startswith("image/"):
        raise SystemExit("not an image: %s" % m["mime"])
    raw = get(m["thumb_url"], binary=True)
    tmp = dest + ".src"
    open(tmp, "wb").write(raw)
    os.makedirs(os.path.dirname(os.path.abspath(dest)), exist_ok=True)
    w, h = normalize(tmp, dest)
    os.remove(tmp)
    m.update({"file_width": w, "file_height": h})
    json.dump(m, open(dest + ".meta.json", "w"), ensure_ascii=False, indent=1)
    return m

if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 2:
        print(__doc__); sys.exit(1)
    if a[0] == "findcat":
        for t in findcat(a[1]):
            print(t)
        sys.exit(0)
    if a[0] in ("search", "cat"):
        n = 15
        if "-n" in a:
            i = a.index("-n"); n = int(a[i + 1]); del a[i:i + 2]
        js = "--json" in a
        a = [x for x in a if x != "--json"]
        res = search(a[1], n) if a[0] == "search" else category(a[1], max(n, 50) if n == 15 else n)
        if js:
            print(json.dumps(res, ensure_ascii=False, indent=1)); sys.exit(0)
        for r in res:
            flag = " " if is_free(r["license"]) else "!"
            if not (r.get("mime") or "image/").startswith("image/"):
                flag = "~"  # pdf/video: usable only if a page thumb is wanted
            print(f"{flag} {r['title']} | {r['license'] or '?'} | {r['width']}x{r['height']} | {r['description'][:160]} | {r['source_url']}")
    elif a[0] == "info":
        print(json.dumps(info(a[1]), ensure_ascii=False, indent=1))
    elif a[0] == "get" and len(a) >= 3:
        m = download(a[1], a[2])
        print(f"OK {a[2]} {m['file_width']}x{m['file_height']} | {m['license']} | {m['author'][:80]}")
        if not is_free(m["license"]):
            print("WARNING: licence not in whitelist:", m["license"])
    else:
        print(__doc__); sys.exit(1)
