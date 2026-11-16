from lib import *
P = Pt(10)
P.p("L'arbre ci-dessous écarte d'abord les urgences, puis oriente vers les causes fréquentes, et conclut au trouble panique seulement lorsque les critères sont réunis [wd8c882-37]. "
    "Chaque nœud correspond à un signe, à un examen ou à une action décrits dans les points précédents [wf778c1-37].")
P.raw("""<ul>
<li><div class="p">Si l'on constate une hypotension, une tachycardie ou une douleur constrictive à l'effort, alors on réalise un ECG et des biomarqueurs immédiats [wbd75ff-11][wd8c882-25].</div>
<ul>
<li><div class="p">Si l'ECG ou les biomarqueurs sont anormaux, alors on ouvre la filière du syndrome coronarien aigu avec prise en charge urgente [wfba9d7-1].</div></li>
<li><div class="p">Si la douleur est brutale ou déchirante, ou si la pression est basse, alors on calcule le score de risque et on demande une imagerie de l'aorte [wc15f7c-13].</div></li>
<li><div class="p">Si la douleur augmente à la respiration avec essoufflement, alors on évoque une péricardite, une embolie pulmonaire ou un pneumothorax [wfba9d7-2].</div></li>
</ul></li>
<li><div class="p">Si les constantes et l'ECG sont normaux, alors on recherche une cause non cardiaque fréquente [wf778c1-37].</div>
<ul>
<li><div class="p">Si la douleur est reproductible à la palpation, alors on retient un syndrome de la paroi thoracique [wd8c882-20].</div></li>
<li><div class="p">Si le patient décrit une brûlure, une régurgitation ou une dysphagie, alors on suspecte un reflux et on tente un inhibiteur de la pompe à protons [wf778c1-34][w1a9f59-37].</div></li>
<li><div class="p">Si les palpitations persistent malgré un ECG normal, alors on propose un monitorage ambulatoire [wf778c1-35].</div></li>
<li><div class="p">Si la TSH ou l'hémoglobine est anormale, alors on traite la cause secondaire [wfba9d7-9].</div></li>
</ul></li>
<li><div class="p">Si l'attaque dure 15 à 30 minutes avec peur de mourir et symptômes autonomes, alors on applique les critères du DSM-5 [w85c0ac-10][wf778c1-35][we22718-34].</div>
<ul>
<li><div class="p">Si une attaque est suivie d'un mois ou plus de crainte persistante ou d'évitement, alors on retient un trouble panique et on propose la psychoéducation, la thérapie cognitivo-comportementale ou un antidépresseur [we22718-33][we22718-65].</div></li>
<li><div class="p">Si l'attaque est isolée, alors on remet une information écrite et on assure le suivi en premier recours, sans hospitalisation [wb6b3cd-40].</div></li>
<li><div class="p">Si le patient évite les transports, les foules ou la solitude, alors on ajoute le diagnostic d'agoraphobie [we22718-37].</div></li>
<li><div class="p">Si le patient exprime des idées suicidaires, alors on organise une surveillance particulière et un avis spécialisé [aips-55391-21][we22718-72].</div></li>
</ul></li>
<li><div class="p">Si le traitement reste sans effet après au moins 12 semaines, alors on réévalue et on demande un avis spécialisé [we22718-62][we22718-72].</div></li>
</ul>""")

P.save()
