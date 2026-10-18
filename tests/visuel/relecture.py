"""Expose bounded CI previews through the GitHub connector for visual review.

This only reads captures. It never adopts or changes the visual reference.
"""
import base64
import io
from pathlib import Path
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[2]
for name in ['clair_ordinateur_not-fenetre','clair_mobile_not-fenetre','clair_ordinateur_not','clair_ordinateur_memo','sombre_ordinateur_not-fenetre']:
    actual=ROOT/'qa/visuel/out/actuel'/f'{name}.png'
    reference=ROOT/'qa/visuel/reference'/f'{name}.webp'
    if not actual.exists() or not reference.exists():
        continue
    difference=ROOT/'qa/visuel/out/diff'/f'{name}.png'
    if difference.exists():
        picture=Image.open(difference).convert('RGB')
        picture=picture.crop((0,0,picture.width,min(picture.height,1100)))
        data=io.BytesIO();picture.save(data,format='PNG',optimize=True)
        print('IRIS_ECARTS '+name+' '+base64.b64encode(data.getvalue()).decode())
    views=[]
    for path in [reference,actual]:
        picture=Image.open(path).convert('RGB')
        picture=picture.crop((0,0,picture.width,min(picture.height,1100)))
        picture.thumbnail((900,900))
        views.append(picture)
    canvas=Image.new('RGB',(sum(v.width for v in views),max(v.height for v in views)+30),'white')
    draw=ImageDraw.Draw(canvas)
    x=0
    for label,picture in zip(['REFERENCE','ACTUEL'],views):
        draw.text((x+8,8),label,fill='black');canvas.paste(picture,(x,30));x+=picture.width
    data=io.BytesIO();canvas.save(data,format='PNG',optimize=True)
    print('IRIS_RELECTURE '+name+' '+base64.b64encode(data.getvalue()).decode())
