from typing import *
from collections import *
from functools import *
from heapq import *
import bisect
import random
from .GraphFunctions import *
from .LinkedList import *
from .Trie import *
from .BiTree import *
from math import *
from sys import setrecursionlimit

inf = float("inf")

to_exclude = ['pow','dist']

for name in to_exclude:
    del globals()[name]
