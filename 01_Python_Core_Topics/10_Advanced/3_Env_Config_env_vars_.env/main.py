"""
Topic: 10_Advanced (Optional)
Subtopic: Env & Config (env vars, .env)
Description: Environment variables and config.

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
import os, configparser
def demo():
    os.environ.setdefault("APP_ENV","dev")
    print("APP_ENV:", os.environ["APP_ENV"])
    cfg=configparser.ConfigParser(); cfg["app"]={"env":"dev"}; print(cfg["app"]["env"])
if __name__ == "__main__":
    demo()
