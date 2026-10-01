"""Generate a consistent notebook sketch note.

Example:
    python tools/generate_sketch_note.py 37 "LLM Model APIs" \
      "request → model → structured output → application" \
      "The interface is a contract between an application and a probabilistic system."
"""
from pathlib import Path
import html, re, sys

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets'/'sketch-notes'

if len(sys.argv) != 5:
    raise SystemExit(__doc__)
num,title,flow,insight=sys.argv[1:]
words=flow.split(' → ')
xs=[55,240,425,610,795] if len(words)==5 else ([90,300,510,720] if len(words)==4 else [90,360,630])
colors=['#fff1b8','#e8f1ff','#e9f7ee','#fde5e1']
boxes=[]
for i,w in enumerate(words[:5]):
    x=xs[i]; y=255 if i%2==0 else 365
    boxes.append(f'<g transform="rotate({-1 if i%2==0 else 1} {x+75} {y+35})"><rect x="{x}" y="{y}" width="150" height="70" rx="12" fill="{colors[i%4]}" stroke="#172033" stroke-width="3"/><text x="{x+75}" y="{y+42}" text-anchor="middle" font-family="Comic Sans MS,Segoe Print,cursive" font-size="20" font-weight="700" fill="#172033">{html.escape(w[:24])}</text></g>')
arrows=[]
for i,x in enumerate(xs[:len(words)-1]):
    y1=325 if i%2==0 else 400; y2=400 if i%2==0 else 325
    arrows.append(f'<path d="M{x+150} {y1} C{x+175} {y1} {x+200} {y2} {xs[i+1]} {y2}" fill="none" stroke="#172033" stroke-width="4" marker-end="url(#arrow)"/>')
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="560" viewBox="0 0 900 560">
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#172033"/></marker></defs>
<rect width="900" height="560" fill="#fffdf8"/>
<text x="70" y="75" font-family="Comic Sans MS,Segoe Print,cursive" font-size="38" font-weight="700" fill="#172033">{html.escape(num)} · {html.escape(title)}</text>
<text x="72" y="125" font-family="Comic Sans MS,Segoe Print,cursive" font-size="24" fill="#b24b43">Think in systems, not syntax.</text>
<path d="M70 150 C220 135 350 170 520 145 S760 140 830 155" fill="none" stroke="#e1b34a" stroke-width="10" opacity=".65"/>
<text x="70" y="205" font-family="Comic Sans MS,Segoe Print,cursive" font-size="24" fill="#172033">{html.escape(insight)}</text>
{''.join(arrows)}{''.join(boxes)}
<text x="70" y="515" font-family="Comic Sans MS,Segoe Print,cursive" font-size="19" fill="#697588">Sketch it → predict it → break it → explain it.</text>
</svg>'''
name=f'{num}-'+re.sub(r'[^a-z0-9]+','-',title.lower()).strip('-')+'.svg'
OUT.mkdir(parents=True,exist_ok=True)
(OUT/name).write_text(svg,encoding='utf-8')
print(OUT/name)
