"""
Topic: 05_Functions & Scope
Subtopic: *args & **kwargs
Description: *args and **kwargs usage.

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
def f(a, *args, **kwargs):
    print("a=", a, "args=", args, "kwargs=", kwargs)
def demo():
    f(1,2,3, x=4, y=5)
if __name__ == "__main__":
    demo()
