"""Asclépios · normalise TIP[*].c[5] (Examen physique ciblé) en format compact rendu par exFmt() :
  §<rid>  ouvre une région (ordre céphalo-caudal) ; ¶<ordre> ouvre une phase (1 I, 2 Pa, 3 Pe, 4 A, 5 Mob, 6 Tests, M Mesures, N Neuro, 0 sans phase)
  • texte  élément d'origine, verbatim ; @k1 k2  puces vers les gestes GES (clé stable k) ou r:<rid> (région).
Aucun fait clinique n'est ajouté : les éléments d'origine sont seulement répartis et ordonnés."""
import json,re,unicodedata,sys
T=json.load(open('data/TIP.json')); G=json.load(open('data/GES.json'))
nz=lambda s:unicodedata.normalize('NFD',s.lower().replace('œ','oe').replace('æ','ae')).encode('ascii','ignore').decode()
REG=[('constantes',r'constantes|temperature|pression arterielle|tension arterielle|frequence (cardiaque|respiratoire)|saturation|spo2|poids|imc|etat general|signes vitaux|glycemie|etat de choc|signes de choc|hemodynami|orthostat|corpulence|anthropometr|perte de poids|deshydrat|volemie'),
('meninge-gcs',r'mening|raideur de nuque|kernig|brudzinski|glasgow'),
('ganglions',r'ganglion|adenopath|aires gangl'),
('seins',r'\bsein|mammaire|mamelon|aisselle'),
('tr-genital',r'bourses|toucher rectal|rectal|marge anale|\banus|canal anal|sphincter anal|prostat|testic|scrot|penis|vagin|vulv|speculum|gyneco|uter|annex|hernie|orifice inguinal|genit|perine|cervix|col de l.uterus'),
('vasc',r'index de pression|pouls|oedem|varic|arteri|veineu|\bips\b|mollet|thrombose|tvp|aorte|carotid|claudication|ischemi|godet|recoloration'),
('thorax',r'poumon|pulmon|crepit|\bsibil|murmure|plevr|souffle tubaire|ampliation|tirage|thorax|thorac|respirat|ronchi|stridor|wheezing|egophon|hippocratisme'),
('coeur-vaisseaux',r'coeur|cardi|souffle|galop|\bb3\b|\bb4\b|jugul|pericard|choc de pointe|rythme|precord'),
('abdomen',r'parenchyme renal|\brein|lombaire|abdom|foie|hepat|splen|\brate\b|ascite|murphy|mcburney|defense|epigastr|fosse iliaque|meteor|bruits hydro|loge renale|fosses? lombaire|giordano|vessie|globe|hypochondre|peristalt|matite'),
('rachis',r'rachis|lombaire|epineuse|lasegue|schober|sacro|scoliose|cyphose|vertebr|queue de cheval'),
('membres',r'epaule|coude|poignet|\bmains?\b|doigt|hanche|genou|cheville|\bpieds?\b|articul|synov|arthr|tendon|menisq|membres?|ottawa|orteil|muscle|amyotroph|deformation'),
('tete-cou',r'\btete|\bcou\b|thyro|goitre|\borl|otoscop|tympan|oreille|\bnez\b|sinus|gorge|pharyn|amygdal|\boeil|\byeux|conjonctiv|fond d|bouche|buccal|langue|dent|\bface|facies|parotid|larynx|\bvoix|exophtalm|rhinoscop|kiesselbach|epistaxis|retin|papille|vitre|oculaire|acuite|champ visuel|cordes vocales|laryng|polype|\bmeat|tympan|cornee|paupiere|cervical'),
('peau',r'epiderm|derm|peau|cutan|tegument|muqueuse|purpura|ictere|paleur|eruption|lesion|ongle|phaner|cheveu|erythem|prurit|xerose|cyanose|escarre|naevus|plaie|ecchymose|hematome|vesicule|papule|macule|pigment'),
('neuro',r'neuro|reflex|force (musculaire|segmentaire)|testing moteur|sensibilite (thermo|tactile|vibratoire|proprio|algique|superficielle|profonde)|deficit sensitif|nerfs? crani|pupill|babinski|romberg|coordination|marche|tonus|deficit|motricit|nystagm|vigilance|parole|langage|tremblement|cognit|mmse|moca|dermatome|paresthes|conscience|confusion|asterixis|dysarthr|orientation|ataxie|fasciculation|paralys|vertige'),
('psychiatrie',r'humeur|psych|suicid|thymi|anxi|delire|halluc|comportement|status mental|affect|idees'),
('pediatrie',r'perimetre cranien|fontanelle|croissance|percentile|nourrisson|\benfant|developpement|nouveau-ne'),
('geriatrie',r'chute|fragilite|timed up|autonomie|equilibre')]
REG=[(k,re.compile(v)) for k,v in REG]
LAB={'membres':'Membres et articulations','neuro':'Neurologique','autres':'Autres éléments ciblés'}
ORDER=['constantes','peau','tete-cou','ganglions','thorax','coeur-vaisseaux','vasc','seins','abdomen','tr-genital','rachis','membres','neuro','meninge-gcs','psychiatrie','pediatrie','geriatrie','autres']
PH=[('M',r'pression arterielle|frequence|temperature|saturation|poids|\bimc|glycemie|tour de taille|\bips\b|mesur|chiffr'),
('1',r'inspect|observ|aspect|morpholog|facies|coloration|paleur|ictere|cyanose|eruption|marbrure|deformation|tumefaction|asymetri|attitude|posture'),
('2',r'palp|toucher|sensible a la pression|douleur provoquee|defense|masse|consistance|thrill|fremissement|pouls|godet|recoloration|hepatomegal|splenomegal|empatement'),
('3',r'percu|matite|tympanisme|ebranlement|giordano|sonorite'),
('4',r'auscult|souffle|crepit|\bsibil|murmure|bruits|galop|frottement|stridor|ronchi'),
('5',r'mobilit|amplitude|mobilisation'),
('6',r'\btests?\b|signe de|signe du|manoeuvre|\bscore|epreuve|lasegue|murphy|kernig|romberg|babinski|ottawa|schober'),
('N',r'reflex|force|sensibilit|nerfs? crani|pupill|coordination|deficit|glasgow|tonus|motricit')]
PH=[(k,re.compile(v)) for k,v in PH]
SEQ={'abdomen':['0','M','1','4','3','2','5','6','N']}
DEF=['0','M','1','2','3','4','5','6','N']
def regof(t,hint):
  x=nz(re.sub('<[^>]+>','',t));best=None
  for k,rx in REG:
    m=rx.search(x)
    if m and (best is None or m.start()<best[0]):best=(m.start(),k)
  return best[1] if best else (hint or 'autres')
def phof(t):
  x=nz(re.sub('<[^>]+>','',t));best=None
  for k,rx in PH:
    m=rx.search(x)
    if m and (best is None or m.start()<best[0]):best=(m.start(),k)
  return best[1] if best else '0'
# gestes : clé distinctive par titre
KEYS=[]
for r in G:
  for it in r['items']:
    s=nz(re.sub(r'\(.*?\)','',it['s'])).strip()
    m=re.match(r"(?:test|signe|manoeuvre|epreuve|regles?)\s+(?:de la |de l'|du |des |de |d')?(.+)",s)
    key=(m.group(1) if m else s).strip()
    orig=re.sub(r'\(.*?\)','',it['s']).strip()
    epon=bool(m) and any(w[:1].isupper() for w in orig.split()[1:])
    if len(key)>=5 and (epon or (len(key.split())>=2 and len(key)>=10)): KEYS.append((re.compile(r'\b'+re.escape(key)+r'\b'),it['k'],r['id']))
RMAP={'membres':None,'neuro':'neuro-moteur','autres':None}
def chips(rk,txt):
  x=nz(re.sub('<[^>]+>','',txt));out=[]
  for rx,k,rid in KEYS:
    if rx.search(x) and k not in out: out.append(k)
  rid=RMAP.get(rk,rk)
  return ([f'r:{rid}'] if rid else [])+out[:4]
def split(s):
  s=s.strip()
  if '\n' in s or '<br>' in s:
    hint=None;lead=None;el=[]
    for ln in re.split(r'\n|<br\s*/?>',s):
      ln=ln.strip()
      m=re.fullmatch(r'<b>([^<]{2,70})</b>\s*:?',ln)
      if m:
        hint=regof(m.group(1),None);lead=None if hint!='autres' else m.group(1)
        if hint=='autres':hint=None
        continue
      ln=re.sub(r'^[•\-]\s*','',ln)
      if ln: el.append(((f'<i>{lead}</i> · ' if lead else '')+ln,hint))
    return el
  return [(p.strip(),None) for p in re.split(r'\s+·\s+',s) if p.strip()]
EMPTY={'G3':'r:constantes r:peau','G4':'r:constantes ganglions_n1','G14':'r:constantes r:meninge-gcs','S8.1':'r:abdomen r:constantes','S8.2':'r:peau r:constantes','S8.3':'r:peau r:vasc','S8.4':'epaule_n1 genou_n1 r:vasc','S8.5':'r:constantes r:thorax','S8.6':'r:tete-cou r:thorax','S8.7':'r:meninge-gcs r:neuro-nc','S8.8':'r:vasc genou_n1 epaule_n1','S8.9':'r:peau r:vasc','S8.10':'r:rachis rachis_13','S8.11':'r:thorax r:constantes','S8.12':'r:vasc r:constantes'}
LAISSES=[]
stats=dict(ssp=0,elements=0,regions=0,chips=0,vides=0,autres=0)
for sid,v in T.items():
  c=v['c']
  if len(c)<6: continue
  if c[5].startswith('§') or c[5].startswith('À compléter'): sys.exit('TIP déjà normalisé')
  if not re.sub('<[^>]+>','',c[5]).strip():
    c[5]='À compléter : aucune source vérifiée n’est encore rattachée à l’examen physique ciblé de cette SSP. Les gestes liés ci-dessous restent valables.\n@'+EMPTY[sid];stats['vides']+=1;continue
  els=split(c[5]);by={}
  cls=[regof(t,None) for t,_ in els]
  if sum(k!='autres' for k in cls)<0.25*len(cls):
    stats['laisses']=stats.get('laisses',0)+1;LAISSES.append(sid);continue
  for t,h in els:
    rk=h if h and h!='autres' else regof(t,None)
    if 'ganglion' in nz(t) or 'adenopath' in nz(t): rk=h or 'ganglions'
    by.setdefault(rk,[]).append((phof(t),t))
  out=[]
  for rk in ORDER:
    if rk not in by:continue
    seq=SEQ.get(rk,DEF);L=sorted(by[rk],key=lambda e:seq.index(e[0]))
    out.append('§'+rk);cur=None
    for ph,t in L:
      if ph!=cur: out.append('¶'+ph);cur=ph
      out.append('• '+t)
    ch=chips(rk,' '.join(t for _,t in L));out.append('@'+' '.join(ch)) if ch else None
    stats['regions']+=1;stats['chips']+=len(ch);stats['autres']+=rk=='autres'
  stats['ssp']+=1;stats['elements']+=len(els)
  c[5]='\n'.join(out)
json.dump(T,open('data/TIP.json','w'),ensure_ascii=False,separators=(',',':'))
print(stats);json.dump(LAISSES,open('/workspace/ssp/audit_examen/tip_laisses.json','w'))
