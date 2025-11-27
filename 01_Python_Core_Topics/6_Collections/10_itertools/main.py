"""
Topic: 06_Collections & Iteration
Subtopic: itertools
Description: itertools utilities.

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
import itertools as it
def demo():
    print(list(it.accumulate([1,2,3])))
    print(list(it.product([1,2],["a","b"])))
    print(list(it.permutations([1,2,3], 2)))
if __name__ == "__main__":
    demo()
