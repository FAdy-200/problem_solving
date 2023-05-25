# https://leetcode.com/problems/sliding-window-median/
from typing import List
import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = [0]
        to_check = [k//2]
        if not k%2:
            to_check.append(to_check[-1]-1)
        wind = list(sorted(nums[:k]))
        for j in to_check:
            ans[-1] += wind[j]
        ans[-1] = ans[-1] / len(to_check)
        for i in range(len(nums) - k):
            wind.pop(bisect.bisect_left(wind, nums[i]))
            bisect.insort(wind,nums[k+i])
            ans.append(0)
            for j in to_check:
                ans[-1] += wind[j]
            ans[-1] = ans[-1]/len(to_check)
        return ans

S = Solution()
with open("480.txt","r") as inp:
    nums = eval(inp.readline())
    k = eval(inp.readline())
X = S.medianSlidingWindow(nums,k)
print(X)