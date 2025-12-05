"""
Topic: 06_Collections & Iteration
Subtopic: Sets
Description: Set ops and membership.

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
    s={1,2,3}; s.add(2); s.add(4)
    print(s, {1,2} | {2,3}, {1,2,3} & {2,3,4})
if __name__ == "__main__":
    demo()
