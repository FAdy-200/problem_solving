# https://leetcode.com/problems/maximum-product-subarray/
from typing import *


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result_max = min_prod = max_prod = nums[0]
        for x in nums[1:]:
            if x < 0:
                min_prod, max_prod = max_prod, min_prod
            max_prod = max(x, x * max_prod)
            min_prod = min(x, x * min_prod)
            result_max = max(result_max, max_prod)
        return result_max


s = Solution()
x = s.maxProduct([0, 2])
print(x)
