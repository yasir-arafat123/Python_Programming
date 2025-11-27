"""
Topic: 03_Strings & Text
Subtopic: Strings
Description: String basics: slicing, methods.

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
    s="  hello,world  "
    print(s.strip().split(","))
    print(s[2:7], s[::-1])
    print("endswith?", "abcxyz".endswith("xyz"))
if __name__ == "__main__":
    demo()
