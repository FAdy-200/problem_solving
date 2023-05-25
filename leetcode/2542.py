# https://leetcode.com/problems/maximum-subsequence-score/
from typing import *
from collections import deque
import bisect
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = list(sorted(zip(nums1,nums2),reverse=True))
        ans = 0
        temp = 0
        mi = deque()
        def comp(x):
            return x[1]
        for i, j in enumerate(pairs[:k]):
            temp += j[0]
            bisect.insort(mi,j, key = comp)

        for i in range(len(pairs) - k):
            sm = mi.popleft()
            ans = max(ans, temp * sm[1])
            temp += pairs[k + i][0]
            bisect.insort(mi, pairs[k + i], key=comp)
            temp-=sm[0]
        sm = mi.popleft()
        ans = max(ans, temp * sm[1])
        return ans



S = Solution()
with open("2542.txt","r") as inp:
    nums1 = eval(inp.readline())
    nums2 = eval(inp.readline())
    k = eval(inp.readline())
X = S.maxScore(nums1, nums2, k)
print(X)
