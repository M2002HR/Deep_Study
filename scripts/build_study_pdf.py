#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, subprocess, tempfile
from pathlib import Path
import yaml
from bs4 import BeautifulSoup, Tag
from weasyprint import HTML, CSS
from pypdf import PdfReader, PdfWriter


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()


def pandoc_fragment(source: Path, out: Path) -> None:
    subprocess.run([
        'pandoc', str(source), '--from', 'gfm+raw_html', '--to', 'html5',
        '--section-divs', '--wrap=auto', '-o', str(out)
    ], check=True)


def build_html(fragment: Path, out: Path, meta: dict) -> None:
    soup = BeautifulSoup(fragment.read_text(encoding='utf-8'), 'html.parser')
    used = set()
    headings = []
    current_h1 = ''
    for idx, h in enumerate(soup.find_all(['h1', 'h2']), 1):
        text = ' '.join(h.get_text(' ', strip=True).split())
        if not text:
            continue
        hid = h.get('id') or f'section-{idx}'
        while hid in used:
            hid += 'x'
        h['id'] = hid
        used.add(hid)
        if h.name == 'h1':
            current_h1 = text
        # Reference/changelog subentries add noise to the navigational TOC.
        # Keep the top-level section, but omit its H2 children.
        if h.name == 'h2' and current_h1 in {'منابع', 'Changelog'}:
            continue
        headings.append((h.name, hid, text))
    for pre in soup.find_all('pre'):
        pre['class'] = pre.get('class', []) + ['ltr-block']
    for code in soup.find_all('code'):
        code['dir'] = 'ltr'

    nav = BeautifulSoup('<nav class="toc-block"><h1 class="toc-title">فهرست مطالب</h1><div class="toc-rows"></div></nav>', 'html.parser').nav
    rows = nav.find('div', class_='toc-rows')
    for level, hid, text in headings:
        cls = 'toc-row toc-level1' if level == 'h1' else 'toc-row toc-level2'
        a = soup.new_tag('a', href=f'#{hid}')
        a['class'] = cls.split()
        title = soup.new_tag('span'); title['class'] = ['toc-entry-title']; title.string = text
        dots = soup.new_tag('span'); dots['class'] = ['toc-dots']
        a.append(title); a.append(dots); rows.append(a)

    cover_title = meta['cover_title']
    subtitle = meta['subtitle']
    cover_note = meta.get('cover_note', '')
    rows_html = ''
    for label, value in [
        ('شناسه سند', meta['document_id']),
        ('نسخه', meta['version']),
        ('وضعیت', meta['status']),
        ('مسیر', meta['track']),
        ('Research cutoff', meta['research_cutoff']),
        ('سطح', meta.get('depth', 'Core')),
    ]:
        rows_html += f'<tr><th>{label}</th><td dir="ltr">{value}</td></tr>'

    html = f'''<!doctype html>
<html lang="fa" dir="rtl"><head><meta charset="utf-8"><title>{meta['pdf_title']}</title></head>
<body>
<section class="cover">
  <div class="cover-kicker">DEEP STUDY</div>
  <div class="cover-title" dir="ltr">{cover_title}</div>
  <div class="cover-subtitle">{subtitle}</div>
  <div class="cover-rule"></div>
  <table class="cover-meta"><tbody>{rows_html}</tbody></table>
  <div class="cover-note">{cover_note}</div>
</section>
{str(nav)}
{str(soup)}
</body></html>'''
    out.write_text(html, encoding='utf-8')


def add_metadata(src: Path, dst: Path, meta: dict) -> None:
    reader = PdfReader(str(src)); writer = PdfWriter(); writer.append_pages_from_reader(reader)
    writer.add_metadata({
        '/Producer': 'WeasyPrint 68.0',
        '/Title': meta['pdf_title'],
        '/Subject': meta.get('subject', meta['subtitle']),
        '/Author': 'Deep Study',
        '/Keywords': '; '.join(meta.get('keywords', [])),
        '/DeepStudyDocumentID': meta['document_id'],
        '/DeepStudyVersion': str(meta['version']),
        '/ResearchCutoff': str(meta['research_cutoff']),
        '/CanonicalFont': 'Vazirmatn v33.003',
        '/VisualQAStatus': 'See repository QA report for exact candidate approval',
    })
    with dst.open('wb') as f:
        writer.write(f)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source', type=Path, required=True)
    p.add_argument('--manifest', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--font-dir', type=Path, required=True)
    p.add_argument('--style', type=Path, required=True)
    a = p.parse_args()
    meta = yaml.safe_load(a.manifest.read_text(encoding='utf-8'))
    for key in ['document_id','version','status','research_cutoff','track','cover_title','subtitle','pdf_title']:
        if not meta.get(key):
            raise SystemExit(f'Missing manifest key: {key}')
    for name in ['Vazirmatn-Regular.ttf','Vazirmatn-Medium.ttf','Vazirmatn-Bold.ttf']:
        if not (a.font_dir / name).exists():
            raise SystemExit(f'Missing font: {a.font_dir/name}')
    css = a.style.read_text(encoding='utf-8')
    css = css.replace('__FONT_BASE__', a.font_dir.resolve().as_uri())
    css = css.replace('__DOC_ID__', meta['document_id']).replace('__VERSION__', str(meta['version']))
    a.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        frag = td / 'body.html'; doc = td / 'document.html'; raw = td / 'raw.pdf'; cssp = td / 'style.css'
        pandoc_fragment(a.source, frag)
        build_html(frag, doc, meta)
        cssp.write_text(css, encoding='utf-8')
        HTML(filename=str(doc), base_url=str(a.source.parent.resolve())).write_pdf(str(raw), stylesheets=[CSS(filename=str(cssp))])
        add_metadata(raw, a.output, meta)
    print(f'{a.output}: sha256={sha256(a.output)}')

if __name__ == '__main__':
    main()
