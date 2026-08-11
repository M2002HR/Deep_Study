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
    parser = argparse.ArgumentParser(
        description='Check effective main-content clearance from page edges and, when configured, from an independent page frame.'
    )
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--min-mm', type=float, default=20.0, help='Minimum real main-content clearance from every paper edge.')
    parser.add_argument('--frame-inset-mm', type=float, default=None, help='Distance of the decorative frame from each paper edge.')
    parser.add_argument('--min-frame-gap-mm', type=float, default=14.0, help='Minimum real gap between main content and the decorative frame.')
    parser.add_argument('--footer-exclude-mm', type=float, default=15.0, help='Bottom area reserved for the footer and excluded from main-content checks.')
    args = parser.parse_args()

    if not args.pdf.is_file():
        print(f'ERROR: PDF not found: {args.pdf}', file=sys.stderr)
        return 2
    if args.frame_inset_mm is not None and args.frame_inset_mm < 0:
        print('ERROR: --frame-inset-mm must be non-negative.', file=sys.stderr)
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
    frame_inset_pt = None if args.frame_inset_mm is None else args.frame_inset_mm * PT_PER_MM
    min_frame_gap_pt = args.min_frame_gap_mm * PT_PER_MM

    global_min = {'left': float('inf'), 'right': float('inf'), 'top': float('inf'), 'bottom': float('inf')}
    edge_failures: list[str] = []
    frame_failures: list[str] = []
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

            # Footer lives in the bottom page margin and is not part of the main content area.
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

        bad_edges = {side: value for side, value in page_min.items() if value < min_pt}
        if bad_edges:
            details = ', '.join(f'{side}={value / PT_PER_MM:.2f}mm' for side, value in bad_edges.items())
            edge_failures.append(f'page {page_count}: {details}')

        if frame_inset_pt is not None:
            bad_frame = {
                side: value - frame_inset_pt
                for side, value in page_min.items()
                if value - frame_inset_pt < min_frame_gap_pt
            }
            if bad_frame:
                details = ', '.join(f'{side}={value / PT_PER_MM:.2f}mm' for side, value in bad_frame.items())
                frame_failures.append(f'page {page_count}: {details}')

    if page_count == 0:
        print('ERROR: no PDF pages found in bbox output', file=sys.stderr)
        return 2

    print('Effective main-content clearance from paper edges:')
    for side in ('left', 'right', 'top', 'bottom'):
        value = global_min[side]
        print(f'  {side}: {value / PT_PER_MM:.2f}mm')

    if frame_inset_pt is not None:
        print(f'Decorative frame inset: {args.frame_inset_mm:.2f}mm from every paper edge')
        print('Effective main-content gap from decorative frame:')
        for side in ('left', 'right', 'top', 'bottom'):
            value = global_min[side] - frame_inset_pt
            print(f'  {side}: {value / PT_PER_MM:.2f}mm')

    if edge_failures or frame_failures:
        if edge_failures:
            print(f'ERROR: paper-edge clearance must be at least {args.min_mm:.2f}mm on every side.', file=sys.stderr)
            for failure in edge_failures[:30]:
                print(f'  {failure}', file=sys.stderr)
        if frame_failures:
            print(f'ERROR: content-to-frame gap must be at least {args.min_frame_gap_mm:.2f}mm on every side.', file=sys.stderr)
            for failure in frame_failures[:30]:
                print(f'  {failure}', file=sys.stderr)
        return 1

    print(f'PASS: every page keeps at least {args.min_mm:.2f}mm main-content clearance from the paper edges.')
    if frame_inset_pt is not None:
        print(f'PASS: every page keeps at least {args.min_frame_gap_mm:.2f}mm main-content gap from the decorative frame.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
