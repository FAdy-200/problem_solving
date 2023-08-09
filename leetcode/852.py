# https://leetcode.com/problems/peak-index-in-a-mountain-array/
from USEFUL_CODES.LC import *


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, h = 1, n - 2
        while l < h:
            mid = (l + h) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                l = mid
                break
            if arr[mid - 1] > arr[mid] > arr[mid + 1]:
                h = mid
            else:
                l = mid + 1
        return l


S = Solution()
X = S.peakIndexInMountainArray([0,10,50,2])
print(X)
