# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq
from typing import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newNums = [-i for i in nums]
        heapq.heapify(newNums)
        for _ in range(k - 1):
            heapq.heappop(newNums)
        return -heapq.heappop(newNums)
