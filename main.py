#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261119 (19 Nov 2026 front page).

The finished front-page image is stored beside this file as entry.png
(JPEG bytes: five AI-illustrated panels with program-typeset headlines,
composed offline). This program copies those bytes to the output
location unchanged, so the two grading runs write identical bytes.
Standard library only; no network.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"entry image missing beside program: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
