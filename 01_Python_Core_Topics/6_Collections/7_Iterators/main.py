"""
Topic: 06_Collections & Iteration
Subtopic: Iterators
Description: Iterator protocol and custom iterator.

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
class Countdown:
    def __init__(self,n): self.n=n
    def __iter__(self): return self
    def __next__(self):
        if self.n<=0: raise StopIteration
        self.n-=1; return self.n+1
def demo():
    for x in Countdown(3): print(x)
if __name__ == "__main__":
    demo()
