"""
Topic: 09_Dev Skills & Quality
Subtopic: Debugging (pdb)
Description: pdb/breakpoint usage.

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
def buggy(x):
    # breakpoint()  # uncomment to step into debugger
    return x + 1
def demo():
    print(buggy(41))
if __name__ == "__main__":
    demo()
