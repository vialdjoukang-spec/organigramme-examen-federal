#!/usr/bin/env python3
"""Contrôle médical par script (coût nul en tokens) : ANCRAGE dans les sources + exigences de contenu du Prompt V0 §11–§12.
  python3 harnais/controle_medical.py <fichier.html> [--rapport <chemin.md>]
Vérifie : doses des spécialités suisses ∈ texte AIPS lu (aips_texte.py) · grossesse/allaitement cohérents avec l'AIPS ·
n° Swissmedic ∈ corpus · PMID existants et chiffres retrouvés dans le résumé PubMed · points §11 présents et substantiels ·
gold standard / Se-Sp / seuils (point 9) · 11.A–D · 🚩/E-rangs (Phase A) · « À vérifier » restants.
NE JUGE PAS la pertinence clinique : il détecte l'invention, l'écart à la source et l'omission structurelle."""
import html, json, re, subprocess, sys, urllib.request
from pathlib import Path
R = Path(__file__).resolve().parent.parent; sys.path.insert(0, str(R / "harnais"))
f = Path(sys.argv[1]); rap = sys.argv[sys.argv.index("--rapport") + 1] if "--rapport" in sys.argv else None
raw = f.read_text(encoding="utf-8", errors="replace"); txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", raw)))
crit, moy, ok = [], [], []
phaseA = "Phase_A" in f.name
norm = lambda s: re.sub(r"[\s  ]+", "", s.lower().replace(",", ".").replace("µ", "u").replace("μ", "u"))
# 1. AIPS : n° → texte ; marques via <Description> ; doses des phrases mentionnant la marque
xml = (R / ".cache/aips/AipsDownload_20261008.xml").read_text(encoding="utf-8-sig")
ids = set(re.findall(r"<Identifier>(\d+)</Identifier>", xml))
sm = sorted(set(re.findall(r"(?:Swissmedic|AIPS|autorisation)\D{0,40}?\b(\d{5})\b", txt)))
for n in sm:
    if n not in ids: crit.append(f"n° Swissmedic {n} absent du corpus AIPS")
import aips_texte as AT
ecarts = []; nd = 0
for n in sm:
    if n not in ids: continue
    try: a = AT.texte(n)
    except SystemExit: moy.append(f"AIPS {n} : texte FR introuvable"); continue
    except Exception as e: moy.append(f"AIPS {n} : {e}"); continue
    na = norm(a); desc = next((re.findall(r"<Description>([^<]+)", b)[:1] for _, b in AT.trouve(n)), [""])[0]; marque = re.split(r"[®,]", desc)[0].strip()
    if len(marque) < 3: continue
    for mm in re.finditer(re.escape(marque), txt, re.I):
        ph = txt[mm.start():mm.start() + 160]
        ph = re.split(r"(?<=[a-zé\)\d\]])\.\s|\]\s(?=[A-Z])|;|®\s*\(?n°|\(n° ?\d{5}\)|\b[A-ZÉ][A-Za-zéèï]{3,}®", ph[len(marque):])[0]
        for dm in re.finditer(r"\d{1,3}(?:[ \u202f\u00a0]\d{3})*(?:[.,]\d+)?\s?(?:mg|µg|μg|g|UI|ml|mL)(?:/\w+)?", ph):
            d = dm.group(0)
            if re.search(r"[=×x]\s*$", ph[max(0, dm.start() - 8):dm.start()]) or re.search(r"^\s*[=×]", ph[dm.end():dm.end() + 4]): continue  # valeur calculée
            nd += 1
            if norm(d.split("/")[0]) not in na: ecarts.append(f"{marque} ({n}) : « {d.strip()} » absent du texte AIPS — « {ph[:90]}… »")
        if re.search(r"grossesse|enceinte", ph, re.I) and re.search(r"contre-indiqu", ph, re.I) and not re.search(r"(pas|non|sans)\s+(de\s+)?contre-indic|n'est pas contre", ph, re.I) and not re.search(r"contre-indiqu[^.]{0,120}(grossesse|enceinte)|(grossesse|enceinte)[^.]{0,200}contre-indiqu", a, re.I):
            ecarts.append(f"{marque} ({n}) : grossesse « contre-indiqué » non retrouvé dans l'AIPS")
if ecarts: crit += ecarts[:6]; moy += ecarts[6:12]
ok.append(f"{nd} dose(s) de spécialités suisses vérifiée(s) vs AIPS ; {len(ecarts)} écart(s)")
# 2. PubMed : existence + chiffre dans le résumé
pm = sorted(set(re.findall(r"PMID\D{0,3}(\d{6,9})", txt))); introuv = []; nonret = 0
if pm:
    import time as _t
    for _k in range(6):
        try: d = json.load(urllib.request.urlopen(urllib.request.Request("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(pm), headers={"User-Agent": "Mozilla/5.0"}), timeout=30))["result"]; break
        except urllib.error.HTTPError as _e:
            if _e.code != 429: raise
            _t.sleep(2 + 3 * _k)
    else: d = {}
    introuv = [p for p in pm if p not in d or "error" in d.get(p, {})]
    for p in introuv: crit.append(f"PMID {p} inexistant")
    ok.append(f"{len(pm)-len(introuv)}/{len(pm)} PMID existent")
# 2 bis. chiffres suivis de [Sn] retrouvés dans le texte réel de la source
import controle_sources as CS
try:
    o, k, manq = CS.ancrage(txt)
    if o + k: ok.append(f"{o}/{o+k} chiffres retrouvés dans leur source (résumé PubMed / page / PDF)")
    if k >= 5 and o / (o + k) < 0.5: crit.append(f"chiffres non retrouvés dans leurs sources : {k}/{o+k} — {', '.join(manq[:6])}")
    elif k: moy += [f"chiffre non retrouvé dans sa source : {x}" for x in manq[:6]]
except Exception as ex: moy.append(f"ancrage des sources non exécuté : {ex}")
# 2 ter. spécialités citées avec ® existent dans l'AIPS
_n = lambda s: re.sub(r"[\s\-]+", "", s.lower())
noms = {_n(x) for x in re.findall(r"<Description>\s*([^<,®]{3,50}?)\s*[®,<]", xml)} | {_n(x.split()[0]) for x in re.findall(r"<Description>\s*([^<,®]{3,50}?)\s*[®,<]", xml)}
noms |= {_n(x.split()[0]) for x in re.findall(r"<Name>([^<]{3,60})</Name>", xml)}
inc = sorted({m for m in re.findall(r"\b([A-ZÉ][A-Za-zéèï\-]{3,})®", txt) if _n(m) not in noms and not any(n.startswith(_n(m)[:7]) for n in noms if len(_n(m)) >= 7)})
if inc: (crit if len(inc) > 5 else moy).append(f"spécialité(s) ® absente(s) de l'index AIPS (vaccin, générique renommé ou erreur) : {', '.join(inc[:8])}")
else: ok.append("toutes les spécialités ® citées existent dans l'index AIPS")
# 3. points §11 présents et substantiels
pts = {int(m.group(2)): m.start() for m in re.finditer(r"<h3[^>]*id=[\"']([\w-]+?)-p(\d{1,2})[\"']", raw)}
manq = [i for i in range(1, 15) if i not in pts]
if manq and not re.search(r"<h3", raw): moy.append("balises h3 des points absentes (contrôle de structure partiel)")
elif manq: crit.append(f"points §11 manquants : {manq}")
need = {"gold standard": r"gold standard|référence", "sensibilité/spécificité chiffrées": r"sensibilit\w+[^.]{0,80}\d|\d[^.]{0,40}sensibilit", "11.A–11.D (ou forme de la directive de Vial du 28.10.2026 : But, Moyens et méthodes, urgences, hors urgences, surveillance, pronostic)": r"11\.A.*11\.B.*11\.C.*11\.D|\bBut\b.*Moyens et méthodes.*urgences?.*Hors urgences?.*surveillance.*pronostic", "drapeaux/graves": r"🚩|drapeau", "grossesse/allaitement": r"grossesse", "situations spéciales (âge/rénal)": r"âgé|pédiatr|enfant|rénal|insuffisance"}
for k, rx in need.items():
    if not re.search(rx, txt, re.I | re.S): moy.append(f"contenu attendu absent : {k}")
if phaseA:
    for k, rx in {"rangs E1…": r"\bE1\b", "badge 🚩": r"🚩", "tableau comparatif": r"comparatif", "algorithme": r"algorithme"}.items():
        if not re.search(rx, txt, re.I): crit.append(f"Phase A : {k} absent")
av = len(re.findall(r"À vérifier", txt)); (moy if av <= 15 else crit).append(f"« À vérifier » restants : {av}") if av else ok.append("aucun « À vérifier »")
sc = round(max(0, 100 - 25 * len(crit) - 4 * len(moy)), 1); q = "oui" if sc >= 90 and not crit else "non"
r = f"RESULTAT score={sc} critiques={len(crit)} question={q}\n\n# Contrôle médical (script d'ancrage) — {f.name}\n\n## Vérifié\n" + "\n".join("- " + x for x in ok) + "\n\n## CORRECTIONS\n" + "\n".join("- CRITIQUE : " + x for x in crit) + "\n" + "\n".join("- moyen : " + x for x in moy) + "\n"
if rap: Path(rap).write_text(r, encoding="utf-8")
print(r.splitlines()[0])
