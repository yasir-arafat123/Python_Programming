"""
Topic: 08_Files & Data
Subtopic: File I/O (open/read/write)
Description: Open/read/write safely with with.

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
    with open("example.txt","w",encoding="utf-8") as f:
        f.write("hello\n")
    with open("example.txt","r",encoding="utf-8") as f:
        print(f.read().strip())
if __name__ == "__main__":
    demo()
