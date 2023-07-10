# https://leetcode.com/problems/total-cost-to-hire-k-workers/
from USEFUL_CODES.LC import *


class Cost:
    def __init__(self, val, ind):
        self.val = val
        self.ind = ind

    def __lt__(self, other):
        if self.val == other.val:
            return self.ind < other.ind
        return self.val < other.val

    def __gt__(self, other):
        if self.val == other.val:
            return self.ind > other.ind
        return self.val > other.val

    def __str__(self):
        return f"val: {self.val}, ind: {self.ind}"

    def __repr__(self):
        return self.__str__()


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        hp: List[Cost] = []
        for i, j in enumerate(costs):
            if i < candidates or i > len(costs) - candidates - 1:
                heapq.heappush(hp, Cost(j, i))

        if len(hp) == len(costs):
            l = len(costs)
            h = 0
        else:
            l = candidates
            h = len(costs) - candidates - 1

        ans = 0
        for _ in range(k):
            worker = heapq.heappop(hp)
            if l <= h:
                if worker.ind < l:
                    heapq.heappush(hp, Cost(costs[l], l))
                    l += 1
                elif worker.ind > h:
                    heapq.heappush(hp, Cost(costs[h], h))
                    h -= 1

            ans += worker.val

        return ans


S = Solution()
X = S.totalCost([1, 2, 4, 1], 3, 3)
print(X)
