#!/usr/bin/env python3
"""Phase A du LOT_161, F2.13 Lipides sériques anormaux."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur import GLOSSAIRE, SOURCES_LI, bouton, ecrire, fenetre, p_html, page, phrases

def bloc(texte: str) -> str:
    return "".join(p_html(t, s) for t, s in phrases(texte))

def section(n, titre, fiche, detail, extra=""):
    classe = "c" if n % 2 else "v"
    ident = f"a-p{n}"
    fiche_html = bloc(fiche)
    ouvre = f"<p>On ouvre {bouton(ident, 'la fenêtre de ce point')}.</p>"
    corps = bloc(detail) + extra
    return (
        f'<section class="ilot {classe}"><h2 id="p{n}">{n}. {titre}</h2>'
        f"{fiche_html}{ouvre}{fenetre(ident, f'{n}. {titre}', corps)}</section>"
    )

F1 = """
La situation F2.13 nomme un bilan lipidique anormal, pas encore une maladie.

Le prélèvement usuel donne le cholestérol total, le cholestérol HDL et les triglycérides.

Le cholestérol LDL est le plus souvent calculé à partir de ces trois mesures.

Une valeur hors norme ouvre une démarche. Elle ne choisit pas à elle seule le médicament.

Les dix diagnostics de la leçon couvrent le LDL haut polygénique, le syndrome métabolique, les deux formes familiales, les triglycérides, les causes secondaires, la lipoprotéine(a), la dysbêtalipoprotéinémie, la chylomicronémie et les hypolipoprotéinémies.
"""

D1 = """
Un lipide sérique anormal est un résultat. Le nom de la maladie vient ensuite de la démarche.

Le cholestérol total se répartit surtout entre VLDL, LDL et HDL. Des parts plus petites voyagent avec les IDL et la lipoprotéine(a).

Le guide de 2019 rappelle que le laboratoire mesure d'ordinaire le cholestérol total, le HDL et les triglycérides. Le LDL en est déduit.|s1

La formule de Friedewald s'écrit, en mmol/l, LDL égal au total moins le HDL moins les triglycérides divisés par 2,2.|s1

En mg/dl, on divise les triglycérides par 5, pas par 2,2.|s1

La formule suppose un rapport constant entre cholestérol et triglycérides dans les VLDL. Ce rapport n'est pas constant chez tout le monde.|s1

Au-dessus de 4,5 mmol/l de triglycérides, soit 400 mg/dl, la formule ne doit pas être utilisée.|s1

Cette limite compte surtout si le patient n'est pas à jeun.|s1

Dès 2 mmol/l de triglycérides, le LDL calculé tend à sous-estimer le LDL mesuré.|s1

Quand le LDL est déjà très bas et que les triglycérides sont hauts, le calcul peut égarer.|s1

Le dosage enzymatique direct du LDL existe. Il a lui aussi un biais, surtout si les triglycérides sont hauts.|s1

Le cholestérol non HDL se calcule en soustrayant le HDL du cholestérol total. Il additionne toutes les particules qui portent l'apolipoprotéine B.|s1

La cible secondaire de non HDL se place 0,8 mmol/l au-dessus de la cible de LDL du même niveau de risque.|s1

Pour un risque très élevé, un risque élevé et un risque modéré, ces cibles secondaires de non HDL sont inférieures à 2,2, à 2,6 et à 3,4 mmol/l.|s1

Les cibles secondaires d'apolipoprotéine B correspondantes sont inférieures à 65, à 80 et à 100 mg/dl.|s1

Après un deuxième événement vasculaire, une cible de non HDL inférieure à 1,8 mmol/l et une apolipoprotéine B inférieure à 55 mg/dl peuvent se discuter.|s1

Exemple chiffré. Cholestérol total 6,2 mmol/l, HDL 1,1 mmol/l, triglycérides 2,2 mmol/l. Les triglycérides divisés par 2,2 valent 1,0. Le LDL calculé vaut 4,1 mmol/l.

Même total et même HDL, mais triglycérides à 6,0 mmol/l. On n'applique plus Friedewald. On garde le non HDL, ici 5,1 mmol/l, et on demande un avis de dosage.

Les unités du cours sont les mmol/l. Les mg/dl des guides sont la traduction lue, pas une deuxième cible inventée.

Un LDL calculé dans la cible ne ferme pas le dossier si les triglycérides, le HDL ou la lipoprotéine(a) racontent autre chose.

La leçon classe dix diagnostics. L'ordre DX est l'ordre du cours. Le rang E est l'ordre d'urgence de l'algorithme, pas une fréquence suisse.
"""

F2 = """
En Suisse, les maladies cardiovasculaires sont la deuxième cause de mortalité après le cancer.|s3

Le GSLA désigne le LDL comme un facteur majeur et rappelle qu'aucune valeur plancher de bénéfice n'est décrite.|s3

Aucune source lue ne classe les dix diagnostics selon leur fréquence en Suisse.
"""

D2 = """
La page suisse lue en 2026 s'appuie sur l'Office fédéral de la statistique pour cette deuxième place.|s3

Le même texte dit que l'hypercholestérolémie génétique expose plus longtemps que la forme acquise. Il parle de cholestérol-années, sur le modèle des paquets-années du tabac.|s3

Le plus tôt le mieux s'ajoute donc à l'idée que plus le LDL est bas, mieux c'est.|s3

Le GSLA aligne ses recommandations sur les guides européens, puis les adapte aux particularités suisses.|s3

Son calculateur s'adresse aux personnes apparemment en bonne santé, de 20 à 69 ans, sans diabète.|s3

SCORE2 et SCORE2-OP servent d'alternative ou de complément de 40 à 89 ans, toujours sans diabète.|s3

SCORE2-Diabète concerne le diabète de type 2, de 40 à 69 ans, sans maladie athérosclérotique ni atteinte sévère d'organe.|s3

Le guide de poche suisse diagnostique l'hypercholestérolémie familiale de l'adulte avec les critères du réseau néerlandais et traite aussi l'intolérance aux statines.|s3

Une étude de laboratoire américaine de 2019 a compté les phénotypes de Fredrickson. Ce n'est pas un registre suisse.|s5

Dans cette étude, le phénotype IV était le plus fréquent, puis le IIb. Les types I et V restaient rares.|s5

Le cours ne transporte pas ces pourcentages comme s'ils décrivaient la Suisse.

L'absence d'un classement suisse des dix diagnostics est notée hors du cours. On ne fabrique pas une prévalence pour remplir la case.

Le risque cardiovasculaire, lui, est chiffré par les outils suisses et européens cités. Ce n'est pas la même question que la fréquence de chaque maladie lipidique.

Homme et femme n'ont pas le même âge de maladie coronaire précoce dans les critères familiaux : avant 55 ans chez l'homme, avant 60 ans chez la femme.|s1

Cette différence sert au réseau néerlandais et à l'histoire familiale. Elle ne dit pas qui a le plus souvent un LDL haut dans le pays.

Le diabète et l'obésité augmentent les phénotypes riches en triglycérides dans l'étude américaine. Le mécanisme est repris au point du syndrome métabolique, sans chiffre suisse inventé.|s5
"""

F3 = """
Le foie fabrique des VLDL. Les LDL naissent de leur dégradation et sont repris par le récepteur LDL.

La lipoprotéine(a) est surtout fixée par le patrimoine génétique. L'alimentation la bouge peu.

Une lipase défaillante laisse les chylomicrons dans le plasma et menace le pancréas.
"""

D3 = """
L'atorvastatine inhibe l'HMG-CoA réductase. Le foie synthétise moins de cholestérol et expose davantage de récepteurs LDL.|s6

Les triglycérides et le cholestérol hépatiques entrent dans les VLDL, puis le plasma. Les LDL viennent de ces VLDL et sont dégradées surtout par le récepteur de haute affinité.|s6

Une mutation qui éteint le récepteur LDL, une mutation de l'apolipoprotéine B, ou une mutation qui active PCSK9, diminuent cette clairance. Environ 95 pour cent des formes familiales monogéniques tiennent au récepteur.|s1

Plus de mille mutations du récepteur sont décrites. La perte complète de fonction élève plus le LDL et le risque vasculaire que la perte partielle.|s1

PCSK9 détruit le récepteur. Un anticorps ou un petit ARN qui baisse PCSK9 laisse davantage de récepteurs à la surface.

L'acide bempédoïque inhibe l'ACL, en amont de l'HMG-CoA réductase. L'enzyme qui l'active est exprimée dans le foie et pas dans le muscle squelettique.|s12

L'ézétimibe bloque l'absorption intestinale du cholestérol. Il ne remplace pas la baisse de synthèse hépatique. Les deux gestes s'additionnent.

Les chylomicrons portent les graisses du repas. La lipase lipoprotéique les vide. L'apolipoprotéine C-II active cette lipase. L'apolipoprotéine C-III la freine.

Une atteinte des deux copies de LPL, d'apoC-II, d'apoA-V, de LMF1, de GPIHBP1 ou de GPD1 casse cette voie. Le guide de 2019 en fait des traits récessifs rares.|s1

Le plasma devient alors lactescent et les triglycérides dépassent 11,2 mmol/l dans la description monogénique.|s1

Entre 2 et 10 mmol/l, l'élévation modérée des triglycérides est le plus souvent polygénique, par production et épuration des VLDL.|s1

La lipoprotéine(a) ajoute une particule de type LDL et une apolipoprotéine(a). Sa concentration est surtout génétique.|s2

Le risque d'événement majeur commence à monter un peu au-dessus de 30 mg/dl, soit 62 nmol/l, et devient net à partir de 50 mg/dl, soit 105 nmol/l.|s2

Au-dessus de 180 mg/dl, soit 430 nmol/l, le guide de 2019 rapproche le risque de celui d'une forme familiale hétérozygote.|s1

Les remnants, ou IDL, s'accumulent dans la dysbêtalipoprotéinémie, souvent sur un fond apoE2 homozygote plus une charge polygénique.

Le HDL ramène le cholestérol vers le foie. Un HDL bas n'est pas, à lui seul, une cible de médicament dans le guide de 2019. Il signale souvent les triglycérides et le syndrome métabolique.

La maladie de Tangier et le déficit en lécithine-cholestérol acyltransférase abaissent fortement le HDL et demandent un avis spécialisé.|s1

L'hypobêtalipoprotéinémie laisse un LDL souvent entre 0,5 et 1,5 mmol/l. L'abêtalipoprotéinémie est plus profonde et touche l'intestin et le système nerveux.|s1

Le déficit en lipase acide lysosomale élève le LDL, baisse le HDL et gonfle le foie. Une statine baisse le LDL mais ne stoppe pas la maladie du foie.|s1
"""

