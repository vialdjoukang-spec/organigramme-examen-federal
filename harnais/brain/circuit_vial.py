#!/usr/bin/env python3
"""Circuit duo → professeur (directive de Vial du 28.10.2026, harnais/etat/DIRECTIVE_VIAL_REFONTE.md). Gratuit, hors ligne.
  python3 harnais/brain/circuit_vial.py memoire <duo|professeur> <fichier> [--garder]  départ obligatoire : directive, gabarits, grille, Prompt ULTIME (professeur),
                                                                               instantané d'entrée (--garder : reprise, instantané conservé)
  python3 harnais/brain/circuit_vial.py scanner <fichier> [--points 7,10,11]  professeur : par point, rappel de la grille + doléances GRAVES/CRITIQUES + texte visible
  python3 harnais/brain/circuit_vial.py algo <fichier> [--appliquer]          rend l'algorithme du point 10 (modèle JSON → cases et traits orthogonaux) + CSS
  python3 harnais/brain/circuit_vial.py point <fichier> N                     contrôle d'UN point après sa rédaction (balises, lignes, forme S21, phrases sans verbe)
  python3 harnais/brain/circuit_vial.py retirer <fichier> "<chiffre>" "<motif>" retrait déclaré d'un chiffre faux ou introuvable (consigné, relu par Vial)
  python3 harnais/brain/circuit_vial.py reparer <fichier>                     réparations mécaniques sûres : algorithme rendu, balises de bloc, lignes > 10 000
  python3 harnais/brain/circuit_vial.py mesurer <fichier> [--json]            relevé chiffré (octets, lignes longues, balises, doléances, scores langue et médical)
  python3 harnais/brain/circuit_vial.py fin <fichier> [--role duo|professeur] PORTE UNIQUE : répare d'abord (reparer), puis refuse si rien n'a changé (R15), si une
                                                                               GRAVE de forme (S21 : D/E/Q/L/H), une GRAVE de source (BS : chiffre
                                                                               ou dose sans renvoi) ou une CRITIQUE reste, si un chiffre sourcé ou un appel
                                                                               de source a disparu, si controle_lot relève une critique, ou si la langue ou le
                                                                               médical d'audit_lot est < 90 ou critique (même verdict que la porte de sortie du lot)
  python3 harnais/brain/circuit_vial.py repartir <dossier|fichiers…> [--phase-b|--phase-a] [--liste f.txt] [--exclure-traites] [--json]
                                                                               vague : 16 leçons → 16 duos Sonnet → 12 professeurs Opus (1 leçon chacun, 4 au tourniquet)
  python3 harnais/brain/circuit_vial.py sortie <dossier> [--json]             porte de fin de vague = audit_sortie (hook pre-commit) ; rapports périmés écartés ;
                                                                               liste des non conformes et de leurs motifs (à renvoyer au duo)
  python3 harnais/brain/circuit_vial.py reprise <fichier>                     départ d'un duo renvoyé par la sortie : instantané + motifs + rapports MED_/CONF_
Ne lit jamais un fichier de cours entier dans le contexte de l'agent : le scanner rend le texte visible point par point."""
import hashlib, json, re, subprocess, sys
from pathlib import Path
D = Path(__file__).resolve().parent; R = D.parents[1]
sys.path[:0] = [str(D / "scriptones"), str(D)]
import bus
import s21_forme_vial as S21

CACHE = R / ".cache/brain/circuit"
SEUIL = 90                                    # audit_lot / audit_sortie : langue et médical ≥ 90, 0 critique
OPUS, LECONS_PAR_OPUS, VAGUE = 12, 1, 16      # directive de Vial : 12 professeurs, une leçon par appel
GABARITS = r"""## Gabarits HTML (le script vérifie exactement ces formes)
- Terme survolable (précision simple) : <span class="tm" tabindex="0">terme<span class="df">précision en une phrase</span></span>
- Terme cliquable à fenêtre (explication complexe) : <span class="dx"><input type="checkbox" id="pN-x"><label class="dxt" for="pN-x">terme</label><span class="dxc">explication</span></span>
  (identifiant unique dans tout le fichier : préfixe du point, ex. p7-godet ; un doublon = doléance R1)
- Point 7, chaque syndrome :
  <p><b>7.1 Syndrome de …</b></p>
  <ul><li><b>Symptômes fonctionnels :</b> x, y, z (termes survolables)</li>
      <li><b>Signes physiques :</b> région / région :
        <span class="sc dx"><input type="checkbox" id="p7-1-godet"><label class="dxt" for="p7-1-godet">Signe du godet</label>
        <span class="dxc"><b>Recherche :</b> La patiente est placée en décubitus dorsal ; l'examinateur presse … pendant … secondes. <b>Valeur :</b> Un godet persistant établit …</span></span> …</li></ul>
  Toute fenêtre (.df, .dxc, détail d'une case d'algorithme) est rédigée en PHRASES COMPLÈTES (sujet, verbe, complément) : le contrôle de langue les lit.
  Une fiche de médicament s'écrit ainsi : « L'Oestrogel® (estradiol) appartient aux œstrogènes seuls (ATC G03CA03). L'AIPS fixe la dose à … »
  Dans un tableau, la cellule « Signes physiques » contient ces mêmes sous-cellules span.sc.dx.
- Point 10, algorithme en cases : écrire le modèle, puis lancer `algo <fichier> --appliquer` (le script dessine rectangles, losanges et traits
  strictement horizontaux et verticaux ; aucun cercle, aucun oblique) :
  <template class="algo-modele">{"titre":"Devant …","noeuds":[
    {"id":"q1","type":"losange","texte":"Drapeau rouge ?","detail":"liste et conduite (HTML court permis)"},
    {"id":"u","type":"case","texte":"Urgence : …","detail":"…"},{"id":"f1","type":"fin","texte":"Diagnostic : …","detail":"…"}],
   "liens":[{"de":"q1","a":"u","etiquette":"Oui"},{"de":"q1","a":"f1","etiquette":"Non"}]}</template>
  Types : case (action), losange (question fermée), fin (conclusion). Texte de case ≤ 60 caractères ; le détail va dans « detail » (fenêtre cliquable).
- Point 11 (titre déjà stylé par la CSS brain-vial : gras, bande colorée, souligné) :
  <p><b>1- But :</b> une phrase claire.</p>
  <p><b>2- Moyens et méthodes :</b></p>
  <p><b>A- En urgences :</b> algorithme d'urgence bref.</p>
  <ul><li><b>Aux urgences par le non-spécialiste</b> (interne senior des urgences, etc.) : premiers temps avant TRANSFERT vers le service spécialisé : …</li>
      <li><b>Dans le service spécialisé :</b> actes et gestes en ordre chronologique, chacun cliquable (span.dx avec fenêtre de détails).</li></ul>
  (SSP sans urgence propre : « A- Sans objet : aucune urgence propre à ce SSP. »)
  <p><b>B- Hors urgences :</b></p>
  <ul><li><b>Mesures générales :</b> …</li><li><b>Mesures spécifiques</b>, par priorité décroissante : pharmacologiques (médicament cliquable, dose AIPS), puis non pharmacologiques (social, professionnel, ergothérapie…).</li></ul>
  Les sous-parties existantes (surveillance, pronostic, situations spéciales) restent après B."""
REGLES = """## Règles absolues
- Rien n'est retranché : notions, chiffres sourcés, références et fenêtres existantes sont conservés (reformuler plus dense, déplacer en puces ou en fenêtre).
- Phrases complètes (sujet, verbe, complément), concises, style universitaire soutenu, termes dédiés ; énumérations en puces, y compris dans les cellules :
  une cellule (hors 1re colonne) contient soit des puces <ul><li>, soit des phrases à verbe conjugué (contrôle L5 ; une consigne à l'infinitif ne suffit pas).
- Une notion à un seul endroit : aucune redite d'un point à l'autre (renvoyer au point qui la porte) ; aucun intertitre « Voici… ».
- Point 11 A- : algorithme d'urgence en cases (modèle <template class="algo-modele">, contrôle E8), puis non-spécialiste → service spécialisé.
- Langue = universitaire, donc soutenue, clarté garantie : ni tutoiement ni impératif familier (tournure impersonnelle ou passive), ni « il y a », « on », « ça » ; aucune phrase nominale
  ni de plus de 40 mots ; aucune répétition. `fin` bloque (GRAVE L1–L4). Relecture de clarté de chaque point avant `fin`.
- Sources (précision de Vial) : l'UNIVERSEL (définitions, sémiologie, physiopathologie, critères internationaux, dénominations des syndromes retenues
  par les sociétés savantes) accepte une source sérieuse non suisse, citée et datée, faute de source suisse ; le LOCAL (recommandations de prise en
  charge, doses, organisation des soins, filières, remboursements, vaccination) exige la Suisse d'abord, sinon l'Europe, sinon une source
  internationale étiquetée « hors AIPS / à valider » (contrôles S21 O1, O2). Souplesse : un contrôle purement formel sans impact pédagogique avertit, il ne bloque pas.
- Doses : AIPS suisse seulement (python3 harnais/aips_texte.py) ; sinon « hors AIPS, recommandation X ; à valider avec un spécialiste avant prescription ». Jamais le Compendium.
- Tout contenu ajouté vient d'une source lue (fichier, liste des sources, PubMed, AIPS) ; sinon « À vérifier ». Rien de mémoire non vérifiée.
- Lecture : jamais le fichier entier ni les lignes data: ; grep -n sur les ancres id="…-pN" puis Read offset/limit ; Edit exact. Pas de commit.
- RÉÉCRITURE POINT PAR POINT (cause des refus de la vague 1 : grosses plaques réécrites, balises perdues, lignes géantes) : un point à la fois ;
  dans un point de plus de 8 000 caractères, une sous-partie par Edit ; jamais un Edit qui chevauche deux points ; jamais Write sur le cours ;
  chaque balise ouverte dans l'Edit y est refermée ; une ligne par paragraphe, puce ou rangée. Après CHAQUE point : `point <fichier> N` jusqu'à VERT."""


def sh(*c):
    return subprocess.run([sys.executable, *c], capture_output=True, text=True, cwd=R).stdout


def lire(f): return Path(f).read_text(encoding="utf-8", errors="replace")


def nu(h): return re.sub(r"(?is)<(script|style|template)\b.*?</\1>", " ", h)     # sans modèle JSON ni CSS


def chiffres(t):
    """Chiffres du texte visible du cours (hors fenêtres) : garde contre la contraction."""
    a, f = bus.bornes_cours(t); tx = bus.texte(nu(t[a:f]))
    return sorted(set(re.findall(r"\d+(?:[,.]\d+)?\s?%|\d+(?:[,.]\d+)?\s?(?:mg|µg|g|ml|mmHg|ans|cm|mmol/l|heures|semaines|jours)\b", tx)))


def instantane(f):
    """Instantané propre au chemin (deux copies d'un même nom ne se mélangent pas)."""
    return CACHE / f"{Path(f).name}.{hashlib.sha1(str(Path(f).resolve()).encode()).hexdigest()[:8]}.json"


def snap(f):
    t = lire(f); CACHE.mkdir(parents=True, exist_ok=True)
    instantane(f).write_text(json.dumps(dict(sha=bus.sha(t), octets=len(t.encode()), chiffres=chiffres(t), sources=t.count('<sup class="r">'))))


def s21(t, nom):
    return S21.analyser(t, nom)[0]


def cerveau(f):
    import cerveau as C
    return C.analyser(lire(f), Path(f).name)[0]


def memoire(role, f, garder=False):
    if not (garder and instantane(f).exists()):                  # --garder : reprise dans la même passe, l'instantané d'entrée reste la référence
        snap(f); couverture(f, raz=True)
    print(f"# CIRCUIT VIAL · rôle {role} · {Path(f).name}\n")
    print(lire(R / "harnais/etat/DIRECTIVE_VIAL_REFONTE.md"))
    print(GABARITS + "\n\n" + REGLES + "\n")
    g = json.loads(lire(R / "harnais/grille14/grille.json"))
    print("## Grille des 14 points (fond à garantir)\nPrincipe : " + g["principe"])
    for p in g["points"]: print(f"- {p[0]}. {p[1]} : {re.sub(chr(10), ' ', p[2])[:420 if role == 'duo' else 2000]}")
    if role == "professeur":
        print("\n## Prompt ULTIME (Prompt universel) : exigences\n" + sh("harnais/prompt_expert.py", "redacteur"))
    D_ = s21(lire(f), Path(f).name)
    print(f"\n## Doléances de forme (S21) à l'entrée : {len(D_)}\n" + "\n".join(f"- {d['severite']} {d['code']} {d['ancre']} : {d['constat']}" for d in D_))
    print("\n## Boucle (point par point, porte courte après chaque point)\n" + ("Pour N = 1 … 14 : a) lis le point N seul (grep -n 'id=\"[^\"]*-pN\"', Read offset/limit) ; "
          "b) stylise-le selon la directive et complète le fond exigé par la grille (source lue, sinon « À vérifier ») par Edit limités à ce point "
          "(une sous-partie par Edit si le point dépasse 8 000 caractères) ; c) `point <fichier> N` jusqu'à VERT. Point 10 : modèle JSON (<template class=\"algo-modele\">, "
          "jamais <script>) puis `algo <fichier> --appliquer`, puis `point <fichier> 10`. Enfin `fin <fichier> --role duo` (porte unique : réparation automatique, "
          "forme, langue ≥ 90, médical ≥ 90) jusqu'à ACCEPTÉ." if role == "duo" else
          "1. `scanner <fichier>` (texte visible par point + rappel de la grille). 2. Vérifie critiquement le fond (doses AIPS, chiffres retrouvés dans leur source, "
          "références existantes, exactitude clinique, ordre de priorité de la prise en charge) et corrige par Edit exact, point par point, avec `point <fichier> N` après chaque point touché. "
          "3. `fin <fichier> --role professeur` (porte unique) jusqu'à ACCEPTÉ."))


def scanner(f, points):
    t = lire(f); nom = Path(f).name; S = bus.sections(t); g = {int(p[0]): p for p in json.loads(lire(R / "harnais/grille14/grille.json"))["points"]}
    D_ = cerveau(f); o = {k: i for i, k in enumerate(bus.SEVERITES)}
    print(f"# SCANNER PROFESSEUR · {nom} · {len(D_)} doléances du cerveau\nRappel du Prompt universel : concis, dense, exhaustif ; Suisse puis Europe ; rien d'inventé ; doses AIPS.\n")
    for n in points:
        if n not in S: print(f"## {n}. ABSENT du fichier → à rédiger\n"); continue
        a, b = S[n]
        la, lb = bus.ligne(t, a), bus.ligne(t, b); ln = lambda d: int((re.search(r"l\.(\d+)", d["ancre"]) or [0, 0])[1])
        dn = sorted([d for d in D_ if d["severite"] in ("CRITIQUE", "GRAVE") and la <= ln(d) < lb], key=lambda d: o[d["severite"]])
        tx = bus.texte_visible(nu(t[a:b]))
        print(f"## {n}. {g[n][1]} · {len(tx)} caractères visibles · ligne {bus.ligne(t, a)}\nExigence : {re.sub(chr(10), ' ', g[n][2])[:900]}")
        for d in dn[:12]: print(f"- {d['severite']} {d['code']} {d['ancre']} : {d['constat']} → {d['correction_prescrite'][:200]}")
        print("Texte : " + tx[:6000] + "\n")


def fin(f, role):
    t = lire(f); nom = Path(f).name; s = instantane(f)
    if not s.exists(): print("REFUSÉ : aucun instantané d'entrée (lance d'abord memoire)"); return 2
    e = json.loads(s.read_text()); ko = []
    if bus.sha(t) == e["sha"]: ko.append("R15 : fichier inchangé (un relevé seul ne termine rien)")
    t2, J = S21.reparer(t)                                   # réparation automatique AVANT la porte (balises, lignes, rendu de l'algorithme)
    if t2 != t: bus.ecrire_atomique(f, t2); t = t2; print("RÉPARÉ : " + " ; ".join(J[:8]))
    elif J: print("À RÉPARER À LA MAIN : " + " ; ".join(J[:4]))
    D_ = cerveau(f); F = [d for d in D_ if d["scriptone"] == S21.ID and d["severite"] in ("GRAVE", "CRITIQUE")]
    C = [d for d in D_ if d["severite"] == "CRITIQUE"]
    BS = [d for d in D_ if d["severite"] == "GRAVE" and d["code"].startswith("BS")]      # chiffre ou dose sans source : vérité médicale (Vial)
    if BS: ko.append(f"{len(BS)} GRAVE de source (chiffre ou dose sans renvoi [Sn] lu) : " + "; ".join(f"{d['code']} {d['ancre']}" for d in BS[:8]))
    retraits = {r["chiffre"] for r in e.get("retraits", [])}
    perdus = [c for c in e["chiffres"] if c not in set(chiffres(t)) and c not in retraits]
    if retraits: print("RETRAITS DÉCLARÉS (relus par l'auditeur et par Vial) : " + " ; ".join(f"{r['chiffre']} ({r['motif']})" for r in e["retraits"]))
    if F: ko.append(f"{len(F)} GRAVE de forme (S21) : " + "; ".join(f"{d['code']} {d['ancre']}" for d in F[:8]))
    if C: ko.append(f"{len(C)} CRITIQUE : " + "; ".join(f"{d['code']} {d['ancre']}" for d in C[:8]))
    if perdus: ko.append(f"chiffres disparus du texte visible ({len(perdus)}) : {', '.join(perdus[:20])} → restituer, ou déclarer un chiffre faux ou introuvable : "
                         f"circuit_vial.py retirer <fichier> \"<chiffre>\" \"<motif et source lue>\"")
    if re.search(r"<script[\s>]|<img[\s>]|<link[^>]+stylesheet", t, re.I): ko.append("<script>, <img> ou feuille externe : interdit par controle_lot (modèle d'algorithme : <template>)")
    src = t.count('<sup class="r">')
    if src < e["sources"]: ko.append(f"appels de source passés de {e['sources']} à {src}")
    if role == "duo":                                         # parcours complet : chaque point passé au VERT par `point`, sur son texte actuel
        cv = couverture(f); S_ = bus.sections(t)
        manque = [n for n in range(1, 15) if n in S_ and cv.get(str(n)) != signature(t, n)]
        if manque: ko.append(f"couverture : point(s) {manque} non contrôlé(s) par `point <fichier> N` sur leur texte actuel (styliser ENTIÈREMENT le cours, point par point)")
    P = portes(f)                                             # porte unique : mêmes mesures que la porte de sortie du lot
    if P["controle_lot"]: ko.append("controle_lot : " + " ; ".join(P["controle_lot"]))
    for k in ("langue", "medical"):
        x = P[k]
        if x["score"] < SEUIL or x["critiques"]: ko.append(f"{k} {x['score']} / {x['critiques']} critique(s) (seuil {SEUIL}, 0) : " + " | ".join(x["corrections"][:6]))
    c = {}
    for d in D_: c[d["severite"]] = c.get(d["severite"], 0) + 1
    print(f"{nom} · rôle {role} · {e['octets']} → {len(t.encode())} octets · doléances {c} · S21 GRAVES {len(F)} · langue {P['langue']['score']} · médical {P['medical']['score']}")
    if ko: print("REFUSÉ :\n- " + "\n- ".join(ko)); return 1
    tr = CACHE / "traites.json"; T = json.loads(tr.read_text()) if tr.exists() else {}
    T.setdefault(str(Path(f).resolve()), {})[role] = bus.sha(t); tr.write_text(json.dumps(T, ensure_ascii=False, indent=0))
    print("ACCEPTÉ"); return 0


def _rapport(script, f):
    """Lance un contrôle d'audit_lot (controle_langue / controle_medical) sur f ; renvoie score, critiques et corrections."""
    CACHE.mkdir(parents=True, exist_ok=True); r = CACHE / f"{Path(script).stem}.{Path(instantane(f)).stem}.md"
    subprocess.run([sys.executable, script, str(f), "--rapport", str(r)], capture_output=True, text=True, cwd=R, timeout=900)
    x = lire(r) if r.exists() else ""; m = re.search(r"RESULTAT score=([\d.]+) critiques=(\d+)", x)
    return dict(score=float(m.group(1)) if m else 0.0, critiques=int(m.group(2)) if m else 99,
                corrections=[l[2:].strip() for l in x.splitlines() if l.startswith("- ")], rapport=str(r))


def portes(f):
    """Mesures de la porte de sortie, pour UN fichier : controle_lot (forme mécanique), langue et médical d'audit_lot."""
    sys.path.insert(0, str(R / "harnais")); import controle_lot as CL
    cl = CL.analyse_fichier(Path(f))
    return dict(controle_lot=cl["critiques"], langue=_rapport("harnais/controle_langue.py", f), medical=_rapport("harnais/controle_medical.py", f))


def mesurer(f):
    t = lire(f); D_ = cerveau(f); c = {}
    for d in D_: c[d["severite"]] = c.get(d["severite"], 0) + 1
    P = portes(f)
    return dict(fichier=Path(f).name, octets=len(t.encode()), lignes=t.count("\n") + 1,
                lignes_longues=sum(1 for l in t.split("\n") if len(l) > 10000 and not S21.RX_LIGNE_OK.search(l)),
                balises=[f"<{g}> {o}/{f_}" + (f" (point {n})" if n else "") for g, o, f_, n in S21.desequilibres(t)],
                doleances=c, graves_s21=sum(1 for d in D_ if d["scriptone"] == S21.ID and d["severite"] in ("GRAVE", "CRITIQUE")),
                codes_graves=sorted({d["code"] for d in D_ if d["severite"] in ("GRAVE", "CRITIQUE")}),
                langue=P["langue"]["score"], langue_crit=P["langue"]["critiques"], medical=P["medical"]["score"], medical_crit=P["medical"]["critiques"],
                controle_lot=P["controle_lot"], chiffres=len(chiffres(t)), sources=t.count('<sup class="r">'))


def signature(t, n):
    """Empreinte du texte d'un point (balises ignorées : une réparation mécanique ne l'invalide pas)."""
    a, b = bus.sections(t)[n]; return bus.sha(bus.texte(t[a:b]))[:16]


def couverture(f, n=None, sig=None, raz=False):
    """Registre des points passés au VERT par `point` depuis l'instantané : preuve que le duo a parcouru les 14 points."""
    c = instantane(f).with_suffix(".couverture.json"); d = {} if raz or not c.exists() else json.loads(c.read_text())
    if n is not None: d[str(n)] = sig
    if raz or n is not None: CACHE.mkdir(parents=True, exist_ok=True); c.write_text(json.dumps(d))
    return d


def point(f, n):
    """Contrôle d'UN point juste après sa rédaction : la boucle courte qui évite les grosses plaques fautives."""
    t = lire(f); S = bus.sections(t)
    if n not in S: print(f"POINT {n} ABSENT (titre <h3 id=\"…-p{n}\"><strong>{n}. …</strong></h3> introuvable)"); return 1
    a, b = S[n]; la, lb = bus.ligne(t, a), bus.ligne(t, b); ko = []
    for g, o, f_, k in S21.desequilibres(t):
        if k == n: ko.append(f"H1 balises <{g}> {o} ouvertes / {f_} fermées dans ce point → refermer dans le même point (ou `reparer`)")
    for i, l in enumerate(t.split("\n")[la - 1:lb - 1], la):
        if len(l) > 10000 and not S21.RX_LIGNE_OK.search(l): ko.append(f"H2 ligne {i} de {len(l)} caractères → une ligne par paragraphe, puce ou rangée")
    ln = lambda d: int((re.search(r"l\.(\d+)", d["ancre"]) or [0, 0])[1])
    for d in S21.analyser(t, Path(f).name)[0]:
        if la <= ln(d) < lb and d["severite"] in ("GRAVE", "CRITIQUE", "MOYEN") and d["code"][0] != "H":
            ko.append(f"{d['severite']} {d['code']} {d['ancre']} : {d['constat']} → {d['correction_prescrite'][:160]}")
    for d in cerveau(f):                                      # sources : chiffre ou dose sans renvoi [Sn] (bloquant à `fin`)
        if la <= ln(d) < lb and d["severite"] in ("GRAVE", "CRITIQUE") and d["code"].startswith("BS"):
            ko.append(f"{d['severite']} {d['code']} {d['ancre']} : {d['constat']} → {d['correction_prescrite'][:160]}")
    if n in (6, 7, 10, 13):
        L = _rapport("harnais/controle_langue.py", f)
        ko += [x for x in L["corrections"] if x.startswith(f"[PHRASES] point {n} ")]
    if not ko: couverture(f, n=n, sig=signature(t, n))
    print(f"POINT {n} · lignes {la}–{lb - 1} · " + ("VERT" if not ko else f"{len(ko)} écart(s) :\n- " + "\n- ".join(ko)))
    return 0 if not ko else 1


def retirer(f, chiffre, motif):
    """Retrait déclaré d'un chiffre faux ou introuvable dans sa source : consigné dans l'instantané et au journal (jamais silencieux)."""
    s = instantane(f)
    if not s.exists(): print("REFUSÉ : aucun instantané (memoire d'abord)"); return 2
    e = json.loads(s.read_text())
    if chiffre not in e["chiffres"]: print(f"REFUSÉ : « {chiffre} » n'est pas un chiffre de l'instantané ({', '.join(e['chiffres'][:12])}…)"); return 1
    if len(motif.split()) < 6: print("REFUSÉ : motif trop court (dire la source lue qui contredit ou ne contient pas le chiffre)"); return 1
    e.setdefault("retraits", []).append(dict(chiffre=chiffre, motif=motif)); s.write_text(json.dumps(e, ensure_ascii=False))
    bus.journal(dict(type="retrait_chiffre", fichier=Path(f).name, chiffre=chiffre, motif=motif))
    print(f"RETRAIT CONSIGNÉ : {chiffre} — {motif}"); return 0


def traite(f):
    """Déjà traité = professeur ACCEPTÉ sur l'état actuel du fichier."""
    tr = CACHE / "traites.json"; T = json.loads(tr.read_text()) if tr.exists() else {}
    return T.get(str(Path(f).resolve()), {}).get("professeur") == bus.sha(lire(f))


def sortie(d):
    """Même verdict que le hook pre-commit (harnais/audit_sortie.py) ; un rapport MED_/CONF_ plus ancien que son cours est périmé (audit_lot
    ne le recalculerait pas) : il est déplacé dans audits/perimes/ pour forcer un nouveau contrôle."""
    d = Path(d).resolve(); lot = re.search(r"LOT_(\d{3})", d.name).group(1); a = d / "audits"; dep = []
    for r in sorted(a.glob("*_C*.md")) if a.exists() else []:
        m = re.match(r"(?:MED|CONF)_(.+\.html)_C\d+\.md$", r.name)
        if m and (d / m.group(1)).exists() and r.stat().st_mtime < (d / m.group(1)).stat().st_mtime:
            (a / "perimes").mkdir(exist_ok=True); r.rename(a / "perimes" / r.name); dep.append(r.name)
    run = lambda *c: subprocess.run([sys.executable, *c], capture_output=True, text=True, cwd=R)
    cl = json.loads(run("harnais/controle_lot.py", "verifier", str(d), "--json").stdout or "{}")
    au = run("harnais/audit_sortie.py", f"LOT_{lot}", "--dossier", str(d))
    nc = {}
    for f in cl.get("fichiers", []):
        if f.get("critiques"): nc.setdefault(f["fichier"], []).append("forme : " + " ; ".join(f["critiques"]))
    for l in au.stdout.splitlines():
        m = re.match(r"\|\s*(LOT_\S+\.html)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*NON\s*\|", l)
        if m:
            c = [x for x in sorted(a.glob(f"*_{m.group(1)}_C*.md"))]
            nc.setdefault(m.group(1), []).append(f"médical {m.group(2).strip()} · langue {m.group(3).strip()} (score / critiques ; seuil 90 et 0) ; rapports : " + ", ".join(str(x.relative_to(R)) if x.is_relative_to(R) else str(x) for x in c))
    ok = au.returncode == 0
    lignes = au.stdout.strip().splitlines()
    return dict(conforme=ok, non_conformes=[dict(fichier=k, motifs=" | ".join(v)) for k, v in nc.items()],
                resume=f"{'SORTIE AUTORISÉE' if ok else 'SORTIE REFUSÉE'} · {next((x for x in lignes if x.startswith('FORME')), '')} · {next((x for x in lignes if x.startswith('BILAN')), '')}"
                       + (f" · lot : {'; '.join(cl.get('critiques_lot', []))}" if cl.get("critiques_lot") else "") + (f" · {len(dep)} rapport(s) périmé(s) écarté(s)" if dep else ""))


def reprise(f):
    snap(f); p = Path(f); a = p.parent / "audits"
    print(f"# REPRISE DE SORTIE · {p.name}\nObjectif : audit_sortie conforme (médical et langue ≥ 90, 0 critique ; controle_lot sans critique) sans rien retrancher.\n"
          "Méthode : skill controle-langue pour CONF_, skill controle-medical pour MED_ ; lecture par points ; Edit exact.\n")
    for r in sorted(a.glob(f"*_{p.name}_C*.md")) if a.exists() else []:
        t = lire(r); print(f"## {r.name}\n" + t[:5000] + ("\n… (suite : Read " + str(r) + ")" if len(t) > 5000 else ""))
    cl = subprocess.run([sys.executable, "harnais/controle_lot.py", "verifier", str(p.parent), "--json"], capture_output=True, text=True, cwd=R).stdout
    for x in json.loads(cl or "{}").get("fichiers", []):
        if x["fichier"] == p.name and x.get("critiques"): print("## controle_lot\n- " + "\n- ".join(x["critiques"]))
    D_ = [d for d in s21(lire(f), p.name) if d["severite"] in ("GRAVE", "CRITIQUE")]
    if D_: print("## Forme (S21)\n" + "\n".join(f"- {d['code']} {d['ancre']} : {d['constat']}" for d in D_))
    print(f"\nFin : python3 harnais/brain/circuit_vial.py fin {f} --role duo")


def repartir(fs):
    fs = [str(Path(x).resolve()) for x in fs]
    if len(fs) > VAGUE: print(f"# {len(fs) - VAGUE} leçon(s) au-delà de {VAGUE} : vague suivante", file=sys.stderr)
    fs = fs[:VAGUE]
    # 12 professeurs, une leçon par appel : le professeur k prend la leçon k ; les leçons 13 à 16 vont au tourniquet (premier professeur libre).
    profs = [dict(opus=k + 1, lecons=[f for j, f in enumerate(fs) if j % OPUS == k]) for k in range(OPUS)]
    return dict(lecons=len(fs), duos=[dict(duo=i + 1, lecon=f) for i, f in enumerate(fs)], professeurs=profs,
                regle=f"{len(fs)} duos Sonnet 5.5 ; 12 professeurs Opus 5.5 moyen, une leçon par appel, chacun dès que le duo de sa leçon a fini ; "
                      "tourniquet : les leçons 13 à 16 vont aux premiers professeurs libres (prévision : Opus 1 à 4) ; puis porte de sortie du lot (boucle bornée)")


def main(a):
    if len(a) < 2 or a[0] in ("-h", "--help"): print(__doc__); return 0
    c = a[0]
    if c == "memoire": memoire(a[1], a[2], "--garder" in a); return 0
    if c == "scanner":
        pts = [int(x) for x in a[a.index("--points") + 1].split(",")] if "--points" in a else list(range(1, 15)); scanner(a[1], pts); return 0
    if c == "algo":
        t = lire(a[1]); t2 = S21.corriger(t)
        print(f"{Path(a[1]).name} : {'aucun changement' if t2 == t else f'{len(t2.encode()) - len(t.encode()):+d} octets'}{'' if '--appliquer' in a else ' (dry-run)'}")
        if "--appliquer" in a and t2 != t: bus.ecrire_atomique(a[1], t2)
        D_ = [d for d in s21(t2, Path(a[1]).name) if d["code"].startswith("D")]
        print("\n".join(f"- {d['severite']} {d['code']} : {d['constat']}" for d in D_) or "point 10 conforme (S21)"); return 0
    if c == "sortie":
        r = sortie(a[1])
        if "--json" in a: print(json.dumps(r, ensure_ascii=False))
        else: print(r["resume"] + "".join(f"\n- {x['fichier']} : {x['motifs']}" for x in r["non_conformes"]))
        return 0 if r["conforme"] else 1
    if c == "reprise": reprise(a[1]); return 0
    if c == "point": return point(a[1], int(a[2]))
    if c == "retirer": return retirer(a[1], a[2], a[3] if len(a) > 3 else "")
    if c == "reparer":
        t = lire(a[1]); t2, J = S21.reparer(t)
        if t2 != t: bus.ecrire_atomique(a[1], t2)
        print(f"{Path(a[1]).name} : " + ("; ".join(J) if J else "rien à réparer")); return 0
    if c == "mesurer":
        r = mesurer(a[1]); print(json.dumps(r, ensure_ascii=False) if "--json" in a else "\n".join(f"{k} : {v}" for k, v in r.items())); return 0
    if c == "fin": return fin(a[1], a[a.index("--role") + 1] if "--role" in a else "duo")
    if c == "repartir":
        xs = [x for i, x in enumerate(a[1:], 1) if not x.startswith("--") and a[i - 1] != "--liste"]
        if "--liste" in a: xs += [l.strip() for l in lire(a[a.index("--liste") + 1]).splitlines() if l.strip() and not l.startswith("#")]
        nat = lambda s: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", s)]
        fs = sorted({str(p) for x in xs for p in (Path(x).glob("LOT_*_Phase_*.html") if Path(x).is_dir() else [Path(x)])}, key=nat)
        if "--phase-b" in a: fs = [f for f in fs if "_Phase_B_" in f]
        if "--phase-a" in a: fs = [f for f in fs if "_Phase_A_" in f]
        if "--exclure-traites" in a:
            t0 = len(fs); fs = [f for f in fs if not traite(f)]
            if t0 != len(fs): print(f"# {t0 - len(fs)} leçon(s) déjà traitée(s) (professeur ACCEPTÉ sur l'état actuel) exclue(s)", file=sys.stderr)
        r = repartir(fs)
        if "--json" in a: print(json.dumps(r, ensure_ascii=False)); return 0
        print(r["regle"])
        for d in r["duos"]: print(f"duo {d['duo']:>2} ← {Path(d['lecon']).name}")
        for p in r["professeurs"]: print(f"opus {p['opus']:>2} ← " + " puis ".join(Path(x).name for x in p["lecons"]))
        return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
