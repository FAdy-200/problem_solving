# https://leetcode.com/problems/top-k-frequent-elements/
from collections import defaultdict
from heapq import nlargest
from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)
        for i in nums:
            freq[i] += 1
        return list(list(zip(*nlargest(k, freq.items(), key=lambda x: x[1])))[0])
