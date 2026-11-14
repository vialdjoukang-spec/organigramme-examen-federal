"""Shared helpers: disk-cached HTTP GET (cache/), polite User-Agent, retries."""
import hashlib, json, os, time, urllib.request, urllib.error
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "cache")
UA = "RadioPairesBot/1.0 (educational offline atlas; contact: grokbot) python-urllib"
os.makedirs(CACHE, exist_ok=True)

def _key(url):
    return os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest())

def get(url, binary=False, retries=4, timeout=40):
    """GET with on-disk cache: a URL is never downloaded twice."""
    p = _key(url)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        with open(p, "rb") as f:
            data = f.read()
        return data if binary else data.decode("utf-8", "replace")
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
            tmp = p + ".tmp"
            with open(tmp, "wb") as f:
                f.write(data)
            os.replace(tmp, p)
            return data if binary else data.decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 * (i + 1) + (int(e.headers.get("Retry-After", "0") or 0)))
                continue
            raise
        except Exception as e:  # network hiccup
            last = e
            time.sleep(1.5 * (i + 1))
    raise last

def get_json(url):
    return json.loads(get(url))
