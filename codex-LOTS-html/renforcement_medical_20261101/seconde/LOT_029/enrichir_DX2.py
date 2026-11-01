#!/usr/bin/env python3
"""Renforcement ciblé de DX2, sauvegarde préalable exigée, sans resérialisation."""
from pathlib import Path
import re,json,hashlib,gzip
from lxml import html
from enrichir import bloc, refs, ajouter_corps

BASE=Path(__file__).resolve().parent
LOT=BASE.parents[2]/'LOT_029'
FN='LOT_029_Phase_B_V0_DX.2.html'

D={
1:(bloc('Un diagnostic associant croissance et anatomie',
    '<strong>Trois éléments doivent concorder :</strong> un périmètre élevé ou croissant, des espaces sous-arachnoïdiens élargis à l’imagerie et l’absence d’autre cause expliquant l’ensemble. Une simple mention d’espaces péricérébraux larges ne suffit pas à retenir le diagnostic. Une petite tête ou un centile céphalique décroissant impose notamment de discuter un défaut de développement cérébral ou une atrophie.',
    'Le mot <em>bénin</em> décrit l’évolution habituellement favorable de la forme typique, sans garantir celle de chaque enfant. Les anciennes expressions hydrocéphalie externe, collection extracérébrale ou hygroma ont parfois été utilisées de façon imprécise. Le compte rendu doit nommer le compartiment réellement atteint : <strong>sous-arachnoïdien</strong> et <strong>sous-dural</strong> ne sont pas synonymes.'),[7,11]),
2:(bloc('Distinguer réduction des espaces et évolution du périmètre',
    'L’évolution typique comporte une accélération du périmètre pendant la première enfance, puis une stabilisation. La diminution des espaces liquidiens ne signifie pas nécessairement que la tête revient au centile médian : le périmètre peut rester élevé en suivant ensuite une courbe parallèle. Les âges publiés varient selon les séries et ne constituent pas une échéance permettant d’attendre malgré des symptômes.',
    '<strong>Le pronostic fonctionnel se vérifie.</strong> La majorité des enfants décrits évoluent favorablement, mais des difficultés motrices ou langagières peuvent être transitoires ou persister. L’imagerie qui s’améliore ne prouve donc pas que tous les besoins développementaux ont disparu. Les données étrangères citées ne permettent pas de fournir une fréquence suisse ni un risque individuel chiffré.'),[7,11]),
3:(bloc('Une physiopathologie discutée, une localisation à préciser',
    'L’espace sous-arachnoïdien contient le liquide cérébrospinal et des vaisseaux. Dans l’aspect typique, ceux-ci traversent les espaces élargis sans être repoussés contre la surface cérébrale. Une collection sous-durale se trouve dans un autre plan et peut déplacer la membrane arachnoïdienne et les vaisseaux vers le cortex.',
    '<strong>Les explications mécanistiques restent des hypothèses :</strong> maturation des voies de résorption du liquide, décalage entre croissance crânienne et cérébrale, ou contribution du drainage veineux. La revue de2023 souligne les connaissances encore incomplètes sur les voies de sortie du liquide chez le nourrisson. Il serait excessif de présenter une immaturité des villosités arachnoïdiennes comme cause démontrée chez chaque enfant.',
    'L’hypothèse d’une prédisposition aux hémorragies sous-durales par étirement des veines est également discutée. La coexistence d’espaces élargis et d’une collection ne suffit pas à démontrer ce mécanisme ni à expliquer des lésions traumatiques associées.'),[7,11]),
4:(bloc('Ne pas attribuer un symptôme aigu à une étiquette rassurante',
    '<strong>Vomissements avec fontanelle tendue, trouble du regard, altération de conscience ou déficit</strong> imposent de rechercher une pression élevée, une collection ou une autre affection. Une crise ou une dégradation de l’état général doit également être évaluée selon sa gravité. La stabilisation attendue du périmètre n’est pas un motif de report.',
    'Lorsque des espaces élargis coexistent avec une collection sous-durale, le peu de symptômes ne permet pas de conclure que le tableau est sans risque. À l’inverse, irritabilité, somnolence ou fontanelle bombée ne déterminent pas à eux seuls l’origine traumatique ou non de cette collection. <em>Le signe clinique détermine la sécurité immédiate ; l’ensemble du bilan recherche la cause.</em>'),[6,7,11]),
5:(bloc('Une chronologie qui évite les explications rétrospectives',
    'Reconstituer les mesures antérieures, leur fiabilité et les données néonatales, puis dater l’apparition des symptômes et des difficultés d’acquisition. Un périmètre qui accélère peut se voir dans plusieurs mécanismes. Une accélération qualifiée de brutale ne distingue pas, à elle seule, un élargissement sous-arachnoïdien d’une autre cause.',
    '<strong>Documenter les faits rapportés :</strong> événement, délai, symptômes et consultations antérieures. Ne pas reconstruire une cause certaine à partir du seul résultat d’imagerie. En présence d’une collection, l’équipe compétente précise aussi les antécédents de traumatisme ou de saignement et recherche des éléments cliniques associés.',
    'Une histoire familiale de grandes têtes est compatible avec ce diagnostic, mais ne localise pas le liquide. Elle ne dispense pas de vérifier le développement, l’examen et l’imagerie lorsqu’elle est indiquée.'),[7,11]),
6:(bloc('L’examen répond à deux questions différentes',
    '<strong>Existe-t-il un retentissement neurologique ?</strong> Évaluer vigilance, regard, fontanelle, tonus, motricité et acquisitions, en tenant compte de l’âge. Comparer la courbe céphalique à la taille et au poids. Une hypotonie ou un retard ne doit pas être banalisé parce que les espaces paraissent typiques.',
    '<strong>Existe-t-il un indice d’autre maladie ou de lésion associée ?</strong> Rechercher anomalies corporelles, cutanées ou vasculaires et signes orientant vers un syndrome. Si une collection sous-durale soulève la question d’un traumatisme, un examen complet est nécessaire, notamment de la peau et de la bouche, avec l’équipe pédiatrique formée.',
    'Un examen général ou un fond d’œil rassurant ne remplace pas les autres volets du bilan lorsque ceux-ci sont indiqués. Les examens recherchent des lésions différentes ; leur valeur ne s’additionne pas en une preuve automatique de bénignité.'),[7,11]),
7:(bloc('Les associations qui font quitter la forme typique',
    '<strong>Espaces élargis avec tête petite ou décélération céphalique :</strong> rechercher un défaut de croissance cérébrale ou une atrophie. <strong>Dilatation ventriculaire importante ou signes de pression :</strong> rechercher une hydrocéphalie et son mécanisme. <strong>Membrane, déplacement vasculaire, effet de masse ou contenu hémorragique :</strong> discuter une collection sous-durale, qui peut coexister avec l’élargissement sous-arachnoïdien.',
    '<strong>Régression, anomalies de substance blanche, organomégalie ou phénotype particulier :</strong> élargir le bilan aux causes génétiques ou métaboliques selon les constatations. Une macrocéphalie familiale constitutionnelle peut avoir une histoire similaire mais ne se définit pas par cet aspect liquidien. Chaque branche répond à une question différente, sans être exclue par le seul caractère familial.'),[7,11]),
8:(bloc('Lire un faisceau de signes, pas seulement une largeur',
    'L’association attendue comprend une prédominance frontale et interhémisphérique antérieure, un liquide d’aspect compatible avec le liquide cérébrospinal, des vaisseaux traversants et l’absence d’effet de masse. Les ventricules peuvent être normaux ou modérément augmentés. Ces éléments doivent être confrontés à l’âge, à la trajectoire et à l’examen.',
    '<strong>Un vaisseau visible ne suffit pas à tout exclure.</strong> Certaines collections sous-durales fines ont un signal proche du liquide cérébrospinal et déplacent peu les veines. La revue radiologique décrit ces exceptions : le signe des veines traversantes est utile dans un ensemble concordant, sans constituer un test infaillible.',
    'Les mesures craniocorticales, sinocorticales et interhémisphériques ne sont pas interchangeables. Les limites rapportées dépendent de l’âge et des méthodes. Le diagnostic doit expliquer la localisation et la concordance clinique, plutôt que se limiter à une largeur qualifiée de pathologique.'),[7,11]),
9:(bloc('Échographie, résonance magnétique et scanner : apports et pièges',
    '<strong>Échographie :</strong> lorsqu’une fontanelle est ouverte, l’examen des convexités avec une sonde adaptée et le Doppler peuvent montrer les vaisseaux dans le liquide. Une membrane visible, un contenu d’échogénicité différente, un déplacement vasculaire ou un effet de masse demandent une caractérisation plus poussée.',
    '<strong><abbr title="imagerie par résonance magnétique">IRM</abbr> :</strong> rechercher un ou plusieurs compartiments liquidiens, comparer leur signal et analyser les vaisseaux et le parenchyme. Si une collection est suspectée, les séquences sensibles aux produits sanguins et la diffusion recherchent respectivement une composante hémorragique et des lésions cérébrales associées. Une collection très proche du signal du liquide cérébrospinal peut rester difficile à identifier.',
    '<strong>Scanner :</strong> il peut être nécessaire dans une urgence, mais expose aux rayonnements. Une collection peu dense peut ressembler au liquide cérébrospinal ; l’absence de différence de densité ne suffit pas à la classer comme sous-arachnoïdienne. L’examen doit être choisi pour répondre à la question clinique, et non pour répéter systématiquement un diagnostic déjà concordant.' )+bloc('Si une collection sous-durale est identifiée',
    'La revue européenne propose une évaluation multidisciplinaire recherchant des lésions associées et les causes possibles de saignement. Elle comporte un examen clinique complet, un bilan hémostatique orienté, un examen ophtalmologique et une exploration squelettique selon le protocole spécialisé. Les auteurs recommandent de considérer cette exploration même si le fond d’œil et l’examen sont rassurants.',
    'Cette démarche relève d’une équipe pédiatrique compétente et des procédures locales. Elle vise à établir les faits et à protéger l’enfant, sans attribuer automatiquement la collection à une maltraitance ou aux espaces élargis. L’avis spécialisé doit être organisé rapidement, car certaines lésions recherchées peuvent évoluer et devenir moins visibles.'),[7,11]),
10:(bloc('Quatre décisions conditionnelles',
    '<strong>Si l’enfant présente une urgence neurologique,</strong> engager l’évaluation urgente sans attendre de confirmer l’étiquette d’élargissement bénin. <strong>Si l’enfant est stable,</strong> vérifier la courbe et confronter le compte rendu d’imagerie à la question du compartiment, du contenu et d’un éventuel effet de masse.',
    '<strong>Si clinique et imagerie sont concordantes, sans collection ni autre anomalie,</strong> organiser surveillance et soutien des acquisitions selon les besoins. <strong>Si une collection ou une discordance est présente,</strong> demander l’évaluation spécialisée correspondante ; une histoire familiale rassurante n’autorise pas à revenir directement à la surveillance simple.',
    'Le bilan de la cause et l’aide au développement peuvent avancer ensemble. L’attente d’une imagerie de contrôle ne doit pas retarder l’évaluation d’un retard, d’une régression ou d’un symptôme nouveau.'),[6,7,11]),
11:(bloc('Un traitement conservateur avec des objectifs concrets',
    '<strong>Dans la forme typique non compliquée,</strong> la surveillance accompagne l’évolution spontanée. L’objectif est de suivre croissance et fonction, d’informer la famille et d’éviter une intervention sans indication. Le seul volume apparent des espaces ne justifie pas une dérivation.',
    'Les traitements décrits dans certaines séries ne constituent pas une prescription standard pour tout nourrisson. Une intervention se discute pour un mécanisme ou une complication identifiés, avec l’équipe spécialisée. Aucune molécule ni posologie empirique n’est ajoutée ici.',
    'Une difficulté motrice ou langagière doit être évaluée et accompagnée selon son retentissement. Elle ne se résout pas nécessairement avec l’amélioration radiologique. Si une collection associée est découverte, son évaluation étiologique et sa prise en charge suivent une filière distincte de la simple surveillance des espaces.'),[7,11]),
12:(bloc('Ce qui guide le contrôle et les consultations anticipées',
    'Le suivi associe mesures fiables, acquisitions, examen neurologique et symptômes nouveaux. Une trajectoire stabilisée avec développement satisfaisant est rassurante. Une régression, un déficit, un trouble du regard, des vomissements inhabituels ou une somnolence demandent une nouvelle évaluation, sans attendre le prochain contrôle programmé.',
    '<strong>L’imagerie de suivi dépend de la question persistante ou nouvelle.</strong> Les sources citées ne fournissent pas un calendrier universel applicable à tous les nourrissons. Si une collection sous-durale est associée, le suivi spécialisé reste nécessaire, même lorsque le bilan initial n’a pas retenu de traumatisme infligé.',
    'Informer les proches des précautions habituelles contre les traumatismes et des signes qui doivent les faire consulter. La possibilité d’une collection doit être expliquée sans la présenter comme inévitable ni présumer de sa cause. La famille doit savoir quel professionnel contacter et quels symptômes relèvent de l’urgence.'),[1,6,7,11]),
13:(bloc('Les trois éléments d’une conclusion utile',
    '<strong>Localisation :</strong> le liquide est-il réellement sous-arachnoïdien, sans collection associée méconnue ? <strong>Concordance :</strong> croissance, développement et examen correspondent-ils au profil attendu ? <strong>Évolution :</strong> un plan permet-il de détecter rapidement une complication ou une discordance ?',
    'La réduction des espaces, la stabilisation du périmètre et le développement sont trois résultats différents. Ils ne doivent pas être utilisés comme synonymes. Un diagnostic initial raisonnable peut être révisé si une donnée nouvelle apparaît ; cette réévaluation fait partie du suivi.'),[7,11]),
}

Q=[
 'Le périmètre renseigne sur la croissance externe, mais pas sur le compartiment liquidien. L’imagerie doit être compatible et la clinique concordante ; une autre cause ne s’exclut pas par la seule grande taille de la tête.',
 'Le liquide entoure les régions frontales et peut élargir la fissure interhémisphérique antérieure. Sa localisation se vérifie avec les vaisseaux et les autres structures, sans se limiter au mot péricérébral.',
 'Une collection sous-durale peut déplacer l’arachnoïde et les vaisseaux vers le cortex. Les deux anomalies peuvent coexister : reconnaître l’une n’exclut pas la seconde.',
 'Une dilatation ventriculaire marquée, une obstruction ou des signes de pression font rechercher un autre mécanisme. Les ventricules se lisent avec le reste de l’imagerie et la clinique.',
 'Les symptômes priment sur l’évolution habituellement favorable. L’évaluation urgente recherche une complication ou une autre maladie ; elle ne doit pas attendre l’âge prévu de stabilisation.',
 'Les séries n’utilisent pas toutes les mêmes repères. La diminution des espaces peut survenir alors que le périmètre reste élevé, et aucun âge ne dispense d’évaluer un symptôme nouveau.',
 'Ce signe soutient la localisation lorsqu’il s’associe à un contenu liquidien et à l’absence d’effet de masse. Certaines collections fines déplacent peu les veines : la présence d’un vaisseau n’est pas une exclusion absolue.',
 'La mesure dépend de la structure mesurée, de l’âge et de la méthode. Un seuil isolé ne rend compte ni d’une membrane, ni du déplacement vasculaire, ni d’un retentissement cérébral.',
 'L’échographie peut montrer espaces, ventricules et vaisseaux au Doppler. Une fenêtre acoustique disponible ne garantit pas que toutes les anomalies pertinentes seront suffisamment caractérisées.',
 'Elle analyse les compartiments, leur signal et le parenchyme. Des séquences adaptées recherchent les produits sanguins ou les lésions associées si une collection est suspectée.',
 'La surveillance est adaptée quand l’ensemble clinique et radiologique est rassurant. Une intervention ne se discute qu’en fonction d’un mécanisme ou d’une complication identifiés, pas du seul qualificatif macrocrâne.',
 'La collection ne désigne pas à elle seule un mécanisme. Le bilan recherche les lésions associées, le contexte et les causes possibles avec une équipe compétente.',
 'Un fond d’œil normal ou peu de symptômes ne clôt pas la démarche. Une collection associée justifie le bilan spécialisé approprié, sans raccourci causal dans un sens ou dans l’autre.',
 'Un centile stabilisé et une imagerie améliorée ne sont pas une preuve de développement normal. Les besoins moteurs, langagiers et relationnels se réévaluent pour eux-mêmes.'
]

def main():
    p=LOT/FN;old=p.read_text();assert 'RENFORCEMENT_MEDICAL_20261101' not in old
    assert gzip.decompress((BASE/'avant'/(FN+'.gz')).read_bytes()).decode()==old
    raw=old
    for n,(text,ns) in D.items():raw=ajouter_corps(raw,f'dx2-detail{n}','<!-- RENFORCEMENT_MEDICAL_20261101 partie '+str(n)+' -->'+text+refs(ns))
    ms=list(re.finditer(r'(<details class="quiz">.*?</summary>)(.*?)(</details>)',raw,re.S));assert len(ms)==14
    for m,q in reversed(list(zip(ms,Q))):raw=raw[:m.start()]+m.group(1)+m.group(2)+'<p><strong>Raisonnement :</strong> '+q+'</p>'+m.group(3)+raw[m.end():]
    raw=ajouter_corps(raw,'dx2-detail14','<p><em>Identifier le signe qui change la conduite et expliquer la limite de son interprétation.</em></p>')
    raw=raw.replace('Sources consultées le 31 octobre 2026.','Sources consultées le 31 octobre 2026 ; compléments relus le 1er novembre 2026.')
    raw=raw.replace('La revue européenne décrit','La revue d’Accogli et ses collègues décrit')
    raw=raw.replace('Accogli et coll. — Diagnostic Approach to Macrocephaly in Children, équipes européennes, 2022','Accogli et coll. — Diagnostic Approach to Macrocephaly in Children, équipes italiennes, portugaise et canadienne, 2022')
    for n in [1,6,7,11]:
        raw,c=re.subn(rf'(<li id="s{n}"[^>]*>.*?)(</li>)',lambda m:m.group(1)+' Passages pertinents relus le 01.11.2026.'+m.group(2),raw,count=1,flags=re.S);assert c==1
    # Corrections typographiques limitées aux nouveaux passages.
    raw=raw.replace('de2023','de 2023').replace('banalisé','banalisé')
    for tag in ['style','figure']:assert re.findall(rf'<{tag}\b.*?</{tag}>',old,re.S)==re.findall(rf'<{tag}\b.*?</{tag}>',raw,re.S)
    a=html.fromstring(old);b=html.fromstring(raw)
    assert a.xpath('//details[@class="quiz"]/summary/text()')==b.xpath('//details[@class="quiz"]/summary/text()')
    assert len(b.xpath('//section[h2[starts-with(@id,"dx2-p")]]'))==14
    p.write_text(raw)
    report={'fichier':FN,'sha256_avant':hashlib.sha256(old.encode()).hexdigest(),'sha256_apres_redaction':hashlib.sha256(raw.encode()).hexdigest(),'mapping':{str(k):ns for k,(_,ns) in D.items()},'questions':14,'reponses_enrichies':14,'fenetres_enrichies':14,'nouvelle_posologie':False}
    report['mapping']['14']=[1,6,7,11]
    (BASE/'CHANGEMENTS_DX2.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
