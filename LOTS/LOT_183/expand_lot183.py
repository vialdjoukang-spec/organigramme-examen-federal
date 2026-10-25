# -*- coding: utf-8 -*-
"""Fenêtres d'approfondissement sourcées, pour atteindre un cours utilisable à l'examen."""
from html import escape

def p(text):
    return f"<p style='margin:4px 0 6px;'>{text}</p>"

def fen(title, paragraphs, source):
    inner = "".join(p(x) for x in paragraphs)
    return (
        "<details style='margin:8px 0;border-left:4px solid #1a5276;background:#f8f9f9;"
        "padding:6px 10px;'><summary style='cursor:pointer;font-weight:bold;color:#1a5276;'>"
        f"{escape(title)}</summary><div style='margin-top:6px;'>{inner}"
        f"<em>Source : {escape(source)}.</em></div></details>"
    )

def block(title, lines, source):
    return fen(title, lines, source)

# Chaque entrée : titre, liste de phrases verbales, source.
DX5 = [
("Consultation 1 — garçon de 14 ans, tempo familial", [
"Un garçon de 14 ans et 3 mois vient parce qu'il est le plus petit de sa classe. Sa mère dit que le père s'est rasé tard. Vous ne concluez pas sur cette phrase.",
"Vous mesurez l'enfant, le père et la mère le jour même, parce que Paediatrica fait de cette mesure un acte médical. Vous reportez la taille sur la courbe recommandée par pédiatrie suisse depuis le 15 juin 2026.",
"Vous palpez les testicules avec l'orchidomètre. S'ils sont encore de volume infantile, le seuil ESPE de 14 ans est franchi et l'évaluation est indiquée.",
"Vous demandez l'âge osseux de la main et du poignet gauches. Un retard d'au moins un an entre dans le type 1 décrit par Galazzi à partir de la classification ESPE 2007.",
"Vous dosez la TSH et la thyroxine libre pour ne pas manquer une hypothyroïdie, et les gonadotrophines avec la testostérone pour ne pas manquer une atteinte testiculaire.",
"Si tout est compatible et qu'aucun signe neurologique n'existe, vous expliquez le retard constitutionnel. Vous ne prescrivez pas de testostérone tant que l'information professionnelle suisse n'est pas lue.",
], "[S201], [S202], [S203], [S204]"),
("Consultation 2 — fille de 13 ans sans sein", [
"Une fille de 13 ans n'a pas de bourgeon mammaire palpable. L'ESPE demande alors un avis, et un caryotype, parce que le syndrome de Turner ralentit la croissance et la puberté et peut toucher le cœur et les reins.",
"Vous ne cherchez pas d'abord une dysmorphie pour décider du caryotype. Le dépliant demande le caryotype chez la fille dont la puberté tarde.",
"Vous mesurez la vitesse. Un déficit en hormone de croissance, dit l'ESPE, rend l'enfant habituellement beaucoup plus petit que le retard constitutionnel.",
"Vous expliquez aux parents que l'attente seule est interdite tant que le caryotype n'est pas connu.",
"Si le caryotype est 46,XX, que l'âge osseux retarde et que la famille décrit un tempo lent, le cadre constitutionnel redevient possible.",
"Si les gonadotrophines sont élevées et que l'œstradiol est bas, vous quittez ce DX : c'est une insuffisance gonadique.",
], "[S201], [S202]"),
("Consultation 3 — souffrance scolaire sans dose écrite", [
"L'ESPE décrit des garçons qui deviennent agressifs ou immatures parce qu'ils vivent mal leur taille et l'absence de caractères sexuels. Un conseil est alors proposé si l'école ou la maison se désorganise.",
"Le dépliant dit qu'aucun traitement n'est habituellement nécessaire, et qu'un stéroïde sexuel peut accélérer le calendrier si une aide est requise.",
"Il demande que la puberté induite ne soit pas plus rapide qu'un parcours d'un à deux ans, alors que la puberté normale dure trois à quatre ans.",
"La revue européenne cite des schémas chiffrés de testostérone et d'estradiol. Vous les lisez comme une information scientifique, pas comme une ordonnance suisse.",
"Vous écrivez dans le dossier : dose AIPS non lue, pas de spécialité retenue, pas de numéro Swissmedic. Vous adressez au pédiatre endocrinologue qui ouvrira l'information professionnelle.",
"Vous revoyez le volume testiculaire. S'il grandit après l'arrêt d'un éventuel essai, la revue utilise cette progression comme un argument pour le retard constitutionnel plutôt que pour l'hypogonadisme permanent.",
], "[S201], [S202]"),
("Ce que le chiffre de 2 à 2,5 % autorise et interdit", [
"Galazzi écrit que la condition touche 2 à 2,5 % de la population. Vous pouvez citer ce chiffre avec la source. Vous ne pouvez pas dire que 2,5 % des élèves suisses sont suivis pour ce motif.",
"Jusqu'à 80 % des garçons qui consultent pour une puberté retardée auraient une forme autolimitée, contre environ un tiers des filles, et environ 10 % dans une cohorte géorgienne de filles où les causes organiques dominent.",
"Vous expliquez le biais : les séries familiales touchent les deux sexes, mais les garçons consultent plus. Une fille n'est donc pas « rassurante » parce qu'elle est une fille.",
"La mortalité n'est pas un enjeu de ce DX dans les sources lues. L'enjeu est la taille finale et la souffrance.",
"L'ESPE ajoute que le pic de croissance est réduit et que les garçons traversent la puberté plus lentement. Un retard extrême peut manquer la cible parentale, contrairement à l'idée ancienne que le seul décalage d'âge osseux garantit la cible.",
"Vous ne transformez pas cette nuance en pourcentage de perte staturale : la source ne donne pas ce pourcentage.",
], "[S201], [S202]"),
("Âge osseux : ce que vous dites à l'oral", [
"Vous demandez la radiographie de la main et du poignet gauches, comme l'ESPE le décrit, parce que les espaces entre les os longs se ferment à la fin de la puberté.",
"Vous dites que l'âge osseux estime le temps de croissance restant. Vous ne dites pas qu'il donne la taille adulte au centimètre près : la source ne fournit pas cette équation.",
"Un retard d'au moins un an fait partie du type 1 de la revue. Un âge osseux égal à l'âge civil éloigne du retard constitutionnel et rapproche d'une petite taille dont le tempo est normal.",
"Vous comparez toujours l'âge osseux à l'âge civil et au stade de Tanner. Un os très retardé avec des signes pubertaires déjà avancés ne colle pas à ce DX.",
"Vous n'utilisez pas l'âge osseux pour éviter le caryotype chez la fille.",
"Vous expliquez aux parents que le cartilage reste ouvert plus longtemps, mais que cette réserve n'est pas infinie si la puberté tarde extrêmement.",
], "[S201], [S202]"),
("Vitesse : refaire le calcul devant l'examinateur", [
"La vitesse est une différence de taille divisée par un intervalle de temps, exprimée en centimètres par an.",
"Exemple déjà vérifié : 118,0 cm à 6,0 ans et 122,4 cm à 6,8 an. Différence 4,4 cm. Intervalle 0,8 an. Vitesse 4,4 / 0,8 = 5,5 cm par an. C'est un calcul dérivé de méthode, pas une norme suisse.",
"La revue dit que la vitesse des garçons avec retard constitutionnel dépasse souvent 3,6 cm par an. Une vitesse très inférieure doit faire chercher un déficit somatotrope ou une maladie chronique.",
"Vous ne comparez pas un prépubère à la vitesse d'un camarade déjà en pic pubertaire sans le dire. Le pic manque précisément parce que les stéroïdes ne sont pas là.",
"Le PEZZ rappelle que, après 2 ans, un changement de canal est suspect. Vous regardez donc la trajectoire, pas le dernier point.",
"Les courbes de vitesse suisses actuelles continuent de s'appuyer sur les études longitudinales de Zurich, dit pédiatrie suisse en 2026. Vous ne mélangez pas ces courbes de vitesse avec les nouvelles courbes de taille sans le préciser.",
], "[S202], [S204], [S205]"),
("Cible parentale : trois familles", [
"Formule lue : [taille maternelle + taille paternelle ± 13 cm] / 2. Plus 13 cm chez le garçon, moins 13 cm chez la fille. Intervalle ± 8,5 cm.",
"Famille A : mère 160 cm, père 178 cm. Somme 338. Garçon (338 + 13) / 2 = 175,5 cm. Fille (338 − 13) / 2 = 162,5 cm. Calcul dérivé.",
"Famille B : mère 150 cm, père 168 cm. Somme 318. Garçon (318 + 13) / 2 = 165,5 cm. Fille (318 − 13) / 2 = 152,5 cm. Calcul dérivé.",
"Si le garçon de la famille B termine à 164 cm, il est dans l'intervalle 157 à 174 cm. Le cadre peut rester cohérent.",
"Si le même garçon termine à 150 cm, il est sous l'intervalle et le mot constitutionnel ne suffit plus.",
"Vous inscrivez la cible sur la courbe, comme Paediatrica le demande, et vous refusez les tailles parentales déclarées de mémoire.",
], "[S203]"),
("Génétique : ce qu'il faut répondre sans surinterpréter", [
"La revue décrit plusieurs modes de transmission possibles, surtout autosomique dominant à pénétrance incomplète, mais aussi récessif, bilinéaire ou lié à l'X. Des mutations de novo existent.",
"Des variants hétérozygotes de gènes d'hypogonadisme hypogonadotrope ont été trouvés dans jusqu'à 7 % des cohortes de retard constitutionnel. Vous ne dites donc pas qu'un test négatif prouve la variante, ni qu'un variant prouve l'hypogonadisme permanent.",
"Des gènes sont discutés dans la revue, dont IGSF10, avec un débat sur leur enrichissement réel par rapport aux témoins. Vous ne récitez pas un gène comme s'il était un test diagnostique suisse.",
"Le test génétique de routine de ce DX n'est pas indiqué par les sources lues. Donnée non trouvée pour un panel suisse remboursé.",
"Vous expliquez à l'étudiant que la clinique et le temps restent le cœur du diagnostic.",
"Vous ne confondez pas ce conseil avec un syndrome déjà nommé, comme un CHARGE ou un Prader-Willi, que la revue cite comme des situations où plusieurs phénotypes hormonaux peuvent coexister.",
], "[S202]"),
("Priming et tests de stimulation : ne pas traiter trop tôt", [
"La revue rappelle que le priming par stéroïdes sexuels avant un test de stimulation de l'hormone de croissance reste discuté, mais que des guides de 2016 le suggèrent chez le garçon prépubère de plus de 11 ans ou la fille prépubère de plus de 10 ans lorsque le pronostic de taille adulte reste dans −2 déviations standards, afin d'éviter une hormone de croissance inutile.",
"Les études citées sont de faible effectif et parfois contradictoires. Vous ne présentez pas le priming comme une obligation suisse.",
"Vous ne faites pas ce test si la taille et la vitesse collent au retard constitutionnel et qu'aucune autre raison n'existe.",
"Un enfant beaucoup plus petit que le cadre habituel, au-delà d'une petite taille modérée, sort de la description « usually not severe » de la revue et mérite le bilan somatotrope.",
"Vous n'annoncez pas un résultat de test que vous n'avez pas. Le gold standard du déficit en hormone de croissance n'est pas relu dans une AIPS ni dans un consensus suisse ici.",
"Piège d'examen : hormone de croissance prescrite le premier jour à un garçon de 14 ans dont le père a poussé tard et dont l'âge osseux a deux ans de retard.",
], "[S202]"),
("Suivi : ce qui confirme et ce qui infirme", [
"Vous revoyez le stade et la vitesse. La croissance du volume testiculaire signe le réveil de l'axe mieux qu'un dosage isolé de LH basse, car cette LH basse est attendue avant la puberté.",
"La revue cite des seuils d'inhibine B et de pic de LH après agoniste qui ont été proposés pour séparer le retard constitutionnel de l'hypogonadisme hypogonadotrope, tout en signalant des chevauchements. Vous ne les utilisez pas comme des lois suisses.",
"Si rien ne progresse après la période convenue, vous reprenez l'hypothèse d'un hypogonadisme permanent et vous adressez.",
"Si un signe neurologique apparaît, vous stoppez l'étiquette de variante et vous cherchez une lésion.",
"Si la fille n'a toujours pas de caryotype, le dossier n'est pas clos.",
"La sortie du suivi spécialisé se justifie quand la puberté propre de l'enfant avance, que la vitesse remonte et que les exclusions tiennent.",
], "[S201], [S202]"),
("Mots interdits à l'oral parce qu'ils dépassent les sources", [
"Vous ne dites pas « 65 % des garçons suisses ». Ce pourcentage n'a pas été lu.",
"Vous ne dites pas « la dose suisse est 50 mg ». Ce chiffre vient de la revue européenne, pas d'une AIPS ouverte.",
"Vous ne dites pas « la taille finale est toujours normale ». L'ESPE dit le contraire pour les retards extrêmes.",
"Vous ne dites pas « une LH basse prouve l'hypogonadisme ». Elle est physiologique chez le prépubère.",
"Vous ne dites pas « les courbes OMS de 2011 restent la référence suisse en 2026 ». pédiatrie suisse recommande les courbes nationales depuis le 15 juin 2026.",
"Vous ne dites pas qu'un audit a validé ce texte. L'audit est différé, et cette session n'en fait pas.",
], "[S201], [S202], [S204]"),
("Réponses brèves aux questions du point 1 à 4", [
"La définition est précise, attribuée à l'ESPE, et elle sépare la variante des maladies d'organe.",
"L'épidémiologie donne un chiffre européen sourcé, l'histoire naturelle du pic, et elle avoue l'absence de registre suisse.",
"La physiopathologie part du silence de l'axe après la minipuberté, passe par le cartilage et l'âge osseux, et relie chaque perturbation à une exploration et à une conduite.",
"Les hypothèses graves viennent avant la variante : Turner, insuffisance gonadique, déficit somatotrope, hypogonadisme permanent, lésion si signe neurologique.",
"Chaque hypothèse a un examen qui tranche et un piège nommé.",
"Si une de ces réponses devenait fausse après lecture de l'Appel A, il faudrait réaligner le nom du DX, pas inventer un compromis.",
], "[S201], [S202]"),
("Réponses brèves aux questions du point 5 à 8", [
"Chaque question d'anamnèse porte une raison : tempo familial, anosmie, cassure de canal.",
"Les drapeaux sont actionnables : caryotype, imagerie si signe neurologique, ne pas conclure si la vitesse s'effondre.",
"L'examen met la mesure normale avant le signe pathologique, et il dit comment palper et comment calculer une vitesse.",
"Le syndrome est éclaté en signes fonctionnels et physiques, et chaque signe physique a un geste.",
"Les critères viennent de l'ESPE et de la revue, pas d'une société suisse nommée que nous n'avons pas lue. Cette limite est écrite.",
"Un père « en retard » ne suffit pas. Un percentile isolé ne suffit pas. Une LH basse isolée ne suffit pas.",
], "[S201], [S202], [S205]"),
("Réponses brèves aux questions du point 9 à 14", [
"Le gold standard biologique unique n'existe pas. C'est écrit. L'âge osseux mesure le temps restant.",
"La première intention et la deuxième intention sont séparées, et les cas discordants sont dans le tableau.",
"L'arbre dit quel signe mène à quelle décision, y compris le refus de classer une céphalée en variante.",
"Le but est chiffré en durée de puberté, pas en dose. La dose AIPS est assumée comme non trouvée.",
"Les trois niveaux de prévention sont présents, et l'absence de programme OFSP nommé est assumée.",
"Les pièges d'examen ont chacun leur bonne réponse, y compris le refus d'une dose de mémoire.",
], "[S201], [S204]"),
]

DX6 = [
("Trois calculs au tableau", [
"Mère 162 cm, père 175 cm. Somme 337. Garçon (337 + 13) / 2 = 175 cm. Fille (337 − 13) / 2 = 162 cm. Intervalle ± 8,5 cm. Calcul dérivé, formule Paediatrica.",
"Mère 155 cm, père 170 cm. Somme 325. Garçon (325 + 13) / 2 = 169 cm. Fille (325 − 13) / 2 = 156 cm. Calcul dérivé.",
"Un enfant qui grandit dans cet intervalle, sur un canal stable depuis l'âge de 2 ans, réalise le modèle décrit par le PEZZ.",
"Le 3e percentile vaut −1,88 déviation standard dans le texte suisse de 2016. Vous citez les deux écritures ensemble.",
"Vous dites qu'il y a statistiquement autant d'enfants sous le 3e percentile qu'au-dessus du 97e, et que les consultations pour petite taille sont pourtant plus nombreuses parce que la société accepte mieux la grande taille.",
"Vous ne transformez pas ce constat sociétal en prévalence de la petite taille familiale.",
], "[S304], [S303], [S302]"),
("Canal et cassure", [
"Le PEZZ donne deux ans pour que l'enfant rejoigne le canal hérité. Une déviation dans cette fenêtre n'est pas, à elle seule, une maladie.",
"Après le deuxième anniversaire, le canal doit tenir jusqu'à la puberté. Un exemple du PEZZ : un garçon au 50e percentile à 2 ans devrait y rester jusque vers 12 ans si tel est son canal.",
"Le 10e percentile signifie que, sur 100 enfants sains du même âge et du même sexe, 9 sont plus petits et 90 sont plus grands. Ce n'est pas un diagnostic.",
"Vous exigez plusieurs mesures. Une courbe n'est pas un point.",
"Si le canal casse, vous quittez la petite taille familiale et vous ouvrez la cœliaquie, l'hypothyroïdie et les autres DX du SSP.",
"La vitesse de l'exemple 110,0 à 115,6 cm en un an vaut 5,6 cm par an. Ce calcul dérivé illustre une trajectoire parallèle, il ne crée pas un seuil officiel.",
], "[S303]"),
("Ce que vous refusez de prescrire", [
"Aucune source lue n'indique l'hormone de croissance pour un enfant dont la taille est expliquée par la cible et dont la vitesse garde le canal.",
"Vous le dites clairement à la famille, pour éviter un traitement qui n'a pas de cible lésionnelle dans ce cadre.",
"Vous ne promettez pas un gain en centimètres. Le but est la justesse du classement.",
"Vous mesurez au moins une fois par an, consigne PEZZ, sur les courbes recommandées depuis le 15 juin 2026.",
"Vous réévaluez si la puberté manque à 13 ans chez la fille ou à 14 ans chez le garçon, seuils ESPE, parce que le cadre familial suppose un tempo normal.",
"Vous demandez alors le raisonnement du DX.5, y compris le caryotype chez la fille.",
], "[S302], [S303], [S306]"),
("Limite honnête du diagnostic", [
"Vous n'avez pas lu de consensus suisse qui porterait le titre « petite taille familiale » avec des critères numérotés. Vous le dites.",
"Le cadre que vous utilisez assemble la formule de cible, le canal du PEZZ et l'absence des critères de retard constitutionnel. C'est une construction explicite, pas une citation unique.",
"Cette honnêteté protège l'étudiant : il sait ce qui est lu et ce qui est opératoire.",
"Si l'Appel A, non lu, a nommé ce DX autrement, l'intégrateur devra aligner le titre. Vous n'inventez pas un second nom.",
"La fréquence suisse de l'entité reste non quantifiée. Le badge le dit.",
"Vous ne comblez pas ce trou par un pourcentage de mémoire.",
], "[S304], [S303]"),
]

DX7 = [
("Algorithme ESPGHAN à voix haute", [
"Vous vérifiez d'abord que l'enfant mange du gluten. Sinon la sérologie et les biopsies perdent leur sens.",
"Vous dosez les IgA totales et les IgA anti-transglutaminase 2. Vous ne commencez pas par les peptides déamidés ni par les anti-gliadine native.",
"Si les IgA sont basses pour l'âge, ou inférieures à 0,2 g/L après 3 ans, vous passez à un test IgG et vous prévoyez des biopsies si ce test est positif.",
"Si les IgA anti-transglutaminase atteignent au moins 10 fois la limite, sur un test dont la calibration couvre cette valeur, vous demandez les anti-endomysium IgA sur un second prélèvement.",
"Si ces anti-endomysium sont positifs et que la famille comprend le diagnostic et accepte le régime, vous pouvez vous passer de biopsie, avec un praticien expérimenté. Les symptômes et le HLA ne sont pas exigés. Cela vaut aussi chez l'enfant asymptomatique.",
"Sous 10 fois la limite, vous demandez au moins quatre biopsies du duodénum distal et au moins une du bulbe, sous gluten.",
], "[S307]"),
("Pourquoi la croissance entre dans ce DX", [
"L'ESPGHAN cite le défaut de croissance, la petite taille, le défaut de prise de poids, la perte de poids et la diarrhée chronique parmi les manifestations.",
"Les symptômes classiques de malabsorption sont plus spécifiques. L'anémie ferriprive, la constipation chronique et les défauts de l'émail augmentent le risque. Les douleurs isolées n'ont pas une preuve suffisante.",
"Une cassure de canal après 2 ans, au sens du PEZZ, justifie cette recherche même si l'abdomen est banal.",
"Vous ne donnez pas d'hormone de croissance avant ce résultat, parce que vous traiteriez le cartilage sans rendre les substrats.",
"Le régime sans gluten est le traitement, pas un test diagnostique. Vous ne le démarrez pas « pour voir » avant les prélèvements.",
"La prévalence suisse n'a pas été lue. Vous ne dites pas 1 %.",
], "[S307], [S303]"),
("Cas de titre intermédiaire", [
"Un enfant casse sa courbe. Les IgA sont normales. Les anti-transglutaminase valent 4 fois la limite supérieure. Vous n'annoncez pas la maladie.",
"Vous adressez pour les biopsies sous gluten. Vous expliquez pourquoi le seuil de 10 fois n'est pas atteint.",
"Si l'histologie et la sérologie discordent, l'ESPGHAN demande une relecture des coupes ou un second avis de pathologiste.",
"Si l'histologie est Marsh 0 ou I alors que l'auto-immunité est confirmée, vous suivez de près. Vous ne banalisez pas.",
"Un HLA DQ2 ou DQ8 positif ne confirme rien. Leur absence rend la maladie très improbable.",
"Vous notez que la guideline citée est celle de 2020 et qu'une version plus récente n'a pas été identifiée dans les sources ouvertes.",
], "[S307]"),
("Ce que vous dites à la famille sur le régime", [
"Le régime vient après le diagnostic, pas avant. La famille doit comprendre l'engagement, condition explicite pour éviter la biopsie.",
"Vous ne promettez pas un nombre de centimètres de rattrapage : ce chiffre suisse n'a pas été lu.",
"Vous dites que le cartilage encore ouvert peut bénéficier de la restauration de l'absorption, sans inventer un délai.",
"Vous corrigez une dénutrition sans attendre la biopsie si l'enfant est en danger, tout en préservant le gluten si les tests ne sont pas faits et si l'état le permet.",
"Il n'y a pas de médicament de première ligne dans les passages lus. Vous ne inventez pas une spécialité.",
"Le suivi appartient à un praticien expérimenté, phrase de la guideline.",
], "[S307]"),
]

DX8 = [
("Deux biologistes, deux chemins", [
"Vous dosez toujours la TSH et la thyroxine libre. Pedlaus construit le diagnostic là-dessus.",
"Thyroxine libre basse et TSH haute : hypothyroïdie primaire. Vous demandez une échographie de la loge, et les anticorps anti-TPO et anti-thyroglobuline si vous suspectez une thyroïdite.",
"Thyroxine libre basse et TSH basse : hypothyroïdie centrale. Vous demandez une IRM hypothalamo-hypophysaire et vous cherchez d'autres déficits. Vous ne vous arrêtez pas à une TSH « normale ».",
"La T3 libre et la TBG sont très rarement nécessaires, phrase lue.",
"La cause la plus fréquente est la thyroïdite de Hashimoto. Vous citez 1 enfant d'âge scolaire sur 500 comme l'écrit la fiche, sans en faire une incidence OFS.",
"Le traitement substitue. Il ne guérit pas la maladie auto-immune.",
], "[S401]"),
("Causes rares à ne pas oublier à l'oral", [
"Kyste du tractus thyréoglosse, parfois familial. Hémithyroïde et autres malformations. Excès d'iode. Lithium. Amiodarone. Radioiode.",
"Hémangiome hépatique : la désiodase de type 3 convertit la T4 en reverse T3 et la T3 en T2. Vous le citez comme cause rare lue, pas comme un diagnostic de première intention.",
"Une hausse de la TBG sous œstrogène ou pendant une grossesse peut diminuer la biodisponibilité. La fiche le dit. Vous ne déduisez pas une dose.",
"L'hypothyroïdie centrale par absence de TSH est rare, mais le chemin IRM reste obligatoire quand la biologie est centrale.",
"Vous palpez le cou à la déglutition avant l'échographie.",
"Vous ne traitez pas un goitre isolé sans biologie, et la fiche admet que certains Hashimoto se surveillent sans lévothyroxine. Le seuil chiffré de cette surveillance n'est pas dans la fiche.",
], "[S401]"),
("Croissance et puberté dans cette fiche", [
"Les signes lus sont la frilosité, la constipation, le retard de croissance avec prise de poids, le goitre, la baisse d'attention, la diminution de croissance des os longs, les cheveux secs et cassants.",
"La puberté retardée est fréquente. Une puberté avancée peut aussi survenir. Vous apprenez les deux.",
"Vous distinguez ce tableau de l'obésité nutritionnelle, où la croissance ne s'arrête pas de cette façon. La fiche décrit ici le couple retard de croissance et prise de poids.",
"Non traitée, l'hypothyroïdie diminue la qualité de vie, la croissance, les réflexes, la mémoire et la force.",
"Chez une femme enceinte non traitée, le développement neuronal du fœtus peut être atteint. Vous traitez. La dose reste celle de l'AIPS, non lue.",
"Le surdosage crée une hyperthyroïdie. Vous le dites au patient sans inventer le palier de réduction.",
], "[S401]"),
("Ce que vous n'écrivez pas sur l'ordonnance", [
"Vous n'écrivez pas de microgrammes par kilogramme. La fiche d'enseignement n'est pas l'information professionnelle Swissmedic.",
"Vous nommez la classe, la lévothyroxine, et vous stoppez le chiffre.",
"Vous adressez ou vous ouvrez l'AIPS avant de signer. Cette session ne l'a pas ouverte.",
"Vous surveillez la TSH et la thyroxine libre jusqu'à leur normalisation et jusqu'à la correction des signes, but écrit par Pedlaus.",
"Le calendrier en semaines n'est pas dans la fiche. Vous ne l'inventez pas.",
"Vous suivez la courbe de croissance pour voir le cartilage répondre, sans promettre un nombre de centimètres.",
], "[S401]"),
]

DX9 = [
("Lire 0,48 cm sans en faire une sentence", [
"La synthèse Cochrane décrit une réduction moyenne de 0,48 cm par an de la vitesse pendant la première année chez l'enfant prépubère qui a un asthme persistant léger à modéré, avec une certitude modérée.",
"Vous dites « en moyenne dans les essais ». Vous ne dites pas « votre enfant perdra 0,48 cm ».",
"L'effet est maximal la première année et moindre ensuite.",
"Une partie de la baisse de taille acquise au début peut rester à l'âge adulte. Elle n'est ni progressive ni cumulative.",
"L'effet paraît dépendre de la dose, certitude modérée. La molécule et le dispositif peuvent compter, avec une certitude plus faible.",
"La fluticasone semble freiner moins que la béclométasone ou le budésonide à dose équivalente dans certains essais. Ce n'est pas un ordre de substitution suisse.",
], "[S402], [S403]"),
("Mécanisme que vous pouvez raconter", [
"Le produit inhalé qui passe dans le sang diminue la sécrétion pulsatile d'hormone de croissance.",
"Il réduit le récepteur de cette hormone au cartilage et au foie, et il réduit l'IGF-1 et son activité.",
"Les chondrocytes prolifèrent moins et entrent davantage en apoptose. L'os long grandit plus lentement.",
"Vous corrigez l'exposition, pas l'IGF-1 par un médicament qui n'est pas dans ces revues.",
"Vous ne stoppez pas un asthme mal contrôlé pour un effet moyen d'un demi-centimètre. Le contrôle respiratoire reste la raison du traitement.",
"Vous cherchez la plus faible dose efficace et vous vérifiez la technique d'inhalation.",
], "[S403]"),
("Quand le spray n'explique plus tout", [
"Un ralentissement massif, des vergetures, une prise de poids rapide ou une hypertension dépassent l'effet moyen des essais sur l'asthme léger.",
"Vous cherchez alors une autre cause du SSP, dont l'hypothyroïdie et la cœliaquie, et vous discutez un hypercorticisme endogène.",
"Le protocole suisse du freinage à la dexaméthasone n'a pas été lu. Vous ne l'inventez pas.",
"Vous listez les voies inhalée, nasale, orale et cutanée. Le piège est d'oublier l'inhalateur « parce qu'il est local ».",
"Vous mesurez surtout pendant la première année, période du maximum d'effet.",
"La fréquence suisse de cet effet indésirable n'est pas dans les revues lues.",
], "[S402], [S403]"),
("Prévention sans interdire la classe", [
"La revue rappelle que les corticoïdes inhalés sont le traitement de fond de l'asthme persistant. La prévention primaire n'est pas l'abstention systématique.",
"La prévention secondaire est la mesure de la taille dès la première année.",
"La prévention tertiaire est la baisse de dose quand le contrôle le permet, pour éviter une exposition inutile.",
"Vous ne promettez pas un retour au potentiel génétique au millimètre.",
"Vous n'écrivez aucune marque ni aucune dose AIPS.",
"Vous documentez la vitesse en centimètres par an, seule grandeur qui rend l'effet visible.",
], "[S402]"),
]

DX10 = [
("Séparer la variante de la puberté précoce", [
"Le chapitre espagnol définit la puberté précoce par des caractères sexuels secondaires avant 8 ans chez la fille et avant 9 ans chez le garçon, pour une population caucasienne de pays développés.",
"La thélarche isolée et la pubarche isolée sont des variantes incomplètes. Elles peuvent rester stables, régresser, ou progresser vers une puberté précoce vraie.",
"Vous palpez une glande. Vous ne comptez pas un coussin graisseux.",
"Une pilosité isolée sans accélération de croissance et sans virilisation reste dans la variante jusqu'à preuve de progression.",
"Dès que la vitesse accélère ou qu'un second caractère apparaît, vous quittez ce DX.",
"Vous ne traitez pas une forme stable par un analogue de la GnRH. La dose AIPS de cet analogue n'a pas été lue, et l'indication n'est pas ce DX.",
], "[S404]"),
("Filles et garçons ne s'équivalent pas", [
"L'incidence citée de la puberté précoce va de 1/5 000 à 1/10 000, avec un rapport filles sur garçons de 20 pour 1. Ce chiffre n'est pas celui de la thélarche isolée.",
"Chez la fille, le chapitre attribue 98 % des pubertés précoces à une forme centrale, et il cite 74 % de formes idiopathiques dans une série italienne.",
"Chez le garçon, la part neurogène varie de 94 % à 40 % selon les auteurs du chapitre. Vous n'applique pas la même attente.",
"Avant 4 ans, la part neurogène est plus haute chez la fille. Le texte recommande aussi de ne pas exclure une étude du système nerveux central chez des filles de plus de 7 ans lorsqu'une lésion est possible.",
"Une ménarche maternelle précoce n'est retrouvée que dans 4 % d'une série citée. L'histoire familiale ne ferme pas le dossier.",
"La fréquence suisse de la thélarche isolée reste non quantifiée.",
], "[S404]"),
("Saignement sans autre signe", [
"La ménarche précoce isolée est rare : filles de 1 à 9 ans, saignements cycliques, pas d'autre signe pubertaire.",
"Vous écartez une infection, un corps étranger, une tumeur, un McCune-Albright, un œstrogène exogène et une hypothyroïdie.",
"Le chapitre demande alors une échographie pelvienne, un âge osseux, un test à la GnRH et un estradiol.",
"Les règles peuvent revenir pendant un à six ans puis laisser place à une puberté à âge normal. Vous surveillez quand même une progression.",
"Vous informez et vous rassurez seulement après ces exclusions, phrase du chapitre.",
"Vous ne posez pas un analogue sur ce seul saignement.",
], "[S404]"),
("Surveillance concrète", [
"Vous datez le premier signe, vous cherchez un produit œstrogénique, vous mesurez la vitesse sur la courbe suisse en vigueur.",
"Vous revoyez la palpation et la courbe. Le chapitre 8 ne fixe pas un nombre de semaines. Vous ne l'inventez pas.",
"Vous élargissez dès qu'un drapeau apparaît : progression, garçon, signe neurologique, virilisation, âge osseux qui avance.",
"L'imagerie et le test à la GnRH appartiennent alors à la puberté précoce, pas à la variante stable.",
"Le pronostic de la variante est la stabilité, la régression ou une puberté plus tard normale. La progression change la taille parce que l'âge osseux avance.",
"Vous le dites aux parents avec ces trois issues, sans pourcentage suisse.",
], "[S404], [S405]"),
]

PACKS = {"dx5": DX5, "dx6": DX6, "dx7": DX7, "dx8": DX8, "dx9": DX9, "dx10": DX10}

def extra(key):
    import importlib.util, os
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gloss_lot183.py")
    spec = importlib.util.spec_from_file_location("gl", path)
    gl = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gl)
    parts = [gl.gloss(key)]
    for title, lines, source in PACKS[key]:
        parts.append(block(title, lines, source))
    import importlib.util as _ilu
    _path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "approfondir_lot183.py")
    _spec = _ilu.spec_from_file_location("ap183", _path)
    _ap = _ilu.module_from_spec(_spec)
    _spec.loader.exec_module(_ap)
    parts.append(_ap.plus(key))
    parts.append(
        "<div style='margin:12px 0;'><strong>Question finale</strong><br>"
        + p("Un lecteur peut répondre aux seuils, à la cible parentale, à l'algorithme qui concerne ce DX et aux pièges d'examen avec les sources citées. Il ne peut pas signer une dose : aucune AIPS n'a été ouverte. Il ne peut pas citer une prévalence suisse qui n'a pas été lue. Avec ces limites écrites, la prise en charge immédiate reste sûre, parce qu'elle consiste à mesurer, à exclure la maladie grave et à ne pas inventer un médicament.")
        + "</div>"
    )
    return "".join(parts)
