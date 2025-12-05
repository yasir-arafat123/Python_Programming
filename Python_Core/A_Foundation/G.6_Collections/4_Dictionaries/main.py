"""
Topic: 06_Collections & Iteration
Subtopic: Dictionaries
Description: Dict methods and views.

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
    d={"a":1}; d.setdefault("b",0); d.update({"c":2})
    print(d.get("x", -1), list(d.items()))
if __name__ == "__main__":
    demo()
