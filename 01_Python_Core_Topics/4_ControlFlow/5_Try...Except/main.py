"""
Topic: 04_Control Flow
Subtopic: Try…Except
Description: Exceptions: try/except/else/finally.

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
def safe_int(x: str) -> int | None:
    try:
        return int(x)
    except ValueError:
        return None
    finally:
        pass
def demo():
    print(safe_int("42"), safe_int("x"))
if __name__ == "__main__":
    demo()
