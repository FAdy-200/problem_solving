# https://leetcode.com/problems/find-k-closest-elements/
from typing import *
from collections import deque


class Solution:
    @staticmethod
    def findClosestElements(arr: List[int], k: int, x: int) -> List[int] | deque[int]:
        sub_arr = deque(arr[:k])
        i = k
        while i < len(arr) and (abs(arr[i] - x) < abs(sub_arr[0] - x) or arr[i] == sub_arr[0]):
            sub_arr.append(arr[i])
            sub_arr.popleft()
            i += 1
        return sub_arr


S = Solution()
X = S.findClosestElements([1, 2, 3, 4, 5], 4, 4)
print(X)
