export const meta = { name: 'circuit-duo-professeur', description: 'Directive de Vial 28.10.2026 : 16 leçons → 16 duos médico-linguistes Sonnet 5.5 → 12 professeurs émérites Opus 5.5 moyen (1 leçon par appel, tourniquet) → porte de sortie du lot (boucle bornée)', phases: [{ title: 'Duo', detail: 'un agent Sonnet par leçon' }, { title: 'Professeur', detail: '12 Opus, une leçon chacun ; les 4 dernières au tourniquet', model: 'opus' }, { title: 'Sortie', detail: 'audit_sortie du lot ; non conformes renvoyés au duo (boucle bornée)' }] }
// Lancement : Workflow({scriptPath: 'harnais/brain/circuit_duo_professeur.js', args: {lecons: [<≤16 chemins absolus>], dossier?: '<dossier du LOT>', boucles?: 2, paquet?: N, tranche?: [debut, fin]}})
// Liste prête : python3 harnais/brain/circuit_vial.py repartir <dossier> --phase-b --exclure-traites --json  (champ duos[].lecon)
// NÉO-CONCEPTION 28.10.2026 : préférer `python3 harnais/brain/lancer_circuit.py <leçons…>` (sous-agents réels claude -p, 16 Sonnet / 12 Opus, porte
// unique rejouée par le script, reprise bornée). Ce workflow reste utilisable ; ses agents suivent la même méthode point par point (définitions .claude/agents).
// Concurrence : le moteur plafonne chaque Workflow à min(16, CPU-2) agents simultanés (2 sur une machine à 4 CPU) ; les appels en trop
// attendent en file. Pour plus de parallélisme : lancer plusieurs Workflow avec `tranche` (ex. [0,4], [4,8], [8,12], [12,16]) — chaque run a son
// propre plafond ; les numéros de leçon et les prompts des duos restent identiques (reprise en cache valide). `paquet` limite les duos simultanés.
const L = (args && args.lecons) || []
if (!L.length) throw new Error('args.lecons vide')
if (L.length > 16) log(`${L.length - 16} leçon(s) au-delà de 16 : reportées à la vague suivante`)
const lecons = L.slice(0, 16)
const C = 'python3 harnais/brain/circuit_vial.py'
const nom = (f) => f.split('/').pop().replace('.html', '')
const [T0, T1] = (args && args.tranche) || [0, lecons.length]
const idx = lecons.map((_, i) => i).filter(i => i >= T0 && i < T1)
if (idx.length < lecons.length) log(`tranche ${T0}–${T1} : ${idx.length} leçon(s) dans ce run`)
// 1. Court-circuit duo (texte des prompts INCHANGÉ : la reprise en cache de wf_3cd7bff3-1e7 reste valide).
const PAQ = (args && args.paquet) || 0
const duos = {}
for (const i of idx) {
  const f = lecons[i]
  const avant = PAQ && idx.indexOf(i) >= PAQ ? duos[idx[idx.indexOf(i) - PAQ]] : null
  duos[i] = (avant ? avant.then(() => null, () => null) : Promise.resolve()).then(() => agent(
    `Leçon ${i + 1}/16 : ${f}. Départ : ${C} memoire duo ${f}. Stylise tout le cours selon la directive et gère le fond des 14 parties ; point 10 : modèle JSON puis ${C} algo ${f} --appliquer ; fin : ${C} fin ${f} --role duo jusqu'à ACCEPTÉ. Une ligne de réponse.`,
    { label: 'duo ' + nom(f), phase: 'Duo', agentType: 'duo-medico-linguiste', model: 'sonnet' }))
}
// 2. Professeurs : 12 ouvriers Opus, une leçon par appel ; chacun tire la leçon suivante dès qu'il est libre (12 leçons, puis 4 au tourniquet).
const NOPUS = 12
let prochaine = 0
const ouvrier = async (k) => {
  const out = []
  while (prochaine < idx.length) {
    const j = idx[prochaine++]
    const etat = await duos[j]
    const f = lecons[j]
    const r = await agent(
      `Professeur émérite Opus ${k + 1}/12. Une seule leçon : ${f}. Retour du duo : ${(etat || 'ÉCHEC DU DUO').slice(0, 300)}. ${C} memoire professeur ${f} ; ${C} scanner ${f} ; revue critique du fond, point par point, et corrections ; ${C} fin ${f} --role professeur jusqu'à ACCEPTÉ. Une ligne de réponse.`,
      { label: `opus ${k + 1} · ${nom(f)}`, phase: 'Professeur', agentType: 'professeur-emerite', model: 'opus', effort: 'medium' })
    out.push({ opus: k + 1, lecon: f, duo: etat, professeur: r })
  }
  return out
}
const res = (await Promise.all(Array.from({ length: NOPUS }, (_, k) => ouvrier(k)))).flat()
// 3. Porte de sortie du lot (le hook pre-commit exige audit_sortie : controle_lot CONFORME + audit médical et langue ≥ 90 %, 0 critique).
//    Les non conformes repartent au duo, boucle bornée ; jamais de commit ici.
const dossier = (args && args.dossier) || lecons[0].split('/').slice(0, -1).join('/')
const SORTIE = { type: 'object', properties: { conforme: { type: 'boolean' }, non_conformes: { type: 'array', items: { type: 'object', properties: { fichier: { type: 'string' }, motifs: { type: 'string' } }, required: ['fichier', 'motifs'] } }, resume: { type: 'string' } }, required: ['conforme', 'non_conformes', 'resume'] }
const BOUCLES = (args && args.boucles) || 2
const sortie = []
// Une seule porte par lot : par défaut sautée dans un run à `tranche` (plusieurs runs parallèles) ; la lancer dans le dernier run (args.sortie: true).
const FAIRE_SORTIE = args && args.sortie !== undefined ? args.sortie : !(args && args.tranche)
if (!FAIRE_SORTIE) log('porte de sortie sautée (tranche) : la lancer une fois pour le lot (args.sortie: true ou circuit_vial.py sortie)')
for (let b = 0; FAIRE_SORTIE && b <= BOUCLES; b++) {
  const s = await agent(`Lance exactement : ${C} sortie ${dossier} --json ; recopie son JSON (conforme, non_conformes[{fichier, motifs}], resume) sans rien modifier ni corriger.`,
    { label: `sortie ${b + 1}`, phase: 'Sortie', schema: SORTIE, model: 'sonnet', effort: 'low' })
  sortie.push(s)
  if (!s || s.conforme || !s.non_conformes.length) break
  if (b === BOUCLES) { log(`lot NON CONFORME après ${BOUCLES} boucle(s) : ${s.non_conformes.map(x => x.fichier).join(', ')} → attente-vial ou vague suivante`); break }
  await Promise.all(s.non_conformes.map(x => agent(
    `Reprise de sortie (boucle ${b + 1}/${BOUCLES}) : ${dossier}/${x.fichier}. Motifs : ${x.motifs.slice(0, 600)}. Départ : ${C} reprise ${dossier}/${x.fichier} (rapports MED_/CONF_ et doléances) ; corrige chaque écart (skills controle-langue et controle-medical) sans rien retrancher ; fin : ${C} fin ${dossier}/${x.fichier} --role duo jusqu'à ACCEPTÉ. Une ligne de réponse.`,
    { label: `reprise ${b + 1} · ${x.fichier.replace('.html', '')}`, phase: 'Sortie', agentType: 'duo-medico-linguiste', model: 'sonnet' })))
}
return { lecons: res, sortie }
