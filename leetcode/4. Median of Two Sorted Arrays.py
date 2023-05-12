# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import *


class Solution:
    def searchInsert(self, nums: List[int], target: int, priority) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low <= high:
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            elif target == nums[mid]:
                if priority:
                    low = mid + 1
                else:
                    high = mid - 1
            mid = (low + high) // 2
        return mid + 1

    def search(self, nums1, nums2, ind, p):
        low = 0
        high = len(nums1) - 1
        mid = (low + high) // 2
        while low <= high:
            temp = mid + self.searchInsert(nums2, nums1[mid], p)
            if temp > ind:
                high = mid - 1
            elif temp < ind:
                low = mid + 1
            elif temp == ind:
                return nums1[mid]
            mid = (low + high) // 2
        return None

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        needed = []

        med = []
        needed.append(n // 2)
        if n % 2 == 0:
            needed.append(n // 2 - 1)
        needed1 = needed[:]
        for i in needed:
            temp = self.search(nums1, nums2, i, True)
            if temp is not None:
                med.append(temp)
        for j in med:
            needed1.remove(j)
        for i in needed1:
            temp = self.search(nums2, nums1, i, False)
            if temp is not None:
                med.append(temp)
        return sum(med) / len(med)


x = Solution()
print(x.findMedianSortedArrays([], [2, 3]))
