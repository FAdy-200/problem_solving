# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/
from USEFUL_CODES.LC import *


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        d: DefaultDict[int, int] = defaultdict(int)
        n = len(requests)

        def count_(x: int):
            return bin(x).count("1")

        def backtrack(i: int, z: int) -> int:
            if i == n:
                for val in d.values():
                    if val:
                        return -1
                return count_(z)
            ans = 0
            for j in range(i, n):
                d[requests[j][0]] -= 1
                d[requests[j][1]] += 1
                temp = z
                temp |= 1 << j
                if (x := backtrack(j + 1, temp)) != -1:
                    if x > ans:
                        ans = x
                d[requests[j][1]] -= 1
                d[requests[j][0]] += 1

            for val in d.values():
                if val:
                    return ans
            cz = count_(z)
            return ans if ans > cz else cz

        return backtrack(0, 0)


S = Solution()
X = S.maximumRequests(n=3, requests=[[1, 2], [1, 2], [2, 2], [0, 2], [2, 1], [1, 1], [1, 2]])
print(X)
