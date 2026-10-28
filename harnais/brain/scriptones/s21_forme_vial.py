#!/usr/bin/env python3
"""Scriptone S21 · forme de la directive de Vial du 28.10.2026 (harnais/etat/DIRECTIVE_VIAL_REFONTE.md). Région AUF.
Hors registre des 160 (chargé directement par cerveau.py) : il AJOUTE des contrôles, il n'en retire aucun.
  Point 10 · arbre décisionnel = vrai algorithme en cases reliées par des traits horizontaux et verticaux
    D1 algorithme en cases absent (liste à puces ou texte)        D2 cercle, ellipse ou coin arrondi à 50 % dans l'arbre
    D3 segment oblique (ligne SVG ou chemin non orthogonal)       D4 moins de 3 cases ou aucun losange de décision
    D5 cases sans détail cliquable                                D6 modèle JSON d'algorithme non rendu (script : corriger)
  Point 11 · prise en charge
    E1 « But » absent      E2 « Moyens et méthodes » absent      E3 A urgences : non-spécialiste puis service spécialisé absents
    E4 B hors urgences : mesures générales puis spécifiques absentes      E5 actes du service spécialisé non cliquables
    E6 ordre B non respecté (générales avant spécifiques ; pharmacologique avant non pharmacologique)   E8 A- urgences sans algorithme en cases
    E7 titre « Prise en charge » sans bande colorée soulignée (h3 id …-p11 absent ou CSS brain-vial non posée → script : corriger)
  Point 7 · syndromes
    Q1 intitulé non numéroté « 7.n Syndrome … »    Q2 « Symptômes fonctionnels » absent    Q3 « Signes physiques » absent
    Q4 signes physiques sans sous-cellules cliquables (span.sc.dx)   Q5 sous-cellule dont la fenêtre ne dit pas comment rechercher le signe
    Q6 intitulé de syndrome non documenté (« intitulé de travail »)
  Origine des sources (précision de Vial) : O1 donnée locale (recommandation, filière, remboursement, vaccination aux points 11, 12 ;
    point 2 en avertissement) appuyée sur une source seulement
    internationale sans étiquette « hors AIPS / à valider » ; O2 dose appuyée sur une source non suisse sans étiquette. L'universel accepte
    une source sérieuse non suisse, datée. Souplesse : contrôles purement formels en MOYEN (non bloquant), p. ex. « voici », questions juxtaposées.
  Q0 point 7 sans aucun syndrome numéroté « 7.n » (titres en gras, en h4 ou en cellule de tableau)
  R1 identifiant de case à cocher dupliqué (fenêtre qui ne s'ouvre pas)
  Intégrité (mêmes seuils que controle_lot, localisés) : H1 balises de bloc déséquilibrées (point fautif) · H2 ligne > 10 000 caractères
  Réparation sûre (reparer) : rendu des algorithmes, balises fermées en fin de point ou fermante orpheline retirée, lignes coupées aux fins de blocs
  Registre universitaire et clarté (texte courant <p> et <li>, hors fenêtres ; directive « Langue = Universitaire ») :
    L1 tournure faible ou familière (tutoiement, impératif familier, « il y a », « on », « ça », « un peu »…)   L2 phrase trop longue (> 40 mots)
    L5 cellule de tableau nominale (≥ 6 mots sans verbe conjugué, hors puces ; 1re colonne exemptée)
    L3 phrase nominale sans verbe dans un paragraphe (≥ 12 mots)    L4 phrase répétée à l'identique (GRAVE) ; mot plein répété 3 fois dans une phrase (MOYEN)
Correction (--appliquer) : rend chaque <template class="algo-modele"> (ou div.algo[data-modele]) en algorithme
en cases (rectangles, losanges), traits strictement horizontaux et verticaux, cases cliquables à fenêtre ; pose la CSS brain-vial.
Le script ne crée jamais de contenu médical : il dessine le modèle écrit par l'agent.
COURS FLASH (harnais/etat/COURS_FLASH.md, 28.10.2026) : contrôles AJOUTÉS, actifs seulement en mode Flash (analyser(..., {"flash": True}),
  flash(t, nom), `circuit_vial.py … --flash` ou instantané pris en mode Flash). Gabarit de référence : harnais/brain/gabarit_flash.html.
  Ko = 1 000 octets, fichier entier (notions, CSS et fenêtres comprises).
    V1 volume > 280 Ko (GRAVE, bloquant ; tolérance de Vial)   V2 volume > 200 Ko (MOYEN : visé 100–200)   V3 volume < 100 Ko (MOYEN : fond peut-être insuffisant)
    N1 bloc « Notions voisines » ou « Diagnostic(s) différentiel(s) » (liste ou tableau) dans le corps, hors fenêtre (GRAVE ; replié en <details> : MOYEN)
    I1 aucun îlot (GRAVE)   I2 points 1–4 hors d'un même îlot (GRAVE si un point est hors îlot, sinon MOYEN)   I3 points 5–6 hors d'un même îlot
       (même règle)   I4 point 7–14 non replié (<details class="ilot"> sans « open ») (MOYEN)   I5 CSS brain-flash (bords, justification, fenêtres
       modales) non posée (MOYEN, script)   I6 style en ligne qui casse la largeur ou la justification d'un îlot (MOYEN)   I7 îlot saturé (MOYEN)
    W1 aucune fenêtre modale cliquable (GRAVE)   W3 symptômes non cliquables (GRAVE si aucun aux points 5 et 7 ; sinon MOYEN par syndrome)
    W4 signes d'examen du point 6 non cliquables (GRAVE si aucun ; fenêtre sans manœuvre : MOYEN)   W5 syndrome sans fenêtre à tableau
       « symptôme | signes physiques » (GRAVE si aucun syndrome n'en a ; sinon MOYEN par syndrome)   W6 tableau de syndrome ≠ 2 colonnes (MOYEN)
    W7 algorithme du point 11 sans détails cliquables (MOYEN)   W8 précision longue en survol (> 40 mots : fenêtre cliquable attendue) (MOYEN)
    D2/D3 traits non orthogonaux ou cercles aussi dans l'algorithme du point 11.
  Souplesse : un défaut sans conséquence d'apprentissage reste MOYEN (avertissement, non bloquant)."""
import html as H, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s21_forme_vial", "AUF", "1.2.0"
COL, ROW, CW, CH, LW, LH, M = 250, 125, 184, 66, 196, 96, 20
CSS = ('<style id="brain-vial">div.algo{margin:14px 0}div.algo>input{position:absolute;opacity:0;width:0;height:0}.algo-t{font-weight:700;color:#4c1d95;margin-bottom:6px}'
       '.algo-sc{overflow-x:auto;padding-bottom:4px}.algo-can{position:relative}.algo-can svg{position:absolute;left:0;top:0}.algo-can svg .tr{stroke:#6d28d9;stroke-width:2;fill:none}'
       '.algo-can svg .ca{fill:#f5f3ff;stroke:#7c3aed;stroke-width:1.5}.algo-can svg .lo{fill:#fef3c7;stroke:#b45309;stroke-width:1.5}.algo-can svg .fi{fill:#dcfce7;stroke:#15803d;stroke-width:1.5}'
       '.algo-can svg .fl{fill:#6d28d9}.algo-can svg text{font-size:12px;fill:#4c1d95;font-weight:700}.algo-n{position:absolute;display:flex;align-items:center;justify-content:center;'
       'text-align:center;font-size:.86em;line-height:1.25;cursor:pointer;color:#1e1b4b;padding:4px 8px;box-sizing:border-box}.algo-n.lo{padding:4px 34px}'
       '.algo-n.cl{text-decoration:underline dotted #7c3aed}.algo-n:hover{color:#6d28d9}.algo-d{display:none;margin:6px 0;padding:8px 12px;background:#f5f3ff;'
       'border-left:4px solid #a78bfa;border-radius:6px;font-size:.95em}'
       'span.sc.dx{display:inline-block;border:1px solid #c4b5fd;background:#faf5ff;border-radius:6px;padding:1px 8px;margin:2px 4px 2px 0}'
       'span.sc.dx>.dxc{border-left:4px solid #a78bfa}'
       'h3[id$="-p11"]{background:linear-gradient(90deg,#ede9fe,transparent);border-left:6px solid #7c3aed;text-decoration:underline;padding:4px 10px}'
       '@media(prefers-color-scheme:dark){.algo-can svg .ca{fill:#241d3f}.algo-can svg .lo{fill:#3b2a10}.algo-can svg .fi{fill:#12301f}.algo-n{color:#ede9fe}'
       '.algo-can svg text{fill:#ddd0ff}.algo-d{background:#241d3f}span.sc.dx{background:#241d3f;border-color:#5b21b6}h3[id$="-p11"]{background:linear-gradient(90deg,#2e1065,transparent)}}</style>')
# Cours Flash : îlots à bords visibles, texte justifié, même largeur ; fenêtres modales sans script (case à cocher + label, contrôle_lot interdit <script>).
# span.dx / span.sc.dx (fenêtre courte, en ligne) et div.fxw > div.fx (fenêtre riche : tableau de syndrome, méthode) ; détails des cases d'algorithme en modale.
CSS_FLASH = ('<style id="brain-flash">'
             '.ilot{display:block;box-sizing:border-box;width:100%;max-width:100%;margin:16px 0;padding:10px 18px 12px;border:1.5px solid #a78bfa;border-radius:8px;background:#fff}'
             '.ilot p,.ilot li{text-align:justify;hyphens:auto}.ilot td,.ilot th{text-align:left}'
             'details.ilot>summary{cursor:pointer;list-style:none;padding:2px 0}details.ilot>summary::-webkit-details-marker{display:none}'
             'details.ilot>summary::before{content:"▸ ";color:#7c3aed;font-weight:700}details.ilot[open]>summary::before{content:"▾ "}'
             'details.ilot>summary>h3{display:inline-block;margin:6px 0}'
             'span.dx>input{position:absolute;opacity:0;width:0;height:0}span.dx>.dxt{cursor:pointer;border-bottom:1px dotted #7c3aed;color:#4c1d95}'
             'span.dx>input:focus-visible+.dxt{outline:2px solid #7c3aed}span.dx>span.dxc{display:none}'
             'span.dx>input:checked~span.dxc{display:block;position:fixed;left:50%;top:50%;transform:translate(-50%,-50%);width:min(680px,92vw);max-height:82vh;'
             'overflow:auto;z-index:95;margin:0;padding:14px 18px;background:#fff;color:#111;border:2px solid #7c3aed;border-radius:10px;'
             'box-shadow:0 0 0 100vmax rgba(15,23,42,.55);text-align:justify;font-size:.95em}'
             '.fxw{display:block;margin:4px 0}.fxw>input{position:absolute;opacity:0;width:0;height:0}'
             '.fxw>.fx-o{cursor:pointer;border-bottom:1px dotted #7c3aed;color:#4c1d95}.fxw>.fx-o::after{content:" ⧉";font-size:.8em;color:#7c3aed}'
             '.fxw>input:focus-visible+.fx-o{outline:2px solid #7c3aed}'
             '.fx{display:none}.fxw>input:checked~.fx{display:flex;position:fixed;inset:0;z-index:90;align-items:center;justify-content:center;background:rgba(15,23,42,.55)}'
             '.fx>.fx-f{position:absolute;inset:0;cursor:pointer}'
             '.fx>.fx-b{position:relative;box-sizing:border-box;width:min(760px,94vw);max-height:84vh;overflow:auto;background:#fff;color:#111;'
             'border:2px solid #7c3aed;border-radius:10px;padding:14px 18px;text-align:justify}'
             '.fx-x{float:right;cursor:pointer;font-weight:700;font-size:1.25em;line-height:1;color:#6d28d9;padding:0 4px}'
             '.fx table{border-collapse:collapse;width:100%}.fx th,.fx td{border:1px solid #c4b5fd;padding:4px 8px;vertical-align:top;text-align:left}'
             '.algo-det>.algo-d{position:fixed;left:50%;top:50%;transform:translate(-50%,-50%);width:min(640px,92vw);max-height:80vh;overflow:auto;z-index:95;'
             'margin:0;background:#fff;border:2px solid #7c3aed;box-shadow:0 0 0 100vmax rgba(15,23,42,.55);text-align:justify}'
             '@media(prefers-color-scheme:dark){.ilot{background:#14112a;border-color:#5b21b6}span.dx>input:checked~span.dxc,.fx>.fx-b,.algo-det>.algo-d'
             '{background:#1e1b4b;color:#ede9fe}.fxw>.fx-o{color:#ddd0ff}}</style>')
KO = 1000                                        # Ko = 1 000 octets ; bande Flash 100–280 Ko (tolérée ; visé 100–200), fichier entier
FLASH_MAX, FLASH_VISE, FLASH_MIN = 280 * KO, 200 * KO, 100 * KO
ILOT_SATURE = 12000                              # caractères visibles (hors fenêtres) au-delà desquels un îlot est saturé
RX_FAIBLE = re.compile(r"(?i)(?<![\wÀ-ÿ-])(?:tu|toi|ton|ta|tes|te|t'|il y a|on|ça|ca va|un peu|pas mal|en gros|truc|trucs|chose|choses|vraiment|super|carrément|quelque chose|voici|voilà)(?![\wÀ-ÿ'])"
                       r"|^(?:Vérifie|Procède|Revois|Organise|Propose|Sois|Prescris|Exclus|Traite|Cherche|Demande|Évite|Pense|Adapte|Décide|Confirme|Fais|Mets|(?:Contrôle|Note|Garde|Demande|Recherche) (?=une?\b|les?\b|la\b|l'|des\b)|Mesure (?=l'|les?\b|la\b))\b")
# Groupe nominal + forme en -e/-ent + mot-outil : verbe conjugué absent du lexique (« l'insuffisance veineuse cause souvent… »)
RX_SV2 = re.compile(r"(?i)(?:^|\s)(?:l'|le |la |les |un |une |ce |cet |cette |ces |il |elle |ils |elles |qui |on )[\wÀ-ÿœ'-]+(?: [\wÀ-ÿœ-]+)? [\wÀ-ÿœ]{2,}(?:e|ent|it|ait) "
                    r"(?:souvent|toujours|parfois|rarement|d'abord|ensuite|alors|aussi|également|surtout|le|la|les|un|une|des|l'|à|au|aux|en|par|sur|chez|dans|que|de|du|d')\b")
RX_TECH = re.compile(r"(?i)recherch|technique|manœuvre|manoeuvre|palp|inspect|percu|auscult|press|mesur|demander|faire|patient (?:debout|couché|assis)|décubitus|comparer|observer|tester|chercher")


# ───────────────────────── rendu de l'algorithme (traits orthogonaux) ─────────────────────────
def _plan(mod):
    N = {n["id"]: n for n in mod["noeuds"]}; ordre = [n["id"] for n in mod["noeuds"]]
    enf = {i: [] for i in ordre}; par = {}
    for l in mod.get("liens", []):
        if l["de"] in N and l["a"] in N and l["a"] not in par and l["a"] != l["de"]:
            par[l["a"]] = l["de"]; enf[l["de"]].append(l["a"])
    # Colonne vertébrale : l'enfant principal (lien « Non », sinon le plus grand sous-arbre) reste dans la colonne du parent (trait vertical
    # droit) ; les autres branches partent à droite. Contour par profondeur : aucune case ne chevauche une autre.
    eti = {(l["de"], l["a"]): str(l.get("etiquette", "")).strip().lower() for l in mod.get("liens", [])}
    taille_ = lambda i: 1 + sum(taille_(c) for c in enf[i])
    prof, x, nf = {}, {}, {}
    def sous(i): return [i] + [y for c in enf[i] for y in sous(c)]
    def place(i, d):
        prof[i] = d
        if not enf[i]:
            x[i] = nf.get(d, 0)
        else:
            cs = sorted(enf[i], key=lambda c: (eti.get((i, c)) != "non", -taille_(c)))
            lat = cs[1] if len(cs) > 1 and N[i].get("type") == "losange" else None     # 1re branche latérale d'un losange : même rangée, trait horizontal
            place(cs[0], d + 1); x[i] = x[cs[0]]
            if x[i] < nf.get(d, 0):
                dx = nf[d] - x[i]
                for y in sous(i):
                    if y in x: x[y] += dx
            nf[d] = max(nf.get(d, 0), x[i] + 1)
            for c in cs[1:]: place(c, d if c == lat else d + 1)
        for y in sous(i):
            if y in x: nf[prof[y]] = max(nf.get(prof[y], 0), x[y] + 1)
    for r in [i for i in ordre if i not in par]: place(r, 0)
    return N, ordre, par, prof, x


def rendre(mod, pre):
    N, ordre, par, prof, x = _plan(mod)
    larg = int(M * 2 + (max(x.values()) + 1) * COL); haut = int(M * 2 + (max(prof.values()) + 1) * ROW - (ROW - LH))
    cx = lambda i: M + x[i] * COL + COL / 2
    def taille(i): return (LW, LH) if N[i].get("type") == "losange" else (CW, CH)
    top = lambda i: M + prof[i] * ROW + (LH - taille(i)[1]) / 2
    bas = lambda i: top(i) + taille(i)[1]
    svg, lab, det, css, sorties = [], [], [], [], {}
    for l in mod.get("liens", []):
        a, b = l["de"], l["a"]
        if a not in N or b not in N: continue
        if prof[b] == prof[a] and x[b] > x[a]:                  # branche latérale : sommet droit du losange → bord gauche de la case
            xa, xb, y = cx(a) + taille(a)[0] / 2, cx(b) - taille(b)[0] / 2, top(a) + taille(a)[1] / 2
            svg.append(f'<path class="tr" d="M{xa:.0f} {y:.0f} H{xb - 7:.0f}"/><polygon class="fl" points="{xb - 8:.0f},{y - 5:.0f} {xb - 8:.0f},{y + 5:.0f} {xb:.0f},{y:.0f}"/>')
            if l.get("etiquette"): svg.append(f'<text x="{xa + 6:.0f}" y="{y - 6:.0f}">{H.escape(l["etiquette"])}</text>')
            continue
        x1, y1, x2, y2 = cx(a), bas(a), cx(b), top(b)
        fleche = f'<polygon class="fl" points="{x2 - 5:.0f},{y2 - 8:.0f} {x2 + 5:.0f},{y2 - 8:.0f} {x2:.0f},{y2:.0f}"/>'
        if par.get(b) == a:                                     # lien de l'arbre : rangée suivante, coude dans le couloir entre les rangées
            ym = y1 + (y2 - y1) / 2
            d_ = f"M{x1:.0f} {y1:.0f} V{y2 - 7:.0f}" if round(x1) == round(x2) else f"M{x1:.0f} {y1:.0f} V{ym:.0f} H{x2:.0f} V{y2 - 7:.0f}"
            svg.append(f'<path class="tr" d="{d_}"/>' + fleche)
            if l.get("etiquette"): svg.append(f'<text x="{x2 + 6:.0f}" y="{ym - 4:.0f}">{H.escape(l["etiquette"])}</text>')
            continue
        # Lien de retour ou de jonction (cible déjà rattachée) : sortie par un côté libre de la source, couloir vertical entre les colonnes
        # (aucune case n'y passe), couloir horizontal au-dessus de la rangée cible, entrée par le haut de la cible. Jamais à travers une case.
        droite_prise = any(prof.get(c) == prof[a] and x[c] > x[a] for c in N if par.get(c) == a)      # branche latérale sortante
        gauche_prise = a in par and prof[par[a]] == prof[a]                                             # branche latérale entrante
        cotes = (["g", "d"] if x[b] <= x[a] else ["d", "g"])
        pris = sorties.setdefault(a, set())                     # un côté ne porte qu'une sortie de retour
        cote = next((c for c in cotes if c not in pris and not (gauche_prise if c == "g" else droite_prise)), "b")
        if cote == "b" and (any(par.get(c) == a and prof.get(c) != prof[a] for c in N) or "b" in pris):
            cote = next((c for c in ("d", "g") if c not in pris and not (gauche_prise if c == "g" else droite_prise)), "b")
        pris.add(cote)
        wa, ha = taille(a); ya = top(a) + ha / 2
        yb = M + prof[b] * ROW - 12
        if cote == "b":                                         # deux côtés pris : sortie par le bas, couloir sous la rangée, puis couloir de colonne
            xc = M + (x[a] + 1) * COL - 20; yc = M + prof[a] * ROW + LH + 8      # couloir décalé : jamais confondu avec une sortie latérale
            d_ = f"M{x1:.0f} {y1:.0f} V{yc:.0f} H{xc:.0f} V{yb + 6:.0f} H{x2:.0f} V{y2 - 7:.0f}"; xs = x1 - 34; ya = y1 + 22
        else:
            xs = cx(a) - wa / 2 if cote == "g" else cx(a) + wa / 2
            xc = M + x[a] * COL + 6 if cote == "g" else M + (x[a] + 1) * COL - 6
            d_ = f"M{xs:.0f} {ya:.0f} H{xc:.0f} V{yb:.0f} H{x2:.0f} V{y2 - 7:.0f}"
        gauche = cote == "g"
        svg.append(f'<path class="tr" d="{d_}"/>' + fleche)
        if l.get("etiquette"):
            svg.append(f'<text x="{(xc + 3) if gauche else (xs + 4):.0f}" y="{ya - 6:.0f}">{H.escape(l["etiquette"])}</text>')
    for j, i in enumerate(ordre):
        n = N[i]; w, h = taille(i); X, Y = cx(i) - w / 2, top(i); typ = n.get("type", "case")
        if typ == "losange":
            svg.append(f'<polygon class="lo" points="{cx(i):.0f},{Y:.0f} {X + w:.0f},{Y + h / 2:.0f} {cx(i):.0f},{Y + h:.0f} {X:.0f},{Y + h / 2:.0f}"/>')
        else:
            svg.append(f'<rect class="{"fi" if typ == "fin" else "ca"}" x="{X:.0f}" y="{Y:.0f}" width="{w}" height="{h}"/>')
        cid = f"{pre}-{j + 1}"; cl = "lo" if typ == "losange" else "ca"
        if n.get("detail"):
            lab.append(f'<label class="algo-n {cl} cl" for="{cid}" style="left:{X:.0f}px;top:{Y:.0f}px;width:{w}px;height:{h}px"><span>{n["texte"]}</span></label>')
            det.append(f'<div class="algo-d" id="{cid}-d"><label class="fx-x" for="{cid}" aria-label="Fermer">×</label><b class="algo-dt">{n["texte"]}</b> · {n["detail"]}</div>')
            css.append(f"#{cid}:checked~.algo-det #{cid}-d{{display:block}}")
        else:
            lab.append(f'<div class="algo-n {cl}" style="left:{X:.0f}px;top:{Y:.0f}px;width:{w}px;height:{h}px"><span>{n["texte"]}</span></div>')
    entrees = [f'<input type="checkbox" id="{pre}-{j + 1}">' for j, i in enumerate(ordre) if N[i].get("detail")]
    modele = json.dumps(mod, ensure_ascii=False, indent=0).replace("</template", "<\\/template")
    # Une ligne par élément (trait, case, étiquette, fenêtre) : aucune ligne > 10 000 caractères (controle_lot), quelle que soit la taille de l'arbre.
    nl = "\n"
    return (f'<div class="algo" data-brain="algo" data-id="{pre}"><template class="algo-modele">{modele}</template>\n<style>{nl.join(css)}</style>\n{nl.join(entrees)}\n'
            f'<div class="algo-t">{mod.get("titre", "Algorithme de décision")}</div>\n<div class="algo-sc"><div class="algo-can" style="width:{larg}px;height:{haut}px">\n'
            f'<svg width="{larg}" height="{haut}" viewBox="0 0 {larg} {haut}" aria-hidden="true">\n{nl.join(svg)}\n</svg>\n{nl.join(lab)}\n</div></div>\n'
            f'<div class="algo-det">\n{nl.join(det)}\n</div></div><!--/algo-->')


RX_MODELE = re.compile(r'(?is)<(template|script)(?: type="application/json")? class="algo-modele"[^>]*>(.*?)</\1>')     # <template> : aucun <script> dans un cours (controle_lot)
RX_BLOC = re.compile(r'(?is)<div class="algo" data-brain="algo" data-id="([^"]+)"(?: data-modele="([^"]*)")?>(.*?)<!--/algo-->')
# Le modèle JSON reste dans le bloc rendu (<template class="algo-modele">, source de vérité lisible) : l'agent corrige le modèle puis relance
# `circuit_vial.py algo <fichier> --appliquer` ; le rendu est recalculé (idempotent).


def _modele(m):
    s_ = RX_MODELE.search(m.group(3))
    return json.loads(s_.group(2)) if s_ else json.loads(H.unescape(m.group(2) or "{}"))


def corriger(t, opt=None):
    blocs = []
    def garde(m):
        blocs.append(rendre(_modele(m), m.group(1))); return f"\x00ALGO{len(blocs) - 1}\x00"
    t2 = RX_BLOC.sub(garde, t)
    pris = set(re.findall(r'data-id="(algo\d+)"', t)); n = [0]
    def neuf(m):
        n[0] += 1
        while f"algo{n[0]}" in pris: n[0] += 1
        pris.add(f"algo{n[0]}"); return rendre(json.loads(m.group(2)), f"algo{n[0]}")
    t2 = RX_MODELE.sub(neuf, t2)
    t2 = re.sub("\x00ALGO(\\d+)\x00", lambda m: blocs[int(m.group(1))], t2)
    if 'class="algo"' in t2 or 'class="sc dx"' in t2 or "-p11" in t2:
        t2 = bus.pose_style(t2, "brain-vial", CSS)
    if (opt or {}).get("flash") or RX_ILOT.search(t2) or 'class="fxw"' in t2 or 'id="brain-flash"' in t2:
        t2 = bus.pose_style(t2, "brain-flash", CSS_FLASH)       # après brain-vial (dernier bloc du <head>) : îlots et fenêtres modales
    return t2


# ───────────────────────── intégrité : mesure et réparation sûre (aucun contenu créé ni retranché) ─────────────────────────
BALISES = ("div", "table", "details", "ul", "ol", "section")
RX_LIGNE_OK = re.compile(r"data:font|font/woff|data:[\w/+.-]+;base64")
RX_INERTE = re.compile(r"(?is)<(style|template|script)\b.*?</\1>|<!--.*?-->")


def _inerte(t):
    """Masque CSS, modèles JSON, scripts et commentaires (positions conservées)."""
    return RX_INERTE.sub(lambda m: " " * len(m.group(0)), t)


def _bornes_points(t):
    """[(n, début, fin)] des points du cours, la fin du dernier point étant le début des sources."""
    S = bus.sections(t); return sorted(((n, a, f) for n, (a, f) in S.items()), key=lambda x: x[1])


RX_ILOT = re.compile(r'(?is)<(section|details|div)\b([^>]*\bclass="(?:[^"]*\s)?ilot(?:\s[^"]*)?"[^>]*)>')


def _fermeture(t, pos, g):
    """Fin (position après la fermante) de l'élément <g> ouvert à pos, par comptage d'imbrication ; None si jamais refermé."""
    n = 0
    for x in re.finditer(rf"(?is)<(/?){g}\b[^>]*>", t[pos:]):
        n += -1 if x.group(1) else 1
        if n == 0: return pos + x.end()
    return None


def ilots(t, m=None):
    """[(début, fin, balise, attributs)] des îlots du Cours Flash (section/details/div de classe « ilot ») ; fin None si non refermé."""
    m = _inerte(t) if m is None else m
    return [(x.start(), _fermeture(m, x.start(), x.group(1).lower()), x.group(1).lower(), x.group(2)) for x in RX_ILOT.finditer(m)]


def _sans_ilots(m):
    """Masque les ouvrantes et fermantes d'îlots appariées : un îlot enjambe plusieurs points sans fausser la localisation par point."""
    for a, b, g, _ in ilots(None, m):
        if b is None: continue
        o = m.find(">", a) + 1; c = m.rfind("<", a, b)
        m = m[:a] + " " * (o - a) + m[o:c] + " " * (b - c) + m[b:]
    return m


def desequilibres(t):
    """[(balise, ouvertes, fermées, point)] : déséquilibres globaux (point 0) et par point (localisation ; îlots appariés ignorés)."""
    m = _inerte(t); out = []; mp = None
    for g in BALISES:
        o, f = len(re.findall(rf"(?i)<{g}[\s>]", m)), len(re.findall(rf"(?i)</{g}\s*>", m))
        if o != f:
            out.append((g, o, f, 0)); mp = _sans_ilots(m) if mp is None else mp
            for n, a, b in _bornes_points(t):
                s = mp[a:b]; o2, f2 = len(re.findall(rf"(?i)<{g}[\s>]", s)), len(re.findall(rf"(?i)</{g}\s*>", s))
                if o2 != f2: out.append((g, o2, f2, n))
    return out


def equilibrer(t):
    """Réparation sûre des balises de bloc déséquilibrées : un bloc ouvert dans un point est fermé avant le titre du point suivant ;
    une fermante sans ouvrante est retirée. N'agit que si le fichier est globalement déséquilibré ; renvoie le texte d'origine si le
    résultat n'est pas équilibré. Retour : (texte, journal)."""
    if not any(n == 0 for *_, n in desequilibres(t)): return t, []
    m = _inerte(t); P = _bornes_points(t)
    if not P: return t, []
    bornes = [a for _, a, _ in P]                          # débuts des points : seule frontière sûre (la fin du point 14 ne l'est pas)
    ev = [(b, 0, "limite", None) for b in bornes]
    for x in re.finditer(r"(?i)<(/?)(%s)\b[^>]*>" % "|".join(BALISES), m):
        ev.append((x.start(), 1, "ferme" if x.group(1) else "ouvre", x))
    ev.sort(key=lambda e: (e[0], e[1]))
    pile, ins, sup, sec, J = [], [], [], -1, []
    # Un îlot du Cours Flash (class="ilot") enjambe plusieurs points : il est traité comme un enveloppant (jamais fermé à une limite de point),
    # et sa fermante referme d'abord les blocs restés ouverts à l'intérieur.
    for pos, _, k, x in ev:
        if k == "limite":
            while pile and pile[-1][2] >= 0:
                g, p0, s0 = pile.pop(); ins.append((pos, f"</{g}>")); J.append(f"<{g}> ouvert l.{bus.ligne(t, p0)} fermé avant le point suivant")
            sec = bornes.index(pos); continue
        g = x.group(2).lower()
        if k == "ouvre": pile.append((g, x.start(), -2 if RX_ILOT.match(m, x.start()) else sec)); continue
        if pile and pile[-1][0] == g: pile.pop(); continue
        cible = next((q for q in reversed(pile) if q[0] == g), None)
        if cible and (cible[2] >= 0 or cible[2] == -2 or sec == len(P) - 1):     # un enveloppant (ouvert avant le point 1) ne se ferme qu'au dernier point ou après
            while pile[-1][0] != g:
                g2, p0, _ = pile.pop(); ins.append((x.start(), f"</{g2}>")); J.append(f"<{g2}> ouvert l.{bus.ligne(t, p0)} fermé avant </{g}>")
            pile.pop(); continue
        sup.append((x.start(), x.end())); J.append(f"</{g}> orpheline retirée l.{bus.ligne(t, x.start())}")
    if not J: return t, []
    grp = {}
    for p_, s in ins: grp[p_] = grp.get(p_, "") + s           # fermantes groupées dans l'ordre de dépilement (</table></div>)
    ops = [(p_, p_, s) for p_, s in grp.items()] + [(a, b, "") for a, b in sup]
    out = t
    for a, b, s in sorted(ops, key=lambda o: (o[0], o[1]), reverse=True): out = out[:a] + s + out[b:]
    if any(n == 0 for *_, n in desequilibres(out)): return t, ["réparation des balises impossible sans ambiguïté : correction à la main"]
    return out, J


def couper_lignes(t, limite=10000):
    """Coupe les lignes > limite aux fins de blocs (</p>, </li>, </tr>, </div>…) hors CSS, modèles et scripts : rendu inchangé."""
    if all(len(l) <= limite or RX_LIGNE_OK.search(l) for l in t.split("\n")): return t, []
    m = _inerte(t); coupes = []; J = []; debut = 0
    for l in t.split("\n"):
        fin = debut + len(l)
        if len(l) > limite and not RX_LIGNE_OK.search(l):
            n0 = len(coupes)
            coupes += [x.end() for x in re.finditer(r"(?i)</(?:p|li|tr|div|ul|ol|table|h[1-6]|details|summary|section)>|<!--/algo-->", m[debut:fin]) if x.end() < len(l)]
            coupes[n0:] = [debut + c for c in coupes[n0:]]
            J.append(f"ligne {bus.ligne(t, debut)} ({len(l)} caractères) coupée en {len(coupes) - n0 + 1}")
        debut = fin + 1
    out = t
    for c in sorted(set(coupes), reverse=True): out = out[:c] + "\n" + out[c:]
    return out, J


def reparer(t, flash=False):
    """Réparations mécaniques sûres de fin de duo : rendu des algorithmes (une ligne par élément), CSS brain-vial (et brain-flash en mode Flash),
    balises de bloc, lignes longues."""
    J = []; t2 = corriger(t, {"flash": flash})
    if t2 != t: J.append("algorithme(s) rendu(s) et CSS brain-vial" + (" / brain-flash" if 'id="brain-flash"' in t2 else "") + " posée(s)")
    t2, j = equilibrer(t2); J += j
    t2, j = couper_lignes(t2); J += j
    return t2, J


RX_CH = re.compile(r"(?i)\bAIPS\b|swissmedic|\.ch\b|\bSGGG\b|\bSSGO\b|\bHUG\b|\bCHUV\b|insel|\bUSZ\b|kantonsspital|\bOFSP\b|\bBAG\b|suisse|swiss|schweiz"
                   r"|\bSSED\b|\bSSCC\b|\bSVGO\b|\bSSMIG\b|\bSGAIM\b|plan de vaccination|Unisanté")
RX_EU = re.compile(r"(?i)\bESC\b|ESHRE|\bEMAS\b|\bESE\b|\bERS\b|\bESRS\b|\bNICE\b|AWMF|\bHAS\b|\bNVOG\b|europ|\bENETS\b|\bEAU\b|\bEASD\b|\bESO\b"
                   r"|\bEMA\b|\bDGGG\b|onkopedia|\bBMJ\b|\.eu\b|\.de\b|\.fr\b|\.uk\b|\.nl\b|\.it\b|\.at\b|royaume-uni|france|deutsch|nederland|ital|\bESMO\b|\bEULAR\b|\bERA\b")
RX_ETIQ = re.compile(r"(?i)hors AIPS|à valider")
# Donnée LOCALE : recommandation de prise en charge, organisation, filière, remboursement, vaccination (les résultats d'essais restent universels)
RX_RECO = re.compile(r"(?i)recommand|préconis|en première intention|en 1re intention|en deuxième intention|en première ligne|rembours|\bLiMA\b|liste des spécialités"
                     r"|filière|transf[eé]r|vaccin|dépistage organisé|plan de")


def origine(ref):
    """Origine d'une entrée de bibliographie : CH (suisse), EU (européenne) ou INT (autre, internationale)."""
    ref = ref.split(" — ")[0]                                  # notice seule : la note de lecture (« pas comme référence suisse ») ne compte pas
    return "CH" if RX_CH.search(ref) else "EU" if RX_EU.search(ref) else "INT"


def cellule_verbale(ph):
    """Phrase de cellule verbale au sens de la directive : forme finie (une consigne à l'infinitif sans sujet ne suffit pas)."""
    import familles as FA
    mots = re.findall(r"[a-zà-ÿœ]+(?:['’][a-zà-ÿ]+)?", ph.lower())
    if mots and "→" not in ph and FA._infinitif(mots[0], FA.verbes()):
        reste = ph.split(None, 1)[1] if " " in ph.strip() else ""
        return bool(reste) and FA.verbale(reste) and not FA._infinitif((re.findall(r"[a-zà-ÿœ]+", reste.lower()) or [""])[0], FA.verbes())
    return FA.verbale(ph)


# ───────────────────────── analyse ─────────────────────────
def _orthogonalite(seg, a, ha, dol):
    """D2/D3 : un algorithme n'a que des cases et losanges reliés par des traits horizontaux et verticaux."""
    for m in re.finditer(r"(?is)<circle\b|<ellipse\b|border-radius\s*:\s*50%", seg):
        dol("D2", a + m.start(), "GRAVE", "cercle ou ellipse dans l'arbre décisionnel", "remplacer par une case rectangulaire ou un losange")
    for m in re.finditer(r'(?is)<line\b[^>]*>', seg):
        g = {k: float(v) for k, v in re.findall(r'\b(x1|y1|x2|y2)="(-?[\d.]+)"', m.group(0))}
        if len(g) == 4 and g["x1"] != g["x2"] and g["y1"] != g["y2"]:
            dol("D3", a + m.start(), "GRAVE", "segment oblique", "tracer des traits horizontaux et verticaux uniquement (coude à angle droit)")
    for m in re.finditer(r'(?is)<path\b[^>]*\bd="([^"]*)"', seg):
        if re.search(r"[^MmHhVvZz\d\s.,-]", m.group(1)):
            dol("D3", a + m.start(), "GRAVE", "chemin non orthogonal (courbe ou diagonale)", "chemin en M/H/V seulement")
    if re.search(r"(?i)rotate\(\s*-?(?!0|90|180|270)\d", seg) and "algo" in seg:
        dol("D3", ha, "MOYEN", "élément pivoté à un angle non droit", "aucun trait pivoté")


RX_CLIC = re.compile(r'class="(?:sc dx|dx|fxw)"')            # déclencheurs de fenêtre cliquable (span.dx, span.sc.dx, div.fxw)
RX_VOISINES = re.compile(r"(?is)<(h4|h5|h6|b|strong|summary|th|p|li)\b[^>]*>\s*(?:<(?:b|strong|em)>\s*)?"
                         r"(notions?\s+voisines?|diagnostics?\s+différentiels?|diagnostic\s+différentiel)")


def _fenetres_modales(seg):
    """Contenus des fenêtres (span.dxc et div.fx) d'un segment."""
    out = [x for x in re.findall(r'(?is)<span class="dxc">(.*?)</span></span>', seg)]
    for x in re.finditer(r'(?is)<div\b[^>]*\bclass="fx"[^>]*>', seg):
        b = _fermeture(seg, x.start(), "div"); out.append(seg[x.end():b] if b else seg[x.end():])
    return out


def flash(t, nom):
    """Contrôles du COURS FLASH (harnais/etat/COURS_FLASH.md) : volume, îlots, fenêtres modales, tableau de syndrome, algorithme du point 11.
    Retour (doléances, mesures). Un défaut sans conséquence d'apprentissage reste MOYEN (avertissement)."""
    me = sys.modules[__name__]; D = []; S = bus.sections(t); M = {}
    h = lambda a: t.find(">", a) + 1
    dol = lambda code, pos, sev, constat, corr, ex="agent", preuve="": D.append(bus.doleance(me, code, nom, bus.ancre(t, pos, preuve), sev, constat, corr, ex, preuve))
    a0, f0 = bus.bornes_cours(t)
    # ── volume (fichier entier)
    o = len(t.encode()); M["octets"] = o; M["ko"] = round(o / KO, 1)
    if o > FLASH_MAX:
        dol("V1", 0, "GRAVE", f"volume {o / KO:.0f} Ko > 280 Ko (bande Flash 100–280, visé 100–200)",
            "contracter : le détail secondaire descend dans une fenêtre, l'inutile est retiré (retrait déclaré) ; aucune redite ; sigles et CSS non dupliqués")
    elif o > FLASH_VISE:
        dol("V2", 0, "MOYEN", f"volume {o / KO:.0f} Ko > 200 Ko (visé 100–200 Ko)", "alléger le corps : détails en fenêtres, redites retirées")
    elif o < FLASH_MIN:
        dol("V3", 0, "MOYEN", f"volume {o / KO:.0f} Ko < 100 Ko : fond des 14 points peut-être insuffisant", "vérifier l'exigence de la grille point par point")
    # ── notions voisines / diagnostic différentiel en bloc dans le corps
    for m in RX_VOISINES.finditer(t, a0, f0):
        if bus.dans_fenetre(t, m.start()): continue
        suite = t[m.end():m.end() + 2500]; coupe = re.search(r"(?i)<h3\b|<h4\b", suite); suite = suite[:coupe.start()] if coupe else suite
        bloc = next((x for x in re.finditer(r"(?i)<(?:ul|ol|table)\b", suite) if not bus.dans_fenetre(t, m.end() + x.start())), None)
        if not bloc: continue
        replie = m.group(1).lower() == "summary"
        dol("N1", m.start(), "MOYEN" if replie else "GRAVE", f"bloc « {m.group(2)} » dans le corps du cours" + (" (replié)" if replie else ""),
            "ranger le diagnostic différentiel utile dans une fenêtre cliquable (div.fxw > div.fx ou span.dx) ; retirer le reste", preuve=m.group(2))
    # ── îlots
    I = ilots(t); M["ilots"] = len(I)
    def ilot_de(n):
        if n not in S: return None
        p = S[n][0]; cs = [x for x in I if x[0] < p and (x[1] or len(t)) > p]
        return max(cs, key=lambda x: x[0]) if cs else None
    if not I:
        dol("I1", a0, "GRAVE", "aucun îlot (parties 1–4, 5–6 et reste replié attendus)",
            "envelopper : <section class=\"ilot\" data-ilot=\"1-4\">points 1 à 4</section>, <section class=\"ilot\" data-ilot=\"5-6\">points 5 et 6</section>, "
            "puis chaque point 7 à 14 dans <details class=\"ilot\"><summary><h3 …>N. …</h3></summary>…</details> (gabarit : harnais/brain/gabarit_flash.html)")
    else:
        for code, grp in (("I2", (1, 2, 3, 4)), ("I3", (5, 6))):
            ils = {n: ilot_de(n) for n in grp if n in S}
            hors = [n for n, x in ils.items() if x is None]
            if hors:
                dol(code, h(S[hors[0]][0]), "GRAVE", f"point(s) {hors} hors îlot (parties {grp[0]}–{grp[-1]} attendues dans un même îlot)",
                    f"envelopper les points {grp[0]} à {grp[-1]} dans un même <section class=\"ilot\">")
            elif len({x[0] for x in ils.values()}) > 1 or (code == "I3" and ilot_de(1) and ils and ilot_de(1)[0] == next(iter(ils.values()))[0]):
                dol(code, h(S[grp[0]][0]) if grp[0] in S else a0, "MOYEN", f"parties {grp[0]}–{grp[-1]} non regroupées dans un îlot propre",
                    f"un îlot pour les points {grp[0]} à {grp[-1]}, distinct des autres groupes")
        for n in range(7, 15):
            x = ilot_de(n)
            if n not in S: continue
            if x is None or x[2] != "details":
                dol("I4", h(S[n][0]), "MOYEN", f"point {n} non replié", "le point dans <details class=\"ilot\"><summary><h3 …>…</h3></summary>…</details>")
            elif re.search(r"(?i)(?:^|\s)open(?:\s|=|$)", x[3]):
                dol("I4", h(S[n][0]), "MOYEN", f"point {n} déplié par défaut (attribut open)", "retirer l'attribut open : le reste est contracté")
        for a, b, g, at in I:
            st = " ".join(re.findall(r'(?is)style="([^"]*)"', at))
            if b is None:
                dol("I6", a, "GRAVE", f"îlot <{g}> jamais refermé", "refermer l'îlot (</" + g + ">) avant l'îlot suivant"); continue
            if re.search(r"(?i)(?:^|;)\s*(?:width|max-width|margin(?:-left|-right)?|padding(?:-left|-right)?|float)\s*:|text-align\s*:\s*(?!justify)", st):
                dol("I6", a, "MOYEN", "style en ligne sur l'îlot (largeur, marge ou alignement)", "retirer le style en ligne : la CSS brain-flash fixe largeur et justification", preuve=st[:80])
            for y in re.finditer(r'(?is)<p\b[^>]*style="[^"]*text-align\s*:\s*(?!justify)[^"]*"', t[a:b]):
                dol("I6", a + y.start(), "MOYEN", "paragraphe d'îlot non justifié (style en ligne)", "retirer text-align du paragraphe"); break
            vis = len(bus.texte_visible(nu_(t[a:b])))
            if vis > ILOT_SATURE:
                dol("I7", h(a), "MOYEN", f"îlot saturé : {vis} caractères visibles (> {ILOT_SATURE})", "rabattre listes, méthodes et détails dans des fenêtres ; aucune redite")
        if not re.search(r'(?is)<style id="brain-flash">.*?\.ilot\{[^}]*border[^}]*\}.*?text-align:justify', t):
            dol("I5", a0, "MOYEN", "CSS brain-flash (bords d'îlot, justification, fenêtres modales) non posée",
                "lancer : python3 harnais/brain/circuit_vial.py reparer <fichier> --flash", "script")
    # ── fenêtres modales
    nclic = len(RX_CLIC.findall(t[a0:f0])); M["fenetres"] = nclic + t[a0:f0].count('class="algo-d"')
    if not M["fenetres"]:
        dol("W1", a0, "GRAVE", "aucune fenêtre cliquable : le détail reste dans le corps",
            "détails, listes, méthodes : fenêtres cliquables (span.dx en ligne, div.fxw > div.fx pour un tableau ou une méthode)")
    sympt_ok = 0
    if 5 in S:
        sympt_ok += len(RX_CLIC.findall(t[S[5][0]:S[5][1]]))
    syn = []
    if 7 in S:
        a, f = S[7]; seg = t[a:f]
        ts = [m for m in re.finditer(r"(?is)<(?:b|strong|h4|td|th)[^>]*>\s*(?:<(?:b|strong|em)>\s*)?(7\.\d+)\.?\s*(?:</(?:b|strong|em)>)?\s*([^<]*)", seg)
              if not bus.dans_fenetre(t, a + m.start())]
        for k, m in enumerate(ts):
            ch = seg[m.start():ts[k + 1].start() if k + 1 < len(ts) else len(seg)]; pos = a + m.start(); titre = (m.group(1) + " " + m.group(2)).strip()
            tabs = [x for w in _fenetres_modales(ch) for x in re.findall(r"(?is)<table\b.*?</table>", w)]
            bon = None
            for tb in tabs:
                tete = re.search(r"(?is)<tr\b[^>]*>(.*?)</tr>", tb); cols = re.findall(r"(?is)<t[hd]\b[^>]*>(.*?)</t[hd]>", tete.group(1)) if tete else []
                cols = [bus.texte(c).lower() for c in cols]
                if len(cols) == 2 and "sympt" in cols[0] and "signe" in cols[1]: bon = tb; break
                if any("sympt" in c for c in cols) and any("signe" in c for c in cols):
                    dol("W6", pos, "MOYEN", f"tableau du syndrome « {titre[:50]} » à {len(cols)} colonnes", "deux colonnes exactement : Symptômes fonctionnels | Signes physiques", preuve=titre); bon = tb; break
            syn.append(bool(bon))
            if not bon:
                dol("W5", pos, "MOYEN", f"syndrome « {titre[:50]} » sans fenêtre à tableau « symptôme | signes physiques »",
                    "intitulé cliquable (div.fxw) ouvrant une fenêtre : tableau à 2 colonnes Symptômes fonctionnels | Signes physiques (sous-cellules span.sc.dx)", preuve=titre)
                continue
            lignes = re.findall(r"(?is)<tr\b[^>]*>(.*?)</tr>", bon)[1:]
            cl1 = sum(1 for l in lignes if RX_CLIC.search((re.findall(r"(?is)<td\b[^>]*>(.*?)</td>", l) or [""])[0]))
            sympt_ok += cl1
            if lignes and not cl1:
                dol("W3", pos, "MOYEN", f"symptômes du syndrome « {titre[:50]} » non cliquables", "chaque symptôme : span.dx avec sa fenêtre (caractère, durée, valeur d'orientation)", preuve=titre)
        M["syndromes_tableau"] = sum(syn)
        if syn and not any(syn):
            dol("W5", h(a), "GRAVE", "aucun syndrome n'ouvre de fenêtre à tableau « symptôme | signes physiques »",
                "chaque « 7.n Syndrome de … » : div.fxw > div.fx contenant le tableau à 2 colonnes (gabarit : harnais/brain/gabarit_flash.html)")
    if (5 in S or 7 in S) and not sympt_ok:
        dol("W3", h(S[5][0] if 5 in S else S[7][0]), "GRAVE", "aucun symptôme cliquable (points 5 et 7)",
            "lister les symptômes simplement, chacun cliquable (span.dx) avec l'information utile dans sa fenêtre")
    if 6 in S:
        a, f = S[6]; seg = t[a:f]; nc = len(RX_CLIC.findall(seg)); M["signes_cliquables"] = nc
        if not nc:
            dol("W4", h(a), "GRAVE", "examen clinique sans signe cliquable", "énumérer les signes ; chacun cliquable : fenêtre « comment le rechercher, manœuvre »")
        else:
            sans = [w for w in _fenetres_modales(seg) if not RX_TECH.search(bus.texte(w))]
            if sans: dol("W4", h(a), "MOYEN", f"{len(sans)} fenêtre(s) de signe sans technique de recherche", "dire comment rechercher le signe (position, geste, manœuvre)",
                         preuve=bus.texte(sans[0])[:80])
    if 11 in S:
        a, f = S[11]; seg = t[a:f]
        _orthogonalite(seg, a, h(a), dol)
        nc = len(re.findall(r'class="algo-n ', seg)); nd = len(re.findall(r'class="algo-d"', seg))
        if nc and nd < nc / 2:
            dol("W7", h(a), "MOYEN", f"algorithme d'urgence : {nd} case(s) cliquable(s) sur {nc}", "donner un « detail » (fenêtre) aux cases d'action et de décision")
    for m in re.finditer(r'(?is)<span class="df">(.*?)</span>', t[a0:f0]):
        n = len(re.findall(r"[\wÀ-ÿœ'’-]+", bus.texte(m.group(1))))
        if n > 40:
            dol("W8", a0 + m.start(), "MOYEN", f"précision de survol de {n} mots (> 40)", "survol réservé aux précisions courtes : passer en fenêtre cliquable (span.dx)",
                preuve=bus.texte(m.group(1))[:80]); break
    return D, M


def nu_(h):
    return re.sub(r"(?is)<(script|style|template)\b.*?</\1>", " ", h)


def analyser(t, nom, opt=None):
    me = sys.modules[__name__]; D = []; S = bus.sections(t); M = {}
    h = lambda a: t.find(">", a) + 1                     # ancre dans le point (après l'ouverture du <h3 id="…-pN">)
    dol = lambda code, pos, sev, constat, corr, ex="agent", preuve="": D.append(bus.doleance(me, code, nom, bus.ancre(t, pos, preuve), sev, constat, corr, ex, preuve))
    # ── point 10
    if 10 in S:
        a, f = S[10]; seg = t[a:f]; M["algo"] = seg.count('data-brain="algo"')
        if RX_MODELE.search(RX_BLOC.sub("", seg)):
            dol("D6", h(a), "GRAVE", "modèle d'algorithme non rendu", "lancer : python3 harnais/brain/circuit_vial.py algo <fichier> --appliquer", "script")
        elif 'data-brain="algo"' not in seg:
            dol("D1", h(a), "GRAVE", "arbre décisionnel sans algorithme en cases" + (" (liste à puces)" if "<ul" in seg else ""),
                "écrire le modèle JSON de l'algorithme (cases, losanges de décision, liens Oui/Non, détail cliquable par case) dans "
                "<template class=\"algo-modele\"> au point 10, puis lancer circuit_vial.py algo <fichier> --appliquer ; garder la liste en texte si elle apporte un détail")
        else:
            nc = len(re.findall(r'class="algo-n ', seg)); nl = len(re.findall(r'class="algo-n lo', seg)); nd = len(re.findall(r'class="algo-d"', seg))
            M.update(cases=nc, losanges=nl, details=nd)
            if nc < 3 or nl == 0:
                dol("D4", h(a), "MOYEN", f"algorithme pauvre : {nc} case(s), {nl} losange(s)", "au moins 3 cases et un losange de décision par question discriminante")
            if nd < nc / 2:
                dol("D5", h(a), "MOYEN", f"{nd} case(s) cliquable(s) sur {nc}", "donner un « detail » (fenêtre) aux cases d'action et de décision")
        _orthogonalite(seg, a, h(a), dol)
    # ── point 11
    if 11 in S:
        a, f = S[11]; seg = t[a:f]; tx = bus.texte(seg); low = tx.lower()
        if not re.search(r"(?is)<(?:b|strong)>[^<]{0,12}\bBut\b", seg):
            dol("E1", h(a), "GRAVE", "« But » absent de la prise en charge", "1- But (gras) : une phrase claire")
        if not re.search(r"(?is)<(?:b|strong)>[^<]{0,12}Moyens et méthodes", seg):
            dol("E2", h(a), "GRAVE", "« Moyens et méthodes » absent", "2- Moyens et méthodes (gras), puis A- En urgences, B- Hors urgences")
        sans_urg = re.search(r"(?i)\ba\s*[-–—]\s*sans objet|aucune urgence propre|pas de situation d'urgence", low)
        iu = low.find("urgence"); ins = low.find("non-spécialiste") if "non-spécialiste" in low else low.find("non spécialiste"); iss = low.find("service spécialisé")
        if not sans_urg and (iu < 0 or ins < 0 or iss < 0 or not iu <= ins < iss):
            dol("E3", h(a), "GRAVE", "A- En urgences incomplet (urgence, puis « aux urgences par le non-spécialiste », puis « dans le service spécialisé »)",
                "écrire A- En urgences : algorithme d'urgence ; aux urgences par le non-spécialiste (premiers temps avant transfert) ; dans le service spécialisé (actes chronologiques cliquables) ; ou « A- Sans objet : aucune urgence propre à ce SSP » si c'est vrai")
        ih = low.find("hors urgence"); ig = low.find("mesures générales"); isp = low.find("spécifique", max(ig, 0))
        if ih < 0 or ig < 0 or isp < 0:
            dol("E4", h(a), "GRAVE", "B- Hors urgences incomplet (mesures générales puis mesures spécifiques)",
                "B- Hors urgences (gras) : mesures générales ; mesures spécifiques par priorité décroissante (pharmacologiques, puis non pharmacologiques : social, professionnel, ergothérapie)")
        else:
            ip = low.find("pharmacolog", isp); inp = low.find("non pharmacolog", isp)
            if ig > isp or (inp >= 0 and ip == inp + 4):
                dol("E6", h(a), "MOYEN", "ordre B non respecté", "mesures générales d'abord ; pharmacologique avant non pharmacologique")
        if iss >= 0 and not sans_urg:
            m = re.search(r"(?i)service spécialisé", seg); fin = re.search(r"(?i)hors urgence", seg[m.end():]) if m else None
            zone = seg[m.end():m.end() + fin.start()] if m and fin else ""
            if m and zone.count('class="dx') + zone.count('class="tm') < 2:
                dol("E5", a + m.start(), "MOYEN", "actes du service spécialisé non cliquables", "chaque acte ou geste : <span class=\"dx\"> cliquable avec sa fenêtre de détails")
        if not sans_urg and 'data-brain="algo"' not in seg and not RX_MODELE.search(seg):
            dol("E8", h(a), "GRAVE", "A- En urgences sans algorithme de prise en charge d'urgence en cases",
                "écrire au début de A- un modèle <template class=\"algo-modele\"> (cases et losanges, détails en phrases) puis lancer circuit_vial.py algo <fichier> --appliquer")
        h3 = re.match(r'(?is)<h3\b([^>]*)>', t[a:a + 300])
        if not (h3 and re.search(r'id="[^"]*-p11"', h3.group(1))):
            dol("E7", h(a), "MOYEN", "titre du point 11 sans identifiant …-p11 : la bande colorée ne s'applique pas", "donner au <h3> l'identifiant <monographie>-p11")
        elif not re.search(r'(?is)<style id="brain-vial">.*?h3\[id\$="-p11"\]\{[^}]*background[^}]*underline', t):
            dol("E7", h(a), "MOYEN", "bande colorée du titre « Prise en charge » non posée", "lancer : python3 harnais/brain/circuit_vial.py algo <fichier> --appliquer (pose la CSS brain-vial)", "script")
    # ── point 7
    if 7 in S:
        a, f = S[7]; seg = t[a:f]
        # Intitulés « 7.n » en gras, en titre h4 ou en cellule de tableau (la directive vaut « y compris dans le tableau »).
        ts = list(re.finditer(r"(?is)<(?:b|strong|h4|td|th)[^>]*>\s*(?:<(?:b|strong|em)>\s*)?(7\.\d+)\.?\s*(?:</(?:b|strong|em)>)?\s*([^<]*)", seg)); M["syndromes"] = len(ts)
        if not ts:
            dol("Q0", h(a), "GRAVE", "aucun syndrome numéroté « 7.n Syndrome de … » au point 7",
                "structurer le point 7 en syndromes « 7.1 Syndrome de … », chacun avec « Symptômes fonctionnels » et « Signes physiques » en sous-cellules cliquables")
        for k, m in enumerate(ts):
            ch = seg[m.start():ts[k + 1].start() if k + 1 < len(ts) else len(seg)]; pos = a + m.start(); titre = m.group(1) + " " + m.group(2)
            ot = seg.rfind("<table", 0, m.start())
            if ot >= 0 and seg.rfind("</table>", 0, m.start()) < ot:          # syndrome en ligne de tableau : les en-têtes de colonnes valent intitulés
                tete = bus.texte(seg[ot:seg.find("</tr>", ot) if "</tr>" in seg[ot:] else ot + 2000]).lower()
                fin_t = seg.find("</table>", m.start()); ch = ch[:fin_t - m.start()] if fin_t > 0 else ch
                ch = ("symptômes fonctionnels " if "symptômes fonctionnels" in tete else "") + ("signes physiques " if "signes physiques" in tete else "") + ch
            if re.search(r"(?i)intitulé de travail|à vérifier", m.group(2)):
                dol("Q6", pos, "GRAVE", f"intitulé « {titre.strip()[:60]} » non documenté", "intitulé tel que documenté dans les références internationales (source lue), sans mention « intitulé de travail »", preuve=titre)
            if not re.match(r"\s*Syndrome\b", m.group(2), re.I):
                dol("Q1", pos, "MOYEN", f"intitulé « {titre.strip()[:60]} » sans « Syndrome »", "« 7.n Syndrome de … » selon l'intitulé international documenté", preuve=titre)
            if "symptômes fonctionnels" not in ch.lower():
                dol("Q2", pos, "GRAVE", "« Symptômes fonctionnels » absent" + (" (« Signes fonctionnels » à renommer)" if "signes fonctionnels" in ch.lower() else ""),
                    "« Symptômes fonctionnels : » suivi des symptômes en puces", preuve=titre)
            ip = ch.lower().find("signes physiques")
            if ip < 0:
                dol("Q3", pos, "GRAVE", "« Signes physiques » absent", "« Signes physiques : région / région » avec sous-cellules cliquables", preuve=titre); continue
            sc = re.findall(r'(?is)<span class="sc dx">.*?<span class="dxc">(.*?)</span></span>', ch[ip:])
            if not sc:
                dol("Q4", pos, "GRAVE", "signes physiques sans sous-cellules cliquables",
                    "chaque signe : <span class=\"sc dx\"><input type=\"checkbox\" id=\"…\"><label class=\"dxt\" for=\"…\">signe</label><span class=\"dxc\">comment le rechercher, manœuvre, valeur</span></span>", preuve=titre)
            for x in sc:
                if not RX_TECH.search(bus.texte(x)):
                    dol("Q5", pos, "MOYEN", "fenêtre de signe sans technique de recherche", "dire textuellement comment rechercher le signe (position, geste, manœuvre)", preuve=bus.texte(x)[:80])
    # ── registre universitaire et clarté
    import familles as FA
    vues = {}; nL = 0
    for pa, pf, inner in bus.blocs(t, None, None, ("p", "li")):
        if re.search(r"(?i)<(?:p|li|ul|ol)\b", inner) or bus.dans_fenetre(t, pa): continue
        tag = t[pa + 1:pa + 3].lower()
        for ph in bus.phrases(bus.texte_visible(re.sub(r"(?is)<template\b.*?</template>", " ", inner))):
            mots = re.findall(r"[\wÀ-ÿœŒ'’-]+", ph); n = len(mots); nL += 1
            if n < 3: continue
            m = RX_FAIBLE.search(ph)
            if m: dol("L1", pa, "MOYEN" if m.group(0).strip().lower() in ("voici", "voilà") else "GRAVE", f"tournure faible ou familière « {m.group(0).strip()} »", "registre universitaire soutenu : tournure impersonnelle ou passive, terme dédié, sans tutoiement", preuve=ph[:160])
            if n > 40: dol("L2", pa, "GRAVE", f"phrase de {n} mots (> 40)", "scinder en phrases complètes et claires, ou passer l'énumération en puces", preuve=ph[:160])
            if tag == "p " or tag.startswith("p>") or tag == "p\t":
                if n >= 12 and not m and not FA.verbale(ph) and not RX_SV2.search(ph): dol("L3", pa, "GRAVE", "phrase nominale sans verbe", "phrase complète : sujet, verbe, complément", preuve=ph[:160])
            k = re.sub(r"\W+", " ", ph.lower()).strip()
            if n >= 6 and k in vues: dol("L4", pa, "GRAVE", "phrase répétée à l'identique", "supprimer la redite (la notion reste une fois)", preuve=ph[:160])
            vues[k] = 1
            pleins = [w.lower() for w in mots if len(w) >= 7]
            rep = sorted({w for w in pleins if pleins.count(w) >= 3})
            if rep: dol("L4", pa, "MOYEN", f"mot répété dans la phrase : {', '.join(rep)}", "varier par un terme dédié ou un pronom", preuve=ph[:160])
    M["phrases_registre"] = nL
    # ── cellules de tableau (directive : phrases complètes et puces « y compris dans les cellules ») ; 1re colonne et en-têtes exemptés
    a0, f0 = bus.bornes_cours(t); nC = 0
    for mt in re.finditer(r"(?is)<table\b.*?</table>", t[a0:f0]):
        for mr in re.finditer(r"(?is)<tr\b[^>]*>(.*?)(?=<tr\b|</table>)", mt.group(0)):
            cel = re.split(r"(?i)<td\b[^>]*>", mr.group(1))[1:]
            for k, c in enumerate(cel):
                if k == 0: continue
                pos = a0 + mt.start() + mr.start(1) + mr.group(1).find(c[:40])
                if bus.dans_fenetre(t, pos): continue
                hors_liste = re.sub(r"(?is)<ul\b.*?</ul>|<ol\b.*?</ol>", " ", re.sub(r"(?is)</td>.*", "", c))
                qs = [x for x in bus.phrases(bus.texte_visible(hors_liste)) if x.rstrip().endswith("?")]
                if len(qs) >= 2:
                    dol("L5", pos, "MOYEN", f"{len(qs)} questions juxtaposées dans une cellule", "une puce <li> par question dans la cellule", preuve=" ".join(qs)[:160]); continue
                for ph in bus.phrases(bus.texte_visible(hors_liste)):
                    mots = re.findall(r"[\wÀ-ÿœŒ'’-]+", ph); nC += 1
                    if len(mots) < 6 or re.match(r"(?i)\s*(symptômes fonctionnels|signes physiques)\b", ph): continue
                    if not cellule_verbale(ph):
                        dol("L5", pos, "GRAVE", "cellule nominale (fragment ou énumération sans verbe)",
                            "phrase complète (sujet, verbe, complément) ou énumération en puces <ul><li> dans la cellule", preuve=ph[:160]); break
    M["phrases_cellules"] = nC
    # ── intégrité HTML (même mesure que controle_lot, localisée au point fautif) et lignes longues
    for tag, o, f_, n_ in desequilibres(t):
        dol("H1", S[n_][0] if n_ in S else 0, "GRAVE", f"balises <{tag}> déséquilibrées {'au point ' + str(n_) if n_ else 'dans le fichier'} ({o} ouvertes / {f_} fermées)",
            "lancer : python3 harnais/brain/circuit_vial.py reparer <fichier> (fermeture en fin de point, fermante orpheline retirée), puis relire le point", "script")
    for i, l in enumerate(t.split("\n")):
        if len(l) > 10000 and not RX_LIGNE_OK.search(l):
            dol("H2", sum(len(x) + 1 for x in t.split("\n")[:i]), "GRAVE", f"ligne {i + 1} de {len(l)} caractères (> 10 000)",
                "lancer : python3 harnais/brain/circuit_vial.py reparer <fichier> (coupe aux fins de blocs)", "script")
    # ── origine des sources (précision de Vial du 28.10.2026) : l'universel (définitions, sémiologie, physiopathologie, critères
    #    internationaux, dénominations des syndromes) accepte une source sérieuse non suisse, datée ; le LOCAL (prise en charge, doses,
    #    organisation des soins, prévention et vaccination, remboursements, filières) exige la Suisse d'abord, sinon l'Europe, sinon une source
    #    internationale étiquetée « hors AIPS » ou « à valider ».
    REF = {k: bus.texte(v) for k, v in re.findall(r'(?is)id="sb-(\d+)"[^>]*>(.*?)(?:<a href="#">fermer|</li>|</div>)', t)}
    for n, sev in ((11, "GRAVE"), (12, "GRAVE"), (2, "MOYEN")):
        if n not in S: continue
        for pa, pf, inner in bus.blocs(t, S[n][0], S[n][1]):
            for ph in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý])", inner):
                ns = re.findall(r'#sb-(\d+)"', ph)
                if not ns or not RX_RECO.search(bus.texte_visible(ph)) or RX_ETIQ.search(bus.texte(ph)): continue
                if all(origine(REF.get(k, "")) == "INT" for k in ns):
                    dol("O1", pa, sev, f"donnée locale (point {n}) appuyée sur une source seulement internationale ({', '.join('S' + k for k in ns)})",
                        "source suisse (AIPS, société suisse) d'abord, sinon européenne ; à défaut, étiqueter « hors AIPS » ou « à valider » dans la phrase",
                        preuve=bus.texte_visible(ph)[:160])
    for pa, pf, inner in bus.blocs(t):                        # dose appuyée sur une source non suisse sans étiquette, où qu'elle soit
        for ph in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý])", inner):
            ns = re.findall(r'#sb-(\d+)"', ph)
            if ns and re.search(r"\d\s?(?:mg|µg|microgrammes?|g/j)\b", bus.texte_visible(ph)) and not RX_ETIQ.search(bus.texte(ph)) \
                    and all(origine(REF.get(k, "")) != "CH" for k in ns):
                dol("O2", pa, "GRAVE", "dose appuyée sur une source non suisse sans étiquette « hors AIPS »",
                    "dose lue dans l'AIPS suisse (renvoi [Sn] AIPS) ; sinon « hors AIPS, recommandation X ; à valider avec un spécialiste avant prescription »", preuve=bus.texte_visible(ph)[:160])
    # ── ids
    ids = re.findall(r'<input type="checkbox" id="([^"]+)"', t); vus = set()
    for i in ids:
        if i in vus: dol("R1", t.find(f'id="{i}"'), "GRAVE", f"identifiant dupliqué « {i} »", "rendre l'identifiant unique (préfixe du point)", preuve=i)
        vus.add(i)
    if (opt or {}).get("flash"):                             # Cours Flash : contrôles ajoutés (volume, îlots, fenêtres), jamais retirés
        D2, M2 = flash(t, nom); D += D2; M["flash"] = M2
    return D, M


if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
