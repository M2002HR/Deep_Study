# PDF Production Workflow - Deep Study

This is the operational companion to `meta/prompts/MASTER_PDF_PROMPT.md`.
The master prompt is authoritative; this document turns it into a repeatable pipeline.

## Inputs required before generation

1. Document ID and Scope Contract.
2. Current syllabus node and prerequisites.
3. Current source registry / canonical sources.
4. Terminology and cross-document owners.
5. Research cutoff and version baseline.
6. Master PDF Prompt and relevant task prompt.

A final study PDF must never be generated from model memory alone.

## Production loop

1. Research and verify version-sensitive claims against canonical sources.
2. Write/update canonical Markdown or other structured source.
3. Run content/gap review against syllabus, scope and dependencies.
4. Generate the PDF using the canonical Vazirmatn font dependency.
5. Run structural preflight:
   - PDF opens, page count is sane, A4 unless deliberately overridden;
   - not encrypted unless required;
   - text is extractable when expected;
   - no replacement glyphs;
   - all used fonts are embedded;
   - Persian text uses Vazirmatn; no accidental fallback.
6. Render the **entire PDF** to images, preferably 180-220 DPI for final review.
7. Visually inspect **every page**, including cover, TOC, tables, boxes, code, URLs, mixed RTL/LTR, headings, page breaks, borders, footer/page numbers and empty-space anomalies.
8. Record every defect. Fix the canonical source/template/style - not only the final PDF artifact.
9. Rebuild and re-render. After a layout-sensitive change, re-review all pages. For metadata-only edits, re-render representative pages and prove visual identity to the already-approved render.
10. Mark Visual QA `PASS` only after the latest candidate has no known visual defects.
11. Create/update the artifact manifest and QA report.
12. Commit source + final PDF + manifest + QA report together.

## Regression rule

Every revision starts from the latest accepted source. A new fix must preserve earlier fixes. If a change can affect layout, the previous QA is invalidated until a new full-page review passes.

## Font rule

- Canonical Persian font: Vazirmatn.
- Font binaries are build dependencies and are not committed or shared as deliverables.
- The pinned font version/retrieval validation is version-controlled separately.
- `pdffonts` or equivalent must confirm embedding before publication.

## Required release evidence

A canonical PDF release should have:

- source file;
- final PDF;
- artifact manifest with hashes and baseline;
- visual QA report;
- source registry/citations;
- coverage/dependency updates when applicable;
- changelog entry when content or baseline changed.
