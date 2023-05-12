import math

n = int(input())
x = []

for _ in range(n):
    x.append(int(input()))


def nawar(x):
    a = x[0]
    ma = -1
    for i in range(1, len(x)):
        if x[i] < a:
            a = x[i]
        elif x[i] - a > ma and x[i]:
            ma = x[i] - a
    return ma if ma > 0 else -1


print(nawar(x))
