# Visual QA Report - DS-DKR-SYL / v1.1.0

- PDF: `curriculum/devops/docker/artifacts/docker_mastery_syllabus_v1.1.0.pdf`
- Canonical source: `curriculum/devops/docker/docker_mastery_syllabus_v1.1.0.md`
- Research cutoff: 2026-08-11
- QA date: 2026-08-11
- Page count: 91
- Final full render: 180 DPI
- Canonical font: Vazirmatn v33.003
- Final status: **PASS**

## Structural preflight

- PDF opens and preflight reports no warnings.
- A4, 91 pages, searchable text.
- `pdffonts` reports only `Vazirmatn`, `Vazirmatn-Medium`, `Vazirmatn-Bold`; all are embedded/subset/Unicode.
- `pdftotext` found zero U+FFFD replacement characters and no black-square placeholder glyphs.

## Visual review

All 91 pages were rendered and inspected. Checks included cover, all TOC pages, content pages, phase gates, table page, prompt/code block, bibliography/source registry, footer/page counters, borders, margins, mixed Persian/English, URLs, headings and page breaks.

### Defect iteration

1. First all-page pass found a bidi rendering defect in URL lines: URLs inside RTL prose could visually place the trailing `/` at the beginning.
2. The source stylesheet was corrected by isolating link direction as LTR.
3. The HTML anchor generation was also corrected so Pandoc section wrapper IDs are moved to the actual heading, eliminating duplicate PDF anchors.
4. PDF was rebuilt; page count remained 91.
5. The corrected PDF was rendered again at 180 DPI and **all 91 pages were reviewed again**. No remaining visible clipping, overlap, broken glyph, table overflow, TOC alignment problem or URL-direction defect was found.

## Metadata-only regression

After visual approval, PDF metadata was enriched with document/version/research/QA fields. Representative pages 1, 12 and 91 were re-rendered at the same 180 DPI and were pixel-identical to the approved render.

## Release hashes

- PDF SHA256: `e4af68904b5c5fbdcda94f743f1969d8ee80ae170023fbf09b2cf4b4fca16d64`
- Markdown SHA256: `14d20dd1628e201df650627cc9005f3b00071856806eeb3b536f5fbe6e9cc737`
