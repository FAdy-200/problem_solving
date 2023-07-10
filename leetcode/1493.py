# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
from USEFUL_CODES.LC import *


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window = [0, 0]
        ans = 0
        l_k = 1
        while window[-1] < len(nums):
            if nums[window[-1]]:
                window[-1] += 1
            elif l_k:
                window[-1] += 1
                l_k -= 1
            else:
                while nums[window[0]]:
                    window[0] += 1
                    if window[0] > window[1]:
                        window[1] += 1
                window[0] += 1
                if window[0] > window[1]:
                    window[1] += 1
                l_k = 1

            ans = ans if ans > (z := window[1] - window[0]) else z

        return ans - 1
