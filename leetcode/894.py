# https://leetcode.com/problems/all-possible-full-binary-trees/
from USEFUL_CODES.LC import *


class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n % 2:
            return []
        if n == 1:
            return [TreeNode(0)]
        ans = []
        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)
            for l in left:
                for r in right:
                    ans.append(TreeNode(0,l,r))
        return ans


S = Solution()
X = S.allPossibleFBT(19)
print(X)
