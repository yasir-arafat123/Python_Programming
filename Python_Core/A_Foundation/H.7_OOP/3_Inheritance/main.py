"""
Topic: 07_Object-Oriented Programming
Subtopic: Inheritance
Description: Inheritance and super().

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
class Animal:
    def speak(self): return "noise"
class Dog(Animal):
    def speak(self): return super().speak() + " woof"
def demo():
    print(Dog().speak())
if __name__ == "__main__":
    demo()
