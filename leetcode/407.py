# https://leetcode.com/problems/trapping-rain-water-ii/description/
from USEFUL_CODES.LC import *


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        hp = []
        seen = set()
        for i, val in enumerate(heightMap[-1]):
            heapq.heappush(hp, (val, m - 1, i))
            seen.add((m - 1, i))
        for i, val in enumerate(heightMap[0]):
            heapq.heappush(hp, (val, 0, i))
            seen.add((0, i))
        for i, row in enumerate(heightMap[1:m - 1]):
            heapq.heappush(hp, (row[0], i + 1, 0))
            seen.add((i + 1, 0))
            heapq.heappush(hp, (row[n - 1], i + 1, n - 1))
            seen.add((i + 1, n - 1))
        ans = 0
        lv = 1
        while hp:
            node = heapq.heappop(hp)
            lv = max(lv, node[0])
            if node[0] < lv:
                ans += lv - node[0]
            for x, y in (
                    (node[1] + 1, node[2]), (node[1], node[2] + 1), (node[1] - 1, node[2]), (node[1], node[2] - 1)):
                if m > x >= 0 and n > y >= 0 and (x, y) not in seen:
                    heapq.heappush(hp, (heightMap[x][y], x, y))
                    seen.add((x, y))
        return ans


S = Solution()
X = S.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]])
print(X)
