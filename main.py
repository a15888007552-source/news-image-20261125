"""news-image-20261125 entry: copy the bundled image to /output/entry.png.

Runs with no network and writes the same bytes on every run.
Local run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The grader sets /output; MAKEFUN_OUTPUT_DIR only stands in for local runs.
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"

OUT.parent.mkdir(parents=True, exist_ok=True)
# Copy, never redraw: the bundled image is the entry, byte for byte.
shutil.copyfile(HERE / "entry.png", OUT)
