#!/usr/bin/env bash
set -euo pipefail
pdf=${1:?usage: check_pdf_fonts.sh file.pdf}
out=$(pdffonts "$pdf")
echo "$out"
if ! printf '%s\n' "$out" | grep -qi 'Vazirmatn'; then
  echo 'ERROR: Vazirmatn is not present in PDF font table.' >&2
  exit 1
fi
if printf '%s\n' "$out" | awk 'NR>2 && $6 != "yes" {bad=1} END{exit !bad}'; then
  echo 'ERROR: at least one PDF font is not embedded.' >&2
  exit 1
fi
echo 'PASS: Vazirmatn present and reported fonts are embedded.'
