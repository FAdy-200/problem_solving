# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

from USEFUL_CODES.LC import *


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, h = 0, len(nums) - 1
        ans = 0
        while l <= h:
            if nums[l] + nums[h] <= target:
                # THIS IS 10 TIMES FASTER THAN (2**x)%MOD https://www.scaler.com/topics/pow-in-python/
                ans += pow(2, h - l, 10 ** 9 + 7)
                l += 1
            else:
                h -= 1
        return ans % (10 ** 9 + 7)


S = Solution()
with open("1498.txt", "r") as inp:
    p1 = eval(inp.readline())
    p2 = eval(inp.readline())
X = S.numSubseq([14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14], 22)
print(X)
