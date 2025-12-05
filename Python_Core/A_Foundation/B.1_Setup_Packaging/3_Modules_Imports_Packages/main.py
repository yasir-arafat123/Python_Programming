"""
Topic: 01_Setup & Packaging
Subtopic: Modules (Imports & Packages)
Description: Python imports & packages.

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
    import importlib, sys
    print("sys.path entries:", sys.path[:3], "...")
    print("Relative imports require a package context.")
    if __name__ == "__main__":
        print("__main__ guard active.")
if __name__ == "__main__":
    demo()
