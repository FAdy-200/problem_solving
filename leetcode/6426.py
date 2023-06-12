from USEFUL_CODES.LC import *


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        """
        collision don't matter think of them passing through each other and switching places
        :param nums:
        :param s:
        :param d:
        :return:
        """
        n = len(nums)
        mod = 10**9+7
        pos = []
        for i in range(n):
            if s[i] == "R":
                pos.append(nums[i]+d)
            else:
                pos.append(nums[i]-d)
        pos.sort()
        ans = pre = 0
        for i in range(n):
            pre+=pos[i]
            ans += (i+1)*pos[i]-pre
            ans %= mod
        return ans
S = Solution()
X = S.sumDistance(nums = [-2,0,2], s = "RLL", d = 3)
print(X)
