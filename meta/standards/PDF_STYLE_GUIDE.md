# Deep Study PDF Style Guide

## Typography

- Canonical Persian font: **Vazirmatn**.
- Body, headings, tables, captions, page numbers and Persian numerals use Vazirmatn.
- Technical identifiers/commands remain Latin; direction is isolated as LTR where needed.
- Font binary is a build dependency and is **not committed**. The pinned release and retrieval/validation workflow are version-controlled.

## Page

- A4 portrait by default; landscape only when semantic content requires it.
- Safe margins; content must never touch border/footer.
- Thin formal page border on content pages.
- Footer: document ID/version + Persian page counter where practical.
- Cover page independent and uncluttered.

## RTL/LTR

- Persian prose true RTL and right-aligned.
- Code, URLs, commands, hashes, version strings and paths are LTR-isolated.
- Mixed Persian/English punctuation must be visually verified after rendering.

## Heading hierarchy

- H1 starts a major phase/chapter when sensible.
- H2/H3 never orphan at page bottom.
- Color palette limited and formal; semantic hierarchy comes mainly from size/weight/spacing.

## Tables and boxes

- Tables must stay within printable area; long text columns get width priority.
- Repeating header row for multi-page tables when supported.
- Avoid a table starting with only its header at page bottom.
- Callout boxes use a consistent style and avoid awkward page splits.

## TOC

- true RTL row layout;
- title at right extreme;
- page number at left extreme;
- full dotted leader between;
- generated/revalidated only after final pagination.

## Visual QA gate

Every final candidate is rendered to PNGs (recommended 180-220 DPI). **Every page** is inspected. Defects trigger source edit -> regeneration -> full rerender/reinspection. Spot checking is not accepted for final status.
