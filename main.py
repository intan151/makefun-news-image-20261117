#!/usr/bin/env python3
"""make.fun news-image-20261117 entrypoint (Python 3.13, standard library only).

Copies the entry.png shipped beside this file into the output directory
($MAKEFUN_OUTPUT_DIR, default /output) as entry.png.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    sys.exit(main())
