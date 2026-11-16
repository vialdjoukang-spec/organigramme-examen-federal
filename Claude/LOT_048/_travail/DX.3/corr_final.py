D='fragments/'
def c(i): return '<sup class="r"><a href="#sb-%s">%s</a></sup>'%(i,i)
def sub(f,a,b):
    t=open(D+f,encoding='utf-8').read()
    assert t.count(a)==1,(f,a[:60],t.count(a))
    open(D+f,'w',encoding='utf-8').write(t.replace(a,b))
sub('p10.html',"<li>Il faut évaluer la déglutition par vidéofluoroscopie ou par endoscopie de la déglutition"+c('w2aac93-11')+".</li>",
 "<li>Si le déficit est aigu, le dépistage de la déglutition est recommandé chez tout patient victime d'accident vasculaire cérébral, puis il bénéficie d'une vidéofluoroscopie ou d'une endoscopie de déglutition"+c('w0a1251-11')+c('w2aac93-11')+".</li>")
sub('p11.html',"L'usage dans l'OeE est donc hors indication, et ce cours n'enseigne aucune dose pour cet usage"+c('w79d85d-3')+".","L'usage des inhibiteurs de la pompe à protons dans l'OeE reste donc hors indication en Suisse, puisque l'information professionnelle ne mentionne que l'œsophagite de reflux"+c('w79d85d-3')+c('aips-55609-1')+".")
sub('p04.html',"Elles portent sur le retard au déclenchement de la déglutition, la régurgitation nasale et la toux pendant la déglutition"+c('w2aac93-126')+".","Elles portent sur le retard au déclenchement, la régurgitation nasale, la toux pendant la déglutition et le besoin de déglutitions répétées"+c('w2aac93-126')+".")
sub('p04.html',"Le patient du cours ressent une gêne rétrosternale à l'ingestion de solides, ce qui oriente vers l'œsophage","Une gêne rétrosternale à l'ingestion de solides oriente vers l'œsophage, alors qu'une gêne au déclenchement oriente vers l'oropharynx")
sub('p09.html'," Ce cours se limite donc à l'adulte jeune.","")
sub('p11.html',"Chez l'enfant, aucun produit déglutit de corticostéroïde n'est autorisé avant 11 ans, et des préparations magistrales sont utilisées","Chez l'enfant de moins de 11 ans, aucun corticostéroïde dégluti n'est autorisé, et des préparations magistrales sont donc utilisées")
