# https://leetcode.com/problems/smallest-number-in-infinite-set/
from typing import *

import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.n = [i for i in range(1, 1001)]
        heapq.heapify(self.n)
        self.s = set(self.n)

    def popSmallest(self) -> int:
        temp = heapq.heappop(self.n)
        self.s.remove(temp)
        return temp

    def addBack(self, num: int) -> None:
        if num in self.s:
            return
        else:
            self.s.add(num)
            heapq.heappush(self.n, num)



x = [i for i in range(1,1001)]
# x.append(1)
heapq.heapify(x)
print(x)
