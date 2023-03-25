# https://leetcode.com/problems/next-greater-element-i/
from typing import *


class Solution:
    def find(self, arr, ele):
        for i, j in enumerate(arr):
            if j == ele:
                return i+1
        return 0

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                z = stack.pop()
                if t := self.find(nums1, nums2[z]):
                    ans[t-1] = nums2[i]
            stack.append(i)

        return ans


S = Solution()
x = S.nextGreaterElement([2,4], [1,2,3,4])
print(x)
