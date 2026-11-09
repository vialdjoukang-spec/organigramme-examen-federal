#!/usr/bin/env python3
"""Ajoute des fenêtres uniques et les tableaux de biologie, puis réassemble."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
PREU = ROOT / "preuves"
OUT = ROOT
ASM = ROOT / "outils" / "assembler.py"

def win(dx, i, label, text):
    pid = f"{dx}-g{i}"
    safe = (label.replace("&", "&amp;").replace("<", "&lt;"))
    return (
        f'<p><button type="button" class="fen" popovertarget="{pid}">{safe}</button>.</p>'
        f'<div id="{pid}" popover class="fenetre">'
        f'<button type="button" class="fermer" popovertarget="{pid}" popovertargetaction="hide">Fermer ✕</button>'
        f'<p>{text}</p></div>'
    )

def table(rows, caption):
    body = "".join(
        "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(*r) for r in rows
    )
    return (
        f'<p>{caption}</p>\n<div class="tw"><table><thead><tr>'
        '<th>Marqueur</th><th>Résultat lu</th><th>Interprétation</th><th>Hypothèse</th>'
        f'</tr></thead><tbody>{body}</tbody></table></div>\n'
    )

# --- biologie, phrases différentes par DX ---
TABLES = {}
TABLES["dx2"] = table([
    ("GGT", "Elle s'élève dès 60 à 70 g d'éthanol par jour pendant au moins quinze jours.",
     "Sensibilité et spécificité tournent autour de 60 %, et la valeur diminue de moitié tous les dix jours d'arrêt.",
     "On retient un excès prolongé, jamais le diagnostic à elle seule."),
    ("CDT", "Elle augmente dès environ 50 g par jour et redescend avec l'abstinence.",
     "Sensibilité d'environ 80 % chez l'homme et 60 % chez la femme, spécificité d'environ 90 %.",
     "L'excès chronique est plausible, sauf hépatopathie, grossesse, insuffisance rénale ou variante de la transferrine."),
    ("VGM", "Il ne bouge pas lors d'une alcoolisation aiguë.",
     "Sensibilité 25 % et spécificité 90 % sans carence vitaminique, après souvent plus de 100 g par jour pendant trois mois.",
     "Un volume haut suggère un usage long, un volume normal n'innocente pas."),
    ("PEth", "Aucun seuil n'a été ouvert dans les sources de ce fichier.",
     "On n'interprète pas un résultat qu'on n'a pas lu.",
     "L'hypothèse reste celle de l'AUDIT et de l'entretien."),
    ("Éthanol urinaire", "Le test qualitatif reste positif environ 24 heures.",
     "Il ne donne pas une quantité.",
     "Un contact récent est possible, pas une dépendance."),
], "Le tableau relie chaque marqueur lu à une hypothèse, et il laisse le PEth vide faute de source.")

TABLES["dx4"] = table([
    ("Recherche urinaire de cannabis", "Elle peut être positive alors que la personne décrit un arrêt depuis plusieurs jours.",
     "Aucune demi-vie suisse n'a été relue ici, donc le test ne date pas l'effet.",
     "On croit d'abord le calendrier clinique et le dommage, pas la case seule."),
    ("Recherche négative le jour d'une prise décrite", "L'entretien et l'effet sont là, la case est négative.",
     "Un test peut manquer un usage très récent.",
     "On empêche quand même la conduite."),
    ("Recherche positive et retentissement scolaire", "Les jours fumés et les notes baissent ensemble.",
     "Le laboratoire confirme un contact, il ne grade pas la dépendance.",
     "On propose un suivi, pas un cannabinoïde."),
    ("PEth ou autre marqueur sanguin", "Aucun seuil de phosphatidyléthanol ni de nanogramme n'a été lu.",
     "On n'invente pas une fenêtre de détection.",
     "Le diagnostic reste l'entretien."),
], "La biologie du cannabis, dans les pages lues, se limite à une urine qui ne date pas l'effet.")

TABLES["dx6"] = table([
    ("Dosage plasmatique d'oxazépam", "Aucun seuil thérapeutique ou toxique n'a été extrait de l'information patient ni du diaporama.",
     "On ne convertit pas une concentration imaginaire en palier.",
     "Le diagnostic se fait sur les boîtes, les nuits et le sevrage."),
    ("Compte des comprimés", "Trente comprimés délivrés le 1er et boîte vide le 12.",
     "Le récit d'une prise par nuit est contredit par l'arithmétique.",
     "Escalade ou prise détournée, à sécuriser avant la baisse."),
    ("Vingt nuits sur trente", "MonAM 2024 classe ce rythme comme presque quotidien, soit 1,8 % de la population.",
     "C'est un comportement, pas une convulsivite.",
     "On ouvre la baisse si un manque apparaît à l'arrêt."),
    ("PEth et urine de benzodiazépine", "Aucune fenêtre de détection urinaire n'a été lue.",
     "On n'écrit pas un nombre de jours de positivité.",
     "On demande le nom du produit plutôt qu'un screening non sourcé."),
], "Aucune biologie de concentration n'a été lue : le tableau dit ce qui a été compté, et ce qui reste vide.")

TABLES["dx8"] = table([
    ("Marqueur sanguin du jeu", "Aucun dosage n'est cité par l'article ni par le panorama.",
     "Le trouble ne se confirme pas au laboratoire.",
     "On reste sur les trois traits et le retentissement."),
    ("PEth ou dépistage urinaire", "Ils cherchent un produit, pas une session de jeu.",
     "Les commander « pour le jeu » mélange deux fiches.",
     "On ne les prescrit que si un produit est suspecté par l'entretien."),
    ("Agenda des sessions", "Deux soirs débordés sur sept après une consigne d'heure.",
     "L'échec partiel de réduction est un signe du panorama, pas un nanogramme.",
     "On poursuit la psychothérapie."),
    ("Heures totales", "Aucun seuil horaire n'a été lu.",
     "Le quotidien concerne environ un sixième des jeunes de 15 ans sans être le trouble.",
     "On ne pathologise pas le chronomètre."),
], "Le point 9 du jeu n'a pas de biologie lue : le tableau sépare ce vide des signes cliniques chiffrés.")

TABLES["dx10"] = table([
    ("GGT pendant le manque", "Elle peut être haute après 60 à 70 g par jour pendant quinze jours, tout en ne disant rien du score de ce matin.",
     "Elle baisse de moitié en dix jours d'arrêt, avec une sensibilité d'environ 60 %.",
     "On traite le tremblement sans attendre cette enzyme."),
    ("CDT au décours", "La hausse dès 50 g par jour survit un temps à l'arrêt.",
     "Spécificité d'environ 90 %, faussée par la grossesse, le foie et le rein.",
     "Elle ne décide pas de l'oxazépam de l'heure."),
    ("VGM au troisième mois", "Il lui faut souvent plus de 100 g par jour pendant trois mois.",
     "Sensibilité 25 %, spécificité 90 % hors carence.",
     "Un volume normal laisse entier un sevrage clinique."),
    ("PEth", "Pas de seuil dans les PDF ouverts pour ce sevrage.",
     "On n'en déduit ni l'abstinence ni la rechute.",
     "Le CIWA-Ar et l'éthylotest restent les outils lus."),
    ("Éthylotest", "Au-dessus de 2,5 pour mille, l'oxazépam est différé.",
     "On reteste une heure plus tard.",
     "Un score haut ne passe pas outre ce pour mille."),
], "Pendant le sevrage, la biologie chronique ne remplace pas le pour mille ni le score.")

def load_items():
    spec = importlib.util.spec_from_file_location("items", ROOT/"outils"/"items_fenetres.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.ITEMS

def main():
    items = load_items()
    spec = importlib.util.spec_from_file_location("asm", ASM)
    asm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(asm)
    for dx, num in (("dx2","2"),("dx4","4"),("dx6","6"),("dx8","8"),("dx10","10")):
        path = PREU / f"corps_{dx}.html"
        t = path.read_text(encoding="utf-8")
        anchor = f'<h3 id="{dx}-p9">'
        i = t.find(anchor)
        if i < 0:
            raise SystemExit("no p9 "+dx)
        j = t.find("</h3>", i) + 5
        if "Marqueur" not in t[j:j+800]:
            t = t[:j] + "\n" + TABLES[dx] + t[j:]
        # remove previous glossaire if rerun
        marker = f'<!-- GLOSSAIRE {dx} -->'
        if marker in t:
            t = t.split(marker)[0] + t.split("<!-- /GLOSSAIRE -->", 1)[1]
        block = [marker + "\n"]
        seen = set()
        for n, (label, text) in enumerate(items[dx], 1):
            if text in seen:
                raise SystemExit("dup text "+dx+" "+label)
            seen.add(text)
            block.append(win(dx, n, label, text))
        block.append("<!-- /GLOSSAIRE -->\n")
        gloss = "".join(block)
        # fit under 149200
        src_anchor = '<section id="sources">'
        if src_anchor not in t:
            raise SystemExit("no sources "+dx)
        lo, hi = 0, len(items[dx])
        best = 0
        while lo <= hi:
            mid = (lo+hi)//2
            trial = t.replace(src_anchor, "".join(block[:1]+block[1:mid+1]+["<!-- /GLOSSAIRE -->\n"]) + src_anchor, 1)
            tmp = Path("/tmp/fit.html")
            asm.assembler(trial, num, tmp)
            size = tmp.stat().st_size
            if size <= 149200:
                best = mid
                lo = mid+1
            else:
                hi = mid-1
        final_gloss = "".join(block[:1] + block[1:best+1] + ["<!-- /GLOSSAIRE -->\n"])
        t = t.replace(src_anchor, final_gloss + src_anchor, 1)
        path.write_text(t, encoding="utf-8")
        out = OUT / f"LOT_129_Phase_B_V0_DX.{num}.html"
        asm.assembler(t, num, out)
        print(dx, "windows_added", best, "html", out.stat().st_size)

if __name__ == "__main__":
    main()
