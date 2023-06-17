# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
from USEFUL_CODES.LC import *


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ma, p = [root.val, 1], 1
        d = deque()
        d.append((root, 1))
        temp = 0
        while d:
            node, lev = d.popleft()
            if lev != p:
                if temp > ma[0]:
                    ma = [temp, p]
                temp = 0
                p = lev
            temp += node.val
            if node.left is not None:
                d.append((node.left, lev + 1))
            if node.right is not None:
                d.append((node.right, lev + 1))
        # if last level is the answer
        if temp > ma[0]:
            ma = [temp, p]
        return ma[1]

S = Solution()
X = S.maxLevelSum(create_tree([1,2,3]))
print(X)
