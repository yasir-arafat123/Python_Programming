"""
Topic: 07_Object-Oriented Programming
Subtopic: Dunder Methods & dataclasses
Description: Dunder methods and @dataclass.

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
from dataclasses import dataclass
@dataclass(order=True, frozen=True)
class Card:
    rank: int
    suit: str
def demo():
    print(Card(10,"H")<Card(11,"S"))
if __name__ == "__main__":
    demo()
