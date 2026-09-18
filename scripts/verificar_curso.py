"""Valida estrutura, manifesto e links locais da publicação estática."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=[];self.links=[];self.topics=[];self.manifest='';self.in_manifest=False;self.h1=0;self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if 'data-inema-topic' in a:self.topics.append(a['data-inema-topic'])
        if tag=='script' and 'data-inema-manifest' in a:self.in_manifest=True
        for k in ('href','src'):
            if a.get(k):self.links.append(a[k])
    def handle_data(self,s):
        if self.in_manifest:self.manifest+=s
    def handle_endtag(self,tag):
        if tag=='script':self.in_manifest=False
pages=[ROOT/'index.html',*(ROOT/'curso').rglob('*.html'),ROOT/'materiais/index.html']
parsed={p:Page(p.read_text()) for p in pages}
expected=None;total=0
for p,d in parsed.items():
    assert d.h1==1,(p,'h1')
    assert len(d.ids)==len(set(d.ids)),(p,'IDs repetidos')
    m=json.loads(d.manifest)
    if expected is None:expected=m
    assert m==expected,(p,'manifesto diferente')
    if p.name.startswith('modulo-'):
        assert len(d.topics)==6,(p,'tópicos')
        total+=len(d.topics)
    for link in d.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        target=(p.parent/unquote(u.path)).resolve() if u.path else p
        if target.is_dir():target=target/'index.html'
        assert target.is_relative_to(ROOT),(p,link,'fora do projeto')
        assert target.exists(),(p,link,'arquivo ausente')
        if u.fragment and target in parsed:assert unquote(u.fragment) in parsed[target].ids,(p,link,'âncora ausente')
assert total==72,total
assert sum(m['topics'] for t in expected['tracks'] for m in t['modules'])==72
print(f'PASS: {len(pages)} páginas, 12 módulos, {total} tópicos, manifestos e links locais válidos.')
