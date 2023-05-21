# https://leetcode.com/problems/shortest-bridge/
from typing import *
from collections import deque,defaultdict


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island1s = set()
        island1e = set()
        n = len(grid)

        def bfs1(lm: int, lk: int, s: set, e: set):
            q = deque()
            q.append((lm, lk))
            s.add((lm, lk))
            while q:
                node = q.popleft()
                for ti in range(-1, 2):
                    for tj in range(-1, 2):
                        if ti == tj or (ti != 0 and tj != 0):
                            continue
                        if n > node[0] + ti >= 0 and n > node[1] + tj >= 0:
                            if grid[node[0] + ti][node[1] + tj]:
                                if not (node[0] + ti, node[1] + tj) in s:
                                    q.append((node[0] + ti, node[1] + tj))
                                    s.add((node[0] + ti, node[1] + tj))
                            else:
                                if not (node[0] + ti, node[1] + tj) in e:
                                    e.add((node[0] + ti, node[1] + tj))

        def bfs2(s: set, e: set,visited:DefaultDict[tuple,int|float]) -> int | float:
            orig = deque()
            for ti in e:
                orig.append(ti)
                visited[ti] = 1

            ans = float("inf")
            while orig:
                node = orig.popleft()
                ti = -1
                while ti < 2:
                    for tj in range(-1, 2):
                        if ti == tj or (ti != 0 and tj != 0):
                            continue
                        if n > node[0] + ti >= 0 and n > node[1] + tj >= 0:
                            x = (node[0] + ti, node[1] + tj)
                            if grid[x[0]][x[1]]:
                                if not x in s:
                                    ans = min(ans, visited[node[:2]])
                            else:
                                if not x in e:
                                    orig.append(x)
                                    e.add(x)
                                tz = min(visited[x],visited[node[:2]]+1)
                                visited[x] = tz

                    ti += 1
            return ans

        for i, j in enumerate(grid):
            for m, k in enumerate(j):
                if k:
                    bfs1(i, m, island1s, island1e)
                    return bfs2(island1s, island1e, defaultdict(lambda: float("inf")))




S = Solution()
X = S.shortestBridge([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,1,1,1,1,0,0,1,0,0],[1,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,1,0],[1,0,1,1,1,1,1,1,1,0],[1,1,0,1,1,1,1,1,1,1]])
print(X)
