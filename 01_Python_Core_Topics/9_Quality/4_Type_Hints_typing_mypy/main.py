"""
Topic: 09_Dev Skills & Quality
Subtopic: Type Hints (typing, mypy)
Description: typing basics.

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
from typing import Optional, Union, TypedDict, Protocol
class P(Protocol):
    def run(self) -> int: ...
class Config(TypedDict):
    host: str
    port: int
def f(x: Optional[int]) -> int:
    return 0 if x is None else x+1
def demo():
    print(f(5), f(None))
if __name__ == "__main__":
    demo()
