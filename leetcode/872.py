# https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75
from USEFUL_CODES.LC import *


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: TreeNode) -> str:
            if not root.left and not root.right:
                return f"{root.val},"
            ans = ""
            if root.left:
                ans += dfs(root.left)
            if root.right:
                ans += dfs(root.right)
            return ans

        return dfs(root1) == dfs(root2)


S = Solution()
t1 = create_tree([3, 5, 1, 6, 2, 9, 8, null, null, 7, 4])
t2 = create_tree([3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8])
X = S.leafSimilar(t1, t2)
print(X)
