#!/usr/bin/env python3
"""Mesures de qualité du français (zéro jeton) sur la prose d'un HTML (div.p, p, li, td de plus de 6 mots).
Usage : python metriques_francais.py fichier.html [--json]
Mesures : phrases sans verbe conjugué (spaCy fr), longueur moyenne, densité de connecteurs logiques /100 mots,
répétition de 4-grammes, débuts de phrase identiques consécutifs, abréviations non développées (approx.)."""
import sys, re, json, html as H, collections
import spacy
nlp = spacy.load("fr_core_news_sm", disable=["ner"])
CONN = ["en effet", "ainsi", "donc", "car", "puisque", "parce que", "cependant", "toutefois", "pourtant", "néanmoins",
        "en revanche", "par conséquent", "de plus", "en outre", "d'abord", "ensuite", "enfin", "puis", "alors", "afin de",
        "afin que", "c'est pourquoi", "dès lors", "or", "d'autant plus", "en particulier", "notamment", "si bien que",
        "à l'inverse", "au contraire", "de même", "lorsque", "tandis que", "bien que", "même si", "en cas de", "faute de"]
def prose(src, cellules=False):
    src = re.sub(r"(?is)<(script|style|button)[^>]*>.*?</\1>", " ", src)
    src = re.sub(r"(?is)<(abbr|span class=\"df\"|span class=\"dxc\")[^>]*>.*?</(abbr|span)>", lambda m: m.group(0) if m.group(1)=="abbr" else " ", src)
    motif = r"(?is)<(?:td|li|dd)[^>]*>(.*?)</(?:td|li|dd)>" if cellules else r"(?is)<(?:div class=\"p\"|p)[^>]*>(.*?)</(?:div|p)>"
    blocs = re.findall(motif, src)
    out = []
    for b in blocs:
        t = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<sup.*?</sup>", "", b)))).strip()
        if len(t.split()) > 6: out.append(t)
    return out
def mesurer(path, cellules=False):
    textes = prose(open(path, encoding="utf-8").read(), cellules)
    n_ph = n_sans = mots = 0; conn = 0; debuts = []; grams = collections.Counter(); exemples = []
    for doc in nlp.pipe(textes, batch_size=64):
        for s in doc.sents:
            w = [t for t in s if t.is_alpha]
            if len(w) < 4: continue
            n_ph += 1; mots += len(w)
            if not any(t.pos_ in ("VERB", "AUX") and ("Fin" in t.morph.get("VerbForm") or t.morph.get("Mood")) for t in s):
                n_sans += 1; len(exemples) < 5 and exemples.append(s.text[:120])
            low = " " + s.text.lower().replace("’", "'") + " "
            conn += sum(low.count(" " + c + " ") + low.count(" " + c + ",") for c in CONN)
            debuts.append(" ".join(t.lower_ for t in w[:2]))
            toks = [t.lower_ for t in w]; grams.update(tuple(toks[i:i+4]) for i in range(len(toks) - 3))
    rep4 = sum(c - 1 for c in grams.values() if c > 1)
    consec = sum(1 for a, b in zip(debuts, debuts[1:]) if a == b)
    return {"fichier": path, "phrases": n_ph, "mots": mots,
            "phrases_sans_verbe_%": round(100 * n_sans / max(n_ph, 1), 1),
            "mots_par_phrase": round(mots / max(n_ph, 1), 1),
            "connecteurs_pour_100_mots": round(100 * conn / max(mots, 1), 2),
            "repetitions_4grammes_pour_1000_mots": round(1000 * rep4 / max(mots, 1), 1),
            "debuts_identiques_consecutifs": consec, "exemples_sans_verbe": exemples}
if __name__ == "__main__":
    r = {"prose": mesurer(sys.argv[1]), "cellules_listes": mesurer(sys.argv[1], True)}; print(json.dumps(r, ensure_ascii=False, indent=None if "--json" in sys.argv else 1))
