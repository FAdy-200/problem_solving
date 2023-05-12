#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
import itertools

c = []
for i in range(int(input())):
    c.append(int(input()))
n = int(input())
d = list(itertools.combinations(c, 2))
ans = 0
i = 0
while i < len(d):
    if abs(d[i][0]-d[i][1]) >= n:
        c.remove(d[i][0])
        c.remove(d[i][1])
        d = list(itertools.combinations(c, 2))
        ans += 1
        i = 0
    i += 1
print(ans)



