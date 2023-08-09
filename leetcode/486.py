# https://leetcode.com/problems/predict-the-winner/description/
from USEFUL_CODES.LC import *

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        su = sum(nums)
        @cache
        def dp(i:int,j:int, t:int) -> int:
            if i > j:
                return 0
            if i == j:
                return nums[i]
            if t:
                return max(dp(i+1,j,0) + nums[i], dp(i,j-1,0) + nums[j])
            return min(dp(i+1,j,1), dp(i,j-1,1))
        return dp(0,len(nums)-1,1) >= su/2
`