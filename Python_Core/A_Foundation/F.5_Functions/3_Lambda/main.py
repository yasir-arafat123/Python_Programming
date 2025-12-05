"""
Topic: 05_Functions & Scope
Subtopic: Lambda
Description: Lambda expressions.

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
    items=[("a",3),("b",1),("c",2)]
    print(sorted(items, key=lambda t: t[1]))
if __name__ == "__main__":
    demo()
