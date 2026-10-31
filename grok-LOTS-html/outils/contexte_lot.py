#!/usr/bin/env python3
"""CONTEXTE DE LOT — paquet de contexte partagé et stable (zéro jeton, Python standard).

Objectif : lire les sources communes UNE fois par LOT, les ranger dans un paquet ordonné du plus stable au plus volatil
(préfixe identique d'une passe à l'autre : le cache de préfixe du fournisseur, s'il existe, peut s'en servir), et donner
à chaque poste un fichier unique « <poste>.md » à lire au lieu de 8 à 10 fichiers entiers (dont MODELE_DD_V8.html, 254 Ko).

  python3 grok-LOTS-html/outils/contexte_lot.py construire LOT_134 [--poste redacteur|redacteur-phase-a|auditeur-medical|auditeur-conformite|transversale|tous]
                                                  [--sortie DOSSIER] [--racine DEPOT]
  python3 grok-LOTS-html/outils/contexte_lot.py empreinte  LOT_134 [--racine DEPOT]      tailles, économie par rapport à la lecture intégrale
  python3 grok-LOTS-html/outils/contexte_lot.py squelette [--racine DEPOT]                squelette du modèle MODELE_DD_V8.html sur la sortie standard

Lecture seule sur le dépôt. Écriture seulement dans --sortie (défaut : grok-LOTS-html/_cache/contexte/, non commité).
Ne remplace ni ne modifie aucun fichier du harnais. Le squelette du modèle est un RÉSUMÉ : l'original reste la référence,
et le rédacteur peut toujours le lire en entier (« python3 contexte_lot.py squelette » ne le supprime pas).
"""
from __future__ import annotations
import argparse, csv, hashlib, html, json, re, subprocess, sys
from html.parser import HTMLParser
from pathlib import Path

POSTES = ("redacteur-phase-a", "redacteur", "auditeur-medical", "auditeur-conformite", "transversale")
ROLE_FICHIER = {"redacteur-phase-a": "redacteur-phase-a.md", "redacteur": "redacteur.md",
                "auditeur-medical": "auditeur-medical.md", "auditeur-conformite": "auditeur-conformite.md",
                "transversale": "auditeur-medical.md"}
BRIEF_FICHIER = {"auditeur-medical": "harnais/briefs/AUDIT_MEDICAL.md", "transversale": "harnais/briefs/AUDIT_MEDICAL.md",
                 "auditeur-conformite": "harnais/briefs/CONFORMITE.md"}


def racine_depot(arg: str | None) -> Path:
    if arg:
        return Path(arg).resolve()
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, cwd=Path(__file__).resolve().parent)
        if out.returncode == 0 and out.stdout.strip():
            return Path(out.stdout.strip())
    except Exception:
        pass
    return Path(__file__).resolve().parents[2]


def lire(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""


def sha(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def sections(md: str, numeros: list[str]) -> str:
    """Extrait d'un Markdown les sections '## <n>.' demandées (numéros) ; texte brut sinon vide."""
    lignes, sortie, garde = md.splitlines(), [], False
    for l in lignes:
        m = re.match(r"^##\s+(\d+)\.", l)
        if m:
            garde = m.group(1) in numeros
        elif l.startswith("## ") and not m:
            garde = any(l.startswith(f"## {n}") for n in numeros)
        if garde:
            sortie.append(l)
    return "\n".join(sortie)


class Squelette(HTMLParser):
    """Résume un HTML : balises conservées, texte tronqué, répétitions repliées (popover, li, tr)."""
    REPLIABLES = {"li": 2, "tr": 3, "dd": 2, "details": 4}

    def __init__(self, tronque=60, popovers=3):
        super().__init__(convert_charrefs=True)
        self.o, self.tronque, self.max_pop, self.n_pop = [], tronque, popovers, 0
        self.pile, self.saut = [], 0
        self.rep = {}  # (parent_id) -> compteur par balise

    def _depth_skip(self):
        return self.saut > 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("style", "script"):
            self.pile.append(tag); self.o.append(f"<{tag}>/* contenu omis : copier style_lecon.css tel quel */</{tag}>") if tag == "style" else None
            self.saut += 1; return
        if self.saut:
            self.saut += 1; self.pile.append(tag); return
        if "popover" in a:
            self.n_pop += 1
            if self.n_pop > self.max_pop:
                self.o.append("<!-- … fenêtre popover du même type omise -->")
                self.saut = 1; self.pile.append(tag); return
        cle = (len(self.pile), tag)
        if tag in self.REPLIABLES:
            self.rep[cle] = self.rep.get(cle, 0) + 1
            if self.rep[cle] > self.REPLIABLES[tag]:
                if self.rep[cle] == self.REPLIABLES[tag] + 1:
                    self.o.append(f"<!-- … {tag} suivants du même type omis -->")
                self.saut = 1; self.pile.append(tag); return
        garde = " ".join(f'{k}="{html.escape(v or "", quote=True)[:40]}"' for k, v in attrs if k in ("id", "class", "popover", "popovertarget", "popovertargetaction", "lang", "name", "href", "data-sub"))
        self.o.append(f"<{tag}{(' ' + garde) if garde else ''}>")
        self.pile.append(tag)

    def handle_endtag(self, tag):
        if self.pile:
            self.pile.pop()
        if self.saut:
            self.saut -= 1
            if tag in ("style", "script") and not self.saut:
                pass
            return
        self.o.append(f"</{tag}>")

    def handle_data(self, d):
        if self.saut:
            return
        t = re.sub(r"\s+", " ", d).strip()
        if t:
            self.o.append(t if len(t) <= self.tronque else t[: self.tronque] + "…")

    def handle_comment(self, d):
        if not self.saut and "FIN_FICHIER" in d:
            self.o.append(f"<!--{d}-->")


def squelette_modele(texte: str) -> str:
    p = Squelette()
    p.feed(texte)
    s = "\n".join(p.o)
    return re.sub(r"\n{2,}", "\n", s)


def ligne_catalogue(racine: Path, lot: str) -> str:
    f = racine / "LOT_Claude_Finaux/CATALOGUE_248.csv"
    if not f.exists():
        return ""
    num = str(int(lot.split("_")[1]))
    with f.open(encoding="utf-8", errors="replace", newline="") as h:
        for r in csv.reader(h):
            if r and any(c.strip() in (num, lot) or c.strip().lstrip("0") == num for c in r[:2]):
                return " | ".join(r)
    return ""


def dernier(racine: Path, motif: str) -> Path | None:
    c = sorted(racine.glob(motif))
    return c[-1] if c else None


def composants(racine: Path, lot: str, poste: str) -> list[tuple[str, str, str]]:
    """[(niveau, nom, texte)] du plus stable au plus volatil."""
    g = racine / "grok-LOTS-html"
    v2, pg = lire(racine / "PROMPT_PRODUCTION_V2.md"), lire(g / "PROMPT_GROK.md")
    comp: list[tuple[str, str, str]] = []
    # N1 : stable pour tous les LOTS et tous les postes
    comp.append(("N1-regles", "PROMPT_PRODUCTION_V2 §2 règles de fond, §4 chaîne, §12 norme V8, article 4",
                 sections(v2, ["2", "4", "12"]) + "\n" + "\n".join(l for l in v2.splitlines() if l.startswith("## Article 4"))))
    comp.append(("N1-regles", "PROMPT_GROK §3 lois, §6 production, §8 norme", sections(pg, ["3", "6", "8"])))
    for nom in ("PIEGES.md", "PROMPTS_QUI_MARCHENT.md"):
        t = lire(g / "connaissance" / nom)
        if t:
            comp.append(("N1-regles", f"connaissance/{nom}", t))
    # N2 : stable par poste
    role = racine / ".claude/agents" / ROLE_FICHIER[poste]
    comp.append(("N2-poste", f".claude/agents/{role.name}", lire(role)))
    if poste in BRIEF_FICHIER:
        comp.append(("N2-poste", BRIEF_FICHIER[poste], lire(racine / BRIEF_FICHIER[poste])))
    else:
        b = dernier(racine, "lot en cours de production/LOT_0*/BRIEF_PHASE_B.md")
        if b:
            comp.append(("N2-poste", str(b.relative_to(racine)), lire(b)))
    l = dernier(racine, "lot en cours de production/LOT_0*/LECONS_LOT_*.md")
    if l:
        comp.append(("N2-poste", str(l.relative_to(racine)), lire(l)))
    if poste in ("redacteur", "redacteur-phase-a"):
        m = lire(racine / "harnais/modele_lecon/MODELE_DD_V8.html")
        comp.append(("N2-poste", "squelette de harnais/modele_lecon/MODELE_DD_V8.html (résumé ; original = référence)", squelette_modele(m)))
    # N3 : propre au LOT
    d = g / lot
    noms = ("LISTE_DX_CANONIQUE.md",) if poste == "auditeur-conformite" else ("LISTE_DX_CANONIQUE.md", "CORRECTIONS_AUDIT.md")
    for nom in noms:
        t = lire(d / nom)
        if t:
            comp.append(("N3-lot", f"{lot}/{nom}", t))
    cat = ligne_catalogue(racine, lot)
    if cat:
        comp.append(("N3-lot", "CATALOGUE_248.csv (ligne du LOT)", cat))
    return comp


def lecture_integrale(racine: Path, lot: str, poste: str) -> int:
    """Octets qu'un agent naïf lirait en entier : prompts complets, rôle, brief, leçons, MODÈLE complet, CSS."""
    g = racine / "grok-LOTS-html"
    fich = [racine / "PROMPT_PRODUCTION_V2.md", g / "PROMPT_GROK.md", racine / "harnais/HARNAIS_OBLIGATOIRE.md",
            racine / "harnais/ROUTAGE_MODELES.md", racine / ".claude/agents" / ROLE_FICHIER[poste],
            racine / "harnais/modele_lecon/MODELE_DD_V8.html", racine / "harnais/modele_lecon/style_lecon.css",
            g / lot / "LISTE_DX_CANONIQUE.md", g / lot / "CORRECTIONS_AUDIT.md"]
    if poste in BRIEF_FICHIER:
        fich.append(racine / BRIEF_FICHIER[poste])
    l = dernier(racine, "lot en cours de production/LOT_0*/LECONS_LOT_*.md")
    if l:
        fich.append(l)
    return sum(p.stat().st_size for p in fich if p.exists())


def construire(racine: Path, lot: str, poste: str, sortie: Path) -> dict:
    comp = composants(racine, lot, poste)
    corps, meta, prefixe = [], [], hashlib.sha256()
    for niveau, nom, texte in comp:
        bloc = f"\n\n<!-- ===== {niveau} · {nom} ===== -->\n{texte.strip()}\n"
        corps.append(bloc)
        meta.append({"niveau": niveau, "nom": nom, "octets": len(texte.encode("utf-8")), "sha256": sha(texte)})
        if niveau != "N3-lot":
            prefixe.update(bloc.encode("utf-8"))
    entete = f"<!-- PAQUET DE CONTEXTE {lot} · poste {poste} · lecture seule · construit par outils/contexte_lot.py -->"
    contenu = entete + "".join(corps)
    sortie.mkdir(parents=True, exist_ok=True)
    (sortie / f"{poste}.md").write_text(contenu, encoding="utf-8")
    taille = len(contenu.encode("utf-8"))
    naif = lecture_integrale(racine, lot, poste)
    stable = sum(m["octets"] for m in meta if not m["niveau"].startswith("N3"))
    info = {"lot": lot, "poste": poste, "fichier": str(sortie / f"{poste}.md"), "octets_paquet": taille,
            "octets_lecture_integrale": naif, "reduction_pct": round(100 * (1 - taille / naif), 1) if naif else None,
            "octets_prefixe_stable": stable, "prefixe_sha256": prefixe.hexdigest(), "composants": meta}
    (sortie / f"PACK_{poste}.json").write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding="utf-8")
    return info


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=("construire", "empreinte", "squelette"))
    ap.add_argument("lot", nargs="?")
    ap.add_argument("--poste", default="tous")
    ap.add_argument("--sortie")
    ap.add_argument("--racine")
    a = ap.parse_args(argv)
    r = racine_depot(a.racine)
    if a.cmd == "squelette":
        print(squelette_modele(lire(r / "harnais/modele_lecon/MODELE_DD_V8.html")))
        return 0
    if not a.lot or not re.fullmatch(r"LOT_\d{3}", a.lot):
        print("LOT attendu au format LOT_XXX"); return 2
    postes = POSTES if a.poste == "tous" else (a.poste,)
    if any(p not in POSTES for p in postes):
        print("poste inconnu :", a.poste); return 2
    sortie = Path(a.sortie) if a.sortie else r / "grok-LOTS-html/_cache/contexte" / a.lot
    if a.cmd == "empreinte":
        sortie = Path("/tmp") / f"contexte_{a.lot}_{abs(hash(str(r))) % 10**6}"
    for p in postes:
        i = construire(r, a.lot, p, sortie)
        print(f"{p:20s} paquet {i['octets_paquet']:>8d} o · lecture intégrale {i['octets_lecture_integrale']:>8d} o · "
              f"réduction {i['reduction_pct']} % · préfixe stable {i['octets_prefixe_stable']} o")
    return 0


if __name__ == "__main__":
    sys.exit(main())
