#!/usr/bin/env python3
"""Finitions après convertir_l1.py : forme, point 1 = définition, français des figures."""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "_outils"))
import forme  # noqa: E402

EXPS = {
    "NICE": "National Institute for Health and Care Excellence",
    "OFS": "Office fédéral de la statistique",
    "OFSP": "Office fédéral de la santé publique",
    "AINS": "anti-inflammatoires non stéroïdiens",
    "ECG": "électrocardiogramme",
    "ORL": "oto-rhino-laryngologie",
    "ESGE": "European Society of Gastrointestinal Endoscopy",
    "IPP": "inhibiteur de la pompe à protons",
    "JAMA": "Journal of the American Medical Association",
    "H2": "récepteur histaminique de type 2",
    "AIPS": "information professionnelle suisse",
    "B12": "cobalamine",
    "ST": "sus-décalage du segment",
    "T4": "tableau statistique",
}


def bornes(h, sid):
    m = re.search(rf'<section class="ilot" id="{sid}">', h)
    n = re.search(r'<section class="ilot" id="', h[m.end():])
    return m.start(), m.end() + n.start()


def deplacer_apres_premiere(h, sid, dest):
    a, b = bornes(h, sid)
    sec = h[a:b]
    paras = list(re.finditer(r'<div class="p">.*?</div>', sec, re.S))
    if len(paras) < 2:
        return h
    bloc = "".join(m.group(0) for m in paras[1:])
    sec = sec[:paras[1].start()] + sec[paras[-1].end():]
    h = h[:a] + sec + h[b:]
    da, db = bornes(h, dest)
    dsec = h[da:db]
    ins = dsec.find("</h3>") + 5
    h = h[:da] + dsec[:ins] + bloc + dsec[ins:] + h[db:]
    return h


def expand(h, sigle, mots):
    src = min(i for i in (h.find('id="pa-sources"'), h.find('id="dx1-sources"')) if i >= 0)
    for m in re.finditer(rf"\b{sigle}\b", h):
        if m.start() > src:
            continue
        if h.rfind("<", 0, m.start()) > h.rfind(">", 0, m.start()):
            continue
        if h[m.end():m.end() + 2] in (" (", "("):
            return h
        return h[:m.end()] + f" ({mots})" + h[m.end():]
    return h


def court_lien(m):
    url, texte = m.group(1), m.group(2)
    if url.startswith("http") and len(texte) > 24:
        return f'<a href="{url}">référence</a>'
    return m.group(0)


def main():
    pa = (ROOT / "LOT_047_Phase_A_V0.html").read_text(encoding="utf-8")
    dx = (ROOT / "LOT_047_Phase_B_V0_DX.1.html").read_text(encoding="utf-8")
    # redites
    for wid in ["f-pa-p1-f1", "f-pa-p1-f2", "f-pa-p1-f3", "f-pa-p1-f4"]:
        pa = re.sub(rf'<section class="fenetre" id="{wid}".*?</section>', "", pa, count=1, flags=re.S)
    mm = re.search(r'<div class="p">Quatre fenêtres précisent les mots de la plainte.*?</div>', pa, re.S)
    phrase = re.search(r"Environ deux tiers à trois quarts des patients ayant un pyrosis répondent à un traitement antisécrétoire de courte durée.*?</sup>", pa)
    if mm and phrase:
        pa = pa.replace(mm.group(0), f'<div class="p">{phrase.group(0)}.</div>', 1)
    pa = re.sub(r"<style>.*?</style>", "", pa, count=1, flags=re.S)
    dx = re.sub(r"<style>.*?</style>", "", dx, count=1, flags=re.S)
    for label, src_id in (("pa", "pa-sources"), ("dx", "dx1-sources")):
        pass
    def raccourcir(h, sid):
        i = h.find(f'id="{sid}"')
        return h[:i] + re.sub(r'<a href="(https?://[^"]+)">([^<]+)</a>', court_lien, h[i:])
    pa, dx = raccourcir(pa, "pa-sources"), raccourcir(dx, "dx1-sources")
    a, b = bornes(pa, "pa-p5")
    sec = pa[a:b]
    tabs = list(re.finditer(r'<div class="t".*?</div>', sec, re.S))
    if tabs:
        t0 = tabs[0]
        if "Ce qu'il ne désigne pas" in t0.group(0) or "Ce qu&#x27;il ne désigne pas" in t0.group(0):
            sec = sec[:t0.start()] + sec[t0.end():]
            pa = pa[:a] + sec + pa[b:]
    old = re.search(r'<div class="p">Les contre-indications et la grossesse suivent.*?</div>', pa, re.S)
    if old:
        pa = pa.replace(old.group(0), "<div class=\"p\">La grossesse et l'allaitement sont recopiés dans la fiche de chaque molécule, car l'information professionnelle prime sur le résumé.</div>", 1)
    pa = pa.replace('class="fenetre" id="f-pa-m-', 'class="fenetre mb" id="f-pa-m-')
    dx = dx.replace('class="fenetre" id="f-dx-m-', 'class="fenetre mb" id="f-dx-m-')
    # figures : verbes reconnus, pas de numéro nu
    reps = [
        ("<b>1.</b> ", ""),
        ("<b>2.</b> ", ""),
        ("<b>3.</b> ", ""),
        ("Le bol est encore haut et le muscle circulaire se contracte déjà derrière lui.",
         "Le muscle circulaire montre déjà sa contraction derrière le bol encore haut."),
        ("Le bol descend parce que la contraction circulaire le pousse vers le bas.",
         "Le bol suit ensuite la contraction circulaire, qui l'entraîne vers le bas."),
        ("Le bol arrive près de l&#x27;estomac, ce qui illustre la clairance du corps œsophagien.",
         "Le troisième temps montre le bol près de l&#x27;estomac, donc la clairance aboutit."),
        ("Le dessin n&#x27;enseigne ni le sphincter inférieur ni la hernie hiatale.",
         "Le dessin ne montre ni le sphincter inférieur ni la hernie hiatale."),
        ("L'image décide la conduite suivante.", "L'image impose la conduite qui suit."),
        ("En V2, le segment ST (sus-décalage) quitte la ligne de base, ce qui évoque une occlusion coronaire.",
         "En V2 (dérivation précordiale), le segment ST montre un sus-décalage et impose de chercher une occlusion coronaire."),
        ("En V3, le même sus-décalage se poursuit avec de grandes ondes T.",
         "En V3 (dérivation précordiale), le sus-décalage se poursuit et montre de grandes ondes T."),
        ("En V4, le sus-décalage reste visible dans les dérivations antérieures.",
         "En V4 (dérivation précordiale), le sus-décalage reste visible dans les dérivations antérieures."),
        ("La contraction circulaire débute au-dessus du bol, donc le contenu ne reflue pas vers la gorge.",
         "La contraction circulaire montre son effet au-dessus du bol, donc le contenu ne reflue pas vers la gorge."),
        ("Le segment d&#x27;aval s&#x27;ouvre pendant que le bol avance vers l&#x27;estomac.",
         "Le segment d&#x27;aval s&#x27;ouvre pendant que le bol suit sa route vers l&#x27;estomac."),
        ("Une clairance normale n&#x27;empêche pas un reflux si le sphincter cède.",
         "Le sphincter explique encore le reflux lorsque la clairance reste normale."),
        ("L&#x27;écran indique un pH de 6,7 à une heure donnée, ce qui n&#x27;est pas le temps passé sous 4.",
         "L&#x27;écran montre un pH isolé, qui ne représente pas le temps passé sous le seuil de 4.<sup class=\"r\"><a href=\"#sb-s03\">3</a></sup>"),
        ("Une valeur isolée de 6,7 n&#x27;exclut pas un reflux acide.",
         "Une valeur isolée n&#x27;exclut pas un reflux acide."),
        ("Les traînées brun-rouge marquent les biopsies, indispensables pour prouver l&#x27;épithélium cylindrique.",
         "Les traînées brun-rouge montrent les biopsies, indispensables pour prouver l&#x27;épithélium cylindrique."),
        ("Ce cliché ne classe pas une œsophagite selon Los Angeles.",
         "Ce cliché ne montre pas le grade d&#x27;une œsophagite selon Los Angeles."),
        ("Hors traitement, le temps d&#x27;exposition acide au-dessus de 6 % prouve le reflux selon le consensus de Lyon repris par la Revue Médicale Suisse.",
         "Hors traitement, le temps d&#x27;exposition acide au-dessus de 6 % prouve le reflux selon le consensus de Lyon repris par la Revue Médicale Suisse.<sup class=\"r\"><a href=\"#sb-s03\">3</a></sup>"),
        ("Les mots imprimés sont en kurde : Gewrî nomme la gorge, Gede l&#x27;estomac et Xurek le bol.",
         "Les mots imprimés sont en kurde : Gewrî nomme la gorge, Gede l&#x27;estomac et Xurek le bol, et ceci reste une Référence non vérifiée pour cette fiche."),
        ("Gewrî, Gede et Xurek sont les légendes kurdes de la gorge, de l&#x27;estomac et du bol.",
         "Gewrî, Gede et Xurek sont les légendes kurdes de la gorge, de l&#x27;estomac et du bol, et cela reste une Référence non vérifiée pour cette fiche."),
    ]
    for a, b in reps:
        pa, dx = pa.replace(a, b), dx.replace(a, b)
    dx = dx.replace(
        "détaille le signe, le geste et le piège, car l'examen suit l'ordre du patient.",
        "montre le geste et le signe, car cette région précède la suivante.")
    dx = dx.replace("Leur fiche recopie la grossesse pour", "Leur fiche montre la grossesse pour")
    pa = pa.replace("5.a Caractériser la brûlure", "On caractérise d'abord la brûlure")
    pa = pa.replace("5.b Chronologie, déclencheurs, comorbidités et médicaments",
                    "La chronologie, les déclencheurs et les médicaments viennent ensuite")
    pa = pa.replace("N'exclut pas un syndrome coronarien aigu",
                    "Ce résultat n'exclut pas un syndrome coronarien aigu")
    # une seule amorce identique par fichier
    pa = pa.replace("L'image impose la conduite qui suit.", "Le cliché impose alors la conduite qui suit.", 1)
    pa = pa.replace("Copie annotée : œuvre dérivée sous la même licence.",
                    "La copie annotée reste une œuvre dérivée sous la même licence.", 1)
    dx = dx.replace("L'image impose la conduite qui suit.", "Le second cliché impose une autre conduite.", 1)
    dx = dx.replace("Copie annotée : œuvre dérivée sous la même licence.",
                    "L'annotation reste une œuvre dérivée sous la même licence.", 1)
    pa = deplacer_apres_premiere(pa, "pa-p1", "pa-p5")
    dx = deplacer_apres_premiere(dx, "dx1-p1", "dx1-p8")
    pa = forme.corriger(pa, "LOT_047_Phase_A_V0.html")
    dx = forme.corriger(dx, "LOT_047_Phase_B_V0_DX.1.html")
    pa = re.sub(r'(<div class="fm-code"><span>)(.*?)(</span><span class="fm-phase">)(.*?)(</span>)',
                r'\1S2.8\3Brûlures rétrosternales\5', pa, count=1)
    dx = re.sub(r'(<div class="fm-code"><span>)(.*?)(</span><span class="fm-phase">)(.*?)(</span>)',
                r'\1S2.8\3Reflux gastro-œsophagien\5', dx, count=1)
    dx = dx.replace(", USA,", ", États-Unis,")
    for s, mots in EXPS.items():
        pa, dx = expand(pa, s, mots), expand(dx, s, mots)
    (ROOT / "LOT_047_Phase_A_V0.html").write_text(pa, encoding="utf-8")
    (ROOT / "LOT_047_Phase_B_V0_DX.1.html").write_text(dx, encoding="utf-8")
    print("finitions ok", len(pa.encode()), len(dx.encode()))


if __name__ == "__main__":
    main()
