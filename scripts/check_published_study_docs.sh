#!/usr/bin/env bash
set -euo pipefail

root="${1:-.}"
registry="$root/DOCUMENT_REGISTRY.md"

test -s "$registry" || { echo "missing registry: $registry" >&2; exit 1; }

trim_field() {
  local value="$1"
  value="${value#${value%%[![:space:]]*}}"
  value="${value%${value##*[![:space:]]}}"
  value="${value//\`/}"
  printf '%s' "$value"
}

count=0
while IFS= read -r line; do
  [[ "$line" == \|* ]] || continue
  IFS='|' read -r _ doc_id curriculum_id track title version status source pdf _rest <<< "$line"
  doc_id="$(trim_field "${doc_id:-}")"
  version="$(trim_field "${version:-}")"
  status="$(trim_field "${status:-}")"
  source="$(trim_field "${source:-}")"
  pdf="$(trim_field "${pdf:-}")"

  [[ "$status" == "published-canonical" ]] || continue
  [[ "$doc_id" == DS-* ]] || continue

  count=$((count + 1))
  echo "Validating published study document: $doc_id v$version"

  test -s "$root/$source" || { echo "missing canonical source: $source" >&2; exit 1; }
  test -s "$root/$pdf" || { echo "missing canonical PDF: $pdf" >&2; exit 1; }

  doc_dir="$(dirname "$source")"
  manifest="$root/$doc_dir/artifact-manifest.yml"
  qa="$root/$doc_dir/QA_REPORT_v${version}.md"
  document_meta="$root/$doc_dir/document.yml"

  test -s "$manifest" || { echo "missing artifact manifest: $manifest" >&2; exit 1; }
  test -s "$qa" || { echo "missing QA report: $qa" >&2; exit 1; }
  test -s "$document_meta" || { echo "missing document metadata: $document_meta" >&2; exit 1; }

  expected_sha=$(awk -F': *' '$1=="pdf_sha256" {print $2}' "$manifest")
  expected_pages=$(awk -F': *' '$1=="page_count" {print $2}' "$manifest")
  manifest_doc_id=$(awk -F': *' '$1=="document_id" {print $2}' "$manifest")
  manifest_version=$(awk -F': *' '$1=="version" {print $2}' "$manifest")

  test -n "$expected_sha"; test -n "$expected_pages"
  test "$manifest_doc_id" = "$doc_id"
  test "$manifest_version" = "$version"
  grep -q '^status: published-canonical$' "$manifest"
  grep -q '^  status: PASS$' "$manifest"

  actual_sha=$(sha256sum "$root/$pdf" | awk '{print $1}')
  actual_pages=$(pdfinfo "$root/$pdf" | awk '/^Pages:/ {print $2}')
  test "$actual_sha" = "$expected_sha"
  test "$actual_pages" = "$expected_pages"

  "$root/scripts/check_pdf_fonts.sh" "$root/$pdf"
  python "$root/scripts/check_pdf_clearance.py" "$root/$pdf" --min-mm 20 --frame-inset-mm 5 --min-frame-gap-mm 14

  tmp_txt=$(mktemp)
  trap 'rm -f "$tmp_txt"' RETURN
  pdftotext "$root/$pdf" "$tmp_txt"
  ! grep -q $'\uFFFD' "$tmp_txt"
  rm -f "$tmp_txt"
  trap - RETURN

done < "$registry"

test "$count" -gt 0 || { echo 'no published-canonical study documents found in registry' >&2; exit 1; }
echo "Published study document contract: PASS ($count document(s))"
