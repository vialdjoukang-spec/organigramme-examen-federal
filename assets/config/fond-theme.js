/* Choix de fonds de lecture : réglage local, sans modifier le contenu. */
(()=>{'use strict';
const key='orga-theme-fond',root=document.documentElement,host=document.getElementById('fond-theme');
if(!host)return;
const colors=[['ciel','Bleu ciel','#eaf7fd'],['vanille','Jaune vanille','#fff9df'],['peche','Pêche','#fff0e8'],['rose','Rose poudré','#fceef3'],['lavande','Lavande','#f2effc'],['lilas','Lilas','#f7edfc'],['menthe','Menthe','#ecf8f1'],['sauge','Vert sauge','#f0f6e9'],['turquoise','Turquoise pâle','#eaf8f8'],['perle','Gris perle','#f1f4f7']];
const trigger=document.createElement('button');trigger.type='button';trigger.className='b';trigger.textContent='Thème de fond';trigger.setAttribute('aria-expanded','false');trigger.setAttribute('aria-controls','fond-palette');
const menu=document.createElement('fieldset');menu.id='fond-palette';menu.hidden=true;
const legend=document.createElement('legend');legend.textContent='Choisir une couleur de fond';menu.append(legend);
const grid=document.createElement('div');grid.className='fond-options';menu.append(grid);
const status=document.createElement('p');status.className='st';status.setAttribute('role','status');menu.append(status);
host.append(trigger,menu);
function paint(id,persist){const item=colors.find(c=>c[0]===id);if(!item)return false;
root.dataset.readingTheme=id;root.style.setProperty('--chosen-reading-bg',item[2]);root.style.setProperty('--bg',item[2]);
for(const button of grid.children)button.setAttribute('aria-pressed',String(button.dataset.fond===id));
let saved=true;if(persist){try{const value=JSON.stringify({couleur:id});saved=typeof lsSet==='function'?lsSet(key,value):(localStorage.setItem(key,value),true)}catch(_){saved=false}}
status.textContent=item[1]+(persist?(saved?' · choix mémorisé.':' · appliqué pour cette session.'):'');return true;}
for(const [id,name,color] of colors){const b=document.createElement('button');b.type='button';b.className='fond-choice';b.dataset.fond=id;b.style.setProperty('--swatch',color);b.setAttribute('aria-pressed','false');b.textContent=name;b.addEventListener('click',()=>paint(id,true));grid.append(b)}
function opened(value,focus){menu.hidden=!value;trigger.setAttribute('aria-expanded',String(value));if(value&&focus)(grid.querySelector('[aria-pressed="true"]')||grid.firstElementChild).focus();}
trigger.addEventListener('click',()=>opened(menu.hidden,true));
host.addEventListener('keydown',event=>{if(event.key==='Escape'&&!menu.hidden){event.preventDefault();event.stopPropagation();opened(false);trigger.focus()}});
document.addEventListener('pointerdown',event=>{if(!host.contains(event.target))opened(false)});
grid.addEventListener('keydown',event=>{if(!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','Home','End'].includes(event.key))return;const buttons=[...grid.children],i=buttons.indexOf(document.activeElement);if(i<0)return;event.preventDefault();let n=event.key==='Home'?0:event.key==='End'?buttons.length-1:(i+(['ArrowLeft','ArrowUp'].includes(event.key)?buttons.length-1:1))%buttons.length;buttons[n].focus()});
let stored=null;try{const value=JSON.parse(localStorage.getItem(key)||'null');stored=value&&value.couleur}catch(_){}
if(!paint(stored,false)){const light=matchMedia('(prefers-color-scheme:light)').matches||root.dataset.theme==='light';if(light){grid.firstElementChild.setAttribute('aria-pressed','true');status.textContent='Bleu ciel · fond par défaut.'}else status.textContent='Fond sombre du système.'}
})();
