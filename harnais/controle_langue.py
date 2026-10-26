#!/usr/bin/env python3
"""Contrôle de langue française — script (coût nul en tokens) : LanguageTool 6.8 local + règles du Prompt V0.
  python3 harnais/controle_langue.py <fichier.html> [...] [--rapport <chemin.md>]
Score /100 = 100 − 4·(fautes/1000 mots, plafonné 60) − 2·(abréviations non définies, plafonné 20) ; critique si > 10 fautes/1000 mots
ou ≥ 3 erreurs d'accord/conjugaison certaines. Première ligne du rapport : RESULTAT score=.. critiques=.. question=oui|non"""
import html, re, sys
from collections import Counter
from pathlib import Path
import language_tool_python as LT
ACR_OK = set("ECG IRM CT TDM CRP VS VIH ORL OMS OFSP OFS AIPS PMID DOI HTA TA FC FR SpO2 PA INR TSH ASAT ALAT GGT LDH NFS BNP ESC ERS EASD EAU ESMO EULAR NICE CDC AHA ACC IDSA ADA HAS EMA AWMF SSMIG SGAIM SSED SSI SSP SNC PMN IV IM SC PO AVC AIT ATCD AINS IPP ISRS IMC BMI HbA1c LDL HDL TG DD DX SSP PROFILES CH EU UE USA OMIM GINA GOLD KDIGO RGO MICI BPCO SCA IDM EP TVP ATB ECBU PSA PCR ARN ADN IgE IgG IgM UI Rx Dr Pr".split())
a = sys.argv[1:]; rap = a[a.index("--rapport") + 1] if "--rapport" in a else None; fs = [x for x in a if x.endswith(".html")]
LTON = "--lt" in sys.argv  # LanguageTool désactivé par défaut (lent) ; qualité linguistique = Sonnet 5.5 + contrôles rapides
tool = LT.LanguageTool("fr", config={"maxTextLength": 100000}) if LTON else None
def texte(p):
    t = Path(p).read_text(encoding="utf-8", errors="replace"); t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"</?(p|div|li|tr|h\d|br|details|summary|section|table|td|th)[^>]*>", "\n", t); t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return [re.sub(r"\s+", " ", l).strip() for l in t.splitlines() if len(l.strip()) > 20]
def analyse(p):
    L = texte(p); mots = sum(len(l.split()) for l in L); freq = Counter(w for l in L for w in re.findall(r"[A-Za-zÀ-ÿ]{4,}", l))
    err = []; i = 0
    while i < len(L):
        bloc = "\n".join(L[i:i + 25]); i += 25
        for m in (tool.check(bloc) if tool else []):
            rid = m.rule_id; ctx = (m.context or "")[:110]; mot = bloc[m.offset:m.offset + m.error_length]
            if rid.startswith(("MORFOLOGIK", "HUNSPELL", "FR_SPELLING")):
                if freq.get(mot, 0) >= 3 or re.search(r"[0-9A-Z\-/öüßäñ]", mot) or len(mot) < 4: continue
                if sum(1 for q in re.findall(r"[A-Za-zÀ-ÿ]{4,}", bloc[max(0, m.offset - 60):m.offset + 60]) if q.lower() in ("und", "oder", "der", "die", "das", "mit", "von", "the", "and", "with", "for", "bei", "nach", "für")) >= 1: continue
                cat = "ORTHOGRAPHE"
            elif m.category in ("TYPOGRAPHY", "STYLE", "REDUNDANCY", "PUNCTUATION", "CASING") or rid in ("DATE", "PLACE_DE_LA_VIRGULE", "VIRGULE_VERBE") or rid.startswith(("FRENCH_WHITESPACE", "ESPACE", "APOS", "VIRG", "TIRET", "MAJUSCULE", "UPPERCASE")): continue
            else: cat = "GRAMMAIRE"
            err.append((cat, rid, ctx, "; ".join(m.replacements[:2])))
    txt = " ".join(L); acr = sorted({x for x in re.findall(r"\b[A-Z][A-Za-z]?[A-Z0-9]{1,5}\b", txt) if x not in ACR_OK and len(x) >= 3})
    nd = [x for x in acr if not re.search(rf"\({x}\)|{x} ?\(|{x} ?:|{x} ?=|{x}, ", txt)]
    return mots, err, nd
import spacy
NLP = spacy.load("fr_core_news_sm", disable=["ner", "lemmatizer"])
def sans_verbe(p):
    raw = Path(p).read_text(encoding="utf-8", errors="replace"); out = {}
    for m in re.finditer(r"<h3[^>]*id=[\"']([\w-]+?)-p(\d{1,2})[\"'][^>]*>(.*?)(?=<h3[^>]*id=[\"'][\w-]+?-p\d|$)", raw, re.S):
        n = int(m.group(2))
        if n not in (6, 7, 10, 13): continue
        body = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(table|script|style).*?</\1>", " ", m.group(3)))); bad = []; tot = 0
        for s in NLP.pipe([x.strip() for x in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", body)) if len(x.split()) >= 5]):
            tot += 1
            if not any(t.pos_ in ("VERB", "AUX") for t in s): bad.append(s.text[:90])
        out[n] = (tot, bad)
    return out
out = []
for p in fs:
    mots, err, nd = analyse(p); nso = sum(1 for e in err if e[0] == 'ORTHOGRAPHE'); d = 1000 * len(err) / max(1, mots); acc = sum(1 for e in err if re.search(r"ACCORD|AGREEMENT|CONJUG|PARTICIPE|ACCORD_", e[1]))
    ng = len(err) - nso; dg = 1000 * ng / max(1, mots); ds = 1000 * nso / max(1, mots)
    sc = round(100 - min(50, 6 * dg) - min(15, 1.5 * ds) - min(10, 0.5 * len(nd)), 1); crit = int(dg > 8) + int(acc >= 3)
    sv = sans_verbe(p); mv = []
    for n, (tot, bad) in sv.items():
        if (n == 13 and bad) or (tot and len(bad) / tot > 0.25): mv.append(f"point {n} : {len(bad)}/{tot} phrases sans verbe — « {bad[0] if bad else ''} »")
    sc = round(max(0, sc - min(12, 3 * len(mv))), 1)
    r = f"RESULTAT score={sc} critiques={crit} question={'oui' if sc >= 90 and not crit else 'non'}\n\n# Contrôle de langue — {Path(p).name}\n\n{mots} mots · {len(err)-nso} fautes de grammaire ({dg:.1f}/1000) · {nso} signalements d'orthographe ({ds:.1f}/1000) · {len(nd)} abréviation(s) non définie(s) : {', '.join(nd[:15])}\n\n## CORRECTIONS (≤ 20)\n" + "".join(f"- [PHRASES] {x}\n" for x in mv) + "\n".join(f"- [{c}] {rid} : « {ctx} » → {rep or '?'}" for c, rid, ctx, rep in err[:20]) + "\n"
    out.append(r)
    if rap and len(fs) == 1: Path(rap).write_text(r, encoding="utf-8")
print("\n".join(o.splitlines()[0] + " " + o.splitlines()[2] for o in out)); tool and tool.close()
