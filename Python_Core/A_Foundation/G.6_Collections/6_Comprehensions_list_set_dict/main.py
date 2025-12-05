"""
Topic: 06_Collections & Iteration
Subtopic: Comprehensions (list/set/dict)
Description: List/set/dict comprehensions.

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
    print([x*x for x in range(5) if x%2==0])
    print({x for x in range(5)})
    print({x: x*x for x in range(3)})
if __name__ == "__main__":
    demo()
