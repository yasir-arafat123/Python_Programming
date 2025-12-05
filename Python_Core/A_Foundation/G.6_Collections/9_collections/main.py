"""
Topic: 06_Collections & Iteration
Subtopic: collections
Description: collections module: Counter/defaultdict/deque/etc.

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
from collections import Counter, defaultdict, deque, ChainMap, OrderedDict
def demo():
    print(Counter("banana"))
    d=defaultdict(int); d["x"]+=1; print(d)
    dq=deque([1,2,3]); dq.appendleft(0); print(dq)
    print(ChainMap({"a":1},{"a":2}))
    od=OrderedDict([("a",1),("b",2)]); od.move_to_end("a"); print(od)
if __name__ == "__main__":
    demo()
