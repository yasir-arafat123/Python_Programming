"""
Topic: 06_Collections & Iteration
Subtopic: bisect (binary search)
Description: bisect for binary search on lists.

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
import bisect
def demo():
    a=[1,2,4,4,5]
    print(bisect.bisect_left(a,4), bisect.bisect_right(a,4))
    bisect.insort_left(a,3); print(a)
if __name__ == "__main__":
    demo()
