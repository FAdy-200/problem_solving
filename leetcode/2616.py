# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
from USEFUL_CODES.LC import *


class Solution:
    def minimizeMaxMem(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        @cache
        def dp(i: int, l_p: int) -> int:
            if not l_p:
                return 0
            if i >= n - 1:
                return inf
            t1 = dp(i + 1, l_p)
            t2 = dp(i + 2, l_p - 1)
            t3 = abs(nums[i] - nums[i + 1])
            return min(t1, max(t2, t3))

        return dp(0, p)

    def minimizeMaxTable(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        dp = [[0] * (n + 2)]

        for i in range(1, p + 1):
            dp.append([0] * (n + 2 - 2 * i))
            dp[-1][-1] = inf
            gg = 2*(p-i)
            for j in range(n - 2 - (i - 1) * 2, -1 + gg, -1):
                t1 = dp[i][j + 1]
                t2 = dp[i - 1][j + 2]
                if (x:=nums[j] - nums[j + 1]) > t2:
                    if x < 0:
                        t2 = -x
                    t2 = -x
                if t2 < t1:
                    t1 = t2
                dp[i][j] = t1
            if i > 1:
                dp[i - 2] = []
        return min(dp[-1])
    def minimizeMax(self,nums:List[int],p:int):
        nums.sort()
        n = len(nums)
        temp = [abs(nums[i] - nums[i+1]) for i in range(n-1)]
        l, h = 0, nums[-1] - nums[0]
        def count_(val:int):
            i = 0
            l_ans = 0
            while i < n-1:
                if temp[i] <= val:
                    i+=1
                    l_ans+=1
                i+=1
            return l_ans

        while l < h:
            mid = (l+h) // 2
            if (z:=count_(mid)) < p:
                l = mid + 1
            else:
                h = mid
        return l
with open("2616.txt", "r") as inp:
    p1 = eval(inp.readline())
    p2 = eval(inp.readline())
S = Solution()
X = S.minimizeMax(p1,p2)
print(X)
