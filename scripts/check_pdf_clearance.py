#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

PT_PER_MM = 72.0 / 25.4


def local_name(tag: str) -> str:
    return tag.rsplit('}', 1)[-1]


def main() -> int:
    parser = argparse.ArgumentParser(description='Check effective main-content distance from the PDF page border.')
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--min-mm', type=float, default=20.0, help='Minimum real content-to-border gap in every direction.')
    parser.add_argument('--footer-exclude-mm', type=float, default=15.0, help='Bottom margin area reserved for footer and excluded from main-content checks.')
    args = parser.parse_args()

    if not args.pdf.is_file():
        print(f'ERROR: PDF not found: {args.pdf}', file=sys.stderr)
        return 2

    try:
        xml_text = subprocess.check_output(
            ['pdftotext', '-bbox-layout', str(args.pdf), '-'],
            text=True,
            stderr=subprocess.STDOUT,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f'ERROR: pdftotext bbox extraction failed: {exc}', file=sys.stderr)
        return 2

    root = ET.fromstring(xml_text)
    min_pt = args.min_mm * PT_PER_MM
    footer_exclude_pt = args.footer_exclude_mm * PT_PER_MM

    global_min = {'left': float('inf'), 'right': float('inf'), 'top': float('inf'), 'bottom': float('inf')}
    failures: list[str] = []
    page_count = 0

    for page_count, page in enumerate((e for e in root.iter() if local_name(e.tag) == 'page'), start=1):
        width = float(page.attrib['width'])
        height = float(page.attrib['height'])
        page_min = {'left': float('inf'), 'right': float('inf'), 'top': float('inf'), 'bottom': float('inf')}
        found_main_content = False

        for word in page.iter():
            if local_name(word.tag) != 'word':
                continue
            text = ''.join(word.itertext()).strip()
            if not text:
                continue
            x_min = float(word.attrib['xMin'])
            y_min = float(word.attrib['yMin'])
            x_max = float(word.attrib['xMax'])
            y_max = float(word.attrib['yMax'])

            # Footer is deliberately placed in the page margin and is not part of the main content area.
            if y_min >= height - footer_exclude_pt:
                continue

            found_main_content = True
            distances = {
                'left': x_min,
                'right': width - x_max,
                'top': y_min,
                'bottom': height - y_max,
            }
            for side, value in distances.items():
                page_min[side] = min(page_min[side], value)
                global_min[side] = min(global_min[side], value)

        if not found_main_content:
            continue

        bad = {side: value for side, value in page_min.items() if value < min_pt}
        if bad:
            details = ', '.join(f'{side}={value / PT_PER_MM:.2f}mm' for side, value in bad.items())
            failures.append(f'page {page_count}: {details}')

    if page_count == 0:
        print('ERROR: no PDF pages found in bbox output', file=sys.stderr)
        return 2

    print('Effective main-content clearance:')
    for side in ('left', 'right', 'top', 'bottom'):
        value = global_min[side]
        print(f'  {side}: {value / PT_PER_MM:.2f}mm')

    if failures:
        print(f'ERROR: clearance must be at least {args.min_mm:.2f}mm on every side.', file=sys.stderr)
        for failure in failures[:30]:
            print(f'  {failure}', file=sys.stderr)
        if len(failures) > 30:
            print(f'  ... and {len(failures) - 30} more pages', file=sys.stderr)
        return 1

    print(f'PASS: every page keeps at least {args.min_mm:.2f}mm effective main-content clearance.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
