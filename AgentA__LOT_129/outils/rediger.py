#!/usr/bin/env python3
"""Assemble des monographies rédigées (textes uniques). La police seule est mécanique."""
import base64, html
from pathlib import Path

POL = Path("/agent/repos/organigramme-examen-federal/codex-LOTS-html/outils/polices")
OUT = Path("/tmp/wt129/AgentA__LOT_129")

def font_css():
    faces = []
    for poids, nom in ((400, "atkinson-hyperlegible-latin-400-normal.woff2"), (700, "atkinson-hyperlegible-latin-700-normal.woff2")):
        raw = base64.b64encode((POL / nom).read_bytes()).decode()
        corps = "\n".join(raw[i:i + 1500] for i in range(0, len(raw), 1500))
        faces.append(
            '@font-face{font-family:"Atkinson Hyperlegible";font-style:normal;font-weight:'
            + str(poids)
            + ';font-display:swap;src:url(data:font/woff2;base64,'
            + corps
            + ') format("woff2")}'
        )
    return "\n".join(faces) + """
body{margin:0;background:#eef7fc;color:#1d2a30;font:1rem/1.55 "Atkinson Hyperlegible",Verdana,sans-serif}
main{max-width:74ch;margin:auto;padding:1rem 1rem 2rem}
h2,h3{font-family:"Atkinson Hyperlegible",Verdana,sans-serif;color:#14303b}
.ilot{border:1px solid #cfe3ec;border-radius:12px;padding:.85rem 1rem;margin:0 0 .75rem;background:#fff}
.tw{overflow-x:auto}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #cfe3ec;padding:.4rem;vertical-align:top;text-align:left}
button.terme{all:unset;cursor:pointer;color:#0b5d86;text-decoration:underline dotted 1.5px}
[popover].fenetre{width:min(96vw,60rem);max-height:88vh;overflow:auto;padding:0;border:1px solid #888;border-radius:.5rem;background:#fff}
[popover]::backdrop{background:rgb(0 0 0 / .35)}
.barre{display:flex;justify-content:space-between;padding:.5rem .8rem;background:#f2f5f7;font-weight:700}
.barre button{border:1px solid #cfe3ec;border-radius:6px;background:#fff;cursor:pointer}
.corps{padding:.8rem 1rem 1rem}
.urgence{border:2px solid #a1262f;border-radius:8px;padding:.7rem .9rem}
.s{color:#4f5f66}
"""

def esc(s):
    return html.escape(s, quote=True)

def fen(did, title, paras):
    body = "".join("<p>" + esc(p) + "</p>" for p in paras)
    return (
        '<div id="' + did + '" popover class="fenetre"><div class="barre"><span>'
        + esc(title)
        + '</span><button type="button" popovertarget="' + did
        + '" popovertargetaction="hide">Fermer</button></div><div class="corps">'
        + body + "</div></div>"
    )

def btn(did, word):
    return '<button type="button" class="terme" popovertarget="' + did + '">' + esc(word) + "</button>"

SOURCES = """<section id="sources"><h3>Sources</h3><ol>
<li id="sb-1">[S1] Favrod-Coune T. L'alcool en médecine de premier recours. HUG, SMPR, 2021. https://www.hug.ch/sites/interhug/files/2022-09/strategie_alcool_smpr_2021.pdf — lu le 9 novembre 2026.</li>
<li id="sb-2">[S2] Probst C, Favrod-Coune T, De Lucia S, Humair JP. Dépendance au tabac en médecine de premier recours. HUG, SMPR, 2024. https://www.hug.ch/sites/interhug/files/2024-10/strategie_tabac_doi.pdf — lu le 9 novembre 2026.</li>
<li id="sb-3">[S3] Tox Info Suisse, accueil. https://www.toxinfo.ch/ — lu le 9 novembre 2026. Le 145 y figure 24 h sur 24.</li>
<li id="sb-4">[S4] Interverband für Rettungswesen, site du 144. https://www.144.ch/ — lu le 9 novembre 2026.</li>
</ol>
<p class="s">Non validé cliniquement. Le fichier de liens du référentiel n'est pas une source : il a seulement indiqué la page HUG des stratégies, ouverte ensuite.</p>
</section>"""

def wrap(pre, h2, blocks):
    bits = []
    for i, (title, body, extra) in enumerate(blocks, 1):
        bits.append(
            '<section class="ilot"><h3 id="' + pre + "-p" + str(i) + '"><strong>'
            + str(i) + ". " + esc(title) + "</strong></h3>\n" + body + "\n" + extra + "</section>"
        )
    return (
        "<!DOCTYPE html>\n<html lang=\"fr\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        "<title>LOT 129</title><style>\n" + font_css() + "</style></head><body><main>\n"
        "<p class=\"s\">LOT 129 · S9.13 · non validé cliniquement.</p>\n"
        "<h2 id=\"" + pre + "\">" + esc(h2) + "</h2>\n"
        + "\n".join(bits) + "\n" + SOURCES + "\n</main></body></html>\n<!-- FIN_FICHIER LOT_129 -->\n"
    )

def alcool():
    d = "dx2"
    return [
        ("Définition et sémantique",
         "<p>En 2021, le service de médecine de premier recours des HUG sépare l'excès et la dépendance. Un verre standard européen contient 10 g d'éthanol. L'ivresse ponctuelle est définie, chez la femme, par plus de 4 verres en une occasion et, chez l'homme, par plus de 5.</p>"
         "<p>Les plafonds hebdomadaires sont dans la fenêtre " + btn(d + "-w1", "plafonds") + ".</p>",
         fen(d + "-w1", "Plafonds HUG 2021", [
             "Femme : au plus 1 verre par jour, 5 par semaine, 4 par occasion. Homme : au plus 2 verres par jour, 10 par semaine, 5 par occasion.",
             "La dépendance ajoute un manque physique ou psychique. L'excès sans manque abîme déjà, mais ce n'est pas le même plan de soin.",
             "Piège. Convertir un verre de restaurant en « un petit verre » sans le ramener à 10 g. Source [S1].",
         ])),
        ("Épidémiologie",
         "<p>La stratégie retient qu'au moins un patient de premier recours sur quatre a une consommation problématique. Elle ne publie pas, dans le PDF lu, une incidence annuelle genevoise séparée de cette proportion.</p>",
         ""),
        ("Physiopathologie",
         "<p>Quand l'alcool manque, apparaissent agitation, anxiété, insomnie, tremblement, sueurs, tachycardie et hypertension, puis parfois fièvre, délire et convulsions. Cette séquence dure de 3 à 10 jours. Le texte HUG la qualifie d'urgence médicale, et il dit qu'elle peut tuer.</p>",
         ""),
        ("Étiologie et facteurs de risque",
         "<p>Sont écrits : histoire familiale de dépendance ou de cancer, autres substances, difficultés psychosociales, métiers de la restauration. Ce ne sont pas des destins. Ils changent la vigilance, pas le respect du récit.</p>",
         ""),
        ("Anamnèse",
         "<p>On cherche hypertension, troubles digestifs, mémoire, concentration, anxiété, dépression, sommeil, chutes, absentéisme, conflits familiaux et ennuis légaux. Le questionnaire ACME (CAGE) atteint une sensibilité de 63 pour cent et une spécificité de 91 pour cent à partir de deux réponses positives. Dès une seule réponse positive, la sensibilité approche 90 pour cent et la spécificité tombe à 52 pour cent : on enchaîne alors avec l'AUDIT, détaillé dans " + btn(d + "-w5", "AUDIT") + ".</p>",
         fen(d + "-w5", "ACME puis AUDIT", [
             "Les quatre lettres françaises : Arrêter, Coupable, Matin, Ennuyé. Deux oui : assez spécifique, pas assez sensible. Un seul oui : on ne s'arrête pas là.",
             "AUDIT, 10 items, sensibilité citée de 85 pour cent et spécificité de 90 pour cent. Moins de 7 points : faible risque. Au-dessus de 7 chez la femme et de 8 chez l'homme : excès. Au-dessus de 13 : dépendance.",
             "Piège. Lire les questions comme une accusation. Le texte HUG prévient que le patient se ferme. Source [S1].",
         ])),
        ("Examen physique",
         "<p>Érythème du visage et des paumes, parotides volumineuses, tremblement fin : ces signes peuvent manquer. Le texte dit de croire d'abord la personne, puis de critiquer les quantités parce que le déni les rabote.</p>",
         ""),
        ("Approche syndromique",
         "<p>Trois situations ne se soignent pas pareil : l'excès sans manque, la dépendance encore stable, le sevrage déjà bruyant. La troisième n'attend pas le questionnaire.</p>",
         ""),
        ("Diagnostic positif",
         "<p>L'excès se chiffre avec les verres et l'AUDIT. La dépendance se reconnaît en plus au manque. Un AUDIT au-dessus de 13, dans la stratégie, nomme l'alcoolo-dépendance.</p>",
         ""),
        ("Examens complémentaires",
         "<p><em>9.a Gold standard.</em> En premier recours, l'outil de référence lu est l'AUDIT, pas une alcoolémie ni un bilan hépatique.</p>"
         "<p><em>9.b 1re intention.</em> Question ouverte, puis ACME, puis AUDIT dès qu'ACME s'allume. Le laboratoire ne vient pas avant.</p>"
         '<div class="tw"><table><thead><tr><th>Cas</th><th>AUDIT</th><th>Lecture</th><th>Hypothèse</th></tr></thead><tbody>'
         "<tr><td>normal</td><td>moins de 7</td><td>faible risque</td><td>renforcer la modération</td></tr>"
         "<tr><td>positif</td><td>plus de 7 (femme) ou plus de 8 (homme)</td><td>excès</td><td>réduction</td></tr>"
         "<tr><td>limite</td><td>un seul item ACME</td><td>spécificité 52 pour cent</td><td>faire l'AUDIT</td></tr>"
         "<tr><td>discordant</td><td>score rassurant mais sueurs et tremblement</td><td>le sevrage clinique prime</td><td>soin du manque</td></tr>"
         "</tbody></table></div>",
         ""),
        ("Arbre décisionnel",
         "<p>Pas de consommation : on la renforce et on parle des autres risques cardiovasculaires. Excès : réduction, par exemple un programme du type Mes choix Alcool, cité par les HUG. Dépendance : l'abstinence est l'objectif préféré ; la consommation contrôlée reste un cadre si l'abstinence ne tient pas.</p>",
         ""),
        ("Prise en charge",
         "<p>Ambulatoire, on revoit la personne tous les deux ou trois jours. Vitamine B1 : 300 mg par jour pendant trois semaines. Oxazépam : 60 à 200 mg par jour en quatre à six prises, baisse d'environ 20 pour cent par jour, ou mieux selon le CIWA. Le choix du lieu est dans " + btn(d + "-w11", "contre-indications") + ".</p>"
         "<p>Ensuite, acamprosate : deux comprimés de 300 mg, deux fois par jour sous 60 kg et trois fois par jour au-dessus, pour trois à douze mois. Naltrexone : un demi à un comprimé de 50 mg une fois par jour pendant six mois.</p>"
         '<div class="urgence"><strong>Urgence — conduite chronologique.</strong> Sueurs, tremblement, tachycardie : c\'est le sevrage, pas une grippe. Contre-indication absolue ou convulsion : hôpital. Sinon thiamine et oxazépam, revue rapide.</div>',
         fen(d + "-w11", "Ne pas sevrer en ville si", [
             "Absolu : comorbidité somatique ou psychique importante, convulsion ou delirium tremens déjà vécus, prise importante de benzodiazépines.",
             "Relatif : échec ambulatoire, souhait de la personne, alliance fragile, isolement, entourage épuisé.",
             "Piège. Appliquer la baisse de 20 pour cent alors que le CIWA remonte. Source [S1].",
         ])),
        ("Prévention",
         "<p>Interroger chaque patient, pas une sous-population déjà étiquetée. L'empathie et un objectif tenable précèdent le discours d'abstinence.</p>",
         ""),
        ("Points clés",
         "<p>Un quart des consultants, au moins, boit de façon problématique. Dix grammes par verre. AUDIT : 7, 8 et 13. Sevrage : 3 à 10 jours, possiblement mortel. Thiamine 300 mg par jour. Oxazépam 60 à 200 mg par jour guidé par le CIWA.</p>",
         ""),
        ("Pièges",
         "<p>Croire le nombre de verres avoué. Sevrer en ville après un delirium. Promettre l'acamprosate sans avoir choisi entre abstinence et contrôle.</p>",
         ""),
    ]

def tabac():
    d = "dx1"
    return [
        ("Définition et sémantique",
         "<p>La stratégie HUG de 2024 exige de voir la consommation quotidienne de tabac comme une maladie, pas comme un vice. Elle rappelle six critères CIM-10 : compulsion, tolérance, perte de contrôle, sevrage, abandon des autres plaisirs, poursuite malgré le dommage.</p>",
         ""),
        ("Épidémiologie",
         "<p>Le texte reprend l'OFSP : environ 10 ans d'espérance de vie en moins. Même 1 à 4 cigarettes par jour comptent. Les médecins abordent le sujet avec 68 pour cent des fumeurs, conseillent l'arrêt à 34 pour cent, alors que 51 pour cent des fumeurs de l'enquête citée voulaient une aide.</p>",
         ""),
        ("Physiopathologie",
         "<p>La nicotine est rangée avec l'héroïne, l'alcool, la cocaïne et les barbituriques parmi cinq produits très addictifs. Le cancer et la BPCO viennent de la combustion, pas de la nicotine seule. Au-delà d'environ 5 cigarettes par jour, l'arrêt peut donner un sevrage de trois semaines à trois mois : craving, humeur basse, insomnie, irritabilité, anxiété, trouble de concentration, agitation, appétit.</p>",
         ""),
        ("Étiologie et facteurs de risque",
         "<p>Génétique, trauma, entourage. Le tabac est relié par le texte à 85-90 pour cent des BPCO, à un risque de dégénérescence maculaire multiplié par quatre, et à des plaies qui ne ferment pas.</p>",
         ""),
        ("Anamnèse",
         "<p>Forme exacte : cigarette, cigare, pipe, snus, prisé, vapoteuse. Début, quantité, arrêts, envie. Le Fagerström, six questions sur 10, est ouvert dans " + btn(d + "-w5", "Fagerström") + ".</p>",
         fen(d + "-w5", "Fagerström 0 à 10", [
             "0 à 2 : pas de dépendance nicotinique. 3 à 4 : faible. 5 à 6 : modérée. 7 à 10 : forte.",
             "Première cigarette dans les cinq minutes : 3 points. Trente et une cigarettes ou plus : 3 points aussi.",
             "Le score sert encore au remboursement du bupropion et de la varénicline, tout en cédant le pas clinique à la Cigarette Dependence Scale.",
             "Piège. Oublier le snus parce que la question ne disait que « fumer ». Source [S2].",
         ])),
        ("Examen physique",
         "<p>Toux, souffle, pouls, tension, claudication, plaie traînante. L'examen documente le dommage. Il ne sert pas à faire honte.</p>",
         ""),
        ("Approche syndromique",
         "<p>Trois personnes : celle qui veut arrêter, celle qui accepte seulement de quitter la combustion, celle qui refuse. Les trois ont droit au conseil. Le refus d'aujourd'hui se réévalue.</p>",
         ""),
        ("Diagnostic positif",
         "<p>La dépendance quotidienne colle aux critères CIM-10, souvent cliniquement au-delà de cinq cigarettes par jour. L'usage rare sans ces critères n'est pas une dépendance, et il n'est pas non plus « sans risque » selon le texte.</p>",
         ""),
        ("Examens complémentaires",
         "<p><em>9.a Gold standard.</em> L'entretien, proposé à chaque patient après son accord. Le Fagerström grade la nicotine. Aucun seuil de CO expiré n'est donné comme référence dans les pages lues.</p>"
         "<p><em>9.b 1re intention.</em> Demander s'il y a une consommation et sous quelle forme. Le score vient pour choisir l'intensité du patch, pas pour autoriser la question.</p>"
         '<div class="tw"><table><thead><tr><th>Cas</th><th>Score</th><th>Lecture 2024</th><th>Suite si arrêt choisi</th></tr></thead><tbody>'
         "<tr><td>normal</td><td>0 à 2</td><td>pas de dépendance</td><td>conseil quand même</td></tr>"
         "<tr><td>positif</td><td>7 à 10</td><td>dépendance forte</td><td>patch à 21 mg</td></tr>"
         "<tr><td>limite</td><td>3 à 6</td><td>faible ou modérée</td><td>dose moyenne ou faible</td></tr>"
         "<tr><td>discordant</td><td>total bas mais cigarette au lit</td><td>un item peut porter seul</td><td>croire le craving</td></tr>"
         "</tbody></table></div>",
         ""),
        ("Arbre décisionnel",
         "<p>Volonté d'arrêt : date et traitement. Volonté de continuer : proposer le non-combustible et revoir. Échec : nouvelle tentative, pas une sentence d'incapacité.</p>",
         ""),
        ("Prise en charge",
         "<p>Patch fort : 21 mg quatre semaines, puis 14 mg deux à quatre semaines, puis 7 mg deux à quatre semaines, sur deux à trois mois, prolongeable jusqu'à six ou douze mois. Dose moyenne : départ à 14 mg. Dose faible : 7 mg.</p>"
         "<p>Bupropion : 150 mg une fois par jour pendant sept jours, puis 150 mg deux fois par jour. Le texte indique environ 60 pour cent de chances d'arrêt en plus à six mois contre placebo. La varénicline est décrite comme supérieure, puis comme retirée du marché mondial en décembre 2022. La cytisine est mentionnée comme alternative à commander.</p>"
         '<div class="urgence"><strong>Urgence — conduite chronologique.</strong> Douleur thoracique ou détresse respiratoire : ce n\'est pas un craving. Orientation vers les urgences. Le craving lui-même se couvre avec le substitut, pas avec l\'ordre de « tenir » sans rien.</div>',
         ""),
        ("Prévention",
         "<p>Tous les services, après accord. Y compris en psychiatrie : le texte refuse l'idée que ces personnes ne voudraient pas ou ne pourraient pas arrêter.</p>",
         ""),
        ("Points clés",
         "<p>Maladie, pas vice. Dix ans perdus en moyenne selon le chiffre OFSP cité. Fagerström sur 10. Patch fort à 21 mg. Bupropion 150 mg puis deux fois 150 mg. Varénicline indisponible depuis le retrait de 2022.</p>",
         ""),
        ("Pièges",
         "<p>Attendre que le fumeur supplie. Attribuer le cancer à la nicotine seule. Prescrire encore la varénicline comme disponible.</p>",
         ""),
    ]

def opio():
    return [
        ("Définition et sémantique", "<p>L'héroïne est nommée deux fois dans les PDF lus : parmi cinq substances très addictives (stratégie tabac) et parmi les dépendances conjointes de l'alcool. Le trouble se décrit avec les six critères CIM-10 de cette stratégie tabac. Aucune préparation n'est expliquée.</p>", ""),
        ("Épidémiologie", "<p>Pas de prévalence opioïde dans ces PDF. L'absence est laissée vide.</p>", ""),
        ("Physiopathologie", "<p>Tolérance et sevrage font partie des critères. Le manque opioïde n'a pas le visage du manque alcoolique et ne reçoit pas son oxazépam.</p>", ""),
        ("Étiologie et facteurs de risque", "<p>Le texte tabac associe dépendance, trauma et entourage. C'est un cadre, pas une explication individuelle.</p>", ""),
        ("Anamnèse", "<p>Produit nommé par la personne, overdoses déjà vécues, prescripteur au courant ou non, idées de mort. On n'invite pas au récit technique de l'injection.</p>", ""),
        ("Examen physique", "<p>Conscience et fréquence respiratoire d'abord. Myosis avec respiration lente : on arrête l'entretien et on appelle.</p>", ""),
        ("Approche syndromique", "<p>Usage chronique, intoxication qui coupe le souffle, et manque douloureux sont trois films. Les confondre fait donner le mauvais soin.</p>", ""),
        ("Diagnostic positif", "<p>Les critères CIM-10 font la dépendance. Une urine positive sans ces critères ne la décrète pas. Aucun seuil urinaire n'a été lu.</p>", ""),
        ("Examens complémentaires",
         "<p><em>9.a Gold standard.</em> Entretien et respiration. Pas de concentration plasmatique dans les PDF.</p><p><em>9.b 1re intention.</em> Compter les respirations. Si elles tombent, le 144 passe avant le flacon d'urine.</p>"
         '<div class="tw"><table><thead><tr><th>Cas</th><th>Souffle</th><th>Laboratoire lu</th><th>Hypothèse</th></tr></thead><tbody>'
         "<tr><td>normal</td><td>ample, conscience claire</td><td>aucun seuil</td><td>pas d'intoxication</td></tr>"
         "<tr><td>positif</td><td>lent, somnolence</td><td>non lu</td><td>intoxication</td></tr>"
         "<tr><td>limite</td><td>usage chronique, souffle tenu</td><td>non lu</td><td>dépendance à discuter</td></tr>"
         "<tr><td>discordant</td><td>déni et apnée</td><td>inutile sur le moment</td><td>croire le thorax</td></tr></tbody></table></div>",
         ""),
        ("Arbre décisionnel", "<p>Souffle en danger : 144 et avis du 145. Souffle tenu : filière de dépendance, sans recopier le protocole alcool. On ne décrit pas la geste d'injection d'un antidote.</p>", ""),
        ("Prise en charge",
         "<p>La naloxone est l'antidote de cette intoxication. Sa dose n'était pas dans les PDF HUG : elle se lit sur l'information professionnelle du produit disponible, elle ne s'invente pas. La substitution de fond n'a pas été ouverte dans une page de société ce jour-là.</p>"
         '<div class="urgence"><strong>Urgence — conduite chronologique.</strong> Parler, compter les respirations, appeler le 144 dès qu\'elles ralentissent ou que la conscience part. Le 145 renseigne sur le produit pendant l\'attente, il ne remplace pas l\'ambulance.</div>',
         ""),
        ("Prévention", "<p>Repérer les opioïdes prescrits au long cours quand une autre dépendance est déjà connue, comme la stratégie alcool le demande pour les produits associés.</p>", ""),
        ("Points clés", "<p>Respiration d'abord. Pas de seuil urinaire lu. Pas d'oxazépam « comme pour l'alcool ». Dose de naloxone non lue, donc non écrite.</p>", ""),
        ("Pièges", "<p>Continuer à questionner une personne qui ne ventile plus. Inventer un gold standard sanguin. Détailler une voie.</p>", ""),
    ]

def cannabis():
    return [
        ("Définition et sémantique", "<p>Le cannabis figure dans la liste HUG des dépendances conjointes de l'alcool, sans chapitre chiffré. On lui applique les critères CIM-10 cités pour toute substance dans la stratégie tabac, et rien d'autre.</p>", ""),
        ("Épidémiologie", "<p>Aucun taux suisse n'a été lu. La case reste blanche.</p>", ""),
        ("Physiopathologie", "<p>Les PDF ne décrivent pas un récepteur. Ils autorisent seulement à chercher anxiété, persécution et retentissement, comme conséquences cliniques.</p>", ""),
        ("Étiologie et facteurs de risque", "<p>Trauma, entourage, autre produit : le cadre général du texte tabac. Il ne hiérarchise pas les formes de cannabis.</p>", ""),
        ("Anamnèse", "<p>Depuis quand, quelles pertes (sommeil, études, poste), envie de changer. Culture et préparation ne font pas partie de l'entretien médical utile.</p>", ""),
        ("Examen physique", "<p>Conjonctives, pouls, anxiété, discours. Aucune sensibilité chiffrée de ces signes dans les PDF.</p>", ""),
        ("Approche syndromique", "<p>L'élève qui décroche n'est pas l'adulte aigu persécuté. Le second va aux urgences. Le premier se suit.</p>", ""),
        ("Diagnostic positif", "<p>Plusieurs critères CIM-10 : on peut parler de dépendance. Un essai unique : non.</p>", ""),
        ("Examens complémentaires",
         "<p><em>9.a Gold standard.</em> L'entretien. Pas de seuil urinaire dans les stratégies lues.</p><p><em>9.b 1re intention.</em> L'entretien, et les urgences si le discours se désorganise.</p>"
         '<div class="tw"><table><thead><tr><th>Cas</th><th>Récit</th><th>Biologie</th><th>Hypothèse</th></tr></thead><tbody>'
         "<tr><td>normal</td><td>pas de dommage</td><td>non lue</td><td>pas un trouble</td></tr>"
         "<tr><td>positif</td><td>critères CIM-10 réunis</td><td>non lue</td><td>dépendance</td></tr>"
         "<tr><td>limite</td><td>usage régulier, dommage flou</td><td>non lue</td><td>revoir</td></tr>"
         "<tr><td>discordant</td><td>famille inquiète, adolescent serein et notes stables</td><td>non lue</td><td>ne pas étiqueter</td></tr></tbody></table></div>",
         ""),
        ("Arbre décisionnel", "<p>Persécution ou agitation : urgences. Dépendance tranquille : suivi et conséquences concrètes. Refus : porte ouverte, pas de chiffre brandi.</p>", ""),
        ("Prise en charge",
         "<p>Aucune posologie propre au cannabis dans les PDF. Anxiété ou dépression associées : leurs filières, sans molécule improvisée.</p>"
         '<div class="urgence"><strong>Urgence — conduite chronologique.</strong> Désorganisation ou danger : urgences. Sinon rendez-vous proche et recherche des autres produits listés par la stratégie alcool.</div>',
         ""),
        ("Prévention", "<p>Parler sommeil et études. Chez l'adolescent, le 147 est un lien humain, pas un sevrage.</p>", ""),
        ("Points clés", "<p>Pas de seuil urinaire. CIM-10 pour le nom. Urgences si persécution. Pas de dose inventée.</p>", ""),
        ("Pièges", "<p>Cours de culture. Diagnostic sur un essai. Morale à la place du retentissement.</p>", ""),
    ]

def stim():
    return [
        ("Définition et sémantique", "<p>La cocaïne est citée avec la nicotine, l'héroïne, l'alcool et les barbituriques comme produit très addictif, et elle est dans la liste des dépendances conjointes. Ce texte ne dit pas comment on la prend.</p>", ""),
        ("Épidémiologie", "<p>Pas de prévalence dans les PDF du 9 novembre 2026.</p>", ""),
        ("Physiopathologie", "<p>Le danger aigu est le cœur et le cerveau. Le tabac, dans la même stratégie, majore déjà infarctus et AVC. Une douleur thoracique sous stimulant se traite d'abord comme un possible infarctus.</p>", ""),
        ("Étiologie et facteurs de risque", "<p>Le cadre génétique, psychique et social du texte HUG s'applique sans préciser une « dose seuil » de cocaïne, qui n'y est pas.</p>", ""),
        ("Anamnèse", "<p>Nom du produit, douleurs de poitrine déjà eues, malaises, envie d'arrêt. Pas la technique.</p>", ""),
        ("Examen physique", "<p>Pouls, tension, chaleur, pupilles, force des membres, douleur thoracique reproduite. Un examen normal ce matin ne couvre pas la douleur de ce soir.</p>", ""),
        ("Approche syndromique", "<p>Craving du lendemain et douleur thoracique de ce soir ne partagent pas la même filière.</p>", ""),
        ("Diagnostic positif", "<p>Dépendance : critères CIM-10. Intoxication : signes vitaux, sans attendre les six cases.</p>", ""),
        ("Examens complémentaires",
         "<p><em>9.a Gold standard.</em> Pour la poitrine, ce n'est pas l'urine de cocaïne. C'est la démarche du syndrome coronarien, qui n'est pas écrite dans les PDF d'addiction.</p>"
         "<p><em>9.b 1re intention.</em> Constantes et ECG aux urgences si la poitrine serre. Le récit d'usage voyage avec le patient, il ne retarde pas le tracé.</p>"
         '<div class="tw"><table><thead><tr><th>Cas</th><th>Poitrine</th><th>Geste</th><th>Hypothèse</th></tr></thead><tbody>'
         "<tr><td>normal</td><td>aucune douleur</td><td>entretien</td><td>dépendance possible</td></tr>"
         "<tr><td>positif</td><td>douleur</td><td>ECG aux urgences</td><td>coronarien d'abord</td></tr>"
         "<tr><td>limite</td><td>palpitations seules</td><td>pouls et tension au minimum</td><td>ne pas étiqueter</td></tr>"
         "<tr><td>discordant</td><td>ECG rassurant hier, douleur aujourd'hui</td><td>nouvel ECG</td><td>hier est périmé</td></tr></tbody></table></div>",
         ""),
        ("Arbre décisionnel", "<p>Douleur, déficit ou convulsion : 144. Rien de tout cela : entretien et produits associés.</p>", ""),
        ("Prise en charge",
         "<p>Pas de posologie anticraving de la cocaïne dans les stratégies lues. Ni bupropion du tabac ni naltrexone de l'alcool ne sont transposés.</p>"
         '<div class="urgence"><strong>Urgence — conduite chronologique.</strong> Douleur thoracique : fin de l\'entretien de motivation, 144, dire qu\'un stimulant est possible. Pas de sédatif de ville en attendant.</div>',
         ""),
        ("Prévention", "<p>Devant un trouble de l'alcool ou du tabac, demander la cocaïne, parce qu'elle est nommée dans les deux textes.</p>", ""),
        ("Points clés", "<p>Produit très addictif selon le texte. Douleur thoracique prioritaire. Pas de dose d'anticraving lue. Pas de voie décrite.</p>", ""),
        ("Pièges", "<p>Appeler cela une panique sans ECG. Faire décrire la prise.</p>", ""),
    ]

def benzo():
    return [
        ("Définition et sémantique", "<p>Dans la stratégie alcool, une prise importante de benzodiazépines est une contre-indication absolue au sevrage ambulatoire. Ailleurs, elles figurent parmi les dépendances conjointes. L'ordonnance courte et tenue n'est pas ce fichier.</p>", ""),
        ("Épidémiologie", "<p>Pas de taux suisse dans les PDF. On n'en pose pas.</p>", ""),
        ("Physiopathologie", "<p>L'arrêt sec au long cours peut convulsiver, danger déjà reconnu pour le sevrage alcoolique compliqué. D'où l'interdiction d'une baisse improvisée.</p>", ""),
        ("Étiologie et facteurs de risque", "<p>Sevrage alcoolique convulsif, comorbidité lourde, isolement : le tableau HUG des contre-indications éclaire aussi cette situation.</p>", ""),
        ("Anamnèse", "<p>Nom, durée, dose dite par la personne, prescripteur, arrêts, convulsions. La dose dite se note. Aucun calendrier de décroissance en milligrammes n'est écrit ici, faute de schéma dans les PDF.</p>", ""),
        ("Examen physique", "<p>Vigilance, élocution, marche, tremblement. Somnolence nouvelle si l'alcool s'y ajoute : penser à la respiration.</p>", ""),
        ("Approche syndromique", "<p>L'escalade sur des mois n'est pas le coma mixte de ce soir. Le coma appelle le 144. L'escalade appelle le prescripteur.</p>", ""),
        ("Diagnostic positif", "<p>Critères CIM-10, surtout sevrage et perte de contrôle. Une prescription stable, connue, sans escalade, ne devient pas une dépendance par principe.</p>", ""),
        ("Examens complémentaires",
         "<p><em>9.a Gold standard.</em> Les boîtes et l'entretien. Pas de concentration sérique dans les documents lus.</p>"
         "<p><em>9.b 1re intention.</em> Reconstituer qui prescrit et si un arrêt a déjà convulsé.</p>"
         '<div class="tw"><table><thead><tr><th>Cas</th><th>Histoire</th><th>Biologie</th><th>Hypothèse</th></tr></thead><tbody>'
         "<tr><td>normal</td><td>cure courte, arrêt simple</td><td>non demandée</td><td>pas une dépendance</td></tr>"
         "<tr><td>positif</td><td>escalade, arrêt impossible</td><td>non lue</td><td>dépendance</td></tr>"
         "<tr><td>limite</td><td>années stables</td><td>non lue</td><td>ne pas sevrer d'office</td></tr>"
         "<tr><td>discordant</td><td>dose dite petite, chutes répétées</td><td>non lue</td><td>les chutes comptent</td></tr></tbody></table></div>",
         ""),
        ("Arbre décisionnel", "<p>Convulsion ou respiration faible : 144. Dépendance sans cela : le prescripteur fait le plan. Sevrage d'alcool concomitant et benzodiazépine importante : hôpital, selon le tableau absolu de 2021.</p>", ""),
        ("Prise en charge",
         "<p>Pas de schéma de baisse. On dit que l'arrêt sec est dangereux et que le plan appartient au prescripteur. On ne recopie pas les milligrammes d'oxazépam sur une autre molécule.</p>"
         '<div class="urgence"><strong>Urgence — conduite chronologique.</strong> Vigilance qui chute ou convulsion : 144, nommer la benzodiazépine et l\'alcool éventuel. Ne pas puiser une dose dans l\'armoire pour « tenir ».</div>',
         ""),
        ("Prévention", "<p>Revoir les renouvellements. Le fatalisme envers les malades psychiques est contredit par la stratégie tabac : on peut aussi viser un changement chez eux.</p>", ""),
        ("Points clés", "<p>Pas de calendrier lu. Contre-indication absolue au sevrage alcoolique de ville si la benzodiazépine est lourde. Convulsion : urgences.</p>", ""),
        ("Pièges", "<p>Arrêt brutal « pour le bien ». Copier-coller de l'oxazépam.</p>", ""),
    ]

def jeu():
    return [
        ("Définition et sémantique", "<p>Les jeux de hasard sont dans la liste HUG des dépendances à traiter avec l'alcool. Aucun critère chiffré du jeu pathologique n'y figure. On parle de perte de contrôle sur l'argent et le temps, jamais d'une méthode de mise.</p>", ""),
        ("Épidémiologie", "<p>Pas de taux suisse dans les PDF ouverts.</p>", ""),
        ("Physiopathologie", "<p>La poursuite malgré le dommage, critère CIM-10 écrit pour les substances, se reconnaît ici quand la personne rejoue après une perte qu'elle sait nuisible.</p>", ""),
        ("Étiologie et facteurs de risque", "<p>L'alcool concomitant est le lien explicitement écrit. Les difficultés psychosociales de la même stratégie se demandent aussi.</p>", ""),
        ("Anamnèse", "<p>Temps, sommes perdues, mensonges, dettes, idées de mort. Pas les systèmes de mise.</p>", ""),
        ("Examen physique", "<p>Pas de signe cutané. On cherche une conséquence : maigreur, ivresse associée, négligence.</p>", ""),
        ("Approche syndromique", "<p>Une soirée limitée n'est pas la poursuite des pertes avec dettes. Seule la seconde ouvre un suivi de dépendance.</p>", ""),
        ("Diagnostic positif", "<p>Contrôle perdu et dommages présents. Sans échelle suisse lue, pas de seuil en francs ni en heures.</p>", ""),
        ("Examens complémentaires",
         "<p><em>9.a Gold standard.</em> L'entretien sur l'argent. Pas de biologie.</p><p><em>9.b 1re intention.</em> Cet entretien et la question des idées de mort, sans demander le moyen.</p>"
         '<div class="tw"><table><thead><tr><th>Cas</th><th>Argent et contrôle</th><th>Test</th><th>Hypothèse</th></tr></thead><tbody>'
         "<tr><td>normal</td><td>jeu borné, pas de dette</td><td>aucun</td><td>pas un trouble</td></tr>"
         "<tr><td>positif</td><td>pertes relancées, mensonge</td><td>entretien</td><td>jeu excessif</td></tr>"
         "<tr><td>limite</td><td>seul l'entourage s'alarme</td><td>voir la personne</td><td>à confirmer</td></tr>"
         "<tr><td>discordant</td><td>déni et dettes écrites</td><td>croiser</td><td>ne pas clore</td></tr></tbody></table></div>",
         ""),
        ("Arbre décisionnel", "<p>Danger suicidaire imminent : 144. Détresse sans cela : 143 et addictologie. Alcool présent : la stratégie alcool s'ajoute.</p>", ""),
        ("Prise en charge",
         "<p>Pas de médicament du jeu dans les PDF. Le seul cadre écrit est le travail motivationnel de l'alcool : empathie, objectifs tenables. Protéger l'accès à l'argent se décide avec la personne.</p>"
         '<div class="urgence"><strong>Urgence — conduite chronologique.</strong> Question sur les idées de mort, sans mode opératoire. Imminent : 144. Sinon 143 et une date de rendez-vous.</div>',
         ""),
        ("Prévention", "<p>Devant un trouble de l'alcool, poser la question du jeu, puisqu'elle est dans la liste.</p>", ""),
        ("Points clés", "<p>Pas de seuil en argent. Jeu cité avec l'alcool. Pas de molécule. Idées de mort sans description de moyen.</p>", ""),
        ("Pièges", "<p>Tactique de mise. Minimiser faute de produit. Oublier l'alcool.</p>", ""),
    ]

def ecran():
    return [
        ("Définition et sémantique", "<p>Le mot « cyber » apparaît dans la stratégie alcool à côté du jeu et du sexe, parmi les comportements conjoints. Il ne définit pas le jeu vidéo. Ici, l'usage excessif est celui qui vole le sommeil et les obligations, et qui rend irritable quand on coupe.</p>", ""),
        ("Épidémiologie", "<p>Pas de prévalence dans les documents ouverts.</p>", ""),
        ("Physiopathologie", "<p>L'irritabilité à l'arrêt s'observe. Aucun modèle de récompense chiffré n'est dans les PDF. On reste sur le retentissement.</p>", ""),
        ("Étiologie et facteurs de risque", "<p>Isolement et difficultés psychosociales, écrits pour l'alcool, se cherchent. Le sommeil peut être cause ou suite.</p>", ""),
        ("Anamnèse", "<p>Heure de fin, heures dormies, notes ou travail, conflits à l'extinction. Pas les mécaniques de jeu.</p>", ""),
        ("Examen physique", "<p>Poids, fatigue, humeur. Pas de signe validé dans les sources lues.</p>", ""),
        ("Approche syndromique", "<p>Le loisir qui laisse dormir n'est pas la nuit blanche qui fait rater la classe.</p>", ""),
        ("Diagnostic positif", "<p>Le retentissement décide. Les PDF ne donnent pas un nombre d'heures.</p>", ""),
        ("Examens complémentaires",
         "<p><em>9.a Gold standard.</em> Entretien, et parent si la personne est mineure et d'accord, ou si un danger l'exige.</p>"
         "<p><em>9.b 1re intention.</em> Cet entretien. Pas d'échelle suisse lue.</p>"
         '<div class="tw"><table><thead><tr><th>Cas</th><th>Sommeil et devoirs</th><th>Échelle</th><th>Hypothèse</th></tr></thead><tbody>'
         "<tr><td>normal</td><td>tenus</td><td>aucune lue</td><td>loisir</td></tr>"
         "<tr><td>positif</td><td>nuits perdues, échec</td><td>entretien</td><td>usage excessif</td></tr>"
         "<tr><td>limite</td><td>peur parentale seule</td><td>voir l'adolescent</td><td>à vérifier</td></tr>"
         "<tr><td>discordant</td><td>heures minimisées, résultats effondrés</td><td>croiser</td><td>ne pas clore</td></tr></tbody></table></div>",
         ""),
        ("Arbre décisionnel", "<p>Danger ou idées de mort : 144. Souffrance sans danger : 147 et recherche d'une dépression ou d'un autre produit.</p>", ""),
        ("Prise en charge",
         "<p>Pas de médicament de l'écran dans les sources. On répare l'horaire de sommeil. Une dépression se soigne dans sa filière. Confisquer l'appareil n'est pas le traitement.</p>"
         '<div class="urgence"><strong>Urgence — conduite chronologique.</strong> Écarter d\'abord le danger vital. Ensuite seulement les horaires. Le 147 accompagne, il ne signe pas le diagnostic.</div>',
         ""),
        ("Prévention", "<p>Demander le sommeil des adolescents suivis, avant tout discours sur les jeux.</p>", ""),
        ("Points clés", "<p>Pas de quota d'heures lu. Le dommage décide. Le 147 n'est pas un diagnostic. Pas de molécule.</p>", ""),
        ("Pièges", "<p>Inventer un quota. Parler technique. Manquer la dépression.</p>", ""),
    ]

def intox():
    return [
        ("Définition et sémantique", "<p>L'intoxication aiguë est l'effet présent d'un produit, pas la dépendance au long cours. Tox Info Suisse, page lue le 9 novembre 2026, affiche le 145 en continu. Le site du 144 organise les secours.</p>", ""),
        ("Épidémiologie", "<p>L'accueil de Tox Info parle d'un volume d'appels important et de ses soixante ans, sans tableau par substance recopié. Pas d'incidence calculée.</p>", ""),
        ("Physiopathologie", "<p>Conscience, respiration ou cœur peuvent lâcher. Ce n'est pas la séquence du sevrage alcoolique, qui a ses propres signes dans le PDF HUG.</p>", ""),
        ("Étiologie et facteurs de risque", "<p>Plusieurs produits ensemble, situation prévue par la stratégie alcool, aggravent le tableau. L'exemple clinique déjà nommé est l'alcool avec une benzodiazépine, sans consigne de dose.</p>", ""),
        ("Anamnèse", "<p>Quoi, quand, quantité approximative, accompagnement, vomissements, convulsion, douleur thoracique. La quantité informe le 145. Elle ne sert pas à calculer une dose mortelle : ce calcul n'est pas dans les pages lues et n'est pas fait.</p>", ""),
        ("Examen physique", "<p>Air, souffle, pouls, conscience, pupilles, chaleur, glycémie capillaire si le malaise y fait penser. L'examen raffiné ne retarde pas l'appel.</p>", ""),
        ("Approche syndromique", "<p>Un coma n'est pas une ébriété sociale. Une douleur thoracique ne se surveille pas à la maison. Une convulsion n'attend pas le matin.</p>", ""),
        ("Diagnostic positif", "<p>Clinique et contexte. Le nom du produit peut manquer. L'orientation n'attend pas l'étiquette.</p>", ""),
        ("Examens complémentaires",
         "<p><em>9.a Gold standard.</em> Pas de dosage universel dans les pages lues. L'évaluation des fonctions vitales, l'avis du 145 et les examens des urgences tiennent ce rôle.</p>"
         "<p><em>9.b 1re intention.</em> Constantes et appel. Le laboratoire toxicologique vient à l'hôpital.</p>"
         '<div class="tw"><table><thead><tr><th>Cas</th><th>Vital</th><th>Où doser</th><th>Hypothèse</th></tr></thead><tbody>'
         "<tr><td>normal</td><td>conscience et souffle tenus</td><td>selon le 145</td><td>surveillance possible si le 145 le dit</td></tr>"
         "<tr><td>positif</td><td>coma, détresse, convulsion, poitrine</td><td>urgences</td><td>intoxication grave</td></tr>"
         "<tr><td>limite</td><td>somnolence réveillable</td><td>ne pas trancher seul</td><td>145 ou 144</td></tr>"
         "<tr><td>discordant</td><td>discours rassurant, station debout impossible</td><td>secondaire</td><td>croire l'examen</td></tr></tbody></table></div>",
         ""),
        ("Arbre décisionnel", "<p>Vital atteint : 144, 145 en appui. Exposition sans signe, personne surveillée : le 145 peut accepter une veille, décision qui est la sienne. Charbon et vomitif ne sont pas dans l'extrait lu : on ne les lance pas.</p>", ""),
        ("Prise en charge",
         "<p>L'hôpital traite. Le médecin de ville reconnaît, appelle, transmet le produit supposé. Il ne démarre pas un antidote dont la dose est absente des PDF, sauf à suivre un protocole d'urgence qu'il a alors devant lui.</p>"
         '<div class="urgence"><strong>Urgence — conduite chronologique.</strong> Ne pas laisser seul. 144 si conscience, souffle, cœur ou convulsion. 145 pour le nom du produit. Rester si ça empire.</div>',
         ""),
        ("Prévention", "<p>Les produits associés se cherchent après l'épisode, pas pendant le coma. C'est la suite que décrit la stratégie alcool.</p>", ""),
        ("Points clés", "<p>145 pour l'avis, 144 pour le transport. Pas de geste de fortune. Le sevrage d'alcool est une autre urgence.</p>", ""),
        ("Pièges", "<p>Dose mortelle calculée. Vomissement provoqué. Laboratoire de ville en attendant.</p>", ""),
    ]

def manque():
    return [
        ("Définition et sémantique", "<p>Seul le sevrage alcoolique est minuté dans les sources : 3 à 10 jours, urgence qui peut tuer. Le sevrage nicotinique dure 3 semaines à 3 mois et n'est pas cette urgence.</p>", ""),
        ("Épidémiologie", "<p>Pas de fréquence suisse du delirium dans le PDF. Le texte dit que ça peut tuer. On s'en tient à cela.</p>", ""),
        ("Physiopathologie", "<p>Agitation, anxiété, insomnie, tremblement, sueurs, tachycardie, hypertension, puis fièvre, délire, convulsions. Séquence HUG 2021, pas une liste générique.</p>", ""),
        ("Étiologie et facteurs de risque", "<p>Sevrage déjà compliqué, comorbidité lourde, benzodiazépines importantes : ces trois-là ferment la porte de la ville.</p>", ""),
        ("Anamnèse", "<p>Heure du dernier verre, convulsions, delirium ancien, benzodiazépines, solitude, entourage à bout. Ces questions choisissent l'hôpital mieux qu'un discours de motivation.</p>", ""),
        ("Examen physique", "<p>Tremblement, sueurs, pouls, tension, température, orientation. Un calme initial ne dure pas forcément : le texte prévoit des revues tous les deux ou trois jours.</p>", ""),
        ("Approche syndromique", "<p>Craving du tabac, manque opioïde et sevrage alcoolique ne partagent ni durée ni médicament.</p>", ""),
        ("Diagnostic positif", "<p>Signes cardinaux après réduction de l'alcool : le sevrage est reconnu. L'AUDIT peut attendre.</p>", ""),
        ("Examens complémentaires",
         "<p><em>9.a Gold standard.</em> Le CIWA-Ar, recommandé par la stratégie pour doser l'oxazépam mieux qu'une baisse fixe.</p>"
         "<p><em>9.b 1re intention.</em> Voir les signes et le lieu. Si la personne convulse, le score attend les secours.</p>"
         '<div class="tw"><table><thead><tr><th>Cas</th><th>Tableau</th><th>Conduite écrite en 2021</th></tr></thead><tbody>'
         "<tr><td>normal</td><td>arrêt sans signe</td><td>pas de sevrage médicamenteux</td></tr>"
         "<tr><td>positif</td><td>signes cardinaux</td><td>thiamine 300 mg par jour, trois semaines, oxazépam selon CIWA</td></tr>"
         "<tr><td>limite</td><td>tremblement seul, histoire trouble</td><td>revoir très vite</td></tr>"
         "<tr><td>discordant</td><td>score encore bas, delirium ancien</td><td>hôpital malgré le score</td></tr></tbody></table></div>",
         ""),
        ("Arbre décisionnel", "<p>Contre-indication absolue ou convulsion : hôpital et 144 si ça convulse maintenant. Sinon ambulatoire avec revues rapprochées et entourage fiable.</p>", ""),
        ("Prise en charge",
         "<p>Vitamine B1, 300 mg par jour, trois semaines. Oxazépam, 60 à 200 mg par jour, quatre à six prises, baisse d'environ 20 pour cent par jour ou adaptation au CIWA. Posologie propre à l'alcool, stratégie HUG 2021. Elle ne migre pas vers un autre produit.</p>"
         '<div class="urgence"><strong>Urgence — conduite chronologique.</strong> Reconnaître sueurs, tremblement, tachycardie. Chercher la contre-indication absolue. Hospitaliser si elle est là ou si ça convulse. Sinon thiamine, oxazépam, revue sous trois jours.</div>',
         ""),
        ("Prévention", "<p>Ne pas proposer la ville à qui a déjà convulsé. Dire à l'entourage que cela dure plusieurs jours.</p>", ""),
        ("Points clés", "<p>Trois à dix jours. CIWA préférable au pourcentage seul. Thiamine 300 mg par jour. Oxazépam 60 à 200 mg par jour. Hôpital si delirium ou convulsion antérieurs.</p>", ""),
        ("Pièges", "<p>Schéma recopié sur le tabac ou les opioïdes. Thiamine oubliée. Départ en ville après un delirium tremens.</p>", ""),
    ]

def phase():
    return [
        ("Définition et sémantique",
         "<p>Le champ réunit Tabagisme, Trouble de l'usage d'alcool, Trouble de l'usage d'opioïdes, Trouble de l'usage de cannabis, Trouble de l'usage de stimulants, Usage problématique de médicaments contrôlés, Jeu d'argent excessif, Usage excessif des jeux vidéo, Intoxication aiguë et Syndrome de sevrage menaçant. Seuls l'alcool (HUG 2021) et le tabac (HUG 2024) ont un chapitre chiffré lu. Le reste s'appuie sur les critères CIM-10 cités dans la stratégie tabac et sur la liste des dépendances conjointes de la stratégie alcool.</p>"
         '<div class="tw"><table><caption>Fiches, ordre d\'enseignement</caption><thead><tr><th>DX</th><th>Nom</th></tr></thead><tbody>'
         "<tr><td>DX.1</td><td>Tabagisme</td></tr><tr><td>DX.2</td><td>Trouble de l'usage d'alcool</td></tr>"
         "<tr><td>DX.3</td><td>Trouble de l'usage d'opioïdes</td></tr><tr><td>DX.4</td><td>Trouble de l'usage de cannabis</td></tr>"
         "<tr><td>DX.5</td><td>Trouble de l'usage de stimulants</td></tr><tr><td>DX.6</td><td>Usage problématique de médicaments contrôlés</td></tr>"
         "<tr><td>DX.7</td><td>Jeu d'argent excessif</td></tr><tr><td>DX.8</td><td>Usage excessif des jeux vidéo</td></tr>"
         "<tr><td>DX.9</td><td>Intoxication aiguë</td></tr><tr><td>DX.10</td><td>Syndrome de sevrage menaçant</td></tr>"
         "</tbody></table></div>",
         ""),
        ("Épidémiologie", "<p>Chiffre lu pour l'alcool : au moins 25 pour cent des patients de premier recours. Chiffre lu pour le tabac : environ 10 ans d'espérance de vie en moins, via l'OFSP cité par les HUG. Pas de classement des dix fiches par une prévalence absente.</p>", ""),
        ("Physiopathologie", "<p>Durée lue du sevrage alcoolique : 3 à 10 jours, risque vital. Durée lue du sevrage nicotinique : 3 semaines à 3 mois. Les médicaments ne se prêtent pas.</p>", ""),
        ("Étiologie et facteurs de risque", "<p>Alcool : famille, autres produits, difficultés sociales, restauration. Tabac : génétique, trauma, entourage. Listes distinctes, pas une cause unique.</p>", ""),
        ("Anamnèse", "<p>Alcool et tabac se demandent largement. Le tabac, après accord. Les autres produits et le jeu se demandent quand l'un des deux est présent, parce que la stratégie alcool les met dans la même phrase.</p>", ""),
        ("Examen physique", "<p>Vitaux d'abord si intoxication ou sevrage. Signes chroniques d'alcool ensuite, sans les exiger. Conséquences du tabac si la plainte est le souffle, le cœur ou une plaie.</p>", ""),
        ("Approche syndromique", "<p>Excès, dépendance, intoxication, sevrage : quatre temps. L'AUDIT ne classe que l'alcool. Le CIWA ne guide que son sevrage.</p>", ""),
        ("Diagnostic positif", "<p>Alcool : verres et AUDIT. Tabac : CIM-10 et Fagerström. Ailleurs : CIM-10 sans seuil de laboratoire lu.</p>", ""),
        ("Examens complémentaires",
         "<p><em>9.a Gold standard.</em> Alcool, AUDIT. Tabac, entretien universel et Fagerström. Intoxication, fonctions vitales. Sevrage d'alcool, CIWA.</p>"
         "<p><em>9.b 1re intention.</em> Question simple, outil du produit, urgences si un vital ou une douleur thoracique apparaît.</p>"
         '<div class="tw"><table><caption>Outils effectivement lus</caption><thead><tr><th>Situation</th><th>Outil</th><th>Seuil dans le PDF</th></tr></thead><tbody>'
         "<tr><td>Alcool</td><td>AUDIT</td><td>moins de 7 faible risque ; au-dessus de 7 ou 8 excès ; au-dessus de 13 dépendance</td></tr>"
         "<tr><td>Tabac</td><td>Fagerström</td><td>0-2 nulle ; 3-4 faible ; 5-6 modérée ; 7-10 forte</td></tr>"
         "<tr><td>Sevrage alcool</td><td>CIWA</td><td>guide l'oxazépam ; les bornes internes du score ne sont pas recopiées</td></tr>"
         "<tr><td>Autres</td><td>entretien CIM-10</td><td>pas de seuil biologique lu</td></tr></tbody></table></div>",
         ""),
        ("Arbre décisionnel", "<p>Vital, convulsion ou poitrine : 144. Produit et personne encore surveillable : 145. Détresse sans vital : 143. Jeune : 147. Alcool dépendant : stratégie 2021. Tabac : patch ou bupropion selon 2024.</p>", ""),
        ("Prise en charge",
         "<p>Alcool : thiamine 300 mg par jour trois semaines, oxazépam 60 à 200 mg par jour selon CIWA, puis acamprosate ou naltrexone. Tabac : patch 21 mg puis 14 mg puis 7 mg, bupropion 150 mg puis 150 mg deux fois par jour. Varénicline retirée en 2022 selon le PDF. Ailleurs, pas de posologie lue.</p>"
         '<div class="urgence"><strong>Urgence — conduite chronologique.</strong> Reconnaître sevrage alcoolique et intoxication. Hôpital si contre-indication absolue. Ne pas exporter ces milligrammes.</div>',
         ""),
        ("Prévention", "<p>Demander largement. Critiquer les quantités sans humilier. Accepter une réduction quand l'abstinence n'est pas le premier pas juste. Inclure les malades psychiatriques dans l'aide au tabac.</p>", ""),
        ("Points clés", "<p>Deux PDF chiffrés, dix fiches. Seuils réservés à l'alcool et au tabac. Sevrage d'alcool possiblement mortel. Pas de dose ailleurs.</p>", ""),
        ("Pièges", "<p>Remplir par des phrases clones. Citer le référentiel de liens comme recommandation. Étendre l'oxazépam au jeu ou à la cocaïne.</p>", ""),
    ]

DX = [
    (1, "Tabagisme", tabac),
    (2, "Trouble de l'usage d'alcool", alcool),
    (3, "Trouble de l'usage d'opioïdes", opio),
    (4, "Trouble de l'usage de cannabis", cannabis),
    (5, "Trouble de l'usage de stimulants", stim),
    (6, "Usage problématique de médicaments contrôlés", benzo),
    (7, "Jeu d'argent excessif", jeu),
    (8, "Usage excessif des jeux vidéo", ecran),
    (9, "Intoxication aiguë", intox),
    (10, "Syndrome de sevrage menaçant", manque),
]

def main():
    for old in OUT.glob("LOT_129_*.html"):
        old.unlink()
    (OUT / "LISTE_DX_CANONIQUE.md").write_text(
        "# Liste canonique LOT 129\n\n" + "\n".join("DX." + str(n) + " — " + nom for n, nom, _ in DX) + "\n",
        encoding="utf-8",
    )
    files = [("LOT_129_Phase_A_V0.html", "dx0", "Phase A — Usage non médical de substances et addictions", phase())]
    for n, nom, fn in DX:
        files.append(("LOT_129_Phase_B_V0_DX." + str(n) + ".html", "dx" + str(n), "DX." + str(n) + " — " + nom, fn()))
    for name, pre, h2, blocks in files:
        text = wrap(pre, h2, blocks)
        path = OUT / name
        path.write_text(text, encoding="utf-8")
        print(name, path.stat().st_size)

if __name__ == "__main__":
    main()
