# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
from USEFUL_CODES.LC import *


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n,m = len(nums1),len(nums2)

        ans = []
        seen = set()

        h = [(nums1[0] + nums2[0], (0, 0))]
        seen.add((0, 0))
        k = min(k,n*m)
        while k:
            val, (i, j) = heapq.heappop(h)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < n and (i + 1, j) not in seen:
                heapq.heappush(h, (nums1[i + 1] + nums2[j], (i + 1, j)))
                seen.add((i + 1, j))

            if j + 1 < m and (i, j + 1) not in seen:
                heapq.heappush(h, (nums1[i] + nums2[j + 1], (i, j + 1)))
                seen.add((i, j + 1))
            k = k - 1

        return ans

S = Solution()
X = S.kSmallestPairs([1, 1, 2], [1, 2, 3], 10)
print(X)
