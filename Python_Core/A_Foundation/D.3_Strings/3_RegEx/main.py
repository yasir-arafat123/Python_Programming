"""
Topic: 03_Strings & Text
Subtopic: RegEx
Description: Regex basics with re module.

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
import re
def demo():
    m = re.search(r"(\w+)@(\w+)", "email:user@domain")
    if m: print("user:", m.group(1), "domain:", m.group(2))
    print(re.sub(r"\d+", "#", "a1b22c333"))
if __name__ == "__main__":
    demo()
