# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        k = total // cost1
        for i in range(k + 1):
            temp = (total - i * cost1) // cost2 + 1
            ans += temp
        return ans


S = Solution()
X = S.waysToBuyPensPencils(total = 5, cost1 = 10, cost2 = 10)
print(X)
