#!/usr/bin/env python3
"""Small CSV generator that will later become an asynchronous worker."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

SAFE_ID = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_-]{0,79}$")


def generate_report(report_id: str, report_name: str, output_dir: str | Path) -> Path:
    """Generate one deterministic demo report and return its path."""
    report_id = report_id.strip()
    report_name = report_name.strip()
    if not SAFE_ID.fullmatch(report_id):
        raise ValueError("report_id contains unsupported characters")
    if not report_name or len(report_name) > 80:
        raise ValueError("report_name must contain 1 to 80 characters")

    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    destination = directory / f"{report_id}.csv"
    temporary = destination.with_suffix(".csv.tmp")

    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["report", "total"])
        writer.writerow([report_name, "42"])
    temporary.replace(destination)
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate one demo CSV report")
    parser.add_argument("--report-id", required=True)
    parser.add_argument("--report-name", required=True)
    parser.add_argument("--output-dir", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    path = generate_report(args.report_id, args.report_name, args.output_dir)
    print(path)


if __name__ == "__main__":
    main()
