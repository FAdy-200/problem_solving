# https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75
from USEFUL_CODES.LC import *


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, big: int) -> int:
            if not node:
                return 0
            ans = 0
            ma = big
            if node.val >= big:
                ans += 1
                ma = node.val
            ans += dfs(node.left, ma)
            ans += dfs(node.right, ma)
            return ans

        return dfs(root, root.val - 1)

S = Solution()
tree = create_tree([3,1,4,3,null,1,5])
X = S.goodNodes(tree)
print(X)

