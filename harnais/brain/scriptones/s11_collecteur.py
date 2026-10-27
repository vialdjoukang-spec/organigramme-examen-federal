#!/usr/bin/env python3
"""Scriptone S11 · harnais externe de collecte (étape 0 du circuit, gratuit). Région ENT.
Garde l'entrée : refuse ce qui est tronqué, mal encodé ou déséquilibré AVANT que le moindre agent ne lise ; puis découpe le cours en
14 paquets (un par point) transmis de nœud en nœud : chaque synapse αn, βn et chaque auditeur ne reçoit que SON paquet (économie de jetons).
  K1 fichier tronqué (balise FIN_FICHIER ou </html> absente)   K2 balises déséquilibrées (p, li, ul, ol, table, tr, details, section, div)
  K3 encodage abîmé (caractère de remplacement U+FFFD, mojibake « Ã© »)   K4 aucun point du plan (fichier vide ou hors gabarit)
  K5 octets nuls ou caractères de contrôle
Mesures : paquets {n: {titre, octets, mots, sha256, jetons}} ; c'est la sortie que l'orchestrateur transmet."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s11_collecteur", "ENT", "1.0.0"
BAL = ("p", "li", "ul", "ol", "table", "tr", "details", "section", "main", "summary")


def paquets(t):
    out = {}
    for n, (a, f) in sorted(bus.sections(t).items()):
        seg = bus.masque(t[a:f], bus.RX_STYLE); txt = bus.texte(seg)
        out[n] = dict(titre=bus.texte(re.match(r"(?is)<h3\b.*?</h3>", t[a:f]).group(0)) if re.match(r"(?is)<h3\b.*?</h3>", t[a:f]) else str(n),
                      octets=f - a, mots=len(txt.split()), sha256=bus.sha(t[a:f])[:16], jetons=bus.estime_jetons(txt))
    return out


def analyser(t, nom, opt=None):
    me = sys.modules[__name__]; D = []; M = {}
    if not re.search(r"FIN_FICHIER|</html>\s*$", t.rstrip()[-400:] if t else ""):
        D.append(bus.doleance(me, "K1", nom, f"#haut · l.{bus.ligne(t, len(t))}", "CRITIQUE", "fichier tronqué : ni balise FIN_FICHIER ni </html> en fin de fichier",
                              "régénérer ou reprendre le fichier depuis sa dernière version complète ; aucun agent ne lit un fichier tronqué", "agent", t[-120:]))
    corps = bus.masque(t, bus.RX_STYLE); dese = []
    for b in BAL:
        o = len(re.findall(r"(?i)<%s\b" % b, corps)); c = len(re.findall(r"(?i)</%s>" % b, corps))
        if b == "p": o -= len(re.findall(r"(?i)<p\b[^>]*/>", corps))
        if o != c: dese.append(f"{b} {o}/{c}")
    if dese:
        D.append(bus.doleance(me, "K2", nom, "#haut · l.1", "GRAVE", f"balises déséquilibrées : {', '.join(dese[:5])}",
                              "fermer chaque balise ouverte (contrôle_lot vérifie l'équilibre) ; un fichier déséquilibré se lit mal et se convertit mal", "agent", ", ".join(dese)))
    abime = t.count("�") + len(re.findall(r"Ã[©¨ª«®´¢§¹¼]|â€[™œ\x9d“”˜]", t))
    if abime:
        i = min([x for x in (t.find("�"), (re.search(r"Ã[©¨ª«®´¢§¹¼]|â€", t) or re.search("$", t)).start()) if x >= 0] or [0])
        D.append(bus.doleance(me, "K3", nom, bus.ancre(t, i, t[i:i + 30]), "GRAVE", f"encodage abîmé : {abime} caractère(s) illisible(s)",
                              "relire le fichier en UTF-8 depuis la source et réécrire les mots abîmés (aucune notion ne doit disparaître)", "agent", t[max(0, i - 20):i + 30]))
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", t):
        D.append(bus.doleance(me, "K5", nom, "#haut · l.1", "GRAVE", "octets nuls ou caractères de contrôle dans le fichier", "retirer les caractères de contrôle (fichier binaire ou mal copié)", "agent"))
    P = paquets(t); M.update(points=len(P), paquets=P, octets=len(t.encode("utf-8", "surrogatepass")))
    if not P:
        D.append(bus.doleance(me, "K4", nom, "#haut · l.1", "CRITIQUE", "aucun point du plan (aucun <h3> « N. … ») : fichier vide ou hors gabarit",
                              "rédiger le cours selon la GRILLE À 14 POINTS", "agent"))
    return D, M


def _m_tronque(t, r): k = int(len(t) * r.uniform(0.3, 0.95)); return t[:k]
def _m_desequilibre(t, r): return re.sub(r"</table>", "", t, count=1) if "</table>" in t else t.replace("</p>", "", 1)
def _m_encodage(t, r):
    i = t.index("<h3"); i = t.index("</h3>", i) + 5; mot = r.choice(["Ã©", "Ã¨", "â€™", "�"])
    return t[:i] + f"<p>La fi{mot}vre persiste.</p>" + t[i:]
def _m_vide(t, r): return re.sub(r"(?is)<h3\b.*?</h3>", "", t)
def _m_controle(t, r): i = r.randrange(len(t) // 3, len(t) // 2); i = t.index("</p>", i); return t[:i] + "\x00\x07" + t[i:]
MUTANTS = [("fichier tronqué", _m_tronque, "K1"), ("balises déséquilibrées", _m_desequilibre, "K2"), ("encodage abîmé", _m_encodage, "K3"),
           ("aucun point", _m_vide, "K4"), ("caractères de contrôle", _m_controle, "K5")]
ECRIT = []

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
