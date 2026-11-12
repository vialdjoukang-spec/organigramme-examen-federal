/* forme.js — menu latéral dynamique des cours (ordre de Vial du 10.11.2026). Seul script autorisé, externe et partagé.
   Surligne la partie en cours de lecture et fait suivre le menu. Sans ce script, le menu reste pleinement utilisable (CSS seul). */
(function () {
  var m = document.getElementById('brain-barre14');
  if (!m) return;
  /* Une seule entrée « Sources » : l'entrée numérotée vers un titre #fm-N s'efface devant l'entrée § (cours déjà publiés). */
  var src = [].slice.call(m.querySelectorAll('a[href^="#"]')).filter(function (a) {
    return /^\s*(sources?|bibliographie|références)(\s|$)/i.test(a.lastChild ? a.lastChild.textContent : '');
  });
  if (src.some(function (a) { return a.firstChild && a.firstChild.textContent === '§'; }))
    src.forEach(function (a) { if (/^#fm-\d+$/.test(a.getAttribute('href')) && a.firstChild.textContent !== '§') m.removeChild(a); });
  var liens = [].slice.call(m.querySelectorAll('a[href^="#"]'));
  var cibles = liens.map(function (a) {
    try { return document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1))); } catch (e) { return null; }
  });
  var actuel = -1, attente = 0;
  m.classList.add('fm-dyn');
  function suivre(a) {
    var r = a.getBoundingClientRect(), mr = m.getBoundingClientRect();
    if (m.scrollHeight > m.clientHeight + 2 && (r.top < mr.top + 48 || r.bottom > mr.bottom - 48))
      m.scrollTop += r.top - mr.top - mr.height / 2 + r.height / 2;
    if (m.scrollWidth > m.clientWidth + 2 && (r.left < mr.left + 24 || r.right > mr.right - 24))
      m.scrollLeft += r.left - mr.left - mr.width / 2 + r.width / 2;
  }
  function maj() {
    attente = 0;
    var seuil = Math.min(window.innerHeight * 0.3, 260), k = -1, meilleur = -Infinity;
    for (var i = 0; i < cibles.length; i++) {
      var c = cibles[i];
      if (!c) continue;
      var t = c.getBoundingClientRect().top;
      if (t <= seuil && t > meilleur) { meilleur = t; k = i; }
    }
    var doc = document.documentElement;
    if (window.innerHeight + window.scrollY >= doc.scrollHeight - 4) {
      for (var j = cibles.length - 1; j >= 0; j--) if (cibles[j]) { if (cibles[j].getBoundingClientRect().top < window.innerHeight) k = j; break; }
    }
    var p = doc.scrollHeight > window.innerHeight ? window.scrollY / (doc.scrollHeight - window.innerHeight) : 1;
    m.style.setProperty('--fm-prog', Math.max(0, Math.min(1, p)).toFixed(3));
    if (k === actuel) return;
    if (actuel >= 0) { liens[actuel].classList.remove('fm-actif'); liens[actuel].removeAttribute('aria-current'); }
    actuel = k;
    if (k >= 0) { liens[k].classList.add('fm-actif'); liens[k].setAttribute('aria-current', 'location'); suivre(liens[k]); }
  }
  window.addEventListener('scroll', function () { if (!attente) attente = requestAnimationFrame(maj); }, { passive: true });
  window.addEventListener('resize', maj);
  window.addEventListener('hashchange', maj);
  maj();
})();
/* L1 : fermer une fenêtre centrale (bouton « Fermer » ou Échap) ramène le lecteur à sa position de lecture. */
(function () {
  var ouverte = false;
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a');
    if (!a) return;
    if (a.classList.contains('ouvre') || /^#med-/.test(a.getAttribute('href') || '')) { ouverte = true; return; }
    if (a.classList.contains('fermer') || (a.classList.contains('fe') && a.closest('.mb'))) { e.preventDefault(); fermer(); }
  });
  function fermer() {
    if (ouverte) { ouverte = false; history.back(); return; }
    var y = window.scrollY;
    location.hash = '';
    window.scrollTo(0, y);
  }
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape' || !location.hash) return;
    var s = document.getElementById(location.hash.slice(1));
    if (s && (s.classList.contains('fenetre') || s.classList.contains('mb'))) { e.preventDefault(); fermer(); }
  });
})();
/* Sources : toute URL écrite en clair dans une entrée de bibliographie (li[id^="sb-"]) devient un lien cliquable (nouvel onglet). */
(function () {
  var re = /https?:\/\/[^\s<>"«»]+[^\s<>"«».,;:)\]]/g;
  [].slice.call(document.querySelectorAll('li[id^="sb-"]')).forEach(function (li) {
    var w = document.createTreeWalker(li, NodeFilter.SHOW_TEXT, null), n, t = [];
    while ((n = w.nextNode())) if (!(n.parentNode.closest && n.parentNode.closest('a')) && re.test(n.nodeValue)) t.push(n);
    t.forEach(function (n) {
      var s = n.nodeValue, f = document.createDocumentFragment(), i = 0, m;
      re.lastIndex = 0;
      while ((m = re.exec(s))) {
        f.appendChild(document.createTextNode(s.slice(i, m.index)));
        var a = document.createElement('a'); a.href = m[0]; a.textContent = m[0]; a.target = '_blank'; a.rel = 'noopener';
        f.appendChild(a); i = m.index + m[0].length;
      }
      f.appendChild(document.createTextNode(s.slice(i)));
      n.parentNode.replaceChild(f, n);
    });
  });
})();
