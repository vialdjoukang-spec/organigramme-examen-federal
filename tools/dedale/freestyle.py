"""Dédale-3D · rendu au crayon des vues d'un nerf crânien à partir du modèle Z-Anatomy.

INSTRUCTIONS (automate, zéro jeton) ------------------------------------------------
Commande, depuis le dossier du modèle (jamais versionné, hors dépôt) :
    blender -b /workspace/ssp/nc_src/Z-Anatomy/Startup.blend -P tools/dedale/freestyle.py -- nc07
    blender -b …/Startup.blend -P tools/dedale/freestyle.py -- nc07 --tour --sortie /workspace/ssp/nc_src/render
Entrées  : tools/dedale/nerfs.json (noms d'objets du modèle ; aucune coordonnée saisie à la main).
Sorties  : <sortie>/<nerf>-<vue>.svg (groupes peau, crane, tronc, territoires, nerf) et
           <sortie>/<nerf>-<vue>.json (ancres projetées : centre de chaque objet nommé, en px).
           Par défaut <sortie> = nc/trait/ du dépôt (vues face, profil, 34) ; --tour ajoute t0…t7.
Méthode  : 1. la peau (régions de la tête, de la face et du cou) est fusionnée en un seul maillage
              (sommets confondus à 2 mm près, normales recalculées) ; le tronc cérébral
              (deux moitiés, trois étages) est fusionné de même à 0,5 mm pour ne garder que le contour, sans les coutures des régions ;
           2. chaque groupe est rendu SEUL par Freestyle (silhouettes visibles), ce qui donne l'effet
              « crâne en transparence » : aucun groupe n'en masque un autre ;
           3. le nerf (courbes de Bézier du modèle) est échantillonné et projeté par la caméra ;
           4. caméras orthographiques : face 0°, profil droit 90°, trois quarts 45° avec 15° de plongée ;
              tour : 8 vues tous les 45° (plongée 15°) ; échelle et centre identiques pour toutes les vues ;
           5. post-traitement déterministe : arrondi au dixième de pixel, simplification de Douglas-Peucker
              (0,35 px), découpe au cadre ; deux exécutions donnent le même fichier à l'octet près.
Interdits: aucun trait dessiné à la main ; aucun fichier du modèle copié dans le dépôt.
Licence  : les vues dérivées sont sous CC BY-SA 4.0 (Z-Anatomy, d'après BodyParts3D CC BY-SA 2.1 JP).
"""
import bpy, addon_utils, bmesh, json, math, os, re, sys, tempfile
from mathutils import Vector, geometry
from bpy_extras.object_utils import world_to_camera_view

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
NERF = argv[0] if argv else 'nc07'
TOUR = '--tour' in argv
VUES = argv[argv.index('--vues') + 1].split(',') if '--vues' in argv else None
SORTIE = argv[argv.index('--sortie') + 1] if '--sortie' in argv else os.path.join(ROOT, 'nc', 'trait')
CFG = json.load(open(os.path.join(HERE, 'nerfs.json'), encoding='utf-8'))
C, N = CFG['commun'], CFG['nerfs'][NERF]
W = C['resolution']
O = bpy.data.objects
sc = bpy.context.scene
addon_utils.enable('render_freestyle_svg', default_set=True)


def coll_meshes(names, side=None):
    out = []
    for cn in names:
        for o in bpy.data.collections[cn].all_objects:
            if o.type == 'MESH' and not re.search(r'\.[a-z]$', o.name.replace('.r', '').replace('.l', '')) \
                    and not o.name.endswith('.j') and (side is None or o.name.endswith('.' + side)):
                out.append(o)
    return sorted(set(out), key=lambda o: o.name)


def fuse(objs, name, dist=0.001):
    """Fusionne des maillages (coordonnées du monde) et confond les sommets (1 mm par défaut)."""
    bm = bmesh.new()
    dg = bpy.context.evaluated_depsgraph_get()
    for o in objs:
        me = o.evaluated_get(dg).to_mesh()
        tmp = bmesh.new(); tmp.from_mesh(me); tmp.transform(o.matrix_world)
        m2 = bpy.data.meshes.new('t'); tmp.to_mesh(m2); tmp.free(); bm.from_mesh(m2); bpy.data.meshes.remove(m2)
        o.evaluated_get(dg).to_mesh_clear()
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=dist)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); sc.collection.objects.link(ob)
    return ob


def centre(o):
    dg = bpy.context.evaluated_depsgraph_get()
    if o.type == 'MESH':
        me = o.evaluated_get(dg).to_mesh()
        v = sum((o.matrix_world @ p.co for p in me.vertices), Vector()) / max(1, len(me.vertices))
        o.evaluated_get(dg).to_mesh_clear(); return v
    pts = [o.matrix_world @ Vector(p.co[:3]) for s in o.data.splines
           for p in (s.bezier_points if s.type == 'BEZIER' else s.points)]
    return sum(pts, Vector()) / len(pts)


def courbe_pts(o, res=16):
    mw, out = o.matrix_world, []
    for s in o.data.splines:
        if s.type == 'BEZIER':
            bp, pts = s.bezier_points, []
            for a, b in zip(bp[:-1], bp[1:]):
                seg = geometry.interpolate_bezier(mw @ a.co, mw @ a.handle_right, mw @ b.handle_left, mw @ b.co, res)
                pts.extend(seg if not pts else seg[1:])
        else:
            pts = [mw @ Vector(p.co[:3]) for p in s.points]
        out.append(pts)
    return out


def rdp(pts, eps):
    if len(pts) < 3:
        return pts
    a, b = Vector((*pts[0], 0)), Vector((*pts[-1], 0))
    ab = (b - a); L = ab.length
    dmax, idx = -1, 0
    for i in range(1, len(pts) - 1):
        p = Vector((*pts[i], 0))
        d = (p - a).length if L == 0 else ab.cross(p - a).length / L
        if d > dmax:
            dmax, idx = d, i
    if dmax > eps:
        return rdp(pts[:idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    return [pts[0], pts[-1]]


def clip(pts):
    out, cur = [], []
    for x, y in pts:
        if -2 <= x <= W + 2 and -2 <= y <= W + 2:
            cur.append((x, y))
        elif cur:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out


def d_path(pl):
    """Chemin relatif au dixième de pixel, calculé sur les valeurs arrondies (pas de dérive)."""
    q = [(round(x * 10), round(y * 10)) for x, y in pl]
    q = [p for i, p in enumerate(q) if i == 0 or p != q[i - 1]]
    if len(q) < 2:
        return ''
    f = lambda v: ('-' if v < 0 else '') + (str(abs(v) // 10) + ('.' + str(abs(v) % 10) if abs(v) % 10 else ''))
    s = 'M' + f(q[0][0]) + ' ' + f(q[0][1])
    for (x0, y0), (x1, y1) in zip(q[:-1], q[1:]):
        dx, dy = f(x1 - x0), f(y1 - y0)
        s += 'l' + dx + ('' if dy.startswith('-') else ' ') + dy
    return s


def lignes(pl_list, minlen=2.0):
    out = []
    for pl in pl_list:
        for c in clip(pl):
            c = rdp(c, 0.35)
            if sum((Vector(b) - Vector(a)).length for a, b in zip(c[:-1], c[1:])) >= minlen:
                d = d_path(c)
                if d:
                    out.append(d)
    return out


# ---------- préparation de la scène ----------
# On ne garde que les objets utiles (le modèle complet dépasse 11 Go une fois évalué) ; chaque objet
# conservé est détaché de son parent sans changer sa position dans le monde.
_util = set(o.name for o in coll_meshes(C['peau_collections'])) | set(C['crane_objets']) | set(C['tronc_objets'])
_util |= set(N['courbes']) | set(N['ancres'])
_util |= {o.name for o in bpy.data.collections[N['territoires_collection']].all_objects
          if o.type == 'MESH' and o.name.endswith('.' + N['cote'])}
_mw = {n: O[n].matrix_world.copy() for n in _util}
for n in sorted(_util):
    o = O[n]
    o.constraints.clear()
    o.parent = None
    o.matrix_world = _mw[n]
bpy.data.batch_remove([o for o in O if o.name not in _util])
bpy.context.view_layer.update()
peau = fuse(coll_meshes(C['peau_collections']), 'DD_peau', 0.002)
crane = [O[n] for n in C['crane_objets']]
tronc = [fuse([O[n] for n in C['tronc_objets']], 'DD_tronc', 0.0005)]
terr = [o for o in bpy.data.collections[N['territoires_collection']].all_objects
        if o.type == 'MESH' and o.name.endswith('.' + N['cote'])
        and not any(x in o.name for x in N.get('territoires_exclure', []))]
terr = sorted(terr, key=lambda o: o.name)
# Territoires : un passage par muscle, contour extérieur seul (les muscles minces vus par la tranche
# produiraient sinon des hachures parasites).
PASSES = [('territoires', [[o] for o in terr], 'ext'), ('crane', [crane], 'crease'), ('tronc', [tronc], 'sil'),
          ('peau', [[peau]], 'sil')]

cad = coll_meshes(C['cadre_collections'])
bb = [o.matrix_world @ Vector(c) for o in cad for c in o.bound_box]
mn = Vector((min(p.x for p in bb), min(p.y for p in bb), min(p.z for p in bb)))
mx = Vector((max(p.x for p in bb), max(p.y for p in bb), max(p.z for p in bb)))
CEN = (mn + mx) / 2
ext = mx - mn
SCALE = C['marge'] * max(ext.z, math.hypot(ext.x, ext.y))
print('DEDALE cadre', tuple(round(v, 4) for v in mn), tuple(round(v, 4) for v in mx), round(SCALE, 4))

for c in bpy.data.collections:
    c.hide_render = False
for lc in sc.view_layers[0].layer_collection.children:
    lc.exclude = False
cam_d = bpy.data.cameras.new('DD_cam'); cam_d.type = 'ORTHO'; cam_d.ortho_scale = SCALE
cam = bpy.data.objects.new('DD_cam', cam_d); sc.collection.objects.link(cam); sc.camera = cam
r = sc.render
r.engine = 'CYCLES'; sc.cycles.samples = 1; sc.cycles.use_denoising = False
r.resolution_x = r.resolution_y = W; r.resolution_percentage = 100
r.use_freestyle = True; r.line_thickness_mode = 'ABSOLUTE'
vl = sc.view_layers[0]; vl.use_freestyle = True
fs = vl.freestyle_settings
fs.crease_angle = math.radians(128)
for ls in list(fs.linesets):
    fs.linesets.remove(ls)
LS = fs.linesets.new('DD')
LS.select_by_visibility = True; LS.visibility = 'VISIBLE'; LS.select_by_edge_types = True
for a in ('select_silhouette', 'select_border', 'select_crease', 'select_contour', 'select_external_contour',
          'select_suggestive_contour', 'select_ridge_valley', 'select_material_boundary', 'select_edge_mark'):
    setattr(LS, a, False)
LS.select_silhouette = True; LS.select_external_contour = True
LS.linestyle.thickness = 1.0; LS.linestyle.color = (0, 0, 0)
sc.svg_export.use_svg_export = True; sc.svg_export.mode = 'FRAME'
TMP = tempfile.mkdtemp(prefix='dedale_')
NUM = re.compile(r'(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)')


def placer(az, pl):
    a, e = math.radians(az), math.radians(pl)
    direc = Vector((-math.sin(a) * math.cos(e), -math.cos(a) * math.cos(e), math.sin(e)))
    cam.location = CEN + direc * 2.0
    cam.rotation_euler = (-direc).to_track_quat('-Z', 'Y').to_euler()
    bpy.context.view_layer.update()


def rendre(objs, mode):
    keep = {o.name for o in objs}
    for o in O:
        o.hide_render = o.name not in keep
    LS.select_crease = mode == 'crease'
    LS.select_silhouette = mode != 'ext'
    r.filepath = os.path.join(TMP, 'p_')
    bpy.ops.render.render(write_still=False)
    f = os.path.join(TMP, 'p_%04d.svg' % sc.frame_current)
    txt = open(f, encoding='ascii').read(); os.remove(f)
    pls = []
    for d in re.findall(r' d="([^"]*)"', txt):
        pts = [(float(x), float(y)) for x, y in NUM.findall(d)]
        if len(pts) >= 2:
            pls.append(pts)
    return pls


def proj(v):
    p = world_to_camera_view(sc, cam, v)
    return (p.x * W, (1 - p.y) * W)


def vue(nom, az, pl):
    placer(az, pl)
    groupes = []
    for gid, lots, mode in PASSES:
        ds = []
        for objs in lots:
            ds += lignes(rendre(objs, mode))
        groupes.append('<g id="%s">%s</g>' % (gid, ''.join('<path d="%s"/>' % d for d in ds)))
    nerf = []
    for cn in N['courbes']:
        for pts in courbe_pts(O[cn]):
            nerf += lignes([[proj(p) for p in pts]], minlen=0.5)
    groupes.append('<g id="nerf">%s</g>' % ''.join('<path d="%s"/>' % d for d in nerf))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" data-nerf="%s" data-vue="%s" '
           'data-azimut="%g" data-plongee="%g">%s</svg>\n') % (W, W, NERF, nom, az, pl, ''.join(groupes))
    anc = {}
    for n in N['ancres']:
        x, y = proj(centre(O[n]))
        anc[n] = [round(x, 1), round(y, 1)]
    os.makedirs(SORTIE, exist_ok=True)
    open(os.path.join(SORTIE, '%s-%s.svg' % (NERF, nom)), 'w', encoding='utf-8', newline='\n').write(svg)
    json.dump({'nerf': NERF, 'vue': nom, 'azimut': az, 'plongee': pl, 'taille': W,
               'echelle_m': round(SCALE, 4), 'ancres': anc},
              open(os.path.join(SORTIE, '%s-%s.json' % (NERF, nom)), 'w', encoding='utf-8', newline='\n'),
              ensure_ascii=False, indent=1, sort_keys=True)
    print('DEDALE vue', nom, len(svg), 'octets')


if TOUR:
    T = CFG['tour']
    for k in range(T['n']):
        vue('t%d' % k, k * T['pas'], T['plongee'])
else:
    for nom, v in CFG['vues'].items():
        if VUES and nom not in VUES:
            continue
        vue(nom, v['azimut'], v['plongee'])
print('DEDALE fin', NERF)
