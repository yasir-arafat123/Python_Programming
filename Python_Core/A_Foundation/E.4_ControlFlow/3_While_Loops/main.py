"""
Topic: 04_Control Flow
Subtopic: While Loops
Description: While loop patterns.

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
    i=0; acc=0
    while i<5:
        acc+=i; i+=1
    else:
        print("done, acc=", acc)
if __name__ == "__main__":
    demo()
