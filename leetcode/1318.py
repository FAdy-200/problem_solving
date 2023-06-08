# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            if c >> i & 1:
                if not (a >> i & 1 or b >> i & 1):
                    ans += 1
            else:
                if a >> i & 1:
                    ans += 1
                if b >> i & 1:
                    ans += 1
        return ans


S = Solution()
X = S.minFlips(4, 2, 7)
print(X)
