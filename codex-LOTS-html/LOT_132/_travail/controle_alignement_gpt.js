#!/usr/bin/env node
"use strict";
/**
 * Vérification reproductible de concordance source JSON ↔ HTML candidat (LOT132).
 * Contrôle structurel uniquement : pas audit médical indépendant, pas Chromium,
 * pas harnais V8 ni preuve de consultation des références.
 * Usage : node codex-LOTS-html/LOT_132/_travail/controle_alignement_gpt.js
 */
const fs = require("node:fs");
const path = require("node:path");
const D = __dirname;
const canon = JSON.parse(fs.readFileSync(path.join(D, "..", "LISTE_DX_CANONIQUE.json"), "utf8"));
function normaliser(s) {
  return s
    .replace(/<sup\b[^>]*>[\s\S]*?<\/sup>/g, "")
    .replace(/<abbr\b[^>]*>/g, "").replace(/<\/abbr>/g, "")
    .replace(/<[^>]+>/g, " ")
    .replace(/&nbsp;|&#160;/g, " ").replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">").replace(/&amp;/g, "&")
    .replace(/&#39;|&apos;/g, "'").replace(/&quot;/g, '"')
    .replace(/\s+/g, " ").trim();
}
function chemins(n) {
  return {
    json: path.join(D, "DX"+n+"_CONTENU.json"),
    html: path.join(D, "brouillons_gpt", "LOT_132_Phase_B_V0_DX."+n+".html")
  };
}
let totals = {lecons:0, controles:0, controles_reussis:0, paragraphes:0, questions:0, erreurs:0};
const rows = [];
for (let n=1;n<=10;n++) {
  const p=chemins(n);
  const j=JSON.parse(fs.readFileSync(p.json,"utf8"));
  const h=fs.readFileSync(p.html,"utf8");
  const plain=normaliser(h);
  const ids=[...h.matchAll(new RegExp('id="dx'+n+'-p([0-9]+)"','g'))].map(x=>+x[1]);
  const pars=j.sections.flatMap(x=>x.detail_html.match(/<p\b[^>]*>[\s\S]*?<\/p>/g)||[]);
  const check={
    titre_canonique: j.titre===canon.diagnostics[n-1].nom,
    sections_13: j.sections.map(s=>s.numero).join(",")===Array.from({length:13},(_,i)=>i+1).join(","),
    parties_html_14: ids.join(",")===Array.from({length:14},(_,i)=>i+1).join(","),
    quiz_json_14:j.quiz.length===14,
    quiz_html_14:(h.match(/<details class="quiz">/g)||[]).length===14,
    sources_contigues:j.sources.every((s,i)=>s.id===i+1),
    references_resolues:[...j.sections,...j.quiz].every(x=>x.refs.every(id=>j.sources.some(s=>s.id===id))),
    questions_uniques:new Set(j.quiz.map(q=>q.question)).size===14,
    paragraphes_restitues:pars.every(x=>plain.includes(normaliser(x))),
    questions_restituees:j.quiz.every(x=>plain.includes(normaliser(x.question))),
    reponses_restituees:j.quiz.every(x=>plain.includes(normaliser(x.reponse))),
    urls_sources:j.sources.every(s=>h.includes(s.url)||h.includes(s.url.replace(/&/g,"&amp;"))),
    mention_non_validation:h.includes("non validé cliniquement par un médecin"),
    marque_finale:h.trimEnd().endsWith("<!-- FIN_FICHIER LOT_132_Phase_B_DX."+n+" -->"),
    pas_script_ni_iframe:!/<script\b|<iframe\b/i.test(h)
  };
  const bad=Object.entries(check).filter(([,ok])=>!ok).map(([k])=>k);
  rows.push({lecon:"DX"+n,checks:check,echecs:bad,paragraphes:pars.length,questions:j.quiz.length});
  totals.lecons++;
  totals.controles+=Object.keys(check).length;
  totals.controles_reussis+=Object.keys(check).length-bad.length;
  totals.paragraphes+=pars.length;
  totals.questions+=j.quiz.length;
  totals.erreurs+=bad.length;
}
console.log(JSON.stringify({
  nature:"Contrôle mécanique d'alignement, non audit médical indépendant",
  ...totals,
  lecons:rows
},null,2));
if(totals.erreurs)process.exitCode=1;
