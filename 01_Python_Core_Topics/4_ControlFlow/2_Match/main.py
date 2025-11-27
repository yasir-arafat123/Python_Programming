"""
Topic: 04_Control Flow
Subtopic: Match
Description: Structural pattern matching.

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
def describe(token):
    match token:
        case ("point", x, y): return f"Point({x},{y})"
        case int() as n if n>0: return "positive int"
        case int(): return "non-positive int"
        case _: return "unknown"
def demo():
    print(describe(("point",2,3)))
    print(describe(5))
if __name__ == "__main__":
    demo()
