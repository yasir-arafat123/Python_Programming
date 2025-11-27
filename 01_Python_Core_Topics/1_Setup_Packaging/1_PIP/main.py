"""
Topic: 01_Setup & Packaging
Subtopic: PIP
Description: Using pip and requirements files.

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
    print("Typical commands (run in shell):")
    print("  python -m pip install -U pip")
    print("  pip install -r requirements.txt")
    print("  pip freeze > requirements.txt")
    print("  pip install -e .   # editable local project")
if __name__ == "__main__":
    demo()
