"""
Topic: 10_Advanced (Optional)
Subtopic: functools & caching (lru_cache, partial)
Description: lru_cache, partial, singledispatch.

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
from functools import lru_cache, partial, singledispatch
@lru_cache(maxsize=None)
def fib(n:int)->int:
    return n if n<2 else fib(n-1)+fib(n-2)
@singledispatch
def show(x): print("obj:", x)
@show.register
def _(x:int): print("int:", x)
def demo():
    print(fib(10))
    show(42); show("hi")
    add5 = partial(lambda a,b: a+b, 5); print(add5(3))
if __name__ == "__main__":
    demo()
