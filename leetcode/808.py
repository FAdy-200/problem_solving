# https://leetcode.com/problems/soup-servings/
from USEFUL_CODES.LC import *


class Solution:
    def soupServingsDP(self, n: int) -> float:
        branches = ((4, 0), (3, 1), (2, 2), (1, 3))
        n = ceil(n/25)
        @cache
        def dp(a: int, b: int) -> float:
            if not a and not b:
                return 0.5
            elif not a:
                return 1
            elif not b:
                return 0
            ans = 0
            for i, j in branches:
                n_a = a - i if a - i > 0 else 0
                n_b = b - j if b - j > 0 else 0
                ans += dp(n_a, n_b)
            return ans * 0.25
        for k in range(n):
            if dp(k,k) > 1 - 1e-5:
                return 1.0
        return dp(n, n)

    def soupServings(self, n: int) -> float:
        remain = n % 25
        n = n//25

        dp:DefaultDict[int,DefaultDict[int,float]] = defaultdict(lambda :defaultdict(float)) # a is x axis b is y axis
        dp[0][0] = 0.5
        branches = ((4, 0), (3, 1), (2, 2), (1, 3))
        for k in range(1, n + 2):
            dp[0][k] = 1
        for a in range(1, n+2):
            for b in range(1,n+2):
                for i,j in branches:
                    n_a = a - i if a - i > 0 else 0
                    n_b = b - j if b - j > 0 else 0
                    dp[a][b] += 0.25 * dp[n_a][n_b]
                dp[a][b] = float(f'{dp[a][b]:.6f}')
                if dp[a][b] > 1 - 1e-5:
                    return 1.0
            if a - 5 >= 0:
                n_a = a - 5
                if n_a in dp:
                    del dp[n_a]
                    # dp.pop(n_a)
        return dp[n+1][n+1] if remain else dp[n][n]



S = Solution()
X = S.soupServings(100023)
print(X)