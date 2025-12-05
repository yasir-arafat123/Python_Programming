"""
Topic: 08_Files & Data
Subtopic: JSON
Description: json dump/load.

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
import json
def demo():
    data={"a":1,"b":[2,3]}
    s=json.dumps(data, indent=2)
    print(s)
    print(json.loads(s)["b"])
if __name__ == "__main__":
    demo()
