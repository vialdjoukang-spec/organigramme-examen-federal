# -*- coding: utf-8 -*-
"""Rédaction LOT_232. Les paragraphes sont le cours. Le script ne fait que les assembler."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from habillage import bouton, fenetre, page  # noqa: E402
from schemas import arbre, chaine, urgence_refus, page_schema  # noqa: E402

RACINE = Path(__file__).resolve().parents[1]
CC = '<abbr title="code civil suisse">CC</abbr>'
ASSM = '<abbr title="Académie suisse des sciences médicales">ASSM</abbr>'
FMH = '<abbr title="Fédération des médecins suisses">FMH</abbr>'
LRH = '<abbr title="loi relative à la recherche sur l&#39;être humain">LRH</abbr>'
OFSP = '<abbr title="Office fédéral de la santé publique">OFSP</abbr> (office fédéral de la santé publique)'
ATF = '<abbr title="arrêt du Tribunal fédéral publié au recueil officiel">ATF</abbr> (arrêt publié)'
PAFA = '<abbr title="placement à des fins d&#39;assistance">PAFA</abbr> (placement à des fins d\'assistance)'
RS = '<abbr title="recueil systématique du droit fédéral">RS</abbr>'
MMSE = '<abbr title="mini-examen de l&#39;état mental">MMSE</abbr> (mini-examen de l\'état mental)'


def s(*n):
    return '<sup class="s">' + ",".join(str(i) for i in n) + "</sup>"


def P(*xs):
    return "".join("<p>" + x + "</p>\n" for x in xs)


def cliche(cid, mot):
    return f'<span class="cliche" data-cliche="{cid}">{mot}</span>'


SOURCES = """
<li>Code civil suisse, {RS} 210, art. 16, 14 et 17. Révision du 19 décembre 2008, en vigueur le 1er janvier 2013. Texte Fedlex consulté le 1er novembre 2026.{s1}</li>
<li>Code civil suisse, art. 19c, droits strictement personnels. En vigueur depuis 2013. Consulté le 1er novembre 2026.{s2}</li>
<li>Code civil suisse, art. 370 à 373, directives anticipées. En vigueur depuis 2013. Consulté le 1er novembre 2026.{s3}</li>
<li>Code civil suisse, art. 377, plan de traitement. En vigueur depuis 2013. Consulté le 1er novembre 2026.{s4}</li>
<li>Code civil suisse, art. 378, représentants. En vigueur depuis 2013. Consulté le 1er novembre 2026.{s5}</li>
<li>Code civil suisse, art. 379 à 381, urgence, {PAFA} et autorité de protection. En vigueur depuis 2013. Consulté le 1er novembre 2026.{s6}</li>
<li>Académie suisse des sciences médicales. La capacité de discernement dans la pratique médicale. Approuvées le 29 novembre 2018, tirage janvier 2019. Consultées le 1er novembre 2026.{s7}</li>
<li>Guide {FMH} et {ASSM}, information du patient. Mise à jour du 22 juin 2026. Consulté le 1er novembre 2026.{s8}</li>
<li>Tribunal fédéral, arrêt 4A_547/2019, reprenant l'{ATF} 133 III 121 de 2007. Consulté le 1er novembre 2026.{s9}</li>
<li>Pro Senectute Suisse et gfs.zürich, enquête du 2 au 23 novembre 2022, 1204 adultes. Consultée le 1er novembre 2026.{s10}</li>
<li>Office fédéral de la santé publique et bureau d'études mandaté, enquête sur les soins palliatifs, résultats 2017, synthèse 2018. Consultée le 1er novembre 2026.{s11}</li>
<li>Office fédéral de la santé publique. Renforcer la volonté du patient. Page consultée le 1er novembre 2026.{s12}</li>
<li>Loi fédérale du 30 septembre 2011 relative à la recherche sur l'être humain, art. 7, 16, 18 et 45. Consultée le 1er novembre 2026.{s13}</li>
<li>Commentaire de l'arrêt 4A_415/2023, février 2024, sur le consentement hypothétique et l'art. 28 du code civil. Consulté le 1er novembre 2026.{s14}</li>
""".format(RS=RS, PAFA=PAFA, FMH=FMH, ASSM=ASSM, ATF=ATF, s1=s(1), s2=s(2), s3=s(3), s4=s(4), s5=s(5), s6=s(6), s7=s(7), s8=s(8), s9=s(9), s10=s(10), s11=s(11), s12=s(12), s13=s(13), s14=s(14))


# --- Matière commune, redistribuée selon le point. Chaque entrée n'est utilisée qu'une fois par fichier. ---

COMMUN = {
1: [
f"Le consentement éclairé est l'autorisation donnée par la personne concernée à une atteinte à son intégrité corporelle. Sans cette autorisation, ou sans un autre fait justificatif, l'acte est illicite, même s'il est indiqué et même s'il est bien exécuté.{s(9)}",
f"Trois conditions se cumulent. L'information doit être adéquate. La personne doit être capable de discernement pour cette décision. Le choix doit être libre. Si une seule manque, le consentement n'est pas valable.{s(7,9)}",
f"L'article 16 du {CC} dit qu'est capable de discernement toute personne qui n'est pas privée de la faculté d'agir raisonnablement en raison de son jeune âge, d'une déficience mentale, de troubles psychiques, d'ivresse ou d'autres causes semblables.{s(1)}",
f"La capacité est présumée. On ne l'évalue que si un doute fondé apparaît, ou si l'incapacité est manifeste, comme chez un nourrisson ou une personne inconsciente.{s(7)}",
],
2: [
f"En 2022, une enquête téléphonique de Pro Senectute auprès de 1204 adultes de 18 à 99 ans trouve que 24 pour cent ont rédigé des directives anticipées. La même année, 85 pour cent disent les connaître.{s(10)}",
f"L'enquête de l'{OFSP} sur les soins palliatifs, dont la synthèse date de 2018, trouve une part plus basse de personnes ayant déposé des directives : 16 pour cent. En région germanophone, 19 pour cent en ont déposé, contre 9 pour cent en région francophone et 7 pour cent en région italophone.{s(11)}",
f"Ces deux enquêtes ne mesurent pas la même chose. L'une demande si la personne a rédigé des directives. L'autre demande si elle en a déposé. Le médecin ne convertit pas l'une dans l'autre.{s(10,11)}",
f"Aucune des sources lues en 2026 ne donne la part, au cabinet ou à l'hôpital, des interventions faites sans information adéquate. Le médecin ne retient donc pas un pourcentage de plaintes.{s(8)}",
],
3: [
f"Le raisonnement est normatif. Le point de départ est l'atteinte à l'intégrité. Le fait justificatif ordinaire est le consentement. Le fait justificatif de l'urgence, chez une personne incapable, est l'article 379 du {CC}.{s(6,9)}",
f"L'information crée la possibilité de choisir. Le Tribunal fédéral, dans l'arrêt 4A_547/2019 qui reprend l'{ATF} 133 III 121, demande des termes clairs sur le diagnostic, la thérapie, le pronostic, les alternatives, les risques, les chances, l'évolution sans traitement et les questions financières.{s(9)}",
f"La capacité n'est pas un test de la sagesse du choix. Les directives de 2019 interdisent de conclure à l'incapacité seulement parce que la décision étonne ou s'écarte de la recommandation.{s(7)}",
f"La liberté manque si la personne décide sous la pression d'un proche, d'une équipe ou d'un délai artificiel. Les directives de 2019 demandent un moment sans tiers, lorsque le patient le souhaite, pour entendre sa volonté propre.{s(7)}",
],
4: [
f"Devant une demande de consentement, le médecin classe d'abord le danger immédiat. S'il existe et que la personne est incapable, il donne les soins indispensables selon la volonté présumée et les intérêts, article 379.{s(6)}",
f"S'il n'y a pas cette urgence, il cherche un refus déjà écrit, puis il apprécie la capacité pour cette décision et à ce moment. Capable, la personne décide. Incapable, il suit les directives puis le représentant.{s(3,5,7)}",
f"Il sépare ensuite le soin et la recherche. Le consentement à l'opération ne couvre pas un projet de recherche. La loi de 2011 exige alors une information orale et écrite, un écrit, un délai de réflexion et l'autorisation de la commission d'éthique.{s(13)}",
f"À chaque embranchement, il écrit ce qu'il a dit, ce qu'il a compris de la personne, et la décision. La charge de la preuve de l'information lui incombe.{s(8,9)}",
],
5: [
f"L'entretien commence par ce que la personne sait déjà et par ce qu'elle veut savoir, y compris ce qu'elle préfère ne pas entendre dans le détail. Le médecin ne remplace pas cette préférence par un formulaire.{s(8)}",
f"Il demande le but que la personne attribue au geste, le risque grave qu'elle retient, l'alternative qu'on lui a nommée, et ce qui se passe si elle refuse. Une réponse vague est une information inachevée, pas un accord.{s(9)}",
f"Il cherche une pression. Il demande si quelqu'un a insisté, et il offre un temps seul. Un changement d'avis dès que le proche sort est un drapeau rouge de liberté, pas une versatilité à mépriser.{s(7)}",
f"Il demande s'il existe des directives anticipées, un mandat pour cause d'inaptitude, une curatelle, et qui devrait parler au médecin si la personne ne pouvait plus décider. L'{OFSP} rappelle que l'équipe doit s'enquérir des directives en cas d'incapacité.{s(12)}",
],
6: [
f"L'examen décisif est l'entretien de capacité, pas un score global. Les directives de 2019 décrivent quatre capacités : comprendre au moins dans les grandes lignes, évaluer la situation pour soi, se forger une volonté à partir de ses valeurs, communiquer cette volonté et la défendre.{s(7)}",
f"L'incapacité n'est retenue que si ces capacités sont fortement limitées, et si cette limite se rattache au jeune âge, à un trouble psychique, à une déficience mentale, à l'ivresse ou à une cause semblable, comme le dit l'article 16.{s(1,7)}",
f"Un {MMSE} bas ne tranche pas. Une personne peut être capable pour un soin simple et incapable pour une décision lourde. L'inverse existe aussi. On juge la décision du jour.{s(7)}",
f"Le médecin observe la {cliche('LOT_232-A-1', 'fluctuation')} de la vigilance, l'heure, la douleur, la langue, et la présence d'un tiers. Il réévalue si l'état change ou si le geste est loin de l'information.{s(7)}",
],
7: [
f"Cinq tableaux se séparent au lit. Le patient capable qui accepte. Le patient capable qui refuse. Le patient dont la capacité est douteuse. Le patient incapable avec un représentant. Le patient incapable en danger immédiat sans représentant joignable.{s(6,7)}",
f"Deux tableaux voisins se trompent souvent. La personne sous curatelle de portée générale n'est pas, par cela seul, incapable de discernement. Le mineur capable n'a pas besoin du consentement parental pour le soin lui-même.{s(2,7)}",
f"Deux autres tableaux concernent la forme. L'information non comprise, surtout si un proche traduit, n'est pas une information. Le consentement de recherche n'est pas le consentement de soin.{s(13)}",
f"Le formulaire signé sans entretien ressemble à un consentement et n'en est pas un. Il se range avec l'acte sans consentement valable ou avec le défaut d'information, selon ce qui a manqué.{s(8,9)}",
],
8: [
f"Le diagnostic de situation est positif quand les trois conditions sont décrites une à une, et non quand une signature est présente. Information, capacité, liberté : chacune est notée.{s(9)}",
f"Pour l'information, le critère est le contenu réellement transmis : diagnostic, nature, but, bénéfices, risques fréquents, risques graves même rares, alternatives, abstention, suites et coût.{s(8,9)}",
f"Pour la capacité, le critère est le jugement clinique sur les quatre capacités, pour cette décision, avec le motif écrit si l'on conclut à l'incapacité. Les directives de 2019 exigent cette trace.{s(7)}",
f"Pour la liberté, le critère est l'absence de contrainte repérée et un délai proportionné. Le guide de juin 2026, citant l'arrêt 4P.265/2002 du 28 avril 2003, retient la veille au plus tard pour un geste simple, et au minimum trois jours avant un geste lourd.{s(8)}",
],
9: [
f"Les compléments ne sont pas un laboratoire. Ce sont les pièces qui rendent la décision loyale : directives écrites, carte d'assuré, mandat, jugement de curatelle, nom du représentant, et identité de l'interprète.{s(3,12)}",
f"L'article 372 demande au médecin qui ignore si des directives existent de consulter la carte d'assuré, sauf urgence. L'article 371 exige un écrit daté et signé.{s(3)}",
f"Si les représentants du même rang ne s'accordent pas, si aucun représentant n'est joignable hors urgence, ou si les intérêts de la personne sont menacés, le médecin saisit l'autorité de protection de l'adulte, article 381.{s(6)}",
f"Pour une recherche, le complément est le dossier du projet : information écrite, consentement écrit, délai laissé, et autorisation de la commission d'éthique, article 45 de la loi de 2011.{s(13)}",
],
10: [
f"L'arbre tient en une question d'ouverture : y a-t-il un danger immédiat chez une personne qui ne peut pas décider ? Si oui, soins indispensables, volonté présumée, et respect d'un refus anticipé déjà connu.{s(6,3)}",
f"Si non, la deuxième question est la capacité pour cette décision. Le capable accepte ou refuse. Le doute se lève en corrigeant ce qui est réversible, puis en réévaluant. L'incapable ouvre les directives, puis l'article 378.{s(5,7)}",
f"La chaîne d'information est un second dessin. Dix maillons vont du diagnostic à la trace écrite. Il manque un maillon décisif, en particulier un risque grave ou une alternative, et l'information n'est pas adéquate.{s(8,9)}",
f"Le troisième dessin sépare le refus et l'urgence. Ils ne se traitent pas par le même réflexe. Le refus capable s'impose. L'urgence de l'incapable autorise les soins indispensables, pas davantage.{s(6,9)}",
],
11: [
f"En Suisse, le médecin informe, vérifie la capacité s'il y a doute, laisse le choix, et écrit. Il n'y a pas de dose à prescrire pour ce motif. La conduite est un entretien et une trace.{s(8)}",
f"L'ordre de l'article 378 est fixe. D'abord la personne désignée dans les directives ou le mandat. Puis le curateur chargé du domaine médical. Puis le conjoint ou le partenaire enregistré qui fait ménage commun ou apporte une aide personnelle régulière. Puis la personne qui fait ménage commun et aide régulièrement. Puis les descendants, les père et mère, les frères et sœurs, aux mêmes conditions d'aide régulière.{s(5)}",
f"Le représentant, s'il n'y a pas d'instruction écrite, décide selon la volonté présumée et les intérêts. Le médecin établit avec lui le plan de traitement et l'informe selon l'article 377, y compris sur le coût et les autres traitements. Il associe la personne incapable autant que possible.{s(4,5)}",
f"Un consentement donné alors que la personne est déjà sous sédatifs n'est pas valable, selon le guide de juin 2026. On n'informe pas la veille un patient pour une opération lourde qui était prévisible depuis longtemps.{s(8)}",
],
12: [
f"La prévention du litige est la prévention de l'atteinte illicite. Le médecin prévoit l'entretien avant le geste électif, dans une langue comprise, avec un interprète professionnel si besoin, et avec un délai.{s(8)}",
f"Il propose les directives anticipées avant la crise, surtout après 65 ans, âge où l'enquête de 2022 trouve une meilleure connaissance. Il ne les impose pas.{s(10)}",
f"Il relit le dossier avant le bloc : qui a informé, quand, quels risques graves ont été dits, quelle alternative, quelle décision. S'il manque une ligne, il reprend l'entretien.{s(8)}",
f"Il apprend à l'équipe à ne pas faire signer à l'accueil. La signature peut aider la preuve. Elle ne crée pas l'information.{s(8,9)}",
],
13: [
f"Un acte non consenti est une atteinte illicite, même parfaitement réalisé. Les trois conditions sont cumulatives : information, capacité, liberté.{s(9)}",
f"L'information inclut les risques graves même rares et les alternatives, dont l'abstention. Le guide de 2026 rappelle qu'aucun pourcentage-seuil n'a été fixé par le Tribunal fédéral pour dire un risque.{s(8)}",
f"La capacité est présumée, relative et réévaluable. Elle ne se confond ni avec la majorité ni avec la curatelle. Le mineur capable consent seul au soin.{s(2,7)}",
f"Le refus éclairé d'une personne capable s'impose. L'incapacité ouvre les directives, le représentant et, seulement en urgence, l'article 379. La recherche a sa propre loi.{s(6,13)}",
],
14: [
f"Piège un : faire signer et croire que le soin est licite. Piège deux : taire un risque grave parce qu'il est rare. Piège trois : déclarer incapable celui qui refuse.{s(7,8,9)}",
f"Piège quatre : prendre le conjoint présent pour le représentant alors qu'une directive désigne quelqu'un d'autre, ou qu'il n'y a ni ménage commun ni aide régulière.{s(5)}",
f"Piège cinq : traduire par l'enfant. Piège six : utiliser le consentement opératoire pour inclure la personne dans une recherche.{s(13)}",
f"Piège sept : en urgence, élargir l'acte au-delà de l'indispensable, ou ignorer un refus anticipé déjà connu et applicable.{s(3,6)}",
],
}
