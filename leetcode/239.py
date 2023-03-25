# https://leetcode.com/problems/sliding-window-maximum/
from typing import *
import heapq
import bisect
from collections import deque

class Solution:
    def helper(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append((nums[i], i))
        return ans

    def bisect_method(self, nums: List[int], k: int) -> List[int]:
        ans = []
        nums = self.helper(nums)
        n_nums = list(sorted(nums[:k], key=lambda x: x[0]))
        for i in range(len(nums) - k):
            ans.append(n_nums[-1][0])
            j = bisect.bisect_left(n_nums, nums[i + k])
            te = [nums[i + k]]
            while j < len(n_nums):
                te.append(n_nums[j])
                j += 1

            n_nums = te
            z = bisect.bisect_left(n_nums, nums[i])
            if n_nums[z][1] == i:
                n_nums.pop(z)

        ans.append(n_nums[-1][0])
        return ans



    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        helper = deque()
        ans = []

        for i in range(len(nums)):
            while helper and helper[0] <= i - k:
                helper.popleft()
            while helper and nums[helper[-1]] < nums[i]:
                helper.pop()
            helper.append(i)

            if i >= k - 1:
                ans.append(nums[helper[0]])
        return ans


S = Solution()
# X = S.maxSlidingWindow(
f = open("test239", "r")
t = eval(f.read())
t = [1,3,-1,-3,5,3,6,7]
# t = [-6, -10, -7, -1, -9, 9, -8, -4, 10, -5, 2, 9, 0, -7, 7, 4, -2, -10, 8, 7]
# X = S.bisect_method(t, 50000)
Y = S.maxSlidingWindow(t, 3)
# print(X)
