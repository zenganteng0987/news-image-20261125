#!/usr/bin/env python3
"""news-image-20261125 entrypoint.

Copies the rendered front page (entry.png) to the output directory.
Python 3 standard library only, no network access.

The image is THE DAILY ATLAS, a one-page newspaper summing up
Wednesday 25 November 2026 in 32 stories: 15 illustrated main cards
plus an ALSO list, a THE DAY IN UTC chronology strip, a BY THE NUMBERS
strip and a DATE CHECK strip naming stories deliberately left out
because they happened before 25 November.
"""

import hashlib
import os
import shutil
import struct
import sys

EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1048576


def png_size(path):
    """Read the width and height from a PNG file's IHDR chunk."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if header[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def sha256_hex(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else os.getcwd()
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    if size > MAX_BYTES:
        print(
            "entry.png is %d bytes, over the 1 MiB limit" % size,
            file=sys.stderr,
        )
        return 1
    width, height = png_size(dst)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        print(
            "entry.png is %dx%d, expected %dx%d"
            % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT),
            file=sys.stderr,
        )
        return 1
    print("entry.png sha256: %s" % sha256_hex(dst))
    print("entry.png: %dx%d" % (width, height))
    return 0


if __name__ == "__main__":
    sys.exit(main())
