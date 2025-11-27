"""
Topic: 09_Dev Skills & Quality
Subtopic: Property-based testing (Hypothesis) (optional)
Description: unittest skeleton.

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
import unittest
def add(a,b): return a+b
class T(unittest.TestCase):
    def test_add(self): self.assertEqual(add(2,3),5)
if __name__ == "__main__":
    unittest.main(argv=["-v"], exit=False)
