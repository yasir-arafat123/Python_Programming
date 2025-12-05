"""
Topic: 09_Dev Skills & Quality
Subtopic: Logging
Description: Basic logging config.

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
import logging
def demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
    logging.info("hello")
if __name__ == "__main__":
    demo()
