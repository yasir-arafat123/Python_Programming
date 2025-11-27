"""
Topic: 10_Advanced (Optional)
Subtopic: Concurrency (threading, multiprocessing, asyncio)
Description: threading, multiprocessing, asyncio skeletons.

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
import threading, asyncio, time
def worker(n):
    s=sum(range(n))
    print("thread done:", s)
async def coro():
    await asyncio.sleep(0.1); print("async done")
def demo():
    t=threading.Thread(target=worker, args=(1000000,)); t.start(); t.join()
    asyncio.run(coro())
if __name__ == "__main__":
    demo()
