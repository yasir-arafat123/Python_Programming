"""
Topic: 07_Object-Oriented Programming
Subtopic: Polymorphism
Description: Duck typing and protocols idea.

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
def area(shape) -> float:
    return shape.area()
class Circle:
    def __init__(self,r): self.r=r
    def area(self): import math; return math.pi*self.r*self.r
def demo():
    print(area(Circle(2)))
if __name__ == "__main__":
    demo()
