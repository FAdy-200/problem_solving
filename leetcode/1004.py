# https://leetcode.com/problems/max-consecutive-ones-iii
from USEFUL_CODES.LC import *


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window = [0, 0]
        ans = 0
        l_k = k
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
                l_k += 1
                l_k = k if l_k>k else l_k
            ans = ans if ans > (z := window[1] - window[0]) else z

        return ans


S = Solution()
X = S.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
print(X)
