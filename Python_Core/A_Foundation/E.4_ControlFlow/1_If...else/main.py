"""
Topic: 04_Control Flow
Subtopic: If…else
Description: If/elif/else and ternary.

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
def classify(x: int) -> str:
    return "even" if x % 2 == 0 else "odd"
def demo():
    for i in range(3): print(i, "->", classify(i))
if __name__ == "__main__":
    demo()
