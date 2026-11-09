#!/usr/bin/env python3
"""Une passe Gemma par rubrique. Aucune sortie n'est renvoyée au modèle."""
from __future__ import annotations
import json, os, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
PREUVES = ROOT / "preuves" / "preuves.jsonl"
PROMPT = (ROOT / "PROMPT_RUBRIQUE_UNE_PASSE.md").read_text(encoding="utf-8")
BRUT = REPO / "Gemma__LOTS_Pilote" / "LOT_131" / "brut"
DUREES = ROOT / "durees.csv"
MODELE = "gemma4:e4b-it-qat"
URL = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434/api/chat")

POINTS = {
    1: ("Définition et sémantique", 4000,
        "Définition selon la source nommée dans l'extrait, termes à éviter, distinction avec les notions voisines. Trois ou quatre phrases porteuses, puis des fenêtres qui développent le geste, le piège et la distinction, jusqu'au budget, sans chiffre nouveau."),
    2: ("Épidémiologie (Suisse, puis Europe)", 6000,
        "Prévalence ou incidence chiffrée uniquement si l'extrait la contient, d'abord la source suisse si elle est fournie, sinon l'européenne. Âge, sexe, histoire naturelle, enjeu de santé publique."),
    3: ("Physiopathologie", 9000,
        "Cascade de la cause au signe. Tableau : lésion, exploration qui la montre, thérapeutique qui la corrige. Aucun mécanisme chiffré hors extrait."),
    4: ("Démarche diagnostique", 6000,
        "D'abord les entités graves à exclure, puis les fréquentes. Pour chacune : le signe qui tranche, le piège, la conduite immédiate."),
    5: ("Anamnèse ciblée et drapeaux rouges", 6000,
        "Chaque question est justifiée par son effet sur la décision. Les drapeaux rouges disent l'action immédiate."),
    6: ("Examen physique ciblé, région par région", 7000,
        "Pour chaque région, le normal attendu puis le pathologique, avec le geste et le piège d'interprétation."),
    7: ("Approche syndromique", 8000,
        "Syndromes numérotés 7.1, 7.2. Chaque syndrome est séparé en signes fonctionnels et signes physiques, avec le geste et le mécanisme."),
    8: ("Diagnostic positif et critères", 6000,
        "Critères de la source citée, ce qui suffit et ce qui ne suffit pas."),
    9: ("Examens complémentaires", 11000,
        "9.a gold standard, 9.b première intention, 9.c alternatives, 9.d deuxième intention. Pour chacun : indication et tableau résultat, signification, conduite."),
    10: ("Arbre décisionnel", 5000,
        "Embranchements « si X, alors Y », en commençant par les situations graves."),
    11: ("Prise en charge", 16000,
        "11.A but, 11.B moyens avec l'urgence chronologique, 11.C surveillance, 11.D pronostic. Aucune dose en milligrammes sans extrait AIPS : écrire « posologie : À vérifier (AIPS) »."),
    12: ("Prévention", 5000,
        "Prévention primaire, secondaire et tertiaire, avec la recommandation suisse ou européenne présente dans les extraits."),
    13: ("Points clés", 2000,
        "Trois à six phrases verbales, mémorisables, chacune porteuse d'une décision. Aucune fenêtre au milieu d'une phrase."),
    14: ("Pièges et questions d'examen", 6000,
        "Chaque piège est une question, suivie de la réponse et d'une raison courte. Rien qui ne soit déjà soutenu par un extrait."),
}

NOMS = {
    "Phase_A": "Variations des organes génitaux externes (F1.2)",
    "DX.1": "Phimosis physiologique ou pathologique",
    "DX.2": "Varicocèle",
    "DX.3": "Cryptorchidie",
    "DX.4": "Hypospadias",
    "DX.5": "Mutilation génitale féminine",
    "DX.6": "Torsion du testicule",
    "DX.7": "Hyperplasie congénitale des surrénales du nouveau-né",
    "DX.8": "Carcinome épidermoïde du pénis",
    "DX.9": "Priapisme ischémique",
    "DX.10": "Gangrène de Fournier",
}

def charger():
    rows = [json.loads(l) for l in PREUVES.read_text(encoding="utf-8").splitlines() if l.strip()]
    return rows

def preuves_du(rows, entite, point):
    sel = [r for r in rows if entite in r["entites"] and point in r["points"]]
    if not sel:
        sel = [r for r in rows if entite in r["entites"]][:2]
    return sel[:4]

def bloc_preuves(sel):
    morceaux = []
    for r in sel:
        morceaux.append(f"- [{r['id']}] ({r['source']}, {r['pays']}, {r['annee']}) « {r['extrait']} »")
    return "\n".join(morceaux) if morceaux else "- Aucun extrait : n'écris aucun chiffre."

def bloc_securite(sel):
    secs = [r for r in sel if r.get("securite")]
    if not secs:
        return "Aucun identifiant de sécurité imposé pour les extraits de ce point. N'invente pas de contre-indication chiffrée."
    return "\n".join(f"- {r['id']} : conduite de sécurité à citer si ce point est le 5, le 6 ou le 11. Extrait : « {r['extrait'][:280]} »" for r in secs)

def squelette(entite, n, titre):
    prefix = "ssp" if entite == "Phase_A" else "dx" + entite.split(".")[1]
    return (
        f'<h3 id="{prefix}-p{n}"><strong>{n}. {titre}</strong></h3>\n'
        f'<div class="p">\n…\n</div>'
    )

def rendu(entite, n, sel):
    titre, octets, exigence = POINTS[n]
    prefix = "ssp" if entite == "Phase_A" else "dx" + entite.split(".")[1]
    corps = PROMPT
    remp = {
        "{N}": str(n),
        "{TITRE_POINT}": titre,
        "{ENTITE}": NOMS[entite],
        "{LOT}": "131",
        "{CODE_SSP}": "F1.2",
        "{CONTENU_EXIGE}": exigence,
        "{PASSAGES}": bloc_preuves(sel),
        "{SECURITE}": bloc_securite(sel),
        "{OCTETS_CIBLE}": str(octets),
        "{PREFIX}": prefix,
        "{SQUELETTE}": squelette(entite, n, titre),
    }
    for k, v in remp.items():
        corps = corps.replace(k, v)
    return corps, octets

def appel(prompt, n_predict):
    body = json.dumps({
        "model": MODELE,
        "messages": [
            {"role": "system", "content": "Tu suis le prompt utilisateur à la lettre. Tu ne fais qu'une seule passe."},
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "think": False,
        "keep_alive": "45m",
        "options": {"temperature": 0.2, "repeat_penalty": 1.1, "num_ctx": 8192, "num_predict": n_predict},
    }).encode()
    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=3600) as r:
        return json.load(r)

def journal(row):
    nouveau = not DUREES.exists()
    with DUREES.open("a", encoding="utf-8") as f:
        if nouveau:
            f.write("entite,point,secondes,eval_count,tok_s,octets,horodatage\n")
        f.write("{entite},{point},{secondes:.1f},{eval_count},{tok_s:.2f},{octets},{horodatage}\n".format(**row))

def rediger_un(rows, entite, n, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    fini = dest.with_suffix(".html")
    if fini.exists() and fini.stat().st_size > 0:
        print(f"SKIP {entite} p{n} déjà écrit")
        return
    sel = preuves_du(rows, entite, n)
    prompt, octets = rendu(entite, n, sel)
    n_predict = max(200, int(1.3 * octets / 3.3))
    (dest.parent / f"p{n:02d}.prompt.txt").write_text(prompt, encoding="utf-8")
    t0 = time.time()
    data = None
    erreur = None
    for essai in range(2):
        try:
            data = appel(prompt, n_predict)
            break
        except Exception as e:
            erreur = e
            time.sleep(5)
    if data is None:
        (dest.parent / f"p{n:02d}.erreur.txt").write_text(str(erreur), encoding="utf-8")
        print(f"ECHEC {entite} p{n}: {erreur}")
        return
    msg = data.get("message") or {}
    texte = (msg.get("content") or "").strip()
    pensee = msg.get("thinking") or ""
    if pensee:
        (dest.parent / f"p{n:02d}.pensee.txt").write_text(pensee, encoding="utf-8")
    fini.write_text(texte + "\n", encoding="utf-8")
    dt = time.time() - t0
    ev = data.get("eval_count") or 0
    ed = data.get("eval_duration") or 0
    tok_s = (ev / (ed / 1e9)) if ed else 0
    meta = {"entite": entite, "point": n, "secondes": round(dt, 1), "eval_count": ev,
            "tok_s": round(tok_s, 2), "octets": len(texte.encode()), "num_predict": n_predict,
            "done_reason": data.get("done_reason"), "modele": MODELE}
    (dest.parent / f"p{n:02d}.meta.json").write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")
    journal({"entite": entite, "point": n, "secondes": dt, "eval_count": ev, "tok_s": tok_s,
             "octets": len(texte.encode()), "horodatage": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    print(f"OK {entite} p{n} {len(texte.encode())} o {tok_s:.1f} tok/s {dt:.0f}s")

def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: rediger_gemma.py <entite> [--seulement N]")
    entite = sys.argv[1]
    seulement = None
    if "--seulement" in sys.argv:
        seulement = int(sys.argv[sys.argv.index("--seulement") + 1])
    if entite not in NOMS:
        raise SystemExit(f"entité inconnue {entite}")
    rows = charger()
    dest_dir = BRUT / entite
    points = [seulement] if seulement else list(range(1, 15))
    for n in points:
        rediger_un(rows, entite, n, dest_dir / f"p{n:02d}.html")

if __name__ == "__main__":
    main()
