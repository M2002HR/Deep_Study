# Visual QA Report - DS-DKR-SYL / v1.1.0

- PDF: `curriculum/devops/docker/artifacts/docker_mastery_syllabus_v1.1.0.pdf`
- Canonical source: `curriculum/devops/docker/docker_mastery_syllabus_v1.1.0.md`
- Research cutoff: 2026-08-11
- QA date: 2026-08-11
- Page count: 91
- Final full render: 180 DPI
- Canonical font: Vazirmatn v33.003
- Approved CI run: `31455150007`
- Approved PDF SHA256: `2f42b4808169a7dfd85a9a46143cbaedaedfe4fa5570be189b4d08c85c404eb9`
- GitHub Actions artifact ZIP digest: `c49e4d4998e5db6b52217e6a4d7f8b4c34a150e64f1cb454636522300759e6a9`
- Final status: **PASS**

## Structural preflight

- PDF opens and preflight reports no warnings.
- A4, 91 pages, searchable text.
- `pdffonts` on the exact approved CI candidate reports only `Vazirmatn`, `Vazirmatn-Medium`, and `Vazirmatn-Bold`; all are embedded/subset/Unicode.
- `pdftotext` found no replacement-glyph condition during the local release preflight.
- CI clean-runner font resolution was tested explicitly. The first clean-runner candidate exposed a DejaVu fallback and was rejected. The pipeline was fixed to register the pinned Vazirmatn files in fontconfig, and the next candidate passed the font contract.

## Visual review

The exact PDF inside the CI artifact from run `31455150007` was rendered at 180 DPI and **all 91 pages were visually inspected**. Twenty-three 2x2 contact sheets were reviewed in sequence, covering every page. Checks included cover, all TOC pages, content pages, phase gates, table page, prompt/code block, bibliography/source registry, footer/page counters, borders, margins, mixed Persian/English text, URLs, headings, whitespace, and page breaks.

Dedicated single-page checks were then performed for:

- cover page (page 1),
- TOC page with mixed RTL/LTR and dotted leaders (page 3),
- Coverage Matrix table (page 85),
- dense bibliography/URL page (page 88).

No clipping, overlap, broken glyph, orphan-heading problem, malformed table, TOC alignment problem, border/margin defect, or bidi URL defect remained.

## Defect iterations retained from the canonical source build

1. The first local all-page pass found a bidi rendering defect in URL lines: URLs inside RTL prose could visually place the trailing `/` at the beginning.
2. The stylesheet was corrected by isolating link direction as LTR.
3. HTML anchor generation was corrected so Pandoc section-wrapper IDs are moved to the actual heading, eliminating duplicate PDF anchors.
4. PDF was rebuilt; page count remained 91.
5. The corrected local PDF was rendered again at 180 DPI and all 91 pages were reviewed.
6. A later clean GitHub runner revealed that CSS font declaration alone did not guarantee Vazirmatn resolution. That CI candidate was rejected because `pdffonts` showed DejaVu Sans fallback.
7. The workflow was corrected to install/register the pinned Vazirmatn v33.003 Regular/Medium/Bold files in fontconfig and to fail if `fc-match` or the generated PDF font table does not resolve Vazirmatn.
8. The resulting CI candidate from run `31455150007` passed mechanical checks and received the full 91-page visual review documented above.
9. Approval bookkeeping was cross-checked against the `SHA256SUMS` file inside the Actions artifact. The PDF SHA and the enclosing ZIP artifact digest are deliberately recorded separately; promotion is locked to the inner PDF SHA.

## Approval rule

Build success alone is not approval. The canonical repository PDF may be promoted only if the downloaded Actions artifact matches the approved run ID and the **inner PDF SHA256** above. The promotion workflow re-verifies the PDF SHA and embedded-font contract before committing the artifact.

## Release hashes

- Approved canonical PDF SHA256: `2f42b4808169a7dfd85a9a46143cbaedaedfe4fa5570be189b4d08c85c404eb9`
- GitHub Actions artifact ZIP SHA256: `c49e4d4998e5db6b52217e6a4d7f8b4c34a150e64f1cb454636522300759e6a9`
- Markdown SHA256: `14d20dd1628e201df650627cc9005f3b00071856806eeb3b536f5fbe6e9cc737`
