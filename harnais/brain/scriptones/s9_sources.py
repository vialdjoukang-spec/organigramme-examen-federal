#!/usr/bin/env python3
"""Scriptone S9 · liste des sources : Suisse d'abord, AIPS seule pour les doses, versions à jour (règles minimales de Vial, Prompt §4). Région AUM.
  I1 Compendium cité (doses : AIPS suisse sur swissmedicinfo.ch seulement, jamais le Compendium)
  I2 recommandation exclusivement américaine (ADA, AHA/ACC, IDSA, FDA, CDC, USPSTF) sans source suisse ou européenne dans la liste
  I3 version périmée connue (EACS 12, ERC 2015, ESC NSTE-ACS 2020, ESE 2014 citée pour l'hyponatrémie sans mention) : registre des versions
  I4 date de consultation absente d'une source          I5 source sans identifiant (PMID, DOI ou URL)
Lecture seule (executant = agent) : aucune source n'est inventée ni remplacée par script."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s9_sources", "AUM", "1.0.0"
US = re.compile(r"\b(?:ADA|AHA|ACC|IDSA|FDA|CDC|USPSTF|American (?:Diabetes|Heart|College)|Infectious Diseases Society of America)\b")
EU_CH = re.compile(r"(?i)\b(?:OFSP|OFS|Obsan|Swissmedic|swissmedicinfo|AIPS|SSMIG|SSED|SSGO|SSI|SSC|SGN|FMH|ASSM|Fedlex|Tox Info|ESC|ERS|ERC|EASL|ESMO|ESE|ESCMID|EACS|EULAR|EAACI|KDIGO|EMA|ECDC|Swiss|Suisse|Schweiz|europ|European|WHO|OMS)\b")
PERIMES = [(re.compile(r"(?i)\bEACS\b[^<]{0,40}\b12(?:\.\d)?\b"), "EACS 12 remplacée par EACS 13.0"),
           (re.compile(r"(?i)\bERC\b[^<]{0,40}\b2015\b"), "ERC 2015 remplacé par ERC 2021 (et 2025)"),
           (re.compile(r"(?i)\bESC\b[^<]{0,60}\bNSTE[^<]{0,40}\b2020\b|\b2020\b[^<]{0,40}\bESC\b[^<]{0,40}\bNSTE"), "ESC NSTE-ACS 2020 remplacée par ESC SCA 2023")]


def entrees(t):
    """Entrées de la liste des sources : <li> de la section Sources (brute ou convertie) et bandes .sb."""
    a, f = bus.bornes_cours(t)
    m = re.search(r'(?is)<details class="refs"[^>]*>.*?</details>|<h2[^>]*>\s*(?:<strong>)?\s*Sources.*?(?:</ol>|</ul>)', t[f:])
    zone, off = (m.group(0), f + m.start()) if m else ("", f)
    L = [(off + x.start(), x.group(1)) for x in re.finditer(r"(?is)<li\b[^>]*>(.*?)</li>", zone)]
    if not L: L = [(f + x.start(), x.group(1)) for x in re.finditer(r'(?is)<div class="sb"[^>]*>(.*?)</div>', t[f:])]
    return [(p, bus.texte(x)) for p, x in L if re.search(r"\w{4}", bus.texte(x))]


def analyser(t, nom, opt=None):
    me = sys.modules[__name__]; D = []; E = entrees(t); tout = " ".join(x for _, x in E)
    for p, x in E:
        if re.search(r"(?i)compendium", x):
            D.append(bus.doleance(me, "I1", nom, bus.ancre(t, p, x), "GRAVE", "Compendium cité : les doses se lisent dans l'AIPS suisse seulement",
                                  "remplacer par l'information professionnelle AIPS (swissmedicinfo.ch) réellement lue, puis relire la dose", "agent", x[:200]))
        for rx, msg in PERIMES:
            if rx.search(x):
                D.append(bus.doleance(me, "I3", nom, bus.ancre(t, p, x), "GRAVE", f"version périmée : {msg}",
                                      "citer la version la plus récente, lue, et vérifier que chaque affirmation tirée de l'ancienne reste vraie", "agent", x[:200]))
        if not re.search(r"(?i)consult|lu le|accès le|accessed", x):
            D.append(bus.doleance(me, "I4", nom, bus.ancre(t, p, x), "MOYEN", "source sans date de consultation", "ajouter « consulté le jj.mm.aaaa » (date réelle de lecture)", "agent", x[:160]))
        if not re.search(r"(?i)PMID|doi|https?://|www\.|\.ch\b|\.org\b|\.int\b", x):
            D.append(bus.doleance(me, "I5", nom, bus.ancre(t, p, x), "MOYEN", "source sans identifiant (PMID, DOI ou URL)", "ajouter l'identifiant réellement ouvert (PMID, DOI ou URL)", "agent", x[:160]))
    us = [x for _, x in E if US.search(x)]
    if us and not EU_CH.search(tout.replace(" ".join(us), "")):
        D.append(bus.doleance(me, "I2", nom, bus.ancre(t, E[0][0], us[0]), "GRAVE", "recommandation exclusivement américaine, sans source suisse ou européenne",
                              "citer d'abord la recommandation suisse, sinon européenne ; l'américaine ne sert jamais seule de référence", "agent", us[0][:160]))
    for m in re.finditer(r"(?i)compendium\.ch", t[slice(*bus.bornes_cours(t))]):
        D.append(bus.doleance(me, "I1", nom, bus.ancre(t, bus.bornes_cours(t)[0] + m.start(), "compendium.ch"), "GRAVE", "lien Compendium dans le texte du cours",
                              "remplacer par l'AIPS (swissmedicinfo.ch) lue", "agent")); break
    return D, dict(sources=len(E))


def _ajout(t, r, x):
    i = t.rfind("</ol>")
    if i < 0: i = t.rfind("</details>")
    return t[:i] + f"<li>[S{r.randint(30, 60)}] {x}</li>" + t[i:]
def _m_comp(t, r): return _ajout(t, r, f"Source fictive de test : Compendium, monographie {r.randint(1000, 9999)}, https://example.invalid/compendium, consulté le 27.10.2026.")
# Les entrées injectées sont des sources FICTIVES de test (domaine example.invalid) : aucune référence réelle n'est fabriquée.
def _m_perime(t, r): return _ajout(t, r, r.choice(["Source fictive de test : ERC Guidelines 2015. https://example.invalid/erc, consulté le 27.10.2026.",
                                                     "Source fictive de test : EACS Guidelines version 12.0. https://example.invalid/eacs, consulté le 27.10.2026."]))
def _m_date(t, r): return _ajout(t, r, "Source fictive de test : revue générale. https://example.invalid/revue.")
def _m_ident(t, r): return _ajout(t, r, "Source fictive de test : revue générale sans identifiant, consulté le 27.10.2026.")
def _m_us(t, r):
    a, f = bus.bornes_cours(t); t2 = t[:f] + re.sub(r"(?is)<li\b[^>]*>.*?</li>", "", t[f:])
    t2 = re.sub(r'(?is)<div class="sb"[^>]*>.*?</div>', "", t2)
    return _ajout(t2, r, "Source fictive de test : American Diabetes Association (ADA), standards. https://example.invalid/ada, consulté le 27.10.2026.")
MUTANTS = [("Compendium cité", _m_comp, "I1"), ("version périmée", _m_perime, "I3"), ("sans date", _m_date, "I4"), ("sans identifiant", _m_ident, "I5"),
           ("source américaine seule", _m_us, "I2")]
ECRIT = []

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
