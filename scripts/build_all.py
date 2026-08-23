#!/usr/bin/env python3
"""Run validation and all build steps."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS = [
    "validate.py",
    "build_markdown.py",
    "build_json.py",
    "build_anki.py",
    "build_cheatsheet.py",
    "build_task_coverage.py",
]


def main() -> int:
    scripts_dir = Path(__file__).resolve().parent
    for name in SCRIPTS:
        path = scripts_dir / name
        print(f"\n=== {name} ===")
        result = subprocess.run([sys.executable, str(path)], check=False)
        if result.returncode != 0:
            return result.returncode
    print("\nAll builds completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
