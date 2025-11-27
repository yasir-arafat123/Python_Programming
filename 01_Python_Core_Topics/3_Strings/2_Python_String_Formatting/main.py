"""
Topic: 03_Strings & Text
Subtopic: Python String Formatting
Description: f-strings, str.format, % formatting.

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
    name, pi = "Ada", 3.14159
    print(f"{name} -> {pi:.2f}")
    print("{n} -> {p:.3f}".format(n=name, p=pi))
    print("%s -> %.1f" % (name, pi))
if __name__ == "__main__":
    demo()
