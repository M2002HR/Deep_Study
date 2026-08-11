# Visual QA Report - <Document ID> / <Version>

- PDF: `<path>`
- Canonical source: `<path>`
- Research cutoff: `<date>`
- QA date: `<date>`
- Reviewer: `<human/agent>`
- Page count: `<n>`
- Render DPI: `<dpi>`
- Font baseline: `Vazirmatn <version>`
- Final status: `PASS | FAIL`

## Structural preflight

- [ ] PDF opens without warnings.
- [ ] Expected page size/count.
- [ ] Text extraction sane / no replacement glyphs.
- [ ] Font embedding verified.
- [ ] No accidental font fallback.
- [ ] Artifact hash recorded.

## Full visual review

- [ ] Cover.
- [ ] TOC: true RTL, right title, left page number, dotted leaders, correct pagination.
- [ ] Every page inspected.
- [ ] No clipping/overlap.
- [ ] No orphan headings.
- [ ] No broken table/box boundaries.
- [ ] Mixed RTL/LTR, URLs, commands, hashes and punctuation checked.
- [ ] Borders, margins and footers/page counters consistent.
- [ ] Tables readable and within page bounds.
- [ ] Suspicious blank pages/large whitespace explained.

## Defects and corrections

| Iteration | Page(s) | Defect | Source-level correction | Re-QA result |
|---|---:|---|---|---|

## Regression evidence

Describe what was re-rendered after each fix. A layout-sensitive change requires another all-page visual pass.

## Final release evidence

- SHA256 PDF: `<hash>`
- SHA256 source: `<hash>`
- Visual QA: `PASS`
