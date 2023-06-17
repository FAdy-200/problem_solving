# https://leetcode.com/problems/make-array-strictly-increasing/
from USEFUL_CODES.LC import *


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        m, n = len(arr1), len(arr2)

        if m == 1:
            return 0
        arr2.sort()

        @cache
        def dp(last, i) -> int:
            if i < 0:
                return 0
            lans = inf
            if arr1[i] < last:
                lans = min(lans, dp(arr1[i], i - 1))
            temp = bisect.bisect_left(arr2, last) - 1
            if temp >= 0:
                lans = min(lans, dp(arr2[temp], i - 1) + 1)

            temp = bisect.bisect_left(arr2, arr1[i])
            if temp != n:
                if arr2[temp] == arr1[i] and temp != n - 1:
                    if arr2[temp + 1] < last:
                        lans = min(lans, dp(arr1[i], i - 1) + 1)
                elif arr2[temp] != arr1[i]:
                    if arr2[temp] < last:
                        lans = min(lans, dp(arr1[i], i - 1) + 1)
            return lans

        if (ans := dp(arr1[-1], m - 2)) != inf:
            return ans
        if (ans := dp(arr2[-1], m - 2)) != inf:
            return ans + 1
        return -1


setrecursionlimit(8000)
S = Solution()
X = S.makeArrayIncreasing([random.randint(1,10**9) for _ in range(random.randint(1,2000))],
                          [random.randint(1,10**9) for _ in range(random.randint(1,2000))])
print(X)
