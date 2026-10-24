#!/usr/bin/env python3
"""Génère les HTML V7 de LOT_183, DX.5 à DX.10. Agent B07. Ne fait pas d'audit."""
from html import escape
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))
DATE = "24.10.2026"

def e(s):
    return escape(s, quote=True)

def p(text):
    return f"<p style='margin:4px 0 6px;'>{text}</p>"

def table(headers, rows):
    th = "".join(
        f"<th style='background:#d4e6f1;text-align:left;vertical-align:top;'>{e(h)}</th>"
        for h in headers
    )
    body = []
    for row in rows:
        tds = "".join(f"<td style='vertical-align:top;'>{c}</td>" for c in row)
        body.append(f"<tr>{tds}</tr>")
    return (
        "<div style='overflow-x:auto;'><table border='1' cellpadding='7' cellspacing='0' "
        "style='width:100%;border-collapse:collapse;font-size:0.92em;'>"
        f"<thead><tr>{th}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"
    )

def inline(term, paragraphs, source):
    inner = "".join(p(x) for x in paragraphs)
    return (
        f"<details style='display:inline;'><summary style='display:inline;cursor:pointer;"
        f"color:#1f618d;text-decoration:underline dotted;'>{e(term)}</summary>"
        f"<div style='display:block;margin:4px 0 8px;padding:8px;background:#f4f6f7;"
        f"border-left:3px solid #1f618d;font-size:0.93em;'>{inner}"
        f"<em>Source : {e(source)}.</em></div></details>"
    )

def fen(title, blocks, source):
    inner = "".join(blocks)
    return (
        "<details style='margin:8px 0;border-left:4px solid #2980b9;background:#ebf5fb;"
        f"padding:6px 10px;'><summary style='cursor:pointer;font-weight:bold;color:#1a5276;'>"
        f"{e(title)}</summary><div style='margin-top:6px;'>{inner}"
        f"<em>Source : {e(source)}.</em></div></details>"
    )

def point(n, title, chunks):
    return (
        f"<div style='margin:16px 0 10px;'><strong>{n}. {e(title)}</strong><br>"
        + "".join(chunks)
        + "</div>"
    )

def ital(label):
    return f"<em>{e(label)}</em>"

def page(title, h2, intro, monos, sources, fin_tag):
    src_li = []
    for sid, desc, url in sources:
        src_li.append(
            f"<li style='margin:4px 0;'><strong>[{e(sid)}]</strong> {e(desc)} "
            f"<span style='word-break:break-all;'>{e(url)}</span> "
            f"(consulté le {DATE}).</li>"
        )
    body = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
</head>
<body>
<div style="font-family:sans-serif;line-height:1.65;max-width:980px;margin:auto;">
<h2 style="color:#1a5276;border-bottom:3px solid #2980b9;padding-bottom:6px;">{h2}</h2>
<p style="color:#444;">{intro}</p>
{''.join(monos)}
<h3>Sources</h3>
<ol>
{''.join(src_li)}
</ol>
<p>Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin.</p>
<p>Lacunes assumées de cette rédaction : l'Appel A et la partie 1 n'ont pas été lus (dossier Drive inaccessible, aucune branche GitHub LOT_183). Les noms et l'ordre DX.5 à DX.10 sont ceux de la liste déjà publiée du SSP O2.1. Aucune information professionnelle AIPS n'a été ouverte : aucune dose chiffrée n'est donc prescrite ici.</p>
</div>
</body>
</html>
<!-- FIN_FICHIER {fin_tag} -->
"""
    # wrap long lines without changing text
    out = []
    for line in body.split("\n"):
        if len(line) <= 2400:
            out.append(line)
            continue
        buf = ""
        for part in line.replace("><", ">\n<").split("\n"):
            if len(buf) + len(part) > 2000:
                out.append(buf)
                buf = part
            else:
                buf += part
        if buf:
            out.append(buf)
    text = "\n".join(out) + "\n"
    # no line over 3000
    for i, line in enumerate(text.split("\n"), 1):
        if len(line) > 3000:
            raise SystemExit(f"ligne {i} trop longue ({len(line)})")
    return text

def mono(dx, name, badge, inner):
    return (
        "<details open style='border:1px solid #2980b9;border-radius:6px;margin:18px 0;"
        "padding:10px 14px;background:#fff;'><summary style='cursor:pointer;font-size:1.15em;"
        f"font-weight:bold;color:#1a5276;'>{e(dx)} — {e(name)} "
        f"<span style='font-size:0.8em;color:#2e8b57;'>{e(badge)}</span></summary>"
        f"{inner}</details>"
    )

# ---------- shared method snippets that stay diagnosis-specific via arguments ----------

def auxo_table(src):
    return table(
        ["Mesure", "Ce que la source suisse demande", "Lecture"],
        [
            ["Taille des parents", "La mesurer soi-même, car c'est un acte médical, puis l'inscrire sur la courbe.", "Sans mesure, la cible parentale n'existe pas."],
            ["Taille cible", "[taille maternelle + taille paternelle ± 13 cm] / 2. On soustrait 13 cm chez la fille et on ajoute 13 cm chez le garçon.", "L'intervalle lu est ± 8,5 cm, soit ± 2 déviations standards."],
            ["Petite taille statistique", "En dessous du 3e percentile, soit −1,88 déviation standard, sur la courbe utilisée.", "Il y a statistiquement autant d'enfants sous le 3e percentile qu'au-dessus du 97e."],
            ["Canal après 2 ans", "Après le deuxième anniversaire, l'enfant devrait rester dans le canal de percentile hérité jusqu'à la puberté.", "Un changement de canal après 2 ans est un signe suspect."],
            ["Courbes 2026", "pédiatrie suisse recommande les courbes nationales PEZZ à compter du 15 juin 2026.", "Les seuils de petite taille restent ceux des sociétés compétentes, pas un nouveau chiffre inventé par la courbe."],
        ],
    )

def exemple_cible(src):
    # (162+175+13)/2 = 175 ; (162+175-13)/2 = 162
    return [
        p("Exemple chiffré, calcul dérivé à partir de la formule lue. La mère mesure 162 cm et le père mesure 175 cm. La somme parentale vaut 337 cm."),
        p("Pour un garçon, on calcule (337 + 13) / 2 = 175 cm. Pour une fille, on calcule (337 − 13) / 2 = 162 cm. L'intervalle de ± 8,5 cm place le garçon entre 166,5 et 183,5 cm, et la fille entre 153,5 et 170,5 cm."),
        p("Ce calcul ne prédit pas une maladie. Il situe seulement l'enfant par rapport à ses parents mesurés."),
    ]

# ===================== DX5 =====================

def dx5():
    S = {
        "espe": "[S201]",
        "gal": "[S202]",
        "jenni": "[S203]",
        "ps": "[S204]",
        "pezz": "[S205]",
    }
    c = []
    c.append(point(1, "Définition et sémantique", [
        p("Le " + inline("retard constitutionnel de croissance et de puberté", [
            "L'ESPE décrit une petite taille temporaire due à un retard du développement pubertaire, chez un enfant par ailleurs en bonne santé, sans anomalie physique qui expliquerait le retard.",
            "Le dépliant précise que la situation est plus fréquente chez les garçons que chez les filles, et qu'elle trouble autant les deux sexes.",
            "Piège : appeler « constitutionnel » un hypogonadisme permanent ou un syndrome de Turner. La définition exige que l'on ait écarté ces entités.",
        ], S["espe"]) + " est une variante du tempo de maturation, et non une maladie d'organe."),
        p("La puberté commence en moyenne à 10–11 ans chez la fille et à 12 ans chez le garçon. L'ESPE demande d'adresser l'enfant s'il n'existe aucun signe physique de puberté à 13 ans chez la fille ou à 14 ans chez le garçon."),
        fen("Fenêtre 1.1 — Trois cadres décrits par la revue européenne", [
            p("Galazzi et Persani, dans Minerva Endocrinologica, distinguent trois situations en s'appuyant sur la classification ESPE de 2007."),
            table(
                ["Cadre", "Ce que la revue écrit", "Conséquence"],
                [
                    ["Type 1", "Enfant prépubère, stade G1 à 14 ans ou plus chez le garçon, ou B1 à 13 ans ou plus chez la fille, souvent avec une vitesse lente et un âge osseux retardé d'au moins un an, et une histoire familiale.", "C'est le tableau classique qui motive le bilan."],
                    ["Type 2", "Puberté commencée, mais progression lente, avec un stade génital inférieur à −2 déviations standards par rapport aux nomogrammes.", "On ne conclut pas parce que « quelque chose a commencé »."],
                    ["Type 3 possible", "Avant ces âges, si trois des quatre conditions suivantes sont réunies : stade de Tanner inférieur à −1 DS, âge osseux retardé de plus d'un an, taille basse pour la cible, histoire familiale de puberté tardive.", "Ce cadre reste une proposition de la revue, pas un seuil suisse officiel."],
                ],
            ),
            p("Piège d'examen : retenir le diagnostic sur la seule histoire d'un père qui a grandi tard, sans âge osseux et sans exclusion d'une cause organique."),
        ], S["gal"]),
    ]))
    c.append(point(2, "Épidémiologie (Suisse, puis Europe)", [
        p("La revue européenne estime que le retard constitutionnel touche 2 à 2,5 % de la population. Elle écrit qu'il représente jusqu'à 80 % des pubertés retardées chez les garçons et environ 33 % chez les filles, avec une cohorte géorgienne de filles où la part tombe autour de 10 % parce que les maladies organiques y dominent."),
        p("La fréquence suisse de cette entité, l'incidence cantonale et la mortalité ne figurent pas dans les sources ouvertes : donnée non trouvée dans les sources consultées. L'enjeu suisse est auxologique : pédiatrie suisse rappelle que la courbe sert à détecter tôt une anomalie, et le PEZZ demande une mesure au moins annuelle."),
        fen("Fenêtre 2.1 — Ce que l'on peut et ne peut pas dire du chiffre", [
            p("Le chiffre de 2 à 2,5 % décrit la condition dans la revue, pas un registre OFS. Le biais de recours aux soins est explicite : les séries familiales touchent les deux sexes, mais les garçons consultent davantage."),
            p("Histoire naturelle lue : le pic de croissance pubertaire est atténué quand la puberté est très tardive, et la taille adulte peut rester en dessous de la cible parentale. L'ESPE le dit pour les retards extrêmes."),
            p("Enjeu : la souffrance sociale et scolaire justifie parfois un traitement court, même si la condition est transitoire."),
        ], S["gal"] + ", " + S["espe"]),
    ]))
    c.append(point(3, "Physiopathologie", [
        p("Après la minipuberté, l'axe hypothalamo-hypophyso-gonadique se tait pendant l'enfance, puis se réveille. La revue décrit des neurotransmetteurs qui stimulent cet axe, dont la kisspeptine, et d'autres qui l'inhibent. La leptine signale la disponibilité énergétique."),
        p("Le cartilage de croissance attend le pic de stéroïdes sexuels. Si ce pic tarde, la vitesse prépubertaire ralentit et l'âge osseux prend du retard, ce qui laisse du temps de croissance. L'ESPE rappelle toutefois qu'un retard extrême peut empêcher d'atteindre la cible parentale."),
        table(
            ["Lésion ou perturbation", "Exploration qui la montre", "Ce qui la corrige, et par quel mécanisme"],
            [
                ["Réveil tardif de l'axe gonadotrope", "Stade de Tanner encore prépubère aux âges seuils, LH et stéroïdes bas, âge osseux retardé.", "Le temps, le plus souvent. Un stéroïde sexuel à faible dose, si on le décide, mime le démarrage et accélère la vitesse sans être une guérison d'un organe malade."],
                ["Pic statural atténué", "Vitesse de croissance comparée aux pairs déjà pubères ; la revue cite souvent plus de 3,6 cm par an chez les garçons, donc ralentie mais non effondrée.", "Le stéroïde sexuel avance le calendrier du pic. Il ne crée pas de cartilage."],
                ["Souffrance psychosociale", "Entretien sur l'école, les pairs et l'humeur.", "Explication, parfois accompagnement. Ce n'est pas un médicament."],
            ],
        ),
        fen("Fenêtre 3.1 — Pourquoi l'âge osseux retarde", [
            p("L'ESPE explique que les espaces entre les extrémités des os longs se ferment à la fin de la puberté, surtout sous l'effet des œstrogènes. Tant que la puberté n'a pas démarré, ces espaces restent ouverts et l'âge osseux, lu sur la radiographie de la main et du poignet gauches, est inférieur à l'âge civil."),
            p("Exemple : un garçon de 14 ans sans volume testiculaire de 4 mL, dont l'âge osseux a au moins un an de retard, entre dans le type 1 décrit par la revue. Le retard osseux est le capital restant, pas une preuve que la taille finale sera normale."),
        ], S["espe"] + ", " + S["gal"]),
    ]))
    c.append(point(4, "Démarche diagnostique", [
        p("On exclut d'abord ce qui menace, puis on reconnaît la variante. L'ESPE demande d'écarter l'insuffisance gonadique, le syndrome de Turner chez la fille, une dysplasie osseuse et un déficit en hormone de croissance, habituellement beaucoup plus petit."),
        table(
            ["Hypothèse à ne pas manquer", "Signe ou examen qui tranche", "Piège"],
            [
                ["Insuffisance gonadique", "Gonadotrophines élevées alors que les stéroïdes sont bas.", "Rassurer trop vite un garçon dont les testicules ne grandissent jamais."],
                ["Syndrome de Turner", "Caryotype chez toute fille dont la puberté tarde.", "Attendre une dysmorphie évidente. L'ESPE demande le caryotype."],
                ["Déficit en hormone de croissance", "Taille beaucoup plus basse et vitesse effondrée, puis tests de stimulation après avoir écarté les causes générales.", "Traiter par hormone de croissance un simple retard, surtout sans priming discuté chez le prépubère de plus de 11 ans (garçon) ou 10 ans (fille) selon les guides cités par la revue."],
                ["Hypogonadisme hypogonadotrope congénital", "Pas de progression après un essai court de stéroïde, anosmie ou cryptorchidie selon le contexte. La revue cite des seuils d'inhibine B et de pic de LH après agoniste, qui se chevauchent.", "Croire qu'un dosage unique sépare les deux entités au premier jour."],
            ],
        ),
    ]))
    c.append(point(5, "Anamnèse ciblée et drapeaux rouges", [
        p("On demande l'âge des règles de la mère et l'époque de la poussée du père, parce que la revue fait de l'histoire familiale un critère des types 1 et 3. On demande aussi l'appétit : ces enfants mangent parfois peu et ont un indice de masse corporelle plutôt bas, et la leptine relie l'énergie à l'axe."),
        p("Drapeaux qui interdisent de conclure à une variante : céphalées matinales, vomissements ou trouble visuel (lésion centrale, hors de ce DX mais à ne pas manquer), fille sans développement mammaire à 13 ans sans caryotype, vitesse effondrée, signes de maladie chronique, cryptorchidie ou micropénis qui orientent vers un hypogonadisme."),
        fen("Fenêtre 5.1 — Questions et leur raison", [
            table(
                ["Question", "Raison physiopathologique", "Réponse qui inquiète"],
                [
                    ["Quand la mère a-t-elle eu ses règles, et quand le père a-t-il grandi ?", "Le tempo se transmet souvent de façon autosomique dominante, avec une pénétrance incomplète.", "Aucun antécédent familial et un tableau sévère."],
                    ["L'enfant sent-il les odeurs ? Les testicules sont-ils descendus ?", "L'anosmie et la cryptorchidie rapprochent d'un hypogonadisme hypogonadotrope, pas d'un simple retard.", "Anosmie ou testicule non palpable."],
                    ["La taille a-t-elle cassé, ou suit-elle un canal bas ?", "Une cassure après 2 ans, selon le PEZZ, est suspecte d'une maladie et non d'un tempo.", "Perte de canal."],
                ],
            ),
        ], S["gal"] + ", " + S["pezz"]),
    ]))
    c.append(point(6, "Examen physique ciblé, région par région", [
        p("Le normal vient d'abord. Un enfant en bonne santé a une vitesse qui suit son canal après 2 ans, des proportions harmonieuses et un stade pubertaire cohérent avec son âge osseux."),
        p(ital("6.1 Mesures.") + " On mesure la taille debout, le poids et le périmètre crânien, puis on calcule la cible parentale sur des parents mesurés. La technique précède l'interprétation."),
        p(ital("6.2 Puberté.") + " On palpe le tissu mammaire et on estime le volume testiculaire. L'absence de tout signe à 13 ans chez la fille ou à 14 ans chez le garçon déclenche l'évaluation, selon l'ESPE."),
        p(ital("6.3 Proportions et dysmorphie.") + " Une disproportion oriente vers une dysplasie osseuse, que l'ESPE demande d'envisager. On cherche aussi les signes de Turner chez la fille."),
        fen("Fenêtre 6.1 — Vitesse, exemple recalculé", [
            p("La vitesse se calcule en centimètres par an. Exemple, calcul dérivé : 118,0 cm à 6,0 ans et 122,4 cm à 6,8 an. La différence est 4,4 cm sur 0,8 an, soit 4,4 / 0,8 = 5,5 cm par an."),
            p("Ce chiffre illustre la méthode. Il ne dit pas, à lui seul, si ce garçon a un retard constitutionnel. La revue indique que la vitesse des garçons avec ce retard dépasse souvent 3,6 cm par an, donc un chiffre très inférieur impose de chercher une autre cause."),
        ], S["gal"]),
    ]))
    c.append(point(7, "Approche syndromique", [
        p(ital("7.1 Tempo pubertaire retardé.") + " Le syndrome réunit une petite taille relative, une puberté absente ou lente et un âge osseux retardé, chez un enfant par ailleurs sain."),
        p("Signes fonctionnels : l'adolescent se plaint d'être plus petit et moins développé que ses camarades, et parfois d'une souffrance à l'école. Signes physiques : stade prépubère au-delà du seuil, proportions conservées, pas de dysmorphie."),
        fen("Fenêtre 7.1 — Chaque signe, sa recherche, son mécanisme", [
            table(
                ["Signe", "Définition et recherche", "Mécanisme"],
                [
                    ["Absence de thélarche à 13 ans", "Pas de bourgeon mammaire palpable. On palpe, on ne se fie pas au regard.", "L'ovaire ne sécrète pas encore assez d'œstradiol parce que l'axe ne s'est pas réveillé, ou parce qu'il est en panne : le caryotype et les gonadotrophines tranchent."],
                    ["Volume testiculaire encore infantile à 14 ans", "Comparaison à l'orchidomètre. Le premier signe pubertaire masculin est la croissance testiculaire.", "Les cellules de Leydig attendent la LH. Sans LH, le volume ne passe pas le seuil pubertaire."],
                    ["Âge osseux retardé d'au moins un an", "Radiographie de la main et du poignet gauches, comparée à un atlas.", "Les œstrogènes n'ont pas encore fait mûrir le cartilage."],
                ],
            ),
            p("Piège : coter un stade sur une adipomastie. On palpe une glande, on ne compte pas un pli graisseux."),
        ], S["espe"] + ", " + S["gal"]),
    ]))
    c.append(point(8, "Diagnostic positif et critères", [
        p("Aucune société suisse lue ici ne publie une liste numérotée unique. Le diagnostic opérationnel, d'après l'ESPE et la revue, est un diagnostic d'élimination : enfant sain, puberté absente aux seuils de 13 et 14 ans ou progression lente, âge osseux retardé, histoire familiale fréquente, et exclusion du Turner, de l'insuffisance gonadique, de la dysplasie et du déficit somatotrope."),
        p("Ce qui ne suffit pas : un père « qui a grandi tard », une taille sous le 3e percentile, ou un dosage unique de LH basse chez un prépubère, car une LH basse est alors physiologique."),
        fen("Fenêtre 8.1 — Ce qui permet de retenir, et ce qui oblige à surseoir", [
            p("On peut retenir le cadre quand le type 1 est réuni et que les examens d'exclusion sont négatifs. On sursoit quand la fille n'a pas de caryotype, quand la vitesse est effondrée, ou quand un signe neurologique existe."),
            p("La revue rappelle que des variants hétérozygotes de gènes d'hypogonadisme hypogonadotrope ont été trouvés dans jusqu'à 7 % des cohortes de retard constitutionnel. Un test génétique négatif ou non fait ne ferme donc pas le dossier à lui seul."),
        ], S["gal"]),
    ]))
    c.append(point(9, "Examens complémentaires", [
        p(ital("9.a Gold standard.") + " Il n'existe pas de gold standard biologique unique. Le diagnostic est clinique et évolutif. L'âge osseux de la main et du poignet gauches est l'examen qui mesure le temps de croissance restant, selon l'ESPE."),
        p(ital("9.b Première intention.") + " Courbe sur les références suisses recommandées depuis le 15 juin 2026, cible parentale, stade pubertaire, âge osseux, TSH et thyroxine libre pour ne pas manquer une hypothyroïdie, et caryotype chez la fille. LH, FSH et stéroïde sexuel classent un hypogonadisme hypergonadotrope."),
        p(ital("9.c Alternatives.") + " Si l'enfant ne peut pas tenir debout, on mesure couché et on le note, car le changement de méthode fausse la vitesse. Donnée non trouvée dans les sources consultées pour un protocole suisse d'adaptation chez l'enfant porteur d'un stimulateur cardiaque : l'âge osseux n'est pas une IRM."),
        p(ital("9.d Deuxième intention.") + " Tests de stimulation de l'hormone de croissance seulement si la taille et la vitesse évoquent un déficit, avec la question du priming chez le prépubère plus âgé. IRM hypothalamo-hypophysaire si un signe neurologique ou un déficit confirmé l'exige, pas de routine dans la variante simple."),
        fen("Fenêtre 9.1 — Interpréter l'âge osseux et les gonadotrophines", [
            table(
                ["Résultat", "Signification", "Conduite"],
                [
                    ["Âge osseux retardé d'au moins 1 an, enfant sain", "Capital de croissance encore ouvert, compatible avec le type 1.", "Surveillance, explication, traitement court seulement si la souffrance ou le retard extrême le justifie."],
                    ["Âge osseux égal à l'âge civil et parents petits", "Le tempo n'est pas en retard. On se rapproche d'une petite taille familiale.", "On ne promet pas un rattrapage pubertaire."],
                    ["FSH élevée, œstradiol ou testostérone bas", "Atteinte gonadique, pas un simple retard.", "Orienter, caryotype chez la fille, ne pas rassurer."],
                    ["LH et FSH basses, prépubère", "Résultat attendu avant le réveil de l'axe. Il ne distingue pas le retard constitutionnel de l'hypogonadisme hypogonadotrope.", "On suit la progression clinique sur plusieurs mois."],
                ],
            ),
            p("Grossesse : ces examens concernent l'enfant. On ne dose pas une gonadotrophine pour ce diagnostic chez une adolescente possiblement enceinte sans avoir écarté la grossesse par le test adapté. Donnée non trouvée pour un algorithme suisse spécifique dans les sources ouvertes."),
        ], S["espe"] + ", " + S["gal"] + ", " + S["ps"]),
    ]))
    c.append(point(10, "Arbre décisionnel", [
        p("Si un signe neurologique existe, on cherche une lésion avant de parler de variante. Si la fille a 13 ans sans sein, on demande le caryotype en même temps que le bilan. Si le garçon a 14 ans sans croissance testiculaire, on mesure LH, FSH et testostérone, et l'âge osseux."),
        p("Si l'âge osseux est retardé, la vitesse n'est pas effondrée, la famille raconte un tempo lent et les examens d'exclusion sont négatifs, on explique le retard constitutionnel et on revoit l'enfant. Si le volume testiculaire grandit seul, on confirme le cadre. S'il ne se passe rien après la surveillance convenue, on reprend l'hypothèse d'un hypogonadisme permanent."),
        fen("Fenêtre 10.1 — Embranchements", [
            table(
                ["Observation", "Décision"],
                [
                    ["Céphalée matinale, vomissement ou trouble visuel", "Ne pas classer en variante. Imagerie selon l'urgence clinique."],
                    ["Fille, aucun sein à 13 ans", "Caryotype et gonadotrophines."],
                    ["Garçon, testicules non pubères à 14 ans, âge osseux retardé, bilan d'exclusion négatif", "Retard constitutionnel probable. Surveillance ou stéroïde faible si souffrance."],
                    ["Vitesse très basse et taille très inférieure à −2,5 DS", "Ne pas s'arrêter au retard constitutionnel. La revue dit que la taille de ce retard n'est habituellement pas si sévère."],
                ],
            ),
        ], S["gal"] + ", " + S["espe"]),
    ]))
    c.append(point(11, "Prise en charge selon les recommandations suisses", [
        p(ital("A- But.") + " Le but est d'atteindre une puberté spontanée et une taille adulte aussi proche que possible de la cible, sans accélérer la maturation osseuse au-delà du rythme normal. L'ESPE fixe la durée normale de la puberté entre trois et quatre ans, et demande qu'un traitement, s'il a lieu, ne fasse pas parcourir la puberté plus vite qu'en un à deux ans."),
        p(ital("B- Moyens.") + " Le moyen de première ligne est l'explication et l'attente, car l'ESPE écrit qu'aucun traitement n'est habituellement nécessaire. Si l'adolescent souffre, un stéroïde sexuel à faible dose peut démarrer le pic et les caractères sexuels. La revue européenne cite, pour les garçons, 50 mg d'énanthate de testostérone en intramusculaire chaque mois pendant 3 à 6 mois, ou 10 mg de gel de testostérone à 2 % chaque jour pendant 3 mois, et pour les filles un quart d'un patch de 25 µg de 17-bêta-estradiol une ou deux fois par semaine pendant 6 mois. Ces schémas ne sont pas une information professionnelle suisse. Dose, spécialité ® et numéro Swissmedic : donnée non trouvée dans les sources consultées, car aucune AIPS n'a été ouverte. On ne prescrit pas ces chiffres tant que l'AIPS n'est pas lue."),
        p("Classe : androgènes et œstrogènes. Les autres principes actifs de la classe, la pharmacocinétique suisse, les effets indésirables à déclarer au patient et les interactions : donnée non trouvée dans les sources consultées au sens AIPS. L'ESPE affirme que la testostérone à faible dose change le calendrier du pic et ne réduit pas la taille adulte attendue."),
        p("Moyens non médicamenteux : explication aux parents, suivi scolaire, et conseil si le comportement devient agressif ou immature, comme l'ESPE le propose. Aucune chirurgie ni régime spécifique n'est indiqué par les sources lues."),
        p("Volet social : l'aptitude scolaire n'est pas limitée par le diagnostic. Arrêt de travail, LAMal et aptitude à conduire : sans objet chez l'enfant pour ce DX, sauf souffrance psychique qui relèverait alors d'un autre cadre. Donnée non trouvée pour une règle d'assurance spécifique."),
        p("Situations spéciales. Grossesse et allaitement : sans objet pour le garçon traité ; chez l'adolescente, on ne démarre pas un œstrogène sans avoir écarté une grossesse, et la source suisse de cette précaution n'a pas été ouverte. Sujet âgé : sans objet. Enfant plus jeune que les seuils : on ne traite pas un prépubère normal. Insuffisance hépatique ou rénale : donnée non trouvée pour une adaptation de ce schéma dans les sources ouvertes. On n'invente pas de palier de DFGe."),
        p(ital("C- Surveillance.") + " On revoit la taille, le stade et le volume testiculaire assez souvent pour voir si la puberté propre de l'enfant dépasse celle que le médicament a induite. L'ESPE arrête l'idée du traitement quand la puberté endogène prend le relais. Seuil biologique d'arrêt pour toxicité : donnée non trouvée."),
        p("Sortie du suivi spécialisé : l'enfant peut rester chez le pédiatre quand la puberté progresse seule, que la vitesse remonte et qu'aucune maladie exclue ne réapparaît. Il n'y a pas ici d'hospitalisation spécifique."),
        p(ital("D- Pronostic.") + " La condition est transitoire. La taille finale peut néanmoins manquer la cible si le retard est extrême. La revue discute un bénéfice statural possible d'un traitement court, qui disparaît si les doses de testostérone sont plus hautes. Recherche 2026 : donnée non trouvée au-delà des courbes suisses PEZZ 2025 et de la recommandation du 15 juin 2026, qui concernent la référence auxologique et non un essai thérapeutique de ce DX."),
        fen("Fenêtre 11.1 — Urgence chronologique, ce qui n'est pas une urgence minute", [
            p("Ce DX n'est pas une urgence à la minute. L'urgence relative est de ne pas manquer une autre maladie le jour de la consultation."),
            p("Heure 0 : mesurer, tracer, chercher un drapeau neurologique ou un Turner. Jour 0 à semaine 2 : âge osseux, TSH, thyroxine libre, gonadotrophines selon l'âge, caryotype chez la fille. Mois suivants : décider l'attente ou l'adressage pour un stéroïde faible dont la dose AIPS reste à lire."),
        ], S["espe"]),
    ]))
    c.append(point(12, "Prévention", [
        p("Prévention primaire : mesurer chaque enfant au moins une fois par an et tenir la courbe, comme le PEZZ le demande. Il n'existe pas de vaccin contre ce tempo."),
        p("Prévention secondaire : adresser aux seuils de 13 et 14 ans pour ne pas laisser s'installer une souffrance ni manquer un Turner. Prévention tertiaire : limiter le retard extrême qui compromet la cible, par l'explication et, si besoin, un traitement dont la dose suisse reste à vérifier dans l'AIPS."),
        p("Donnée non trouvée pour un programme OFSP nommé de dépistage de cette variante."),
    ]))
    c.append(point(13, "Points clés", [
        p("Vous adressez une fille sans sein à 13 ans et un garçon sans croissance testiculaire à 14 ans."),
        p("Vous lisez l'âge osseux sur la main et le poignet gauches avant de promettre une taille."),
        p("Vous demandez un caryotype à la fille, parce que l'ESPE veut exclure un Turner."),
        p("Vous n'appelez pas déficit en hormone de croissance un garçon dont la taille n'est pas sévère et dont la famille a poussé tard."),
        p("Vous n'écrivez une dose de testostérone ou d'œstrogène qu'après avoir lu l'AIPS suisse."),
    ]))
    c.append(point(14, "Pièges et questions fréquentes à l'examen fédéral suisse", [
        p("Piège : rassurer sans caryotype. Bonne réponse : toute fille avec puberté absente à 13 ans a un caryotype."),
        p("Piège : croire qu'une LH basse chez le prépubère prouve un hypogonadisme. Bonne réponse : elle est attendue, et seul le suivi ou un contexte particulier sépare les deux."),
        p("Piège : prescrire 50 mg d'énanthate parce qu'une revue européenne le cite. Bonne réponse : ce chiffre n'est pas une AIPS lue ; la dose suisse est non trouvée tant que l'information professionnelle n'est pas ouverte."),
        p("Piège : utiliser encore, sans le dire, une courbe antérieure à la recommandation du 15 juin 2026. Bonne réponse : pédiatrie suisse recommande les courbes nationales PEZZ à partir de cette date, et les seuils cliniques restent ceux des sociétés."),
        fen("Fenêtre 14.1 — Question type", [
            p("Un garçon de 14 ans et 2 mois a des testicules de volume infantile, un père qui s'est rasé tard, une taille à −2 DS, un âge osseux retardé de deux ans et un examen par ailleurs normal. Que faites-vous en premier ?"),
            p("Vous ne démarrez pas une hormone de croissance. Vous complétez l'exclusion (thyroïde, gonadotrophines, recherche de signe d'hypogonadisme permanent) et vous expliquez le retard probable. Vous ne donnez un stéroïde qu'après lecture de l'AIPS et discussion de la souffrance."),
        ], S["espe"] + ", " + S["gal"]),
    ]))
    return mono(
        "DX.5",
        "Retard constitutionnel de croissance et de puberté",
        "2 à 2,5 % de la population selon la revue européenne [S202] ; fréquence suisse non quantifiée",
        "".join(c),
    )

# The remaining monographs follow the same skeleton with their own facts.
# To keep this generator maintainable, dx6–dx10 call a builder with a rich spec.

def build_from_spec(dx, name, badge, spec):
    """spec: list of (n, title, list of html chunks)."""
    inner = "".join(point(n, t, ch) for n, t, ch in spec)
    return mono(dx, name, badge, inner)

def sentences_block(paragraphs, window_title, window_paragraphs, table_data, trap, source):
    chunks = [p(x) for x in paragraphs]
    blocks = [p(x) for x in window_paragraphs]
    if table_data:
        blocks.append(table(table_data[0], table_data[1]))
    if trap:
        blocks.append(p(trap))
    chunks.append(fen(window_title, blocks, source))
    return chunks

# imported by gen_suite.py
