#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261121.

Copies the front-page image this repository holds to the output path the
grader reads. Standard library only, no network, no randomness: running it
twice writes the same bytes twice.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The image this repository holds is the whole deliverable; the program
# only places a byte-identical copy where the grader reads it.
SRC = os.path.join(HERE, "entry.png")
if not os.path.isfile(SRC):
    raise SystemExit("entry.png missing from the repository")
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
