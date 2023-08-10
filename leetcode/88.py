# https://leetcode.com/problems/merge-sorted-array
from USEFUL_CODES.LC import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        for _ in range(n):
            nums1.pop()
        while len(nums1) != m + n:
            if i >= len(nums1):
                nums1.append(nums2[j])
                j+=1
            elif nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                j += 1
            else:
                i += 1


S = Solution()
S.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
