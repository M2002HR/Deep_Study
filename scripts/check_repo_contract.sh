#!/usr/bin/env bash
set -euo pipefail
root="${1:-.}"
required=(
  README.md PROJECT.md STUDY_METHOD.md CONTENT_STANDARD.md SOURCE_POLICY.md
  RESEARCH_METHOD.md MASTERY.md AGENTS.md DOCUMENT_REGISTRY.md
  meta/prompts/MASTER_PDF_PROMPT.md
  meta/prompts/source/REPORT_GENERATION_PROMPT_ORIGINAL.md
  meta/standards/PDF_STYLE_GUIDE.md
  meta/standards/PDF_PRODUCTION_WORKFLOW.md
  meta/standards/CROSS_DOCUMENT_CONSISTENCY.md
)
for f in "${required[@]}"; do test -s "$root/$f" || { echo "missing: $f" >&2; exit 1; }; done
# Font binaries and commercial book binaries are intentionally not repository assets.
if find "$root" -type f \( -iname '*.ttf' -o -iname '*.otf' -o -iname '*.woff' -o -iname '*.woff2' \) | grep -q .; then
  echo 'font binary found in repository tree; forbidden' >&2; exit 1
fi
if find "$root/library" -type f \( -iname '*.pdf' -o -iname '*.epub' -o -iname '*.mobi' \) | grep -q .; then
  echo 'book binary found under library/; use catalog metadata instead' >&2; exit 1
fi
echo 'Deep Study repository contract: PASS'
