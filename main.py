#!/usr/bin/env python3
"""Sum up 23 November 2026's world news in one image.

The entry image (entry.png, a newspaper front page drawn in this
session: COP31 collapse as the lead, plus Ukraine, the Middle East,
Indonesia, the US, markets and Mexico) is copied to /output/entry.png.

Standard library only, no network; running twice writes the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(dst, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))


if __name__ == "__main__":
    main()
