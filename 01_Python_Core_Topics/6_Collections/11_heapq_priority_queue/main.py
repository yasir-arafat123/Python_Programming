"""
Topic: 06_Collections & Iteration
Subtopic: heapq (priority queue)
Description: Min-heap, nlargest/nsmallest.

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
import heapq
def demo():
    h=[]; [heapq.heappush(h, x) for x in [5,1,3]]
    print(heapq.heappop(h), heapq.nsmallest(2, [5,1,3,2]))
if __name__ == "__main__":
    demo()
