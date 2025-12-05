"""
Topic: 05_Functions & Scope
Subtopic: Scope & Namespaces
Description: LEGB, global, nonlocal, closures.

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
def make_adder(delta: int):
    def add(x: int) -> int:
        return x + delta
    return add
def demo():
    add5 = make_adder(5)
    print(add5(10))
if __name__ == "__main__":
    demo()
