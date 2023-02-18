# https://www.hackerrank.com/challenges/stockmax/problem
o = open("testCases.txt", "r")
import sys

sys.setrecursionlimit(10000)


def maximizeProfit(x, i, n, paid):
    if i == len(x):
        return 0

    if ans.get((i + 1, 0, 0)) is not None:
        a = ans.get((i + 1, 0, 0))
    else:
        ans[(i + 1, 0, 0)] = maximizeProfit(x, i + 1, 0, 0)
        a = ans[(i + 1, 0, 0)]

    if ans.get((i + 1, n + 1, paid + x[i])) is not None:
        b = ans.get((i + 1, n + 1, paid + x[i]))
    else:
        ans[(i + 1, n + 1, paid + x[i])] = maximizeProfit(x, i + 1, n + 1, paid + x[i])
        b = ans[(i + 1, n + 1, paid + x[i])]

    if ans.get((i + 1, n, paid)) is not None:
        c = ans.get((i + 1, n, paid))
    else:
        ans[(i + 1, n, paid)] = maximizeProfit(x, i + 1, n, paid)
        c = ans[(i + 1, n, paid)]
    return max(n * x[i] + a - paid, b, c)


for _ in range(int(input())):
    # n = int(o.readline())
    # x = list(map(int, o.readline().split()))
    x = [i for i in range(1, 51)]
    x += [i for i in range(1, 51)]
    ans = dict()
    print(50 * 49 - sum(range(1, 50)))
    print(maximizeProfit(x, 0, 0, 0))
# 3
# 3
# 5 3 2
# 3
# 1 2 100
# 4
# 1 3 1 2
