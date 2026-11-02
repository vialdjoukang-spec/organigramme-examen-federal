#!/usr/bin/env python3
"""Gabarit du BRAIN-HARNESS : génère les 140 scriptones des synapses (α1…α14 × 5 familles, β1…β14 × 5 familles) à partir de
scriptones/synapses.json et de scriptones/familles.py, puis écrit le registre des 160 scriptones (registre.json) et les empreintes.
  python3 harnais/brain/outils/gabarit.py [--verifier]
Génération par gabarit, jamais à la main : un scriptone généré n'est pas édité ; on change la famille, les paramètres, puis on régénère.
--verifier : refuse (code 1) si un fichier généré diffère de ce que le gabarit produirait (dérive manuelle)."""
import importlib.util, json, re, sys
from pathlib import Path
B = Path(__file__).resolve().parents[1]; S = B / "scriptones"
sys.path.insert(0, str(S))
import bus, familles as F

MODELE = '''#!/usr/bin/env python3
"""{titre}
Généré par harnais/brain/outils/gabarit.py depuis synapses.json et familles.py : NE PAS ÉDITER À LA MAIN (régénérer).
Codes : {codes}
Entrée : paquet du point {n} (cours HTML) · sortie : contrat brain.scriptone/1 · écrit : {ecrit} · jumeau : {jumeau}."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import bus, familles as F

ID, REGION, VERSION, ZONE, POINT, FAMILLE = "{id}", "{region}", F.VERSION, "{zone}", {n}, "{f}"
DEPEND = ["familles.py", "synapses.json", "verbes.json"]
analyser = F.analyseur("{z}", FAMILLE, POINT)
corriger = F.correcteur("{z}", FAMILLE, POINT)
MUTANTS = F.mutants("{z}", FAMILLE, POINT)
ECRIT = F.zones("{z}", FAMILLE, POINT)

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
'''

# (id, fichier, région, signal, nom, fonction, entrée, sortie, doléances de Vial servies, jumeau)
TRANSVERSAUX = [
 ("s1_police", "s1_police.py", "AUF", "forme", "Police Atkinson Hyperlegible partout", "repère la police non embarquée, externe, cassée par un saut de ligne, concurrencée ; la réembarque (woff2 400 et 700)", "HTML converti (CSS réel)", "P1–P7 ; --appliquer : @font-face réparé + garde de police", [1], None),
 ("s2_rythme", "s2_rythme.py", "AUF", "forme", "Rythme vertical et interlignes", "interligne, blancs inutiles, paragraphes détachés, orphelines, colonne trop large ; pose la grille de rythme", "HTML converti", "L1–L6 ; --appliquer : blancs retirés + style de rythme", [2], None),
 ("s3_concision", "s3_concision.py", "AUL", "langue", "Concision extrême", "formules creuses, redites entre points, métadiscours, phrases juxtaposées sans connecteur", "cours HTML", "C1–C4 ; --appliquer : formules creuses retirées en tête de phrase", [3], None),
 ("s4_budget", "s4_budget.py", "AUL", "langue", "Budget de lignes par point", "épidémiologie en 3 à 4 lignes, chiffre sourcé dans sa phrase, dénominateur ; inventaire des chiffres à conserver", "cours HTML", "B1–B4 (agent, avec inventaire)", [4], "a02_Q"),
 ("s5_arbre", "s5_arbre.py", "AUF", "forme", "Arbre de classification déroulant", "parents cliquables qui déroulent leurs homologues explicités, notion surlignée parmi eux", "cours HTML (point 1)", "A1–A6 ; --appliquer : rendu details/summary natif", [6], "a01_S"),
 ("s6_barre14", "s6_barre14.py", "AUF", "forme", "Barre des 14 points fixe et cliquable", "barre fixe à l'écran, un lien par point vers son ancre, sources, titre jamais masqué", "cours HTML", "N1–N6 ; --appliquer : ancres, barre, style", [7], "s20_ancres"),
 ("s7_captures", "../../bilan/captures.js", "VIS", "forme", "Captures pleine longueur par chapitre, en rotation", "captures navigateur de toute la page, chapitre par chapitre, rotation entre passages ; police réellement chargée, orphelines, débordements", "fichiers HTML (navigateur Playwright)", "V1–V5 + captures.json", [1, 2, 9], None),
 ("s8_tableaux", "s8_tableaux.py", "AUF", "forme", "Tableaux à en-têtes explicites", "en-têtes génériques, portée des pourcentages, unités, légende ; règle de réécriture « mesure portée (unité) »", "cours HTML", "T1–T7 ; --appliquer : unité ajoutée à l'en-tête", [8], "a03_S"),
 ("s9_sources", "s9_sources.py", "AUM", "medical", "Sources : Suisse d'abord, AIPS pour les doses", "Compendium, source américaine seule, version périmée, date de consultation, identifiant", "liste des sources", "I1–I5 (agent)", [], "b02_S"),
 ("s10_memoire", "s10_memoire.py", "MEM", "memoire", "Mémoire tentaculaire des fautes corrigées", "empêche la récidive des fautes déjà jugées (P2Y12, anaphylaxie, C4, ESE, FDA, rangs, title=)", "cours HTML + memoire_fautes.json", "M1–M8 (agent, routées par tentacule)", [], None),
 ("s11_collecteur", "s11_collecteur.py", "ENT", "forme", "Harnais externe de collecte", "garde l'entrée (tronqué, encodage, équilibre) et découpe le cours en 14 paquets transmis de nœud en nœud", "fichier brut", "K1–K5 + paquets par point", [], None),
 ("s12_ordonnanceur", "s12_ordonnanceur.py", "BUS", "doleance", "Ordonnanceur anti-conflit", "un seul écrivain par zone (registre), confluence de tous les ordres, idempotence, écriture hors zone", "cours HTML + registre", "O1–O4", [], None),
 ("s13_disjoncteur", "s13_disjoncteur.py", "SEC", "doleance", "Disjoncteurs et ré-routage", "panne → disjoncteur ouvert → jumeau → escalade ; stagnation ; lenteur", "cours HTML + pannes injectées", "Z1–Z4", [], None),
 ("s14_journal", "s14_journal.py", "BUS", "memoire", "Journal de circulation", "intégrité du journal JSONL rejoué par la vue 3D (lignes tronquées, champs, types, rangs concurrents)", "journal JSONL", "J1–J4 ; --appliquer : quarantaine", [], None),
 ("s15_gardien", "s15_gardien.py", "SEC", "doleance", "Gardien d'intégrité", "empreintes SHA-256 des 160 scriptones et cohérence du registre", "SHA256SUMS + registre", "G1–G4", [], None),
 ("s16_economie", "s16_economie.py", "ECO", "jetons", "Économie de jetons par étage", "mesure relecture intégrale, paquets, doléances ; plafonds par nœud", "cours HTML (+ doléances)", "W1–W3 + mesures de jetons", [], None),
 ("s17_brief", "s17_brief.py", "ENT", "jetons", "Compilateur de brief", "ce que l'agent reçoit : règle absolue, interdits, doléances [agent] par point, plafond", "doléances → brief Markdown", "F1–F4 (contrôle du brief)", [3, 5], None),
 ("s18_vote", "s18_vote.py", "BUS", "doleance", "Nœud de vote α/β", "compare les verdicts α et β par point et route les désaccords vers les nœuds Sonnet ou Opus", "cours HTML", "X1–X2 + table de routage", [], None),
 ("s19_couverture", "s19_couverture.py", "MEM", "memoire", "Couverture des fautes récurrentes", "classe le cumul des corrections (262 rapports) et vérifie qu'un scriptone empêche chaque famille de récidiver", "cumul Markdown", "U1–U2 + table de couverture", [], None),
 ("s20_ancres", "s20_ancres.py", "AUF", "forme", "Ancres et liens internes", "liens morts, cibles ambiguës, liens non sûrs (barre, exposants, bandes)", "cours HTML", "Y1–Y3", [7], "s6_barre14"),
]


def mutants_de(m):
    return [[x[0], x[2]] for x in getattr(m, "MUTANTS", [])]


def charger(p):
    spec = importlib.util.spec_from_file_location("g_" + p.stem, p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def generer():
    sortie = {}
    for z, rep, fams, cle in (("A", "alpha", F.FAM_A, "familles_alpha"), ("B", "beta", F.FAM_B, "familles_beta")):
        (S / rep).mkdir(exist_ok=True)
        for n in range(1, 15):
            for f in fams:
                i = F.ident(z, f, n); jz = F.SYN["jumeaux"]["alpha" if z == "A" else "beta"][f]
                jum = F.ident("B" if z == "A" else "A", jz, n).ID
                titre = f"{'α' if z == 'A' else 'β'}{n}·{f} — {F.SYN[cle][f]['nom']} · point {n} « {F.P[n]['titre']} »"
                sortie[S / rep / f"{i.ID}.py"] = MODELE.format(titre=titre, codes=F.SYN[cle][f]["codes"], n=n, ecrit=", ".join(F.zones(z, f, n)) or "rien (lecteur)",
                                                               jumeau=jum, id=i.ID, region=i.REGION, zone=rep, f=f, z=z)
    return sortie


def registre():
    out = []
    for i, fic, reg, sig, nom, fonc, ent, sor, vial, jum in TRANSVERSAUX:
        p = (S / fic).resolve(); e = dict(id=i, fichier=fic, langage="js" if fic.endswith(".js") else "python", zone="transversal", synapse=None, point=None, famille=None,
                                           region=reg, signal=sig, nom=nom, fonction=fonc, entree=ent, sortie=sor, doleances_vial=vial, jumeau=jum, cout_jetons=0, etat="implémenté")
        if e["langage"] == "python":
            m = charger(p); e.update(ecrit=list(getattr(m, "ECRIT", [])), mutants=mutants_de(m), version=m.VERSION, dore=str(Path(getattr(m, "DORE", B / "dore/cours_dore.html")).relative_to(B)))
        else:
            e.update(ecrit=[], mutants=[["police cassée vue au navigateur", "V1"], ["rotation des chapitres", "V-"]], version="1.0.0", dore="dore/cours_dore.html")
        e["sha256"] = bus.sha(p.read_bytes()); e["test"] = "test_scriptones.py · test_synapses.py · mutation.py" if e["langage"] == "python" else "test_scriptones.Captures (navigateur)"
        out.append(e)
    for z, rep, fams, cle in (("A", "alpha", F.FAM_A, "familles_alpha"), ("B", "beta", F.FAM_B, "familles_beta")):
        for n in range(1, 15):
            for f in fams:
                i = F.ident(z, f, n); p = S / rep / f"{i.ID}.py"; jz = F.SYN["jumeaux"]["alpha" if z == "A" else "beta"][f]
                vial = [5] if f == "R" else [4] if (f == "Q" and n == 2) else [3] if f in ("H", "D") else []
                out.append(dict(id=i.ID, fichier=f"{rep}/{i.ID}.py", langage="python", zone=rep, synapse=f"{'α' if z == 'A' else 'β'}{n}", point=n, famille=f,
                                region=i.REGION, signal=F.signal(z, f), nom=f"{F.SYN[cle][f]['nom']} · point {n}", fonction=F.SYN[cle][f]["nom"],
                                entree=f"paquet du point {n} « {F.P[n]['court']} »", sortie=F.SYN[cle][f]["codes"], doleances_vial=vial,
                                jumeau=F.ident("B" if z == "A" else "A", jz, n).ID, cout_jetons=0, etat="généré", ecrit=F.zones(z, f, n),
                                mutants=[[x[0], x[2]] for x in F.mutants(z, f, n)], version=F.VERSION, dore="dore/cours_dore.html",
                                sha256=bus.sha(p.read_bytes()), test="test_synapses.py · mutation.py"))
    return dict(version=3, total=len(out), note="Catalogue des scriptones du BRAIN-HARNESS (généré par outils/gabarit.py). Coût en jetons : 0 pour tous (scripts) ; seuls les nœuds auditeurs consomment des jetons.",
                scriptones=out)


def main(a):
    gen = generer()
    if "--verifier" in a:
        der = [str(p.relative_to(B)) for p, x in gen.items() if not p.exists() or p.read_text(encoding="utf-8") != x]
        print("gabarit : conforme" if not der else f"DÉRIVE : {len(der)} fichier(s) : {der[:5]}"); return 1 if der else 0
    for p, x in gen.items():
        if not p.exists() or p.read_text(encoding="utf-8") != x: p.write_text(x, encoding="utf-8")
    for p in list((S / "alpha").glob("*.py")) + list((S / "beta").glob("*.py")):
        if p not in gen: p.unlink()
    R = registre()
    (S / "registre.json").write_text(json.dumps(R, ensure_ascii=False, indent=1), encoding="utf-8")
    noms = bus.ecrire_empreintes()
    z = {}
    for e in R["scriptones"]: z[e["zone"]] = z.get(e["zone"], 0) + 1
    print(f"gabarit : {len(gen)} scriptones générés · registre {R['total']} scriptones {z} · {len(noms)} empreintes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
