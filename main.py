#!/usr/bin/env python3
"""Entrypoint for news-image-20261125 V2. Python 3 standard library only.

Copies entry.png from this same directory to the output directory and
checks the result: a whole PNG, 1024x1024, under 1 MiB. Prints the
sha256 of the written file. Exits 0 when the checks pass, 1 otherwise.
"""
import hashlib
import os
import shutil
import sys
import zlib

MAX_BYTES = 1048576
WANT_W, WANT_H = 1024, 1024
PNG_SIG = b"\x89PNG\r\n\x1a\n"


def output_dir():
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    return os.getcwd()


def check_png(path):
    """Return (width, height) or raise ValueError on a bad PNG."""
    with open(path, "rb") as f:
        data = f.read()
    if len(data) < 8 or data[:8] != PNG_SIG:
        raise ValueError("not a PNG file")
    if len(data) > MAX_BYTES:
        raise ValueError("file is %d bytes, over the 1 MiB limit" % len(data))
    pos = 8
    seen_iend = False
    width = height = None
    while pos + 8 <= len(data):
        length = int.from_bytes(data[pos:pos + 4], "big")
        ctype = data[pos + 4:pos + 8]
        end = pos + 8 + length + 4
        if end > len(data):
            raise ValueError("truncated PNG chunk")
        chunk = data[pos + 4:end - 4]
        crc = int.from_bytes(data[end - 4:end], "big")
        if zlib.crc32(chunk) & 0xFFFFFFFF != crc:
            raise ValueError("bad CRC in chunk %r" % ctype)
        if ctype == b"IHDR":
            width = int.from_bytes(data[pos + 8:pos + 12], "big")
            height = int.from_bytes(data[pos + 12:pos + 16], "big")
        if ctype == b"IEND":
            seen_iend = True
            break
        pos = end
    if width is None or height is None:
        raise ValueError("PNG has no IHDR chunk")
    if not seen_iend:
        raise ValueError("PNG has no IEND chunk")
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    shutil.copyfile(src, dst)
    try:
        width, height = check_png(dst)
    except (OSError, ValueError) as e:
        print("error: output failed PNG check: %s" % e, file=sys.stderr)
        return 1
    if (width, height) != (WANT_W, WANT_H):
        print("error: expected 1024x1024, got %dx%d" % (width, height),
              file=sys.stderr)
        return 1
    size = os.path.getsize(dst)
    with open(dst, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    print("entry.png: %dx%d, %d bytes, sha256 %s" % (width, height, size,
                                                     digest))
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
