"""Check source integrity, full page coverage, scores, provenance and public links."""
from pathlib import Path
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from hashlib import sha256
import re, json
from build_transcripts import ROOT, BASE, SPECS, CONTEXT_FILES, source_pages, read, portable_markdown

PDF_HASHES={
    '34-19-q-q.pdf':'e204c014af0427517abaaec53a423ee2ed70de628d6788c8d783d8abbbf5853d',
    'Eng_yaxshi_veb_sayt_baholash_mezonlari.pdf':'d783492c9729875ac49f09ad574f5eaf2d1f08a2e3a9c2951540f91dddf8cb1e',
    'ustoz-ai-saytdagi-nizom.pdf':'b96018da0184cbabc5cd09a1864abcd895b68441a9f503b5bec6ff8ff71f378e',
}
def tight(text):return re.sub(r'\s','',text)
def check():
    for filename,expected in PDF_HASHES.items():
        assert sha256((ROOT/'sources'/filename).read_bytes()).hexdigest()==expected,filename
    combined=read(ROOT/'nizom.md')
    full=read(ROOT/'ai.md')
    assert combined in full
    assert read(ROOT/'CONTEXT-STATUS.md') in full
    for filename in CONTEXT_FILES:
        body=read(ROOT/filename)
        assert portable_markdown(body).strip() in full, ('Outdated combined context',filename)
    assert portable_markdown('[PDF](sources/test.pdf)\n```text\n[example](keep.md)\n```\n') == '[PDF]('+BASE+'/sources/test.pdf)\n```text\n[example](keep.md)\n```\n'
    facts=json.loads(read(ROOT/'07-FACTS.json'))
    assert facts['scope']=='historical_research_snapshot'
    total=0
    for spec in SPECS:
        slug,title,pdf,raw,count,status=spec
        md=read(ROOT/'transcripts'/f'{slug}.md')
        assert md in combined
        assert len(re.findall(r'^## PDF sahifa \d+ /',md,re.M))==count
        for n,source in source_pages(spec).items():
            anchor=f'<a id="{slug}-p{n:02}"></a>'
            assert md.count(anchor)==combined.count(anchor)==1
            assert f'{pdf}#page={n})' in md
            page=md.split(anchor,1)[1].split('\n\n---\n\n',1)[0]
            if slug!='qaror':
                body=page.split('```text\n',1)[1].split('\n```',1)[0]
                if slug=='mezon':assert tight(body)==tight(source), ('draft omitted/reordered text',n)
                else:assert Counter(tight(body))==Counter(tight(source)),('site omitted text',n)
            total+=1
        assert status in md
    assert total==39
    signed=read(ROOT/'transcripts/qaror.md')
    # Source differences are not harmonized or silently made into current rules.
    assert 'real vaqt rejimida kichik texnik' in signed
    assert "mezoni (5-mezon)" in signed
    site=read(ROOT/'transcripts/sayt.md')
    assert 'Kreativlik va originallik' in site
    assert '16¹.' in signed and '20¹.' in signed and '33¹.' in signed
    for n in list(range(1,35)):
        assert re.search(rf'(?<!\d){n}\.\s',signed),f'Signed clause {n} missing'
    # Reconstructed signed tables: all 3 tracks still sum to 100.
    tables=json.loads(read(ROOT/'transcripts/qaror-tables.json'))
    allrows=[]
    for n in (14,15,16):
        for line in tables[str(n)]['markdown'].splitlines():
            if re.match(r'^\| [1-6] \|',line):allrows.append(line.split('|')[1:-1])
    assert len(allrows)==18
    for start in (0,6,12):
        rows=allrows[start:start+6]
        assert [int(r[0]) for r in rows]==list(range(1,7))
        assert [int(r[-1]) for r in rows]==[30,20,10,10,20,10]
    draft=read(ROOT/'transcripts/mezon.md')
    assert 'Tashkilotchilar tasdig‘iga taqdim etiladigan tahrir' in draft
    for code in ['1.1','1.2','1.3','1.4','2.1','2.2','2.3','2.4','3.1','3.2','3.3','4.1','4.2','4.3','5.1','5.2','5.3','5.4','6.1','6.2','6.3']:
        assert code in draft
    assert 'Bilet 001' in draft and all(f'T{n}' in draft for n in range(1,5))

    class Document(HTMLParser):
        def __init__(self):super().__init__();self.ids=[];self.links=[]
        def handle_starttag(self,tag,attrs):
            attrs=dict(attrs)
            if 'id' in attrs:self.ids.append(attrs['id'])
            if tag=='a' and 'href' in attrs:self.links.append(attrs['href'])
    checked=0
    for f in [ROOT/'index.html',ROOT/'ai.html',ROOT/'nizom.html',*sorted((ROOT/'transcripts').glob('*.html'))]:
        doc=Document();doc.feed(read(f));assert len(doc.ids)==len(set(doc.ids)),f
        for link in doc.links:
            parts=urlsplit(link)
            if parts.scheme and not link.startswith(BASE+'/'):continue
            if link.startswith(BASE+'/'):target=ROOT/unquote(parts.path.removeprefix('/ustoz/'))
            elif parts.path:target=f.parent/unquote(parts.path)
            else:target=f
            if target.is_dir():target=target/'index.html'
            assert target.is_file(),(f.name,link)
            if parts.fragment and target.suffix=='.html':
                other=Document();other.feed(read(target));assert parts.fragment in other.ids,(f.name,link)
            checked+=1
    manifest=json.loads(read(ROOT/'MANIFEST.json'))
    assert manifest['research_as_of']=='2026-10-09'
    for record in manifest['files']:
        data=(ROOT/record['path']).read_bytes()
        assert len(data)==record['bytes'] and sha256(data).hexdigest()==record['sha256'],record['path']
    print(f'PASS: 39 pages, both digital PDFs fully covered, all signed clauses, 3 × 100-point tables, draft/sample status, {checked} local links, original PDF hashes, package manifest.')

if __name__=='__main__':check()
