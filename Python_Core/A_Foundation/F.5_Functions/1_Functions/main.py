"""
Topic: 05_Functions & Scope
Subtopic: Functions
Description: Function defs, returns, annotations, defaults.

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
def add(a: int, b: int = 0) -> int:
    return a + b
def demo():
    print(add(2,3), add(5))
if __name__ == "__main__":
    demo()
