#!/usr/bin/env python3
"""lot3.py — outil de travail du chercheur lot 3 (réutilise fetch_commons/normalize/_common).
  cs "query" [n]         recherche Commons -> refs S.i (registre cache/lot3_cands.json)
  oi "query" [n]         recherche Open-i + licence Europe PMC -> refs S.i (seulement CC*/PD affichés en clair, autres marqués !)
  sheet ref ref ...      planche contact /tmp/sheet.jpg (cellules 300 px, numérotées)
  look ref [crop]        vue unique /tmp/look.jpg (≤700 px), crop=x0,y0,x1,y1 normalisé
  take ID normal|patho ref [crop]   télécharge, recadre, normalise -> images/<role>/ID_<role>.jpg + .meta.json (cache/meta/)
  ov ID "tx,ty,fx,fy;..."  overlay flèches sur patho + normale à gauche -> /tmp/ov.jpg
  grid ID role           image avec grille 10% -> /tmp/grid.jpg
"""
import sys, os, json, re, html, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import get, get_json, ROOT
import fetch_commons as fc
from normalize import normalize
from PIL import Image, ImageDraw, ImageFont
REG = os.path.join(ROOT, "cache", "lot3_cands.json")
META = os.path.join(ROOT, "cache", "meta"); os.makedirs(META, exist_ok=True)
def reg():
    return json.load(open(REG)) if os.path.exists(REG) else {"n": 0, "c": {}}
def save(r): json.dump(r, open(REG, "w"), ensure_ascii=False)
def strip(s): return fc.strip(s)
FREE = re.compile(r"(cc0|public domain|cc[- ]by(-sa)?|pd-)", re.I)
NC = re.compile(r"(nc|nd)", re.I)
def lic_ok(l):
    l = (l or "").lower()
    return bool(FREE.search(l)) and not re.search(r"\b(nc|nd)\b|-nc|-nd|noncommercial|noderiv", l)
def epmc_license(pmcid):
    try:
        d = get_json("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:PMC%s&resultType=core&format=json" % pmcid)
        r = d["resultList"]["result"][0]
        return r.get("license") or "?"
    except Exception as e:
        return "?"
def cs(q, n=12):
    r = reg(); r["n"] += 1; S = r["n"]
    res = fc.search(q + " filetype:bitmap", n)
    for i, m in enumerate(res):
        k = f"{S}.{i}"
        m["src"] = "commons"; r["c"][k] = m
        fl = " " if lic_ok(m["license"]) else "!"
        print(f"{fl}{k} {m['title'][5:90]} | {m['license']} | {m['width']}x{m['height']} | {m['description'][:150]}")
    save(r)
def oi(q, n=12):
    r = reg(); r["n"] += 1; S = r["n"]
    q = re.sub(r"[^\w\s-]", " ", q)
    url = "https://openi.nlm.nih.gov/api/search?" + urllib.parse.urlencode({"query": q, "m": 1, "n": n})
    try: d = get_json(url)
    except Exception as e:
        import hashlib; fp = os.path.join(ROOT, "cache", hashlib.sha1(url.encode()).hexdigest())
        if os.path.exists(fp): os.remove(fp)
        print("openi error", e); return
    for i, x in enumerate(d.get("list", [])):
        k = f"{S}.{i}"
        im = x.get("image", {}); cap = strip(im.get("caption", "")) if isinstance(im, dict) else ""
        lic = epmc_license(x.get("pmcid", ""))
        m = {"src": "openi", "title": x.get("title"), "uid": x.get("uid"), "pmcid": x.get("pmcid"),
             "source_url": "https://openi.nlm.nih.gov" + x.get("detailedQueryURL", "").split("&query")[0],
             "article_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC%s/" % x.get("pmcid"),
             "license": lic, "author": strip(x.get("authors", "")), "description": cap,
             "journal": x.get("journal_title"), "thumb_url": "https://openi.nlm.nih.gov" + x.get("imgLarge", "")}
        r["c"][k] = m
        fl = " " if lic_ok(lic) else "!"
        print(f"{fl}{k} [{lic}] {m['journal'][:30]} | {cap[:260]}")
    save(r)
def cat(c, n=40):
    r = reg(); r["n"] += 1; S = r["n"]
    d = fc._q({"action": "query", "generator": "categorymembers", "gcmtitle": c if c.startswith("Category:") else "Category:"+c, "gcmtype": "file|subcat", "gcmlimit": str(n)})
    pages = list((d.get("query", {}).get("pages", {}) or {}).values())
    for i, p in enumerate(pages):
        if p.get("ns") == 14: print("  [cat]", p["title"]); continue
        m = fc._meta(p); k = f"{S}.{i}"; m["src"] = "commons"; r["c"][k] = m
        fl = " " if lic_ok(m["license"]) else "!"
        print(f"{fl}{k} {m['title'][5:80]} | {m['license']} | {m['width']}x{m['height']} | {m['description'][:110]}")
    save(r)
def subcats(q):
    d = get_json("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({"action":"query","list":"search","srnamespace":"14","srsearch":q,"srlimit":"15","format":"json"}))
    for x in d["query"]["search"]: print(x["title"])
def titles(ts):
    r = reg(); r["n"] += 1; S = r["n"]
    for i, t in enumerate(ts):
        m = fc.info(t); m["src"] = "commons"; k = f"{S}.{i}"; r["c"][k] = m
        print(f"{' ' if lic_ok(m['license']) else '!'}{k} {m['title'][5:80]} | {m['license']} | {m['width']}x{m['height']} | {m['description'][:200]}")
    save(r)
def gif(ref, step=1):
    import io
    m = reg()["c"][ref]; raw = get(m["orig_url"].split("?")[0], binary=True)
    im = Image.open(io.BytesIO(raw)); r = reg(); r["n"] += 1; S = r["n"]
    d = os.path.join(ROOT, "cache", "frames"); os.makedirs(d, exist_ok=True)
    print("frames", im.n_frames); out = []
    for f in range(0, im.n_frames, step):
        im.seek(f); fp = os.path.join(d, re.sub(r"\W", "_", m["title"])[:60] + f"_{f:03d}.png"); im.convert("RGB").save(fp)
        mm = dict(m); mm["local"] = fp; mm["frame"] = f; k = f"{S}.{f}"; r["c"][k] = mm; out.append(k)
    save(r); print(" ".join(out))
LOT = {x["id"]: x for x in json.load(open(os.path.join(ROOT, "lot3.json")))}
def man(ID, js):
    j = json.loads(js); x = LOT[ID]
    out = {"id": ID, "dx": x["dx"], "cliche": x["cliche"], "statut": j["statut"]}
    for role in ("normal", "patho"):
        mp = os.path.join(META, f"{ID}_{role}.json")
        if not os.path.exists(mp): continue
        m = json.load(open(mp)); src = m.get("source_url"); 
        if m.get("src") == "openi": src = m.get("article_url")
        if m.get("src") == "pmc": e0 = {"figure_url": m.get("thumb_url"), "doi": m.get("doi"), "journal": m.get("journal")}
        else: e0 = {}
        e = {"file": m["file"], "source_url": src, "license": m["license"], "author": m["author"],
             "title": (m.get("title") or "")}
        if m.get("frame") is not None: e["note_source"] = f"image {m['frame']} de l'animation"
        if m.get("crop"): e["recadrage"] = m["crop"]
        if m.get("src") == "openi": e["openi_url"] = m["source_url"]; e["journal"] = m.get("journal")
        e.update(e0); e.update(j.get(role, {})); out[role] = e
    for k in ("pair_match", "a_verifier", "queries"): out[k] = j.get(k, [] if k != "pair_match" else "")
    json.dump(out, open(os.path.join(ROOT, "manifest", f"{ID}.json"), "w"), ensure_ascii=False, indent=1)
    print("manifest", ID, out["statut"], "arrows", len(out.get("patho", {}).get("arrows", [])))
EP = "https://www.ebi.ac.uk/europepmc/webservices/rest/"
def ep(q, n=8, kw=None):
    r = reg(); r["n"] += 1; S = r["n"]; i = 0
    qq = f'({q}) AND OPEN_ACCESS:y AND (LICENSE:"cc by" OR LICENSE:"cc0" OR LICENSE:"cc by-sa") AND HAS_FT:y'
    d = get_json(EP + "search?" + urllib.parse.urlencode({"query": qq, "format": "json", "pageSize": n, "resultType": "core"}))
    print("hits", d.get("hitCount"))
    for res in d["resultList"]["result"]:
        pmc = res.get("pmcid"); lic = res.get("license") or "?"
        if not pmc: continue
        try: x = get(EP + pmc + "/fullTextXML")
        except Exception as e: print("noxml", pmc); continue
        auth = res.get("authorString", "")[:120]
        for fg in re.findall(r"<fig[ >].*?</fig>", x, re.S):
            cap = strip(re.sub(r"<label>(.*?)</label>", r"\1. ", fg))
            hrefs = re.findall(r'xlink:href="([^"]+)"', fg)
            if not hrefs: continue
            if kw and not re.search(kw, cap, re.I): continue
            k = f"{S}.{i}"; i += 1
            r["c"][k] = {"src": "pmc", "pmcid": pmc, "href": hrefs[0], "title": res.get("title"), "license": lic,
                         "author": auth, "journal": (res.get("journalInfo") or {}).get("journal", {}).get("title"),
                         "year": res.get("pubYear"), "description": cap,
                         "source_url": f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/", "doi": res.get("doi")}
            fl = " " if lic_ok(lic) else "!"
            print(f"{fl}{k} [{lic}] {pmc} | {cap[:300]}")
    save(r)
def pmc_img(m):
    html_ = get(m["source_url"]); base = re.sub(r"\.(jpe?g|tiff?|gif|png|webp)$", "", m["href"])
    u = re.findall(r'https://cdn\.ncbi\.nlm\.nih\.gov/pmc/blobs/[^"\s]*?/' + re.escape(base) + r'\.(?:jpe?g|png|gif|webp)', html_)
    if not u: raise Exception("no cdn url for " + base)
    return u[0]
def fetch(ref):
    m = reg()["c"][ref]
    if m.get("local"): return m, Image.open(m["local"]).convert("RGB")
    if m.get("src") == "pmc" and not m.get("thumb_url"):
        r = reg(); m["thumb_url"] = pmc_img(m); r["c"][ref] = m; save(r)
    return m, Image.open(__import__("io").BytesIO(get(m["thumb_url"], binary=True))).convert("RGB")
def cropim(im, crop):
    if not crop: return im
    x0, y0, x1, y1 = [float(v) for v in crop.split(",")]
    W, H = im.size
    return im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
CS = int(os.environ.get("CS", 300))
def sheet(refs):
    cells = []
    for ref in refs:
        try:
            m, im = fetch(ref); im.thumbnail((CS, CS)); cells.append((ref, im))
        except Exception as e: print("ERR", ref, e)
    CS2 = CS; cols = min(int(os.environ.get("COLS", 4)), len(cells)); rows = (len(cells) + cols - 1) // cols
    sh = Image.new("RGB", (cols*(CS+5), rows*(CS+20)), (40, 40, 40)); d = ImageDraw.Draw(sh)
    for i, (ref, im) in enumerate(cells):
        x, y = (i % cols)*(CS+5), (i//cols)*(CS+20)
        sh.paste(im, (x, y+18)); d.text((x+3, y+3), ref, fill=(255, 255, 0))
    sh.save("/tmp/sheet.jpg", quality=80); print("/tmp/sheet.jpg", sh.size)
def look(ref, crop=None):
    m, im = fetch(ref); im = cropim(im, crop); im.thumbnail((700, 700)); im.save("/tmp/look.jpg", quality=85)
    print("/tmp/look.jpg", im.size)
def take(ID, role, ref, crop=None):
    m, im = fetch(ref); im = cropim(im, crop)
    dest = os.path.join(ROOT, "images", role, f"{ID}_{role}.jpg")
    tmp = "/tmp/take.png"; im.save(tmp); w, h = normalize(tmp, dest); os.remove(tmp)
    m = dict(m); m.update({"ref": ref, "crop": crop, "file": f"images/{role}/{ID}_{role}.jpg", "file_size": [w, h]})
    json.dump(m, open(os.path.join(META, f"{ID}_{role}.json"), "w"), ensure_ascii=False, indent=1)
    print("OK", dest, w, h, m["license"], "|", m["author"][:60], "| lic_ok=", lic_ok(m["license"]))
def ov(ID, spec):
    P = Image.open(os.path.join(ROOT, "images", "patho", f"{ID}_patho.jpg")).convert("RGB")
    W, H = P.size; d = ImageDraw.Draw(P); lw = max(3, W//200)
    for j, a in enumerate(spec.split(";")):
        tx, ty, fx, fy = [float(v) for v in a.split(",")]
        T, F = (tx*W, ty*H), (fx*W, fy*H)
        d.line([F, T], fill=(0, 0, 0), width=lw+4); d.line([F, T], fill=(255, 230, 0), width=lw)
        import math; ang = math.atan2(T[1]-F[1], T[0]-F[0]); L = lw*5
        pts = [T, (T[0]-L*math.cos(ang-0.45), T[1]-L*math.sin(ang-0.45)), (T[0]-L*math.cos(ang+0.45), T[1]-L*math.sin(ang+0.45))]
        d.polygon(pts, fill=(255, 230, 0), outline=(0, 0, 0)); d.text((F[0]+4, F[1]+4), str(j+1), fill=(0, 255, 255))
    npth = os.path.join(ROOT, "images", "normal", f"{ID}_normal.jpg")
    if os.path.exists(npth):
        N = Image.open(npth).convert("RGB"); h = 500
        N = N.resize((int(N.width*h/N.height), h)); P = P.resize((int(W*h/H), h))
        out = Image.new("RGB", (N.width+P.width+10, h)); out.paste(N, (0, 0)); out.paste(P, (N.width+10, 0))
    else:
        out = P; out.thumbnail((700, 700))
    out.save("/tmp/ov.jpg", quality=85); print("/tmp/ov.jpg", out.size)
def grid(ID, role):
    P = Image.open(os.path.join(ROOT, "images", role, f"{ID}_{role}.jpg")).convert("RGB")
    P.thumbnail((700, 700)); W, H = P.size; d = ImageDraw.Draw(P)
    for i in range(1, 10):
        d.line([(i*W/10, 0), (i*W/10, H)], fill=(0, 255, 0), width=1); d.line([(0, i*H/10), (W, i*H/10)], fill=(0, 255, 0), width=1)
        d.text((i*W/10+2, 2), str(i), fill=(255, 255, 0)); d.text((2, i*H/10+2), str(i), fill=(255, 255, 0))
    P.save("/tmp/grid.jpg", quality=85); print("/tmp/grid.jpg", P.size)
if __name__ == "__main__":
    a = sys.argv[1:]; c = a[0]
    if c == "cs": cs(a[1], int(a[2]) if len(a) > 2 else 12)
    elif c == "oi": oi(a[1], int(a[2]) if len(a) > 2 else 12)
    elif c == "cat": cat(a[1], int(a[2]) if len(a) > 2 else 40)
    elif c == "cats": subcats(a[1])
    elif c == "t": titles(a[1:])
    elif c == "gif": gif(a[1], int(a[2]) if len(a) > 2 else 1)
    elif c == "man": man(a[1], open(a[2]).read() if a[2].endswith(".json") else a[2])
    elif c == "ep": ep(a[1], int(a[2]) if len(a) > 2 else 8, a[3] if len(a) > 3 else None)
    elif c == "sheet": sheet(a[1:])
    elif c == "look": look(a[1], a[2] if len(a) > 2 else None)
    elif c == "take": take(a[1], a[2], a[3], a[4] if len(a) > 4 else None)
    elif c == "ov": ov(a[1], a[2])
    elif c == "grid": grid(a[1], a[2])
    elif c == "info": print(json.dumps(reg()["c"][a[1]], ensure_ascii=False, indent=1)[:3000])
