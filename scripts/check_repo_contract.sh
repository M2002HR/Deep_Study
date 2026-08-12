#!/usr/bin/env bash
set -euo pipefail
root="${1:-.}"
required=(
  README.md PROJECT.md STUDY_METHOD.md CONTENT_STANDARD.md SOURCE_POLICY.md
  RESEARCH_METHOD.md MASTERY.md AGENTS.md DOCUMENT_REGISTRY.md
  START_HERE.md CURRENT_STATE.md
  meta/CONTINUATION_PROTOCOL.md
  meta/prompts/MASTER_PDF_PROMPT.md
  meta/prompts/PDF_GENERATION.md
  meta/prompts/CONTINUE_EXISTING_TRACK.md
  meta/prompts/NEW_TOPIC_SYLLABUS.md
  meta/prompts/source/REPORT_GENERATION_PROMPT_ORIGINAL.md
  meta/standards/GIT_WORKFLOW.md
  meta/standards/PROGRESSION_AND_PREREQUISITES.md
  meta/standards/PDF_STYLE_GUIDE.md
  meta/standards/PDF_PRODUCTION_WORKFLOW.md
  meta/standards/CROSS_DOCUMENT_CONSISTENCY.md
  meta/standards/MODULE_GRANULARITY.md
  meta/standards/TERMINOLOGY.md
  meta/templates/study-document.yml
  meta/templates/STUDY_PDF_WORKFLOW.md
  scripts/build_study_pdf.py
  scripts/check_published_study_docs.sh
  assets/styles/deep-study-study-pdf.css
  curriculum/devops/docker/PROGRESS.md
  curriculum/devops/docker/coverage-matrix.md
  subjects/docker/DKR.01/README.md
  subjects/docker/DKR.01/DKR.01.md
  subjects/docker/DKR.01/document.yml
  subjects/docker/DKR.01/SOURCES.md
  subjects/docker/DKR.01/QA_REPORT_v1.0.0.md
  subjects/docker/DKR.01/artifact-manifest.yml
  subjects/docker/DKR.01/APPROVED_CANDIDATE.yml
  subjects/docker/DKR.01/artifacts/DS-DKR-01_v1.0.0.pdf
)
for f in "${required[@]}"; do test -s "$root/$f" || { echo "missing: $f" >&2; exit 1; }; done
# Font binaries and commercial book binaries are intentionally not repository assets.
if find "$root" -type f \( -iname '*.ttf' -o -iname '*.otf' -o -iname '*.woff' -o -iname '*.woff2' \) | grep -q .; then
  echo 'font binary found in repository tree; forbidden' >&2; exit 1
fi
if find "$root/library" -type f \( -iname '*.pdf' -o -iname '*.epub' -o -iname '*.mobi' \) | grep -q .; then
  echo 'book binary found under library/; use catalog metadata instead' >&2; exit 1
fi
# Stable handoff rules: published study docs must be discoverable and state dimensions must stay separate.
grep -q 'DS-DKR-01' "$root/DOCUMENT_REGISTRY.md"
grep -q 'DKR.01' "$root/CURRENT_STATE.md"
grep -q 'DKR.02' "$root/curriculum/devops/docker/PROGRESS.md"
grep -q 'published-canonical' "$root/curriculum/devops/docker/coverage-matrix.md"
grep -q 'Authoring eligibility' "$root/meta/standards/PROGRESSION_AND_PREREQUISITES.md"
grep -q 'Learner mastery' "$root/meta/standards/PROGRESSION_AND_PREREQUISITES.md"
# Git workflow must remain explicit and recoverable in a fresh session.
grep -q 'branch پیش‌فرض و canonical پروژه: `main`' "$root/meta/standards/GIT_WORKFLOW.md"
grep -q 'branch جدا نساز' "$root/meta/standards/GIT_WORKFLOW.md"
grep -q 'Pull Request نساز' "$root/meta/standards/GIT_WORKFLOW.md"
echo 'Deep Study repository contract: PASS'
