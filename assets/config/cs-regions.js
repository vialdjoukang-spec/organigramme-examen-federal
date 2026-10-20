/* GAMMA · CS : décore la ligne des régions (couleur, nom accessible, état sélectionné). Aucun contenu clinique. */
(function(){
  const AX={reg:'Région',sys:'Système',pop:'Population'};
  function deco(){
    const box=document.getElementById('g-reg');if(!box)return;
    box.setAttribute('role','group');box.setAttribute('aria-label','Régions de l’examen clinique, défilement horizontal');box.tabIndex=0;
    const bs=[...box.querySelectorAll('button[data-r]')],n=bs.length||1;let sel=null;
    bs.forEach((b,i)=>{
      if(!b.querySelector('.cs-l')){
        const ax=b.closest('[data-ax]')?.dataset.ax||'reg',t=b.textContent,m=t.match(/^(.*) · (\d+)\/(\d+)$/);
        const nom=m?m[1]:t;
        b.textContent='';
        const a=document.createElement('span');a.className='cs-ax';a.textContent=AX[ax]||'';
        const l=document.createElement('span');l.className='cs-l';l.textContent=nom;
        b.append(a,l);
        if(m){const c=document.createElement('span');c.className='cs-n';c.textContent=m[2]+'/'+m[3];const h=document.createElement('span');h.className='cs-sr';h.textContent=' gestes maîtrisés';c.append(h);b.append(c)}
        b.dataset.csNom=nom;b.dataset.csK=m?m[2]+' sur '+m[3]+' gestes maîtrisés':'';
      }
      b.type='button';b.style.setProperty('--h',Math.round(i*360/n*7)%360);
      const on=b.classList.contains('on');b.setAttribute('aria-pressed',on?'true':'false');
      b.removeAttribute('aria-label');
      if(on)sel=b;
    });
    if(sel&&box.scrollWidth>box.clientWidth){const l=sel.offsetLeft-box.offsetLeft,r=l+sel.offsetWidth;if(l<box.scrollLeft||r>box.scrollLeft+box.clientWidth)box.scrollLeft=Math.max(0,l-8)}
  }
  function init(){const box=document.getElementById('g-reg');if(!box)return;deco();new MutationObserver(deco).observe(box,{childList:true})}
  document.readyState==='loading'?document.addEventListener('DOMContentLoaded',init):init();
})();
