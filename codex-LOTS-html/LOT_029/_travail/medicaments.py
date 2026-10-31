import gzip
from html import escape
from format_lecon import R,paras
def valganciclovir(l):
 t=gzip.open(R/'ressources_ia/aips/fi_fr/65221.txt.gz','rt').read()
 text=paras('Valganciclovir Sandoz, comprimés pelliculés, information professionnelle suisse n° 65221 consultée. Cette présentation et ses indications ne fournissent pas un schéma de traitement du nouveau-né atteint de CMV congénital. L’usage décrit dans les recommandations pédiatriques relève donc d’une prescription hors information professionnelle, à discuter avec infectiologue pédiatrique et pharmacie.', 'Aucune dose adulte de rétinite ou de prophylaxie après transplantation ne doit être transposée au nourrisson. Le choix de la formulation, de la dose selon le poids et la fonction rénale, de sa réévaluation et du calendrier de surveillance doit être validé dans le protocole spécialisé. Posologie néonatale AIPS : non trouvée dans cette notice ; à vérifier avec l’équipe avant prescription.')
 quotes=[
 "La tolérance et l'efficacité n'ont pas été démontrées chez les patients pédiatriques. L'administration de Valganciclovir Sandoz chez les patients pédiatriques n'est pas recommandée, étant donné que les propriétés pharmacocinétiques du valganciclovir n'ont pas été étudiées chez cette population de patients (voir «Mises en garde et précautions»).",
 'Les comprimés pelliculés ne doivent être ni cassés ni écrasés.',
 "Valganciclovir Sandoz est contre-indiqué chez les patients présentant une hypersensibilité connue au valganciclovir, au ganciclovir ou à l'un des excipients conformément à la composition.",
 'Leucopénie, neutropénie, anémie, thrombopénie, pancytopénie, insuffisance médullaire et anémie aplasique sévères ont été observées chez des patients traités par le valganciclovir (et par le ganciclovir).',
 "Valganciclovir Sandoz ne doit pas être utilisé durant la grossesse (voir «Contre-ind ications»)."
 ]
 # L’extrait conserve les espaces internes de la transcription AIPS locale.
 quotes.append(next(x for x in t.splitlines() if x.startswith('Valganci clovir Sandoz est contre-indiqué pendant la grossesse')))
 for q in quotes:
  assert q in t,q
  text+='<blockquote><p>« '+escape(q)+' »</p></blockquote>'
 text+=paras('Ces mentions sont reproduites pour délimiter l’information professionnelle, et non pour proposer ce comprimé au nouveau-né. La restriction d’allaitement concerne l’administration du médicament à la personne qui allaite ; elle ne constitue pas à elle seule une interdiction d’allaiter un enfant traité.', 'Surveiller notamment numération sanguine, fonction hépatique et fonction rénale selon le protocole pédiatrique. Une cytopénie ou une toxicité peut imposer adaptation ou interruption par l’équipe. Vérifier les interactions avec médicaments myélosuppresseurs ou néphrotoxiques ; les bénéfices attendus et risques sont expliqués aux parents.')
 return l.subwindow('valganciclovir','Valganciclovir : limites AIPS et surveillance',text,(3,20,25))
