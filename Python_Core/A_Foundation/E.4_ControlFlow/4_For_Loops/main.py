"""
Topic: 04_Control Flow
Subtopic: For Loops
Description: For loops, enumerate, zip.

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
    items=["a","b","c"]
    for i,x in enumerate(items): print(i,x)
    for a,b in zip([1,2],[3,4]): print(a,b)
if __name__ == "__main__":
    demo()
