"""
Topic: 06_Collections & Iteration
Subtopic: Arrays (optional)
Description: array module & memoryview.

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
import array
def demo():
    a=array.array("i",[1,2,3]); mv=memoryview(a)
    print(a.tolist(), mv.tolist())
if __name__ == "__main__":
    demo()
