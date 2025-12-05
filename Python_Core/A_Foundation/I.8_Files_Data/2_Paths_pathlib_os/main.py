"""
Topic: 08_Files & Data
Subtopic: Paths (pathlib, os)
Description: pathlib for path ops.

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
from pathlib import Path
def demo():
    p=Path("."); print([str(x) for x in p.iterdir()][:3])
if __name__ == "__main__":
    demo()
