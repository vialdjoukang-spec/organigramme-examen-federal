"""Fabrique un LOT FICTIF (jamais un vrai LOT) pour les tests et le banc d'essai."""
from pathlib import Path

TITRES = ["Définition et sémantique", "Épidémiologie (Suisse, puis Europe)", "Physiopathologie", "Démarche diagnostique",
          "Anamnèse ciblée et drapeaux rouges", "Examen physique ciblé, région par région", "Approche syndromique",
          "Diagnostic positif et critères", "Examens complémentaires", "Arbre décisionnel",
          "Prise en charge selon les recommandations suisses", "Prévention", "Points clés", "Pièges et questions fréquentes à l'examen fédéral suisse"]

def fenetre(i, k):
    corps = (f"Le mécanisme progresse de la cause vers le signe ; ainsi, la natrémie chute sous 135 mmol/L [S1]. "
             f"Par exemple, une patiente de 72 ans présente une natrémie à 128 mmol/L, car elle prend un thiazidique [S2]. ") * 3
    return (f"<details style='display:inline;'><summary>notion {i}.{k}</summary><p>{corps}</p>"
            "<div style='overflow-x:auto;'><table><tr><th>Valeur normale [S1]</th><th>Seuil</th></tr>"
            "<tr><td>135–145 mmol/L</td><td>&lt; 135 mmol/L</td></tr></table></div></details>")

def point(n, i, defauts):
    t = TITRES[n - 1]
    principal = (f"Le clinicien évalue d'abord la gravité [S1] {fenetre(i, n)}. "
                 f"Il recherche ensuite la cause, car elle oriente le traitement [S2] {fenetre(i, n + 20)}. ")
    if "volume" in defauts and n == 4:
        principal += "Il examine le patient. Il note les signes. Il prescrit un bilan. Il revoit le patient. Il conclut. Il écrit. "
    extra = ""
    if n == 9:
        extra = "<p><em>9.a</em> Le gold standard reste l'osmolalité [S1]. <em>9.b</em> La natrémie se dose en 1re intention [S1]. <em>9.c</em> Les alternatives existent [S2]. <em>9.d</em> Le test de 2e intention se discute [S2].</p>"
    if n == 3:
        extra = "<div style='overflow-x:auto;'><table><caption>Corrélation lésion → exploration → thérapeutique [S1]</caption><tr><th>Lésion</th><th>Exploration</th><th>Thérapeutique</th></tr><tr><td>Rétention d'eau</td><td>Osmolalité</td><td>Restriction</td></tr></table></div>"
    if n == 11:
        extra = ("<p><em>11.A- But</em> : le traitement vise une natrémie remontée de 4 à 6 mmol/L en 24 h [S1].</p>"
                 "<p><em>11.B- Moyens</em> : la restriction hydrique s'applique ; chez la femme enceinte, l'allaitement, le sujet âgé, l'enfant, "
                 "l'insuffisant hépatique et l'insuffisant rénal (paliers de DFGe), la dose s'adapte selon l'AIPS [S1].</p>"
                 "<p>La forme compliquée impose une conduite immédiate [S1] <details style='display:inline;'><summary>Urgence — conduite chronologique</summary>"
                 "<p>Le médecin perfuse 150 ml de NaCl 3 % en 20 minutes, puis il contrôle la natrémie [S2].</p></details>.</p>"
                 "<p><em>11.C- Surveillance</em> : le médecin surveille la natrémie toutes les 4 h [S1].</p>"
                 "<p><em>11.D- Pronostic</em> : la sortie se décide lorsque les critères de retour à domicile sont remplis [S1].</p>")
        if "pec_sans_source" in defauts:
            extra += "<p>La dose recommandée atteint 500 mg deux fois par jour pendant 7 jours.</p>"
    if "vague" in defauts and n == 2:
        extra += "<p>Cette maladie survient souvent chez les patients âgés, il est important de noter que le monitoring reste utile.</p>"
    return f"<p><strong>{n}. {t}</strong></p><p>{principal}</p>{extra}"

def monographie(i, defauts):
    pts = [n for n in range(1, 15) if not ("point_manquant" in defauts and i == 1 and n == 12)]
    return f"<details open><summary>DX.{i} — Hyponatrémie de type {i}</summary>" + "".join(point(n, i, defauts) for n in pts) + "</details>\n"

def fabriquer(chemin, lot=230, nb=3, defauts=(), cible=150_000):
    etiquette = f"LOT_{lot}_Appel_B_V7_Partie_2"
    sources = ("<h2>Sources</h2><ol>"
               "<li>[S1] Swissmedic, Information professionnelle, 2026, https://www.swissmedicinfo.ch/ (consulté le 2026-10-24)</li>"
               "<li>[S2] OFSP, Recommandations, 2026, https://www.bag.admin.ch/ (consulté le 2026-10-24)</li></ol>")
    corps = ""; i = 0
    while True:
        i += 1; corps += monographie(i, defauts)
        if len(corps.encode()) > cible - 3000 or i >= 40: break
        if i >= nb and len(corps.encode()) > cible * 0.6: break
    html = ("<!DOCTYPE html>\n<html lang='fr'><head><meta charset='utf-8'><title>LOT fictif</title></head><body>\n"
            f"<h2>LOT_{lot} — fichier FICTIF de test</h2>\n" + corps + sources +
            "\n<p>Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin.</p>\n</body></html>\n"
            f"<!-- FIN_FICHIER {etiquette} -->\n")
    html = "\n".join(l if len(l) < 2900 else l.replace("</p>", "</p>\n") for l in html.split("\n"))
    Path(chemin).parent.mkdir(parents=True, exist_ok=True); Path(chemin).write_text(html, "utf-8")
    return chemin, etiquette
