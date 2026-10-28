export const meta = { name: 'circuit-duo-professeur', description: 'Directive de Vial 28.10.2026 : 16 leçons → 16 duos médico-linguistes Sonnet 5.5 → 6 professeurs émérites Opus 5.5 moyen (2 leçons par appel, tourniquet)', phases: [{ title: 'Duo', detail: 'un agent Sonnet par leçon' }, { title: 'Professeur', detail: '6 Opus simultanés, 2 leçons chacun', model: 'opus' }] }
// Lancement : Workflow({scriptPath: 'harnais/brain/circuit_duo_professeur.js', args: {lecons: [<≤16 chemins absolus>]}})
// Liste prête : python3 harnais/brain/circuit_vial.py repartir <dossier|fichiers…> --json  (champ duos[].lecon)
const L = (args && args.lecons) || []
if (!L.length) throw new Error('args.lecons vide')
if (L.length > 16) log(`${L.length - 16} leçon(s) au-delà de 16 : reportées à la vague suivante`)
const lecons = L.slice(0, 16)
const C = 'python3 harnais/brain/circuit_vial.py'
const nom = (f) => f.split('/').pop().replace('.html', '')
// 1. Court-circuit duo : les 16 agents démarrent ensemble (plafond de concurrence du moteur : min(16, CPU-2)).
const duos = lecons.map((f, i) => agent(
  `Leçon ${i + 1}/16 : ${f}. Départ : ${C} memoire duo ${f}. Stylise tout le cours selon la directive et gère le fond des 14 parties ; point 10 : modèle JSON puis ${C} algo ${f} --appliquer ; fin : ${C} fin ${f} --role duo jusqu'à ACCEPTÉ. Une ligne de réponse.`,
  { label: 'duo ' + nom(f), phase: 'Duo', agentType: 'duo-medico-linguiste', model: 'sonnet' }))
// 2. Professeurs : paires (1-2, 3-4, …) ; 6 ouvriers Opus tirent la paire suivante dès qu'ils sont libres (tourniquet : 12 leçons puis 4).
const paires = []
for (let i = 0; i < lecons.length; i += 2) paires.push([i, i + 1].filter(j => j < lecons.length))
let prochaine = 0
const ouvrier = async (k) => {
  const out = []
  while (prochaine < paires.length) {
    const p = paires[prochaine++]
    const etats = await Promise.all(p.map(j => duos[j]))
    const fs = p.map(j => lecons[j])
    const r = await agent(
      `Professeur émérite Opus ${k + 1}. Deux leçons, l'une après l'autre : ${fs.join(' ; ')}. Retour des duos : ${etats.map(e => (e || 'ÉCHEC DU DUO').slice(0, 200)).join(' | ')}. Pour chaque fichier : ${C} memoire professeur <fichier> ; ${C} scanner <fichier> ; revue critique du fond et corrections ; ${C} fin <fichier> --role professeur jusqu'à ACCEPTÉ. Une ligne par fichier.`,
      { label: `opus ${k + 1} · ${fs.map(nom).join(' + ')}`, phase: 'Professeur', agentType: 'professeur-emerite', model: 'opus', effort: 'medium' })
    out.push({ opus: k + 1, lecons: fs, duos: etats, professeur: r })
  }
  return out
}
const res = (await Promise.all([0, 1, 2, 3, 4, 5].map(ouvrier))).flat()
return res
