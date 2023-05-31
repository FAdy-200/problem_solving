# https://leetcode.com/problems/continuous-subarray-sum/
from typing import *
from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map:DefaultDict[int,Optional[int]] = defaultdict(lambda: None)
        hash_map[0] = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if hash_map[s % k] is None:
                hash_map[s % k] = i + 1
            elif hash_map[s % k] < i:
                return True
        return False


S = Solution()
X = S.checkSubarraySum([23, 2, 4, 6, 6], 7)
print(X)
