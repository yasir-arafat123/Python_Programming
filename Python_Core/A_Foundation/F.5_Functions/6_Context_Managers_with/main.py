"""
Topic: 05_Functions & Scope
Subtopic: Context Managers & with
Description: Context managers and contextlib.

TODO:
- Read the README.md in this folder.
- Run this file to see examples, then extend experiments.
"""
from __future__ import annotations
from typing import *
import sys, os, math, json, re, pathlib, itertools, collections, functools, logging, datetime
# Optional third-party (uncomment if installed)
# import numpy as np
# import pandas as pd
from contextlib import contextmanager
@contextmanager
def open_read(path: str):
    f = open(path, "w", encoding="utf-8")
    try:
        yield f
    finally:
        f.close()
def demo():
    with open_read("demo.txt") as f:
        f.write("hello")
    print("wrote demo.txt")
if __name__ == "__main__":
    demo()
