#!/usr/bin/env python3
"""Auditeur-script (gratuit, déterministe) : contrôles du Prompt V0 qui n'exigent aucun jugement clinique.
  python3 harnais/auditeur_script.py <fichier.html> [--liens]   → rapport court + .cache/.../audits/SCRIPT_<fichier>.md
Contrôles : n° Swissmedic cités ∈ corpus AIPS · PMID existants (PubMed) · DOI existants (Crossref) · liens (HTTP, avec --liens)
· « À vérifier » restants · pourcentages sans source à proximité · bande Ko / FIN_FICHIER / title= (controle_lot).
Ne remplace PAS l'audit médical (jugement, exhaustivité, pertinence) : il l'allège et le précède."""
import concurrent.futures as cf, hashlib, json, re, subprocess, sys, urllib.request
from pathlib import Path
R = Path(__file__).resolve().parent.parent; CA = R / ".cache/script_audit"; CA.mkdir(parents=True, exist_ok=True)
f = Path(sys.argv[1]); t = f.read_text(encoding="utf-8", errors="replace"); txt = re.sub(r"<[^>]+>", " ", t); rep = []
def get(u, m="GET"):
    k = CA / hashlib.sha256((m + u).encode()).hexdigest()[:24]
    if k.exists(): return int(k.read_text())
    try: c = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}, method=m), timeout=20).status
    except urllib.error.HTTPError as e: c = e.code
    except Exception: c = 0
    k.write_text(str(c)); return c
ids = set(re.findall(r"<Identifier>(\d+)</Identifier>", open(R / ".cache/aips/AipsDownload_20261008.xml", encoding="utf-8-sig").read()))
sm = set(re.findall(r"(?:Swissmedic|AIPS|autorisation|Zul\.?-?Nr\.?)\D{0,40}?\b(\d{5})\b", txt)); bad = sorted(n for n in sm if n not in ids)
rep.append(("Swissmedic cités ∈ corpus AIPS", f"{len(sm)-len(bad)}/{len(sm)}", "OK" if not bad else "ÉCART " + ",".join(bad)))
pm = sorted(set(re.findall(r"PMID\D{0,3}(\d{6,9})", txt))); ko = []
if pm:
    d = json.load(urllib.request.urlopen(urllib.request.Request("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(pm), headers={"User-Agent": "Mozilla/5.0"}), timeout=30))["result"]
    ko = [p for p in pm if p not in d or "error" in d.get(p, {})]
rep.append(("PMID existants (PubMed)", f"{len(pm)-len(ko)}/{len(pm)}", "OK" if not ko else "INTROUVABLES " + ",".join(ko)))
dois = sorted(set(x.rstrip(".,;)") for x in re.findall(r"\b(10\.\d{4,9}/[^\s<>\"']+)", t))); 
with cf.ThreadPoolExecutor(8) as ex: kd = [d for d, c in zip(dois, ex.map(lambda x: get("https://api.crossref.org/works/" + x), dois)) if c == 404]
rep.append(("DOI existants (Crossref)", f"{len(dois)-len(kd)}/{len(dois)}", "OK" if not kd else "INTROUVABLES " + ",".join(kd[:5])))
if "--liens" in sys.argv:
    us = sorted(set(re.findall(r"href=[\"'](https?://[^\"']+)", t)))
    with cf.ThreadPoolExecutor(12) as ex: st = dict(zip(us, ex.map(lambda u: get(u), us)))
    mort = [u for u, c in st.items() if c in (0, 404, 410)]; rep.append(("Liens (HTTP)", f"{len(us)-len(mort)}/{len(us)} répondent", "OK" if not mort else "MORTS " + " ; ".join(m[:70] for m in mort[:5])))
av = len(re.findall(r"À vérifier", txt)); rep.append(("« À vérifier » restants", str(av), "OK" if av == 0 else "À TRAITER"))
pc = [m for m in re.finditer(r"\d+(?:[.,]\d+)? ?%", txt)]; sans = sum(1 for m in pc if not re.search(r"\[S\d+\]|PMID|doi|10\.\d{4}|OFS|OFSP|Obsan|source", txt[max(0, m.start() - 250):m.end() + 250], re.I))
rep.append(("Pourcentages sans source à ≤250 car.", f"{sans}/{len(pc)}", "OK" if sans <= max(2, len(pc) // 10) else "TROP"))
c = subprocess.run([sys.executable, str(R / "harnais/controle_lot.py"), "verifier", "--sans-nom", str(f.parent)], capture_output=True, text=True).stdout.strip().splitlines()
rep.append(("controle_lot (forme, bande, FIN_FICHIER)", c[0][:60] if c else "?", "OK" if c and "CONFORME" in c[0] and "NON" not in c[0] else "VOIR controle_lot"))
out = f"# Auditeur-script — {f.name}\n\n| Contrôle | Résultat | Verdict |\n|---|---|---|\n" + "\n".join(f"| {a} | {b} | {v} |" for a, b, v in rep) + "\n"
(f.parent / "audits").mkdir(exist_ok=True); (f.parent / "audits" / f"SCRIPT_{f.name}.md").write_text(out, encoding="utf-8"); print(out)
