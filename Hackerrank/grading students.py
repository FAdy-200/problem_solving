from math import *

n, x = int(input()), []

for i in range(n):
    x.append(int(input()))

for i in range(n):
    y = (ceil(x[i] / 5)) * 5
    if y >= 40 and y-x[i] < 3:
        x[i] = y

for i in x:
    print(i)




















