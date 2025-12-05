"""
Topic: 05_Functions & Scope
Subtopic: Decorators
Description: Writing decorators; functools.wraps.

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
import functools
def timing(fn):
    @functools.wraps(fn)
    def wrapper(*a, **k):
        import time; t0=time.perf_counter()
        r=fn(*a, **k)
        print(f"{fn.__name__} took {time.perf_counter()-t0:.6f}s")
        return r
    return wrapper
@timing
def work(n: int): return sum(range(n))
def demo():
    print(work(1000000))
if __name__ == "__main__":
    demo()
