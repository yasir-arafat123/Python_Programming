"""
Topic: 03_Strings & Text
Subtopic: Unicode & encoding (bytes ↔ str)
Description: Encoding/decoding between str and bytes.

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
def demo():
    s = "π"
    b = s.encode("utf-8")
    print(s, b, b.decode("utf-8"))
if __name__ == "__main__":
    demo()
