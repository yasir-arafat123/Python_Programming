"""
Topic: 07_Object-Oriented Programming
Subtopic: Classes & Objects
Description: Classes, __init__, __repr__.

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
class Point:
    def __init__(self,x:int,y:int): self.x,self.y=x,y
    def __repr__(self): return f"Point({self.x},{self.y})"
def demo():
    print(Point(2,3))
if __name__ == "__main__":
    demo()
