# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem?h_r=internal-search
# from collections import deque
# import sys
# sys.setrecursionlimit(10000)
op = open("testCases.txt", "r+")


class Node:
    def __init__(self):
        self.visited = False
        self.value = 0
        self.parent = None


n = int(op.readline())
m = int(op.readline())
x = [[None] * (m + 2)]
for i in range(n):
    a = op.readline().split()
    z = [Node() if j == "1" else None for j in a]
    z.insert(0, None)
    z.append(None)
    x.append(z)
x.append([None] * (m + 2))


def BFS(x):
    ans = 0
    z = [-1, 0, 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i][j] is None:
                continue
            if x[i][j].visited:
                continue
            ma = 0
            q = deque()
            x[i][j].visited = True
            q.append((i, j))
            while len(q) != 0:
                ni, nj = q.popleft()
                ma += 1
                for ii in z:
                    for jj in z:
                        if ii == jj == 0:
                            continue
                        if x[ni + ii][nj + jj] is None:
                            continue
                        if x[ni + ii][nj + jj].visited:
                            continue
                        x[ni + ii][nj + jj].visited = True
                        q.append((ni + ii, nj + jj))

            if ma > ans:
                ans = ma
    return ans


print(BFS(x))
# import random
# op.write("10\n100\n")
# for i in range(10):
#     for j in range(100):
#         op.write(str(random.randint(0,1))+" ")
#     op.write("\n")
#
#