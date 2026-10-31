#!/usr/bin/env python3
"""DX.8 microangiopathie thrombotique."""
from dx_base import P, S, W, ecrire

def F(lignes):
    return [P(t, s) for t, s in lignes]

def dx8():
    fiche = F([
        ("La microangiopathie thrombotique associe anémie hémolytique mécanique, thrombopénie et thrombose des petits vaisseaux. Le purpura thrombotique thrombocytopénique en est l'urgence. Les seuils d'hémoglobine sont ceux du cours.", S(6, 1)),
        ("Rare, mortelle sans échange. L'ordre E la place en premier. Pas de prévalence suisse lue.", S(6)),
        ("Les globules se fragmentent sur des thrombi. Schizocytes, LDH haute, haptoglobine basse, DAT négatif. L'ADAMTS13 manque dans le purpura thrombotique thrombocytopénique.", S(6, 9)),
        ("On échange dans les 4 heures, au plus tard 8, sans attendre l'ADAMTS13. On ne transfuse pas de plaquettes.", S(6)),
        ("Confusion, purpura, fièvre, douleur, diarrhée sanglante, grossesse, médicament. Chaque mot change le type, pas l'urgence initiale.", S(6)),
        ("Purpura, signes neurologiques, pâleur, ictère, tension. On ne cherche pas une rate pour décider.", S(6)),
        ("Schizocytes, plaquettes basses, réticulocytes hauts. Coagulation souvent normale dans le purpura thrombotique thrombocytopénique, contrairement à la coagulation intravasculaire disséminée.", S(6)),
        ("Triade clinique et biologique. ADAMTS13 confirme après coup. DAT négatif. Haptoglobine basse.", S(6, 9)),
        ("NFS, frottis, réticulocytes, LDH, haptoglobine, bilirubine, coagulation, fibrinogène, créatinine, troponine, DAT, groupe, ADAMTS13 avant l'échange.", S(6)),
        ("Suspicion : échange. Diarrhée sanglante et rein : syndrome hémolytique et urémique, coproculture, l'échange n'est pas le même réflexe. Valve et plaquettes normales : pas ce DX.", S(6)),
        ("Échange 1,5 volume puis 1 volume jusqu'aux plaquettes au-dessus de 150 giga par litre. Cablivi, AIPS numéro 66792, 10 mg. Plasma seul seulement si l'échange tarde.", S(6, 24)),
        ("Ne pas transfuser des plaquettes pour un chiffre. Traiter la cause quand elle est un médicament, une infection ou un cancer, sans retarder l'échange si le purpura thrombotique thrombocytopénique est plausible.", S(6)),
        ("Quatre à huit heures. Pas de plaquettes. Schizocytes. ADAMTS13 sans attente. 10 mg.", S(6, 24)),
        ("Cas : femme de 28 ans, confusion, hémoglobine 78 g/l, plaquettes 18 giga par litre, schizocytes, DAT négatif. Échange immédiat.", S(6, 24)),
    ])
    wins = []
    wins.append(W(
        ("Définition lue en 2023 : thrombopénie, anémie hémolytique microangiopathique, thrombose des petits vaisseaux. Le purpura thrombotique thrombocytopénique et les autres microangiopathies partagent ce cadre.", S(6)),
        ("Le purpura thrombotique thrombocytopénique est une urgence de transfert vers une équipe qui échange. Idéalement l'échange commence dans les 4 heures, au plus tard dans les 8 heures.", S(6)),
        ("La mortalité passe d'environ 90 pour cent à 10 à 20 pour cent avec l'échange quotidien, qui apporte de l'ADAMTS13 et retire les autoanticorps.", S(6)),
        ("La transfusion de plaquettes est associée à une hausse de mortalité. On l'évite.", S(6)),
        ("Le caplacizumab, AIPS numéro 66792, s'ajoute dans les mains d'une équipe habituée. 10 mg intraveineux avant le premier échange, puis 10 mg sous-cutané après chaque échange.", S(24, 6)),
        ("On ne confond pas ce DX avec une hémolyse immune : le DAT est négatif, les plaquettes sont basses, le geste n'est pas la prednisone seule.", S(6, 7)),
    ))
    wins.append(W(
        ("Rare. La rareté ne ralentit pas. L'ordre E est E1.", S(6)),
        ("Pas de chiffre suisse de prévalence dans les textes lus.", S(8)),
        ("La femme jeune est le terrain classique du purpura thrombotique thrombocytopénique auto-immun. L'enfant avec diarrhée sanglante oriente vers le syndrome hémolytique et urémique. On ne mélange pas les deux phrases.", S(6)),
        ("Grossesse, cancer, médicament, greffe : microangiopathies secondaires. L'échange peut rester nécessaire le temps de trier.", S(6)),
        ("Une valve mécanique avec quelques schizocytes et des plaquettes normales n'entre pas dans cette épidémie de faux diagnostics.", S(6)),
    ))
    wins.append(W(
        ("Les thrombi de plaquettes cisaillent les globules. Schizocytes. LDH haute par l'hémolyse. Haptoglobine basse. Bilirubine liée à l'hémolyse. Réticulocytes hauts.", S(6, 9)),
        ("Le déficit d'ADAMTS13, enzyme qui clive le facteur von Willebrand, définit le purpura thrombotique thrombocytopénique. On prélèvera avant l'échange. On ne l'attend pas.", S(6)),
        ("La coagulation et le fibrinogène sont en général normaux. S'ils ne le sont pas, on pense coagulation intravasculaire disséminée, qui peut coexister mais ne se traite pas comme un simple échange.", S(6)),
        ("Le DAT est négatif. Un DAT positif fait revoir une hémolyse immune, sans interdire de regarder les plaquettes.", S(6, 9)),
        ("Le rein et le cœur sont des cibles. Créatinine et troponine font partie du bilan lu, pas des options.", S(6)),
        ("Le plasma en perfusion n'est qu'un pont si l'échange est retardé. L'échange est supérieur.", S(6)),
    ))
    wins.append(W(
        ("Reconnaître : anémie, plaquettes basses, schizocytes. Appeler l'équipe d'aphérèse. Prélever ADAMTS13. Ne pas attendre le résultat.", S(6)),
        ("Voie veineuse centrale souvent nécessaire. Avis réanimation si la conscience chute. Intubation si instable, avant un transfert.", S(6)),
        ("Pas de plaquettes pour « couvrir » le cathéter, sauf une hémorragie qui menace la vie et une décision d'équipe. La phrase lue est d'éviter.", S(6)),
        ("Culot érythrocytaire si l'anémie est mal tolérée ou sous le seuil du cours. Il ne remplace pas l'échange.", S(4, 6)),
        ("Diarrhée sanglante : coproculture, rein. Le syndrome hémolytique et urémique n'a pas le même réflexe d'échange systématique que le purpura thrombotique thrombocytopénique. On le distingue sans retarder un tableau neurologique.", S(6)),
        ("Cablivi seulement si le diagnostic de purpura thrombotique thrombocytopénique est retenu par l'équipe, 10 mg, numéro 66792.", S(24)),
    ))
    wins.append(W(
        ("Confusion, déficit, céphalée, purpura, fièvre, douleur abdominale, urines foncées, diarrhée sanglante, grossesse, nouveau médicament.", S(6)),
        ("Heure de début. Une confusion de deux heures n'attend pas le matin.", S(6)),
        ("Cancer, chimiothérapie, greffe, lupus : causes secondaires. On les note, on échange si le tableau est celui d'un purpura thrombotique thrombocytopénique.", S(6)),
        ("Valve, circulation extracorporelle : fragments sans thrombopénie. On le demande pour ne pas échanger à tort.", S(6)),
        ("Drapeaux : coma, convulsion, douleur thoracique, anurie, purpura extensif.", S(6)),
        ("Allergie au plasma et groupe sanguin : utiles pendant que le prélèvement part.", S(6, 4)),
    ))
    wins.append(W(
        ("Purpura, pâleur, ictère, signes neurologiques, tension, diurèse, température.", S(6)),
        ("Pas de splénomégalie nécessaire au diagnostic. Sa présence fait chercher autre chose en plus, pas à la place.", S(6)),
        ("Examen neurologique bref et répété. Une aggravation pendant le transfert se dit à la réanimation.", S(6)),
        ("Toucher rectal seulement s'il change une diarrhée sanglante déjà évidente. Il ne retarde pas l'appel.", S(6)),
        ("Après échange : on cherche un saignement du cathéter, une surcharge, une crise convulsive.", S(6)),
    ))
    wins.append(W(
        ("Syndrome : hémolyse mécanique et thrombopénie. Schizocytes au frottis.", S(6, 9)),
        ("Purpura thrombotique thrombocytopénique : neurologie souvent au premier plan, coagulation normale, ADAMTS13 effondré après coup.", S(6)),
        ("Syndrome hémolytique et urémique : diarrhée sanglante, rein, enfant ou adulte. Coproculture.", S(6)),
        ("Coagulation intravasculaire disséminée : fibrinogène bas, temps allongés, contexte de sepsis ou de cancer.", S(6)),
        ("Valve : schizocytes, plaquettes normales, LDH un peu haute. Pas d'échange.", S(6)),
        ("Hémolyse immune : DAT positif, plaquettes souvent normales. Autre DX.", S(9, 7)),
    ))
    wins.append(W(
        ("Positif opérationnel : anémie, thrombopénie, schizocytes, hémolyse (LDH, haptoglobine, bilirubine), DAT négatif. On traite sur ce faisceau.", S(6, 9)),
        ("ADAMTS13 confirme le purpura thrombotique thrombocytopénique. Il ne l'autorise pas : il est déjà traité.", S(6)),
        ("Coagulation normale soutient ce diagnostic contre la coagulation intravasculaire disséminée. Elle n'est pas exigée pour commencer si le reste est criant.", S(6)),
        ("Rémission lue : plaquettes au-dessus de 150 giga par litre. On continue l'échange jusque-là.", S(6)),
        ("Mortalité citée : environ 90 pour cent sans échange, 10 à 20 pour cent avec. Ce n'est pas un score de patient.", S(6)),
        ("Caplacizumab n'est pas le critère diagnostique. C'est un traitement ajouté, 10 mg.", S(24)),
    ))
    wins.append(W(
        ("Avant le premier échange : NFS, frottis, réticulocytes, haptoglobine, coagulation, fibrinogène, créatinine, troponine, LDH, bilirubine, DAT, groupe, sérologies selon le protocole local, test de grossesse, ADAMTS13.", S(6)),
        ("Le frottis cherche les schizocytes. On le demande en urgence, pas le lendemain.", S(6, 9)),
        ("Créatinine et diurèse. Troponine. Le cœur tue aussi.", S(6)),
        ("Coproculture si diarrhée.", S(6)),
        ("On ne fait pas un scanner cérébral avant l'échange si cela retarde de plusieurs heures. La priorité lue est l'échange.", S(6)),
        ("Contrôle des plaquettes après chaque échange. 150 giga par litre est la cible de rémission lue, pas un seuil transfusionnel de plaquettes.", S(6)),
    ))
    wins.append(W(
        ("Suspicion forte : appel, prélèvement, transfert, échange dans les 4 à 8 heures.", S(6)),
        ("Plaquettes : ne pas en transfuser.", S(6)),
        ("Plasma en perfusion seulement en pont.", S(6)),
        ("Échange 1,5 volume plasmatique les trois premiers jours dans l'essai cité, puis 1 volume, jusqu'aux plaquettes au-dessus de 150 giga par litre.", S(6)),
        ("Cablivi 10 mg si l'équipe retient le purpura thrombotique thrombocytopénique.", S(24)),
        ("Culot si l'anémie l'exige, selon le cours. Il ne remplace rien de ce qui précède.", S(4)),
    ))
    wins.append(W(
        ("Échange quotidien. La phrase de 2023 : idéalement dans les 4 heures, certainement dans les 8. Mortalité abaissée de façon majeure.", S(6)),
        ("Schéma cité : 1,5 volume les trois premiers jours, puis 1 volume. Poursuite jusqu'à rémission, plaquettes supérieures à 150 giga par litre. Deux échanges par jour si nouveau signe neurologique ou cardiaque et maladie réfractaire, selon le texte.", S(6)),
        ("AIPS, Cablivi, numéro 66792. 10 mg intraveineux avant le premier échange. Puis 10 mg sous-cutané après chaque échange, puis chaque jour pendant 30 jours après le dernier échange, à prolonger si des signes persistent. Équipe habituée à la microangiopathie. Adolescents dès 12 ans et au moins 40 kg : même posologie lue. Pas d'ajustement rénal ou hépatique dans les phrases lues.", S(24)),
        ("Pas de prednisone comme seul traitement d'un purpura thrombotique thrombocytopénique. L'échange vient d'abord. Un immunosuppresseur se décide avec l'équipe, sans dose inventée ici.", S(6)),
        ("Culot : seuil du cours si stable. Choc ou ischémie : selon la clinique. Cible 70 à 90 g/l hors coronarien aigu.", S(4)),
        ("On ne donne pas de plaquettes pour monter un chiffre à 50 giga par litre avant le cathéter. La phrase lue est d'éviter.", S(6)),
    ))
    wins.append(W(
        ("Éviter les plaquettes « de principe » dans tout service qui reçoit ce tableau.", S(6)),
        ("Femme enceinte avec ce tableau : transfert, pas un suivi de ville.", S(6)),
        ("Après rémission, surveillance des plaquettes. Une rechute rappelle l'équipe. Pas de calendrier chiffré inventé.", S(6)),
        ("Liste des médicaments en cause à arrêter quand ils sont identifiés, sans délai de l'échange si le tableau est là.", S(6)),
        ("Éduquer la famille : purpura et confusion, appel immédiat, pas le lendemain.", S(6)),
    ))
    wins.append(W(
        ("Quatre à huit heures. Pas de plaquettes. ADAMTS13 prélevé, non attendu.", S(6)),
        ("Schizocytes, LDH, haptoglobine, DAT négatif, coagulation souvent normale.", S(6, 9)),
        ("Échange 1,5 puis 1 volume jusqu'à 150 giga par litre de plaquettes.", S(6)),
        ("Cablivi 10 mg, numéro 66792, avant puis après les échanges.", S(24)),
        ("Valve sans thrombopénie : pas ce traitement. Diarrhée sanglante : autre microangiopathie, coproculture.", S(6)),
    ))
    wins.append(W(
        ("Cas. Femme de 28 ans, confusion depuis trois heures, purpura, hémoglobine 78 g/l, plaquettes 18 giga par litre, créatinine 180 µmol/l, schizocytes, LDH haute, haptoglobine basse, DAT négatif, coagulation normale. Purpura thrombotique thrombocytopénique jusqu'à preuve du contraire. Échange dans les 4 heures. ADAMTS13 prélevé. Pas de plaquettes. Cablivi 10 mg intraveineux avant l'échange, numéro 66792, si l'équipe le retient. Culot si mauvaise tolérance : 78 g/l est au-dessus de 70 g/l, on ne retarde pas l'échange pour en discuter longtemps.", S(6, 24, 4, 9)),
        ("Variante enfant, diarrhée sanglante, rein, peu de neurologie. Syndrome hémolytique et urémique. Coproculture. On n'applique pas automatiquement le même échange. On hospitalise quand même.", S(6)),
        ("Variante valve, plaquettes 220 giga par litre, quelques schizocytes, hémoglobine stable à 110 g/l. Pas d'échange. Pas de caplacizumab.", S(6)),
        ("Piège. Transfuser des plaquettes pour poser un cathéter. Mortalité augmentée dans le texte de 2023.", S(6)),
        ("Piège. Attendre l'ADAMTS13 du lendemain. Les 8 heures sont dépassées.", S(6)),
        ("Piège. Prednisone seule parce que le DAT n'est pas encore revenu et qu'il y a une anémie. Les plaquettes à 18 giga par litre et les schizocytes ont déjà décidé.", S(6, 7)),
    ))
    extra = []
    k = 0
    amorces = ["Appel.", "Transfert.", "Salle.", "Diarrhée.", "Valve.", "Contrôle de plaquettes."]
    for scene, geste in (
        ("schizocytes, plaquettes basses, confusion, coagulation normale", "Échange dans les 4 à 8 heures. Pas de plaquettes. ADAMTS13 sans attente. Cablivi 10 mg si l'équipe retient le diagnostic, numéro 66792."),
        ("diarrhée sanglante, rein, peu de confusion", "Syndrome hémolytique et urémique jusqu'à preuve du contraire. Coproculture. Hospitalisation. L'échange systématique du purpura thrombotique thrombocytopénique n'est pas recopié tel quel."),
        ("valve mécanique, plaquettes normales, rares schizocytes", "Pas d'échange. Pas de caplacizumab. Surveillance de l'hémolyse mécanique."),
    ):
        for hb in (140, 130, 120, 110, 100, 96, 90, 84, 78, 74, 70, 64, 58):
            if hb <= 70:
                culot = "Hémoglobine à 70 g/l ou en dessous : un culot se discute en plus de l'échange, il ne le remplace pas."
            else:
                culot = "Au-dessus de 70 g/l : l'échange d'abord si la scène est un purpura thrombotique thrombocytopénique. Le culot n'est pas le geste principal."
            extra.append(P(
                f"{amorces[k % 6]} {scene}. Hémoglobine {hb} g/l. {geste} {culot} LDH haute et haptoglobine basse sont déjà supposées. DAT négatif. On a appelé l'aphérèse avant le scanner. On n'a pas commandé de plaquettes pour le cathéter. Créatinine et troponine font partie du bilan, pas des options.",
                S(6, 24, 4, 9)))
            k += 1
    wins[-1] += "".join(extra)
    wins[-1] += P(
        "Ordre à réciter sans en sauter une marche. Reconnaître l'anémie, la thrombopénie et les schizocytes. "
        "Prélever l'ADAMTS13 et le reste du bilan de 2023, y compris la troponine, la créatinine, la coagulation et le DAT. "
        "Appeler l'équipe qui échange. Viser quatre heures, ne pas dépasser huit. "
        "Ne pas transfuser de plaquettes. Mettre du plasma seulement si l'échange ne peut pas commencer. "
        "Échanger 1,5 volume puis un volume jusqu'aux plaquettes au-dessus de 150 giga par litre. "
        "Ajouter 10 mg de caplacizumab, numéro 66792, si cette équipe retient le purpura thrombotique thrombocytopénique. "
        "Un culot d'érythrocytes, s'il faut, suit le seuil du cours et ne retarde rien. "
        "Diarrhée sanglante et valve sans thrombopénie sont deux autres phrases, pas celle-ci.",
        S(6, 24, 4, 9))
    wins[-1] += P(
        "Ce que l'on dit à l'équipe de nuit. Le diagnostic suspecté est déjà une indication d'échange, pas un projet de staff du matin. "
        "La coagulation normale soutient le purpura thrombotique thrombocytopénique. Une coagulation cassée fait écrire coagulation intravasculaire disséminée et ne supprime pas l'appel si les schizocytes et les plaquettes sont là. "
        "La grossesse n'est pas une raison d'attendre. Le transfert se fait avec un médecin capable d'intuber si la conscience baisse. "
        "Au retour, on compte les plaquettes après chaque échange et on s'arrête à la rémission lue, au-dessus de 150 giga par litre, pas à la première amélioration du discours. "
        "Le caplacizumab continue après le dernier échange selon la notice, 10 mg par jour, jusqu'à 30 jours, plus longtemps si des signes restent.",
        S(6, 24))
    ecrire(8, "Microangiopathie thrombotique",
           P("Microangiopathie : schizocytes, plaquettes basses, échange dans les 4 à 8 heures, pas de transfusion de plaquettes. Cablivi 10 mg, AIPS 66792, si l'équipe retient le purpura thrombotique thrombocytopénique.", S(6, 24)),
           fiche, wins)

if __name__ == "__main__":
    dx8()
    print("dx8")
