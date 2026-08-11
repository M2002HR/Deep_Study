#!/usr/bin/env python3
from __future__ import annotations
import argparse, subprocess, tempfile, hashlib
from pathlib import Path
from bs4 import BeautifulSoup, Tag
from weasyprint import HTML, CSS
from pypdf import PdfReader, PdfWriter

DOC_ID='DS-DKR-SYL'
VERSION='1.1.0'
CUTOFF='2026-08-11'

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024), b''): h.update(b)
    return h.hexdigest()

def pandoc_fragment(source: Path, out: Path) -> None:
    subprocess.run(['pandoc', str(source), '--from', 'gfm', '--to', 'html5', '--section-divs', '--wrap=auto', '-o', str(out)], check=True)

def build_html(fragment: Path, out: Path) -> None:
    soup=BeautifulSoup(fragment.read_text(encoding='utf-8'),'html.parser')
    first_h1=soup.find('h1')
    if first_h1 and 'Deep Study' in first_h1.get_text(): first_h1.decompose()
    first_section=soup.find('section', class_='level1')
    if first_section:
        for child in list(first_section.children):
            if isinstance(child, Tag) and child.name=='p':
                child.decompose(); continue
            if isinstance(child, Tag) and child.name=='section': break
    used=set()
    def slug(h, idx):
        if h.get('id'): return h['id']
        parent=h.parent
        if isinstance(parent, Tag) and parent.get('id'):
            parent_id=parent['id']; del parent['id']; return parent_id
        base=f'section-{idx}'
        while base in used: base += 'x'
        return base
    headings=[]
    for idx,h in enumerate(soup.find_all(['h1','h2']),1):
        text=' '.join(h.get_text(' ',strip=True).split())
        if not text: continue
        hid=slug(h,idx); h['id']=hid; used.add(hid)
        headings.append((h.name,hid,text))
        if h.name=='h1': h['class']=h.get('class',[])+['phase-heading']
    for pre in soup.find_all('pre'): pre['class']=pre.get('class',[])+['ltr-block']
    for code in soup.find_all('code'): code['dir']='ltr'
    nav=BeautifulSoup('<nav class="toc-block"><h1 class="toc-title">فهرست مطالب</h1><div class="toc-rows"></div></nav>','html.parser').nav
    rows=nav.find('div',class_='toc-rows')
    for level,hid,text in headings:
        cls='toc-row toc-level1' if level=='h1' else 'toc-row toc-level2'
        a=soup.new_tag('a', href=f'#{hid}'); a['class']=cls.split()
        title=soup.new_tag('span'); title['class']=['toc-entry-title']; title.string=text
        dots=soup.new_tag('span'); dots['class']=['toc-dots']
        a.append(title); a.append(dots); rows.append(a)
    cover_sub='سیلابس جامع تسلط عمیق بر Docker و پشته‌ی کانتینر<br><span dir="ltr" class="cover-stack">Linux Containers / OCI / containerd / runc / Implementation</span>'
    html=f'''<!doctype html>\n<html lang="fa" dir="rtl"><head><meta charset="utf-8"><title>Docker Mastery Syllabus v1.1.0 - Deep Study</title></head>\n<body>\n<section class="cover">\n  <div class="cover-kicker">DEEP STUDY</div>\n  <div class="cover-title" dir="ltr">Docker Mastery Syllabus</div>\n  <div class="cover-subtitle">{cover_sub}</div>\n  <div class="cover-rule"></div>\n  <table class="cover-meta"><tbody>\n    <tr><th>نسخه</th><td dir="ltr">1.1.0</td></tr>\n    <tr><th>وضعیت</th><td dir="ltr">Canonical Foundation</td></tr>\n    <tr><th>Research cutoff</th><td dir="ltr">2026-08-11</td></tr>\n    <tr><th>نقش سند</th><td dir="ltr">Master Curriculum / Pre-first-module baseline</td></tr>\n    <tr><th>فونت اصلی</th><td dir="ltr">Vazirmatn</td></tr>\n  </tbody></table>\n  <div class="cover-note">این سند نقشه‌ی اصلی مسیر <bdi dir="ltr">Docker</bdi> در پروژه <bdi dir="ltr">Deep Study</bdi> است. نسخه‌ی Markdown منبع اصلی و قابل ویرایش است و PDF برای مطالعه استفاده می‌شود.</div>\n</section>\n{str(nav)}\n{str(soup)}\n</body></html>'''
    out.write_text(html,encoding='utf-8')

def add_metadata(src: Path, dst: Path) -> None:
    reader=PdfReader(str(src)); writer=PdfWriter(); writer.append_pages_from_reader(reader)
    writer.add_metadata({
        '/Producer':'WeasyPrint 68.0',
        '/Title':'Docker Mastery Syllabus v1.1.0 - Deep Study',
        '/Subject':'Canonical Docker mastery curriculum for Deep Study',
        '/Author':'Deep Study',
        '/Keywords':'Docker; OCI; containerd; runc; Moby; BuildKit; DevOps; Deep Study',
        '/DeepStudyDocumentID':DOC_ID,
        '/DeepStudyVersion':VERSION,
        '/ResearchCutoff':CUTOFF,
        '/VisualQAStatus':'Tracked in repository QA report and exact approved-candidate contract',
        '/VisualQADate':'See curriculum/devops/docker/QA_REPORT_v1.1.0.md',
        '/CanonicalFont':'Vazirmatn v33.003',
    })
    with dst.open('wb') as f: writer.write(f)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source', required=True, type=Path)
    p.add_argument('--output', required=True, type=Path)
    p.add_argument('--font-dir', required=True, type=Path)
    p.add_argument('--style', default=Path('assets/styles/deep-study-pdf.css'), type=Path)
    a=p.parse_args()
    a.output.parent.mkdir(parents=True,exist_ok=True)
    for name in ['Vazirmatn-Regular.ttf','Vazirmatn-Medium.ttf','Vazirmatn-Bold.ttf']:
        if not (a.font_dir/name).exists(): raise SystemExit(f'Missing font: {a.font_dir/name}')
    css=a.style.read_text(encoding='utf-8').replace('__FONT_BASE__', a.font_dir.resolve().as_uri())
    with tempfile.TemporaryDirectory() as td:
        td=Path(td); frag=td/'body.html'; doc=td/'document.html'; raw=td/'raw.pdf'; cssp=td/'style.css'
        pandoc_fragment(a.source,frag); build_html(frag,doc); cssp.write_text(css,encoding='utf-8')
        HTML(filename=str(doc),base_url=str(td)).write_pdf(str(raw),stylesheets=[CSS(filename=str(cssp))])
        add_metadata(raw,a.output)
    print(f'{a.output}: sha256={sha256(a.output)}')

if __name__=='__main__': main()
